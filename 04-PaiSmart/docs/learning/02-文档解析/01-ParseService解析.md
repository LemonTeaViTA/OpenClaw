# ParseService - 文档解析与智能切分

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/service/ParseService.java`
- **触发时机**：Kafka消费者收到消息后，第一步执行
- **核心依赖**：Apache Tika（解析）+ HanLP（中文分词）

---

## 🎯 一句话理解

> ParseService = 文档的「理解者」
> 把PDF/Word等格式的文件，变成一段段有语义的文字块

---

## 🗺️ 在整体流程中的位置

```
Kafka消费者接收任务
    ↓
下载文件（MinIO预签名URL）
    ↓
① ParseService ← 当前文件
   Apache Tika解析 → 提取纯文本
   流式切分 → 父块(1MB) → 子块(512字符)
   HanLP分词 → 保持语义完整性
   存入MySQL document_vectors 表
    ↓
② VectorizationService
   读MySQL → 调API → 存ES
```

---

## 🏗️ 核心设计：父子文档切分策略

```
大文件（如100MB PDF）
    ↓ 流式读取（避免OOM）
父块（1MB）
    ↓ 按段落、句子切分
子切片（512字符）← 最终存入数据库的单元

为什么两级切分？
父块：流式处理的单位，控制内存占用
子切片：RAG检索的单位，大小适合语义匹配
```

---

## ⚙️ 配置参数（来自 application.yml 实际值）

```yaml
file:
  parsing:
    chunk-size: 512          # 子切片最大字符数 ← 实际配置值
    # parent-chunk-size 未配置，使用代码默认值 1048576 = 1MB
    buffer-size: 8192        # 流式读取缓冲区 = 8KB
    max-memory-threshold: 0.8  # 内存使用率超80%触发GC
```

> ⚠️ 注意：`application.yml` 中没有配置 `parent-chunk-size`，代码中 `@Value("${file.parsing.parent-chunk-size:1048576}")` 的冒号后是默认值，所以父块大小默认 1MB。

---

## 🔥 主方法：parseAndSave()

```java
public void parseAndSave(
    String fileMd5,
    InputStream fileStream,  // 文件输入流
    String userId,
    String orgTag,
    boolean isPublic
) throws IOException, TikaException {

    // 1. 检查内存是否充足
    checkMemoryThreshold();

    // 2. 创建流式处理器
    StreamingContentHandler handler =
        new StreamingContentHandler(fileMd5, userId, orgTag, isPublic);

    // 3. 使用Apache Tika流式解析
    Metadata metadata = new Metadata();
    ParseContext context = new ParseContext();
    AutoDetectParser parser = new AutoDetectParser();  // 自动识别格式

    parser.parse(bufferedStream, handler, metadata, context);
    // Tika解析时，每遇到文字就调用 handler.characters()
    // handler积累够1MB就切分保存，流式处理不会OOM
}
```

---

## 🔥 StreamingContentHandler - 流式处理器

```java
private class StreamingContentHandler extends BodyContentHandler {
    private final StringBuilder parentBuffer = new StringBuilder();
    // 积累文本，到达1MB时触发切分

    @Override
    public void characters(char[] ch, int start, int length) {
        // Tika每解析出一段文字就调用这个方法
        parentBuffer.append(ch, start, length);

        // 积累够一个父块（1MB）就处理
        if (parentBuffer.length() >= parentChunkSize) {
            processParentChunk(parentBuffer.toString());
            parentBuffer.setLength(0);  // 清空缓冲区
            checkMemoryThreshold();      // 检查内存
        }
    }

    @Override
    public void endDocument() {
        // 文档结束，处理最后一段（可能不足1MB）
        if (parentBuffer.length() > 0) {
            processParentChunk(parentBuffer.toString());
        }
    }
}
```

---

## 🔥 processParentChunk() - 切分为子块

```java
private void processParentChunk(String parentText) {
    // 按段落和句子边界智能切分
    List<String> subChunks = splitIntoChunks(parentText, chunkSize);

    // 批量保存到MySQL
    List<DocumentVector> documents = new ArrayList<>();
    for (int i = 0; i < subChunks.size(); i++) {
        DocumentVector doc = new DocumentVector();
        doc.setFileMd5(fileMd5);
        doc.setChunkId(chunkCounter++);  // 全局递增序号
        doc.setTextContent(subChunks.get(i));
        doc.setUserId(userId);
        doc.setOrgTag(orgTag);
        doc.setPublic(isPublic);
        documents.add(doc);
    }
    documentVectorRepository.saveAll(documents);
}
```

---

## 🔥 splitTextIntoChunksWithSemantics() - 三级切分（实际代码）

> ⚠️ 实际方法名是 `splitTextIntoChunksWithSemantics`，不是 `splitIntoChunks`，以下是真实逻辑：

### 第一级：按段落切（\n\n 空行）

```java
String[] paragraphs = text.split("\n\n+");
for (String paragraph : paragraphs) {
    if (paragraph.length() > chunkSize) {
        // 段落太长 → 进入第二级
        chunks.addAll(splitLongParagraph(paragraph, chunkSize));
    } else if (currentChunk.length() + paragraph.length() > chunkSize) {
        // 加进来会超 → 先保存当前，开新块
        chunks.add(currentChunk.toString().trim());
        currentChunk = new StringBuilder(paragraph);
    } else {
        // 可以合并 → 累加到当前块
        currentChunk.append("\n\n").append(paragraph);
    }
}
```

### 第二级：按句子切（。！？；.!?;）

```java
// 段落超过512字符时，按句子边界切
String[] sentences = paragraph.split("(?<=[。！？；])|(?<=[.!?;])\\s+");
for (String sentence : sentences) {
    if (currentChunk.length() + sentence.length() > chunkSize) {
        chunks.add(currentChunk.toString().trim());
        currentChunk = new StringBuilder();
    }
    // 单个句子本身超过512 → 进入第三级
    if (sentence.length() > chunkSize) {
        chunks.addAll(splitLongSentence(sentence, chunkSize));
    } else {
        currentChunk.append(sentence);
    }
}
```

### 第三级：HanLP分词切（超长句子兜底）

```java
// 句子超过512字符时，用HanLP按词语边界切
List<Term> termList = StandardTokenizer.segment(sentence);
StringBuilder current = new StringBuilder();
for (Term term : termList) {
    String word = term.word;
    if (current.length() + word.length() > chunkSize && !current.isEmpty()) {
        chunks.add(current.toString());
        current = new StringBuilder();
    }
    current.append(word);
}
// HanLP失败时降级到按字符切（splitByCharacters）
```

### 三级切分全流程

```
原文本（1MB父块）
    ↓ 第1级：按 \n\n 分段落
段落A（300字）→ 直接保存
段落B（800字）→ 超过512
    ↓ 第2级：按 。！？ 分句子
    句子1（200字）+ 句子2（250字）→ 合并（450字<512）→ 保存
    句子3（600字）→ 超过512
        ↓ 第3级：HanLP分词
        按词语边界切成 ["...机器学习", "是AI的核心..."] → 保存
```

**为什么不直接用HanLP？**
```
HanLP对整个1MB文本分词 → 性能消耗极大
优先用简单的段落/句子边界（字符串操作，极快）
只有在句子太长时才用HanLP（最后兜底）
分层处理 = 兼顾性能和语义完整性
```

---

## 📊 内存管理

```java
private void checkMemoryThreshold() {
    Runtime runtime = Runtime.getRuntime();
    long usedMemory = runtime.totalMemory() - runtime.freeMemory();
    long maxMemory = runtime.maxMemory();
    double usageRatio = (double) usedMemory / maxMemory;

    if (usageRatio > maxMemoryThreshold) {  // 超过80%
        System.gc();  // 建议JVM进行垃圾回收
        logger.warn("内存使用率 {:.1f}%，已触发GC", usageRatio * 100);
    }
}
```

**为什么需要内存检查？**
```
场景：处理一个500MB的PDF

没有内存检查：
→ 内存不断增长 → OOM（OutOfMemoryError）→ 服务崩溃

有内存检查：
→ 每处理完一个父块（1MB）检查内存
→ 超过80% → 触发GC → 释放不再使用的对象
→ 内存保持在安全水位
```

---

## 💡 Apache Tika 支持的格式

```
AutoDetectParser 自动识别并处理：

文档类：PDF, Word(.doc/.docx), Excel(.xls/.xlsx),
        PowerPoint(.ppt/.pptx), OpenOffice
文本类：TXT, Markdown, HTML, XML, JSON
图片类：JPEG, PNG（OCR需要额外配置Tesseract）
压缩包：ZIP（递归解析内部文件）
邮件：EML, MSG
...

共支持 1000+ 种MIME类型
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 512字符是固定的吗？ | 来自配置文件，可以调整。字符数越小 → 检索越精准但存储量大；越大 → 上下文丰富但可能引入无关内容 |
| 流式处理和一次性加载的区别？ | 流式：边读边处理，内存始终只有8KB缓冲区；一次性：把整个文件读到内存，500MB文件就占500MB内存 |
| ParseService处理失败会怎样？ | 抛出异常 → Kafka消费者捕获 → 消息重试（最多3次）→ 都失败则进入死信队列 |

---

## 🔗 相关文件

- [UploadService](../01-数据摄入/02-文件上传Service.md) - 上一步：文件上传
- [VectorizationService](../03-向量化/01-VectorizationService.md) - 下一步：向量化

