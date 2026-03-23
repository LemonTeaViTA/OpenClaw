# HybridSearchService - 混合检索服务

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/service/HybridSearchService.java`
- **触发时机**：用户提问时，ChatHandler调用
- **核心技术**：KNN向量检索 + BM25全文检索 + 权限过滤

---

## 🎯 一句话理解

> HybridSearchService = 「语义理解」+「关键词匹配」的双引擎检索
> 向量检索找「意思相近」的内容，BM25找「词语相同」的内容，两者取长补短

---

## 🗺️ 在整体流程中的位置

```
用户提问："RAG系统怎么工作的？"
    ↓
【ChatHandler】
    ↓
① HybridSearchService ← 当前文件
   KNN检索：找到语义相似的文档块
   BM25检索：找到包含关键词的文档块
   权限过滤：只返回用户有权看的内容
   结果合并排序
    ↓
② 把检索结果注入Prompt
"你是AI助手，基于以下文档回答：[检索结果]
用户问题：RAG系统怎么工作的？"
    ↓
③ DeepSeek生成回答 → WebSocket推送给用户
```

---

## 🔍 KNN向量检索 vs BM25全文检索

| 对比项 | KNN向量检索 | BM25全文检索 |
|--------|------------|-------------|
| 核心原理 | 计算向量余弦相似度 | 词频+逆文档频率 |
| 擅长 | 语义相似（同义词、换一种说法）| 关键词精确匹配 |
| 示例 | "AI趋势"能找到"人工智能发展方向" | "RAG"只能找包含"RAG"的文档 |
| 缺点 | 对专有名词不敏感 | 换个说法就找不到了 |

**混合检索 = 两者优势互补，召回率更高**

---

## 🔥 核心方法：hybridSearch()

```java
public List<EsDocument> hybridSearch(
    String query,          // 用户的问题
    String userId,         // 当前用户
    List<String> orgTags,  // 用户所属组织列表
    int topK               // 返回前K个结果
) {
    // 第1步：把用户问题也转成向量
    float[] queryVector = embeddingClient.embedSingle(query);

    // 第2步：KNN向量检索（语义）
    List<EsDocument> knnResults = knnSearch(queryVector, userId, orgTags, topK * 2);

    // 第3步：BM25全文检索（关键词）
    List<EsDocument> bm25Results = bm25Search(query, userId, orgTags, topK * 2);

    // 第4步：合并去重，RRF重排序
    return mergeAndRerank(knnResults, bm25Results, topK);
}
```

**为什么每个方法都查 topK*2？**
```
合并时会有重复，去重后数量会减少
所以每种方法多查一倍，确保合并后还有足够的topK个结果
```

---

## 🔥 knnSearch() - 向量检索

```java
private List<EsDocument> knnSearch(
    float[] queryVector,
    String userId,
    List<String> orgTags,
    int size
) {
    SearchRequest request = SearchRequest.of(s -> s
        .index("knowledge_base")
        .knn(knn -> knn
            .field("vector")           // 向量字段
            .queryVector(queryVector)  // 查询向量
            .k(size)                   // 返回K个最相似
            .numCandidates(size * 10)  // 候选集大小
        )
        .query(buildPermissionFilter(userId, orgTags))  // 权限过滤！
    );
    return executeSearch(request);
}
```

**numCandidates 是什么？**
```
KNN是近似算法（HNSW图算法）：
不是精确找最近的K个，而是从候选集中找

candidates = size * 10：先找100个候选
再从100个中精确计算距离，取最近的10个

候选越多 → 结果越准 → 但越慢
候选越少 → 速度越快 → 但可能漏掉好结果
```

---

## 🔥 bm25Search() - 全文检索

```java
private List<EsDocument> bm25Search(
    String query,
    String userId,
    List<String> orgTags,
    int size
) {
    SearchRequest request = SearchRequest.of(s -> s
        .index("knowledge_base")
        .query(q -> q
            .bool(b -> b
                // 全文匹配
                .must(m -> m.match(mt -> mt
                    .field("textContent")
                    .query(query)
                ))
                // 权限过滤（AND关系）
                .filter(buildPermissionFilter(userId, orgTags))
            )
        )
        .size(size)
    );
    return executeSearch(request);
}
```

---

## 🔥 buildPermissionFilter() - 权限过滤（安全核心！）

```java
private Query buildPermissionFilter(String userId, List<String> orgTags) {
    return Query.of(q -> q
        .bool(b -> b
            .should(   // OR关系：满足其中一个即可
                // 条件1：公开文档（所有人可见）
                Query.of(q2 -> q2.term(t -> t
                    .field("isPublic").value(true))),

                // 条件2：用户自己的文档
                Query.of(q2 -> q2.term(t -> t
                    .field("userId").value(userId))),

                // 条件3：用户所属组织的文档
                Query.of(q2 -> q2.terms(t -> t
                    .field("orgTag")
                    .terms(tv -> tv.value(
                        orgTags.stream()
                            .map(FieldValue::of)
                            .toList()
                    ))
                ))
            )
            .minimumShouldMatch("1")  // 至少满足1个条件
        )
    );
}
```

**权限逻辑：**
```
用户能看到的文档 = 公开文档 OR 自己的文档 OR 组织文档

示例：
用户A（属于TECH组织）搜索
→ isPublic=true 的文档 ✅
→ userId=A 的文档 ✅
→ orgTag=TECH 的文档 ✅
→ userId=B AND orgTag=SALES AND isPublic=false ❌
```

---

## 🔥 mergeAndRerank() - RRF融合重排序

```java
private List<EsDocument> mergeAndRerank(
    List<EsDocument> knnResults,
    List<EsDocument> bm25Results,
    int topK
) {
    Map<String, Double> scores = new HashMap<>();
    Map<String, EsDocument> docMap = new HashMap<>();

    // RRF公式：score = 1/(k + rank)
    // k=60 是经验值，防止排名靠后的文档得分过低
    int k = 60;

    // KNN结果打分
    for (int i = 0; i < knnResults.size(); i++) {
        EsDocument doc = knnResults.get(i);
        scores.merge(doc.getId(), 1.0 / (k + i + 1), Double::sum);
        docMap.put(doc.getId(), doc);
    }

    // BM25结果打分（叠加）
    for (int i = 0; i < bm25Results.size(); i++) {
        EsDocument doc = bm25Results.get(i);
        scores.merge(doc.getId(), 1.0 / (k + i + 1), Double::sum);
        docMap.put(doc.getId(), doc);
    }

    // 按总分降序排列，取topK
    return scores.entrySet().stream()
        .sorted(Map.Entry.<String, Double>comparingByValue().reversed())
        .limit(topK)
        .map(e -> docMap.get(e.getKey()))
        .toList();
}
```

**RRF（Reciprocal Rank Fusion）示例：**

```
文档A：KNN排第1 → 1/(60+1) = 0.0164
       BM25排第3 → 1/(60+3) = 0.0159
       总分 = 0.0323

文档B：KNN排第2 → 1/(60+2) = 0.0161
       BM25不在结果中 → 0
       总分 = 0.0161

文档C：KNN不在结果中 → 0
       BM25排第1 → 1/(60+1) = 0.0164
       总分 = 0.0164

最终排名：A(0.0323) > C(0.0164) > B(0.0161)
文档A在两个检索方式中都排前列，综合得分最高
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 为什么不直接用向量检索，还要BM25？ | 向量检索对专有名词（如"RAG"、"HNSW"）不敏感，BM25能精确匹配这些词 |
| RRF的k=60是怎么来的？ | 学术论文中的经验值，在实践中表现稳定。可以根据业务调整 |
| 权限过滤加在哪里？ | 作为ES查询的filter，在ES层面过滤，不是拿到结果再过滤 |
| topK一般取多少？ | 通常3-10个，太少上下文不足，太多超出LLM的context window |

---

## 🔗 相关文件

- [VectorizationService](../03-向量化/01-VectorizationService.md) - 前置：建立向量索引
- [ChatHandler](#) - 后续：注入上下文生成回答

