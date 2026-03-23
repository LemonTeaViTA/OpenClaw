# VectorizationService - 文本向量化服务

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/service/VectorizationService.java`
- **代码行数**：102行（短小精悍）
- **触发时机**：Kafka消费者收到消息后，ParseService解析完成之后

---

## 🎯 一句话理解

> VectorizationService = 连接「文本世界」和「向量世界」的桥梁
> 把人能看懂的文字，变成机器能计算的数字数组

## ⚠️ 重要澄清：切分不在这里！

```
❌ 错误理解：VectorizationService 自己切分文本再向量化
✅ 正确理解：VectorizationService 直接读取 ParseService 已切好的分块

切分逻辑完全在 ParseService.java 里：
  段落（\n\n）→ 句子（。！？）→ HanLP分词（超长句子兜底）
  最终每块最大 512 字符（来自 application.yml: chunk-size: 512）

VectorizationService 只做一件事：
  MySQL里的文本块 → 通义千问API → 2048维向量 → Elasticsearch
```

---

## 🗺️ 在整体流程中的位置

```
文件上传 → 合并 → Kafka消息
                        ↓
              FileProcessingConsumer
                        ↓
              ① ParseService（解析+切分）
                    文字存入MySQL
                        ↓
              ② VectorizationService ← 当前文件
                    读MySQL → 调API → 存ES
                        ↓
              RAG检索可用
```

---

## 🏗️ 类的结构

```java
@Service
public class VectorizationService {

    // 依赖1：调用通义千问API生成向量
    @Autowired
    private EmbeddingClient embeddingClient;

    // 依赖2：批量存入Elasticsearch
    @Autowired
    private ElasticsearchService elasticsearchService;

    // 依赖3：从MySQL读取ParseService切好的文本
    @Autowired
    private DocumentVectorRepository documentVectorRepository;

    // 对外公开的主方法
    public void vectorize(String fileMd5, String userId,
                         String orgTag, boolean isPublic)

    // 内部私有方法
    private List<TextChunk> fetchTextChunks(String fileMd5)
}
```

---

## 🔥 主方法：vectorize() - 5个步骤

### 步骤1：接收4个参数

```java
public void vectorize(
    String fileMd5,    // 查询哪个文件的分块
    String userId,     // 权限：谁上传的
    String orgTag,     // 权限：属于哪个组织
    boolean isPublic   // 权限：所有人能搜到吗
)
```

**为什么要传权限参数？**
```
权限信息要跟着文档一起存入Elasticsearch！

私有文档存入ES时：
{ textContent: "机密财务数据", userId: "A", isPublic: false }

公开文档存入ES时：
{ textContent: "AI入门教程", userId: "B", isPublic: true }

检索时自动过滤：
用户C搜索 → ES只返回C有权限的文档
```

---

### 步骤2：从MySQL读取文本分块

```java
List<TextChunk> chunks = fetchTextChunks(fileMd5);

if (chunks == null || chunks.isEmpty()) {
    logger.warn("未找到分块内容，fileMd5: {}", fileMd5);
    return;  // 没有内容直接退出
}
```

**fetchTextChunks() 内部实现：**

```java
private List<TextChunk> fetchTextChunks(String fileMd5) {
    // 查询 document_vectors 表
    List<DocumentVector> vectors =
        documentVectorRepository.findByFileMd5(fileMd5);

    // DocumentVector → TextChunk（只取需要的字段）
    return vectors.stream()
        .map(v -> new TextChunk(v.getChunkId(), v.getTextContent()))
        .toList();
}
```

**数据转换：**

```
MySQL document_vectors 表（ParseService存的）：
[{id:1, fileMd5:abc, chunkId:1, text:"AI是...", userId:"u1", ...},
 {id:2, fileMd5:abc, chunkId:2, text:"ML是...", userId:"u1", ...}]
          ↓ 只取 chunkId 和 textContent
TextChunk列表（轻量对象）：
[TextChunk(chunkId=1, content="AI是..."),
 TextChunk(chunkId=2, content="ML是...")]
```

---

### 步骤3：提取纯文本列表

```java
List<String> texts = chunks.stream()
    .map(TextChunk::getContent)
    .toList();
// 结果：["AI是...", "ML是...", "深度学习是..."]
// API只需要纯文字，不需要chunkId等元数据
```

**注意：texts 和 chunks 索引严格对应！**
```
texts[0]  ←对应→  chunks[0]
texts[1]  ←对应→  chunks[1]
texts[2]  ←对应→  chunks[2]
后面步骤5中用索引 i 同时访问两个列表
```

---

### 步骤4：调用AI API生成向量（核心！）

```java
List<float[]> vectors = embeddingClient.embed(texts);
```

**EmbeddingClient内部流程：**

```
texts（N个文本）
    ↓ 按批次处理（每批10条，API限制）
第1批：texts[0-9]
    ↓ HTTP POST 通义千问API
    ↓ 请求体：{model:"text-embedding-v4", input:[...], dimension:2048}
    ↓ 等待响应（最多30秒，失败重试3次）
    ↓ 解析响应：{data:[{embedding:[2048个float]}, ...]}
第2批：texts[10-19]  ...
    ↓
vectors（N个 float[2048]）
```

**发送给API的请求：**
```json
POST https://dashscope.aliyuncs.com/compatible-mode/v1/embeddings
Authorization: Bearer sk-xxxx

{
  "model": "text-embedding-v4",
  "input": ["AI是计算机科学分支...", "机器学习是..."],
  "dimension": 2048,
  "encoding_format": "float"
}
```

**API返回的响应：**
```json
{
  "data": [
    {"embedding": [0.12, -0.34, 0.89, ..., 0.23], "index": 0},
    {"embedding": [-0.56, 0.78, 0.12, ..., 0.67], "index": 1}
  ]
}
```

**向量是什么？**
```
"AI是计算机科学分支" → [0.12, -0.34, 0.89, ..., 0.23]
                         ↑ 2048个浮点数，约8KB

语义相似的文本，向量距离很近：
"AI的发展趋势" 和 "人工智能未来方向"
→ 向量距离 = 0.05（很近，语义相似）

语义不同的文本，向量距离很远：
"AI的发展趋势" 和 "今天天气不错"
→ 向量距离 = 0.89（很远，语义不同）
```

---

### 步骤5：构建EsDocument（最精妙！）

```java
List<EsDocument> esDocuments = IntStream.range(0, chunks.size())
    .mapToObj(i -> new EsDocument(
        UUID.randomUUID().toString(),  // ES文档唯一ID
        fileMd5,                        // 文件指纹
        chunks.get(i).getChunkId(),     // 分块序号
        chunks.get(i).getContent(),     // 文本内容
        vectors.get(i),                 // 对应的向量！（索引i配对）
        "deepseek-embed",               // 模型版本
        userId,                         // 权限字段
        orgTag,                         // 权限字段
        isPublic                        // 权限字段
    ))
    .toList();
```

**为什么用IntStream.range()？**
```java
// 问题：需要同时遍历两个列表，按索引配对
// chunks[i] 的文本 对应 vectors[i] 的向量

// ❌ 无法用forEach（只能遍历一个列表）
chunks.forEach(chunk -> {
    // 怎么拿到对应的vector？不知道索引！
});

// ✅ IntStream.range 生成索引序列
IntStream.range(0, chunks.size())  // 生成 0,1,2,...,n-1
    .mapToObj(i -> new EsDocument(
        chunks.get(i).getContent(),  // 用i取chunk
        vectors.get(i),              // 用i取vector
    ));
```

**EsDocument的完整结构：**
```java
{
    id: "550e8400-e29b-41d4-a716-446655440000",  // UUID
    fileMd5: "abc123def456",
    chunkId: 1,
    textContent: "AI是计算机科学的一个分支...",
    vector: float[]{0.12, -0.34, ..., 0.23},      // 2048维
    modelVersion: "deepseek-embed",
    userId: "user123",    // 权限
    orgTag: "TECH_DEPT",  // 权限
    isPublic: false        // 权限
}
```

---

### 步骤6：批量存入Elasticsearch

```java
elasticsearchService.bulkIndex(esDocuments);
```

**ElasticsearchService.bulkIndex() 内部：**

```java
// 构建批量操作
List<BulkOperation> bulkOperations = documents.stream()
    .map(doc -> BulkOperation.of(op -> op.index(idx -> idx
        .index("knowledge_base")  // 索引名
        .id(doc.getId())           // 文档ID
        .document(doc)             // 文档内容
    )))
    .toList();

// 执行批量写入（一次网络请求写入所有文档）
BulkResponse response = esClient.bulk(
    BulkRequest.of(b -> b.operations(bulkOperations))
);

// 检查是否有失败的文档
if (response.errors()) {
    // 打印失败详情
}
```

**为什么用bulkIndex而不是逐条写入？**
```
逐条写入（100个分块）：
100次HTTP请求 × 10ms/次 = 1000ms = 1秒

bulkIndex（100个分块）：
1次HTTP请求 = 约50ms

性能提升：20倍！
```

---

## 📊 完整数据流总结

```
MySQL document_vectors 表
（ParseService已存好的文本分块）
    ↓ fetchTextChunks()
    ↓
List<TextChunk>  [{chunkId:1, content:"AI是..."}, ...]
    ↓ .map(TextChunk::getContent)
    ↓
List<String>     ["AI是...", "ML是...", ...]
    ↓ embeddingClient.embed()
    ↓ 调用通义千问API（每批10条）
    ↓
List<float[]>    [[0.12,-0.34,...], [-0.56,0.78,...], ...]
    ↓ IntStream.range() 配对
    ↓
List<EsDocument> [{text+vector+权限}, {text+vector+权限}, ...]
    ↓ elasticsearchService.bulkIndex()
    ↓
Elasticsearch knowledge_base 索引
（可以被HybridSearchService检索了！）
```

---

## 💡 关键设计点

### 1. 权限信息贯穿全流程
```
上传时指定：userId + orgTag + isPublic
    ↓ 存入 file_upload 表
    ↓ 通过 Kafka 传递给消费者
    ↓ ParseService 存入 document_vectors
    ↓ VectorizationService 存入 Elasticsearch
    ↓ 检索时 HybridSearchService 过滤
```

### 2. 代码中的小问题
```java
// 注释说"deepseek-embed"，但实际用的是通义千问！
"deepseek-embed"  // ← 注释有误，实际是 text-embedding-v4
// 这是一个可以在面试中提出的优化点
```

### 3. 没有处理 texts 和 vectors 数量不一致的情况
```java
// 如果 embeddingClient.embed() 返回的向量数量
// 和 texts 数量不同，IntStream.range() 会越界！
// 更健壮的写法：
if (vectors.size() != texts.size()) {
    throw new RuntimeException(
        "向量数量不匹配: texts=" + texts.size() +
        ", vectors=" + vectors.size());
}
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 向量2048维是怎么决定的？ | 通义千问text-embedding-v4支持256/512/1024/2048维，维度越高语义表达越精准，但存储空间越大 |
| 为什么不直接存向量到MySQL？ | Elasticsearch专门为向量检索优化，支持KNN算法，MySQL不支持高效的向量相似度查询 |
| EmbeddingClient为什么每批10条？ | 通义千问API的限制，单次请求最多10条输入 |
| 向量化完成后还能更新吗？ | 目前没有更新机制，若文件内容变更需要删除旧向量重新处理 |

---

## 🔗 相关文件

- [ParseService](../02-文档解析/01-ParseService解析.md) - 前一步：文档解析和切分
- [HybridSearchService](../04-混合检索/01-HybridSearchService.md) - 后一步：混合检索
- [EmbeddingClient](#) - 调用通义千问API的客户端
- [ElasticsearchService](#) - ES操作封装

