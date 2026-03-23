# ParseService 深度分析：现有设计的问题与企业级差距

> 本文档基于对 `ParseService.java` 源码的逐行分析，记录7个代码层面的真实问题，以及从「能跑」到「企业级 RAG」还缺什么。
>
> **阅读前提**：先看 [01-ParseService解析.md](./01-ParseService解析.md) 了解基本流程。

---

## 问题1：名字叫「父-子切片」，数据库里只有子，没有父

### 代码现状

```java
// StreamingContentHandler.processParentChunk()
private void processParentChunk() {
    String parentChunkText = buffer.toString();       // 父块（1MB文本）
    List<String> childChunks =                         // 切成子块
        splitTextIntoChunksWithSemantics(parentChunkText, chunkSize);
    this.savedChunkCount =
        saveChildChunks(..., childChunks, ...);        // 只存子块！
    buffer.setLength(0);                               // 父块直接丢弃
}
```

```java
// saveChildChunks() 存入数据库的字段
vector.setFileMd5(fileMd5);       // 文件标识
vector.setChunkId(currentChunkId); // 子块序号
vector.setTextContent(chunk);      // 子块文本
vector.setUserId(userId);
vector.setOrgTag(orgTag);
vector.setPublic(isPublic);
// ← 没有 parentChunkId，没有 sectionTitle，没有 offset
```

### 后果

| 功能 | 需要什么 | 现在有吗 |
|------|---------|----------|
| 命中子块后扩展上下文 | parent_chunk_id，回溯父块 | ❌ |
| 把相邻子块合并还原段落 | chunk_order + offset | ❌ |
| 按章节做 rerank | section_title / section_path | ❌ |
| 答案来源显示"第X章第X节" | section_path | ❌ |

### 数据库应有的字段（参考）

```sql
CREATE TABLE document_chunk (
    id              BIGINT PRIMARY KEY,
    file_md5        VARCHAR(32),
    doc_id          VARCHAR(64),       -- 文档业务ID
    parent_chunk_id BIGINT,            -- 父块ID（NULL表示是顶级）
    chunk_order     INT,               -- 在父块内的顺序
    section_title   VARCHAR(256),      -- 所在章节标题
    section_path    VARCHAR(512),      -- 完整章节路径，如"第一章/第二节"
    page_no         INT,               -- 所在页码
    start_offset    INT,               -- 在原文中的起始字符位置
    end_offset      INT,               -- 结束字符位置
    text_content    TEXT,
    chunk_checksum  VARCHAR(32),       -- chunk 级别 MD5
    language        VARCHAR(16),
    is_active       BOOLEAN DEFAULT TRUE,  -- 版本失效标记
    created_at      DATETIME,
    -- 权限字段
    user_id         VARCHAR(64),
    org_tag         VARCHAR(64),
    is_public       BOOLEAN
);
```

### 一句话总结

> 代码注释说的是「父-子策略」，实际数据库里是「扁平的子块列表」。层级关系只活在内存里，存完就丢了。

---

## 问题2：按字符数切，不是按 Token 数切

### 代码现状

```java
// splitTextIntoChunksWithSemantics()
if (paragraph.length() > chunkSize)        // ← 字符长度
if (currentChunk.length() + paragraph.length() > chunkSize)  // ← 字符长度

// splitLongSentence()
if (currentChunk.length() + word.length() > chunkSize)  // ← 字符长度
```

### 为什么字符数和 Token 数不一样？

```
文本类型          512字符约等于多少Token
────────────────────────────────────
中文正常文本       约 170-200 token（中文1字≈0.4-0.6 token）
英文正常文本       约 100-130 token（英文1词≈1-2 token）
代码（Python）     约 200-300 token（符号多）
中英混合           差异最大，难以预测
────────────────────────────────────
```

### 实际影响

```
场景：代码文档，512字符的代码块

实际Token数可能：250-350 token
text-embedding-v4 最佳窗口：约 512 token

→ 字符数看起来安全，Token数也在范围内
→ 这个例子还好

场景：英文技术文档，512字符
实际Token数可能：100-130 token
→ chunk太小，语义不完整，向量质量差

场景：表格内容（数字+符号密集），512字符
实际Token数可能：400-500 token
→ 接近模型上限，风险区
```

### 更稳健的做法

```java
// 引入 tokenizer 计算 token 数
// 例如使用 tiktoken-java 库
Encoding encoding = Encodings.newDefaultEncodingRegistry()
    .getEncodingForModel(EncodingType.CL100K_BASE);

int tokenCount = encoding.countTokens(text);
if (tokenCount > maxTokens) {
    // 按 token 边界切
}
```

### 一句话总结

> 配置文件里的 `chunk-size: 512` 是字符数，不是 Token 数。大多数场景下不会出大问题，但在英文、代码、表格内容时会有明显偏差，chunk 质量不稳定。

---

## 问题3：没有 Overlap（重叠），跨块语义容易断

### 代码现状

```java
// splitTextIntoChunksWithSemantics()
// 纯切断，没有任何重叠逻辑
chunks.add(currentChunk.toString().trim());
currentChunk = new StringBuilder();  // 直接清空，不保留尾部
```

### 问题示例

```
原文：
"...合同第3条规定，承包方须在竣工后30日内提交
验收申请。[chunk A 结束]
[chunk B 开始]申请材料包括：竣工报告、质量检测报告..."

用户提问："验收申请需要提交什么材料？"

向量检索命中：chunk B（"申请材料包括：..."）
但 chunk B 里没有"验收申请"这个词！
→ 检索可能找不到 chunk B
→ 即使找到，LLM 也不知道这是在说"验收申请"
```

### Overlap 的标准做法

```
无 overlap（当前）：
[..chunk A...][..chunk B...][..chunk C..]

有 overlap（建议）：
[..chunk A.....][           ]
         [....chunk B.....]
                    [....chunk C..]

通常 overlap = chunk_size 的 10%-20%
例如 chunk=512，overlap=50-100字符
```

```java
// 实现思路（伪代码）
String tail = "";  // 上一个 chunk 的尾部
for (String paragraph : paragraphs) {
    String content = tail + paragraph;  // 拼接上一个 chunk 的尾部
    // ... 切分逻辑 ...
    tail = getLastNChars(currentChunk, overlapSize);  // 保留尾部
}
```

### 一句话总结

> FAQ 类文档影响不大，但制度、合同、技术文档里"定义在 A，适用在 B"的场景非常多，没有 overlap 会显著降低召回率。

---

## 问题4：父块在随机位置被硬截断

### 代码现状

```java
// StreamingContentHandler.characters()
@Override
public void characters(char[] ch, int start, int length) {
    buffer.append(ch, start, length);
    if (buffer.length() >= parentChunkSize) {
        processParentChunk();   // ← 立即处理！
        // buffer 被清空，Tika 继续输出的内容接着下一个父块
    }
}
```

### 问题根源

```
Tika 的 SAX characters() 回调不保证在语义边界触发。
它可能在以下位置调用：

- 段落中间
- 句子中间
- 表格的某一行中间
- 标题和正文之间
- 列表项中间

当 buffer 凑巧在这些位置到达 1MB，就会被硬切断。

后续的 splitTextIntoChunksWithSemantics() 只是对
「已经被截断的文本」再做语义切分，根上的连续性已经破坏。
```

### 具体场景

```
原文：
"...第三条款 承包方责任：
1. 按时完工
2. 质量达标
3. [← 恰好1MB到这里，父块被截断]
保证金退还条件]..."

父块1末尾："3."
父块2开头："保证金退还条件"
→ 子切片里出现了"3."这个无意义片段
→ "3. 保证金退还条件" 的完整语义被拆散了
```

### 更稳的做法

```java
// 达到阈值后，向后找最近的自然边界
if (buffer.length() >= parentChunkSize) {
    // 向后扫描最近的段落结束符
    int cutPoint = findNearestBoundary(buffer, parentChunkSize);
    String toProcess = buffer.substring(0, cutPoint);
    String tail = buffer.substring(cutPoint);  // 保留尾部到下一个父块
    processParentChunk(toProcess);
    buffer.setLength(0);
    buffer.append(tail);  // 接续，不丢弃
}

// 自然边界查找
private int findNearestBoundary(StringBuilder buf, int from) {
    // 向后找 \n\n（段落边界）
    int pos = buf.indexOf("\n\n", from);
    if (pos != -1 && pos - from < 200) return pos;
    // 退而求其次找句号
    pos = buf.indexOf("。", from);
    if (pos != -1 && pos - from < 100) return pos + 1;
    // 实在找不到，硬切
    return from;
}
```

### 一句话总结

> 流式触发点是字节数凑满1MB，不是语义边界。父块被截断是必然事件，不是偶发情况。这会给后续所有子切片的质量带来系统性的底线问题。

---

## 问题5：内存保护靠 System.gc()，生产环境不可靠

### 代码现状

```java
private void checkMemoryThreshold() {
    double memoryUsage = (double) usedMemory / maxMemory;
    if (memoryUsage > maxMemoryThreshold) {  // 超过80%
        System.gc();                          // ← 建议GC，不保证执行
        // 重新检查，如果还高就抛异常
        if (memoryUsage > maxMemoryThreshold) {
            throw new RuntimeException("内存不足");
        }
    }
}
```

### 三个具体问题

**① System.gc() 不保证立即执行**
```
System.gc() 只是「建议」JVM做GC，JVM可以完全忽略。
在 G1GC / ZGC 等现代垃圾回收器下，
实际触发时间不可预测，可能是几秒后，也可能根本不触发。
```

**② 检查时机太晚，而且只检查一次**
```
只在 parseAndSave() 入口检查一次。
真正消耗内存的是后面的：
  - StringBuilder buffer 累积1MB文本
  - splitTextIntoChunksWithSemantics() 生成 List<String>
  - saveChildChunks() 循环写DB
这些都不在保护范围内。
```

**③ 多并发时会互相踩**
```
用户A 和 用户B 同时上传大文件：
  - 各自的 parseAndSave() 都检查内存
  - 检查时内存OK，开始处理
  - 两个任务叠加，内存实际超出
  - GC压力大 → STW停顿 → 处理超时
```

### 企业级做法

```
1. 限制单任务文件大小（如 200MB 上限）
2. Kafka 消费者设置并发数上限（如最多3个并发解析任务）
3. 批量写入替代逐条写入（见问题6）
4. embedding 异步化，解析和向量化分开队列
5. 监控内存指标，超阈值时告警 + 暂停新任务入队
```

### 一句话总结

> `System.gc()` 是最后一道救场措施，用在生产代码的核心路径上不合适。真正的保护是「限流 + 异步 + 批量」，而不是「检测到满了再GC」。

---

## 问题6：单条插入数据库，性能差且不一致

### 代码现状

```java
// saveChildChunks() —— for 循环里逐条 save
for (String chunk : chunks) {
    currentChunkId++;
    var vector = new DocumentVector();
    // ... 设置字段 ...
    documentVectorRepository.save(vector);  // ← 每次一条，一条一个事务！
}
```

### 三个后果

**① 性能**
```
一个100页PDF，假设切出200个子块：

单条插入：200次 INSERT，200次事务提交
  每次约 5-10ms（本地MySQL）
  总耗时：1-2秒（单机），生产环境网络延迟更高

bulk 插入（saveAll）：1次 INSERT，1次事务提交
  总耗时：约 50-100ms
  性能差距：10-20倍
```

**② 部分成功的数据不一致**
```
200个子块，存到第150个时，MySQL连接断了。

当前情况：
  前150个块已提交（无法回滚）
  后50个块没有存入
  → 数据库里有150个孤立的chunk
  → 向量化时只处理150个，但文件显示完整
  → 用户查询时，文件后30%内容永远找不到
```

**③ 失败重试困难**
```
 Kafka 消费失败后重试，会重新调用 parseAndSave()：

当前代码没有幂等保护：
  → 200个chunk再存一遍
  → 数据库里有重复的 chunkId
  → 检索时同一内容命中两次，结果混乱
```

### 改进方案

```java
// ① 批量写入
documentVectorRepository.saveAll(documents);  // 一次事务

// ② 先删后存，保证幂等
@Transactional
private void saveChildChunks(String fileMd5, List<String> chunks, ...) {
    // 先删除该文件的旧数据
    documentVectorRepository.deleteByFileMd5(fileMd5);
    // 批量插入新数据
    List<DocumentVector> toSave = buildDocumentVectors(chunks, ...);
    documentVectorRepository.saveAll(toSave);
}

// ③ 分批提交（文档极大时防止单事务过大）
List<List<DocumentVector>> batches = partition(toSave, 100);
for (List<DocumentVector> batch : batches) {
    documentVectorRepository.saveAll(batch);
}
```

### 一句话总结

> `save()` 在 for 循环里是最常见的初学者写法，测试能跑，但一到生产会同时暴露性能差、数据不一致、重试污染三个问题。

---

## 问题7：fileMd5 不足以支撑文档版本管理

### 代码现状

```java
// 所有地方只用 fileMd5 标识一个文件
vector.setFileMd5(fileMd5);   // 存chunk时
findByFileMd5(fileMd5);       // 取chunk时
```

### 实际会遇到的场景

```
场景1：用户更新了文档（改了几段话）
  新文件的 MD5 变了 → 是新文件
  旧文件的 chunk 还在数据库里 → 没有失效机制
  → 检索时新旧版本都会命中
  → LLM 拿到矛盾的上下文，给出混乱答案

场景2：同一个文档内容，被两个用户分别上传
  MD5 相同 → 两条 file_upload 记录（因为有userId区分）
  chunk 却存了两份（各自的 parseAndSave）
  → 空间浪费，检索命中重复

场景3：文档只改了第1页
  MD5 变化 → 需要全量重新解析
  → 10MB文档改1行，也要重新处理整个文件
  → 处理成本和实际变化量完全不成比例

场景4：用户删除了文件
  file_upload 表删除了记录
  但 document_vectors 表里的 chunk 还在！
  且 Elasticsearch 里的向量还在！
  → 三处数据不一致
```

### 完整的版本治理需要

```
字段                说明
──────────────────────────────────────────────
file_md5           内容指纹（当前有）
doc_id             业务文档ID，跨版本稳定
version_id         版本号，每次更新递增
source_uri         原始文件路径/URL
is_active          当前是否有效（false=已被新版本替代）
updated_at         最后更新时间
indexed_at         进入ES的时间
──────────────────────────────────────────────
```

### 一句话总结

> `fileMd5` 是内容指纹，不是版本号。没有版本管理，文档更新后旧数据无法失效，用户会持续收到基于过期内容的回答。

---

## 从「能跑」到「企业级 RAG」还缺什么

### 缺口一：文档结构信息全部丢失

当前 ParseService 提取出来的是「平面文本流」，以下结构信息完全丢失：

```
❌ 一级标题 / 二级标题
❌ 表格的行列关系（只保留了文字，丢失了结构）
❌ 图片说明 / 图注
❌ 页码
❌ 列表层级（一级列表、二级列表）
❌ 附录 / 备注 / 脚注
❌ FAQ 的问题-答案对应关系
❌ 合同里的「定义 / 适用范围 / 例外条款」结构
```

**影响：** 结构往往比正文更重要。「第三章第二节」这个信息，比正文本身更能帮助检索和定位。

### 缺口二：特殊格式文档处理能力弱

```
文档类型           Tika 能处理吗    企业里占比
────────────────────────────────────────────
普通 Word/PDF      ✅ 较好          约40%
扫描版 PDF         ❌ 无法识别      约25%
表格密集文档       ⚠️  结构丢失     约20%
PPT 文本框         ⚠️  顺序混乱     约10%
图片里的文字       ❌ 无法识别      约5%
────────────────────────────────────────────
```

企业知识库里，扫描件、财务表格、制度附件、截图类 SOP 占比很高。这部分用当前方案效果会明显差。

**补充需要：**
```
- OCR（Tesseract 或商业服务）
- 表格结构提取（camelot、pdfplumber）
- Layout Analysis（检测栏目、图文关系）
- 图片描述生成（多模态模型）
```

### 缺口三：只有 chunk，没有完整的检索策略

```
当前流程：
切好 chunk → 向量化 → KNN检索 → 返回结果

企业级检索 pipeline：
            ┌─ KNN向量检索（语义）
用户查询 ──→├─ BM25关键词检索（精确匹配）
            ├─ metadata filter（部门/版本/日期过滤）
            └─ 混合召回
                ↓ reranker（对召回结果重排序）
                ↓ context expansion（命中chunk → 扩展到父块）
                ↓ 去重 / 聚类
                ↓ prompt packing（按token限制塞入上下文）
                ↓ LLM生成
```

**PaiSmart 已经有：** KNN + BM25 + RRF（HybridSearchService）

**还缺：** context expansion（命中后扩大上下文窗口）、reranker、chunk 级别去重

### 缺口四：权限是「存时打标签」，检索时过滤有隐患

当前设计：
```
存入时：chunk 上打 userId + orgTag + isPublic
检索时：ES filter 过滤
```

**企业里真正难的场景：**
```
- 用户的 orgTag 变了（调岗、离职），旧 chunk 上的标签不会自动更新
- 一个文档对多个部门可见，需要 ACL 列表，不是单个 orgTag
- 离职员工的私有文档：应该对管理员可见，对同事不可见
- 审计需求：为什么这条回答引用了这份文档？
```

**更健壮的设计方向：**
```
- 权限独立存储，检索时动态计算，不硬编码在 chunk 里
- ACL 列表替代单个 orgTag
- 操作日志：谁、什么时间、检索了什么、引用了什么
```

---

## 总体评价

```
维度                 现状评分    说明
──────────────────────────────────────────────────────
核心链路完整性        ★★★★☆    上传→解析→向量→检索→问答，链路通
代码可读性            ★★★★☆    注释清晰，结构清楚
文本切分质量          ★★★☆☆    三级切分思路对，但无overlap、无token控制
数据完整性            ★★☆☆☆    父块关系丢失，无版本管理，单条写入无事务
生产健壮性            ★★☆☆☆    内存保护弱，无并发控制，无幂等保障
企业特殊格式支持      ★★☆☆☆    只支持文本型文档，扫描件无法处理
权限治理              ★★★☆☆    基础 ACL 有了，动态变更和审计缺失
──────────────────────────────────────────────────────
```

**定位：**
- 作为**学习项目**：完整度非常高，能理解 RAG 全链路 ✅
- 作为**简历项目**：技术栈选型合理，亮点足够 ✅
- 作为**生产企业系统**：还需要在数据完整性、健壮性上补课 ⚠️

---

## 面试中如何用这些分析

> 如果面试官问「你们的文档切分有什么不足」，可以这样回答：

**第一层（说出来就加分）：**
> 当前用字符数控制 chunk 大小，没有按 token 数控制。对于英文、代码类文档，512字符的 chunk 实际 token 数差异很大，会影响向量质量。

**第二层（说出来很亮眼）：**
> 切分时没有设计 overlap 机制，跨 chunk 的语义关系可能断裂。企业级做法是保留 10-20% 的尾部文本作为下一个 chunk 的前缀。

**第三层（说出来显示有深度）：**
> 数据库里只存了子切片，父块的层级关系、章节路径、页码等结构信息都没有持久化。这导致命中子块后无法回溯上下文扩窗，也无法告诉用户"这段来自第几章"。

---

## 相关文件

- [01-ParseService解析.md](./01-ParseService解析.md) - 基本流程和配置
- [../03-向量化/01-VectorizationService.md](../03-向量化/01-VectorizationService.md) - 下一步：向量化
- [../04-混合检索/01-HybridSearchService.md](../04-混合检索/01-HybridSearchService.md) - 检索策略

