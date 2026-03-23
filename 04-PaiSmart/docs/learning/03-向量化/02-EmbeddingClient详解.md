# EmbeddingClient - 向量化API客户端

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/client/EmbeddingClient.java`
- **作用**：调用通义千问 text-embedding-v4 API，将文本转成向量

---

## 🎯 一句话理解

> EmbeddingClient = 应用和AI模型之间的「快递员」
> 把文本打包发给通义千问，再把返回的向量数组交给调用方

---

## ⚙️ 配置参数（来自 application.yml）

```yaml
embedding:
  api:
    url: https://dashscope.aliyuncs.com/compatible-mode/v1
    key: sk-xxxx           # 通义千问API Key
    model: text-embedding-v4
    batch-size: 10         # 每次最多发10条（API限制）
    dimension: 2048        # 向量维度
```

```java
@Value("${embedding.api.model}")
private String modelId;          // text-embedding-v4

@Value("${embedding.api.batch-size:100}")
private int batchSize;           // 实际是10（配置覆盖默认值）

@Value("${embedding.api.dimension:2048}")
private int dimension;           // 2048维
```

---

## 🔥 核心方法：embed() - 批量生成向量

```java
public List<float[]> embed(List<String> texts) {
    List<float[]> all = new ArrayList<>(texts.size());

    // 分批处理，每批最多 batchSize(=10) 条
    for (int start = 0; start < texts.size(); start += batchSize) {
        int end = Math.min(start + batchSize, texts.size());
        List<String> batch = texts.subList(start, end);

        // 调用一次API
        String response = callApiOnce(batch);

        // 解析响应，提取向量
        all.addAll(parseVectors(response));
    }

    return all;  // 所有文本对应的向量
}
```

**分批处理示意图：**

```
输入：25个文本

batch-size = 10

第1批：texts[0-9]   → 1次API请求 → vectors[0-9]
第2批：texts[10-19] → 1次API请求 → vectors[10-19]
第3批：texts[20-24] → 1次API请求 → vectors[20-24]

最终合并：all = vectors[0-24]
```

---

## 🔥 callApiOnce() - 发送HTTP请求

```java
private String callApiOnce(List<String> batch) {
    // 构建请求体
    Map<String, Object> requestBody = new HashMap<>();
    requestBody.put("model", modelId);           // text-embedding-v4
    requestBody.put("input", batch);             // 文本数组
    requestBody.put("dimension", dimension);     // 2048
    requestBody.put("encoding_format", "float"); // 返回浮点数

    return webClient.post()
        .uri("/embeddings")  // 完整: .../compatible-mode/v1/embeddings
        .bodyValue(requestBody)
        .retrieve()
        .bodyToMono(String.class)
        // 失败自动重试3次，每次间隔1秒
        .retryWhen(Retry.fixedDelay(3, Duration.ofSeconds(1))
            .filter(e -> e instanceof WebClientResponseException))
        .block(Duration.ofSeconds(30));  // 最多等30秒
}
```

**HTTP请求示例：**

```http
POST https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings
Authorization: Bearer sk-d047c088c9fe4fb68d1c9310dab3aca4
Content-Type: application/json

{
  "model": "text-embedding-v4",
  "input": [
    "人工智能是计算机科学的分支...",
    "机器学习是AI的核心技术..."
  ],
  "dimension": 2048,
  "encoding_format": "float"
}
```

**API响应示例：**

```json
{
  "data": [
    {
      "embedding": [0.12, -0.34, 0.89, 0.45, ...],
      "index": 0
    },
    {
      "embedding": [-0.56, 0.78, 0.12, -0.90, ...],
      "index": 1
    }
  ],
  "usage": { "total_tokens": 150 }
}
```

---

## 🔥 parseVectors() - 解析响应

```java
private List<float[]> parseVectors(String response) throws Exception {
    JsonNode jsonNode = objectMapper.readTree(response);
    JsonNode data = jsonNode.get("data");  // 取data数组

    List<float[]> vectors = new ArrayList<>();
    for (JsonNode item : data) {
        JsonNode embedding = item.get("embedding");

        // 把JSON数组转换成 float[]
        float[] vector = new float[embedding.size()];
        for (int i = 0; i < embedding.size(); i++) {
            vector[i] = (float) embedding.get(i).asDouble();
        }
        vectors.add(vector);
    }
    return vectors;
}
```

**数据转换过程：**

```
JSON字符串
"[0.12, -0.34, 0.89, ...]"
    ↓ objectMapper.readTree()
JsonNode数组
    ↓ 遍历 + asDouble() + 强转float
float[] {0.12f, -0.34f, 0.89f, ...}
```

---

## 🔑 关键技术点

### 1. 重试机制
```java
.retryWhen(Retry.fixedDelay(3, Duration.ofSeconds(1))
    .filter(e -> e instanceof WebClientResponseException))
```
- 失败最多重试3次
- 每次重试间隔1秒
- 只对HTTP错误重试（网络错误等）
- 防止API偶发性故障导致整个向量化失败

### 2. 超时控制
```java
.block(Duration.ofSeconds(30))
```
- 最多等待30秒
- 防止API响应慢导致线程一直阻塞

### 3. 为什么用WebClient而不是RestTemplate？
```
RestTemplate（同步）：
发送请求 → 阻塞等待 → 收到响应

WebClient（响应式）：
发送请求 → 继续其他工作 → 异步收到响应

这里用了.block()变成同步，但WebClient的
重试、超时等功能比RestTemplate更强大
```

### 4. 2048维向量的含义
```
每个文本块 → 一个2048维的向量

内存占用：2048 × 4字节(float) = 8KB

维度选择：
256维：速度快，精度低
512维：平衡
1024维：较高精度
2048维：最高精度（当前选择）

维度越高 = 语义表达越丰富 = 检索越准确
         = 存储空间越大 = 计算越慢
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 为什么batch-size配置是100但实际限制是10？ | application.yml中配置了batch-size: 10覆盖了代码默认值100，配置文件优先级更高 |
| 向量化失败了会重试整个文件吗？ | Kafka消费者抛出异常后会触发重试，但会重新下载文件、重新解析、重新向量化，代价较大 |
| 能换成其他向量模型吗？ | 可以，只需修改application.yml中的url、model、dimension即可 |

