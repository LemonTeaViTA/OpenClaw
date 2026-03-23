# PaiSmart RAG系统学习笔记导航

> 记录学习PaiSmart项目的过程、理解、疑问和答案

## 📚 学习路线图

```
第一章：数据摄入（文件上传）        ✅
    ↓
第二章：文档解析与文本切分           ✅
    ↓
第三章：文本向量化                  ✅
    ↓
第四章：混合检索                    ✅
    ↓
第五章：Kafka与异步处理             ✅
    ↓
第六章：RAG对话系统                 ✅
    ↓
第七章：安全与认证（JWT）           ✅
    ↓
第八章：用户与组织管理              ✅
    ↓
第九章：文档管理                    ✅
```

## 📁 笔记目录

| 章节 | 笔记文件 | 状态 |
|------|---------|------|
| 第一章：数据摄入 | [01-文件上传Controller](./01-数据摄入/01-文件上传Controller.md) | ✅ 已完成 |
| 第一章：数据摄入 | [02-文件上传Service](./01-数据摄入/02-文件上传Service.md) | ✅ 已完成 |
| 第一章：数据摄入 | [03-面试问题汇总](./01-数据摄入/03-面试问题汇总.md) | ✅ 已完成 |
| 第二章：文档解析 | [01-ParseService解析](./02-文档解析/01-ParseService解析.md) | ✅ 已完成 |
| 第二章：文档解析 | [02-ParseService深度分析与不足](./02-文档解析/02-ParseService深度分析与不足.md) | ✅ 已完成 |
| 第三章：向量化   | [01-VectorizationService](./03-向量化/01-VectorizationService.md) | ✅ 已完成 |
| 第三章：向量化   | [02-EmbeddingClient详解](./03-向量化/02-EmbeddingClient详解.md) | ✅ 已完成 |
| 第四章：混合检索 | [01-HybridSearchService](./04-混合检索/01-HybridSearchService.md) | ✅ 已完成 |
| 第五章：Kafka异步 | [01-FileProcessingConsumer](./05-Kafka与异步处理/01-FileProcessingConsumer.md) | ✅ 已完成 |
| 第六章：RAG对话系统 | [01-ChatHandler](./06-RAG对话系统/01-ChatHandler.md) | ✅ 已完成 |
| 第七章：安全与认证 | [01-JWT认证体系](./07-安全与认证/01-JWT认证体系.md) | ✅ 已完成 |
| 第八章：用户与组织 | [01-UserService](./08-用户与组织管理/01-UserService.md) | ✅ 已完成 |
| 第九章：文档管理 | [01-DocumentService](./09-文档管理/01-DocumentService.md) | ✅ 已完成 |

## 🗺️ 整体架构数据流

```
用户上传文件
    ↓
【UploadController】接收HTTP请求，参数验证，协调Service
    ↓
【UploadService】分片上传MinIO + Redis记录状态 + MySQL记录元数据
    ↓
合并分片（MinIO composeObject）→ 发送Kafka消息
    ↓
【FileProcessingConsumer】Kafka消费者接收任务，下载文件
    ↓
【ParseService】Apache Tika解析文档 → HanLP智能切分 → 存MySQL
    ↓
【VectorizationService】读MySQL分块 → 调用通义千问API → 存Elasticsearch
    ↓
用户提问
    ↓
【HybridSearchService】KNN向量检索 + BM25全文检索 + 权限过滤
    ↓
【ChatHandler】注入上下文 → DeepSeek生成回答 → WebSocket推送
```

## 🔑 核心技术选型速查

| 技术 | 用途 | 关键参数/说明 |
|------|------|----------|
| Redis Bitmap | 分片上传状态追踪 | 比List省40-80倍内存，一次读取全部状态 |
| MinIO composeObject | 分片服务端合并 | 不占应用服务器带宽，原子操作 |
| 5MB 分片大小 | 文件切片标准 | MinIO/S3协议硬性要求的最小值 |
| Apache Tika AutoDetectParser | 文档格式解析 | 自动识别1000+格式，提取纯文本，图片默认不OCR |
| 三级切分策略 | 文本语义切分 | 段落(\n\n) → 句子(。！？) → HanLP分词兜底 |
| 512字符 chunk-size | 文本切片大小 | application.yml配置，三级切分的最终粒度 |
| 1MB parent-chunk-size | 流式处理单元 | 代码默认值，控制内存防止OOM |
| text-embedding-v4 | 文本向量化 | 通义千问模型，2048维，每批最多10条 |
| Elasticsearch KNN | 向量语义检索 | HNSW算法，找意思相近的内容 |
| BM25 | 全文关键词检索 | 精确匹配专有名词，与KNN互补 |
| RRF融合排序 | 检索结果重排 | score=1/(60+rank)，两路结果合并排名 |
| Kafka 异步队列 | 解耦上传与处理 | 削峰填谷，失败重试，死信队列兜底 |
| JWT | 身份认证 | 无状态，userId+orgTag贯穿全链路权限 |

## 💡 学习方法建议

1. **每学完一个文件** → 在对应的md文件里补充你自己的理解
2. **遇到疑问** → 在「我的疑问记录」章节记下来，再找答案
3. **面试准备** → 重点看「面试问题汇总」章节
4. **忘记了** → 直接看这个README的数据流图和技术速查表

## 📅 学习记录

| 日期 | 内容 | 备注 |
|------|------|------|
| 2026-03-15 | Controller层学习、Service层分析、面试问题 | 第一章完成 |
| 2026-03-15 | VectorizationService向量化分析 | 第三章完成 |
| 2026-03-16 | ParseService三级切分逻辑分析、切分参数确认（512字符）| 第二章完成 |
| 2026-03-16 | EmbeddingClient批处理/重试、HybridSearchService混合检索 | 第四章完成 |
| 2026-03-16 | 建立docs/learning笔记体系，完成全流程文档化 | 文档体系建立 |
| 2026-03-16 | FileProcessingConsumer、ChatHandler、DeepSeekClient、WebSocket | 第五、六章完成 |
| 2026-03-16 | JWT认证体系、SecurityConfig、UserService、DocumentService | 第七、八、九章完成 |

