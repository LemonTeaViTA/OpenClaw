# RAG面试预测

> 来源：RAG面试预测.pdf

> 解析时间：2026-03-14 16:24:14

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 29

- **文件大小**: 40.60 MB


---


## 第 1 页


 泊聪明RAG面试题预测，31 道高频 Al 面试八股，1.2 万字 50 张手绘图，真吊打面试官

二请详细描述完整的RAG系统架构，包括主要组件和数据流向?

RAG 系统本质上要解决一个问题: 如何让 Al 能够基于企业内部的知识库来回答用户问题。所以整个架构设计围绕着-文件上传-文件存储-向量生成-答案生成"这条
主线来展开。

当用户上传文档后，我们首先通过 upload 接口来处理上传文件，并支持分片上传避免大文件传输问题。然后很关键的一点是，我们没有选择同步处理，而是把文件
处理任务和到 Kafka 的消息队列里，      完就能立即得到         长的处理
接口层面
oaccnurs拉叶               nio           eprecesangconsunaproeesamaeg
egepie认讼计                 Rssik人标记             六御央与由化冯理

poaaservce megechakslp二                   aa如Fleprocesangmaax

Uppagservce upuoaachuwgp 二         所有分上上人守成断

并发处理与消息队列

接下来是文档解析环节， Fileprocessingconsumer 作为 Kafka 消费者会异步处理这些任务。我们使用 Apache Tika 来解析各种格式的文档，比如 PDF、Word、
Excel 等，然后通过 parseservice 把文档内容切分成小段，这样做的好处是既能保持语义的完整性，又能控制向量化的粒度。

向量化这块是整个 RAG 系统的核心， Vectorizationservice 会调用豆包的 Embedding AP| 把文本转换成向量表示。我们选择把这些向量存储在 Elasticsearch 中，
主要是因为 ES 在向量检索方面的性能比较好，而且支持混合检索-

说到检索，这是 RAG 系统能理准确回答问题的关键我们实现了混合检索第略，既有基于向量相似度的语义检索，也有传统的关键词检索，这样能够在不同场景下
都有比较好的召回效果。特别重要的是，我们在检索时加入了权限控制，确保用户只能检索到自己有权限访问的文档

生威这块，我们集成了 Deepseek 大语言模型，通过 beenseekclient
到结果，而是可以实时看到 Al 的回答过程，体验会好很

后把这些文档作为上下文传给大语言模型，最后把生成的回答通过 Websocket
行多轮对话。

整个对话流程是通过 chathandler 来协调的，它会先调用检索服务找到相关文档，
实时推送给用户。我们还在 Redis 中维护了对话历史，这样 Al 能够理解上下文，进;

权限控制方面，我们实现了基于组织

等的多租户架构。通过 OrgTagAuthorizationFiter 确保用户只能访问自己组织内的文档，实现数据的安全隔离
总的来说，这套 RAG 架构的设计理念就是要在保证准确性的前提下，尽可能提升用户体验和系统性能，同时确保企业级的安全性。

2.在设计RAG系统时，如何选择合适的向量数据库? Elasticsearch、Pinecone等有什么区别?

首先说说我们为什么在派聪明中选择了 Elasticsearch。第一个原因是我们团队对 ES 比较热悉，第二个原因是 ES 的混合检索能力很强，上既支持传统的全文检索，也
支持向量检索，这对 RAG 系统来说是个很大的优势-

Nearestneighbor                      Vector





## 第 2 页


计的云服务，性能确实很不错，而且使用起来很简单，基本上开箱即用。但是有个问题就是成本，
安全和合规性可能是一些企业需要考虐的问

但是说实话，ES 在纯向量检索性能上并不是最优的选择。如果系统主要是向量相似度搜索，专门的向量数据库会更合适。比如 Pinecone，它是专门为向量检索设

特别是数据量大的时候，费用会比较高。而且作为云服务，数据

Post Processing
Query resuhts

d 三 时  固 <二| 属
Source Data            Application
\   Query
.汪" 一”|四四四四四
Vector
Embeddng      Embedding
Model

Vector
patobase

就我个人的体验来说，可以先用 ES 这样的通用方案快速验证业务价值，等业务稳定后再根据性能拒矣考虑迁移到专门的向量数据库。这样既能快速上线，又能控

制技术风险。毕竟 RAG 系统的核心价值还是在业务远辑和数据质量上，选择合适的就行，不一定非要追求最新最迷的技术。

3.RAG系统中的混合检索是什么? 如何实现?





## 第 3 页


第一阶段: KNN 向量召回

1ave 复制人
/am 风量召回有和
ntkn -> in
Head(cvectorn)
queryWecrortqueryuecter) // 坦询疝量
ktrecallg        /1/ 召回最 (topk ”38)
-numCandidarestrecallx) 。 1/ 保选所量

第二阶段: 关键词过泪

ja复制代本
7 才须击中关键河 季风
query(9 -，q-boole -
ausrtmsr -> gstmgtt
-trertf -> 丰baalbf -时
sheuld(sl -ys1tera(t -》 teld(vuserld-).valueuserDbla))) 1/ 用户机

本laldtrxextContent").querytquary))) 1/ 关键启区配

-ayoundfs2 -》 steratt -tfied(rpublic-)-valuettrue))) /公开文和
.should(s3 -》/” 组织各限“/)                          /1/ 组织要
D
六
第三个阶段: BM25重排序

java 复制代到
1 eas rescere 年排序
reaceretr
indoustzerecalat)
Coerytrg -> rq
eueryeiehtB.aa)         7 aa分瞄要重2ax
reaceregueryeight(1.6d) 1/ EBD5分数检重ex
-aoarytrqq -> raavmatchtm -> 昌
iueryauery)
operatortoperater nd) 1/ 严各关键词区本

六
)
六

具体的算法是这样的: 假设一个文档在适义检索中的得分是 08，在关键检索中的得分是 06，我们可以设置语义检索权重为 07，关键词检索权重为 03，那么最
终得分就是oara.7 ，6.6r6.3 -6.74。 当然这个权重可以根据实际效果来调整.

在此基础上，我们还加入了权限过滤的远辑。用户只能检索到自己有权限访问的文档，这个过滤是在检索结果合并之后进行的。

java 复抽代本
7 三种和邮访问虹式

shoula(s1 -》 sl.teratr -yt人ield(ruserld") .value(usergbd))) 。 // 自己的文簿|

shoula(s2 -》s2-teratt -cfield(-publtc")-valuettrue)))       7/ 公开文区

houla(s3 -》/" 和织民信权限 “/)                         1 组织六

4 .解释向量embedding的维度选择对系统性能的影响? 为什么我们选择2048维而不是384维?

首先，从模型能力角度来看，我们使用的是火山引擎的 doubao-embedding-text-240515 模型。 根据官方文档，这个模型的最高维度向量是 2048 维，支持 512、
1024 降维使用。我们选择 2048 维实际上是在使用这个模型的原生最高维度输出，这样能够最大程度地保留模型训练时学到的语义信息。

最大上下文
版本                         模型ID (ModellD)         模型能力                    长度            EN
(token)

doubao-embedding-               检察

text-250515                                                                       |             央                本
large-text-250515                支持中英文双语

extasog15             doubao-embedding-      向量检索                机
ext-                                                  本
large-text-240915           支持中英文双语
有             doubao-embedding-      文本向量化              本
                                                                                   和
text-240715                支持中英文双语
文本向量化

doubao-embedding-

text-240515       4k        2048
text-240515                       支持中英文双语

从语义表达能力来说，维度越高向量能够表达的语义信息就越丰富。2048 维相比 384 维有着显著的优势。高维向量能够在语义空间中更精确地区分不同概念之
间的细微差别，这对于 RAG 系统来说至关重要。

尿人”立夫应音吐苦直二两站




## 第 4 页


从技术实现角度，我们在 ES 的            中也配置了向量字段为 2048 维，使用 cosine 相似有

这个配置

和包的 embedding 模型完全匹配。

Paismart

Explorer                     elease Notes 。。 己 UploadControllerjava     1 nowledge basejson x
Y Folder                                                          癸
main                        mappings": {
javajcomjyizhaoqilsmartpa           properties*
vi                         fitend5":
java                     typ
/ectorizationServiceja                )}，
uls                             "chunkId
GenerateJwtKeyjava                     “type”
Jwtutilsjava
Logutilsjava
passwordUtiljava
忌 SmartpaiApplicationjava
resources
es-mappi                                :
1) knowledge_basejson                  "dims": 2648，
static                        indexn:
application-devy                         "sinitarity"
applicationyml                      】}
logbackcspring xml                    "aodetversion": 《

testhtml                                        en

语义漂移是 RAG 系统中一个非常关键的问题，简单来说就是随着时间推移，向量表示的语义可能

发生偏移，导致检索效果下降

Siage Onme:
Initially the sign (ima
presentation) isa

Elymology ed

he bird | al

reflection of basic reality

Srage Tivo

The sign masks a basic

reality. The image becomes

a distortion of re:

Srage IJree

The sign marks the absence
of basic reality The image call
into question what the reality
is and ifit even exists

Syage Foum

1 kangaroo ma                 The sign bears no relation

ee            to any reality whatsoever 让
2.waler strider

is its own pure simulacrum

在派聪明项目中
模型生成的。这样

我们采用了多层次的旬

策略。第一个层面是模型版本管理。我们在     中专门设计了 modelversion 字段来记录每个向量是由哪个版本
量需要重新生成.





## 第 5 页


id;

fiLeMd5;
chunkId;

>                                    textContent;

Vector;

modeLVersion;

UserId ;

orgTag;
isPubLic;

个层面是增量更新策略。我们不是一次性答换所有历史向量，而是采用渐进式的方法。当检测到某些文档的检索效果明显下降时，我们会优先对这些文档进行
点

第三个层面是混合检索的优势。我们结合了语义检索和关键词检索。即使语义向量出现漂移，关键词检索仍然能够提供稳定的基准效果。

6.在多租户RAG系统中，如何设计权限控制和数据隔离

首先，我们采用了多层级的权限控制架构。在用户层面，系统支持普通用户和管理员两种角色，管理
组织层面，我们设计了灵活的     系统，每个用户可以属于多个组织，并且有一个主组
(PRIVATE 用户名) ，确保用户有独立的私人空间。

有全局访问权限，可以管理所有用户的组织;
签。特别值得一提的是，系统为每个用户自动创建私人组

组织标签                                                             十 新增   C剧新 密列设置
标签名称             描述                        操作
aa           用村答只有和BR                   到 [辐]
aaua            天BA从和，自动人可所有着记P             CC] (]
~ ivangengs&A         且的了人给人用户本人和             CR [国]
Ah-           三-he                      ECIIO3
文档所有者，orgTag 标识文档所属组织，isPublic 标识是否为公开资源。

在文件上传
用户也能访问。

签自动为文档分配组织标签，确保数据从源头就有正确的权限标识。同时，用户可以选择将文档设置为公开，这样其他

文件上传                                                                    X

组织标签 *

是否公开*  公开 。” @@) 私有

标签描述 ” 。” 上传文件

取

，

证用户是否为资源所
源的组织标签时才多许访问。

ielease Notes       UploadControllerjava                                Logutilsja “    四





## 第 6 页


return;

resource0rgTag = resourceInfo.get0rgTag();

(resourceInfo.isPubticO) |
resource0rgTag           由

resource0rgTag.isEmpty() |
equaLs(resource0rgTag)) {
.debug(ms
fitterChain.doFitter(request，response);

return;

token = extractToken(request);
(token        )

在 RAG 系统的核心功能混合检索中，
腿访问的文档

了权限感知的搜索。系统会根据用户的有效组织标签构建 lasticsearch 查询条件，确保用户只能检索到有权

Ss.query(q -> q.booL(b -> b
must(mst -> mst.match(m -> m.fieLd(vatLue          ).query(query)))
.fitter(f -> f.booL(bf -> bf

.ShouLd(s1 -> s1.term(t -> t.fieLd(v           .VaLue(userDbId)))

.ShoutLd(s2 -> S2.term(t -> t.fietLd            .Value         ))

.shoutd(s3 -> {
话 (userEffectiveTags.isEmpty()
return SsS3.matchNone(mn -> mn);
eLse ji (userEffectiveTags.size()
return s3.term(t -> t.fieLd(         )] .vaLue(userEffective
elLse
urn S3.booL(inner -> {
UserEffectiveTags.forEach(tag -> inner.shouLd(sh2 -> sh2.tel
return inner;

可以修改所
议核实

间，比如说设置优先级规则，让检索到的参考信息优先

高于预训练知识，在遇到冲突时优先采用检索信息，无法确定时明确告知-存在|

汪息，并明交说明-要所最新检索信息
夭知识，介标注"补充基于通才知识
息间实，建该

首先是召回率 《Recall) ，也就是相关文档中有多少被成功检索出来了。比如用户问一个技术问题，实际上知识库中有 10 个相关文档，系

就是 70%




## 第 7 页


Precislongkc 前K个结果中相关文档的比例

和精确率”“| MAP Mean Average Precisionj: 平均精度均值

Hit Rate; 命中率
Recallakc 前K个结果中包含相关文档的比例

召回率”| MRR Mean Reciprocal Rank: 平均倒数排名

NDCGakc 归一化折扣累积增放

让分数。 FI-Score是精确术和召回的调和平均

平均精度均值 (MAP) 。。 计算所有查询的平均精确率

RAG评估指标

用户点击行为分析 。。 点击率、停久时间等指标的应用

用户反馈评估法”用户满意度调查 。 问卷设计与数据分析
A/B测试法对比不同检索策几的用户反馈

然后是精确率 (Precision) ，检索出来的文档中有多少是真正相关的。如果我们检索出了 10 个文档，但只有 7 个是相关的，精确率就是 703%6。

1 在 Waridsearchservice 中者加评估屯
Publec Evaluartomletrtcs evalware5earchtStrtng query，tistcSerlngy relevantDocIds，tnt
ape) 人

stcsearchesuaty results - searchiithperatssiontquery，userla， topgi

0 计量Precisionex
eng relevantCount - results stream0)
mtettopg
-aapTolong(result -，relevantDocTas-containstresult-getfilayds0) 3 1: 昌
ai
esble preclsion (double) relevantcount / math-ein人topt，results -size()

/计量 mecaleK
euple recall ”double) relevantount / relevantDocIas .stze()i

0 计生 NmR
ouble mrr = calculateyWRtresults，relevantDocTds);

Treesrn nen Emaluationletricstpracsiony racally mn)i

9.什么是RAG中的"幻觉"问题? 如何预防?

RAG 中的"纪驼-是指大语言横型生成的内容与检索到的真实信息不符，或者模型编造了不存在的信息。在派了明项目中，我们采用了多种第中来防幻问题

colonl

使用了混合检索第咯，

过提高检索精度来减少无关信息的二

10.如何设计置信度评分机制来判断检索结果的可靠性?

置信度是 RAG 系统用来保证检索质量的一个重要指标。所以要综合多个维度来考虑。





## 第 8 页


pepu

Ne Retreval

Knowledge 1 Andover US
USD 385 is a unified school district headl
mA     Ha
Knowledge 2: Pr
as        川Prnce isa census-de
yette County West Virginia_ United
lsus ts Population wi

States,      urb of
10 census the city population was
114.791                      knowledge 2: N
Knowledge 2: Andover USD 38             Mekvemisacityin
USD 385 isa unifed school distric

ned
an Amtrak station

Relevant | [ Fuly supported
Conf 993% WA: 11.791

Relevant | Parialy supponed

Conf 562% 汉A: 12,898    Conf 57.1% 汉A: 12.795

Rank 3
(2.56)

Rank1
03.48)

算查询向量和文档向量的余弦相似度，这个

是向量相似度。当用      ，我们利用 Elasticsearch 的 KNN 算;

说明文档和查询在语义上直

recaLLK = topK * 3
s.knn(kn -> kn
.fieLd(vaLue:
.queryVector(
.k(CrecaLLK)
.numCandidates(recaLLK)

是文本关键词匹配度。我们会利用 ES 球认的 BM25 算法对关键词在文档中的出现频率、重要性进行打分

s.query(q -> q.booLC(b -> b
.must(mst -> mst.match(m -> m.fieLd("textContent") .query(query)))
.fiLter(f -> f.booLCbf -> bf              ))

));

- 评分方式: BM25算法评分

一                       同时进行权限过滤

- 特上      t 查询                 ，fitter 查询不

Ss.rescore(r ->
.WindowSize(recaLLK)
.query(rq -> rq
.queryWeight(   )
.rescoreQueryWeight(   )
.query(rqq -> rqq.match(m -> m

.fieLd("textContent")
.query(query)
.operator(0perator .And)

系统中两种主要的文档分庆策略，"*"固定长度
对于计算资源

@param text

En         言|rNN                7 全全                eeal
ve city in which     人         村
Andover USD 3     located?                                 全 19040804                 Model Uncertain:

an altitude of 1.263 feet (385 m) tis served by

Relevant Pariaiy supported

映语义层面的相





## 第 9 页


语义分块会基于文档的语义结构来分害，比如按照段落、章节、主题来切分。这样能确保每个 chunk 包含相对完整的语义|
分块，对于结构化程度高的文档，比如技术手册、政策文件等，采用语义分块，充分利用文档的结构信息。对于结构化程度低的文档，比如聊天记录、邮件等，采

用固定长度分块，确保处理的稳定性。

String[] paragraphs = text-split(-wmwme)

utder currentchunk - nev Strtnglutlder(

hunks addtcurrentChunk .taStrdng()trta()
Careentci    StrangButlder(;

else af (currentchunk length() + paragraph_length() ，chunksize)

4 (currentchunilength() ，9) 人
hunks-add(currentchunkc toString()-tria))，

CurrentChunk -new StringButlder人paraeraphy

4 (correntchunk_lengthO) 是

Carrentchunk -appendtparaeraph，

Strtne[] sentences = parseraph-splitr(cc[。 1 9 ])1GcC5)Net

utder currentchunk - nev Strtnglutlder(;

Hor (String sentence :sentencea) 人

本(currentchunk.length() + sentence_length() 》chunkSize)
4 (currentchuniclength() ，9) 人
hunks-add(currentChunk toString()-tria)，

addhl(splittongSentence人sentence，chunksize))

mks addfeurrentchunk to5trinaly .tri

信息。我们打算在下一个版本中增加语义




## 第 10 页


esern chanksi

分烛起攻条子，按词界
rtvate Listcstrangy spltttongsentencetstring sentence， int chankstze) {
srcStrtngy chunks ”new hnraytistey人六
Strtng[] verds - sentence.splirrNvst

Strineautder currentchunk - ne Stringgullder();

Hor Gertng word :werde) 人
Searrentchunklength() 。 vondLlength() 。1 chumistze)
af (carrentchunk'length() 的
Chunks ,add(correntChunkcroString人.tria))
Currentchunk -new StrtngButlder();
1
了              )

4 (coreentchunk -length() ，晤
arrentchenk append(”
)

Cerrentchunk .appenatoord)i
1

if (currentchunk-lengtn() ，国
humks-add(currentchunk .tostrang().triaC)

1

earn hanksi

12.如何处理跨chunk的信息完整性问题?

最直接有效的解决方案是引入滑动窗口机制，在相邻 chunk 之间保持一定的重合区域。具体实现上，可以优化派聪明的分块去辑，设置 20-30% 的重亚率。例如,，
如果 chunk 大小为 512 字符，则每次移动 350-400 字符，保留 100-150 字符的重伏。这样能够确保被切断的信息在相邻 chunk 中得到保留，提高信息检索的完整
性。重登策略虽然会增加存储空间，但能显著改善跨边界信息的连续性。

站
使用草台曾口分宇
7
prtvare HiskcStringy splirTexkhtrhoverlap(strlg rext，lns chunkSize，tnt overlapSize) ff
srcstrtngy chunks = neo ArrayListeo()

》       7 百先进行分抽
srcstrtngy semanttcchunks - splitfextlntechunksttext，chunkSize))

7 漳加重星内容
or (int -85 1 < somenticchunks-size(; ieo)
SrringButlder chunktrhoverlap ”new Stringsutlder(;

7/ 漂加前一个chunk的结尾部分作为重双
2 91
String prevchunk -seaanttcchunks.gee(t - 1)
tring prevoverlap = BetLastNCharatprevChunky overlapsize 1 2
haniithoverlap.append(prevDverlap)-append(”
)

1/ 潭加当前chenk
hanktthoverlap -appendtsewanticChunks-get人7)

7/ 潭加下一个chunk的开头部分作为重双
4 (< samanticGhunks-size() - 1
Sring nexrChunk = semanticChunks.geri + 1
Srring nexroverlap = getFirstMCharstnextChunk，overlapSize 1 2)
haniitMoverlap .append(-“) .appendnextOverlap);
)

ns.addtchunitttoverlap_tostrtng())
)

了

，，13.多模态内容如何在RAG中处理?

多模态内容包含文本、图像、表格等不同类型的信息载体，每种模态都有其独特的信息表达方式和语义特征。文本承载概念性和描述性信息，图像包含视觉和空间
信息，表格则体现结构化的数据关系。

在 RAG 系统中处理这些内容的主要挑战在于: 不同模态的信息密度差异巨大，语义表达方式各异，以及如何在统一的向量空间中表示和检索这些异构信息。

派聪明目前支持 bt、PDF、Word 等文本内容的处理，通过 Apache Tika 来完成，

文件名                                                    文件大小 上传状态 组织标签                 是否公开 。。 上传时间
\

wangerbt                                           0.09K               已完成           管理员组织                  私有              2025-06-30

色。。 paismartpdf                             osak           已守成。 对认组织                型有          2025-07-02

国国国有

晶    简历0704.docx                                     1.44M              已完成           itwanger的私人空间        公开              2025-07-14

》。 Apache Tika 是一个开源的多格式内容分析工具，可以从超过 1000 种文件格式 (如 PDF、Word、纯文本等) 中提取文本内容和元数据(如作者、标题、创建时间
等)。




## 第 11 页


站
7月 [国

对于下一版的泊腾明，我人也打算追加图像、表格等内容的多模太支持。对于图像内容，可以集成 OCR 技术提取图像中的文字信息，同时使有图像指述模型(如
CUP、BUP 等) 生成图像的文本描述。对于表格内容，需要将其转换为结构化的文本表示，如 CSV 格式或者带有行列标识的|

14.RAG系统的主要性能瓶颈在哪里? 如何优化?

向量检索是最主要的瓶颈。当知识库规模达到几十万甚至上百万文档时，实时的向量相似度计算会成为明显的性能瓶颈。

>

embeclcling

Query | wWret is serverless <owput   |一会zwosoox-

Finel Top K
Boseol cn

felevonce

4nswer the aubstion base4 on this context;

Question;

优化方案包括; 使用更高效的向量索引算法，如 HNSW，HNSW 算法构建了一个分层的小世界图，通过高效的导航和连接节点，实现快速的近似最近邻搜索。它利
用图结构的优势，在多层次上进行跳跃和搜索，能      检索时间，

Vector Search
Hierarchical Navigable Small Worlds (HNSW)





## 第 12 页


也是一个重要拒预。用户查询|
豆包的向量 API，整体的体验我认为还是非常不错的

时需要实时生成 query 的 embedding，如果模型比较大，这个过程可能需要很长时间。派陪明目前调用的是

是一块大的性能开销，所以派聪明采用了流式输出的方式，让用户能够实时看到生成过

首先是知识入库阶段。我们不会在用户提问时才把所有文档都委给模型相反，我们会预先将所有的知识 (比如公司的规章制度、产品手册、技术文档等) 进行处
理。这个处理过程包括

1 将长文档切分成更小的、远辑完整的段落或"块"(Chunks) ;

。 2) 调用 Embedding 模型，将每个文本块都转换成一个数学向量，这个向量可以被认为是该文本块在多维空间中的语义坐标
引 将这些文本块和它们对应的向量存入向量数据库中，比如说 ElasticSearch

生成间淘内量

最生成成功

执行KNN报过

构建布尔查询

第一自重排序          执行纯文本搜索

用户自己的文档                                    所属组织文档              使用BM25耻法                        2 重排序权醒10              返回opk结果

其次是检索与生成阶段。当用户提出一个问是

，RAG 并不会直接把问题扔给 LLM。它会执行以下步村

派陪明当前采用了基于 Redis 的对话历史管理机制，每个用户都有一个唯一的会

D，所有的对话内容都按照时间顺序存在 Redis 中，并设置了 7 天的过期时间

get0rCreateConversationId(     userId) {
key =       + UserId +                  1

conversationId =          .opsForVaLue() .get(key);





## 第 13 页


if (conversationId
conversationId     .randomUUID() .toString();
.opsForVaLue() .set(key，conversationId，       .ofDays(   S 7)) 7
.info(format                  ，userId，conversationId);

.info(f                                 ，userId，conversationId);

return conversationId;

考虑到上下文会越来越长

我们打算在下一版实现一个滑动窗口，比如只保留最近 10 轮对话，或者根据 token 数

指代消解是多轮对话中的关键技术挑战，需要让 Al 理解'它-、*这个"、-那个"等指代词具体指向什么

派陪明的策路是

第一步，识别对话中的关键实体 【人名、地名、概念等) ，建立实体库。比如用户问"什么是机器学习
户说'它有哪些应用"时，能够识别"它-指的是"机器学习

统要记住"机器学习"这个实体。然后在后续对话中，当用

第二步，设计一个滑动窗口，重点关注最近 3-5 轮对话，因为指代关系通常不会跨越太远

根强的精确性要求，一个词蕊的差异可能导肥                       基于权威的法律文本，不能出现任何-创造性"的解矢。我们在回
答中强制要求引用具体的法条和案例，并且会标注信息来源的权威级别。对于模糊的问题，系统会明确建议咨询专业律师，而不是给出可能误导的回答

的挑战主要在于专业术语和安全性要求。RAG系统绝对不能给出具体的诊断建议或治疗方案，因为这涉及到医疗执业资格问题。我们在系统设
围，只提供医学知识科普，对于任何可能被理解为诊疗建议的内容，都会自动添加免责声明，建议用户咨询专业医生

完全不同的法律后果。所以法律意见必须

限制了

面临的主要挑战是数据的实时性和准确性要求。金融市场变化很快，昨天的数据今天可能就过时了。所以需要建立实时的数据更新机制，对于价格、汇率
等高频变化的数据，要标注明确的时间玲，提醒用户数据的时效性.

另外要

答中明确标注风险提示，说明这只是|

息查询而非投资建议。对

在设计派聪明 RAG       时，我首先会遵循几个核心的设计原则，确保 AP| 清晰
第一，一切以资源为中心。我会把系统的核心功能抽象成资源，比如知识库' (Knowledge Bases) 、文档 (Documents) 、'对话 (Conversations) 等等。然后
的 HTTP 方法，像 GET、POST、DELETE，来对这些资源进行操作

raer

redisTemptate，

Conversationcontroleriama

Tene                             username = jwtutits.extractusernameFromTokenttokenreptacef

Casernan      sernane_isEnptyC)) {

aen                                                       CustomExcaption

第二，我在 URL 里了加上版本号，比如
好。

的好处是，未来系

升级，推出新版 AP| 的

全，不会影响到正在使用旧版接口的用户，兼容性会非常




## 第 14 页


格式都应该是统一的JSON    比如都包含 code、message 和 data 这几         册或者其他调用方处理

回 rssnon

Explorer                                                  Comersationcontolerjaa 。。 」 ResponseEntgrclass x

Faer
8。 pubtie ctass RasponseEntitycTy extends MttpEntityery

rivate finat httpstatuscode status

webcientconfgiamn                                         param

websocketconfi av                    pubtie            netpstatvscode
               um

ouaine

                                                     paran

ResponseEntiyltpstatusCodel                              7

pubte            Cutuabte       etpstatuscode

etstatuscodel

aoastobiec

hashcode0                                                        2

tostane0                                                 2

oa0
本

Taine
av Projects

waven                                                         paran

20.RAG系统中如何保护敏感数据?

在派聪明中，我们通过 Spring S    NT 实现了基于 RBAC 的权  系统。当用户提问时，系统会根据用户的角色权限和组织标签，  索时自动过滤掉无
访问的数据

[TOTTTTT)
pubtic Map<String，0bject>          (@RequestParam String
@RequestParanm(
@RequestAttribute(
LoguUtits.PerformanceMonitor       = LoguUtits.
try 工
Logutits                         SEARCI

opK=%
List<SearchResutt>
证            1= nutLL

hybridSearchSservice.

hybridSsearchService.

LoguUtits.                  != nutL ?      0           "HYBRID_SEAR|
t:"SUC

LoguUtits.                     HYBRID_SEARCI                           anonymous"，

出时，采用 HTTPS 的加密方式，没有密钥是无法

LocaLhost





## 第 15 页


21.如何进行A/B测试来优化RAG效果?
AVB 测试的策略可以分为三个核心部分: “测什么“怎么评"和-如何做" 。

目标人群
ELSE
[

了                                                          +
50% 用户                                  50% 用户

[|e83a
|

         应用

汉
| 可 4 四   示

测什么阶段我们需要明确测试的实验变量，比如说派聪明中有一个服务叫混合检索融合了语义检索和关键词检索，那我们就可以测试不同的融合权重。比如，A
组是6.5 ”vector_score + 9.5 ”bm25_score，B 组可以是 6.7 ”vector_score + 6.3 * bm25_score，看看哪个组合更能命中用户的真实意图。

再比如说我们可以测试不同的文档分块策略，是 500 个字符还是 400 个字符还是有一部分重梧字符，看哪种第路能产生最恰当的上下文片段。
冥包，看哪个模型的回答更流轧、更准确、更能地和指令。

还有，我们可以对比不同的大模型，比如和组用 DeepSeek，8 组用通义二

有了实验目标后，我们需要一套科学的评价体系来判断"谁优谁劣-。 比如说我们可以在每个回答后面加上-*顶/中按钮。A/8 测试的核心目标就是看哪个版本的"顶
率更高，足率更低-

如果你希望突出某一技术细节 (比如 Kafka、AOP 实现细节)，可以进一步加深技术点描述。
口中上四 内

后，我们需要通过技术手段来支撑整个 A/B 测试流程。比如说当一个请求进来时，系统会根据用户 ID 或会话1D，通过哈希等方式，将用户稳定地分配到 A 组或

8组

一旦 8 组被验证为更优，我们再进行小范围的灰度发布 【比如，先切 10% 的流量到 B 组) ，观察系统稳定性和核心指标。确认无误后，再逐步将所有流量切换到新
版本，并最终下线旧版本-

22.GraphRAG与传统RAG有什么区别?

GraphRAG 是对 RAG 的增强，通过整合知识图谱中存储的结构化领域知识来增强检索，借动知识图谱中丰富|
的局限性，并提供更准确、更易于解释的查询响应。

Question

连接和语义关系，GraphRAG 可以克服纯向量 RAG

>

Instruction |-………-->| LELM |->| Answer

>

CE

SearchT
h
350   LV   Leuer 】

和   四

Graph Database





## 第 16 页


传统的 RAG 知识库本质上是一个"文档集合"。无论是 PDF、Word 还是网页，我们都将它们切割成一个个独立的文本块，然后对每个块进行向量化，存入向量数据
库。

GraphRAG 的核心是"知识图谱-。在数据预处理阶段，我们不仅仅分块，还会利用大模型从文本中提取出实体 (Entities) 、关系 (Relationships) 和属性
Attributes) ，然后将它们构建成一个图。比如，从-沉默王二吹了一个牛通*这句话中，我们可以抽取出 《实体: 沉默王二) - [关系: 吹了] -> (实体: 牛副) 这
样的结构。这就把零散的知识点编织成了一张巨大的、相互连接的知识网络-

Document Chunking
Element Extraction         awayaaag            User provided

硬-

Realahionship Linking                                                                 Medical papers
                                                             到Books
@。
e e 一-一
Medical
Cluster the Meta-graphs

a. MedGraphRAG Pipeline                                            b. 3 Level Hierarchy Linking

在检索阶段，传统的 RAG 是基于语义相似度的。就像我们在派陪明中做的那样，将用户问题向量化，然后在向量数据库中寻找与之最相似的文本块。

GraphRAG 的检索变成了在知识图谐上的图追历或子图查询 。当用户问'沉默王二吹的牛吉是喻? "时，GraphRAG 可以:

。 第一跳 :在图计中定位到-沉默王二-这个节点
， 第二跳 : 沿着吹了这条边，找到"牛通节点。
再从"牛表-节点出发，找到* 26 万订阅号读者*、"GiHub 14000+ star等内容。

23.对RAG技术的未来发展有什么看法?

未来的 RAG 将是多模态的。图片、音频、视频、代码、表格、APL.…任何信息形态都可以被索引和检索。到时候，我们的提问可以是“这张图里穿蓝色衣服的人在
做什么2“

和reaitonat eaa vs Huc             名 omeawoouofos om





## 第 17 页


Response

24.如果RAG系统返回0个检索结果，你会如何排查问题?

首先，我要确定这是特殊情况还是普遍现象。如果所有的提问都无法检索到结果，那很可能是系统级的故障，比如向量数据库连接失败了、索引被误出了、或者向
量 AP| 服务宕机了。如果只是特殊情况，那么问题很可能出在数据处理、查询理解或召回策略上。比如，用户问了一个知识库里完全没有涉及的领域，或者查询的
关键词过于生信-

接着，我会检查召回的候选集数量 k 是否设

得过小，导致过滤条件区加后没有结果。
权限也需要排查。可能是用户的权限不足，无法访问相关文档。

25.如何处理不同API服务 (豆包 embedding、DeepSseek) 的调用失败?
在调用豆包向量 AP| 失败时，我们会自动回退到纯文本搜索，实现服务降级，确保检索服务可用。

public HiatdgepcString，Objecty》 searchiithgersission(String quary。 Strine wserTd， int siae) {

areh 《EnbeddingServiceException ej
egser-varn(-疝时务不可用，降维到文本扫索:人}"，e-Betyessage())
resurn textnlySearchtquery，userTd，size)

Ca aasticaaciicagtian 四下
logger error(-搜过最务呈常人
Treesrn collections-emptytiat()

sara，size)

etbessage()

并且在调用豆包向量 AP| 时，我们采用了 Reactor 的重试机制，支持固定延迟重试 3 次，并设置了 30 秒的超时保护。

componen

renbeddings)

oayvalue(requestBody)

bodyTokenetstring class)

retryuhentRetry -backoff(3，Duration-ofsecendst1))
axBackofftDuration -ofSeconds(19))

alter人shisssasRetryableException))
dmeoutfDuration ofSeconds(38))
lockOi

《GepclienshesponseException) ex)-BatStatusCoda()-isSuxServertrrer(

下个版本中，我们打算接入更多的大模型 APl，当 DeepSeek 不可用的时候，能够自动切换到豆包、文心
快速切换到本地的模型服务

壬讯混元、阿里通义千问等。派脱明目前已经支持

26.请说说你AlGC、RAG、Agent 的理解?

AIGC，全称为 Al Generated Content，意为-人工智能生成内容*。它指的是利用人工智能技术自动生成文本、图片、音频、视频等多种内容的过程。2022 年 11 月
30 日，OpenAl 基于 GPT-35 的 ChatGPT 正式上线，引爆了 AIGC 热潮。

允 一一PT re | cc 系统

vcd

RAG， 是一种格信息检索 (IR) 与大型语言模型 (LLM) 的文本生成能力相结合的技术。其核心思想是: 当 LLM 需要回答一个问题或生成文本时，不是仅依赖其
内部训练时学到的知识，而是先从一个外部知识库中检索出相关的信息片段，然后将这些检索到的信息与原始问题/指令一起提供给 LLM，让 LLM 基于这些最新、
最相关的上下文信息来生成更准确、更可靠、更少幻觉的答案

模块




## 第 18 页


朴素RAG                                       进阶RAG，                                                      模块化RAG
Naive RAG                        Advanced RAG                                     Modular RAG

Agent，也就是智能体"，在计算机科学和人工智能领域指的是一个能够感知环境、自主决策并采取行动以实现特定目标的实体或系统。它可以是软件程序、机器人
硬件，甚至是生物实体 (如和类或动物) ，但在 Al 领域通常指软件智能体-

Agent 和 AIGC 最大的区别:

，。 AIGC 主要以生成式任务为主，而 Agent 是可以通过自主决策能力完成更多通用任务的智能系统。
。 常见的 AIGC 系统(文生文，文生图) 的核心就是一个生成模型，而 Agent 是一个集 Function Cal 模型、软件工程于一体的复杂系统，需要处理模型和外界的信息交互。
，。 Agent 可以集成 AIGC 能力完成某些特定的任务，也就是 AIGC 可以是 Agent 系统里面的一个子模块。

也就是说，Agent 最大的特点是，借助 Function Call 模型，可以自主决策使用外接的一些工具来完成特定的任务。
27.那什么是 function call 模型?

Function Calliing，也就是函数调用， 是大型语言模型的关键技术。RAG技术是为了解决模型无法和外接数据交互的问题，但是 RAG 的局限在于只妖予了模型检
过数据的能力，而 Function Calling 允许模型理解用户请求中的潜在意图，并自动生成结构化参数来调用外部任何函数/工具，从而突破纯文本生成的限制，实现
与真实世界的交互，比如可以调用查天气、发邮件、数学计算等工具。

Function Call 模型最旱由 OpenAl 在 2023 年 6月 13 日提出并发布，首次在 GPT-4 模型上实现了 Function Caling 能力。

生有结构化参数              执行外部本数              结果返回LUN              生万最终回复

用户输入            Luw电析理图

理_。。 直接文本回复

Function Call 需要先定义函数，向 LLM 描述函数的用途、输入参数格式 (JSON Schema) :

java 复抽代表
{

aaer: "aet_current weather

-aescriptienr: “获取指定城市的天气"…，

Parameterers 人
Cepery "oblectr，
preperttesr: 人

reters
ypers “sr
escrtpron'，

拓市各褒-

realsaus"，"fahrenneirr]

要
Teauarety [am

了
)

当用户提问"北京今天需要带们吗?“
一 LUM 识别到意图需要调用 get_ current_weather
一 并生成结构化参数:frcity"; "北京"'，"anit"; "celsius

然后执行 get_current_weather 函数调用天气 API，获到真实数据:《"tenp"; 25，"rain_prob"; 3e%} ，然后将结果交回LUM，生成最终回复: “北京今天25"C，降水
概率30%，建议带补。

那也就是 OpenAl 发布 Function Cal 模型后，Agent 才开始迅速发展。Agent 真正进入到公众视野，被大家广泛关注的事件是 2025年4月 Manus 发布的通用智能体
产品，引入了 Computer Use 和 Browser Use，首次展现出智能体的强大能力。





## 第 19 页


| 生成模型 | 重新生成recuest，| 工具结果加 ]
| request  再次调用模型“| 入历史记录

调用障型

了让 call

Im

<用、 是         | 工程测调用|
工具调用-                      工具

~纪站|

MCP，是 Model Context Protocol 的缩写，也就是模型上下文协议，由人工智能公司 **Anthropic

正式发布并开源.

MKCP 协议旨在解决大型语言模型 (LLM) 与外部数据源、工具间的集成难题，被比喻为"Al 应用的 USB-C 接口"。通过标准化通信协议|
即多个模型与多个数据源的点对点连接) 转化为-M+N模式*，大幅降低开发成本。

统的"-MxN集成问是

Using MCP for Tool calling

    Protocol

Unique API Unique APIUnique AP Unique API

|    |    |
全     |     人                                          Unique API Unique API Unique AP Unique API
1           | 1    |    |

Tools       已 4 o

MCpP自





## 第 20 页


AcA ，即 Agent-to-Agent ，后因赴一种夭珊宁何，具本刘多下焉业鸭、豆| Ji Agent 进人行动LTF ，以元成芋下 Agent 乃好于罗更旺瑟国信六。
单个 Agent 就像是一个全能的"通才"，他什么都伐一点，但可能没有哪个领域是顶尖的。

A2A 就像一个专家团队，有项目经理、数据分析师、文案专家、软件工程师等。项目经理负责拆解任务，然后分发给最合适的专家去执行-

1 WACP vs. 站2启 protocol | wpoeomseon

IACP Host

一个 Agent 要能解决问题，首先需要获取准确的信息。RAG 可以作为这个 Agent 获取和理解信息的核心工具之一<

User                                            Client                  E                                    Remote Agent 2

Remote Agent 3

AZA 架构的优势在于每个 Agent 都可以专注于一个特定领域(如代码执行、数据库查询、AP| 调用、文案写作) ，使得开发、测试和维护更加简单。

30.了解Transformer 吗?

Transformer 是近年来深度学习领域，尤其是自然语言处理 (NLP) 中，最具革命性的模型架构。它奠定了所有现代大型语言模型 (LLM) ，包括 GPT、BERT 等的基
而

Transformer 最初是为机器翻译任务设计的，所以它有一个经典的编码器-解码器(Encoder-Decoder) 结构。

our
Transformer




## 第 21 页


四-加

INPUT

AreyouOK?

GPT 本质上就是把 Tansformer 的 Decoder 部分拿出来，进行大量的预训练

在 Tansformer 出现之前，处理序列数据 (如文本) 的主流模型是 RNN，它的工作方式像人阅读一样，一个词一个词地顺序处理，并试图通过一个"记忆单元"来记
住前面的信息。

RNN 的问题是必须处理完前一个词才能处理后一个词，这在硬件 (GPU/TPU) 飞速发展的当下阶段，极大地限制了训练速度。并且当句子很长时，RNN 很难记住
最开始的信息，会出现'遗忘'现象

Transformer 完全失弃了 RNN 的循环结构，提出了自注意力机制。

对于一句话中的每一个词，自注意力机制都会计算这句话中所有其他词对这个词的"重要性或"相关性"得分。然后根据这个得分，将所有词的信息加权融合，生成
这个词在当前上下文中的新表示。

比如说在"派联明是一个企业级的 RAG 知识库，它是由沉默王二的团队研发的"这个句子中，自注意力机制能够识别出"它"指的是派聪明，而不是沉默王

Transformer 通过位置编码感知单词在句子中的位置顺序。位置编码是一个与词向量维度相同的向量，通过数学公式正弦和余弦函数) 生成，包含了单词在序列
中的绝对或相对位置信息。在输入模型前，它会和词向量相加，让模型知道每个词的位置。

模型推理结果:
人工标注数据: y
误差: loss(y 让

在 RAG 中，最后负责整合检索到的知识并生成答案的那个"生成"模块，通常就是一个基于 Transformer 的大型语言模型。而用于将文本块转换为向量的模型，也都
是基于 Transformer 的 Encoder 结构训练出来的。

31.在做检索时，你是否尝试过或了解过其他的重排 (Re-ranking) 方法?

我们考虑过一种轻量级的重排方法
排名靠前，那么它应该更重要。

倒数排名融合 〈RRF) 。它是 Milvus 混合搜索的一种重新排名策略，核心思想是，一个文档如果在多个不同的召回列表中都

抽                                                      攻E                     [Eee
让             ai                         攻
一                本                      车
                   二
站as
三

具体来说，我们会分别从向量检索和关键词检索语到两个排好序的文档列表。对于任何一个文档，我们计算一个 RRF 分数，公式是1 / (k + ranki) + 1 1 (k +
ranka)，其中 rank1 和 rank2 是它在两个列表中的排名(如果不在某个列表中，则该项为0) ，k 是一个小的平滑常数比如60)。最后，我们根据这个新的 RRF 分
数对所有文档进行最终排序。

另外就是大模型重排，将召回的 Top N 个文档块的内容，连同原始查询一起，通过一个精心设计的提示词全部提交给 LUM。这个 Prompt 大臻会是这样:

查询 : [用户的原始问题|




## 第 22 页


》

文档列表 :
攻档人1: [文档1的文本内容]
文档21: [文档2的文本内容]

任务 : 请根据以上文档与查询的相关性，对文档进行重排，并以JSON 格式输出排序后的文档素引列表。
然后，我们再解析 LLM 返回的JSON 结果，得到最终的排序

人曙
一一           47人点届              一一

生昌国月@ 伟业日

加                                                                                                o2 大醒

热站评论 划

访m                                                                                                  onewoanB ios4

有7个是相关的，

| mms amanexar ofzm，

@派联明，相关性是大部分功能进行判断相关的
由总革 用日R5

Ti                                                                                                                              026和0月1日1056
在RAG系统中，文档相关性判断主要通过以下核心机制实现:
1 混合检索第路 《核心功能)

。 语义检索: 基于向量相似度《如余弦相似度) 判断语义相关性。例如，用户问"提升工作效率"，系统会下本语义相近的文档(如-优化工作流程
。 关键词检索: 通过BM25莽法计算关键词配度，确保精确术语《如技术和名酒、人名) 的召回.

， 加权几合: 结合两种检索结果，按权重计算综合得分 (如 最络得分 -Port分数"0.3 + By分数1.0 )。

2 置信诬评分机制

， 向量相似订阅值: 设置相似度下限 (如07) ，过沁低相关文档(参考资料第10节)。

。 BM25重排序: 对候选文档进行二次评分，确保关键词配高的文档优先级更高(参考资料第3节)。

3 权限过泪

， 通过"标签 ( -rrrag )、用户ID 〔 acerza )、公开标识【 ispuablic ) 过泪无权限访问的文档，确保结果与用户相关(参考资料第6节)。
4 人工标注评估(准确性验证)

， 情确素 【Precision@K : 如检索10个文档中7个相关，稍确素-703% 《参考资料第8节)。

。 召回率 (Recall@kK) : 若知识库实际有10个相关文格，仅召回7个，召回率=7034,

。 实际震人工标注 zlevannccrds 作为基准，通过代码计算:

7/ 计划 《示的)

aeepml

LeapTereeglz -yselevanroocraaveonratnslrcgesralosas011 3 1 1
La

esie preetatea = (deublel salewansceame 1 sepwi

复员人到

关键点总结

自动判断: 信人检索的加权融合和置信度间值过站低相关结果。

， 人工验证: 通过精确率/至回率评估系统准确性，需人工标注相关文档[D作为参天

， 优化方向: 调整权重、提高向重维度 如2048维)、优化分块策略可提升相关性 (参考资料第4、11节) -

出上 用卓

字
达

026征03朋1日 1059

召回率是指检索到的文档占全部文档的比例。 精确率是指召回文档中相关性文档占的比例，对吗

在RAG系统中，文档相关性判断主要通过以下核心机制实现;4#4# 1. “混合检索第路 核心功能) " - "语义检索": 基于向量相似度〈如余纺相似度】 判断滞
出 用上昌E
Ti                                                               12026年月1 1059

您的理解基本正确，但需要更精确的表述:




## 第 23 页


召回素 (Recall) : 指检索到的相关文档占全部相关文档的比例

， 公式: 召回率 = 检索到的相关文档数 /全部相关文覆

。 反映系统找出所有相关内容的能力

精确率 【precision) : 指检索到的文档中，相关文档所占的比例

。 公式: 精确素 = 检索到的相关文档数 /检索到的文档总数

。 反映检索结果的相关性质量

您的表述中需要注意:

1 召回率不是"检索到的文档占全部文档*，而是,检索到的相关文档占全部相关文档-
精确率中的召回文档"建议改为检索到的文档-更准确

这两个指标通常坑要权街，高召回率可能带来低精确率，反之亦然

召回率是指检索到的文档占全部文档的比例。精确率是指召回文格中相关性文档占的比例，对吗
出5向 国旧和

镶岂                                                                        onewoamnB io
结个合子。比加返回了10个文档，相关的有7个。全部文档是20个。畏确率，吾回率多少

您的理解基本正确，但坟要更精确的表述: “召回率 【Recal) “:指检索到的~"相关文档”"占~"全部相关文格"*的比例 - 公式: 召回率 - 检索到的相关文档数

》

出从 国旧和

026征09月1日1102

。 知识库"有20个相关文档
， 系统检索返回10个文档

。 其中1个是真正相关的|

和精确率(Precision) = 7110 = 70%

。 表示返回的10个文档中，70%是真正相关的

召回率(Recal = 7120 = 35%

。 表示知识库中所有相关文格的35%被成功检索出来

3析:

。 精确束高但召回率低，说明系统很送慎，返回的都是高时信度结果，但沁掉了较多相关文档
。 可通过调整召回网值来平衡两者，提高召回率可能会了低铺确率

。 实际应用中需根据业务场景选择侧重点

给个例子。比如返回了10个文档，相关的有7个。全部文档是20个精确率，召回率多少
出5划 国晶

10 条评论

图 mc                                                                                     ozewoamnaa aoos

引用原文: 只保留最近 10 轮对话

具体应该保丰多少轮对话，这个怎么设置@泊聪明
出上间 国昌1

Ti                                                                                                                              026和0月1日 2006
在RAG系统中，对活管理的核心是平衡上下文完整性和性能开销"*。以下是具体设置方法及优化策路:

工 国定轮数控制(当前方案)

配置方式:

>                 在Redis中存储对话记录时，按用户会话ID (如 sac:usex123 ) 维护列表，仅保留最近N轮对话 (如10轮) 。
示例代码加

7/ 二和dh的"忆
asscsrrdagy htaery = radarenglasevopsgcratasll -rangelrchaciaserl2av， 0 -1
>

atarenplase-epagorlaat 0 .ertalrchatroseri23n，- -1 1/ 全加
1)
复审人到

2

， 为什么是10轮?
， 经验值: 10轮对话通常能可关多轮交互的核心上下文，同时避免token超限 【LUM上下文窗口有限)。
， 性能优化: 减少每次请求传递给LLM的"数据量，降低推理下。

.动态Token控制 (推荐优化方案)

实现到加

根据LUM的上下文窗口(如DeepSeek支持32K token) ，动态计算可容纳的…轮数-
志村:

直统计每轮对话的平均token消耗 (如用户问题59+okeney |右答200 tokens)。




## 第 24 页


2 设定安全辐值 (如保留总token < 25K)。

3 每次新对放时，移除超出半值的记录。
示例

》

as earrensrokeaa = calcalaseresalrokeasfhtasergly 1 计有当间-昌caren
ae earee                     ee 1

7 1/ 和天昌的-花

1)
复制人到

，优区:
， 更录活适应不同长度的对话 (如复杂讨论需更多上下文)。
， 过锡因定轮数导致的上下文吉断或资源浪费。

3 关键优化点
优先级第路:
着寺匀，优先保留用户最新指令和关键回答"，合记作内容-
* 语义压缩:
对长对话进行摘要 《如用LLM生成”对话的摘要) ，仅保留摘要+最新1-2轮完整记录。
， 领域适配:
* 法律/医疗领域: 增加轮数 (如15轮) ，确保细节不丢失。
。…场: 减少轮政《细05轮) ，提升只应速度.

4 配置建议
场最                                   推基轮                      Taken届值                       才用系统
通用知识问答                           0                        15k25k                         企业内部知识库
复亲技术讨论                           1只                      okaok                         质术到持发甸作
Sm                                 3                         Tokrnsk                         用户服务系统

提示:通过A/8测试验证欠数设置《如对比10轮 vs 15轮的-项/吧"齐) ，选择最优值，

总结

。 基础方案: 固定10轮对话，简单高效〔如涛聪明当前实现)

， 过内方案: 动态Token控制，更知能笑应场最需求-

。 扩展优化: 结合语义压缩或优先级第路，在有限上下文中最大化信息价值_
出5全 用日

图 ws                                                                                     aaso有8 no5

引用原文: 最终分数 = KNN分数 x 02 + BM25分数 x 10

BM25分数占比1009%6踢@泊聪明
由s 几昌1

Ti                                                               026和03朋13日1953
亿观认得非常准确! 参考资料中描术的“最终分数 = KNN分数 x 0 2 + BM25分数 x 10" 确实存在明显的权重失竺问题。以下是具体分析和建议:

问题分析

1 权重分配不合理

。 BM25 分数权重为 10 《100%6) ，而 KNN (向量相似度) 权重仅 02 (20%) ，这意味着是终结果几乎完全依厅关键词匹配 (BM25) ，向量检索的语义相关性
被严重弱。

， 这违背了 混合检索 的核心目标: 结合语义检索 (KNN) 和关键词检索 (8M25) 的优势。

技术这辑矛盾
， 车 BM25 权重占绝对主导，KNN 的存在意义被大机弱，系统退化为细关键词检索，无法解决语义模交问题(如-提升工作效率'下配-提高生产力")。

合理优化建议
1 调整权重平衡
建议采用更均街的权重分配，例如:

= ng糙 0.5 ， aaa5烤0 .5 stsov
复员加

或根据实际效果动态调整 如KNNx07 + BM25x03)。

增加相似度闻值过涉
。 对 KNN 结果设置 相似订阅值(如 > 07) ，过汽低相关性结果，避免现声干扰
。 示例代码〈伪代玛) :

1 maseore < 9.T) zecarai 1/ 过质量间申果

复提代码

3 分阶段重排序优化
第一阶段: KNN 召回 Top 30 候选集《保留多样性) 。




## 第 25 页


， 槛二队段: 用 BM25 对候选集重排序 (如参考资料中的代码) ，但需调豆 sharyisighr 和 rsscorscoeryweight 为均壬值(姑0505)-

为什么当前设置可能存在?

1临时调试方案:可能是测试阶段临时设置，用于验证 BM25 的主导作用..

2 特定场最宽求: 若知识库术语高度标准化(如医疗、法律) ，关键词匹配可能比语义检索更可
3 描述误差: 原文可能存在笔误，实际权重应为02和08 (非 10).

当前公式 KNNx0 2 + BM25x10" 了混合检索的平衡性，建议调整为 05.0.5 或动态权重**，并增加相似度过小。真正的混合检索应让语义和关键河优势豆补，而
非单方面依肝。

出5 用四

026年03朋1日13223
而是模型版本管理。我们在 EsDocument 中专门设计了 modelversion 字段来记录每个向量是由哪个版本模型生成的。

这里意思是因为模型不行而导至的"语义信物"问是的产生吗?所以发现 -语义信移"时候加更新模型，然后重新生成向量? @泊肌明
由六”国 旧

Ti                                                               12026年月1日1323
不是完全因为-模开不行"导致的语义偏移。语义漂移是RAG系统中随时间推和的自然现象，即使模型本身是好的，随着知识变化和模型演进，向量表示的语义也会
发生仿移-
针对语义洒移，我们采用增量更新策咯而非简单更新模型:

1 只对检索效果明显下降的文档重新向量化

2 通过modelversion字段亿路向量来源，精准定位需要更新的部分

3 采用渐进式方法，间免一次性替换所有"向量

这种精细化的处理方式路能解决语义洒移问题，又能有效控制计基成本-
册5 国旧

图 ms                                                                                assoaiaa toan
不更新模型版本的话，同一个句子在两个时间点进行向量化，结果不一致吗?

不是完全因为,模型不行"导致的语义偏移。语义漂移是RAG系统中随时间推和的自然现象，即使模型本身是好的，随着知识变化和模型演进，向量表示的语义
出汪 国日

Ti                                                                                                                              026和0月1日1932
即使不更新模型版本，同一个句子在不同时间点向量化结果可能不一致，主要原因包括:
二模型内部状态的非确定性

。 部分深度学习模型(如Transformer) 在推理时可能包含非确定性计算 (如Dropout、随机初始化等) ，即使输入相同，输出也可能因内部芋机杖坊不同而咯有差
异

， 尼例: 豆包的Embedding模型若示显式设置确定性模式，同一文本的向量可能存在微小浮动.

2 输入预处理差异

， 文本预理步圣(如分词、大小写转换、标点处理) 若未严格标准化，可能导致输和表示不同，进而影响向量结果.
， 示例: 句子 -As greatr 着被处理为“ai is great (小写+去标点) 与原句，向最化结果可能不同。

3 计算环境或椎哥版本变化

。 不同时间点的计算环境《如CUDA版本、PyTorch杠架更新)可能影响数值精度，导到向量结果存在微小差异。

， 示例: 升级Pyiorch版本后，同一失阵委法可能因旗层优化算法不同产生不同光点结果。

4 模型权重微调 (未发布版本)

。 即使未发布新版本，模型可能经历未公开的内部微调或参数调整，导致入出漂移。

示例: 团队在训练过程中调攻了正则化参数，但未更新版本号，导至向量生成结果变化-

解决方案(参考RAG系统设计)
1 显式设置确定性模式

在调用Embedding AP时，强制模型关闭随机性(如设置 :==-' )，确保相同答入产生相同答出-

 示全有名xpz时设本定性

esponae = cbeadaag_sp: -geaeracel
err同-9
sermtateserrros 关键娄|

复审人到

标准化预处理流程
固定文本预处理规则(如统一使用 ji abs 分词、保留标点、小写转的等) 确保答入一致性。

， 却便;标准化Ht理
ee preprccessteexrl
ER

EN， seael 二

复审人到

3 记录模型版本与参数
在向量存储时附加 nodelvezsicn 和预处理参数 (如 hash preprocess_ccntigl ) ，便于拓查差异.

7 二出所




## 第 26 页


ec

4 混合检索多诬

即使向量存在微小差昼，通过关键词检索 (BM25) +向量检索的混合策路，可提升召回稳定性 (参考资料3)-
关键结论
， 可能不一致: 模型非克定性、预处理差昼、环境变化均可能导到向量结果不
。 可控制: 通过确定性模式、标准化预处理、版本管理可显著减少关异。
。 风度方案: 混合检索机制 (如BM25+向量】能缓解向量洒移对检索效果的影响-

不更新模型版本的话，同一个句子在两个时间点进行向和化，结果不一致?
出训时 国四
侈 =oe                                                                              026生03月1日1556
@涛联明，第三步，距高最近的同类型实体优先-
而训半 国旧1
Se                                                               oz6生03月日 1557

在RAG系统的指代消解中，"… -中南旺近的同类型实体优先"是关键策略之一，具体实现逻辑如下:

核心逻辑
1实体识别与分类
。 在对话"中提取关键实体(如人名、报念、项目名等) ，并按类型分类(如技术术语、产品名称、操作指令等)。
， 例如: 用户癌"机器字习是什么? “一 提取实体机器学习"(技术术语类)。
2 时间窗口控制
， 重点关注最近 3-5轮对话(测动窗口) ，因指代关系通常中越拉短殉离-
， 超出窗口的实体被乱咯，站免信息过吉。
3 同类型实体匹配
，* 当用户使用指代词 (如"它…这个") 时，系统在窗口内坦找与指代词美型相同的实体-
， 优先选择距南最近的实体 若同一类型出现多个实体 (如两个技术术语) ，优先选择最近一次提及的实体。
示例
“到放"” (最近3轮)
1用户:什么是机器学习?
一 提取实体 机吕池习 (技术术语类)

了用户:"它有哪些应用?“
一 指代词'它"需匹配技术术语类实体 一 选中最近的 机器闻习 。

3用户:这个算法的优缺版?“
一 指代词,这个"匹配技术术语类 -选中最近的 算法 《假设前文提及过)。

1 提取:对话中的人

cear_earates exrraet_enctsdeslatalog haaceryl-3i]，ensdry_ryperv盾机要
人
statae = le toc ein oaca              1

网玫排序，取最的人

eesrn canataaceat01 最人和

ear sae 天
复制代码

优势与局限

优势:
简单高灼，适合90%的常见指代场景，减少复杂计算。

局限:
。若奖一类型实体频公切换(如"模型A和-模型9交替出现) ，可能误判-
， 钊结合实体权重 (如用户强调的实体可提升优先级)】优化-

扩展优化

结合上下化"…: 着指代词出现在特定场暴 《如"这个方案) ，优先号配最近出现的方案类实体-
用户反馈学习: 运过用户-顶/中标记，动态调整实体优先级权重。

此第路在泊陪明系统中已验证有效，显著提升多轮对话的连俩性-

出5 用上




## 第 27 页


图                                                                                                     oocgoaBB it24

引用原文。 派明当前采用了基于 Redis 的对话历史管理机制，每个用户都有一个唯一的会话ID，所有的对话内容都按照时间顺序存在 Redis 中，并设置了7天的过
期时间

七天后，对话记录会消失吗
出上 用四

图 cae                                                                                               assoamaa om
引用原文 语义检索

@派聪明 如何实现语义检索
由S 国生1

5                                                                                                                              026征09月1日1012
基于参考资料，语义检索的实现主要依志向量相似度计算和Embedding寞型，只体流程如下
核心实现步避

1 文本向量化
， 使用Embedding模型(如豆包 :abao -snbeasing-*ext-240515 )】交用户查询和文档内容转换为高维向量 (如2048维)。

， 示例代码 Elasticsearch)

aeaalrweeserr) 1/
aoeeywecrortqaeeyecsozl 1/ 查jg量
eecaaam        /下午

mcandadases tecallm 11 名

复制代码

向量相似度计算
。 通过余弦相似度 (Cosine Similarity) 计算查询向量与文档向量的相关性-
，* 高相似度表示语义高度相关 (如-提升工作效率"匹配-提高生产力")。

3 混合检索策略
， 语义检索与关负词检索 (BM25莽法)结合，提升召回率:

1/ 条县， ma加
局

1/ 基且了，关久启叶渤 ， 要和

人
aa -erse全-ones rssscessensny goesy tauezyn)) 1/ 关和

aeaaalal -orete -orrelraserranl valaelasercezal) 1/ 用PH央

ae tsrae))) 71/ 公开村

La

了，aas重上

eececele -> =
andowsdaeeecaaam
aaametshe lo.2a1         0 ao
reacerecoeryedghe 1 .0a) 。 1/ mn时和no
EECEESRN

， 语义理解: 即使关键词不完全匹配，也能捕所语义相关性 (如效率"本本"生产力 。
， 混合增强-结合关键词检索的精确性，避免线向量检索的只声干扰-
， 权限控制: 通过 ,szza 、 publi 等字段实现数据内离，确保结果合规。

应用场景

。 RAG系统:为LUM提供精准的上下文知识，减少幻角-

， 企业知识库: 支持模灶查询(如 -报销流程"下配-费用申请指南")。
， 多租户架构 通过权限过沁 (如 -dray ) 保障数据安全

考责和中语义检索是浊合检索的核心组件，与关键词检索、BM25重排序协回工作，最终通过加权隆合〔 rs分娄-0.3 。 aazs分区*1.0 】 生成综合排序结果。

出s 国上四

四 om                                                                                                oasoamne aoa

引用原文: RRF

@派脱明 在泊税明项目中可以如何引入这种re -ranking方法?
页二兴国四1




## 第 28 页


CT 5                                                               026年月1日 308
1               在尖联明项目中，RRF可作为现有混合检索的重排补充。具体实现:

1 在现有BM25重排后增加RRF步圣，对向量检索和关键词检索结果进行融合排序。

2 实现RRF算法:

7 ij骨
aaable rzfacore = 1.0 1 (60 ， vectecaaakl 。1.0 1 (60 ，xeyeecaaaa

复制代码

了 修改HybridSearchsevice，在rescore阶段后添加RRF重拓:

1/ 全丙个村果半基weg娄|
asscsearchgesslsy zzfpesalta = cicalaregRTscoreslvectorgesulsa， heyosraResalta

复制代码

4 参数可配置，k值设为60，平清不同召回列表的排名差异-

.与现有权限过滩集成，确保RRF结果仍符合访问控制。

RRF优势是不参半外部模型，计算轻量，能有效平衡语义和关键词检索结果
出训汪 国旧

图 omm                                                                                                                assoang aos

引用原文: RRF

在注陪明中可以如体引入这种rerank方法?
由二革 加四和

司坟                                                                                                  26和03月1日Ta2

引用原文: 未来的 RAG 将会向智能体方向发展，比如模型在检索后会先刊断我找到的知识足够回答问题吗? "如果不够，它可能会主动向用户僻问，或者调用 function
al 去外部查询，再根据前面的检索结果，生成新的、更精确的查询-

针对上面的问题，你预想下咱样实现

者点革 国目瑟1
处mm                                                                        aasoanB ta
回泊陪明针对上面的问题，你预想下咱样实现
咖点时 用曲和
四        你 吃                                                                                                                   oo6t03朋1日 1054

引用原文: 如果我们检索出了 10 个文档，但只有 7 个是相关的，

@泊了明，相关性是电部分功能进行判断相关的
由二革用日E5

Ta                                                               026征03月1日 1056
在RAG系统中，文档相关性判断主要通过以下核心机制实现:
1 混合检索策咯《核心功能)
语义检索: 基于向量相似度 如余相似度) 判断语义相关性。例如，用户问 -提升工作效率"，系统会下本语义相近的文档(如-优化工作流程)。
， 关键词检索- 适过BM25算法计算关键词匹配度，确保精确术语《如技术和名酒、人名) 的召回.
， 加权可合: 结合两种检索结果，按权重计算综合得分 (如 关络得分 = Port分吉"0.2 + By人吉.0 )。
.置信度评分机制
。 向量相似度亲值:设置相似度下限 (如07) ，过尖任相关文档(参考资料第10节)。
。 8M25重排序: 对候选文档进行二次评分，确保关键词配高的文档优先级更高(参考资料第3节)。
3 权限过汉
， 通过"标签( -ras )、用户ID 〔 aaarza )、公开标识【 ;spablic ) 过泪无权限访问的文档，确保结果与用户相关(参考资料第6节)
4 人工标注评估(准确性验证)
四               ， 畏确率 【Precision@K : 如检索10个文档中7个相关，精确率=70% (参考资料第8节)-
，。 召回率 (Recall@kK) : 若知识库实际有10个相关文格，仅召回7个，召回率=7036.
。 实际震人工标注 riovansnecrds 作为基准，通过代码计算:

/计生本机
aaa tecpml
LeagTezeaa lz -yselevanrooczasveonratnslreespaleaas011 3 1 1

eesiel seeweascoane 1 sepmy





## 第 29 页


。 自动判断: 全厅混合检索的加权柄合和里信度间值过渤低相关结果。
。 人工验证: 通过精确率/百回率评估系统准确性，需人工标注相关文档[D作为参遇。
， 优化方向: 调整权重、提高向量维度 (如2048维) 、优化分块策略可提升相关性 (参考资料第4、11节)

出兴国四

叫                                                                                                                                  26年月1日 1059
召回率是指检索到的文档占全部文档的比例。精确率是指召回文档中相关性文档占的比例，对吗

在RAG系统中，文档相关性判断主要通过以下核心机制实现;### 1. “混合检索第路 核心功能) *" - "语义检索*: 基于向量相似度〈如余弦相似度】 判断滞
出5 国卓
有                                                                                                                              oz6年月1 1059

 您的理解基本正确，但需要更精确的表述:
召回率 (Recall) : 指检索到的相关文格占全部相关文档的比例

， 公式: 召回率 = 检索到的相关文档数 /全部相关文格数

。 反映系统找出所有相关内容的能力

和精确率 (Precision) : 指检索到的文档中，相关广档所占的比例

， 公式: 精确素 = 检索到的相关文档数 /检索到的文格总数

。 反映检索结果的相关性质量

您的表述中需要注意:

1 召回率不是"检索到的文档占全部文档*，而是 检索到的相关文档占全部相关文档-
了精确率中的召回文档"建议改为-检索到的文档更准确

这两个指标通常要权街，高召回率可能带来低精确率，反之亦然

召回率是指检索到的文档占全部文档的比例。精确率是指召回文格中相关性文档占的比例，对吗

出5 国旧和
叫                                                                                                            2026年9有TIB 1101
给个例子。比如返回了10个文档，相关的有7个。全部文格是20个。精确率，召回率多少

您的理解基本正确，但需要更靖确的表述: “召回率 【Recal) …:指检索到的“相关文档”"占"全部相关文格"*的比例 - 公式: 召回率 = 检索到的相关文档数
册5 国四和

12026年09月1日1102

， 知识库"有20个相关文档

。 系统检索运回10个文档

。 其中1个是真正相关的|

精确率(precision) = TI0 = 70%

表示返回的10个文档中，70%是真正相关的

召回率(Recall = 7120 = 35%

。 表示知识库中所有相关文档的35%补成功检索出来

新:

。 博确率离但召回率低，说明系统很慎，返回的都是高填信度结果，但漏兵了较多相关文档
。 可通过调整召回网值来平衡两者，提高召回率可能会降低生确率
。 实际应用中需根据业务场景选择侧重点

给个例子。比如返回了10个文档，相关的有7个。全部文档是20个。和精确不，召回率多少



