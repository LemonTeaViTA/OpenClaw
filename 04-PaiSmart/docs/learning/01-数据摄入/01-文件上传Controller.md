# UploadController - 文件上传控制层

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/controller/UploadController.java`
- **API前缀**：`/api/v1/upload`
- **层级职责**：Controller层（HTTP接口层）

---

## 🎯 一句话理解

> Controller层 = HTTP世界和业务世界之间的「翻译官」
> 不干活，只负责接收请求、验证参数、调用Service、返回响应

---

## 🔌 提供的接口（3个核心 + 1个辅助）

| 接口 | 路径 | 方法 | 作用 |
|------|------|------|------|
| 上传分片 | `/chunk` | POST | 上传文件的某一个分片 |
| 查询状态 | `/status` | GET | 查询哪些分片已上传（断点续传用）|
| 合并分片 | `/merge` | POST | 所有分片上传完后触发合并 |
| 支持类型 | `/supported-types` | GET | 获取系统支持的文件类型列表 |

---

## 📋 参数提取方式（重要！）

```java
@PostMapping("/chunk")
public ResponseEntity uploadChunk(
    @RequestParam("fileMd5") String fileMd5,
    // ↑ 从HTTP表单数据提取，前端发送：fileMd5=abc123

    @RequestParam("chunkIndex") int chunkIndex,
    // ↑ 自动类型转换：字符串"0" → 整数 0

    @RequestParam(value="orgTag", required=false) String orgTag,
    // ↑ required=false：可选参数，不传则为null

    @RequestParam(value="isPublic", defaultValue="false") boolean isPublic,
    // ↑ defaultValue：不传则默认false

    @RequestParam("file") MultipartFile file,
    // ↑ 文件上传专用类型

    @RequestAttribute("userId") String userId
    // ↑ 不是请求参数！由JwtAuthenticationFilter解析JWT后放入
    //   前端 → 携带JWT → 过滤器解析 → request.setAttribute("userId", id)
)
```

### @RequestParam 和 @RequestBody 的区别

| 注解 | 数据来源 | 适用场景 | Content-Type |
|------|---------|---------|---------------|
| `@RequestParam` | URL参数或表单数据 | 简单参数、文件上传 | multipart/form-data |
| `@RequestBody` | 请求体JSON | 复杂对象 | application/json |
| `@RequestAttribute` | 请求属性（程序内部放入）| JWT解析后的userId | - |

---

## 🔄 uploadChunk() 执行流程

```
1. [参数验证] 文件类型验证（只在chunkIndex==0时）
   ├─ 不支持 → 返回400错误，记录日志
   └─ 支持 → 继续
       ↓
2. [参数预处理] orgTag自动填充
   ├─ orgTag为空 → 调用userService.getUserPrimaryOrg(userId)
   └─ orgTag不为空 → 直接使用
       ↓
3. [调用Service] uploadService.uploadChunk(所有参数)
   ← 真正的业务逻辑在这里
       ↓
4. [获取状态] 获取已上传分片列表 + 计算进度百分比
       ↓
5. [构建响应] 统一格式
   {
     code: 200,
     message: "分片上传成功",
     data: { uploaded: [0,1,2], progress: 60.0 }
   }
```

## 🔄 mergeFile() 执行流程（更重要！）

```
1. [权限验证] 文件必须属于当前用户
   ← findByFileMd5AndUserId(fileMd5, userId)
       ↓
2. [完整性检查] 所有分片是否都已上传
   ← uploadedChunks.size() < totalChunks → 返回400
       ↓
3. [合并操作] uploadService.mergeChunks()
   ← MinIO服务端合并，返回预签名URL
       ↓
4. [构建任务] 携带权限信息的FileProcessingTask
   FileProcessingTask task = new FileProcessingTask(
       fileMd5, objectUrl, fileName,
       fileUpload.getUserId(),   // ← 权限！
       fileUpload.getOrgTag(),   // ← 权限！
       fileUpload.isPublic()     // ← 权限！
   );
       ↓
5. [发送Kafka] 事务性发送，触发后续解析+向量化
   kafkaTemplate.executeInTransaction(kt -> {
       kt.send("file-processing-topic1", task);
   });
       ↓
6. 返回文件URL
```

---

## 💡 关键设计点解析

### 1. 为什么只在第一个分片验证文件类型？
```java
if (chunkIndex == 0) {  // 只在第一个分片
    validateFileType(fileName);
}
// 原因：避免每个分片都验证，100个分片就要验证100次
// 文件名在所有分片中是一样的，验证一次就够了
```

### 2. 为什么自动获取orgTag而不强制用户填写？
```java
if (orgTag == null || orgTag.isEmpty()) {
    orgTag = userService.getUserPrimaryOrg(userId);
}
// 原因：提升用户体验，用户不需要关心组织标签
// 系统自动给文件打上用户所属组织的标签
```

### 3. 为什么用事务性发送Kafka消息？
```java
kafkaTemplate.executeInTransaction(kt -> {
    kt.send(topic, task);
    return true;
});
// 原因：保证原子性
// 场景：文件合并成功，但Kafka消息没发出去
// 后果：文件存在但永远不会被解析和向量化
// 事务性发送：数据库更新和消息发送要么都成功，要么都失败
```

### 4. Controller不做什么？
```
❌ 不直接操作MySQL
❌ 不直接操作Redis
❌ 不直接操作MinIO
❌ 不包含复杂的业务逻辑
✅ 这些都由Service层完成
```

---

## 📊 统一响应格式

```json
// 成功响应
{
    "code": 200,
    "message": "分片上传成功",
    "data": {
        "uploaded": [0, 1, 2],
        "progress": 60.0
    }
}

// 错误响应（400/403/500）
{
    "code": 400,
    "message": "文件类型不支持",
    "data": null
}
```

---

## ❓ 我的疑问记录

> 在这里记录学习过程中的疑问，找到答案后填入

| 疑问 | 答案 |
|------|------|
| @RequestAttribute如何获取userId？ | JWT过滤器解析token后调用request.setAttribute()放入，Controller通过@RequestAttribute取出 |
| 
