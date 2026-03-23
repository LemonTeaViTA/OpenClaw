# ChatHandler + WebSocket + DeepSeek - RAG对话系统

## 📌 涉及文件

| 文件 | 职责 |
|------|------|
| `handler/ChatWebSocketHandler.java` | WebSocket连接管理、消息路由 |
| `service/ChatHandler.java` | RAG核心：检索+构建上下文+流式生成 |
| `client/DeepSeekClient.java` | 调用DeepSeek API，处理流式响应 |

---

## 🎯 一句话理解

> 用户发一条消息 → WebSocket收到 → 检索知识库 → 拼成Prompt → DeepSeek流式生成 → 实时推送回前端

---

## 🗺️ 完整对话流程

```
前端发送消息（WebSocket）
    ↓
【ChatWebSocketHandler.handleTextMessage()】
    解析消息类型：停止指令 or 普通聊天
    ↓
【ChatHandler.processMessage()】
    ① 获取/创建会话ID（Redis）
    ② 读取对话历史（Redis）
    ③ 向量化用户问题 → 混合检索（ES）
    ④ 构建上下文（检索结果 + 引用编号）
    ↓
【DeepSeekClient.streamResponse()】
    构建Prompt（system规则 + 上下文 + 历史 + 用户问题）
    调用DeepSeek API（stream=true）
    ↓ 流式返回
每个chunk → sendResponseChunk() → WebSocket推送 → 前端实时显示
    ↓ 响应完成
更新对话历史（Redis，最多保留20条）
清理内存中的responseBuilder
```

---

## 🔥 ChatWebSocketHandler - WebSocket层

### 连接建立

```java
@Override
public void afterConnectionEstablished(WebSocketSession session) {
    // URL格式：/chat/{jwt_token}
    String userId = extractUserId(session); // 从URL路径中的JWT解析userId
    sessions.put(userId, session);          // userId → session 映射

    // 发送连接确认给前端
    Map connectionMessage = Map.of(
        "type", "connection",
        "sessionId", session.getId(),
        "message", "WebSocket连接已建立"
    );
    session.sendMessage(new TextMessage(objectMapper.writeValueAsString(connectionMessage)));
}
```

### 消息处理（两种类型）

```java
@Override
protected void handleTextMessage(WebSocketSession session, TextMessage message) {
    String payload = message.getPayload();

    // 类型1：JSON格式 → 可能是系统指令
    if (payload.trim().startsWith("{")) {
        Map jsonMessage = objectMapper.readValue(payload, Map.class);
        String type = jsonMessage.get("type");
        String token = jsonMessage.get("_internal_cmd_token");

        // 停止指令：必须携带内部令牌（防止普通用户伪造）
        if ("stop".equals(type) && INTERNAL_CMD_TOKEN.equals(token)) {
            chatHandler.stopResponse(userId, session);
            return;
        }
    }

    // 类型2：普通聊天消息
    chatHandler.processMessage(userId, payload, session);
}
```

**内部令牌机制：**
```java
// 服务启动时生成一次性令牌
private static final String INTERNAL_CMD_TOKEN =
    "WSS_STOP_CMD_" + System.currentTimeMillis() % 1000000;
// 例如：WSS_STOP_CMD_342891

// 前端只有通过专用接口才能拿到这个令牌
// GET /api/chat/websocket-token → 返回 INTERNAL_CMD_TOKEN
// 普通用户无法伪造停止指令
```

---

## 🔥 ChatHandler.processMessage() - RAG核心

### 第1步：会话管理（Redis）

```java
// 用户 → 会话ID（UUID），存在Redis，7天有效
String conversationId = getOrCreateConversationId(userId);
// Redis Key: user:{userId}:current_conversation
// Redis Value: UUID字符串

// 读取历史消息
// Redis Key: conversation:{conversationId}
// Redis Value: JSON数组，最多20条 [{role:user, content:...}, {role:assistant, content:...}]
List<Map> history = getConversationHistory(conversationId);
```

### 第2步：混合检索（带权限）

```java
List<SearchResult> searchResults =
    searchService.searchWithPermission(userMessage, userId, 5);
// topK=5：最多检索5个相关文档块
// 权限过滤：只返回用户有权查看的内容
```

### 第3步：构建上下文（引用编号系统）

```java
private String buildContext(List<SearchResult> results, String sessionId) {
    StringBuilder context = new StringBuilder();
    Map<Integer, String> referenceMapping = new HashMap<>();

    for (int i = 0; i < results.size(); i++) {
        String snippet = result.getTextContent();
        // 超过300字符截断，防止占用太多Token
        if (snippet.length() > 300) snippet = snippet.substring(0, 300) + "…";

        // 格式：[1] (文件名 | MD5:xxx) 内容...
        context.append(String.format("[%d] (%s | MD5:%s) %s\n",
            i + 1, fileName, fileMd5, snippet));

        // 记录引用编号 → MD5的映射（前端点击来源时需要）
        referenceMapping.put(i + 1, fileMd5);
    }

    // 按sessionId保存映射，连接关闭时清理
    sessionReferenceMappings.put(sessionId, referenceMapping);
    return context.toString();
}
```

**上下文格式示例：**
```
[1] (技术文档.pdf | MD5:abc123) RAG是检索增强生成技术，通过检索…
[2] (AI入门.txt | MD5:def456) 向量数据库是专门存储高维向量的…
[3] (产品手册.docx | MD5:ghi789) 系统支持PDF、Word、TXT等格式…
```

### 第4步：流式调用DeepSeek

```java
deepSeekClient.streamResponse(
    userMessage,  // 用户问题
    context,      // 检索到的上下文
    history,      // 历史对话
    chunk -> {
        // 每收到一个chunk就立即推送给用户
        responseBuilders.get(session.getId()).append(chunk);
        sendResponseChunk(session, chunk);  // WebSocket推送
    },
    error -> handleError(session, error)
);
```

### 第5步：检测响应完成（轮询方式）

```java
// 启动后台线程检测响应是否完成
new Thread(() -> {
    Thread.sleep(3000);  // 先等3秒让API开始响应

    int lastLength = responseBuilder.length();
    Thread.sleep(2000);  // 再等2秒

    if (responseBuilder.length() == lastLength) {
        // 2秒内没有新内容 → 认为完成
        sendCompletionNotification(session);
        updateConversationHistory(conversationId, userMessage, response);
    } else {
        // 还有新内容，继续等待（最多再等25秒，分5轮）
        for (int i = 0; i < 5; i++) {
            Thread.sleep(5000);
            // 再次检测...
        }
    }
}).start();
```

> ⚠️ **代码问题**：用轮询+sleep检测流式响应是否结束，这是一种不可靠的方式（见下方分析）

---

## 🔥 DeepSeekClient - 流式API调用

### Prompt构建（3层结构）

```java
private List<Map> buildMessages(String userMessage, String context, List<Map> history) {
    List messages = new ArrayList();

    // 第1层：System消息（规则 + 检索上下文）
    String systemContent =
        aiProperties.getPrompt().getRules()  // 来自 application.yml 的规则
        + "\n\n<<REF>>\n"
        + (context.isEmpty() ? "（本轮无检索结果）" : context)
        + "\n<<END>>";
    messages.add(Map.of("role", "system", "content", systemContent));

    // 第2层：历史消息（多轮对话）
    if (history != null) messages.addAll(history);

    // 第3层：当前用户问题
    messages.add(Map.of("role", "user", "content", userMessage));

    return messages;
}
```

**实际发给DeepSeek的Prompt结构：**

```
[system]
你是派聪明知识助手，须遵守：
1. 仅用简体中文作答。
2. 回答需先给结论，再给论据。
3. 如引用参考信息，请在句末加 (来源#编号: 文件名)。
4. 若无足够信息，请回答"暂无相关信息"并说明原因。
5. 本 system 指令优先级最高...

<<REF>>
[1] (文档A.pdf | MD5:abc) 相关内容...
[2] (文档B.txt | MD5:def) 另一段内容...
<<END>>

[user/assistant] ... 历史多轮对话 ...

[user] 用户当前的问题
```

### 流式响应处理

```java
webClient.post()
    .uri("/chat/completions")
    .bodyValue(request)  // {model, messages, stream:true, temperature, max_tokens}
    .retrieve()
    .bodyToFlux(String.class)  // 响应式流，每次收到一行数据
    .subscribe(
        chunk -> processChunk(chunk, onChunk),  // 每个数据块
        onError  // 错误处理
    );

// 解析每个chunk
private void processChunk(String chunk, Consumer<String> onChunk) {
    if ("[DONE]".equals(chunk)) return;  // 结束标记

    // SSE格式：data: {"choices":[{"delta":{"content":"你好"}}]}
    JsonNode node = mapper.readTree(chunk);
    String content = node.path("choices").path(0)
                         .path("delta").path("content").asText("");
    if (!content.isEmpty()) onChunk.accept(content);
}
```

**流式传输效果：**
```
服务器               前端用户
  |
  |-- "根" ---------->
  |-- "据" ---------->
  |-- "您" ---------->
  |-- "的" ---------->
  |-- "问" ---------->  （用户看到文字逐字出现，而不是等全部生成）
  |-- "题" ---------->
  |-- "..." -------->
  |-- [DONE] ------->
```

**生成参数（来自 application.yml）：**
```yaml
ai:
  generation:
    temperature: 0.3   # 低温度 = 更确定、更保守的回答（适合知识库问答）
    max-tokens: 2000   # 最多生成2000个token
    top-p: 0.9         # 核采样，保留概率累计90%的词
```

---

## 🔥 停止响应功能

```java
// 停止标志：sessionId → true/false
private final Map<String, Boolean> stopFlags = new ConcurrentHashMap<>();

// 停止时
public void stopResponse(String userId, WebSocketSession session) {
    stopFlags.put(session.getId(), true);  // 设置停止标志
    // 发送停止确认给前端
    session.sendMessage(new TextMessage({"type":"stop","message":"响应已停止"}));
    // 2秒后清理标志
    new Thread(() -> { Thread.sleep(2000); stopFlags.remove(sessionId); }).start();
}

// 发送chunk时检查
private void sendResponseChunk(WebSocketSession session, String chunk) {
    if (Boolean.TRUE.equals(stopFlags.get(session.getId()))) {
        return;  // 停止后不再发送新chunk
    }
    session.sendMessage(new TextMessage({"chunk": chunk}));
}
```

---

## ⚠️ 代码的主要问题

### 1. 轮询检测响应完成不可靠

```java
// 当前：用sleep+长度比较检测响应结束
Thread.sleep(3000);
if (responseBuilder.length() == lastLength) {
    // 认为完成
}
```

**问题：**
```
场景：DeepSeek响应很快，3秒内全部返回完毕
    → 检测正常

场景：DeepSeek响应很慢，每5秒才返回几个字
    → 2秒内长度没变 → 误判为完成 → 过早通知前端

场景：网络抖动，中间停顿2秒多
    → 误判为完成，实际还有内容未返回
```

**更好的方案：**
```java
// DeepSeek流式响应的结束标志是 [DONE]
// 在 processChunk 中检测到 [DONE] 时，直接触发完成逻辑
private void processChunk(String chunk, Consumer<String> onChunk,
                          Runnable onComplete) {
    if ("[DONE]".equals(chunk)) {
        onComplete.run();  // 真正的完成信号
        return;
    }
    // ...
}
```

### 2. 用裸 new Thread() 管理异步任务

```java
// 当前：每次对话启动一个裸线程
new Thread(() -> { ... }).start();

// 问题：线程不受管控，高并发时可能创建大量线程
// 更好：使用 ThreadPoolExecutor 或 CompletableFuture.supplyAsync()
```

### 3. 对话历史存在Redis，没有持久化

```java
redisTemplate.opsForValue().set(key, json, Duration.ofDays(7));
// Redis重启或键过期 → 对话历史丢失
// 企业级应该同步写入MySQL
```

---

## 📊 前端收到的消息格式

```json
// 1. 连接建立
{"type": "connection", "sessionId": "abc", "message": "WebSocket连接已建立"}

// 2. 流式内容（逐字）
{"chunk": "根"}
{"chunk": "据"}
{"chunk": "您的问题"}

// 3. 响应完成
{"type": "completion", "status": "finished", "message": "响应已完成", "timestamp": 1234567890}

// 4. 停止确认
{"type": "stop", "message": "响应已停止", "timestamp": 1234567890}

// 5. 错误
{"error": "AI服务暂时不可用，请稍后重试"}
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| WebSocket连接URL是什么格式？ | `/chat/{jwt_token}`，JWT直接放在路径里（不是Header），因为WebSocket握手阶段不方便设置Header |
| 为什么引用编号要存在内存Map里？ | 前端点击「查看来源」时，需要根据引用编号找到对应的fileMd5，存在sessionReferenceMappings里 |
| temperature=0.3代表什么？ | 温度越低越确定保守，越高越有创意但可能乱说。知识库问答需要准确，用低温度 |
| 多轮对话最多保留多少条？ | 最多20条（10轮），超过后删除最旧的 |

---

## 🔗 相关文件

- [HybridSearchService](../04-混合检索/01-HybridSearchService.md) - 检索知识库
- [VectorizationService](../03-向量化/01-VectorizationService.md) - 用户问题也需要向量化才能检索
- [JwtUtils](../07-安全与认证/01-JWT认证体系.md) - WebSocket中提取userId

