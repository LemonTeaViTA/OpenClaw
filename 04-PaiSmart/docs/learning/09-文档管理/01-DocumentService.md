# DocumentService + ElasticsearchService - 文档管理

## 📌 涉及文件

| 文件 | 职责 |
|------|------|
| `service/DocumentService.java` | 文档删除、文件列表、下载URL、预览 |
| `service/ElasticsearchService.java` | ES批量写入、按fileMd5删除 |

---

## 🎯 一句话理解

> DocumentService = 文档的「生命周期管理员」
> 负责文档的查询、下载、预览、删除（四处同步：ES + MinIO + MySQL向量表 + MySQL文件表）

---

## 🗺️ 文档存储的四个位置

```
一个文档上传后存在四个地方：

① MySQL file_upload 表
   存：文件名、MD5、大小、userId、orgTag、isPublic、状态
   用：文件列表、权限判断、下载链接生成

② MySQL document_vectors 表
   存：切分后的文本块（chunkId + textContent + 权限）
   用：向量化的输入数据

③ MinIO 对象存储
   路径：uploads/merged/{fileMd5}
   存：实际文件二进制
   用：下载、预览、重新处理

④ Elasticsearch knowledge_base 索引
   存：文本块向量（textContent + vector + 权限）
   用：语义检索

删除文档时，这四个地方都要清理！
```

---

## 🔥 deleteDocument() - 四步删除

```java
@Transactional
public void deleteDocument(String fileMd5, String userId) {
    // 权限验证：文件必须属于当前用户
    FileUpload fileUpload = fileUploadRepository
        .findByFileMd5AndUserId(fileMd5, userId)
        .orElseThrow(() -> new RuntimeException("文件不存在"));

    // 步骤1：删除ES中的向量数据
    elasticsearchService.deleteByFileMd5(fileMd5);

    // 步骤2：删除MinIO中的文件
    // 新路径：merged/{fileMd5}
    // 旧路径（兼容）：merged/{fileName}
    minioClient.removeObject(RemoveObjectArgs.builder()
        .bucket("uploads")
        .object("merged/" + fileMd5)
        .build());

    // 步骤3：删除MySQL document_vectors 记录
    documentVectorRepository.deleteByFileMd5(fileMd5);

    // 步骤4：删除MySQL file_upload 记录
    fileUploadRepository.deleteByFileMd5(fileMd5);
}
```

**删除顺序的考量：**
```
为什么ES先删？
  ES删除后，用户立即无法检索到该文档
  即使后续步骤失败，用户也不会看到已删除文档的内容

为什么file_upload最后删？
  file_upload是"根记录"，删了就找不到文件信息了
  前几步失败时，通过file_upload还能重试

问题：没有全局事务
  ES删成功 → MinIO删失败 → 数据不一致
  需要补偿事务或幂等重试机制（当前没有）
```

---

## 🔥 getAccessibleFiles() - 权限感知的文件列表

```java
public List<FileUpload> getAccessibleFiles(String userId, String orgTags) {
    // 获取用户有效的组织标签（含层级继承）
    User user = userRepository.findByUsername(userId);
    List<String> effectiveTags =
        orgTagCacheService.getUserEffectiveOrgTags(user.getUsername());

    if (effectiveTags.isEmpty()) {
        // 无组织标签：只返回自己的 + 公开的
        return fileUploadRepository.findByUserIdOrIsPublicTrue(userId);
    } else {
        // 有组织标签：自己的 + 公开的 + 组织内的
        return fileUploadRepository
            .findAccessibleFilesWithTags(userId, effectiveTags);
    }
}
```

**对应的SQL查询：**
```sql
SELECT * FROM file_upload
WHERE user_id = :userId          -- 自己上传的
   OR is_public = true           -- 公开文档
   OR org_tag IN (:orgTagList)   -- 组织内的文档
```

---

## 🔥 generateDownloadUrl() - 预签名下载

```java
public String generateDownloadUrl(String fileMd5) {
    FileUpload fileUpload = fileUploadRepository.findByFileMd5(fileMd5);

    // 先尝试新路径（MD5），再降级到旧路径（文件名）
    String objectName = "merged/" + fileMd5;
    String presignedUrl = minioClient.getPresignedObjectUrl(
        GetPresignedObjectUrlArgs.builder()
            .method(Method.GET)
            .bucket("uploads")
            .object(objectName)
            .expiry(3600)  // 1小时有效
            .build()
    );
    return presignedUrl;
}
```

**预签名URL示例：**
```
http://localhost:19000/uploads/merged/abc123
  ?X-Amz-Algorithm=AWS4-HMAC-SHA256
  &X-Amz-Credential=admin%2F...
  &X-Amz-Date=20260316T120000Z
  &X-Amz-Expires=3600
  &X-Amz-SignedHeaders=host
  &X-Amz-Signature=xxx

任何人拿到这个URL，1小时内可以直接下载文件
不需要登录，不需要API Key
```

---

## 🔥 ElasticsearchService - ES操作封装

### bulkIndex() - 批量写入

```java
public void bulkIndex(List<EsDocument> documents) {
    List<BulkOperation> ops = documents.stream()
        .map(doc -> BulkOperation.of(op -> op.index(idx -> idx
            .index("knowledge_base")
            .id(doc.getId())
            .document(doc)
        )))
        .toList();

    BulkResponse response = esClient.bulk(
        BulkRequest.of(b -> b.operations(ops))
    );

    // 检查部分失败
    if (response.errors()) {
        for (BulkResponseItem item : response.items()) {
            if (item.error() != null) {
                logger.error("文档 {} 写入失败: {}",
                    item.id(), item.error().reason());
            }
        }
        throw new RuntimeException("批量索引部分失败");
    }
}
```

### deleteByFileMd5() - 按文件删除

```java
public void deleteByFileMd5(String fileMd5) {
    esClient.deleteByQuery(DeleteByQueryRequest.of(d -> d
        .index("knowledge_base")
        .query(q -> q.term(t -> t
            .field("fileMd5")
            .value(fileMd5)
        ))
    ));
    // 删除该文件的所有向量chunk
}
```

---

## 🔥 getFilePreviewContent() - 文件预览

```java
public String getFilePreviewContent(String fileMd5, String fileName) {
    // 从MinIO获取文件流
    InputStream inputStream = minioClient.getObject(...);

    String ext = getFileExtension(fileName).toLowerCase();

    if (isTextFile(ext)) {
        // 文本文件：读取前10KB
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(inputStream, "UTF-8"));
        // 读取直到10KB，超出部分显示截断提示
        return content + "\n... (内容已截断，仅显示前10KB)";
    } else {
        // 非文本文件：返回文件信息
        return String.format(
            "文件名: %s\n文件大小: %s\n文件类型: %s\n上传时间: %s\n\n此文件类型不支持预览",
            fileName, formatFileSize(size), ext.toUpperCase(), createdAt
        );
    }
}
```

**判定为文本文件的扩展名：**
```java
String[] textExtensions = {
    "txt", "md", "doc", "docx", "pdf", "html", "xml", "json",
    "csv", "log", "java", "js", "ts", "py", "cpp", "sql", "yml"
};
// ⚠️ 注意：doc/docx/pdf 被当作文本文件直接读取
// 但这些格式是二进制，直接读会显示乱码
// 应该用 Apache Tika 提取纯文本，而不是直接读字节
```

---

## ⚠️ 代码的不足

### 1. deleteDocument 四步操作没有事务保障

```
ES删成功 → MinIO删成功 → document_vectors删失败
→ ES和MinIO已清理，但MySQL里还有向量记录
→ 向量化时会查到这些孤立记录但ES里已无对应文档
→ 数据不一致

改进：补偿事务 / 软删除（先标记deleted，定时清理）
```

### 2. MinIO路径有新旧两套，靠降级兜底

```java
// 代码里反复出现这种降级逻辑
try {
    // 新路径：merged/{fileMd5}
} catch (Exception e) {
    // 旧路径：merged/{fileName}
}
// 这是历史遗留问题，新旧数据路径不统一
// 应该做一次数据迁移，统一使用fileMd5路径
```

### 3. 文件预览对 doc/docx/pdf 判断有误

```java
// isTextFile() 里包含了 doc, docx, pdf
String[] textExtensions = {"txt", "md", "doc", "docx", "pdf", ...};
// 但这些文件是二进制格式！直接读取 InputStream 会显示乱码
// 应该用 Apache Tika 提取文本内容再展示
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 为什么MinIO路径用fileMd5而不是文件名？ | 文件名可以重复，MD5唯一。用MD5做路径可以天然去重 |
| 删除文档时为什么不删除MinIO分片？ | 分片在合并时已经被删除了（UploadService.mergeChunks步骤4），合并后只剩merged/{fileMd5} |
| BulkIndex失败时会回滚已成功的记录吗？ | 不会，ES Bulk API是尽力而为，部分成功部分失败，没有事务 |

---

## 🔗 相关文件

- [UploadService](../01-数据摄入/02-文件上传Service.md) - 文件写入MinIO的过程
- [VectorizationService](../03-向量化/01-VectorizationService.md) - 调用bulkIndex写入ES
- [HybridSearchService](../04-混合检索/01-HybridSearchService.md) - 调用deleteByFileMd5

