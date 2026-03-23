# FileProcessingConsumer - Kafka消费者与异步处理

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/consumer/FileProcessingConsumer.java`
- **触发方式**：Kafka消息驱动，主题 `file-processing-topic1`
- **消费者组**：`file-processing-group`

---

## 🎯 一句话理解

> FileProcessingConsumer = 异步处理流水线的「总调度员」
> 收到Kafka消息 → 下载文件 → 解析 → 向量化，三步串行执行

---

## 🗺️ 在整体流程中的位置

```
【UploadController.mergeFile()】
    ↓ kafkaTemplate.executeInTransaction() 发送消息
【Kafka Topic: file-processing-topic1】
    ↓
【FileProcessingConsumer.processTask()】← 当前文件
    ↓ downloadFileFromStorage()
    ↓ parseService.parseAndSave()
    ↓ vectorizationService.vectorize()
    ↓
文档可检索
```

---

## 🔥 核心方法：processTask()

```java
@KafkaListener(
    topics = "#{kafkaConfig.getFileProcessingTopic()}",  // file-processing-topic1
    groupId = "#{kafkaConfig.getFileProcessingGroupId()}" // file-processing-group
)
public void processTask(FileProcessingTask task) {
    // 1. 下载文件
    InputStream fileStream = downloadFileFromStorage(task.getFilePath());

    // 2. 解析文档（Tika + 切分 + 存MySQL）
    parseService.parseAndSave(
        task.getFileMd5(), fileStream,
        task.getUserId(), task.getOrgTag(), task.isPublic()
    );

    // 3. 向量化（读MySQL + 调API + 存ES）
    vectorizationService.vectorize(
        task.getFileMd5(),
        task.getUserId(), task.getOrgTag(), task.isPublic()
    );
}
```

**FileProcessingTask 的内容：**

```java
// 来自 model/FileProcessingTask.java
class FileProcessingTask {
    String fileMd5;    // 文件指纹
    String filePath;   // MinIO预签名URL（或本地路径）
    String fileName;   // 原始文件名
    String userId;     // 权限
    String orgTag;     // 权限
    boolean isPublic;  // 权限
}
```

> ⚠️ 权限信息从上传时就跟着任务走，parseService 和 vectorizationService 都用同一份权限。

---

## 🔥 downloadFileFromStorage() - 文件下载

```java
private InputStream downloadFileFromStorage(String filePath) {
    // 情况1：本地文件路径
    File file = new File(filePath);
    if (file.exists()) {
        return new FileInputStream(file);
    }

    // 情况2：HTTP/HTTPS URL（MinIO预签名URL）
    if (filePath.startsWith("http://") || filePath.startsWith("https://")) {
        URL url = new URL(filePath);
        HttpURLConnection connection = (HttpURLConnection) url.openConnection();
        connection.setConnectTimeout(30000);  // 连接超时30秒
        connection.setReadTimeout(180000);    // 读取超时3分钟
        connection.setRequestProperty("User-Agent", "SmartPAI-FileProcessor/1.0");

        int responseCode = connection.getResponseCode();
        if (responseCode == HTTP_OK) {
            return connection.getInputStream();
        } else if (responseCode == HTTP_FORBIDDEN) {
            throw new IOException("预签名URL已过期");
        }
    }
    throw new IllegalArgumentException("不支持的路径格式: " + filePath);
}
```

**为什么支持两种路径格式？**

```
开发环境：文件在本地磁盘 → 直接 FileInputStream
生产环境：文件在MinIO → HTTP下载预签名URL

预签名URL格式：
http://minio:19000/uploads/merged/abc123?X-Amz-Signature=xxx&X-Amz-Expires=3600
有效期1小时（合并时生成），消费者必须在1小时内处理完
```

**预签名URL过期怎么办？**
```
消费者抛出 IOException("预签名URL已过期")
    ↓
Kafka DefaultErrorHandler 捕获
    ↓
固定退避重试：每3秒重试1次，最多4次（共5次）
    ↓
全部失败 → 消息发送到死信队列(file-processing-dlt)
    ↓
需要人工干预重新处理
```

---

## 🔧 Kafka 错误处理配置（KafkaConfig.java）

```java
// 固定退避策略：每 3 秒重试，最多 4 次
DefaultErrorHandler errorHandler = new DefaultErrorHandler(
    recoverer,
    new FixedBackOff(3000L, 4)  // 间隔3秒，最多4次重试
);

// 死信队列：失败消息发送到 file-processing-dlt
DeadLetterPublishingRecoverer recoverer = new DeadLetterPublishingRecoverer(
    kafkaTemplate,
    (record, ex) -> new TopicPartition(
        fileProcessingDltTopic,  // file-processing-dlt
        record.partition()        // 保持分区一致
    )
);
```

**重试流程：**

```
第1次处理失败
    ↓ 等待3秒
第2次重试失败
    ↓ 等待3秒
第3次重试失败
    ↓ 等待3秒
第4次重试失败
    ↓ 等待3秒
第5次重试失败
    ↓
发送到死信队列 file-processing-dlt
```

---

## 🔧 Kafka 生产者可靠性配置

```java
// ProducerFactory 配置
config.put(ProducerConfig.ACKS_CONFIG, "all");          // 全部ISR副本落盘才确认
config.put(ProducerConfig.ENABLE_IDEMPOTENCE_CONFIG, true); // 幂等生产者，防止重复消息
config.put(ProducerConfig.RETRIES_CONFIG, 3);           // 自动重试3次

// 事务支持
factory.setTransactionIdPrefix("file-upload-tx-");
// UploadController用 executeInTransaction 发消息：
// 保证「合并成功」和「发消息」是原子操作
```

**为什么用事务性发送？**

```
非事务场景的风险：
  文件合并成功 → 发Kafka消息失败
  结果：文件存在但永远不会被处理
  用户的文档进了知识库但检索不到

事务性发送：
  文件合并 + 发消息 = 原子操作
  要么都成功，要么都失败
  失败了用户会看到错误，可以重新上传
```

---

## 🔁 为什么用Kafka而不是直接调用？

```
直接调用方式（同步）：
用户点击上传 → 等待解析 → 等待向量化 → 才能看到结果

解析一个10MB文档：约30-120秒
向量化100个文本块：约10-30秒（调用外部API）
总等待：60-150秒

→ 用户体验极差

Kafka异步方式：
用户点击上传 → 立即返回"上传成功" → 后台慢慢处理

优点：
① 用户体验好（秒级响应）
② 解耦：上传服务和处理服务独立扩展
③ 削峰：突发大量上传时，Kafka缓冲请求
④ 容错：处理失败可重试，不丢消息
```

---

## ⚠️ 当前代码的不足

### 1. 流式读取后直接关闭，parseService 中流可能被截断

```java
// FileProcessingConsumer 在 finally 中关闭流
finally {
    if (fileStream != null) fileStream.close();
}
// 但 parseService.parseAndSave() 内部也在 try-with-resources 里操作同一个流
// 如果 parseService 未读完，Consumer 就 close 了，流被截断
// 实际上因为 parseService 是同步调用，finally 在 parse 完成后才执行，所以没问题
// 但代码结构容易误解
```

### 2. 解析和向量化是串行的，效率不高

```java
// 当前：串行
parseService.parseAndSave(...);   // 等解析完
vectorizationService.vectorize(...); // 才开始向量化

// 更高效：解析完一批存MySQL，立即触发向量化（流水线）
// 或者：解析和向量化放入不同的Kafka Topic，实现真正的流水线并行
```

### 3. 没有处理部分成功的情况

```java
// 场景：parseService 成功，vectorizationService 失败
// 结果：MySQL 里有分块，ES 里没有向量
// Kafka 重试时，parseService 会重复写入 MySQL（产生重复数据）
// 因为 saveChildChunks 没有幂等保护（见 ParseService 分析）
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 为什么@KafkaListener用SpEL表达式 `#{kafkaConfig.xxx}`？ | 因为Topic名称和GroupId在运行时才能从配置中读取，SpEL允许动态获取Bean的属性 |
| 死信队列里的消息怎么处理？ | 目前没有死信队列消费者，需要人工查看DLT消息然后手动重发 |
| Kafka消费者是单线程还是多线程？ | 默认单线程（并发=1），可配置 `concurrency` 属性增加并发消费者数 |

---

## 🔗 相关文件

- 
