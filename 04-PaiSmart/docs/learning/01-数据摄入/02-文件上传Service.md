# UploadService - 文件上传业务逻辑层

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/service/UploadService.java`
- **层级职责**：Service层（业务逻辑层）
- **代码行数**：641行（最复杂的Service之一）

---

## 🎯 一句话理解

> UploadService = 分片上传的「大脑」，真正实现Redis+MySQL+MinIO三层协同

---

## 🏗️ 三层存储架构（核心设计）

```
┌─────────────────────────────────────┐
│ Redis（Bitmap）                      │
│ Key: upload:{userId}:{fileMd5}      │
│ 作用：快速查询分片状态，断点续传     │
│ 特点：快但可能丢失                   │
└─────────────────────────────────────┘
              ↕ 互补
┌─────────────────────────────────────┐
│ MySQL（两张表）                      │
│ file_upload：文件基本信息+权限       │
│ chunk_info：分片路径+MD5             │
│ 作用：持久化，Redis丢失时可恢复      │
└─────────────────────────────────────┘
              ↕ 指向
┌─────────────────────────────────────┐
│ MinIO（对象存储）                    │
│ chunks/{fileMd5}/{index}：分片文件  │
│ merged/{fileMd5}：合并后完整文件    │
│ 作用：存储实际的文件二进制数据       │
└─────────────────────────────────────┘
```

---

## 🔥 核心方法1：uploadChunk() - 四个阶段

### 阶段1：创建文件记录（MySQL）

```java
// 检查文件是否第一次上传
boolean fileExists = fileUploadRepository
    .findByFileMd5AndUserId(fileMd5, userId).isPresent();

if (!fileExists) {
    FileUpload fileUpload = new FileUpload();
    fileUpload.setFileMd5(fileMd5);
    fileUpload.setFileName(fileName);
    fileUpload.setTotalSize(totalSize);
    fileUpload.setStatus(0);        // 0=上传中
    fileUpload.setUserId(userId);   // 权限！
    fileUpload.setOrgTag(orgTag);   // 权限！
    fileUpload.setPublic(isPublic); // 权限！
    fileUploadRepository.save(fileUpload);
}
```

**为什么用 (file_md5, user_id) 联合唯一索引？**
```
同一个文件（相同MD5）可以被不同用户上传
用户A 上传 技术文档.pdf (MD5=abc) → file_upload记录1
用户B 上传 技术文档.pdf (MD5=abc) → file_upload记录2
两者互不影响，权限独立
```

---

### 阶段2：三层验证（最精妙的设计！）

```java
// 第一层：Redis检查（最快）
boolean chunkUploaded = isChunkUploaded(fileMd5, chunkIndex, userId);

// 第二层：MySQL检查（持久化验证）
boolean chunkInfoExists = chunkInfoRepository
    .findByFileMd5OrderByChunkIndexAsc(fileMd5)
    .stream()
    .anyMatch(chunk -> chunk.getChunkIndex() == chunkIndex);

// 第三层：MinIO检查（最终验证）
try {
    minioClient.statObject(StatObjectArgs.builder()
        .bucket("uploads")
        .object(storagePath)
        .build());
} catch (Exception e) {
    // MinIO中不存在 → 需要重新上传
    chunkUploaded = false;
}
```

**三层验证解决的场景：**

| 场景 | Redis | MySQL | MinIO | 处理方式 |
|------|-------|-------|-------|----------|
| 全部正常 | ✅ | ✅ | ✅ | 跳过，幂等 |
| Redis被清空 | ❌ | ✅ | ✅ | 补充Redis记录 |
| MySQL记录丢失 | ✅ | ❌ | ✅ | 补充MySQL记录 |
| MinIO文件丢失 | ✅ | ✅ | ❌ | 重新上传文件 |

**核心思想：容错 + 幂等**
- 重复上传同一分片不出错（幂等性）
- 某一层数据丢失可自动修复（容错性）

---

### 阶段3：上传分片到MinIO

```java
// 1. 计算分片MD5（用于验证完整性）
byte[] fileBytes = file.getBytes();
String chunkMd5 = DigestUtils.md5Hex(fileBytes);

// 2. 构建存储路径
String storagePath = "chunks/" + fileMd5 + "/" + chunkIndex;
// 例如：chunks/abc123.../0
//      chunks/abc123.../1

// 3. 上传到MinIO
PutObjectArgs putObjectArgs = PutObjectArgs.builder()
    .bucket("uploads")
    .object(storagePath)
    .stream(file.getInputStream(), file.getSize(), -1)
    .contentType(file.getContentType())
    .build();
minioClient.putObject(putObjectArgs);

// 4. 标记Redis（即使失败也不抛异常！）
try {
    markChunkUploaded(fileMd5, chunkIndex, userId);
} catch (Exception e) {
    // 不抛异常：文件已上传成功，Redis标记只是加速查询
    // 优先级：MinIO > MySQL > Redis
    logger.error("标记分片失败，但不影响主流程", e);
}
```

**MinIO存储结构：**
```
uploads/ （桶）
├── chunks/
│   └── abc123def456/  （文件MD5）
│       ├── 0           （第0个分片）
│       ├── 1           （第1个分片）
│       └── 2           （第2个分片）
└── merged/
    └── abc123def456   （合并后的完整文件）
```

---

### 阶段4：保存分片信息到MySQL

```java
// 保存到 chunk_info 表
ChunkInfo chunkInfo = new ChunkInfo();
chunkInfo.setFileMd5(fileMd5);
chunkInfo.setChunkIndex(chunkIndex);
chunkInfo.setChunkMd5(chunkMd5);       // 用于完整性验证
chunkInfo.setStoragePath(storagePath);  // 合并时需要这个路径
chunkInfoRepository.save(chunkInfo);
```

**chunk_info表的作用：**
- 记录每个分片在MinIO的路径（合并时按顺序读取）
- 记录分片MD5（验证完整性）
- Redis丢失时可以从这里恢复状态

---

## 🔥 核心方法2：mergeChunks() - 五个步骤

```
1. 查询所有分片信息（MySQL，按index排序！）
    ↓ 为什么排序？合并必须按顺序，顺序错了文件损坏
2. 验证分片数量 + 每个分片是否存在于MinIO
    ↓ 先检查，避免合并一半失败无法回滚
3. MinIO服务端合并（composeObject）
    ↓ 不占应用服务器带宽，速度快，原子操作
4. 清理工作
   ├─ 删除MinIO分片文件（释放空间）
   ├─ 删除Redis分片状态
   └─ 更新MySQL status=1（已完成）
5. 生成预签名URL（1小时有效）
    ↓ 返回给Controller，Controller发给Kafka
```

**为什么用MinIO的composeObject而不是应用层合并？**

```
传统方式（应用层合并）：
MinIO → 下载到应用服务器内存 → 合并 → 上传回MinIO
缺点：占用服务器带宽和内存，速度慢

composeObject（服务端合并）：
MinIO内部直接操作，应用服务器只发一个命令
优点：零带宽占用，零内存占用，速度快，原子操作
```

**预签名URL是什么？**
```
普通URL（需要认证）：
http://minio:19000/uploads/merged/abc123
→ 访问需要提供AccessKey+SecretKey

预签名URL（临时授权）：
http://minio:19000/uploads/merged/abc123?X-Amz-Signature=xxx&X-Amz-Expires=3600
→ 任何人在1小时内都可以直接访问，无需认证
→ 这个URL会发给Kafka消费者，用于下载文件解析
```

---

## 🔥 核心方法3：Redis Bitmap操作

### markChunkUploaded() - 标记已上传

```java
String redisKey = "upload:" + userId + ":" + fileMd5;
// 例如：upload:user123:abc123def456

redisTemplate.opsForValue().setBit(redisKey, chunkIndex, true);
// 将第chunkIndex位设置为1
```

### Redis Bitmap原理

```
假设文件有5个分片：

初始：00000  （所有bit=0，未上传）
上传分片0：10000
上传分片1：11000
上传分片3：11010
全部上传：11111

内存对比（1000个分片）：
List存储：约5KB
Bitmap：  约125字节  → 节省40倍！
```

### getUploadedChunks() - 性能优化亮点

```java
// ❌ 低效方式：逐个查询（1000分片=1000次Redis请求）
for (int i = 0; i < totalChunks; i++) {
    if (redisTemplate.opsForValue().getBit(key, i)) {
        uploadedChunks.add(i);
    }
}

// ✅ 高效方式：一次性读取整个Bitmap（1次请求）
byte[] bitmapData = redisTemplate.execute(
    (RedisCallback<byte[]>) connection -> connection.get(key.getBytes())
);
// 然后在内存中解析bit位
for (int i = 0; i < totalChunks; i++) {
    if (isBitSet(bitmapData, i)) {
        uploadedChunks.add(i);
    }
}
// 性能提升：100-1000倍！
```

### isBitSet() - Bitmap位解析

```java
private boolean isBitSet(byte[] bitmapData, int bitIndex) {
    int byteIndex = bitIndex / 8;           // 第几个字节
    int bitPosition = 7 - (bitIndex % 8);  // 字节内第几位
    // 注意：Redis Bitmap从高位到低位存储！

    if (byteIndex >= bitmapData.length) return false;

    return (bitmapData[byteIndex] & (1 << bitPosition)) != 0;
}

// 例如：bitIndex=3
// byteIndex = 3/8 = 0  → 第0个字节
// bitPosition = 7-(3%8) = 4 → 字节内第4位
// 检查第0字节的第4位是否为1
```

---

## 🔥 核心方法4：getTotalChunks() - 
