# 面渣逆袭MySQL篇V2.2

> 来源：面渣逆袭MySQL篇V2.2.pdf

> OCR 解析时间：2026-03-14 17:27:43

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 302

- **文件大小**: 53.56 MB


---


## 第 1 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

合 ”二哥的Java进阶之路

三分恶

沉默王二修订版

No. 11302




## 第 2 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

了

前

5.5 万字 331 张手绘图，详解 83 道 MYSQL 面试高频题 (让天下没有难背的八股) ，面渣背会这些 MySQL 八股
文，这次吊打面试官，我觉得稳了 (手动 dog) 。整理: 沉默王二，戳转载链接，作者: 三分恶，戳原文链接。

亮白版本更适合拿出来打印，这也是很多学生党喜欢的方式，打印出来背诵的效率会更高。

@@@ 回 器 了 C”立 面洁逆甘MySQL简V2.0.pdf - 福昕阅读器 〇 搜索                            而且@
文件 主页 注释 视图 表单 保护 共享 帮助                                            vv
开始            面条闻贰MySQL篇V，XX                                                                  ~
                                                                      No.1211302
国 尺入大
   二                             而wySQL有二后-让天下所有的天
岛                                                                     一eroen veerem
汕 “只 数据库架构
绝让 中 存傅3l舍
省 站 昌志
让 内 SQL 优化
= 只 案引

内 翅 35 .索引为什么能提高MYSQL

直 只”这36 能简单说一下索引的分类[                                                             ]         蔬]          1
只 弃37创建索引有也     人
二 只 计38 索引哪些情况下会失效呢34
*吕39 案引不适合甩些场录呢?        每个表只能有一个主键索引，一般是表中的自增id 字段。
#。吕40 案引是不是建的越多越好?7
二 内 示41为什么 InnoDB 要使用 B+:         CRERTE TABLE emp6 (emp_id INT PRIMARY KEY，name VARCHAR(50))) -~ 单列主键
<只党42.一横B+匀能存全多少条风        RERTE TABLE countryLanguage
由           也有             counsrycode cBARI3) ，
中 43案引为什么用 B+机不用通-            angkage Vancaan 30
二 内 汉44.为什么用 B+ 树而不用B才           PRIMRRY KEY (Countrycode，Language) -~ 复合主键
只 45.B+树索引和 Hash 索引有什么               于
只 去 46 孙族索引和非聚族索引有人
=只 47回表了解加?               一 这部分是帮助大家理解 start，面试中可不背 一
#吕48 联合索引了解吗? (补充)        如果创建表的时候没有指定主键，MySQL 的InnoDB 存储引擎会优先选择一个非空的唯一索引作为主键; 如果没
 只 49 覃关索引了解吗?             有符合条件的索引，MySQL 会自动生成一个隐藏的_rowid 列作为主键。
# 只 去50 什么是最左前曙原则?
央 61什么是索引下推?                      上f you do not define a PRIMARY KEY for your table, MySQL locates the frst
# ”只 52 如何章看是否用到了索引? 《             UNIQUE index where all the key columns are NOT NULL and InnoDB uses it as the
八《   ?12 -1302 >》必昨品              国蛋困归一   CO   十 12706%

2025 年 02 月 27 日开始着手第二版更新。

。 对于高频题，会标注在 《java 面试指南(付费) 》中出现的位置，哪家公司，原题是什么，并且会加愉，目
录一目了然; 如果你想节省时间的话，可以优先背诵这些题目，尽快做到知彼知己，百战不列。

。 区分八股精华回答版本和原理底层解释，让大家知其然知其所以然，同时又能做到面试时的高效回答。

。 结合项目 (技术派、pmhub) 来组织语言，让面试官最大程度感受到你的诚意，而不是机械化的背诵。

。 修复第一版中出现的问题，包括球友们的私信反馈，网站留言区的评论，以及 GitHub 仓库中的issue，让这
份面试指南更加完善。

。 增加二哥编程星球的球友们拿到的一些 offer，对面渣逆袭的感谢，以及对简历修改的一些认可，以此来激励
大家，给大家更多信心。

。 优化排版，增加手绘图，重新组织答案，使其更加口语化，从而更贴近面试官的预期。

No. 21302




## 第 3 页


逆区MySQL篇V2-让天下所有的面渣都能逆袭

Curent Reposhomy                       rrent Braneh
toBeBetteravaer         时 master

多 An updated version of GHHub Desktopis avaiiable and wil beinstaled atthenext aunch See whats new orrestart GiHub Deskton                                   x
changes       Histen     面洁逆绪 MySQL 篇第二版 寺

时 mg王= -oa050294d9 口 14732

Select Branch to Compai

_                         Ti changedfiles
面半地殴 MySQL 篇第二版

和       REAovEmd     器     :
set                 RPR和PT      1013 +
@rms   om             ，      ol4
 zuoy       1615 +
到际dist           docweenice- einmd
六 mm- .anonnsa             lol6| +
Www 国      0
重新部在
新部四              sideba_jiavasemd 器    1018
me      二
al9 +
docslerlsiavathneadmd 回
2025年3月4日build                 1929 +
玉 mmE= .2nonhsa        docslsrelsidebar_jmysqlmd 回
并发编程菩2.0 版PDF 完结       hnreadaqsmd 。 回    224| *
站           ae22
下                       iianlimd 回
并发编程篇             ic   hish-readme.md 器     1623| *
名 mpE= .anonnea                      lo24
Update javathread md
名 rmE= .2monhsa                    1825| “
1026 +
JUvw 和并发编程                   1o27 +
到 mmE= .anonneao                 84 1e28
Updatejnmmd
入 mrE- .anoulas                   sas lo29
有制除 dist                            986 ”1039
名 mmE- .anonnea
集合框架篇
 mm   4   ths ago                           2725| 2759

由于 PDF 没?
码，关注二哥的公众号，回复【222】即可拉取最新版本。

enelmysqlmd

页实的记录会按负指定的行格式存鱼到 User Records 中

HGrowthpBA: User_ Recordsl(https://cdn.tobebetterjavaer,com/stutynore/mysqt-2925
8464115235 ,png)

每个数据责的 Fite Header
都有一个上一页和下一页的编号，所有的数据页会形成一个双疝甸表-

HGrowthpBA: 数据贡通过双向链表过接] (https://cdn tobebetterjavaer,com/stutynore/mysq
126258464115648,png)

在 InnoDB 中，默认的页大小旺 16KB。可以通过 show
查看-

以一可的ava 进瞪之路: 贾的大小] (https://cdn.tobebetterjavaer,com/stutymore/mysqt-2
86246322135441,png)

推荐癌读:IlyS0L之数据下结构 (https://www ,modb,pro/db/139652)

Dava 面试指南《付瘟) ] (https://javabetter,cm/zhishixingqiu/mianshi htmU)收录的
字节眩动面经同学 1 Java 后击技术画面斌原盟; MyISAM 和 InnoDB 的区别有取些?

> 2，IDava 面试指南【付费)] (https//javabetter,cn/zhishixingqlu/mianshi htmt)收录的
美国同学 9一面试原旺: nysqt存全的数据都是什么样的?

人 -1715,13 +1759

年 3 月 21 日修改至此。今天[有球友报窜

法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】 ，或者扫描/长按识别下面的二维

No. 31302




## 第 4 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，  人
我有必要让他们先享受到一 点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、 人
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

< 公众号                        沉默王二                                                  wangpan                 尘人        于 由
名称                                    ^
晤                          己 二哥的 JVM 进阶之路.epub            2024年7月11日 14:0
二哥的 JVM 进阶之路.md              2024年7月11日 14:0
二哥的 JVM 进阶之路.pdf              2024年7月11日 14:0
60*13薪别说新疆 ，外派到伊拉克都行                                    “ 面淹逆获 Java 基础篇第二版.md                 2024年12月31日 08
巳 面渣逆获 JVM篇 V2.0.epub             2025年1月21日 14:2
渣逆效 JVM篇 V2.0 (上暗黑版).pdf        2025年1月21日 14:2
“ 面渣逆费 JVM篇第二版.md             2025年1月21日 14:2
访 面秸逆芍 MyBatis.md                          2024年7月11日 14:0
面渣逆装 MyBatis.pdf               2024年7月11日 14:0
面渣逆绪 Redis 篇.md               2024年7月11日 14:0
一       ，            一                    面渣逆装 Redis 篇.pdf               2024年7月11日 14:0
量   再济闻交+一可的 Jave 进阶之路 PDF，第一                        忆 面淹逆袭 Spring 篇.md                    2024年7月11日 14:0
版，GitHub 星标13000+                                                  本 面渣逆效 Spring 篇.pdf                       2024年7月1日 14:0
忆 面渣逆闭-分布式篇.md                     2024年7月11日 14:0
驹闪避国几开二 Tree 下mm                  呈 面渣逆闭-分布式篇.pdf            2024年7月11日 14:0
aa                                        忆 面渣逆闭并发编程篇第二版.md           2025年2月26日 11:2
靖有局回岂有二 Treo 可 9                    口 面渣逆袭并发编程篇V2.0.epub           2025年2月26日1
1 1                                      名 面济逆区并发编程篇V2.0.pdf           2025年2月26日1
 面渣逆袭并发编程篇V2.0 (暗黑版) .pdf      2025年2月26日 11:3
二哥的并发编程小册: https://iavabetter'cn/                       二 面洁逆歼操作系统.md                    2024年7月11日 14:0
thread/                                          9 E 四             2024年7月11日 14:0
一       、。      .      |                          口 面济逆闭集合     二版.epub         2025年1月8日 18:3:
二可的 JVM 进阶之路: tpsViavabettercn/                             忆 面淹逆效集合框架篇第二版                     2025年1月8日 18:26
jm/                                             面淹逆赣集合框架篇V2.0.pdf           2025年1月8日 18:27
面尖逆绪集合框架篇V2.0 (暗黑) .pdf       2025年1月8日 18:26
'* 面渣逆效计算机网络.md                        2024年7月11日 14:0
  白 %-                                          面渣逆获计算机网络.pdf              2024年7月11日 14:0

'” 面渣逆效微服务篇.md                 2024年7月11日 14:0
面渣逆著微服务篇.pdf                 2024年7月11日 14:0
面渣逆效 Java基础篇V2.0.epub          2024年12月31日 09
面渣逆效Java基础篇V2.0.pdf           2024年12月30日 20
外 面渣逆芍Java基础篇V2.0 (暗黑) .pdf       2024年12月30日 20

我把二哥的java 进阶之路、JVM 进阶之路、并发编程进阶之路，以及所有面渣逆袭的版本都放进来了，涵盖 Java
基础、jJava集合、java并发、JVM、Spring、MyBatis、计算机网络、操作系统、MySQL、Redis、RocketMQ 、分
布式、微服务、设计模式、Linux 等 16 个大的主题，共有 40 多万字，2000+张手绘图，可以说是诚意满满。

展示一下暗黑版本的 PDF 吧，排版清晰，字体优雅，更加适合夜服，晚上看会更舒服一点。

222

No. 41302




## 第 5 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

它  局    忌                 Q 搜索                   册 及

文件 主页 注释 视图 才单 保护 共享 帮助

开始            面包并MySQL篇V2    画演地著MySQL篇V.，X                                                     "~
只| 王
[ES
包                                        最小的事务上
下一个将要生成
用                                                  二本的 uava 过内之路 。 的事务
在m_ids，读不             未知世界，读不
了,未确定呢                了
309
ae
4
310                              于 min_trx_id，风
时当表
0果 DB_TRX_ID 大于 max_tpcid，则表示        了                 2       ]
对当前       可见
如果 DB_TRX_ID 在 min_tp_id 和 max_trx_id 之间    要判断 DB_TR
311
名 《    311     0 >》》 目                  国由明明一       十 12706%

MySQL 基础
0.过什么是MySQL?

MySQL 是一个开源的关系型数据库，现在隶属于 Oracle 公司。是我们国内使用频率最高的一种数据库，我在本地
安装的是最新的 8.3 版本。

mysqL --Vverston

mysqL Ver 8.3.0 for macos14.2 on arm64 (Homebrew)

怎么删除/创建一张表?
可以使用 pRoP TaBLE 来删除表，使用 cREATE TABLE 来创建表。
创建表的时候，可以通过 PRIMARY KEY 设定主键。

No. 51302




## 第 6 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CRERTE TRBLE users (
id INT RUTO_INCREMENT，
name VRARCHRAR(100) NOT NULLV
email VRRCHRAR(100) ，
PRIMRARY KEY (id)

)

请写一个升序/降序的 SQL 语句?

在 SQL 中，可以使用 ORDER BY 子句来对查询结果进行升序或者降序。默认情况下，查询结果是升序的，如果需
要降序，可以通过 psc 关键字来实现。

比如说在员工表中，我们要按工资降序，就可以使用 ORDER BY salary DESC 来完成:

SELECT id，name，Ssalary
FROM employees
ORDER BY salary DESC?

如果需对多个字段进行排序，例如按工资降序，按名字升序，就可以 ORDER BY salary DESC，name RSC 来完
成:

SELECT id，name，Ssalary
FROM employees
ORDER BY salary DESC，name RSC1

MySQL出现性能差的原因有哪些?
可能是 SQL 查询使用了全表扫描，也可能是查询语句过于复杂，如多表JOIN 或庶套子查询。
也有可能是单表数据量过大。

通常情况下，添加索引就能解决大部分性能问题。对于一些热点数据，还可以通过增加 Redis 缓存，来减轻数据库
的访问压力。

1. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: 你平时用到的数据库
2. java 面试指南 (付费) 收录的腾讯云智面经同学 16 一面面试原题: 数据库用过哪些，对哪个比较熟?
3. java 面试指南 (付费) 收录的 360 面经同学 3 java 后端技术一面面试原题: 用过哪些数据库

4. java 面试指南 (付费)_收录的招商银行面经同学 6 招银网络科技面试原题: 了解 MYSQL、Redis 吗?

5. Java 面试指南 (付费) 收录的国企零碎面经同学 9 面试原题: 数据库用什么多 (说了 Mysql 和 Redis)
6.

.Java 面试指南 (付费) 收录的vivo 面经同学 10 技术一面面试原题: 怎么删除/创建一张表和设定主键
，举例用sql实现升序降序

7. Java 面试指南 (付费) 收录的滴泣面经同学 3 网约车后端开发一面原题: MySQL性能慢的原因
1.两张表怎么进行连接?

可以通过内连接 inner join 、外连接 outer join 、交叉连接 cross join 来合并多个表的查询结果。
什么是内连接?

No. 61302




## 第 7 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

内连接用于返回两个表中有匹配关系的行。假设有两张表，用户表和订单表，想查询有订单的用户，就可以使用内
连接 users INNER JOIN orders ，按照用户 ID 关联就行了。

SELECT users.name，orders.order_id
FROM users

INNER JOIN orders ON users.id = orders.user_id;

只有那些在两个表中都存在 user_id 的记录才会出现在查询结果中。

什么是外连接?

和内连接不同，外连接不仅返回两个表中匹配的行，还返回没有匹配的行，用 nul1 来填充。
外连接又分为左外连接 left join 和右外连接 right join 。

left join 会保留左表中符合条件的所有记录，如果右表中有匹配的记录，就返回匹配的记录，否则就用 null 填充，
常用于某表中有，但另外一张表中可能没有的数据的查询场景。

假设要查询所有用户及他们的订单，即使用户没有下单，就可以使用左连接:
SELECT users.id，users.name，orders.order_id

FROM users
LEFT JOIN orders ON users.id = orders.user_ id

查询前:
users                                                                         orders
id                                                                    name
1                                                                                                 王二
2                  张三
3                  李四
查询后:
id                                  name                                                   order id
1                               王二                                              10
2                              张三                                              20
3                              李四                                              null

右连接就是左连接的镜像，right join 会保留右表中符合条件的所有记录，如果左表中有匹配的记录，就返回匹配
的记录，否则就用 null 填充。

什么是交叉连接?

No.71302




## 第 8 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获
交叉连接会返回两张表的笛卡尔积，也就是将左表的每一行与右表的每一行进行组合，返回的行数是两张表行数的
乘积。
假设有A表和 B 表，A 表有 2 行数据，B 表有 3 行数据，那么交叉连接的结果就是2 X 3=6行。

SELECT R.id，B.id
FROM 及
CROSS JOIN By

笛卡尔积是数学中的一个概念，例如集合 a={a,b} ，集合 B={0,1,2} ，那么A愉B= {<a,0>,<avl>,<av2>，
<b,0>,<b,1l>,<b,2>，} 。

1. Java 面试指南付费) 收录的用友面试原题: 两张表怎么进行连接
2.内连接、左连接、右连接有什么区别?

MySQL 的连接主要分为内连接和外连接，外连接又可以分为左连接和右连接。

SQL JOINS

SELECT <select_list>
FROM TableA A

SELECT <select_list>
FROM TableA A
RIGHTJOIN TableB B
ON ALKey = B.Key

LEFTJOIN TableB B
ON ALKey = B.Key

SELECT <select_list>
FROM TablecA A
INNERJOIN TableB B
ON A.Key = B.Key

SELECT <select_list>                                                                                                    SELECT <select_list>
EROM TableA A                                                                                                                                         EROM TableA A
ILEFTJOIN TableB B                                                                                                                RIGHT JOIN TableB B
ON AKey = B.Key                                                                                                        ON AKey = B.Key
WHERE B.KeyIS NULL                                                                                                WHERE A.KeyIS NULL

SELECT <select_list>

SELECT <seleet_list>                                                                                                      FROM TableA A
FROM TableA A                                                                                                             FULL OUTER JOIN TableB B
EULL OUTER JOIN TableB B                                                                                       ON AKey = B.Key
ON A.Key = B.Key                                                                                               WHERE AKeyIS NULL
@@CL Moffatt 2008                       OR B.KeyISNUIL

内连接可以用来找出两个表中共同的记录，相当于两个数据集的交集。

左连接和右连接可以用来找出两个表中不同的记录，相当于两个数据集的并集。两者的区别是，左连接会保留左表
中符合条件的所有记录，右连接则刚好相反。

No. 81302




## 第 9 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

拿               的表为例来详细验证下。

有三张表，一张文章表 article，主要存文章标题 title， 一张文章详情表 article_detail，主要存文章的内容
content，一张文章评论表 comment，主要存评论 content，三个表通过文章 id 关联。

先来看内连接:

(a      ，20)    RrticleTitle，     (c        ，20)    CommentContent

article aa
27

SELECT LEFT(a.tite，20) AS ArtictLeTitLe，LEFT(c.content，20) AS CommentContent

FROM articte a
INNER JOIN comment cC ON a.id = c.articte_id

LIMIT 2;

| ArtictLeTitte                                | CommentContent

+-          ---------------------------+------
| 程序员 35 岁危机，如何破局 ?
| 分布式系统的8个廖误

2 rows in set (0.00 sec)

返回至少有一条评论的文章标题和评论内容 (前 20 个字符) ，只返回符合条件的前 2 条记录。

再来看做连接:

(a      ，20)    RrticleTitle，     (c        ，20)    CommentContent

article

27

mysqL> SELECT LEFT(a.titLe，20) AS ArtictLeTitLe，LEFT(c.content，20) AS CommentContent
-> FROM articte a
-> LEFT JOIN comment c ON a.id = c.articte_id
-> LIMIT 2;

十           -

| ArtictLeTitte

十           -

| “Cent0S7同步时间
| [古诗文]-泊船瓜洲
+-         -    ---
2 rows in set (0.01 sec

(a      ，20)    RrticleTitle，     (c        ，20)    CommentContent

article       已       =

No. 91302




## 第 10 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

SELECT LEFT(a.titLe，20) AS ArtictLeTitLe，LEFT(c.content，20) AS CommentContent
FROM comment <

RIGHT JOIN articte a ON a.id = c.articte_id

LIMIT 2;

| ArticteTitte               | CommentContent
二

"Cent0S7同步时间
| [古诗文]-泊船瓜洲

+----
2 rows in set (0.00 sec)

Ujava 后端实习一面原题: 请访

1. java 面试指南 (付费) 收录由

别

i MYSQL 的内联、左联、右联的区

memo: 2025年 2 月 27 日修改至此。给大家看一条球友的面经，基本上都是面渣逆袭中常见的八股，所以只
能把面渣中的高频题拿下，面试 OC 的概率真的很大，真心话。

记忆                                                                                                                 收进专栏
#面经八股

分享一下前几天面试的面经
小赢科技 (已oc)

一面:

1.jvm内存模型

2.内存溢出会出现在哪里，出现的场景
3.你认为哪个区域出现的概率比较大
4.垃圾回收的方法
5.Java集合的底层数据结构

6.使用多线程带来的问题，如何解;
7.redis的使用场景
8.redis的持久化机制

9.redis事务

10.redis的特性

11.MySQL事务

12.乐观锁和悲观锁

13.红黑树和二叉树的区别
14.InnoDB和MylISAM的区别

15.实习的相关内容

3.说一下数据库的三大范式?

No. 101302




## 第 11 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

第一范式，确保表的每一列都是不可分割的基本数据单元，比如说用户地址，应该拆分成省、市、区、详细地址等

4个字段。
编号 姓名
1     张红欣
2       李四平
3 。， 刘苇国
4     郭小明

用户信息表
性别 年龄 ”联系电话     省份 ”城市
男   26   0378-23459876 河南 ”开封
妈   32   0751-65432584 广州 广东
男   21   0371-87659852 河南 ”郑州
妈   27   0371-62556789 河南 |郑州

详细地址
朝阳区新华路23号
白云区天明路148号
二七区大学路198号

新郑市芒店北街218号

第二范式，要求表中的每一列都和主键直接相关。比如在订单表中，商品名称、单位、商品价格等字段应该拆分到

商品表中。
订单编号 商品编号 ”商品名称 ”数量            单位            价格                  客户
001          1              挖掘机 。 I              台             1200000Y 。 张三
001          2              冲击牛 8              把             230六             张三
002          3              铲车          2              辆             980000        李四

然后新建一个订单商品关联表，用订单编号和商品编号进行关联就好了。

No.111302

所属单位 联系方式

上海玖智 ”020-1234567

上海孜智 ,020-1234567

北京公司 010-1234567




## 第 12 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

订单编号            商品编号            数量

001                         工                              1
001                         2                              8
002                         ，                              2

第三范式，非主键列应该只依赖于主键列。比如说在设计订单信息表的时候，可以把客户名称、所属公司、联系方

式等信息拆分到客户信息表中，然后在订单信息表中用客户编号进行关联。
订单信息表
订单编号    订单项目    负责人     业务员      订单才旺    客户编号
001                    挖掘机               刘明                   李东明               1台                    1
002                    冲击钻               李刚                   和霍新峰               8个                    2
003                    久车                   郭新一               艾美丽               2炳                    1
客户信息表
客户编号          客户名称          所属公司           联系方式
1                                    李聪                               五一建设                         13253661015
2                                    刘新明                            个体经营                         13285746958

建表的时候需要考虑哪些问题?

首先需要考虑表是否符合数据库的三大范式，确保字段不可再分，消除非主键依顿，确保字段仅依赖于主键等。
然后在选择字段类型时，应该尽量选择合适的数据类型。

在字符集上，尽量选择 utfgmb4，这样不仅可以支持中文和英文，还可以支持表情符号等。

当数据量较大时，比如上千万行数据，需要考虑分表。比如订单表，可以采用水平分表的方式来分散单表存储压
力。

No. 12 1 302




## 第 13 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

1. Java 面试指南 (付费)_收录的字节跳动面经同学 13 java 后端二面面试原题;: 什么是三大范式，为什么
要有三大范式，什么场景下不用遵循三大范式，举一个场景

2 Java 面试指南(付费) 收录的京东面经同学 5 java 后端技术一面面试原题: 建表考点哪些问题
4.varchar 与 char 的区别?

varchar 是可变长度的字符类型，原则上最多可以容纳 65535 个字符，但考虑字符集，以及 MySQL 需要1到 2个
字节来表示字符串长度，所以实际上最大可以设置到 65533。

latin1 字符集，且列属性定义为 NOT NULL。

chat  下 i | ea ft

Vatchat

char 是固定长度的字符类型，当定义一个 cHaR(10) 字段时，不管实际存储的字符长度是多少，都只会占用 10
个字符的空间。如果插入的数据小于 10 个字符，剩余的部分会用空格填充。

值           CHAR(4)     存储需求 (字节)       VARCHAR(4)      存储需求 (字节)
                     的                  4                               机                         1
"ab'          "ab        4                 "ab'            3
"abcd'         "abcd'       4                 "abcd'           5
"abcdefgh'     "abcd'       4                 "abcd '           5

5.blob 和text 有什么区别?

blob 用于存储二进制数据，比如图片、音频、视频、文件等; 但实际开发中，我们都会把这些文件存储到 OSS 或
者文件服务器上，然后在数据库中存储文件的 URL。

text 用于存储文本数据，比如文章、评论、日志等。
memo: 2025年2月28 日修改至此。今天有球友反馈拿到了理想汽车的补录 offer， 真的葡喜了!

No. 13 1302




## 第 14 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

对的, 算是补录吧, 泡池子给我捞
上来了

确实是仍念劲, 但凡少一点可能
融还是选含稳定的了

6.DATETIME 和TIMESTAMP 有什么区别?

DATETIME 直接存储日期和时间的完整值，与时区无关。
TIMESTAMP 存储的是 Unix 时间戳，1970-01-01 00:00:01 UTC 以来的秒数，受时区影响。

No. 141302





## 第 15 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆效

另外，DATETIME 的默认值为 null，占用 8 个字节; TIMESTAMP 的默认值为当前时间一一
CURRENT_TIMESTAMP，占 4 个字节，实际开发中更常用，因为可以自动更新。

record.setNotifyTime(     Date()) ;

record.setNotifyCcnt(record.getNotifyCnt() + 1) ;

7.in和exists的区别?

当使用 IN 时，MySQL 会首先执行子查询，然后将子查询的结果集用于外部查询的条件。这意味着子查询的结果集
需要全部加载到内存中。

而 EXISTS 会对外部查询的每一行，执行一次子查询。如果子查询返回任何行，则 ExIsTs 条件为真。 EXISTS 关
注的是子查询是否返回行，而不是返回的具体值。

No. 15 1 302




## 第 16 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-- IN 的临时表可能成为性能瓶颈
SELECT * FROM users
WHERE id IN (SELECT user_id FROM orders WHERE amount > 100)7

-- EXISTS 可以利用关联索引

SELECT * FROM users
WHERE EXISTS (SELECT 1 FROM orders o
WHERE o.user_ id = u.iqd RND oamount > 100)7

IN 适用于子查询结果集较小的情况。如果子查询返回大量数据， IN 的性能可能会下降，因为它需要将整个结果
集加载到内存。

而 EXISTS 适用于子查询结果集可能很大的情况。由于 BXISTS 只需要判断子查询是否返回行，而不需要加载整个
结果集，因此在某些情况下性能更好，特别是当子查询可以使用索引时。

NULL值陷了解吗?

IN : 如果子查询的结果集中包含 NuLL 值，可能会导致意外的结果。例如， wHERE column IN (subquery) ，如
果 subquery 返回 NULL ，则 column IN (subquery) 永远不会为真，除非 column 本身也为 NULL 。

EXISTS : 对 NULL 值的处理更加直接。 ExISTS 只是检查子查询是否返回行，不关心行的具体值，因此不受 NULL
值的影响。

memo: 2025年3月1日修改至此。

8.记录货币用什么类型比较好?

如果是电商、交易、账单等涉及货币的场景，建议使用 DECIMAL 类型，因为 DECIMAL 类型是精确数值类型，不
会出现浮点数计算误差。
例如，pEcIMaAL(19,4) 可以存储最多 19 位数字，其中 4 位是小数。
CRERTE TRBLE orders |(
id INT RUTO_INCREMENT，
amount DECIMRAL(19，4) ，

PRIMRARY KEY (id)
)

如果是银行，涉及到支付的场景，建议使用 BIGINT 类型。可以将货币金额乘以一个固定因子，比如 100，表示以
“分"为单位，然后存储为 BIGINT 。这种方式既避免了浮点数问题，同时也提供了不错的性能。但在展示的时候需
要除以相应的因子。

为什么不推荐使用 FLOAT 或 DOUBLE?
因为 LOAT 和 DOUBLE 都是浮点数类型，会存在精度问题。

在许多编程语言中，0.1 + 0.2 的结果会是类似 0.30000000000000004 的值，而不是预期的 0.3 。

9.二怎么存储emoji?

No. 16 1 302




## 第 17 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

因为 emoji (候) 是4个字节的 UTF-8 字符，而 MySQL 的 utf8 字符集只支持
在 MySQL 中存储emoji 时，需要使用 utf8mb4 字符集。

辕

多 3 个字节的 UTF-8 字符，所以

RLTER TRBLE mytable CONVERT TO CHRARRACTER SET utf8mb4 COLLRATE utf8mb4_unicode_ciy

MySQL 8.0 已经默认支持 utf8gmb4 字符集，可以通过 SHOW VARIABLES WHERE Variable_name LIKE

"character\_set\ 8%'，OR Variable_name LIKE 'collations'; 查看。

mySsqL> SHOW VARIABLE9S LIKE 'character_Sset_server ' ;
十-一一

13 Java 后端二面面i

mysql 怎么存emoji，怎

么编码

10.drop、delete 与 truncate 的区别?
DROP 是物理删除，用来删除整张表，包括表结构，且不能回滚。
DELETE 支持行级删除，可以带 WHERE 条件，可以回滚。
TRUNCATE 用于清空表中的所有数据，但会保留表结构，不能回滚。

memo: 2025年3月4日修改至此。给大家传递一个喜报，一位球友拿到了科大讯飞的 offer，这薪资在合肥真
的会很香。

No. 171302




## 第 18 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

二哥你好呀, 我现在offer 二选一，
能帮有我分析一下吗

1. 讯飞, 做Al+ 医疗业务的, 合肥
年包 上
2. 银联上海, 年包 3:

11.UNION 与UNION ALL 的区别?
UNION 会自动去除合并后结果集中的重复行。UNION ALL 不会去重，会将所有结果集合并起来。

12.count(1)、count(*) 与 count(列名) 的区别?

在InnoDB 引擎中，couNT(1) 和 couNT(*) 没有区别，都是用来统计所有行，包括 NULL。
如果表有索引， couNT(* ) 会直接用索引统计，而不是全表扫描，而 couNT(1) 也会被 MySQL 优化为

COUNT(* ) 。

COUNT (列名) 只统计列名不为 NULL 的行数。

-- 假设 users 表:

+----+-------+------------+
| id | name | email    |
+----+-------+------------+
| 1 |张三 | zhangexx.com |
| 2 | 李四 | NULL     |

| 3 | 王二 | wangexx.com |
+----+-------+------------+
-- COUNT(x)

SELECT COUNT(*) FROM usersy
-- 结果: 3 (统计所有行)

-- COUNT(1)
SELECT COUNT(1) FROM usersy

-- 结果: 3 (统计所有行)

-- COUNT(email)
SELECT COUNT(email) FROM usersy

No. 18 1 302




## 第 19 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆效
-- 结果: 2 (NULL 不计入统计)
这里解释一下，假设有这样一张表:

CRERTE TRABLE 七1
id INT，
name VRARCHRR(50) ，
value INT

插入的数据为:

INSERT INTO 上1 VALUES
1   ，10)，
，NULL) ，
，30)，
NULL，40)，

，NULL) ;

因为 id 列没有索引，所以 select count(*) 是全表扫描。

mysqtL> explLatin seLect count(*) from t1 NO;
痰火火火火火火火火火火火火火火火火火火火火火火火火火在。 六DOW 大火火火火火火火火大大火火火火火火火火火炎火火火火大大
id: 1
SetLect_type: SIMPLE
tabLe: t1
partitions: NULL
type: ALL
possibLe_keys: NULL
key: NULL
key_Len: NULL
ref: NULL
rows: 5
fittered: 100.00
Extra: NULL
1 row in set，1 warning (0.00 sec)

然后我们给 id 列加上索引。

No. 191302




## 第 20 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqtL> DESCRIBE t1;

rows in set (0.00 sec)
再来看一下 select count(*) ，发现用了索引 (MySQL 默认为给主键添加索引) 。

mysqL> expLain seLect Count(*) from t1 NG;
痰火火火火火火火火火火火火火火火炎火炎火炎火炎火炎大大 1. OW 大大火大火炎火炎大火大火炎大火大火炎火炎大火大火炎大大
id: 1
SeLect_type: SIMPLE
tabLe: t1
partitions: NULL
type: index

possibtLe_keys: NULL
key: PRIMARY
key_tLen: 4
ref: NULL
rows: 5
fiLtered: 100.00

Extra: Using index
1 row in set，1 warning (0.00 sec)

另外，MySQL 8.0 官方手册有明确说明，InnoDB 引擎对 SELECT coUNT(*) 和 SELECT coOUNT(1) 的处理方式完
全一致，性能并无差异。

No. 201302




## 第 21 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

mysql> SELECT student .student_name,COUNT(*)
FROM student,course
WHERE student .student_id=course.student_id
GROUP BY student_name;

COUNT(* ) is somewhat different in that it returns a count of the number of rows retrieved, whether or not
they contain NULL values.

For transactional storage engines such as InnoDB, storing an exact row count is problematic. Multiple
transactions may be occurring at the same time, each of which may affect the count.

InnoDB does not keep an internal count of rows in atable because concurrent transactions might “see”
different numbers of rows at the same time. Consequently, SELECT COUNT(* ) statements only count
rows visible to the current transaction .

As of MySQL 8.0.13, SELECT COUNT(*) FROM tb]lI_name query performance for InnoDB tables is
optimized for single-threaded workloads if there are no extra clauses Such as WHERE Or GROUP BY.

InnoDB processes SELECT COUNTI(*) statements by traversing the smallest available secondary index
unless an index or optimizer hint directs the optimizerto use a different index. If a secondary index is not
present, InnoDB processes SELECT COUNT(* ) Statements by scanning the clustered index.

Processing SELECT COUNT(* ) statements takes some time if index records are not entirely in the
buffer pool. For a faster count, create a counter table and let your application update it according to the
inserts and deletes it does. However, this method may not scale well in situations where thousands of
concurrent transactions are initiating updates to the same counter table. If an approximate row count is
Sufficient, use SHOW TABLE STATUS.

InnoDB handles SELECT COUNT(*) and SELECT COUNT(1) operations in the same way. There is no
performance difference.

memo: 2025年3月5日修改至此。再晒一个喜报给正在刷八股的你，一位球友拿到了咪咕的大模型应用开发，
很不错的方向，恭喜了! 给你也加加好运敬buff，你也加把劲。

No. 211 302




## 第 22 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥， 我想问一  下， 我拿到一  二
咕公司 的大各 本有下

上午1129

视频也是很好的方向   时
13.SQL 查询语句的执行顺序了解吗?

了解。先执行 FROM 确定主表，再执行JOIN 连接，然后 WHERE 进行过滤，接着 GROUP BY 进行分组，HAVING
过滤聚合结果，SELECT 选择最终列，ORDER BY 排序，最后 LIMIT 限制返回行数。

No. 221 302




## 第 23 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

WHERE 先执行是为了减少数据量，HAVING 只能过滤聚合数据，ORDER BY 必须在 SELECT 之后排序最终结果，
LIMIT 最后执行以减少数据传输。

No. 231302




## 第 24 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

执行顺序                   SQL 关键字                     作用

@)                      FROM                      确定主表，准备数据
@                      ON                         连接多个表的条件

四             JOIN              执行INNERJOIN /LEFTJOIN 等
团                     WHERE                     过滤行数据 (提高效率)
加                      GROUP BY                 进行分组

@                      HAVING                    过滤聚合后的数据

@                      SELECT                     选择最终返回的列
                      DISTINCT                   进行去重

四                        ORDER BY                    对最终结果排序

@                      LIMIT                       限制返回行数

这个执行顺序与编写 SQL 语句的顺序不同，这也是为什么有时候在 SELECT 子句中定义的别名不能在 WHERE 子句
中使用得原因，因为 WHERE 是在 SELECT 之前执行的。

LIMIT 为什么在最后执行?

因为 LIMIT 是在最终结果集上执行的，如果在 WHERE 之前执行 LIMIT，那么就会先返回所有行，然后再进行
LIMIT 限制，这样会增加数据传输的开销。

ORDER BY 为什么在 SELECT 之后执行?
因为排序需要基于最终返回的列，如果 ORDER BY 早于 SELECT 执行，计算 couNT(*) 之类的聚合函数就会出问

题。

SELECT name，COUNT(*) RS order_count
FROM orders

GROUP BY name

ORDER BY order_count DESC;

14.介绍一下 MySQL 的常用命令 (补充)

2024年03 月 13 日增补。

No. 241302




## 第 25 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

创建数据库

删除数据库
选择数据库

创建表

MySQL 的常用命令@沉

创建索引

添加主键约束
添加外键约束

创建用户

撤销权限

开始事务

提交事务
回滚事务

MySQL 的常用命令主要包括数据库操作命令、表操作命令、行数据 CRUD 命令、索引和约束的创建修改命令、用
户和权限管理的命令、事务控制的命令等。

说说数据库操作命令?

CREATE DATABRASE database_name; 用于创建数据库; DROP paTABASE database_name; 用于删除数据库;
SHOW DaATABRSES; 用于显示所有数据库; USsE database_name; 用于切换数据库。

说说表操作命令?

No. 251 302




## 第 26 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CRERATE TRBLE table_name (列名1 数据类型1，列名2 数据类型2, . . . ) ; 用于创建表; DROP TABLE
table_name; 用于删除表; sHow TABLES; 用于显示所有表; DESCRIBE table_name; 用于查看表结构; ALTER
TABLE table_name RDD column_name datatype; 用于修改表。

说说行数据的 CRUD 命令?

INSERT INTO table_name (column1，column2，...) VALUES (valuel，value2，...); 用于插入数据;
SELECT column_names FROM table_name WHERE condition; 用于查询数据; UPDpaTE table_name SET
columnl = valuel，column2 = value2 WHERE condition; 用于更新数据; DELETE FROM table_name
WHERE condition; 用于删除数据。

说说索引和约束的创建修改命令?

CRERTE INDEX index_name ON table_name (column_name); 用于创建索引 ALTER TABLE table_name RDD
PRIMRARY KEY (column_name); 用于添加主键; ALTER TABLE table_name ADD CONSTRRINT fk_name
FOREIGN KEY (column_name) REFERENCES parent_table (Parent_column_name); 用于添加外键。

说说用户和权限管理的命令?

CRERTE USER 'username'e'host' IDENTIFIED BY 'password'; 用于创建用户; GRANT ALL PRIVILEGES ON
database_name.table_name TO 'username'e'host'; 用于授予权限; REVOKE ALL PRIVILEGES ON
database_name.table_name FROM 'username'e'host'; 用于撤销权限; DROP UsER 'username'e'host'

用于删除用户。

说说事务控制的命令?

START TRANSRACTION; 用于开始事务; coMMIT; 用于提交事务; ROLLBACK; 用于回滚事务。
1. java 面试指南 (付费) 收录的用友金融一面原题: 介绍一下 MySQL 的常用命令

15.MySQL bin 目录下的可执行文件了解吗 (补充)

2024年 03 月 13 日增补
推荐阅读: MySQL bin 目录下的一些可执行文件
了解的。MySQL 的 bin 目录下有很多可执行文件，主要用于管理 MySQL 服务器、数据库、表、数据等。比如
说:
。 mysql: 用于连接 MySQL 服务器
。 mysqldump: 用于数据库备份，对数据备份、迁移或恢复时非常有用
。 mysqladmin: 用来执行一些管理操作，比如说创建数据库、删除数据库、查看 MySQL 服务器的状态等。
。 mysqlcheck: 用于检查、修复、分析和优化数据库表，对数据库的维护和性能优化非常有用。
。 mysqlimport: 用于从文本文件中导入数据到数据库表中，适合批量数据导入。
。 mysqlshow: 用于显示 MySQL 数据库服务器中的数据库、表、列等信息。
。 mysqlbinlog: 用于查看 MySQL 二进制日志文件的内容，可以用于恢复数据、查看数据变更等。

16.MySQL 第 3-10 条记录怎么查? (补充)

No. 26 1 302




## 第 27 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

2024 年 03 月 30 日增补

可以使用limit 语句，结合偏移量和行数来实现。
SELECT * FROM table_name LIMIT 2，87

limit 语句用于限制查询结果的数量，偏移量表示从哪条记录开始，行数表示返回的记录数量。
。 2: 偏移量，表示跳过前两条记录，从第三条记录开始。
。 8: 行数，表示从偏移量开始，返回 8 条记录。
偏移量是从 0 开始的，即第一条记录的偏移量是 0; 如果想从第 3 条记录开始，偏移量就应该是 2。
1. java 面试指南 (付费) 收录的美团面经同学 16 暑期实习一面面试原题: MySQL 第 3-10 条记录怎么

查?

17.用过哪些 MySQL 函数? (补充)
2024年 04 月 12 日增补
用过挺多的，比如说处理字符串的函数:
。 cONCaT() : 用于连接两个或多个字符串。
。 LENGTH() : 用于返回字符串的长度。
。 SUBSTRING() : 从字符串中提取子字符串。
。 REPLRCE() : 替换字符串中的某部分。
。 TRIM() : 去除字符串两侧的空格或其他指定字符。

实测数据:

-- 连接字符串

SELECT CONCRT( '沉默' ，'“'，“'王二') RS concatenated string7

-- 获取字符串长度
SELECT LENGTH( "沉默 王二') AS string_lengthy

-- 提取子字符串
SELECT SUBSTRING( '沉默 王二'，1，5) AS substringy

-- 蔡换字符串内容
SELECT REPLRCE( '沉默 王二'，“'王二' ，'MySOL ') AS replaced_stringy

-- 去除字符串两侧的空
SELECT TRIM(' 沉默 王二 “') AS trimmed _ stringy

处理数字的函数:
。 aBs() : 返回一个数的绝对值。
。 ROUND() :四舍五入到指定的小数位数。

No. 271302




## 第 28 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

。 MOD() : 返回除法操作的余数。
实测数据:

-- 返回绝对值

SELECT RARBS(-123) AS absolute_valuei

-- 四舍五入
SELECT ROUND(123.4567，2) AS rounded_valuey

-- 余数

SELECT MOD(10，3) RS modulus;
日期和时间处理函数:

。 NOW() : 返回当前的日期和时间。

e。 CURDRTE() : 返回当前的日期。
实测数据:

-- 返回当前日期和时间

SELECT NOW() RS current_date_timey

-- 返回当前日期

SELECT CURDRATE() RS current_date)
汇总函数:

。 SUM() : 计算数值列的总和。

。 avG() : 计算数值列的平均值。

。 coOUNT() : 计算某列的行数。
实测数据:

-- 创建一个表并插入数据进行聚合查询
CRERTE TABLE sales |(
product_id INT，
sales_amount DECIMRAL(10，2)
)

INSERT INTO sales (product_id，sales_amount) VRLUES (1，100.00);
INSERT INTO sales (product_id，sales_amount) VRLUES (1，150.00);
INSERT INTO sales (product_id，sales_amount) VRLUES (2，200.00);

-- 计算总和

SELECT SUM(sales_amount) RS total_sales FROM sales;

-- 计算平均值

SELECT RVG(sales_amount) RS_ average _sales FROM sales)

No. 28 1 302




## 第 29 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

-- 计算总行数
SELECT COUNT(*) RS total_entries FROM salesi
逻辑函数:
。 IF() : 如果条件为真，则返回一个值; 否则返回另一个值。
。 casE : 根据一系列条件返回值。

-- IF函数

SELECT IF(1 > 0，'True'，'False') RS simple if7

-- CASE表达式
SELECT CRSE WHEN 1 > 0 THEN 'True，ELSE 'False，END RS case_expression)

所

1. Java 面试指南 (付费) 收录的华为 OD 面经同学 1 一面面试原题: 用过哪些 MySQL 函数?

2. Java 面试指南 (付费) 收录的 小公司面经合集好未来测开面经同学 3 测开一面面试原题: 知道 MySQL
的虽    ，如 order by count()

18.说说 SQL 的隐式数据类型转换? (补充)
2024年 04 月 25 日增补
当一个整数和一个浮点数相加时，整数会被转换为

SELECT 1 + 1.0; -- 结果为 2.0

当一个字符串和一个整数相加时，字符串会被转换为整数。
SELECT '1' + 1; -- 结果为 2

隐式转换会导致意想不到的结果，最好通过显式转换来规避。
SELECT CRST('1' RS SIGNED INTEGER) + 1) -- 结果为 2

实际验证结果:

mySsqL> SELECT 1 + 1.0;

1 row in set (0.00 sec )

No. 291302




## 第 30 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

mysqL> SELECT '1' + 1;

1 row in set (0.00 sec )

mysqL> SELECT '北京" + 2008;

1 row in set，1 warning (0.00 sec )

mysqL> SELECT HELLO ”+ “WORLD! ';

(付费) 收录的小公司面经合集同学 1 java 后端面试原题: 说说 SQL 的隐式数据类型转

memo: 2025年3月6 日修改至此。
19. 说说 SQL 的语法树解析? (补充)

2024年 09 月 19 日增社





## 第 31 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭
SQL 语法树解析是将 SQL 查询语句转换成抽象语法树 一一 AST 的过程，是数据库引警处理查询的第一步，也是防
止 SQL 注入的重要手段。
通常分为 3 个阶段。
第一个阶段，词法分析: 拆解 SQL 语句，识别关键字、表名、列名等。
---这部分是帮助大家理解 start，面试中可不背---
比如说:

SELECT id，name FROM users WHERE age > 187
将会被拆解为:
[SELECT] [idq] [,] [name] [FROM] [users] [WHERE] [age]l [>] [18] [7

-这部分是帮助大家理解end，面试中可不背--

第二个阶段，语法分析: 检查 SQL 是否符合语法规则，并构建抽象语法树。
-这部分是帮助大家理解 start，面试中可不背--

比如说上面的语句会被构建成如下的语法树:

SELECT
/          \
Columns            FROM
/          、\           |
id          name USserSs

或者这样表示:

SELECT
|一 coruNs: id，name
|六 FRoM: users
|一 wazgRE
上六 coNpImION: age > 18

-这部分是帮助大家理解 end，面试中可不背--

第三个阶段，语义分析: 检查表、列是否存在，进行权限验证等。
--这部分是帮助大家理解 start，面试中可不背--

比如说执行:

No. 311302




## 第 32 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

SELECT id，name FROM users WHERE age > 'eighteen')
会报错:
ERROR: Column 'age' is INT，but 'eighteen'， is STRING.

---这部分是帮助大家理解end，面试中可不背---
1. Java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: sq|的语法树解析

memo: 2025年3月7日修改至此。再晒一个 offer，一位球友拿到了经纬恒润的实习 offer，并且直言面试了很
多场，我说超过 5 次的题目基本上都碰到了，哈都别说了，面渣逆袭 YYDS。

No. 321302




## 第 33 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

哥您好 束是经纬恒润这边大约
=:1- 入职

, 面了那么多疡， 基本上你说
的超过五   次出现在面渣的面试题，
基本上都; 遇到了， 并且大部分都是
那些题目

数据库架构

20.说说 MySQL 的基础架构?
MySQL 采用分层架构，主要包括连接层、服务层、和存储引擎层。





## 第 34 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

[                       连接/线程处理                      了

Server

ED |

存储引擎

InnnoDB          MYISAM

亿、连接层主要负责客户端连接的管理，包括验证用户身份、权限校验、连接管理等。可以通过数据库连接池来提
升连接的处理效率。

@@、服务层是 MySQL 的核心，主要负责查询解析、优化、执行等操作。在这一层，SQL 语句会经过解析、优化器
优化，然后转发到存储引擎执行，并返回结果。这一层包含查询解析器、优化器、执行计划生成器、日志模块等。

@@、存储引擎层负责数据的实际存储和提取。MySQL 支持多种存储引擎，如 InnoDB、MylISAM、Memory 等。
binlog写入在哪一层?

binlog 在服务层，负责记录 SQL 语句的变化。它记录了所有对数据库进行更改的操作，用于数据恢复、主从复制
等。

1. Java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: mysql分为几层? binlog
写入在哪一层

21. 一条查询语句是如何执行的?

当我们执行一条 SELECT 语句时，MySQL 并不会直接去磁盘读取数据，而是经过 6 个步骤来解析、优化、执行，
然后再返回结果。

No. 341302




## 第 35 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

客户端                          MySQL 服务器                                     存储引擎
ER                            二                                  二哥的 Java 进阶之路
了
分析器
了
优化器

InnoDB

执行器             通过             存储引擎

第一步，客户端发送 SQL 查询语句到 MySQL 服务器。
第二步，MySQL 服务器的连接器开始处理这个请求，跟客户端建立连接、获取权限、管理连接。

第三步，解析器对 SQL 语句进行解析，检查语句是否符合 SQL 语法规则，确保数据库、表和列都是存在的，并处
理 SQL 语句中的名称解析和权限验证。

第四步，优化器负责确定 SQL 语句的执行计划，这包括选择使用哪些索引，以及决定表之间的连接顺序等。
第五步，执行器会调用存储引擎的 AP 来进行数据的读写
第六步，存储引擎负责查询数据，并将执行结果返回给客户端。客户端接收到查询结果，完成这次查询请求。

1. java 面试指南 (付费)_收录的美团面经同学 2 java 后端技术一面面试原题: MySQL 执行语句的整个过
程了解吗?

2. java 面试指南(付费) 收录的美团面经同学 18 成都到家面试原题: mysql一条数据的查询过程

No. 351302




## 第 36 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

3. java 面试指南 (付费) 收录的字节跳动面经同学19番茄小说一面面试原题: MySQL中一条SQL的执行

流程

memo: 2025年3月8 日修改至此。

22.一条更新语句是如何执行的?

总的来说，一条 UPDATE 语句的执行过程包括读取数据页、加锁解锁、事务提交、日志记录等多个步骤。

Update Test set a=1 where id=2

                                                                                                                    服务层执行器
取id=2这一行        修改id为2的这一行为1                         写入binlog

    结果更新到内存

”并将这行记目国提交事务，并在redo log中
改为prepare    将该事务状态设为commit

拿 update test set a=1l where id=2 举例来说:

在事务开始前，MySQL 需要记录undo log，用于事务回滚。

操作                                 id                   旧值                        新值

Update                              2                    N                           1
除了记录 undo log，存储引擎还会将更新操作写入 redo log，状态标记为 prepare，并确保 redo log 持久化到磁
盘。这一步可以保证即使系统崩溃，数据也能通过 redo log 恢复到一致状态。

写完 redo log 后，MySQL 会获取行锁，将 a 的值修改为 1，标记为脏页，此时数据仍然在内存的 buffer pool
中，不会立即写入磁盘。后台线程会在适当的时候将脏页刷盘，以提高性能。

最后提交事务，redo log 中的记录被标记为 committed，行锁释放。
如果 MySQL 开启了 binlog，还会将更新操作记录到 binlog 中，主要用于主从复制。

以及数据恢复，可以结合 redo log 进行点对点的恢复。binlog 的写入通常发生在事务提交时，与 redo log 共同构
成“两阶段提交"，确保两者的一致性。

注意，redo log 的写入有两个阶段的提交，一是 binlog 写入之前 prepare 状态的写入，二是 binlog 写入之后
commit 状态的写入。

memo: 2025年3月9日修改至此。

No. 361302




## 第 37 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

23.说说 MySQL 的段区页行 (补充)
2024年 04 月 26 日增补
推荐阅读: 了解 MySQL的数据行、行溢出机制吗?_
MySQL 是以表的形式存储数据的，而表空间的结构则由段、区、页、行组成。
表空间(tablespace)

段(segment)

亿、段: 表空间由多个段组成，常见的段有数据段、索引段、回滚段等。

创建索引时会创建两个段，数据段和索引段，数据段用来存储叶子节点中的数据; 索引段用来存储非叶子节点的数
据。

回滚段包含了事务执行过程中用于数据回滚的旧数据。

@@、区: 段由一个或多个区组成，区是一组连续的页，通常包含 64 个连续的页，也就是 1M 的数据。
使用区而非单独的页进行数据分配可以优化磁盘操作，减少磁盘寻道时间，特别是在大量数据进行读写时。
图、页: 页是 InnoDB 存储数据的基本单元，标准大小为 16 KB，索引树上的一个节点就是一个页。

也就意味着数据库每次读写都是以 16 KB 为单位的，一次最少从磁盘中读取 16KB 的数据到内存，一次最少写入
16KB 的数据到磁盘。

图、行: InnoDB 采用行存储方式，意味着数据按照行进行组织和管理，行数据可能有多个格式，比如说
COMPACT、REDUNDANT、DYNAMIC 等。

MySQL 8.0 默认的行格式是 DYNAMIC，由COMPACT 演变而来，意味着这些数据如果超过了页内联存储的限制，
则会被存储在溢出页中。

No. 371 302




## 第 38 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

可以通过 show table status Like 'sarticles' 查看行格式。

火火火火大火火火大火火火火火大火火火大火火火火火大火大 不 。 三OW 大大大火大大火火大火炎大火火大火火大大火大火火大大火炎

Name: coLumn_articte
Engine: InnoDB
Version: 10
Row_format: Dynamic
一3
Avg_row_Length: 5461
Data_Length: 16384
Max_data_Length: 0
Index_Length: 16384
Data_free: 0
Auto_increment: 4
Create_time: 2023-12-29 16:32:53
Update_time: NULL
Check_time: NULL
CoLLation: utf8mb4_0900_ai_ci
Checksum: NULL
Create_options :
Comment: 专栏文章列表
4 rows in set (0.01 sec)

存储引擎
24.二MySQL 有哪些常见存储引擎?

MySQL 支持多种存储引擎，常见的有 MylISAM、InnoDB、MEMORY 等。

---这部分是帮助大家理解 start，面试中可不背---

No. 381302




## 第 39 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

支持事务

支持行级锁

InnoDB
支持外键

MySQL 默认存储引擎

不支持事务
存储引擎@沉默王二

支持表级锁

不支持外键

MEMORY             存储在内存

我来做一个表格对比:

功能                                         InnoDB                     MylSAM                      MEMORY
支持事务                                         Yes                                No                                   No
支持全文索引                              Yes                           Yes                             No
支持 B+树索引                            Yes                           Yes                             Yes
支持哈希索引                              Yes                           No                              Yes
支持外键                                         Yes                                No                                   No

---这部分是帮助大家理解 end，面试中可不背---

除此之外，我还了解到:

外、MySQL 5.5 之前，默认存储引警是 MylISAM，5.5 之后是 InnoDB。
InnoDB 支持的哈希素引是自适应的，不能人为干预。

InnoDB 从 MySQL 5.6 开始，支持全文索引。

InnoDB 的最小表空间略小于 10M，最大表空间取决于页面大小。

8 8 8

No. 391302




## 第 40 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

InnoDB Page Size| Maximum Tablespace Size
4KB                      16TB

8KB                      32TB

16KB                      64TB

32KB                      128TB

64KB                    256TB

如何切换 MySQL 的数据引擎?
可以通过 alter table 语句来切换 MySQL 的数据引擎。

RALTER TRBLE Your_ table_name ENGINE=InnoDB7

不过不建议，应该提前设计好到底用哪一种存储引擎 。

1. Java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: MySQL 支持哪些存储
引擎?

2. java 面试指南 (付费) 收录的用友面试原题: innodb 引擎和 hash 引擎有什么区别
3. Java 面试指南 (付费) 收录的国企零碎面经同学 9 面试原题: MySQL 的存储引擎

4. Java 面试指南 (付费) 收录的京东同学 4 云实习面试原题: mysql的数据引擎有哪些, 区别
(innodb,MylISAM,Memory)

5. Java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题; 存储引擎介绍
memo: 2025年3月10 日修改至此。

25.存储引擎应该怎么选择?

大多数情况下，使用默认的 InnoDB 就可以了，InnoDB 可以提供事务、行级锁、外键、B+ 树索引等能力。
MyISAM 适合读多写少的场景。

MEMORY 适合临时表，数据量不大的情况。因为数据都存放在内存，所以速度非常快。

1. java 面试指南 (付费) 收录的快手同学 2 一面面试原题: MySQL的InnoDB特点? 为什么用B+树?而不
是B树，区别?

26.InnoDB 和 MylSAM 主要有什么区别?

No. 401302




## 第 41 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

InnoDB 和 MylSAM 的最大区别在于事务支持和锁机制。InnoDB 支持事务、行级锁，适合大多数业务系统; 而
MyISAM 不支持事务，用的是表锁，查询快但写入性能差，适合读多写少的场景。

MyYISAM和InnoDB区别
挛钨
索引类型                        Co乡                               表行数

另外，从存储结构上来说，MyISAM 用三种格式的文件来存储，.frm 文件存储表的定义; .MYD 存储数据; .MYI 存
储索引，而 InnoDB 用两种格式的文件来存储，.frm 文件存储表的定义; .ibd 存储数据和索引。

从索引类型上来说，MyISAM 为非聚簇索引，索引和数据分开存储，索引保存的是数据文件的指针。

本
一

50

0Ox37             0x4             0x50 0x6                                  user_myisam.MYD

(64,F13,1)

人>Ox50|        (61,E,14,1)

和> Ox4          (60,A,15,1)

(50.B,12,0)

(40,C,20.1)

(20,D,20,1)

No. 411302




## 第 42 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

InnoDB 为聚簇索引，索引和数据不分开。

柄强 一

一亲]  面 |

者站-请忆-上证-恒东

更细微的层面上来讲，MyISAM 不支持外键，可以没有主键，表的具体行数存储在表的属性中，查询时可以直接返
回; InnoDB 支持外键，必须有主键，具体行数需要扫描整个表才能返回，有索引的情况下会扫描索引。

InnoDB的内存结构了解吗?

2025 年 04 月 04 日增补

InnoDB 的内存区域主要有两块，buffer pool 和 log buffer。
buffer pool 用于缓存数据页和索引页，提升读写性能; log buffer 用于缓存 redo log，提升写入性能。

No. 421302




## 第 43 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

In-Memory Structures                                           On-Disk Structures
Buffer Pool        |               Sat全Pace
File-Per-Table
国   国口目口目  Iaaas       InnoDB Data              Tablespaces
首 国   国国    国 国             Dictionary          innodb_file_per_table=ON
三      ]                                   CD    CD
三                        1    ]
起 口   国国国国 四    1     |          Doublewrite Buffer         国上    证
工                        1    ]
羡国   国口国口上                                  tlibd tibd
站 口                              1                Change Buffer
1    ]
国国口口国  ，      |                                  General Tablespaces
日国国国上日 ol             Undo Logs               tslibd
r------------ | |                                   如 _t4 45
| changeBuffer | | 和< |         TD IF < 走 媒 aaa       重         ts2,ibd
      ndo Tablespaces           目
|国目口口国| 从  |      pa   |    tt8 e
1
!国四图目日| | | oo | |
1    ]    1           昌         1
      |         (system)        ]
|      |      4                       :    | Temporary
和      |      中                            1 Tablespaces  )
1         1             Redo Log             1 1 r-------，    |
1      ]      1                Y       ]    !   | ibtmp1l |   1
Log Buffer      1                        1    | 1 (global /|
->     一一~                  一一  1
日目日@目一    加   区 |
1                   1
|      |      | ibToegfieo ibTogfiel |
 |       4       |
数据页的结构了解吗?

InnoDB 的数据页由 7 部分组成，其中文件头、页头和文件尾的大小是固定的，分别为 38、56 和 8 个字节，用来
标记该页的一些信息。行记录、空闲空间和页目录的大小是动态的，为实际的行记录存储空间。

No. 431302




## 第 44 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

InnoDB数据页结构示意图

File Header (38字节)

Page Header (56字节)

Infimum + supremum (26字节)

User Records (大小不确定)

Free Space (大小不确定)

Page Directory (大小不确定)

File Trailer (8字节)

来个表格总结下:

名称

File Header

Page Header
Infimum + Supermum
User Records

Free Space

Page Directory

File Trailer

中文名

文件头部

页面头部

最小记录和最大记录
用户真实记录

空闲空间

页面目录

文件尾部

大小 (单位: B)

38

No. 44 1 302

这些是记录

描述

页的一些通用信息
数据页专有的一些信息
两个虚拟的行记录
实际存储的行记录内容
页中尚未使用的空间

页中的某些记录的相对位置

校验页是否完整




## 第 45 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

真实的记录会按照指定的行格式存储到 User Records 中。

新申请的数据页                                           依次插入记录                                            数据页插满记录

File Header                                           File Header                                          File Header

Page Header                                         Page Header                                         Page Header

Infmum + Supremum                                Infmum + Supremum                                Infmum + Supremum
只          urnecords | 目EE    路         ornecorts |上

Free Space

Free Space                                 (Free Space被用完了)    [aaN_ |]

Page Directory                                     Page Directory                                    Page Directory

File Trailer                                               File Trailer                                               File Trailer

每个数据页的 File Header
都有一个上一页和下一页的编号，所有的数据页会形成一个双向链表。

数据页1               数据页2               数据页3                             数据页n
和|                                                                                           je
Fie Header                               File Header                               File Header                              File Header
-~                                            -~                                            <                             <
Page Header                             Page Header                             Page Header                                                            Page Header
infmum + Supermum                  Inhmum + Supermum                  infmum + Supermum                                             infmum + Supermum

User Records

User Records                           User Records                           User Records
Free Space                              Free Space                               Free Space                                                             Free Space
Page Directory                          Page Directory                          Page Directory                                                        Page Directory
File Trailer                                  File Trailer                                  File Trailer                                                                    File Trailer

在InnoDB 中，默认的页大小是 16KB。可以通过 show variables like 'innodb_ page _size'; 查看。

mySsqL> Show VvariabLes Like "innodb_page_Ssize ';

推荐阅读: MySQL之数据页结构

1. Java 面试指南 (付费) ，
的区别有哪些?

2. java 面试指南 (付费) 收
memo: 2025年3月11 日修改至此。

术一面面试原题: MylSAM 和 InnoDB

mysql存储由

No. 451302




## 第 46 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

27. InnoDB 的Buffer Pool了解吗? (补充)

2024年11 月 04 日增补
Buffer Pool 是 InnoDB 存储引擎中的一个内存缓冲区，它会将经常使用的数据页、索引页加载进内存，读的时候
先查询 Buffer Pool，如果命中就不用访问磁盘了。

InnoeDB 4rcnitecture in NAYSQL

Queryresvkt

Operating System Coache

O_PIREcT   人

如果没有命中，就从磁盘读取，并加载到 Buffer Pool，此时可能会触发页淘汰，将不常用的页移出 Buffer Pool。

@@O极客时间

写操作时不会直接写入磁盘，而是先修改内存中的页，此时页被标记为脏页，后台线程会定期将脏页刷新到磁盘。
Buffer Pool 可以显著减少磁盘的读写次数，从而提升 MySQL 的读写性能。

Buffer Pool 的默认大小是多少?

我本机上 InnoDB 的 Buffer Pool 默认大小是 128MB。
SHOW VRRIRBLES LIKE "innodb buffer_pool_size' 7

No. 46 1302




## 第 47 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

另外，在具有 1GB-4GB RAM 的系统上，默认值为系统 RAM 的 25%; 在具有超过 4GB RAM 的系统上，默认值为
系统 RAM 的 50%，但不超过 4GB。

mysqL> SHOW VARIABLES LIKE "innodb_buffer_poot_size ';

| innodb_buffer_pooL_size | 134217728 |
十-                         -十
1 row in set (0.00 sec)

InnoDB 对 LRU 算法的优化了解吗?
了解，InnoDB 对 LRU 算法进行了改良，最近访问的数据并不直接放到 LRU 链表的头部，而是放在一个叫
midpoiont 的位置。默认情况下，midpoint 位于 LRU 列表的 5/8 处。

midpoint

-|
新生代                     老年代

比如 Buffer Pool 有 100 页，新页插入的位置大概是在第 80 页; 当页数据被频繁访问后，再将其移动到young
区，这样做的好处是热点页能长时间保留在内存中，不容易被挤出去。

-这部分是帮助大家理解 start，面试中可不背-…-

可以通过 innodb_old_blocks_pct 参数来调整 Buffer Pool 中 old 和 young 区的比例; 通过
innodb_old_blocks_time 参数来调整页在 young 区的停留时间。

No. 471302




## 第 48 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqtL> SHOW VARIABLES LIKE "innodb_otLd_bLocks_pct ' ;

1 row in set (0.00 sec )

mysqL> SHOW VARIABLES LIKE "innodb_oLd_btocks_time ';

默认情况下，LRU 链表中 old 区占 37%; 同一页再次访问提升的最小时间间隔是 1000 毫秒。
也就是说， 如果某页在 1 秒内被多次访问，只会计算一次，不会立刻升级为热点页，防止短时间批量访问导致缓存

----这部分是帮助大家理解end，面试中可不背
1                 收录的美团面经

学 15 点评后端#

说说 bufferpool

memo: 2025年3月12 日修改至此。继续给大家一个喜报，今天         说社招拿到了京东和美团的 offer,，
后续补充说滴滴也过了，我只能说太强了呀。

二哥，目前两个offer，社招
京东零售会员 _n*19
美团小象超市履约配送 (n+4)* 15.5

怎么选啊

n+4 我

十
AN

28.二MySQL 日志文件有哪些?

有 6 大类，其中错误日志用于问题诊断，慢查询日志用于 SQL 性能分析，general log 用于记录所有的 SQL 语
句，binlog 用于主从复制和数据恢复，  redo log 用于保证事务持久性，undo log 用于事务回滚和 MVCC。

No. 481302




## 第 49 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

错误日志

ettor log

重做上日志            回滚日志

redo log                               undo log

-一这部分是帮助大家理解 start，面试中可不背---
外、错误日志 (Error Log) : 记录 MySQL 服务器启动、运行或停止时出现的问题。

@@、慢查询日志 (Slow Query Log) : 记录执行时间超过long_query_time 值的所有 SQL 语句。这个时间值是可
配置的，默认情况下，慢查询日志功能是关闭的。

图、一般查询日志 (General Query Log) : 记录 MySQL 服务器的启动关闭信息，客户端的连接信息，以及更
新、查询的 SQL 语句等。

图、二进制日志 (Binary Log) : 记录所有修改数据库状态的 SQL 语句，以及每个语句的执行时间，如 INSERT、
UPDATE、DELETE 等，但不包括 SELECT 和 SHOW 这类的操作。

@@、重做日志 (Redo Log) : 记录对于 InnoDB 表的每个写操作，不是 SQL 级别的，而是物理级别的，主要用于
崩溃恢复。

@@、回滚日志 (Undo Log，或者叫事务日志) : 记录数据被修改前的值，用于事务的回滚。
-这部分是帮助大家理解end，面试中可不背---

请重点说说 binlog?

推荐阅读: 带你了解 MySQL Binlog 不为人知的秘密

binlog 是一种物理日志，会在磁盘上记录数据库的所有修改操作。

如果误删了数据，就可以使用 binlog 进行回退到误删之前的状态。

# 步骤1: 恢复全量备份

mysql -u root -pP < ful1_backup.sql

# 步骤2: 应用Binlog到指定时间点

mysqlbinlog --start-datetime="2025-03-13 14:00:00”--stop-datetime="2025-03-13 15:00:00"
binlog.000001 | mysql -u root -Pp

如果要搭建主从复制，就可以让从库定时读取主库的 binlog。

No. 491302




## 第 50 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

浊合，

MySQL 提供了三种格式的 binlog: Statement、Row 和 Mixed，分别对应 SQL 语句级别、行级别和混合级别，默
认为行级别。

mysqL> SHOW VARIABLES LIKE "binLog_format ' ;

从后缀名上来看，binlog 文件分为两类: 以 .index 结尾的索引文件，以 .00000* 结尾的二进制日志文件。
binlog 默认是没有启用的。
生产环境中是一定要启用的，可以通过在 my.cnf 文件中配置 log_bin 参数，以启用 binlog。

1og_bin = mysql-bin #开启binlog

4mysql-bin.x日志文件最大字节 (单位: 字节)
#设置最大100MB
max_binlog size=104857600

#设置了只保留7天BINLOG (单位: 天)
expire_logs_days = 7

#binlog日志只记录指定库的更新
#binlog-do-db=db_name

#binlog日志不记录指定库的更新
#binlog-ignore-db=db_name

#写缓冲多少次，刷一次磁盘，默认0
sync_binlog=0

binlog 的配置参数都了解哪些?

1og_bin = mysql-bin 用于启用 binlog，这样就可以在 MySQL 的数据目录中找到 db-bin.000001、db-
bin.000002 等日志文件。

No. 501302




## 第 51 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

/usr/LocatL/mysqt/data (0.095s)
1Ls

auto.cnf                    itwanger .LocatL.err
cmower                             itwanger.LocaL.pid
cmower_13.5SDI                    itwanger .Log
codingmore                       itwanger_33.SDI

codingmore_19.5SDI           jeesite                     pai_coding_31.SDI
tib_buffer_poolL              jeesite_10.SDI              performance_sche_3.5SDI
ib_LogfiLe0                 jepf                        performance_schema
ib_LogfitLe1                      jepf_8.SDI                       pmhub

ibdatal1                       LaitgeofferG002dpmhub         pmhub_34.SDI

ibtmp1                        LaigeofferGQ002dpmhub_35.SDI sys

itwanger                          mysqtL                              SyS_4.SDI

max_binlog_size=104857600 用于设置每个 binlog 文件的大小，不建议设置太大，网络传送起来比较麻烦。
当 binlog 文件达到 max_binlog_size 时，MySQL 会关闭当前文件并创建一个新的 binlog 文件。

expire_logs_days = 7 用于设置 binlog 文件的自动过期时间为 7 天。过期的 binlog 文件会被自动删除。防止
长时间累积的 binlog 文件占用过多存储空间，技术派实战项目所在的项目是下版服务器，所以这个配置很重要。

binlog-do-db=db_name ，指定哪些数据库表的更新应该被记录 。
binlog-ignore-db=db_name ，指定忽略哪些数据库表的更新。

sync_binlog=0 ，设置每多少次 binlog 写操作会触发一次磁盘同步操作。默认值为0，表示 MySQL 不会主动触
发同步操作，而是依赖操作系统的磁盘缓存策略。

即当执行写操作时，数据会先写入缓存，当缓存区满了再由操作系统将数据一次性刷入磁盘。
如果设置为 1，表示每次 binlog 写操作后都会同步到磁盘，虽然可以保证数据能够及时写入磁盘，但会降低性
能。

可以通过 show variables like '%1log_bins'; 查看 binlog 是否开启。

mysqL> Show variabLes Like “5%55Log_bins ' ;

Log_bin_basename

Log_bin_index
Log_bin_trust_functiton_creators
Log_bin_use_Vv1_row_events
sqL_Log_bin

rows in set (0.01 sec )

No. 511302




## 第 52 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

有了binlog为什么还要undolog redolog?

binlog 属于 Server 层，与存储引擎无关，无法直接操作物理数据页。而 redo log 和 undo log 是InnoDB 存储引
擎实现 ACID 的基石。

binlog 关注的是逻辑变更的全局记录; redo log 用于确保物理变更的持久性，确保事务最终能够刷盘成功; undo
log 是远辑逆向操作日志，记录的是旧值，方便恢复到事务开始前的状态。

另外一种回答方式。

binlog 会记录整个 SQL 或行变化; redo log 是为了恢复“已提交但未刷盘“的数据，undo log 是为了撤销未提交的
事务。

以一次事务更新为例:

# 开启事务

BEGIN7

# 更新数据

UPDRTE users SET age = age + 1 WHERE id = 17
# 提交事务

COMMIT
事务开始的时候会生成 undo log，记录更新前的数据，比如原值是 18:
undo log: id=-1，age=18

修改数据的时候，会将数据写入到 redo log。
比如数据页 page_id=123 上，id=1 的用户被更新为 age=26:

redo 1og (prepare) :
page_id=123，offset=0x40，before=18，after=26

等事务提交的时候，redo log 刷盘，binlog 刷盘。

binlog 写完之后，redo log 的状态会变为 commit:

redo 1og (commit) :
page_id=123，offset=0x40，before=18，after=26

binlog 如果是 Statement 格式，会记录一条 SQL 语句:
UPDRTE users SET age = age + 1 WHERE id = 17
binlog 如果是 Row 格式，会记录:

表: users
before: id=1，age=18
after: id=1，age=26

No. 52 1 302




## 第 53 页


面尖逆区MySQL篇V2-让天下所有的面洁都能逆装
随后，后台线程会将 redo log 中的变更异步刷新到磁盘。

memo: 2025年3月13 日修改至此。有球友报喜，字节二面过了，找暑期顺利的不可思议，八股直接吟唱面
渣。

二哥，我做题面的字节二面，今天微信问她说是
通过了，但是要等安排hr给我面试

这个步骤会出差错吗? 真的好慌

好哺，那我就放心了

找暑期顺利到不可思议图

二哥的八股太好用辣

常规八股直接吟唱

说说 redo log 的工作机制?

当事务启动时，MySQL 会为该事务分配一个唯一标识符。

在事务执行过程中，每次对数据进行修改，MySQL 都会生成一条 Redo Log，记录修改前后的数据状态。
这些 Redo Log 首先会被写入内存中的 Redo Log Buffer。

No. 531302




## 第 54 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mySsqL> SHOW VARIABLE9S LIKE "innodb_Log_buffer_size ';

1 row in set (0.00 sec)

当事务提交时，MySQL 再将 Redo Log Buffer 中的记录刷新到磁盘上的 Redo Log 文件中。
只有当 Redo Log 成功写入磁盘，事务才算真正提交成功。

InnoDB存储引擎

2.直接更新缓存数据  和              |

缓冲池                                              重做日志缓存

(Buffer Pool)                   (Redo Log Buffem)

1.磁盘加载数据放入缓冲池                                4.清空Redo Log Buffer
刷盘到Redo日志中
了
GreatSQL社区
redo.file
硬盘

当 MySQL 崩溃重启时，会先检查 Redo Log。对于已提交的事务，MySQL 会重放 Redo Log 中的记录。

No. 541302




## 第 55 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

MysQL
InnoDB存储引擎           重启

[一实例挂了或宕机了 一

当发生宕机且数据未刷到磁盘的时候，可以通过Redo Log来恢复

redo.file

对于未提交的事务，MySQL 会通过 Undo Log 回滚这些修改，确保数据恢复到崩溃前的一致性状态。

Redo Log 是循环使用的，当文件写满后会覆盖最早的记录。

为避免绪盖未持久化的记录，MySQL 会定期执行 CheckPoint 操作，将内存中的数据页刷新到磁盘，并记录

CheckPoint 点。

事务提交结束
tna ine 二2000                                                                                       人                       9
update
data_ in_ buffer lsn
LSN 800
data_page_ on
-4                                                                                                                                                  LSN 800
i
redo log in_
buffer_ hn                         LSN 110           LSN 150           LSN 300 ! | LSN300         LSN 800 ”LSN 800
1
redo log on                                                                         1
_disk lsn                                                                                          SN 300                                                LSN 800
checkpoint lsn                                                                       四|                                                  1
45| 300                             LSN 800
i   久、                                checkpoint出现
初始LSN                                               checkpoint ”checkpoint
100                                出现    局盘完成

重启时，MySQL 只会重放 CheckPoint 之后的 Redo Log，从而提高恢复效率。
redo log 文件的大小是固定的吗?

redo log 文件是固定大小的，通常配置为一组文件，使用环形方式写入，旧的日志会在空间需要时被覆盖。

No. 551302




## 第 56 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

redo日志文件组示意氏

。          ib logfile n

ib logfile 0         ib logfile 1

命名方式为 ib_logfile0、iblogfilel、、、iblogfilen 。默认 2 个文件，每个文件大小为 48MB。

mysqL mysqL    3591 0ct 19 17:54 ib_ buffer_pool
mysqL mysqL 12582912 0ct 19 17:59_ibdatal

mysqL mysqL 56331648 0ct 19 18:9
mysqL mysqL 560331648 QSt 19 17:11 ib Logfitel
mysqL mysqL 12582912 na
mysqL mysqL    4996 0ct 19 17:54

mysqL mysqL    4096 0ct 19 17:11

可以通过 show variables like 'innodb log file_size'; 查看 redo log 文件的大小; 通过 show
variables like 'innodb log files_in_group'; 查看 redo log 文件的数量。

mysqL> SHOW VARIABLES LIKE 'innodb_Log_fitLes_in_group ';

| 1 -09- fiLes_in_group | 2
十--

1 row in set (0. .00 Sec)

mysqL> SELECT einnod  Log_fiLe_size/1024/1024 AS 'innodb_Log_fiLe_size
+------               =-+

| Moon _1og_ fite_ Size (MB) |
十         二---

+一
1 row in set (0.00 sec)

说说 WAL?
WAL一一Write-Ahead Logging。

预写日志是 InnoDB 实现事务持久化的核心机制，它的思想是: 先写日志再刷磁盘。

No. 561302




## 第 57 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

即在修改数据页之前，先将修改记录写入 Redo Log。
这样的话，即使数据页尚未写入磁盘，系统崩溃时也能通过 Redo Log 恢复数据。
-一这部分是帮助大家理解 start，面试中可不背---
解释一下为什么需要 WAL:
。 数据最终是要写入磁盘的，但磁盘 IO 很慢;
。 如果每次更新都立刻把数据页刷盘，性能很差;
。 如果还没写入磁盘就宕机，事务会丢失。
WAL 的好处是更新时不直接写数据页，而是先写一份变更记录到 redo log，后台再慢慢把真正的数据页刷盘，一

举多得。
-这部分是帮助大家理解 end，面试中可不背-一

1. Java 面试指南 (付费) 收录的华为面经同学 8 技术二面面试原题: MySQL 中的 bin log 的作用是什
么?

2. java 面试指南 (付费) 收录的美团面经同学 2 java 后端技术一面面试原题: 说说 MySQL 的三大日志?

No. 571302




## 第 58 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

3. Java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: redolog undolog
binlog，有了binlog为什么还要undolog redolog，redolog的工作机制，说说 WAL

memo: 2025年3月14 日修改至此。今天修改简历的时候，碰到一位比赛经历韭党丰富的球友，大家在校期间
如果有时间，也可以冲一下。

S 获奖情况

金牌, 2024 年中国大学生程序设计竞赛全国邀请赛 (山东)

银牌, 2024 ICPC 亚洲南京赛区赛

银牌, 2024 ICPC 亚洲杭州赛区赛

铜牌, 第 10 届 CCPC 中国大学生程序设计竞赛郑州站

满分, 第 36 次 CCF 计算机软件能力认证

市级一等奖, 第十届杭州市大学生科技创新大赛

全国三等奖, 第十五届中国大学生服务外包创新创业大赛

省级三等奖,浙江省第十四届”" 挑战杯”中国大学生创业计划竞赛

29.binlog 和 redo log 有什么区别?

binlog 由 MySQL 的 Server 层实现，与存储引擎无关; redo log 由 InnoDB 存储引警实现。

No. 581302




## 第 59 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

MySQL分层与redo log binlog

binlog文件，由server层产生，可
配置是否打开该日志，默认存放
在data文件夹下。

四 “四

mysql-bin.000001 mysqi-bin.000002

redo |og文件，是innodb特有日
志，由引擎层生成。

局

ib_logfleo 。ib_logfile1

binlog 记录的是逻辑日志，包括原始的 SQL 语句或者行数据变化，例如"将 id=2 这行数据的 age 字段+1"。
redo log 记录物理日志，即数据页的具体修改，例如"将 page_id=123 上 offset=0x40 的数据从 18 修改为 26"。

binlog 是追加写入的，文件写满后会新建文件继续写入，不会覆盖历史日志，保存的是全量操作记录; redo log
是循环写入的，空间是固定的，写满后会覆盖旧的日志，仅保存未刷盘的脏页日志，已持久化的数据会被清除。

另外，为保证两种日志的一致性，innodb 采用了两阶段提交策略，redo log 在事务执行过程中持续写入，并在事
务提交前进入 prepare 状态; binlog 在事务提交的最后阶段写入，之后 redo log 会被标记为 commit 状态。

可以通过回放 binlog 实现数据同步或者恢复到指定时间点; redo log 用来确保事务提交后即使系统宕机，数据仍
然可以通过重放 redo log 恢复。

1. Java 面试指南 (付费) 收录的美团同学 2 优选物流调度技术 2 面面试原题: redo log、bin log

30.二 为什么要两阶段提交呢?

为了保证 redo log 和 binlog 中的数据一臻性，防止主从复制和事务状态不一致

No. 591302




## 第 60 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

+ransacf+ion commi

write redo log

一阶段提交                  (prepare)

write binlog

二阶段提交

(committed)

为什么 2PC 能保证 redo log 和 binlog 的强一致性?

假如 MySQL 在预写 redo log 之后、写入 binlog 之前崩溃。那么 MySQL 重启后 InnoDB 会回滚该事务，因为
redo log 不是提交状态。并且由于 binlog 中没有写入数据，所以从库也不会有该事务的数据。

No. 601302




## 第 61 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

有完整的 commi++ed 数据

check redo log

有完整的 prepare 数据

有完整的 binlog 数据
check binlog

没有完整的 binlog 数据

假如 MySQL 在写入 binlog 之后、redo log 提交之前崩溃。那么 MySQL 重启后 InnoDB 会提交该事务，因为
redo log 是完整的 prepare 状态。并且由于 binlog 中有写入数据，所以从库也会同步到该事务的数据。

伪代码如下所示:

// 事务开始

beginy

V// ty

{
// 执行 SOL
execute SOL;

// 写入 redo 1og 并标记为 prepare
write redo 1og prepare xid)

// 写入 binlog
write binlog xid sql17

// 提交 redo log
commit redo 1og xiqd

)
// catch

{
// 回滚 redo log
innodb rollback redo 1og xid)

)}

// 事务结束

No. 611302




## 第 62 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭
endi7

XID 了解吗?
XID 是 binlog 中用来标识事务提交的唯一标识符。

binary_log::Binary

binary_log::Xid_event               Xid_apply_log_event

Xid_log_event

在事务提交时，会写入一个XID_EVENT 到 binlog，表示这个事务真正完成了。

Log_name      | Pos | Event_type    | Server_id | End_ log pos | Info

| mysql-bin.000003 | 2005 | Gtid       | 1013307 |     2070 | SET
eeSESSION.GTID_NEXT= 'f971d5fl-d450-1lec-9e7b-5254000a56df:11，            |

| mysql-bin.000003 | 2070 | ouery       | 1013307 |     2142 | BEGIN

|

| mysql-bin.000003 | 2142 | Table_map    | 1013307 |     2187 | table_id: 109
(test.tl)

| mysql-bin.000003 | 2187 | Write_rows    | 1013307 |     2227 | table_id: 109

flags: STMT_END_F
| mysql-bin.000003 | 2227 | Xid
/

COMMIT /* Xid=121

1013307 |       2258

它不仅用于主从复制中事务完整性的判断，也在崩溃恢复中对 redo log 和 binlog 的一致性校验起到关键作用。

XID 可以帮助 MySQL 判断哪些 redo log 是已提交的，哪些是未提交需要回滚的，是两阶段提交机制中非常关键的
一环。

memo: 2025年3月16 日修改至此。

31. redo log 的写入过程了解吗?

InnoDB 会先将 Redo Log 写入内存中的 Redo Log Buffer，之后再以一定的频率刷入到磁盘的 Redo Log File 中。

No. 621302




## 第 63 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

内存 |        tedo log buffet        ]

fsync      2和商

哪些场景会触发 redo log 的刷盘动作?
比如说 Redo Log Buffer 的空间不足时，事务提交时，触发 Checkpoint 时，后台线程定期刷盘时。

不过，Redo Log Buffer 刷盘到 Redo Log File 还会涉及到操作系统的磁盘缓存策略，可能不会立即刷盘，而是等
待一定时间后才刷盘。

No. 631302




## 第 64 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

让

参数你了解多少?

gat trx_commit

innodb flush_lo:

种。

时，Redo Log 的刷盘策略，一共有

交

commit 参数是用来控制事务提

log_at_trx_

innodb _flush_lo

No. 641302




## 第 65 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

JInnodb_flush_log _at_trx_commit= 1

I   jb flush 1                                         File
nnodb_flush log at_trx_commit= 2         106            System                   ，
                              BUFFER          Buffer           es

Innodb_flush_log_at_trx_commit= 0

[

0 表示事务提交时不刷盘，而是交给后台线程每隔 1 秒执行一次。这种方式性能最好，但是在 MySQL 宕机时可能
会丢失一秒内的事务。

1 表示事务提交时会立即刷盘，确保事务提交后数据就持久化到磁盘。这种方式是最安全的，也是 InnoDB 的默认

mysqL> SHOW VARIABLES LIKE 'innodb_fLush_Log_at_trx_commit ' ;

十~----

| Var

》

十----
| innodb_ftLus

1 row in set (0.01 sec )

2 表示事务提交时只把 Redo Log Buffer 写入到 Page Cache，由操作系统决定什么时候刷盘。操作系统宕机时，
可能会丢失一部分数据。

一个没有提交事务的 redo log，会不会刷盘?

InnoDB 有一个后台线程，每隔 1 秒会把 Redo Log Buffer 中的日志写入到文件系统的缓存中，然后调用刷盘操
作。

InnoDB存储引擎

重做日志缓存
(Redo Log Buffen)

文件系统缓存
(page cache)

1S刷新一次

>人yy- |   后台线程

GreatSQL
社区

No. 651302




## 第 66 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

因此，一个没有提交事务的 Redo Log 也可能会被刷新到磁盘中。
另外，如果当 Redo Log Buffer 占用的空间即将达到 innodb_log_buffer_size 的一半时，也会触发刷盘操作。
memo: 2025年3月17 日修改至此。已经有球友发来喜报，暑期实习拿到恒生电子的暑期实习了 。

全  沉默王二                                            起 收进专栏
202  )3-16 22:51  读人数 4

”提问: 二哥您好，感谢您之前对简历的修改和指点，先报个喜，开学第一周boss投了
四天约了十家面试基本上都cc了，但是都是小广，原本想着接着一步一步往大了投，发现
自己不愿面了，然后现在选了杭州的恒生电子实习，因为双非0实习 (那实习是前端实习
包装的) 能进稍微规模大点的公司实习一步一步来，先真正有个后端实习，我已经挺满意

Redo Log Buffer 是顺序写还是随机写?

MySQL 在启动后会向操作系统申请一块连续的内存空间作为 Redo Log Buffer，并将其分为若干个连续的 Redo
Log Block。

Redo Log Buffer
人

Block 1             Block 2             Block 3             Block 4             Block 5

那为了提高写入效率，Redo Log Buffer 采用了顺序写入的方式，会先往前面的 Redo Log Block 中写入，当写满
后再往后面的 Block 中写入。

外    全、放大，                Log Buffer 结构示意图
LE |                  已被填充满的                已被填充满的                                              ee
已被十充满的             ~           Log Block Body             Log Block Body             Log slod body               站呈
Log BlockBody                    己基的                                                                     Le Biodkeedy
让              Log Block Body              Log Block Body
Log sloc mailer                      Log Block Trailer           Log Block Trailer           Log Block Trailer                    Log Block Tailer
一一

这些block都以及填满了Redo日志，已经没有空闲的空间了

No. 661302




## 第 67 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

于此同时，InnoDB 还提供了一个全局变量 buf_free，来控制后续的 redo log 记录应该写入到 block 中的哪个位
置。

buf_next_ to_write 了解吗?

buf_next_to_write 指向 Redo Log Buffer 中下一次需要写入硬盘的起始位置。

Redo Log Buffer

此部分Redo Log
已被写入到硬盘         此部分Redo Log还未写入到硬盘

buf_next_to_write                            buf_free

而 buf_free 指向的是 Redo Log Buffer 中空闲区域的起始位置。

了解 MTR 吗?
Mini Transaction 是 InnoDB 内部用于操作数据页的原子操作单元。

mtr 七 mt
mtr_start(&mtr) 7

// 1. 加锁

// 对待访问的index加锁
mtr_s_lock(rw_lock 七，mtr) 1
mtr_x_lock(rw_lock 七，mtr) 1

// 对待读写的page加锁
mtr_memo_push(mtr，buf_block 七，MTR_MEMO_PRGE S_FIX) 7
mtr_memo_push(mtr，buf_block 七，MTR_MEMO_PRGE X_FIX) 7

// 2. 访问或修改page
btr_cur_search_to_nth_level
btr_cur_optimistic_insert

// 3. 为修改操作生成redo

mlog_open
mlog_ write_initial 1og record fast

No. 671302




## 第 68 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

mlog_close

// 4. 持久化redo，解锁

mtr_commit (&mtr) 7

多个事务的 Redo Log 会以 MTR 为单位交替写入到 Redo Log Buffer 中，假如事务 1 和事务 2 均有两个 MTR，一
旦某个 MTR 结束，就会将其生成的若干条 Redo Log 记录顺序写入到 Redo Log Buffer 中。

Redo Log Buffer

Block 1            Block 2            Block 3            Block 4           Block 5

事务下MTR1中全
部的redo log记录

也就是说，一个 MTR 会包含一组 Redo Log 记录，是 MySQL 崩溃后恢复事务的最小执行单元。

No. 681302




## 第 69 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

SQL语句 1
redo log 记录 1

SQL语句2 | MTR1 | redolog记录2
MTR 2       redo log 记录 3

宇务      SQL语句3 < MTR 3
redo log 记录 n

MTR n

SQL语句 n

Redo Log Block 的结构了解吗?

Redo Log Block 由日志头、日志体和日志尾组成，一共占用 512 个字节，其中日志头占用 12 个字节，日志尾占
用 4 个字节，剩余的 496 个字节用于存储日志体。

ea                redo log block结构

~ 12B

总共是512B 人 496字节

508B

` 512B

日志头包含了当前 Block 的序列号、第一条日志的序列号、类型等信息。

No. 691302




## 第 70 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

字段                                                    作用

当前 Block 的序号，假如把 Redo Log Buffer 看成一个数组，那么

LOc-8LOCKGCHDRNO                 LOG_BLOCK_HDR_NO 就相当于 Block 在 Buffer 中的下标。

Block 已使用的字节数，初始值为 12，也就是日志头的长度; 如果日志
LOG_BLOCK_HDR_DATA_LEN       体被写满，值增长为 512。
LOG_BLOCK_FIRST_REC_GROUP 该 Block 中第一个 MTR 起始处的偏移量

LOG_BLOCK_CHECKPOINT_NO        Block 最后被写入时的checkpoint

志尾主要存储的是 LOG_BLOCK_CHECKSUM，也就是 Block 的校验和，主要用于判断 Block 是否完整。

Redo Log Block 为什么设计成 512 字节?

因为机械硬盘的物理扇区大小通常为 512 字节，Redo Log Block 也设计为同样的大小，就可以确保每次写入都是
整数个扇区，减少对齐开销。

redo log buffer
王认大小16MB
时面划分了NT rodo log block

|     Header (12byte)    ]    |     Header (12byte)    ]   |     Header (12byte)    |
redo log 数据                                  redo log 数据                                 redo log 数据      j
>
Body (496byte)        Body (496byte)       Body (496byte)
   Leeoeoag ]      [ET     [esoogm昌                oo
| raw | | mms | | ran |           玖

于和提交时会持久化
edo og bufer 占用的空间达到 nnngp log_bufer_sze一兴空间时持久化
并生事物提交般基3多化

比如说操作系统的页缓存默认为 4KB，8 个 Redo Log Block 就可以组合成一个页缓存单元，从而提升 Redo Log
Buffer 的写入效率。

memo: 2025年3月18 日修改至此。
LSN 了解吗?

Log Sequence Number 是一个 8 字节的单调递增整数，用来标识事务写入 redo log 的字节总量，存在于 redo
log、数据页头部和 checkpoint 中。

No. 701302




## 第 71 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Redo Log Buffer
人

Block1              Block 2              Block 3              Block 4             Block 5

1二 log block header | log block header | log block header | log block header| log block header

LSN = 8704 + 12 + 300
= 9016

“1{

LSN = 9016 + 900 + 12*2 + 4*2
= 9948

-一这部分是帮助大家理解 start，面试中可不背---

MySQL 在第一次启动时，LSN 的初始值并不为 0，而是 8704; 当 MySQL 再次启动时，会继续使用上一次服务停
止时的 LSN。

在计算 LSN 的增量时，不仅需要考虑 log block body 的大小，还需要考虑 log block header 和log block tail 中部
分字节数。

比如说在上图中，事务 3 的 MTR 总量为 300 字节，那么写入到 Redo Log Buffer 中的 LSN 会增长为 8704 + 300
+12 = 9016。

假如事务 4 的 MTR 总量为 900 字节，那么再次写入到 Redo Log Buffer 中的 LSN 会增长为9016 + 900 + 12*2 +
4+2 = 9948。

2个12 字节的log block header+ 2 个4字节的log block tail。

----这部分是帮助大家理解end，面试中可不背-一

核心作用有三个:

第一，redo log 按照 LSN 递增顺序记录所有数据的修改操作。LSN 的递增量等于每次写入日志的字节数。

第二，InnoD8B 的每个数据页头部中，都会记录该页最后一次刷新到磁盘时的 LSN。如果数据页的 LSN 小于 redo
log 的 LSN，说明该页需要从日志中恢复; 否则说明该页已更新。

第三，checkpoint 通过 LSN 记录已刷新到磁盘的数据页位置，减少恢复时需要处理的日志。
-一这部分是帮助大家理解 start，面试中可不背---

No. 711302




## 第 72 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

场景                           LSN 的作用

园 -edo log 记录             每条 redo log 对应一个唯一的 LSN
》 数据页刷盘             每个数据页会记录当前刷盘时的 LSN (FIL_PAGE_LSN)
 checkpoint           表示“脏页已经刷盘，可以释放 redo"的安全点

诸 崩溃恢复                  重启时从 checkpoint LSN 开始重放 redo log

可以通过 show engine innodb status; 查看当前的 LSN 信息。

sequence number          4075686829
buffer asstigned Up to    4075686829
buffer compLeted up to ”4075686829
written Up to            4075686829

fLushed up to            4075686829
Added dirty pages up to      4075686829
Pages fLushed up to          4075686829
Last checkpoint at           4075686829
Log mintimum fiLLe 1Ld 1Ss       1244
Log maximum fiLe 1Ld 1Ls       1244
2021 Log iVo's done，0.00 Log iiVo'Ss/Ssecond

。 Log sequence number: 当前系统最大 LSN (已生成的日志总量) 。

。 Logflushed up to: 已写入磁盘的 redo log LSN。

。 Pages flushed up to: 已刷新到数据页的 LSN。

。 Last checkpoint at: 最后一次检查点的 LSN，表示已持久化的数据状态。
一-这部分是帮助大家理解end，面试中可不背-一

memo: 2025年3月19 日修改至此。今天有读者问怎么付费购买纸质版       ，说看到网友有这个，好羡慕
啊。说实话，第一眼看到这个封面，真的觉得挺惊艳 (虽然是我设计的) 。仿

No. 721302




## 第 73 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

我看到有人有你的纸质版了

就是这个 哥

11:47

是打印出来的吗?

和  攻
Checkpoint 了解多少?

Checkpoint 是InnoDB 为了保证事务持久性和回收 redo log 空间的一种机制。

它的作用是在合适的时机将部分脏页刷入磁盘，比如说 buffer pool 的容量不足时。并记录当前 LSN 为
Checkpoint LSN，表示这个位置之前的 redo log file 已经安全，可以被覆盖了。

MySQL 崩溃恢复时只需要从 Checkpoint 之后开始恢复 redo log 就可以了，这样可以最大程度减少恢复所花费的
时间。

No. 731302




## 第 74 页


面渣逆歼MySQL篇V2-让天下所有的面渣都能逆袭
redo log file 的写入是循环的，其中有两个标记位置非常重要，也就是 Checkpoint 和 write pos。

可写入

三                                                                                                                了有
checkpoint                 _                   WwWtite pos

write pos 是 redo log 当前写入的位置，Checkpoint 是可以被覆盖的位置。

当 write pos 追上 Checkpoint 时，表示 redo log 日志已经写满。这时候就要暂停写入并强制刷盘，释放可覆写的
日志空间。

wtite bos
八国 玫宣
国国月空
checkpoint
|                                                 wtite pos
checkpoint                                     write pos追上checkpoint,无可用空间

关于redo log 的调优参数了解多少?
如果是高并发写入的电商系统，可以最大化写入吞吐量，容忍秒级数据丢失的风险。

innodb_flush_ log_at_trx_commit = 2
sync_binlog = 1000
innodb_redo_1og_capacity = 64G
innodb_io_capacity = 5000
innodb_lru_scan_depth = 512
innodb_ log_buffer_size = 256M

如果是金融交易系统，需要保证数据零丢失，接受较低的吞吐量。

No. 741302




## 第 75 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

innodb flush 1og_at_trx_commit = 1
sync_binlog = 1
innodb_redo_1og_capacity = 32G
innodb_io_capacity = 2000
innodb_lru_scan_depth = 1024

核心参数一览表:

参数名                                         控制内容                               影响点
innodb _log file_size                       每个 redo log 文件大小             总 redo 空间、恢复时间
innodb_log files_in_group               redo log 文件个数                 配合文件大小决定总容量
innodb_log_buffer_size                     redo log buffer 缓冲区大小         是否频繁刷盘、写入性能
innodb_flush_log_at_trx_commit           redo 刷盘策略                          安全性 vs TPS
innodb_max_dirty_pages_pct                脏页比例阔值                             何时触发刷盘 / Checkpoint
innodb_io_capacity                           后台刷盘速度                           限制 checkpoint 刷盘压力
总结:

。 对数据一致性要求高的场景，如金融交易使用 innodb_flush_1log_at_trx_commit=1 ，对写入吞吐量敏感的
场景，如日志采集可以使用 =2 或 =0，需要结合 sync_binlog 参数

。 sync_binlog 参数控制 binlog 的刷盘策略，可以设置为0、1、N，0 表示依赖系统刷盘，1 表示每次事务提交
都刷盘 (推荐与 innodb_flush_ log_at_trx_commit=1l 搭配) ，N=1000 表示累计 1000 次事务后刷盘

。 innodb_redo_log_capacity 动态调整 Redo Log 总容量，可以根据业务负载情况调整，建议设置为 1 小时写
入量的峰值 (如每秒 10MB 写入则设为 36GB)

。 innodb_io_capacity 定义 InnoDB 后台线程的每秒 MO 操作上限，直接影响脏页刷新速率; 机械硬盘建议
200-500，SSD 建议 1000-2000，NVMe SSD 可设为 5000+

。 innodb_lru_scan_depth 控制每个缓冲池实例中 LRU 列表的扫描深度，决定每秒可刷新的脏页数量，默认值
1024 适用于多数场景，MO 密集型负载可适当降低 (如 512) ，减少 CPU 开销。

memo: 2025年3月 20 日修改至此。有球友报喜说拿到了滴滴的测开实习 offer，恭喜恭喜!

二哥，我收到滴滴的测开实习 offer，但是现在我犹物，要不要继续冲开
发，还是接了这个 offer。以后我想找国企，我现在担心的是接了这个
offer对我以后进国企有帮助吗，国企也可能看重学历，但网上说背书很
重要。

No.751302




## 第 76 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

32.二什么是慢 SQL?
推荐阅读: 慢 SQL 优化一点小思路

MySQL 中有一个叫 long_query_time 的参数，原则上执行时间超过该参数值的 SQL 就是慢 SQL，会被记录到慢查
询日志

一-这部分是帮助大家理解 start，面试中可不背-一-

可通过 show variables like 'long_query _time'; 查看当前的long_query _time 的参数值。

mysqL> Show VvariablLes Like "Long_query_time ' ;

十一    加
1 row tin set (

-一-这部分是帮助大家理解end，面试中可不背-…-
SQL 的执行过程了解吗?
了解。

SQL 的执行过程大致可以分为六个阶段: 连接管理、语法解析、语义分析、查询优化、执行器调度、存储引擎读写
等。Server 层负责理解和规划 SQL 怎么执行，存储引警层负责数据的真正读写 。

返回查询结果
Server层                                |
YY         f      风
一    、                1
/  ia \_建立链接/      -缓存是否开、_直      化器|   行   人
2 汪广机是”和摘蝇|><、启? 一 |  站   “二
二 太                                 一
;                                      查询结果写入缓存

key-value形式

No. 761302




## 第 77 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

----这部分是帮助大家理解 start，面试中可不背----
来详细拆解一下:
1. 客户端发送 SQL 语句给 MySQL 服务器。

2，如果查询缓存打开则会优先查询缓存，缓存中有对应的结果就直接返回。不过，MySQL 8.0 已经移除了查询
缓存。这部分的功能正在被 Redis 等缓存中间件取代。

3. 分析器对 SQL 语句进行语法分析，判断是否有语法错误。
4. 搞清楚 SQL 语句要干嘛后，MySQL 会通过优化器生成执行计划。
5. 执行器调用存储引擎的接口，执行 SQL 语句。
SQL 执行过程中，优化器通过成本计算预估出执行效率最高的方式，基本的预估维度为:
。 10 成本: 从磁盘读取数据到内存的开销。
。 CPU 成本: CPU 处理内存中数据的开销。
基于这两个维度，可以得出影响 SQL 执行效率的因素有:
人外、I10 成本，数据量越大，1O 成本越高。所以要尽量查询必要的字段; 尽量分页查询; 尽量通过索引加快查询。
@、CPU 成本，尽量避免复杂的查询条件，如有必要，考虑对子查询结果进行过滤。
-这部分是帮助大家理解end，面试中可不背---
如何优化慢 SQL 呢?
首先，需要找到那些比较慢的 SQL，可以通过启用慢查询日志，记录那些超过指定执行时间的 SQL 查询。
也可以使用 show processlist; 命令查看当前正在执行的 SQL 语句，找出执行时间较长的 SQL。

mysqt> show processtisti

+一一一一一一一+一一-一一一-一一-一一-一一一+一一一一一二
1 Id | user        | Host        1 db      | Command | Time | State            1 Info         1
+一-一一一一一一一一一一     一一一        一一一一一一一

| 5 | event_scheduter | tocathost     | NULL     | Daemon | 262498 | Waiting on empty queue | NULL         1
1 1445 | root        1 tocathost:38834 | pai_coding | Steep |    31                | NULL         1
1 1446 | root        | Locathost:57096 | pai coding | Steep | 751                | NULL         1
1 1447 | root        | Locathost:57164 | pai_ coding | Steep | 3361                | NULL         1
1 1448 | root        | Locathost:37749 | pai_ coding | Steep | 307 1                | NULL         1
1 1449 | root        | Locathost:37756 | pai_ coding | Steep | 396 1                | NULL         1
1 1456 | root        | Locathost:46626 | pai_ coding | Steep | 2341                | NULL         1
1 1451 | root        | Locathost:55154 | pai_coding | Steep | 158 |                | NULL         1
1 1452 | root        | Locathost:55166 | pai_coding | Steep | 155 |                | NULL         1
1 1453 | root        | Locathost:59374 | pai_ coding | Steep | 1371                | NULL         1
1 1454 | root        | Locathost:53522 | pai_coding | Steep | 431                | NULL         1
1 1455 | root        | Locathost     | NULL     | Query 1    9 | in计             1 show processtist |

12 rows in set，1 warning (9.90 sec)

或者在业务基建中加入对慢 SQL 的监控，常见的方案有字节码插桩、连接池扩展、ORM 框架扩展等。

No.771302




## 第 78 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

pf LohetpersgLoginHetper'，
3138643.166646127881 1"togget
31653192953.1696461271211f1oggei
1199628862.1731653254941.166646127191|f"toggei
193928882.1731653316646.16864612731| |f"toggei
1198928862.1731653378942.16664612736| |f"togget
whetperWxLoginHet
.1731653448068.16064612741| 1f109ger，
.1731653562637.169646127431 fw10ggei
.1731653564947.160646127491 1f"1ogger'iwc.9。

1 MLoginControttergsubscribe = gms"
1 MLoginControttergsubscribe = gas"
3 MLoginControttergsubscribe = gas"
4 MLoginControttergsubscribe = lns"
3 MLoginControttergsubscribe = gms"

Toram_core .ndchdchspect
orum .corevndc.hdchspect
threadrthttp-nio-8886-e
oram .corevndc.hdchspect
forum .core .ndc.hdchspect
faram corevndc-hdchspectv，

1 MLoginControtterysubscribe = gmso
1 MWLoginControttergsubscribe = lms")
1 MLoginControttergsubscribe = gaso

然后，使用 EXPLAIN 查看慢 SQL 的执行计划，看看有没有用索引，大部分情况下，慢 SQL 的原因都是因为没有用
到索引。

了EXPLRIN SELECT * FROM Your_ table WHERE conditions;

最后，根据分析结果，通过添加索引、优化查询条件、减少返回字段等方式进行优化。
慢sql日志怎么开启?

编辑 MySQL 的配置文件 my.cnf，设置 slow_query_log 参数为 1。

[mysqld]
slow_query_ log = 1

slow_query_1og file = /var/log/mysql/slow.1log
long_query_time = 2 ，## 记录执行时间超过2秒的查询

然后重启 MySQL 就好了。

也可以通过 set global 命令动态设置。

SET GLOBAL slow_query_ log = 'ON' 1
SET GLOBAL slow_query_1og_file = '/var/log/mysql/slow.1og';
SET GLOBAL long_query time = 27

1. java 面试指南 (付费) 收录的腾讯云智面经同学 16 一面面试原题: 场景题: sql 查询很慢怎么排查
2. java 面试指南 (付费) 收录的快手面经同学 5 面试原题: 慢sql日志怎么开启?

3. java 面试指南 (付费) 收录的美团面经同学 3 java 后端技术一面面试原题: 如何判断sql的效率，怎样
排查效率比较低的sql

Java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: mysql中如何定位慢查询
Java 面试指南(付费) 收录的同学 1 贝壳找房后端技术一面面试原题: 慢查询怎么分析

Java 面试指南(付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 如何优化慢查询语句?
java 面试指南 (付费) 收录的虾皮面经同学 13 一面面试原题: mysql慢查询

memo: 2025年3 月 21 日修改至此。今天有球友报喜说拿到了 wxg 的实习 offer，阿里云和美团也在进行当中，
真的 tql。

六 了中上

No. 781302




## 第 79 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

三  hm“                                                                 < 收进专栏
站

#晒个offer虚 #球友提问疹

好久好久没有来打卡了，之前确实是因为实习一直没有空，晚上回去随便收拾下然后玩一会
满足心理就休息了。这里简单分享下进度&问下二哥建议

2月开始高强度投署期实习，目前拿到了第一个offer，是腾讯wxg的，部门是微信读书&输
入法，后台开发，也算是有个保底了。      Sa

然后阿里去有个部门，对接人和我说二面过了准备hr面，同时美团一面感觉良好应该也过

了，等后面二面吧。感觉如黑阿里云和美团都过了，可能还是要再纠结一下要不要去wxg，

虽然wxg的名头很大但是转正率低来着，同时美团那个是核心本地商业，算非常核心的部

33.愉 你知道哪些方法来优化 SQL?
SQL 优化的方法非常多，但本质上就一句话: 尽可能少地扫描、尽快地返回结果。
最常见的做法就是加索引、改写 SQL 让它用上索引，比如说使用覆盖索引、让联合索引遵守最左前组原则等。

No. 791302




## 第 80 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

select 沉默王二

不要 select *

延迟关联

适当使用前缀索引
避免列上函数运算
正确使用联合索引

优化子查询
小表驱动大表
适当增加宛余字段
避免 join 太多的表

利用索引扫描做排序

UNION all 奉代 UNION

如何利用覆盖索引?
履盖索引的核心是查询所需的字段都在同一个索引里"，这样 MySQL 就不需要回表，直接从索引中返回结果。

No. 801302




## 第 81 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

ER                                                                                       |
(村焦素引)                                                                                                                     (非到作素引)

人
是
只 加一目-目] ELEEIIEE 沾一目目|
sos |        apmsezeal

实际使用中，我会优先考虑把 WHERE 和 SELECT 涉及的字段一起建联合索引，并通过 EXPLAIN 观察结果是否有
Using index，确认命中索引。

-一这部分是帮助大家理解 start，面试中可不背---
举个例子，现在要从 test 表中查询 city 为上海的name 字段。

select name from test where city='上海，

如果仅在 city 字段上添加索引，那么这条查询语句会先通过索引找到 city 为上海的行，然后再回表查询 name 字

段。

为了避免回表查询，可以在 city 和 name 字段上建立联合索引，这样查询结果就可以直接从索引中获取。
alter table test add index indexl(cityvname);

一-这部分是帮助大家理解 end，面试中可不背-…

如何正确使用联合索引?

使用联合索引最重要的一条是遵守最左前缀原则，也就是查询条件需要从索引的左侧字段开始。
一-这部分是帮助大家理解 start，面试中可不背-一

比如说我们创建了一个三列的联合索引。

CRERTE INDEX idx_name_age_sex ON user(name，age，sex);

我们来看一下什么样的查询条件可以用到这个索引 :

No. 811302




## 第 82 页


查询条件

WHERE name = 'itwanger

WHERE name = 'itwanger AND
age=20

WHERE age = 20

WHERE name='itwanger AND
Sex='女'

WHERE name LIKE 'it%'

WHERE name LIKE '"%wanger%'

面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

能否用上

idx_name_age_sex?

 可以

 可以

X 不行

贺 部分可用 (只用前一列)
加可以(前级匹配)

X 直行

说明

匹配第一列，命中索引

匹配前两列，命中索引

第一列没用上，索引失效

age 被跳过，后面的列无法使
用

name 是前缀匹配，不影响使
用

通配符在前，不能用索引

----这部分是帮助大家理解end，面试中可不背---

如何进行分页优化?

分页优化的核心是避免深度偏移带来的全表扫描，可以通过两种方式来优化: 延迟关联和添加书签。

延迟关联适用于需要从多个表中获取数据且主表行数较多的情况。它首先从索引表中检索出需要的行1D，然后再
根据这些 ID 去关联其他的表获取详细信息。

SELECT e.id，e-name，d.details

FROM employees e

JOIN department d ON e.department_ id = d.id
ORDER BY e.id

LIMIT 1000，207

延迟关联后，第一步只查主键，速度快，第二步只处理 20 条数据，效

SELECT e.id，e-name，d.details
FROM 1(
SELECT id

FROM employees
ORDER BY id
LIMIT 1000，20
) Rs sub
JOIN employees e ON sub.id = e.id
JOIN department d ON e.department_id = qd.id;

添加书签的方式是通过记住上一次查询返回的最后一行主键值，然后在下一次查询的时候从这个值开始，从而跳过
偏移量计算，仅扫描目标数据，适合翻页、资讯流等场景。

假设需要对用户表进行分页。

No. 82 1 302




## 第 83 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

SELECT id，name
FROM users
ORDER BY id
LIMIT 1000，207

通过添加书签来优化后，查询不再使用 OFFSET ，而是从上一页最后一个用户的 ID 开始查询。这种方法可以有效避
免不必要的数据扫描，提高了分页查询的效率。

SELECT id，name

FROM users
WHERE id > last_max_id -- 假设1ast_max_id是上一页最后一行的ID
ORDER BY id
LIMIT 207
个在悍
为什么分页会变慢?

分页查询的效率问题主要是由于 OFFSET 的存在，OFFSET 会导致 MySQL 必须扫描和跳过 offset + limit 条数据，
这个过程是非常耗时的。

比如说，我们要查询第 100000 条数据，那么 MySQL 就必须扫描 100000 条数据，然后再返回 10 条数据。

SELECT * FROM user ORDER BY id LIMIT 100000，10;

数据越多、偏移越大，就越慢!

memo: 2025年3 月 22 日修改至此。今天有球友说等腾讯云的 HR 面，很着急，但我赌他一定能拿到 offer，等
一个后续哈。

No. 831302




## 第 84 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥二哥，最新战报

我昨天中午进的 hr面

但是一直还没有约，是不是hr面隔两天约也是正
常的呀，之前技术面都是当天就约面了

网: 2025.03.21                                    投送册位。 软件开发后台开发方向
当前状态: HR面试                                        二
关宫癌字进入本环节，接下来面试官持会进一步评估，若有面试安排，同他将收村面试请，请保持联系
方式电通1
投进简历               测评                 面试让本试反傅            offer                 三方协议
@               @               日
9
日
2                 人HR面试

等着有点前熬仿

JOIN 代替子查询有什么好处?

第一， JOIN 的 ON 条件能更直接地触发索引，而子查询可能因赂套导致索引失效。

第二，JOIN 的一次连接操作蔡代了子查询的多次重复执行，尤其在大数据量的情况下性能差异明显。
一-这部分是帮助大家理解 start，面试中可不背-一

比如说我们有两个表 orders 和 customers。

No. 841302




## 第 85 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CRERTE TRBLE orders |(
order_iqd INT PRIMRARY KEY，
customer_id INT，
amount DECIMRAL(10,2)，
INDEX idx_customer _id (customer_id)  -- customer id字段有索引
)
CRERTE TRBLE customers |(
customer_id INT PRIMRARY KEY，
name VRARCHRAR(100)
)

子查询的写法:

SELECT o.order_id，o.amount，
(SELECT c.name
FROM customers c

WHERE c.customer_ id = o.customer_id) RS customer_name
FROM orders oy

JOIN 的写

SELECT o.order_id，o.amount，c.name RS customer_name
FROM orders o

JOIN customers c ON o.customer_ id = c.customer_ id;

对

比 ” 子查询                                   JOIN

项

引    内层子查询 WHERE c.customer_id =        JOIN 的ON 条件 o.customer id =
o-customer_id 每次执行时，可能无法直接 c-customer _id 可以直接利用 orders 的

局     利用 orders 表的 customer_id 索引。             idx_customer_id 索引，加速连接过程。

优化器可能选择通过索引快速关联两张表，减少数据
扫描量。例如，先通过 orders 的索引找到
customer_id，再与 customers 主键快速匹配。

行 ，子查询会被重复执行 《每次外层 orders 行都
计 会触发一次子查询) ，导致全表扫描。

划

性

能 ，”当 orders 表数据量大时，子查询可能因重复 ”JOIN 的一次连接操作通常更高效，尤其在大数据量
表 执行导致性能急剧下降。                          时。

现

对于子查询，执行流程是这样的:
。 外层 orders 表的每一行都会触发一次子查询 。
。 如果 orders 表有 1000 条记录，则子查询会执行 1000 次。

No. 851302




## 第 86 页


面渣逆袭MySQL篇V2-让天下所有的面渣者

袭

。 每次子查询都需要单独查询 customers 表 (即使 customer_id 相同) 。
而JOIN 的执行流程是这样的:
。 数据库优化器会将两张表的连接操作合并为一次执行。
。 通过索引 (如 orders.customer_id 和 customers.customer_id) 快速关联数据。
。 仅执行一次关联操作，而非多次子查询。
来看一下子查询的执行计划:

O                开
{            c                  customers c            c                     = o                    )

oraders o)

mysqL> EXPLAIN SELECT o.order_id，              (SELECT c.name FROM customers 5 WHERE 5c.cCustomer_id = 0.Cc|
ustomer_id)        FROM orders 0 \G;
六赤灵炎灾炎灾灾炎去灾南灾赤灾 全。 下ONW 六灾赤亦赤赤灾赤友玉雪灾广大
id: 1
setect_type: PRIMARY
tabte: 0
partitions: NULL
type: index
possibte_keys: NULL
key: idx_customer_id
key_Len: 5
ref: NULL
rows: 1
fiLtered: 100.00
Extra: Using index

灵赤亦赤赤赤二赤页灾击六赤去赤赤雪灾赤”了 。 ON六赤赤赤赤去灾赤灾赤灾赤灾去宙灾雪灾二

id: 2
Seltect_type: DEPENDENT SUBQUERY
tabte: C
partitions: NULL
type: eq_ref
possibte_keys: PRIMARY
key: PRIMARY
key_Len: 4
ref: test.o.customer_id
rows: 工
fittered: 100.00
Extra: NULL
2 rows in set，2 warnings (0.01 sec)

子查询 (DEPENDENT SUBQUERY) 类型表明其依赖外层查询的每一行，导致重复执行。

再对比看一下JOIN 的执行计划:

O                开
{            c                  customers c            c                     = o                    )

oraders o)

No. 861302




## 第 87 页


面渣逆袭MySQL篇V2-让天下所有的面渣都仙

mysqL> EXPLAIN SELECT o.order_id，c.name        FROM orders 0       JOIN customers 5 ON 0.customer_id =|
c.cCustomer_id \G;

灵灵赤赤亦炎去炎炎炎炎赤灾灾 “全 。 三OW 雪灾亦去灾炎亦赤赤灾灾太灾灾赤灾炎
id: 1
setLect_type: SIMPLE
tabte: 0
partitions: NULL
type: index
possibte_keys: idx_customer_id
key: idx_customer_id
key_tLen: 5
ref: NULL
rows: 1
fiLtered: 100.00
Extra: Using whereji Using index
关炎炎亦赤赤灾灾灾炎赤灾赤灾炎赤灾炎亦夫2 。 三OW 灾炎大灾灾赤炎炎炎类灾灾灾广大
id: 1
selLect_type: SIMPLE
tabte: 5
partitions: NULL
type: eq_ref
possibte_keys: PRIMARY
key: PRIMARY
key_tLen: 4
ref: test.0o.customer_id
rows; 1
fiLtered: 100.00
Extra: NULL
2 rows in set，1 warning (0.00 sec)

JOIN 通过 eq_ref 类型直接利用主键 (customers.customer_id) 快速关联，减少扫描次数。
-这部分是帮助大家理解 end，面试中可不背-一

memo: 2025 年3 月 23 日修改至此，今天有球友说，通过一晚上的时间，就在星球里学到很多知识，让他这个了
年经验的 CRUD Boy 受益菲浅。

No. 871302




## 第 88 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

你好，二哥，昨晚在你的星球复习了很多知识

哈哈，这也算是一种褒奖了

邀请你加入群聊

沉默王二-二哥邀请你加入群聊二哥 创
8辽

立
贞
VIP 10 群，进入可查看详情           王

如果能够深度挖掘的话，星球里确实沉淀了不少，怨够学好几个晚上了
是的呢，最近在准备面试，看了一些实习的简历都比我这个7年的crud
boy好的多局)

把它们统统学到手，鸟

JOIN操作为什么要小表驱动大表?
第一，如果大表的JOIN 字段有索引，那么小表的每一行都可以通过索引快速匹配大表。

No. 88 1 302




## 第 89 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

tQ

引工             索引0           索引 吉

结果集

时间复杂度为小表行数 N 乘以大表索引查找复杂度 log(大表行数 M)，总复杂度为 N*log(M)。
显然小表做驱动表比大表做驱动表的时间复杂度 M+xlog(N) 更低。
第二，如果大表没有索引，需要将小表的数据加载到内存，再全表扫描大表进行匹配。

No. 891 302




## 第 90 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

训

R2
EE                 join buffe                               舍果集
2                                                       ce

3 R.A=L.b

十--
1 row in set (0.01 sec )

显然小表做驱动表的时候 K 的值更小，大表做驱动表的时候需要多次分段。

No. 901302




## 第 91 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Cielo                                                           办
林 没看懂没有索引的时间复杂度。小表总行数N,大表M，小标做驱动表，时间复杂度
(NVjoin_buffer_size) * M 和 大表做驱动表 (M/join_buffer_size) * N这不就是一个式子吗。
旺 沉默王二 作者                                                           办
你再动脑子一下但馈创
青柠初上                                               加 … 四

“公式看着一样，实际执行效率不同。k分段肯定小表分的快呀，效率高。 举个例子， 与
1000时，相当于大表只加了个where条件，但是如果先走大表，得过滤找出1000条记录分
段存储，还得拿这个大结果去和小表一一比对。

六 Cielo                                                                                    办

回复 青柠初上: 听不懂。先小表，分段了，和大表比，大表数据多，想要加载全部的，不照
样很多io操作吗。如果大表分段，分段多一些，但是小表内容少，io也少啊

师 1.5语                                        四
公式是一样，实际性能差异巨大
青柠初上                                   目

 回复 Cielo:先大表，结果1000记录，循环访问小表需要io访问一千次，而且先大表结果集
大需要的内存也大，大表做驱动表还需要全表扫描，这只是我的理解哈哈

-- 小表驱动 (高效)
SELECT * FROM smal1l _ table S
JOIN large_table 1 ON s.id = 1.id; -- 1.id有索引

-- 大表驱动 (低效)
SELECT * FROM Large _table 1
JOIN small_table s ON 1.id = s.id;) -- s.id无索引

1. 当使用 left join 时，左表是驱动表，右表是被驱动表。

2. 当使用 right join 时，刚好相反。

3. 当使用join 时，MySQL 会选择数据量比较小的表作为驱动表，大表作为被驱动表。
----这部分是帮助大家理解 start，面试中可不背----
为了验证这一点，我特意新建了两个表 departments 和 employees。

No. 911302




## 第 92 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqL> desc departments ;

2 rows in set (0.00 sec )

mysqL> desc empLoyees ;

| emp_name
| dept_id

INSERT     departments   TUE
1
2，
3，
INSERT INTO employees VALUES
1     ，1)，
2       1
3       2
4，     ，2)，
5     ，3)，
6      ，NULL) ，
7       1)，
8      2);

然后用 explain 查看执行计划:

No. 921 302

PRI | NULL
| NULL





## 第 93 页


面渣逆袭MySQL篇V2-让天下所有的面渣都仙

3qL> EXPLAIN SELECT * FROM empt     e LEFT JOIN departments d ON edept_
type | possibte_k    key | key_ten | ref | rows | fittered | Extra

1e | NULL     | ALL | NULL       | MULL | MLL | MLL |

in set，1 warning (9.69 sec)
EXPLAIN SELECT * FROM emptoyees e RIGHT JOIN departments d ON e.dept_id = d.dept_id

ftttered | Extra

SINPLE                  ALL | MULL      ALL TAILL AtL 1 8                ; Ustng jotn buffer (hash jotn) |

SIMPLE    1     | MULL      ALL | PRIMARY     | MULL | MLL | ALL |           | NULL
PLE         | AULL      ALL | RULL       | RULL | NULL                     sing where; Using join buffer (

当使用 left join 的时候，第一行是employees 表，说明左表是驱动表; 当使用 right join 的时候，第一行是
departments 表，说明右表是驱动表; 当使用 join 的时候，第一行是 departments 表，说明 MySQL 默认选择了
小表作为驱动表。

-一-这部分是帮助大家理解 end，面试中可不背一-
这里的小表指实际参与 JOIN 的数据量，而不是表的总行数。大表经过 where 条件过滤后也可能成为逻辑小表。

-- 实际参与JOIN的数据量决定小表

SELECT * FROM Large _table 1

JOIN small table s ON 1.id = s.iqd

WHERE 1.created_at > '2025-01-01';  -- 1经过过滤后可能成为小表

也可以强制通过 STRAIGHT_JOIN 提示 MySQL 使用指定的驱动表。

explain select table_1.col1，table 2.col2，table_3.col2
from table_1

straight_ join table_2 on table _1.coll=table_2.col1l
straight_ join table 3 on table 1.coll = table 3.coll)

explain select straight_join table 1.coll，table_2.col2，table_3.col2
from table_1

join table_ 2 on table_1.coll=table_2.col1

join table 3 on table_1.coll = table_3.colli

为什么要避免使用JOIN 关联太多的表?

第一，多表jJOIN 的执行路径会随着表的数量呈现指数级增长，优化器需要估算所有路径的成本，有可能会导致出
现大表驱动小表的情况。

SELECT * FROM 有
JOIN B ON R.id = B.a_ id
C.b_ id

JOIN C ON B.id
JOIN D ON C.id =
JOIN E ON D.id = EB.d id;j -- 5 个表，优化器

需评估 5! = 120 种顺序

第二，多表JOIN 需要缓存中间结果集，可能超出 join_buffer_size，这种情况下内存临时表就会转为磁盘临时表，
性能也会急剧下降。

No. 931302




## 第 94 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

《阿里巴巴 Java 开发手册》上就规定，不要使用 join 关联太多的表，最多不要超过 3 张表。

2.，【强制】 超过三个表禁止 join。需要 join 的字段，数据类型必须绝对一致;多表关联查询时，保证被
关联的字段需要有索引。(这个我觉得不能算强制吧，数据量大可以，很多项目数据量都能小，一年都
没10万数据，join 4 5张表我都见过,但是关联的字段需要有索引是必须的)

说明:即使双表 join 也要注意表索引、SQL 性能。

memo: 2025年3 月 24 日修改至此，今天有球友反馈说，简历上加了 mydb 项目后，也顺利拿到腾讯的暑期实
习 offer。

宝  二哥好!
之前在二哥的建议下在简历中加了一个java数据库
的项目，今天收到腾讯暑期的offer啦! 感谢!

如何进行排序优化?
第一，对 ORDER BY 涉及的字段创建索引，避免 flesort。

-- 优化前 (可能触发 filesort)

SELECT * FROM users ORDER BY age DESC;

-- 优化后 (添加索引)

RALTER TRBLE users RDD INDEX idx_age (age);

如果是多个字段，联合索引需要保证 ORDER BY 的列是索引的最左前缀。

-- 联合索引需与 ORDER BY 顺序一致 (age 在前，name 在后)

RALTER TRBLE users RDD INDEX idx_age_name (age，name) 7

-- 有效利用索引的查询

SELECT * FROM users ORDER BY age，name)

-- 无效案例 (索引失效，因 name 在索引中排在 age 之后)

SELECT * FROM users ORDER BY name，agej

第二，可以适当调整排序参数，如增大 sort_buffer_size、max_length_for_sort_data 等，让排序在内存中完成。
----这部分是帮助大家理解 start，面试中可不背----

No. 941302




## 第 95 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqL> SHOW VARIABLES LIKE 'sort_buffer_size ';

1 row in set (0.00 sec)

mysqL> SHOW VARIABLES LIKE 'max_Length_for_sort_data ' ;

1 row in set (0.00 sec)

mysqL> mysqL> SHOW VARIABLES LIKE 'max_sort_Length ' ;

row in Set (0.00 sec)

。 sort_buffer_size: 用于控制排序缓冲区的大小，默认为 256KB。也就是说，如果排序的数据量小于 256KB，
MySQL 会在内存中直接排序; 否则就要在磁盘上进行 flesort。

s。 max_length_for_sort_data: 单行数据的最大长度，会影响排序算法选择。如果单行数据超过该值，MySQL
会使用双路排序，否则使用单路排序。

。 max_sort_length: 限制字符串排序时比较的前妇长度。当 MySQL 不得不对 text、blob 字段进行排序时，会
截取前 max_sort_length 个字符进行比较。

-一-这部分是帮助大家理解end，面试中可不背-…-
第三，可以通过 where 和 limit 限制待排序的数据量，减少排序的开销。

No. 951302




## 第 96 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-- 优化前

SELECT * FROM users ORDER BY age LIMIT 100;

=-- 优化后 (减少数据传输和排序开销)

SELECT id，name，age FROM users ORDER BY age LIMIT 100)

-- 深度分页优化 (避免 OFFSET 扫描全表)

SELECT * FROM users ORDER BY age LIMIT 10000，20;  -- 低效
SELECT * FROM users WHERE age > last_age ORDER BY age LIMIT 20;  -- 高效 (记录上一页最后一条的
age 值)

什么是filesort?

推荐阅读: MySQL 如何执行 ORDER BY

当不能使用索引生成排序结果的时候，MySQL 需要自己进行排序，如果数据量比较小，会在内存中进行， 如果数
据量比较大就需要写临时文件到磁盘再排序，我们将这个过程称为文件排序。

-一这部分是帮助大家理解 start，面试中可不背---
好，让我们来验证一下 filesort 的情况，建表、插入数据。

No. 96 1 302




## 第 97 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆效

CREATE DATABASE IF NOT EXIST9S test_db;
USE test_db;

DROP TABLE IF EXIST9 user_tabltLe;
CREATE TABLE user_tabltLe (人

td INT AUTO_INCREMENT，

name VARCHAR(50 ) ，

age INT，

emaiL VARCHAR(50 ) ，

PRIMARY KEY (id )

) ;

INSERT INT0O user_tablte (name，age，emaitL) VALUES
( '张三'，25， 'zhangsanGQexampLe.com' )，

( '李四 ，30，'LisiGexampLe.com ' )，

( 于五  35， 'wangwuGQexampLe.com' )，
(

(

40， 'zhaoLiuGQexampLe.com ' )，
证，  45， "sunqiGQexampLe.com' );

查询1: 使用有索引的字段排序 (不会产生 fitLesort)
LAIN SELECT * FROM user_tabLe ORDER BY id;

查询2: 使用无索引的字段排序 (会产生 fitesort)
LAIN SELECT x FROM user_tabtLe ORDER BY age;

执行 explain 查看执行计划。





## 第 98 页


V2-让天下所有的面

mysqL> exptLain select *x from user_tabLe order by id NG;

痰火大火火火火大火火火火火火火火大火火火火火火火火大火 了
id :
SeLect_type:
tabltLe:
partitions :
type :
possibLe_keys :
key :

key_tLen:

ref :

rows :
fiLtered :
Extral

1 row in set，

ERROR :

工
SIMPLE
User_tablLe
NULL
index
NULL
PRIMARY
4

NULL

5
100.00
NULL

No query specified

OW 大火炎大大火火火大火火大火火火火大大火火大火炎大火炎大

1 warning (0.00 sec )

mysqL> exptLain setLect *x from user_tablLe order by age \G;

痰火火火火大火火火火火火火炎大大大火火火火大火大大大大 人
id :
SeLect_type:
tablLe:
partitions :
type:
possibtLe_keys :
key :

key_tLen:

ref :

rows :
fiLtered :
Extra:

1

SIMPLE
User_tablLe
NULL

ALL

NULL

NULL

NULL

NULL

5

100.00
Using fitesort

IFOW 大大大大大大大大大大火炎大大大大大大大火大大大大大大大

1 row in set， ITWarnng  U.U0 sec)

一-这部分是帮

没有触发 flesort; 当 order by age 的时候，由于没有索引，

，拿到了阿里云的实习 offer，真的 tql。





## 第 99 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

阿里云给意向书了
应该不会再出问题了@9
再等两天
22:11
nice
这是真的稳了

全字段排序和 rowid 排序了解多少?
当排序字段是索引字段且满足最左前原则时，MySQL 可以直接利用索引的有序性完成排序。

tbl1                tbl2                 tbl3

Ordered
ouf+puf

No join buffering

index scan            for +fhose
+ables

No. 991302




## 第 100 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

当无法使用索引排序时，MySQL 需要在内存或磁盘中进行排序操作，分为全字段排序和 rowid 排序两种算法。

全字段排序会一次性取出满足条件行的所有字段，然后在 sort buffer 中进行排序，排序后直接返回结果，无需回
表。

以 SELECT * FROM user WHERE name = “"王二”ORDER BY age 为例:

。 从name 索引中找到第一个满足 name= '张三”的主键id;
。 根据主键 id 取出整行所有的字段，存入 sort buffer;

。 重复上述过程直到处理完所有满足条件的行

。 对sort buffer 中的数据按 age 排序，返回结果。

优点是仅需要一次磁盘 IO，缺点是内存占用大，如果数量超过 sort buffer 的话，需要分片读取并借助临时文件合
并排序，IO 次数反而会增加。

也无法处理包含 text 和 blob 类型的字段。

No. 1001302




## 第 101 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Ctty=   四 、                                      隐介                       排厅
加

rowid 排序分为两个阶段:
。 第一阶段: 根据查询条件取出排序字段和主键ID，存入 sort buffer 进行排序;
。 第二阶段: 根据排序后的主键 ID 回表取出其他需要的字段。
同样以 SELECT * FROM user WHERE name = "王二”ORDER BY age 为例:
。 从name 索引中找到第一个满足 name= '张三”的主键id;
。 根据主键 id 取出排序字段age，连同主键 id 一起存入 sort buffer;
。 重复上述过程直到处理完所有满足条件的行
。 对sort buffer 中的数据按 age 排序;
。 遍历排序后的主键 id，回表取出其他所需字段，返回结果。

优点是内存占用较少，适合字段多或者数据量大的场景，缺点是需要两次磁盘 IO 。

MySQL 会根据系统变量 max_length_for_sort_data 和查询字段的总大小来决定使用全字段排序还是 rowid 排序。
如果查询字段总长度 <= max_length_for_sort_data，MySQL 会使用全字段排序;否则会使用 rowid 排序。
你对 Sort_ merge_passes 参数了解吗?

推荐阅读: 深入了解 MySQL Order By 文件排序

Sort_merge_passes 是一个状态变量，用于统计 MySQL 在执行排序操作时进行归并排序的次数。

No. 1011 302




## 第 102 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

当 MySQL 需要进行排序但排序数据无法完全放入 sort_buffer_size 定义的内存缓冲区时，就会使用临时文件进行
外部排序，这时就会产生 Sort_merge_passes。

如果 Sort_merge_passes 在短时间内快速激增，说明排序操作的数据量较大，需要调整 sort_buffer_size 或者优
化查询语句。

mysdqL> SHOW GLOBAL STATUS LIKE 'Sort_merge_passes ' ;
十-一-一

1 row in set (0.00 sec)

MySQL 在执行排序操作时，会经历两个过程:
。 内存排序阶段，MySQL 首先尝试在 sort buffer 中进行排序。如果数据量小于 sort_buffer_size 缓冲区大小，
会完全在内存中完成快速排序。
。 外部排序阶段，如果数据量超过 sort_buffer_size，MySQL 会将数据分成多个块，每块单独排序后写入临时
文件，然后对这些已排序的块进行归并排序。每次归并操作都会增加 Sort_merge_passes 的计数。

No. 1021 302




## 第 103 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

从存储引擎读取记录

排序缓冲区

缓冲区满对记录进行排序
生成数据块

S                                               数据块
Merge_chunk                        所有数据记录

写和人 chunk _file                                 写人temp_file

chunk _file                               temp _file                                  out file

Merge_chunk                  多轮
归并排序

memo: 2025年3 月 27 日修改至此，今天有球友说，通过了快手二面，并且 HR 面是不排序的，已经确定了入职
时间，葵喜啊。

No. 103 1302




## 第 104 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

避  者 吧ET本                                         二 收进专栏

##晒个offer旧”球友提问从
最想去的快手二面过了还剩一个说好不排序的hr面 (二面已经确定入职时间了) @@甸，只是

发现耐这是Java入职是大模型微调，业务是tob的aigc应用开发，个人爱好原因很喜欢这个

场景 (虽然据说组是新成立的不那么核) 也能接触一点大模型

条件下推你了解多少?

条件下推的核心思想是将外层的过滤条件，比如说 where、join 等，尽可能地下推到查询计划的更底层，比如说子
查询、连接操作之前，从而减少中间结果的数据量。

比如说原始查询是:
SELECT x* FROM (
SELECT * FROM orders WHERE total > 100

) RS subquery
WHERE subquery.status = 'shipped')

就可以将条件下推到子查询:

SELECT * FROM (
SELECT * FROM orders WHERE total > 100 RND status = 'shipped'
) RS subquery;

这样就可以减少查询返回的数据量，避免外层再过滤。
再比如说 union 中的原始查询是:

(SELECT * FROM tl)

UNION RLL

(SELECT * FROM 七2)
ORDER BY col LIMIT 107

就可以将条件下推到每个子查询:

(SELECT * FROM tl ORDER BY col LIMIT 10)
UNION RLL
(SELECT * FROM t2 ORDER BY col LIMIT 10)7

每个子查询仅返回前 10 条数据，减少临时表的数据量。
再比如说连接查询 join 中的原始查询是:

SELECT * FROM orders
JOIN customers ON orders.customer_id = customers.id
WHERE customers.country = "china'

No. 1041 302




## 第 105 页


面尖逆区MySQL篇V2-让天下所有的面洁都能逆装
就可以将条件下推到表扫描的时候:

SELECT * FROM orders
JOIN 1(
SELECT * FROM customers WHERE country = 'china'
) RS filtered_customers
ON orders.customer_id = filtered_customers.iqdy

先过滤 customers 表，减少join 时的数据量。
为什么要尽量避免使用 select *?
SELECT * 会强制 MySQL 读取表中所有字段的数据，包括应用程序可能并不需要的，比如 text、blob 类型的大字

段。

加载了见余数据会占用更多的缓存空间，从而挤占其他重要数据的缓存资源，降低整体系统的吞吐量。
也会增加网络传输的开销，尤其是在大字段的情况下。

最重要的是，SELECT * 可能会导致覆盖索引失效，本来可以走索引的查询最后变成了全表扫描。

-- 使用覆盖索引 (假设索引为 idx_country)

SELECT id，country FROM users WHERE country = 'china';  -- 可能仅扫描索引
-- 使用 SELECT *
SELECT * FROM users WHERE country = 'china' 7          -- 需回表读取所有列

你还知道哪些 SQL 优化方法?
@D、避免使用 != 或者 <> 操作符
= 或者 <> 操作符会导致 MySQL 无法使用索引，从而导致全表扫描。

可以把 column<>'aaa' ，改成 column> 'aaa' or column<'aaa' 。

@、使用前缀索引

比如，邮箱的后缀一般都是固定的 exxx.com ，那么类似这种后面几位为固定值的字段就非常适合定义为前缀索
引:

alter table test add index index2(email(6)))

需要注意的是，MySQL 无法利用前组索引做 order by 和 group by 操作。
图、避免在列上使用函数
在 where 子句中直接对列使用函数会导致索引失效，因为 MySQL 需要对每行的列应用函数后再进行比较。

select name from test where date_format(create time，'sY-sm-sd')='2021-01-01'7

可以改成:

No. 1051302




## 第 106 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

select name from test where create time>='2021-01-01 00:00:00' and create _ time<'2021-01-
02 00:00:00' 7

通过日期的范围查询，而不是在列上使用函数，可以利用 create_time 上的索引。

memo: 2025年3月28 日修改至此，今天有球友说，字节跳动和腾讯的暑期实习都 OC 了，很感谢当时加了二
哥的编程星球，看球友们日常的学习分享，以及二哥推荐的轮子。

No. 1061302




## 第 107 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥您好，现在我有一点纠结。目前是接了腾讯
.十了的oc，提交了入职申请。
但是今天刚面完字节，字节也oc了。

很感谢当时加了二哥的知识星球hhh

加了后看到群友们日常的学习分享，以及二哥推
荐的轮子项目

99 ME 三

确实也很感谢hhh

No. 1071302




## 第 108 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

1. java 面试指南 (付费) 收录的腾讯面经同学 22 暑期实习一面面试原题: 查询优化、联合索引、覆盖索
引

java 面试指南(付费) 收录的华为面经同学 8 技术二面面试原题: 说说 SQL 该如何优化
java 面试指南 (付费) 收录的华为面经同学 6java 通用软件开发一面面试原题: 说说 SQL 该如何优化
java 面试指南 (付费) 收录的微众银行同学 1 java 后端一面的原题: MySQL 索引如何优化?

java 面试指南 (付费) 收录的携程面经同学 10 java 暑期实习一面面试原题: 讲一讲 MySQL 的索引，
如何优化 SQL?

6. Java 面试指南 (付费) 收录的用友面试原题: 了解 mysql 怎么优化吗
7. java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题: 查询如何优化

34.愉explain平常有用过吗?

mm 和ww DSS

No. 108 1 302




## 第 109 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

table

type
exblain        |
|                                                                                  index_subquety

tange

index

bossible_keys

Using index

Using whete

Using temportaty

No. 1091302




## 第 110 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

比如说 type=aLL,key=NULL 表示 SQL 正在全表扫描，可以考虑为 where 字段添加索引进行优化; Extra=Using
filesort 表示 SQL 正在文件排序，可以考虑为 order by 字段添加索引。

使用方式也非常简单，直接在 select 前加上 explain 关键字就可以了。
explain select * from students where name='王二' )

更高级的用法可以配合 format=json 参数，将 explain 的输出结果以JSON 格式返回。

explain format=json select * from students where name='

No. 1101 302




## 第 111 页


|
"query_btLock": 二

"SetLect _ id" : 1

"Cost_info" :
"query_cost": "5.75”

}，

"ordering_operation": 荆
"using_fiLLesort": true，
"cost_info":

"Sort_cost": "5.00"
】

"tabtLe":
"tabtLe_name": "User_tablLe'" ，
”access_type": "ALL”，
"rows_examitined_per_scan": 5
"rows_produced_per_jotin": 5，
"fiLLtered": "100.00"，
"cost_info": {
"read_cost": "0.25"，
"evalL_cost": "0.50"，
"prefiLx_cost": "0.75"，
"data_read_per_jotin": "2K"

?》

}，

"used_coLumns": [
"id"，
“name "，
“age ，
"emaitL"

explain 输出结果中常见的字段含义理解吗?

No. 1111302





## 第 112 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

在 EXPLAIN 输出结果中我最关注的字段是 type、key、rows 和 Extra。

我会通过它们判断 SQL 有没有走索引、是否全表扫描、预估扫描行数是否太大，以及是否触发了 filesort 或临时
表。一旦发现问题，比如 type=ALL 或者 Extra=Using filesort，我会考虑建索引、改写 SQL 或控制查询结果集来
做优化。

-一这部分是帮助大家理解 start，面试中可不背---

以 EXPLAIN SELECT * FROM orders WHERE user_id = 100 的输出为例:

字段                   值                   含义与优化指导
id                       1                     查询序列号。

简单查询 (无子查询或 UNION) 。复杂场景还有 PRIMARY、

ER      和       SUBQUERY、DERIVED 等。
table                  orders             当前步骤操作的表名。
partitions           NULL             涉及的分区。

访问类型: 关键性能指标，常见类型:
- System/const: 唯一值匹配 (性能最佳)
-eq_ref: 主键/唯一索引连接
type            ref           - ref: 非唯一索引匹配
-range: 索引范围扫描
-index: 全索引扫描
-ALL: 全表扫描 (需优化)

possible_keys ”idx_user_id 可能使用的索引。若为空，说明无合适索引。

key          idx_user_id 实际选择的素引。若为 NULL，表示未使用索引。
eyen           A              索引使用的字节数，可判断是否使用完整索引。例如，联合索引 (a,b)，若
类                                         key _len=4 可能只用到了 a 列。

ref                Const           与索引比较的列或常量 (如 WHERE user_id=100 中的 100) 。

1ows             本             预估扫描行数。数值越小越好，若与实际差距大，可能统计信息过期 (需
ANALYZE TABLE) 。

                           查询条件过滤后剩余行的百分比。例如 rows=1000 且 filtered=10%，则

filtered           100.00             、           一
最终返回约 100 行。
附加信息:

EN            Using        - Using index: 覆盖索引 (无需回表)

四              where          - Using temporary: 使用临时表
- Using filesort: 文件排序

非表格版本:

外、id 列: 查询的执行顺序编号。id 相同: 同一执行层级，按 table 列从上到下顺序执行 (如多表JOIN) ; id 递
增: 庶套子查询，数值越大优先级越高，越先执行。

No. 1121 302




## 第 113 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

EXPLRIN SELECT * FROM tl JOIN (SELECT * FROM t2 WHERE id = 1) RS sub;

t2 子查询的 id=2，优先执行。
@@、select type 列: 查询的类型。常见的类型有:
。 SIMPLE: 简单查询，不包含子查询或者 UNION。
PRIMARY: 查询中如果包含子查询，则最外层查询被标记为 PRIMARY。需要关注子查询或派生表性能。
SUBQUERY: 子查询;需要避免多层嵌套，尽量改写为JOIN 。
。 DERIVED: 派生表 (FROM 子句中的子查询) 。需要减少派生表数据量，或物化为临时表。
@@、table 列: 查的哪个表。

。 derivedN: 表示派生表 (N 对应id) 。
。 unionNM,N: 表示 UNION 合并的结果 (M、N 为参与 UNION的id) 。

图、type 列: 表示 MySQL 在表中找到所需行的方式。

。 system，表仅有一行 (系统表或衍生表) ，无需优化。

。 const: 通过主键或唯一索引找到一行 (如 WHERE id = 1) 。理想情况。

。 eq_ref: 对主键/唯一索引JOIN 匹配 (如 aA JorN B ON aid = B.id) 。确保JOIN 字段有索引。
。 ref: 非唯一索引匹配 (如 wagRE name =“'王二' ，name 有普通索引) 。

。 range: 只检索给定范围的行，使用索引来检索。在 where 语句中使用 bettween.. .and 、<、> 、<=、
in 等条件查询 type 都是 range 。

。 index: 全索引扫描，如果不需要回表，可接受;否则考虑覆盖索引。
ALL: 全表扫描，效率最低。

昌

人@@、possible_keys 列: 可能会用到的索引，但并不一定实际被使用。

人@@、key 列: 实际使用的索引。如果为 NULL，则没有使用索引。如果为 PRIMARY，则使用了主键索引。

@、key _len 列: 使用的索引字节数，反映索引列的利用率。使用联合索引 (a, bj)，key _len 是 a 和 b 的字节总和
(仅当查询条件用到 a 或 a+b 时有效) 。

-- 表结构: CRERATE TRBLE t (a INT，b VRRCHRAR(20)，INDEX idx ab (a，b)) 7
EXPLRAIN SELECT * FROM 七 WHERE a = 1 RND b = "test' 7

key_len=4 (INT) +20*3 (utf8) +2= 66字节。

图、ref 列: 与索引列比较的值或列。

。 const: 常量。例如 WHERE column = 'value' 。

。 func: 函数。例如 WHERE column = func(column) 。

加、rows 列: 优化器估算的需要扫描的行数。数值越小越好，若与实际差距大，可能统计信息过期 (需 ANALYZE
TABLE) 。结合 fittered 字段可以计算最终返回行数 (rows x filtered) 。

@@、Extra 列: 附加信息。

No. 113 1 302




## 第 114 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

。 Using index: 覆盖索引，无需回表。

。 Using where: 存储引擎返回结果后，Server 层需要再次过滤 (条件未完全下推) 。

。 Using temporary : 使用临时表 (常见于 GROUP BY、DISTINCT) 。

。 Using filesort: 文件排序 (常见于ORDER BY) 。考虑为 ORDER BY 字段添加索引。

。 Select tables optimized away: 优化器已优化 (如 COUNT(*) 通过索引直接统计) 。

。 Using join buffer: 使用连接缓冲区 (Block Nested Loop 或 Hash join) 。考虑增大 join_buffer_size。

示例:

mysqL> exptLain seLect * from students where id =9\G
火火火火火火火大火火火火火火大大火火火大火火炎大火炎大 人 。 三OW 大火炎大大大火炎大火火火火火火火炎大火炎大火火大大火炎
id: 1
SeLect_type: SIMPLE
tabLe: students
partitions: NULL
type: Const
possibtLe_keys: PRIMARY

key: PRIMARY
key_Len: 4
ref: const
rows: 1
fiLtered: 100.00
Extra: NULL
1 row in set，1 warning (0.00 sec)

----这部分是帮助大家理解end，面试中可不背---

type的执行效率等级，达到什么级别比较合适?

从高到低的效率排序是 system、const、eq_ref、ref、range、index 和 ALL。

一般情况下，建议 type 值达到 const、eq_ref 或 ref，因为这些类型表明查询使用了索引，效率较高。
如果是范围查询，range 类型也是可以接受的。

ALL 类型表示全表扫描，性能最差，往往不可接受，需要优化。

1. java 面试指

2. java 面试指                               key-len和key没什么区别，什

memo: 2025年3月 29 日修改至此，今天有球友说美团的 offer 口头 OC 了，真的太棒了。

No. 114 1 302




## 第 115 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥，请问美团的口头 offer稳吗?

刚刚美团 hr问问到岗时间，说在5天内发 offer给我

8:15

索引

35.忆索引为什么能提高MySQL查询效率?
索引就像一本书的目录，能让 MySQL 快速定位数据，避免全表扫描。

它一般是 B+ 树结构，查找效率是 O(log n)，比从头到尾扫一遍数据要快得多。

No. 115 1 302

稳的




## 第 116 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

intermediate node

Page 1003              Page 1004
1    Jery 1       5   Roc |101     10 。 Emiy 105   -13 chen 109
2       112      6      103   昌           一人
La node     Moly        <一   Moly       11      104     14 An 1o06
3   Tom 108    一>7  Sunny |102   2 ww 113       Page 1008
4    Tony lto7      8 uack 110
Page 1007
ET和        9   Uy 108

Page 1006
除了查得快，索引还能加速排序、分组、连接等操作。
可以通过 create index 创建索引，比如:

create index idx_name on students(name) 7

-一这部分是帮助大家理解 start，面试中可不背---
我们通过 wrap 的 agent 验证一下有没有索引的查询效率。
先上结果，有索引的查询时间是 0.007 秒，没有索引的查询时间是 0.036 秒。

No. 116 1 302




## 第 117 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

Let me Summarize the performance comparison resulLts:

。 Without Index:
Access type: "ALL" (fuLL tabltLe scan)
Rows examined: 100,140
Query execution time: 0.036 seconds
Query cost: 10,102.25

.With Index:
Access type: "ref" (using index)
Rows examined: 1,597
Query execution time: 0.007 seconds
Query cost: 424.45

Performance Improvement :
。 Query execution is about 5x faster with the index (0.036s ”0.007s)
。 _ Query cost reduced by 96s (10,102.25 ”424.45)
se。 Number of rows examined reduced by 98%5 (100,140 ”1,597)

创建数据库和表。

mysqL -h LocatLhost -u root -p123456 -e "CREATE DATABASE IF NOT
EXIST9S demo_performance; USE demo_performance;i CREATE TABLE IF NOT

EXISTS test_performance (id INT _ PRIMARY KEY AUT0O_INCREMENT ，name
VARCHAR(100)，age INT，creation_date DATETIME ) ;”

插入 10 万条数据。

No. 1171302




## 第 118 页


SQL篇V2-让天下所有的面渣都能:

mysqtL -h LocaLhost -u root -p123456 demo_performance << “EOF'
DELIMITER //

CREATE PROCEDURE PopuLateTestData( )
BEGIN

DECLARE 1 INT _ DEFAULT 1;
WHILE 1 <= 100000 D0
INSERT INTO test_performance (name，age，creation_date)
VALUES (
CONCAT( 'Person_“，，蕊)，
18 + FLOOR(RAND() * 63)，
DATE_SUB(NOW( ) ，INTERVAL FLOOR(RAND() x 365) DAY)

CALL PoputLateTestData( ) ;

DROP PROCEDURE PopuLateTestDataj;
芭

然后依次执行 explain 查看没有索引和有索引时的执行计划。

mysqL -h LocatLhost -u root -p123456 demo_performance -e "CREATE
INDEX idx_age ON test_performance(age);"

The index has been created successfuLLty. Now Let's execute step 4 of the
plLan:

1. Run the same SELECT query again

2. Use EXPLAIN to see the new execution plLan
3. Measure the execution time

We'LL use the same command structure as before to ensure a fair
Comparison.

mysqtL -h LocalLhost -uU root -p123456 demo_performance << “EOF'

SET profiLing = 1;

EXPLAIN FORMAT=JSON SELECT * FROM test_performance WHERE age = 30;
SELECT * FROM test_performance WHERE age = 30;

SHOW PROFILES ;

漳end，面试中可不背-一





## 第 119 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

2. Java 面试指南(付费) 收录的小米面经同学 E 第二个部门 java 后端技术一面面试原题: 为什么需要索

引
3. java 面试指南 (付费) 收录的小公司面经同学 5 java 后端面试原题: 数据库索引讲一下，然后为什么
会加快查询速度

.java 面试指南 (付费) 收录的去哪儿面经同学 1 技术二面面试原题: mysq|为什么用索引

.java 面试指南 (付费)_收录的 OPPO 面经同学 1 面试原题: 对MySQL索引的理解

.Java 面试指南(付费) 收录的vivo 面经同学 10 技术一面面试原题: 索引，为什么使用索引更快

.java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 介绍下索引? 底层是喻?
memo: 2025年3月30 日修改至此，之前有球友说拿到了淘天搜索的暑期实习，真的恭喜了。

曙

署期实习选择:
贺 淘天搜索技术; 目前在排序，可能得等一周，内推的说有机会; base杭放

36.二能简单说一下索引的分类吗?

从功能上分类的话，有主键索引、唯一索引、全文索引; 从数据结构上分类的话，有 B+ 树索引、哈希索引，从存
储内容上分类的话，有聚得索引、非聚簇索引。

4
5
6.
7

索引类型@沉默王二

聚复索引

非聚簇索引

你对主键索引了解多少?

主键索引用于唯一标识表中的每条记录，其列值必须唯一且非空。创建主键时，MySQL 会自动生成对应的唯一索
引。

No. 1191302




## 第 120 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

nnedb3 |区，二1页只末了近，tshudent有本人和只示人轿

和下5 | miss 9 5

习间

每个表只能有一个主键索引，一般是表中的自增 id 字段。

CRERTE TABLE emp6 (emp_id INT PRIMRRY KEY，name VRRCHRR(50)); -~- 单列主键

CRERTE TRBLE CountryLanguage (
CountryCode CHRAR(3) ，
Language VRRCHRAR(30) ，
PRIMARY KEY (CountryCode，Language) “-- 复合主键

)

-一这部分是帮助大家理解 start，面试中可不背 -一

如果创建表的时候没有指定主键，MySQL 的 InnoDB 存储引擎会优先选择一个非空的唯一索引作为主键; 如果没
有符合条件的索引，MySQL 会自动生成一个隐藏的_rowid 列作为主键。

"If you do not defne a PRIMARY KEY for your table, MySQL locates the frst
UNIQUE index where all the key columns are NOT NULL and InnoDB uses it as the

clustered index. If there is no such index, InnoDB creates a hidden clustered index

named GEN_CLUST_INDEX.”
一一《MySQL 8.0 Reference Manual》

可以通过 show index from table_name 查看索引信息:

No. 1201302




## 第 121 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqL> SHOW INDEX FROM usersNG
火火火火火火火火火火火火火火火火火火火火火火火火火大火 人。 三OW 大大火火火火大大火火火火火火火火火火火火火火炎火火火炎
TabtLe: Users
Non_unique: 0
Key_name: PRIMARY
Seq_in_index:
CoLumn_name :
CoLLation:
CardinatLity :
Sub_part :
Packed :
NULL:
Index_type:
Comment :
Index_comment :
Visibte:
row in set (0.00 sec)

。 Table 当前索引所属的表名。

。 Non_unique 是否唯一索引，0 表示唯一索引 (如主键) ，1 表示非唯一。

。 Key_name 主键索引默认叫 PRIMARY; 普通索引为自定义名。

。 seq_in_index 索引中的列顺序，在联合索引中这个字段表示第几列 (第1个) 。
。 column_name 当前索引中包含的字段名。

。 collation A表示升序 (Ascend) ; D 表示降序。

。 cardinality 索引的基数，即不重复的索引值的数量。越高说明区分度越好 (影响优化器是否用此索引) 。
。 sub_part 前缀索引的长度。

。 Packed 是否压缩存储索引;一般不用，默认为 NULL。

。 Mul1 字段是否允许为 NULL; 主键字段不允许为 NULL。

。 Index_type 索引底层结构，InnoDB 默认是 B+ 树 (BTREE) 。

。 comment 索引的注释。

e。 Visible 是否可见， MySQL 8.0+ 可隐藏索引。
--- 这部分是帮助大家理解 and，面试中可不背 -一
唯一索引和主键索引有什么区别?
主键索引=唯一索引+非空。每个表只能有一个主键索引，但可以有多个唯一索引。

CRERATE TABLE userS
id INT AUTO_INCREMENT PRIMRARY KEY，
username VARCHRAR(50) NOT NULL，
emai1l VARCHAR(100) NOT NULL，

No. 1211 302




## 第 122 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

UNIOUE KEY uk_email (email

CRERTE TARBLE user_roles
user_iqd INT NOT NULL，
role VRRCHRAR(20) NOT NULL，

UNIOUE KEY uk_user_role (user_id，zrole

主键索引不允许插入 NULL 值，尝试插入 NULL 会报错; 唯一索引允许插入多个 NULL 值。

mysqL> SELECT * FROM test_unique_nutLtL;
---+

1 | Test1 | NULL
2 | Test2 | NULL
3 | Test3 | not_nulLL

3 rows in set (0.00 sec)
mysqL> INSERT INTO test_unique_nutLt (id，name，unique_coL) VALUES

-> (1，'Test4'，NULL);
Query 0K，1 row affected (0.01 sec)

mysqL> SELECT * FROM test_unique_nutLtL;
=----     ---+
| unique_coltL |

1 | Test1 | NULL
2 | Test2 | NULL
3 | Test3 | not_nulLL
1 | Test4 | NULL

4 rows in set (0.00 sec)

mysqL> INSERT INTO test_primary (id，name) VALUES (NULL， 'Test1 ' );
ERROR 1048 (23000): CoLumn "id' cannot be _nulLL

unique key 和 unique index 有什么区别?
创建唯一键时，MySQL 会自动生成一个同名的唯一索引; 反之，创建唯一索引也会隐式添加唯一性约束。

可通过 UNIQUE KEY uk_name 定义或者 CONSTRAINT uk_name UNIQUE 定义唯一键。

No. 122 1 302




## 第 123 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

CRERTE TARBLE users
id INT PRIMRARY KEY，
email VRARCHRR(100) ，

CONSTRRAINT uk_email UNIOUE (email

CRERTE TRBLE users3
id INT PRIMRARY KEY，
email VRRCHRR(100) ，
UNITOUE KEY uk_email (email

可通过 CREATE UNIQUE INDEX 创建唯一索引。

CRERTE TARBLE users
id INT PRIMRARY KEY，
email VRRCHRR(100

CRERTE UNIOUE INDEX uk_email ON users(email

通过 sHow CRERATE TABLE table_name 查看表结构时，结果都是一样的。

| users3 | CREATE TABLE “users3`” (
“id int NOT NULL，
“emaitL ”varchar(100) DEFAULT NULL，
PRIMARY KEY ( id  )，
UNIQUE KEY “uk_emaitL (emait )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

Users1 | CREATE TABLE “users1 (人
id” int NOT NULL，
“emaiL ”varchar(100) DEFAULT NULL，

PRIMARY KEY (id )，
UNIQUE KEY “uk_emaiL (emaitL )
ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci

Users | CREATE TABLE “users (人

"id ”int NOT NULL，

“emaiL ”varchar(100) DEFAULT NULL，

PRIMARY KEY (id  )，

UNIQUE KEY “uk_emait (emaitL )

ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci |

普通索引和唯一索引有什么区别?
普通索引仅用于加速查询，不限制字段值的唯一性; 适用于高频写入的字段、范围查询的字段。

No. 123 1 302




## 第 124 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

-- 日志时间戳允许重复，无需唯一性检查

CRERTE INDEX idx_1og time ON access_logs(access_time);

-- 订单状态允许重复，但需频繁按状态过滤数据

CRERTE INDEX idx_order_status ON orders(status) 7

唯一索引强制字段值的唯一性，插入或更新时会触发唯一性检查; 适用于业务唯一性约束的字段、防止数据重复插
入的字段。

-- 用户邮箱必须唯一

CRERTE UNIOUE INDEX uk_email ON users(email) 1;

-- 确保同一用户对同一商品只能有一条未支付订单
CRERTE UNIOUE INDEX uk_user_product ON orders(user_id， Product_id) WHERE status =
"unpaid'

memo: 2025年3月31 日修改至此，今天有球友说，拿到了淘天署期实习的 offer，并且再次强调背面渣逆袭的
重要性，哈哈。

谢谢二哥，已经拿到暑期淘天的实习了

ER
已发意向书，待谈offer: 辆攻守 五JL 大学

今天早上发的

二哥的面经我全背完了，还是很有效的

你对全文索引了解多少?

No. 1241 302




## 第 125 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

全文索引是 MySQL 一种优化文本数据检索的特殊类型索引，适用于 CHAR、VARCHAR 和 TEXT 等字段。
MySQL 5.7 及以上版本内置了 ngram 解析器，可处理中文、日文和韩文等分词。

建表时通过 FULLTEXT (title，body) 来定义。通过 MarcH(col1，co1l2) AGAINST('keyword' ) 进行检索，
默认按照降序返回结果，支持布尔模式查询。

*。 + 表示必须包含;
。 - 表示排除;
*。 * 表示通配符;

-- 建表时创建全文索引 (支持中文)
CRERTE TRBLE articles |(
id INT UNSIGNED AUTO_INCREMENT PRIMRRY KEY，
title VRARCHRAR(200) ，
content TEXT，
FULLTEXT(title，content) WITH PRRSER ngram
) ENGINE=InnoDB》

-- 使用布尔模式查询
SELECT * FROM articles
WHERE MRTCH(title，content) RGRINST('+MYSOL -Oracle' IN BOOLERN MODE)7

底层使用倒排索引将字段中的文本内容进行分词，然后建立一个倒排表。性能比 ZIKE “skeywords，高很多。
-一这部分是帮助大家理解 start，面试中可不背 -一

倒排索引通过一个辅助表存储单词与单词自身在一个或多个文档中所在位置之间的映射，通常采用关联数组实现。

有两种表现形式: inverted file index ({单词，单词所在文档的ID})) 和full inverted index ({单词，(单词所在文档
的ID，在具体文档中的位置))

比如有这样一个文档:

DocumentId Text
Pease porridge hot，pease porridge cold
Pease porridge in the pot
Nine days old
Some like it hot，some like it cold
Some like it in the pot

au ee ww N PP

Nine days old

inverted file index 的关联数组存储形式为:

days -376
old ”376
pease ”1，2
porridge 1，2

fullinverted index 更加详细:

No. 1251 302




## 第 126 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

days ”(3:5)，(6:5)
old ”(3:11)，(6:11)
pease ” (1:1)，(1:7)，(2:1)
porridge ”(1:7)，(2:7)

fullinverted index 不仅存储了文档ID，还存储了单词在文档中的具体位置。
InnoDB 采用的是 fullinverted index 的方式实现全文索引。

如果需要处理中文分词的话，一定要记得加上 wITH PRARSER ngram ，否则可能查不出来数据。

mysqtL> CREATE TABLE artictes {
id INT PRIMARY KEY AUTO_INCREMENT ,
titLe VARCHAR(100) ，
Content TEXT，
FULLTEXT (titLe，content)
) ENGINE=InnoDB;
Query 0K，0 rows affected (0.04 sec)

mysqtL> INSERT INTO artictes (titte，content) VALUES
-> 。 ("必SQL全文索引简介' "全文索引是数据库中的一种索
-> 。 _('全文搜索实例,，'这是      索的实例，用于演示
Query 0K，2 rows affected (0.00 sec)
Records: 2 DuplLicates: 0 Warnings: 0

mysqt> SELECT td，titte
-> FROM artictes
-> WHERE MATCH(titLe，content) AGAINST( '全文索
Empty set (0.00 sec)
mysqtL> ALTER TABLE artictes
-> DROP INDEX titLe，
-> ADD FULLTEXT idx_tittLe_content (titte，content) WITH PARSER ngramj;
Query 0K，0 rows affected (0.05 sec)
Records: 0 DuptLicates: 0 Warnings: 0

mysqL> SELECT *

-> FROM artictes

-> WHERE MATCH(titLe，content)

-> AGAINST(      引” IN BOOLEAN MODE)
+----+--------           ---+---
1 id | titte            | content

1 | MySQL全

二+-
2 rows in set (0.00 sec)

mysqL> SELECT * FROM artictes WHERE MATCH(titte，content) AGAINST( "全文索
+----+---
| id | titte            | content

对文本字段进行高效的全文
索引的应用。

2 rows in set (0.00 sec)

不过，对于复杂的中文场景，建议使用                    ，技术派项目中就用了这种方案。

No. 126 1 302




## 第 127 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

国技术派ES实现.， 外  四站 S 上中  分享  日 四

图技术派ES实现查询 (起强
网四                 列推荐)

三 目录        人驴 :三     ov前言                          日
AN  由吾
加技术派Mysql/Redis缓存…                 刚豆
加技术派Mysq/Redis缓存…           首先在阅读这篇文章之前请小伙伴们移驾的上篇技术派整合
加RanalsawVSQL         Canal，并且已经实现MySQL到ES数据同步，接下来才可以继续阅
Te          读这篇文章去SpringBoot整合ES。希望这些前期工作大家一定做
园技术派ES实现查询 (疙…           好。
加技术派Redis分布式锁 (..           在SpringBoot整合ES中，有两种常见方法，一种是
加技术派xjob实现定时              ElasticsearchRestTemplate，另一种是RestHighLevelClient。
ElasticsearchRestTemplate是ES基于Spring集成用法，但是用法
加技术派服务监控之Actua         比较单一，有些复杂查询无法完成; 另一种RestHighLevelClient是
图技术派端口号冲突解决方案        ES原生客户端，适合各种场景查询 。
加技术派Filter实现请求日                   综合考虑下来技术派采用后者ES原生客户端
RestHighLevelClient。
加技术派记录SQL执行日志
加技术派深入理解DB连接..                      、              。                  。             要
    略       1、构造RestHighLevelClient客户端         5
园技术派异常日志报警通知                                                血
加技术派并行访问性能优化         10、引入依赖                         部
加技术泊通用丛语词莹换 (…            在paicoding-service模块中的pom文件中引入es和es-olent 。 忆

加技术派内网穿透模型之o.…              相关依赖
一- 这部分是帮助大家理解 end，面试中可不背 -…-

memo: 2025年4月1 日修改至此，今天有球友说，拿到了美团的实习 offer，真的太棒了，18 号一面、25 号二
面、30 号OC，4月 1 发邮件 offer，节奏拉满了

No. 1271 302




## 第 128 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

一面18号 二面25号 30号 oc 今天的offer

时型: 这么慢吗 一面是几号?
i

要得!
1. java 面试指南 (付费) 收录的科大讯飞非凡计划研发类面经原题: 聊聊 MySQL 的索引
2. Java 面试指南 (付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: MySQL 索引，为什么用

B+树
3. Java 面试指南 (付费) 收录的携程面经同学 10 java 暑期实习一面面试原题: 讲一讲 MySQL 的索引，
如何优化 SQL?

4. Java 面试指南 (付费) 收录的阿里面经同学 5 阿里妈妈 java 后端技术一面面试原题: 索引的分类，创
建索引的最佳实践

5. Java 面试指南 (付费) 收录的 360 面经同学 3 java 后端技术一面面试原题: mysql 的索引用过哪些
6. Java 面试指南 (付费) 收录的用友面试原题: 索引是什么”有哪些索引

7. java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: 普通索引的叶子节点存储的
是什么

8. java 面试指南(付费) 收录的作业帮面经同学 1 Java 后端一面面试原题: innodb底层有哪些数据结构

No. 128 1 302




## 第 129 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

9. Java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: 索引有哪些，区别是什么

37.尽创建索31有哪些注意点?
第一，选择合适的字段
。 比如说频繁出现在 WHERE、JOIN、ORDER BY、GROUP BY 中的字段。

。 优先选择区分度高的字段，比如用户 ID、手机号等唯一值多的，而不是性别、状态等区分度极低的字段，如
果真的需要，可以考虑联合索引。

第二，要控制索引的数量，避免过度索引，每个索引都要占用存储空间，单表的索引数量不建议超过5 个。

要定期通过 SHOW INDEX FROM table_name 查看索引的使用情况，删除不必要的索引。比如说已经有联合索引
(a, b)，单索引 (a) 就是允余的。

第三，联合索引的时候要遵循最左前原则，即在查询条件中使用联合索引的第一个字段，才能充分利用索引。
比如说联合索引 (AR，B，Cc) 可支持 AR、A+B、R+B+C 的查询，但无法支持B或C 的单独查询。
区分度高的字段放在左侧，等值查询的字段优先于范围查询的字段。例如 wHERE A=1 AND B>10 AND c=2 ，优先

(RAR，C，B) 。
如果联合索引包含查询的所需字段，还可以避免回表，提高查询效率。
1. java 面试指南 (付费) 收录的用友人金融一面原题: 索引的作用，加索引需要注意什么

2. Java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 查询和更新都频繁的字段是否适合创
建索引，为什么

3. java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: 索引怎么设计才是最好的

4. Java 面试指南 (付费) 收录的京东面经同学 1 java 技术一面面试原题: MySQL 索引结构，建立索引的
策略

5. java 面试指南 (付费) 收录的阿里面经同学 5 阿里妈妈 java 后端技术一面面试原题: 索引的分类，创
建索引的最佳实践

6. Java 面试指南 (付费) 收录的oppo 面经同学 8 后端开发秋招一面面试原题: 建索引的时候应该注意什
么
7. Java 面试指南 (付费) 收录的京东面经同学 5 java 后端技术一面面试原题: 建立索引考虑哪些问题
38.盖索引哪些情况下会失效呢?

简版: 比如索引列使用了函数、使用了通配符开头的模糊查询、联合索引不满足最左前缀原则，或者使用 or 的时
候部分字段无索引等。

第一，对索引列使用函数或表达式会导致索引失效。

No. 1291 302




## 第 130 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-- 索引失效
SELECT * FROM users WHERE YEAR(Create_time) = 2023;
SELECT * FROM products WHERE pricex2 > 100)

-- 优化方案 (使用范围查询)
SELECT * FROM users WHERE create_time BETNEEN '2023-01-01，'， RND '2023-12-31'，
SELECT * FROM products WHERE price > 50;

第二，LIKE 模糊查询以通配符开头会导致索引失效。

-- 索引失效
SELECT * FROM articles WHERE title LIKE 's%数据库s'

-- 可以使用索引 (但范围有限)
SELECT * FROM articles WHERE title LIKE '数据库s'

-- 解决方案; 考虑全文索引或搜索引擎
SELECT * FROM articles WHERE MATCHI(title) AGAINST( '数据库' );

第三，联合索引违反了最左前缀原则，索引会失效。

-- 假设有联合索引 (a，b，c)

SELECT * FROM table WHERE b = 2 RND c = 3;) -- 索引失效
SELECT * FROM table WHERE a = 1 AND c = 3; -- 只使用a列索引
-- 正确使用联合索引

SELECT * FROM table WHERE a = 1 RND b = 2 RND c = 3;

。 联合索引，但 WHERE 不满足最左前缀原则，索引无法起效。例如: SELECT * FROM table WHERE
column2 = 2 ，联合索引为 (column1，column2) 。

--- 这部分是帮助大家理解 start，面试中可不背 ----
第四，使用 OR 连接非索引列条件，会导致索引失效。

-- 假设name有索引但age没有
SELECT * FROM users WHERE name = '张三' OR age = 25;  -- 全表扫描

-- 优化方案1: 使用UNION ALL

SELECT * FROM users WHERE name = “'张三，
UNION RLL
SELECT * FROM users WHERE age = 25 AND name != '张三';

-- 优化方案2; 考虑为age添加索引

第五，使用 != 或 <> 不等值查询会导致索引失效。

No. 1301302




## 第 131 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

SELECT * FROM user WHERE status != 1;  -- 若大部分行 “status=1`，可能全表扫描

-- 优化方案: 使用范围查询

SELECT * FROM user WHERE status < 1 OR status > 17

-一这部分是帮助大家理解end，面试中可不背 -一-

什么情况下模糊查询不走索引?
模糊查询主要使用 LIKE 语句，结合通配符来实现。
% (代表任意多个字符) 和 (代表单个字符)

SELECT * FROM table WHERE Column LIKE “%XXX名 7

这个查询会返回所有 column 列中包含 xxx 的记录。

但是，如果模糊查询的通配符 % 出现在搜索字符串的开始位置，如 ZIKE “sxxx' ，MySQL 将无法使用索引，
为数据库必须扫描全表以匹配任意位置的字符串。

1. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: where b =5 是否一定
会命中索引? (索引失效场景)

2. java 面试指南 (付费) 收录的京东面经同学 1 Java 技术一面面试原题: 索引失效的情况

3. Java 面试指南(付费) 收录的小公司面经合集同学 1 java 后端面试原题: 编写 SQL 语句哪些情况会导
致索引失效?

Java 面试指南(付费) 收录的比亚迪面经同学 12 java 技术面试原题: 索引失效场景

java 面试指南(付费) 收录的 OPPO 面经同学 1 面试原题: 什么情况下索引失效?

java 面试指南 (付费) 收录的京东面经同学 5java 后端技术一面面试原题: 索引失效情况
java 面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题;: 什么操作会导致索引失效?

39.索引不适合哪些场景呢?

第一，区分度低的列，可以和其他高区分度的列组成联合索引 。

第二，频繁更新的列，索引会增加更新的成本。

第三，TEXT、BLOB 等大对象类型的字段，可以使用前缀索引、全文索引替代。
第四，当表的数据量很小的时候，不超过 1000 行，全表扫描可能比使用索引更快。
---- 这部分是帮助大家理解 start，面试中可不背 ----

为了验证第四条，我们创建了一个小表，然后分别执行全表扫描和索引查询。

六 mm 上

No. 1311 302




## 第 132 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

USE test_db ;

SELECT “WITH INDEX” as test_case;
SELECT UNIX_TIMESTAMP(NOW(6) ) ;
SELECT x FROM users WHERE age
SELECT x FROM users WHERE age
SELECT x FROM users WHERE age
SELECT UNIX_TIMESTAMP(NOW(6) ) ;

II IN
Wu Wu Wu
一放一下一

ve

ALTER TABLE users DROP INDEX idx_age;

SELECT “WITHOUT INDEX” as test_case;
SELECT UNIX_TIMESTAMP(NOW(6) ) ;
SELECT x FROM users WHERE age
SELECT * FROM users WHERE age
SELECT x FROM users WHERE age
SELECT UNIX_TIMESTAMP(NOW(6 ) ) ;

30 ;
30 ;
30 ;

得出的结论的确是这样的，全表扫描更快一些。

No. 132 1 302




## 第 133 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

基于我们的测试结果，我可以得出以下结论:

。 执行计划分析:

无索引时:
type = ALL (全表扫描)
possibtLe_keys = NULL
rows = 20 (预估扫描20行)
Extra =   ing where

有索引时:
type = ref (索引查找)
possibtLe_keys = idx_age

key = idx_age
rows = 5 (预估扫描5行)
fiLtered = 100%

。性能测试结果:
有索引查询时间: 1743576165 .597259 - 1743576165.596335 = 0.000924秒
无索引查询时间: 1743576165.608383 - 1743576165.607739 = 0.000644秒

。 重要发现:
在这个小数据集 (约20条 记录) 的场景下，全表扫描实际上比使用索引还要快一些!

这验证了我们的假设: 在数据量很小的情况下，索引并不一定能提升查询性能，反而可和
外的索引查找开销而咯短降低性能

原因时当数据量很小时，全表扫描的成本很低，因为所有的数据可能都加载到内存中了，使用索引反而需要先查找
索引，再通过索引去找到实际的数据行，增加了额外的 VO 寻址时间。

-一这部分是帮助大家理解 and，面试中可不背 一
性别字段要建立索引吗?
性别字段不适合建立单独索引。因为性别字段的区分度很低。

如果性别字段确实经常用于查询条件，数据规模也比较大，可以将性别字段作为联合索引的一部分，与区分度高的
字段一起，效果会好很多。

什么是区分度?
区分度是衡量一个字段在 MySQL 表中唯一值的比例。

区分度 = 字段的唯一值数量 / 字段的总记录数; 越接近 1，就越适合作为索引。因为索引可以更有效地缩小查询范
围。

例如，一个表中有 1000 条记录，其中性别字段只有两个值 (男、女) ，那么性别字段的区分度只有 0.002，就不
适合建立索引。

可以通过 couNT(pISTINCT column_name) 和 couNT(*) 的比值来计算字段的区分度。例如

No. 1331302




## 第 134 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

SELECT

COUNT(DISTINCT gender) / COUNT(*) RS gender_selectivity
FROM

usersy

什么样的字段适合加索引?
一句话回答:

一般来说，主键、唯一键、以及经常作为查询条件的字段最适合加索引。除此之外，字段的区分度要高，这样索引
才能起到过滤作用; 如果字段经常用于表连接、排序或分组，也建议加索引。同时如果多个字段经常一起出现在查
询条件中，也可以建立联合索引来提升性能。

-一这部分是帮助大家理解 start，面试中可不背 -一
查询条件中的高频字段，比如说WHERE子句中频繁用于等值查询、范围查询或者 IN 列表的字段。

SELECT * FROM orders WHERE status = 'PRID，RND create time > '2023-01-01'7
-- 若`status`和`~create _ time `常组合查询，建联合索引` (status，create_time) ~

多表连接时的关联字段，比如说 user.id 和 order.user_id。
SELECT * FROM user u JOIN order o ON u.id = o.user _ id; -- “user_id-`需索引
参与排序或者分组的字段，可以直接利用索引的有序性，如免文件排序。

SELECT * FROM product ORDER BY price DESC)      -- 单字段排序
SELECT category，COUNT(*) FROM product GROUP BY category;  -- 分组统计

需要利用覆盖索引的字段，可以避免回表操作。

-- 创建联合索引 (user_id，create_ time)
SELECT user_id，create_time FROM orders WHERE user_id = 100;  -- 覆盖索引生效

-一这部分是帮助大家理解end，面试中可不背 -一-

1. java 面试指南 (付费) 收录的字节跳动面经同学 1 技术二面面试原题: 性别字段要建立索引吗? 为什
么? 什么是区分度?” MySQL查看字段区分度的命令?

2. Java 面试指南付费) 收录的快手同学 2 一面面试原题: 什么样的字段适合加索引? 什么不适合?
40.索引是不是建的越多越好?

索引不是越多越好。虽然索引可以加快查询，但也会带来写入变慢、占用更多存储空间、甚至让优化器选错索引的
风险。

---- 这部分是帮助大家理解 start，面试中可不背 ---
每次数据写入 (INSERT/UPDATE/DELETE) 时，MySQL 都需同步更新所有相关索引，索引越多，维护成本越高。
假如某表有 10 个索引，插入一行数据需更新 10 个 B+树结构，导致写入延迟增加 5~10 倍。

No. 1341302




## 第 135 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

假如某表数据量 100GB，若建 5 个索引，总存储可能达到 200GB+ 。

索引过多时，优化器需评估更多可能的执行路径，可能导致选择困难症，优化器也会选错索引。
再比如说，已有联合索引 (A, B, C)，再单独建 (A) 或 (A, B) 索引即为允余。

单表索引数量建议不超过 5 个，MySQL 官方建议单表索引总字段数 < 表字段数的 30% 。

---- 这部分是帮助大家理解end，面试中可不背 ----

说说索引优化的思路?

一句话回答:

先通过慢查询日志找出性能瓶颈，然后用 EXPLAIN 分析执行计划，判断是否走了索引、是否回表、是否排序。接
着根据字段特性设计合适的索引，如选择区分度高的字段，使用联合索引和有覆盖索引，避免索引失效的写法，最后
通过实测来验证优化效果。

1. java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: 索引优化的思

memo: 2025年4月2日修改至此，今天有球友说，拿到了百度的实习 offer，仅用了一个月的时间，可太强
了。

No. 1351 302




## 第 136 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥 VIP 10 群 (443) CS                     v |
名- 沉默王二-二哥: 面渣逆获并发编程篇 2.0 .…
 全 百度hr面过了
上 me-
7 口头oc了
轩和=
从 太强了1
| 恭喜六:
站 大
了 IE
”恭喜恭喜

一苞

六 昌 |
这 信  现在已经是度xz 了
41.二为什么 InnoDB 要使用 B+树作为索引?

一句话总结:

因为 B+ 树是一种高度平衡的多路查找树，能有效降低磁盘的 IO 次数，并且支持有序遍历和范围查询。

No. 1361302




## 第 137 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

本 四 本
Eee

这里的条针P林醒:t                                                       这里的村P未面出

了
7
二                                                                                                                                                                                       加
村
E2                                                                                                                               E
中             呈            四                mm             mm             mo                    ml           mm           m3
[1

查询性能非常高，其结构也适合 MySQL 按照页为单位在磁盘上存储。
像其他选项，比如说哈希表不支持范围查询，二又树层级太深，B 树又不方便范围扫描，所以最终选择了 B+ 树。
再换一种回答:

。 相比哈希表: B+ 树支持范围查询和排序

。 相比二又树和红黑树: B+ 树更矮胖"，层级更少，磁盘 IO 次数更少

。 相比B树: B+ 树的非叶子节点只存储键值，叶子节点存储数据并通过链表连接，支持范围查询
另外一种回答版本:

B+树是一种自平衡的多路查找树，和红黑树、二又平衡树不同，B+树的每个节点可以有 m 个子节点，而红黑树和
二叉平衡树都只有 2 个。

No. 1371302




## 第 138 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

MYSQL INNODB B+ TREE

另外，和 B 树不同，B+树的非叶子节点只存储键值，不存储数据，而叶子节点存储了所有的数据，并且构成了一
个有序链表。

这样做的好处是，非叶子节点上由于没有存储数据，就可以存储更多的键值对，再加上叶子节点构成了一个有序链
表，范围查询时就可以直接通过叶子节点间的指针顺序访问整个查询范围内的所有记录，而无需对树进行多次遍
历。查询的效率比 B 树更高。

1. 推荐阅读: 终于把 B 树搞明白了
2. 推荐阅读: 一篇文章讲透 MySQL 为什么要用 B+树实现索引
---- 这部分是帮助大家理解 start，面试中可不背 ---
先说说B 树。
B 树是一种自平衡的多路查找树，和红黑树、二叉平衡树不同，B 树的每个节点可以有 m 个子节点，而红黑树和
二叉平衡树都只有 2 个。

换句话说，红黑树、二又平衡树是细高个，而 B 树是矮胖子。

ooto |                                 0023                                             0066

0009 | 0011         0013 | 0024 ”0027 |‖ 0064 | 0070 “0088

再来说说内存和磁盘的 1O 读写。

No. 1381302




## 第 139 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

磁盘

为了提高读写效率，从磁盘往内存中读数据的时候，一次会读取至少一页的数据，如果不满一页，会再多读点。

比如说查询只需要读取 2KB 的数据，但 MySQL 实际上会读取 4KB 的数据，以装满整页。页是 MySQL 进行内存
和磁盘交互的最小逻辑单元。

再比如说需要读取 5KB 的数据，实际上 MySQL 会读取 8KB 的数据，刚好两页。

因为读的次数越多，效率就越低。就好比我们在工地上搬砖，一次搬 10 块砖肯定比一次搬 1 块砖的效率要高，反
正我每次都搬 10 块 (钨) 。

对于红黑树、二又平衡树这种细高个来说，每次搬的砖少，因为力气不够嘛，那来回跑的次数就越多。

通常 B+ 树高度为 3-4 层即可支持 TB 级数据，而每次查询只需 2-4 次磁盘 VDO，远低于二叉树或红黑树的
O(log2N) 复杂度

树越高，意味着查找数据时就需要更多的磁盘 10，因为每一层都可能需要从磁盘加载新的节点。

B 树的节点通常与页的大小对齐，这样每次从磁盘加载一个节点时，正好就是一页的大小。

No. 1391302




## 第 140 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

上         四            四         四            加        加

ww  we  ar    av|] [au   36mm| [6  75p] Dan  soaq| [saw

B 树的一个节点通常包括三个部分:
。 键值: 即表中的主键
。 指针: 存储子节点的信息
。 数据: 除主键外的行数据

正所谓“祸兮福所倚，福兮祸所伏"，因为 B 树的每个节点上都存储了数据，就导致每个节点能存储的键值和指针变
少了，因为每一个节点的大小是固定的，对吧?

于是 B+树就来了，B+树的非叶子节点只存储键值，不存储数据，而叶子节点会存储所有的行数据，并且构成一个
有序链表。

P 4 PP 8 p         指向子结点的揪针
己“] 六
|               E
P 2 P      P 6 P      P 10
1   2 3   全 5   6 了   8 9   10 11
汪  四本 因汪攻 人IEE

这样做的好处是，非叶子节点由于没有存储数据，就可以存储更多的键值对，树就变得更加矮绊了，于是就更有劲
了，每次搬的砖也就更多了 (和驴) 。

相tt B 树，B+ 树的非叶子节点可容纳的键值更多，一个 16KB 的节点可存储约 1200 个键值，大幅降低树的

局展。

由此一来，查找数据进行的磁盘 IO 就更少了，查询的效率也就更高了。

No. 140 1 302




## 第 141 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭
再加上叶子节点构成了一个有序链表，范围查询时就可以直接通过叶子节点间的指针顺序访问整个查询范围内的所
有记录，而无需对树进行多次遍历。
B 树就做不到这一点。
一- 这部分是帮助大家理解 end，面试中可不背 一
B+树的叶子节点是单向链表还是双向链表? 如果从大值向小值检索，如何操作?
B+树的叶子节点是通过双向链表连接的，这样可以方便范围查询和反向遍历。

。 当执行范围查询时，可以从范围的开始点或结束点开始，向前或向后遍历。
。 在需要对数据进行逆序处理时，双向链表非常有用。

如果需要在 B+树中从大值向小值进行检索，可以先定位到最右侧节点，找到包含最大值的叶子节点。从根节点开
始向右遍历树的方式实现。
国 曲面: 和记录中的主键
国 ms wereameaee        oevJ TIRE
 et  | 省
ozJJREEIRGIREEEDI                          osJ REGTRGRECEDI
[下辐四办  四加图邓 |翌国必   卡国图图轿 |图图图图 ME

欧智华1593480648@qqcom

定位到最右侧的叶子节点后，再利用叶节点间的双向链表向左遍历就好了。
为什么 MongoDB 的索引用 B树，而 MySQL 用 B+ 树?

MongoDB 通常以JSON 格式存储文档，查询以单键查询 (如 find({_idq: 123}) ) 为主。B 树的“节点婚存键又
存数据"的特性允许查询在非叶子节点提前终止，从而减少 /O 次数。

简化 B- 树

No. 1411 302




## 第 142 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

MySQL 的查询通常涉及范围 (waERE id > 100) 、排序 ( oORpER BY ) 、连接 ( JorN ) 等操作。B+ 树的叶子
节点是链表结构，天然支持顺序遍历，无需回溯至根节点或中序遍历，效率远高于B 树。

简化 B+ 树

-一这部分是帮助大家理解 start，面试中可不背 -一

特性                            MongoDB (B树)

数据模型                         文档型数据库

存储方式                      数据文件+索引文件分离
查询模式                         侧重单文档查询

数据访问模式                  随机访问为主

索引存储内容                非叶节点存储数据指针
范围查询效率                  需要多次树人遍历

内存利用率                      单个查询路径缓存更有效

推荐阅读: 为什么 MongoDB 索引用 B树，而 MySQL 用 B+ 树?

---- 这部分是帮助大家理解and，面试中可不背 ---
1. java 面试指南 (付费) 收录的字节跳动商业化一面的原题: 说说 B+树，为什么 3 层容纳 2000W 条，

ww

为什么 2000w 条数据查的快

MySQL InnoDB (B+树)
关系型数据库

聚簇索引数据与主键绑定存储
侧重范围查询和复杂连接
顺序访问更频繁

只有叶节点存储数据

通过叶节点链表高效遍历
适合批量扫描缓存

.java 面试指南 (付费) 收录的国企面试原题: 说说 MySQL 的底层数据结构，B 树和 B+树的区别
.java 面试指南 (付费) 收录的腾讯面经同学 22 暑期实习一面面试原题: MySQL 为什么选用 B+树

.java 面试指南 (付费) 收录的小米面经同学 E 第二个部门java 后端技术一面面试原题:

索引的底层机制

说一说 mysql

. java 面试指南(付费) 收录的京东面经同学 1 java 技术一面面试原题: MySQL 索引结构，建立索引的

策略

.java 面试指南 (付费) 收录的腾讯云智面经同学 16 一面面试原题:

B+树?

No. 142 1 302

MySQL 索引结构，为什么用




## 第 143 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

7. java 面试指南 (付费) 收录的小公司面经同学 5 java 后端面试原题: 数据库索引讲一下，然后为什么
会加快查询速度，我讲到了 B+树，然后问了 B 数与 B+树区别

8. java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题;: B+树的页是单向
链表还是双向链表? 如果从大值向小值检索，如何操作?

9. java 面试指南 (付费) 收录的得物面经同学 1 面试原题: 项目索引，MySQL索引，mongoDB为什么用
的B树，二者比较

10. java 面试指南 (付费) 收录的oppo 面经同学 8 后端开发秋招一面面试原题: Mysql索引的数据结构，
为什么选择这样的数据结构

11. java 面试指南 (付费) 收录的京东面经同学 8 面试原题: 索引

12. java 面试指南 (付费) 收录的美团同学 9 一面面试原题: B+树?

13. java 面试指南 (付费) 收录的美团面经同学 15 点评后端技术面试原题: 索引的数据结构

14. java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: B+树了解吗? 底层呢? 为什么这么用?

15. java 面试指南 (付费) 收录的滴滴面经同学 3 网约车后端开发一面原题: MySQL索引原理，B+树更扁
有什么好处

memo: 2025年4月3日修改至此，今天有球友说，拿到了美团的实习 offer，恭喜啊。

二哥二哥，我想请教一个问题。
沾立亏出音全二二有本了 包芝-于国语Pr 划

用六村 轩必号LT十已Pa 革
下来。然后刚刚又收到美团的邮件 offer了

42.二一棵B+树能存储多少条数据呢?
一句话回复:

一棵 B+ 树能存多少数据，取决于它的分支因子和高度。在 InnoDB 中，页的默认大小为 15KB，当主键为 bigint
时，3 层 B+ 树通常可以存储约 2000 万条数据。

No. 1431302




## 第 144 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

非叶子节点
键值+指针=14字节
16384/14=1170单元
Degree=1170

1条记录1k
一个叶子节点存16条             树的深度树2，只需要3次IO
1170x1170x16=21902400条记录
一- 这部分是帮助大家理解 start，面试中可不背 -一

先来看一下计算公式:

最大记录数 = (分支因子)”(树高度-1) x 叶子节点容量
再来看一下关键参数:
外、页大小，默认 16KB

@@、主键大小，假设是 bigint 类型，那么它的大小就是 8 个字节。
图、页指针大小，InnoDB 源码中设置为 6 字节，4 字节页号 + 2 字节页内偏移。

#define ERADDRESTZE 6      /#k address size is 6 bytes #/
#define FLST_BASE_NODE_SIZE     (4+2#kFILADDR SIZE)

/水

水                   List--Length:4

炒               FEERADDRESIZE prv page node :4

水                  offset      :2

水              FILLADDRLSTZE nxt page node :4

水                  offset      :2

水                                            闭/

所以非叶子节点可以存储 16384/14(键值+指针)=1170 个这样的单元。

-一这部分是帮助大家理解end，面试中可不背 -一-

No. 1441 302




## 第 145 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

现在有一张表 2kw 数据，我这个 b+树的高度有几层?
对于 2KW 条数据来说，B+树的高度为 3 层就够了 。

上-了                                                            1170个单元
根节点                                                        (1170个指针
指针1            指针2           到          指针1170
1条记录1k                  1条记录1k        AN                 1条记录1k
叶节点                       1页大小16k                      1页大小16k | ee                   1页大小16k
可存16条记录                            可存16条记录                                                           可存16条记录

推荐阅读: Innodb 引敬中 B+树一般有几层? 能容纳多少数据量?

每个叶子节点能存放多少条数据?

如果单行数据大小为 1KB，那么每页可存储约 16 行 (16KB/1KB) 数据。
一- 这部分是帮助大家理解 start，面试中可不背 -一

假设有这样一个表结构:

CRERTE TRBLE “user” (

~id” BIGINT PRIMRRY KEY，       -- 8字节

~name” VRRCHAR(255) NOT NULL， -~- 实际长度50宇节 (UTF8MB4，每个字符最多4字节)
~age” TINYINT，             -- 1字节

~emai1l”VRARCHRAR(255)         -- 实际长度30字节，可为NULL

) ROW_FORMRT=COMPRCT)

那么一行数据的大小为: 8 + 50 + 1 + 30 = 89 字节。

行格式的开销为: 行头 5 字节+指针 6 字节+可变长度字段开销 2 字节 (name 和email 各占 1 字节) + NULL 位图
1字节 = 14 字节。

所以每行数据的实际大小为: 89 + 14 = 103 字节。

每页大小默认为 16KB，那么每页最多可以存储 16384 / 103 = 158 行数据。

--- 这部分是帮助大家理解end，面试中可不背 ----

1. java 面试指南 (付费) 收录的字节跳动商业化一面的原题: 说说 B+树，为什么 3 层容纳 2000W 条，
为什么 2000w 条数据查的快

2. java 面试指南(付费) 收录的奇安信面经同学 1 java 技术一面面试原题: innodb 使用数据页存储数
据? 默认数据页大小 16K，我现在有一张表，有 2kw 数据，我这个 b+树的高度有几层?

3. java 面试指南(付费) 收录的美团面经同学 18 成都到家面试原题: 一张表最多存多少数据 (我答得
2kw，根据b+树的三层高度计算)

4. java 面试指南 (付费) 收录的得物面经同学 1 面试原题: MySQL B+树的度数越大越好吗，一般设多少

No. 1451302




## 第 146 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

5. Java 面试指南 (付费) 收录的腾讯面经同学 29 java 后端一面原题: InnoDB中一个三层的B+树能存多
少数据? 每个叶子节点能存放多少条数据?

memo: 2025年4月4日修改至此，今天有球友问，有没有英文版的面渣逆效，他人在国外留学，国外也开始卷
八股了吗，真的离谱。

请问有英文翻译版的吗

12:46

上

要在国外找工作

请问有吗?

13:00

对的，就是直接翻译翻译不出一些术语，实不相
瞒我昨天刚挂了八股文图

cicd的岗位，他问我编程的八股文
43.索引为什么用 B+树不用普通二叉树?

No. 146 1 302




## 第 147 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

普通二又树的每个节点最多有两个子节点。当数据按顺序递增插入时，二叉树会退化成链表，导致树的高度等于数
据量。

此时查找 id=7 就需要 7 次 VO 操作，相当于全表扫描。而 B+ 树作为多叉平衡树，能将数亿级的数据量控制在 3-4
层的树高，能极大减少磁盘的 /O 次数。

为什么不用平衡二叉树呢?
平衡二又树虽然解决了普通二又树的退化问题，但每个节点最多只有两个子节点的问题依然存在。

No. 1471 302




## 第 148 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

1. Java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习java 后端面试原题: MySQL 索引为什
么使用 B+树而不是用别的数据结构?

2. java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 为什么不用二叉树? 为什么
不用AVL树?

44.二为什么用 B+ 树而不用 B 树呢?
B+ 树相比 B 权有 3 个显著优势:
第一，B 树的每个节点既存储键值，又存储数据和指针，导致单节点存储的键值数量较少。

ET
一[17| [5
奖 |P1| |P3| |P3
夏                         磁
= 回叫  26| 38      总 65 87
亲轩国医      加加上蔬区      殉国国医
3 5   9 10  13 15  28 29  36 68  75 79  90 99
磁盘块5       磁盘块6       磁盘块7       磁盘块8       磁盘块9       磁盘块10      磁盘块11

一个16KB 的 InnoDB 页，如果数据较大，B 树的非叶子节点只能容纳几十个键值，而 B+ 树的非叶子节点可以容
纳上千个键值。

No. 148 1 302





## 第 149 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

第二，B 树的范围查询需要通过中序人遍历逐层回溯; 而 B+ 树的叶子节点通过双向链表顺序连接，范围查询只需定
位起始点后顺序遍历链表即可，没有回溯开销。

1            8           14          18          24 人31             35 41 53
3 /111 /118 /5 /33        sz| /4 /加
5             1            17            22             29 ) 34                39 /47 /6
P         P         P         P         Pl/ IIP            P        P/ |IP

磁盘块5 磁盘块6 。 磁盘块7 磁盘块8 磁盘块9 ”磁盘块10 磁盘块11 。 磁盘块12 ”磁盘块13

第三，B 树的数据可能存储在任意节点，假如目标数据恰好位于根节点或上层节点，查询仅需 1-2 次 VO;， 但如果
数据位于底层节点，则需多次 /O，导致查询时间波动较大。

而 B+ 树的所有数据都存储在叶子节点，查询路径的长度是固定的，时间稳定为 O(logN)，对 MySQL 在高并发场
景下的稳定性至关重要。

想要了解 B 树和 B+树的更多区别，推荐阅读:
。 GitHub: B 树和 B+树详解
。 思否: 面试官问你 B 树和 B+树，就把这篇文章丢给他
。 极客时间: 为什么用 B+树来做索引?
。 二是到悍的种子: 用 16 张图就给你讲明白 MySQL 为什么要用 B+树做索引
B+树的时间复杂度是多少?
O(logN)。
树的高度 h 为:

关= logw N|                                                     (上
其中 N 是数据总量，m 是阶数。每层需要做一次二分查找，复杂度为 $O(log m)$。
总复杂度为:

No. 1491 302




## 第 150 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

O(logw N.logm)=O(logN)                              (2)
为什么用 B+树不用跳表呢?
跳表本质上还是链表结构，只不过把某些节点抽到上层做了索引。

一|  加“~              >国人

Rbtt去 国生 >天| 。   7。 上 1 。 16|

一条数据一个节点，如果需要存放 2000 万条数据，且每次查询都要能达到二分查找的效果，那么跳表的高度大约
为24层 (2的24次方) 。

在最坏的情况下，这 24 层数据分散在不同的数据页，查找一次数据就需要 24 次磁盘 /O。
而 2000 万条数据在 B+树中只需要 3 层就可以了。

B+树的范围查找怎么做的?
一句话回答:

先通过索引路径定位到第一个满足条件的叶子节点，然后顺着叶子节点之间的链表向右/向左扫描，直到超过范
围。

详细版:
B+ 树索引的范围查找主要依赖叶子节点之间的双向链表来完成。
第一步，从 B+ 树的根节点开始，通过索引键值逐层向下，找到第一个满足条件的叶子节点。

第二步，利用叶子节点之间的双向链表，从起始节点开始，依次向后遍历每个节点。当索引值超过查询范围，或者
遍历到链表末尾时，终止查询。

--- 这部分是帮助大家理解 start，面试中可不背 ----
比如说在下面这棵 B+ 树上查找 45。

No. 1501302




## 第 151 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

第一步，从根节点开始，因为比 25 大，所以从右子树开始。因为 45 比 35大，所以和右边的索引比较，右侧的索
引也是 45，所以继续往右子树查找。

第二步，从叶子节点 45 开始，依次遍历，找到 45。

No. 1511 302




## 第 152 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

国辆-

一- 这部分是帮助大家理解 end，面试中可不背 一
了解快排吗?
快速排序使用分治法将一个序列分为较小和较大的 2 个子序列，然后递归排序两个子序列，由东尼:霍尔在 1960 年

提出。
| 引 | 外 | |
加
  二  |
其核心思想是:
1. 选择一个基准值。

2， 将数组分为两部分，左边小于基准值，右边大于或等于基准值。
3 对左右两部分递归排序，最终合并。

public static void quickSort(int[] arr，int low，int high) {
if (low < high) {
int pivotIndex = partition(arr，1low，high) 7
quickSort(arr，1low，PpivotIndex - 1);
quickSort(arr，PpivotIndex + 1，high) 7
】}
】}
private static int partition(int[] arr，int low，int high) {
int pivot = arzr[high];

No. 1521 302




## 第 153 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

int研= low - 17;
for (int j = low; j < high; j++) {
if (arr[j] <= pivot) {
了+二7
swap(arr，i，j) 1;
】
】}
swap(arr，i + 1，high)7
return 斌+ 17
)
Private static void swap(int[] arr，int i，int j) {
int temp = arr[i];

arr[il = arr[j]7
arr[j] = temp;
)}
推荐链接: 快速排序

1. java 面试指南 (付费) 收录的支付宝面经同学 2 春招技术一面面试原题: 聚簇索引和非聚复索引的区
别? B+树叶子节点除了存数据还有什么?

2. Java 面试指南 (付费) 收录的奇安信面经同学 1 java 技术一面面试原题: b 树和 b+树有什么区别

3. java 面试指南(付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: MySQL 索引为什
么使用 B+树而不是用别的数据结构?

4. java面试指南 (付费) 收录的字节跳动面经同学 8 java 后端实习一面面试原题: mysql b+树和b树的区
别

5. java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: B+树有哪些优点
6. java 面试指南 (付费) 收录的同学 1 贝壳找房后端技术一面面试原题: 为什么用b+树不用b树

7. Java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题;: 索引为什么用B+树不用B树 时间复
杂度深究 b+树 快速排序…

45.B+树索引和 Hash 索引有什么区别?
简版回答:
B+ 树索引支持范围查询、有序扫描，是 InnoDB 的默认索引结构。

No. 1531302




## 第 154 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

Hash 索引只支持等值查找，速度快但功能弱，常见于 Memory 引擎。
国 sp一人itmtef丰as

国 sr一aasietpos

行in隶数据
|

稍微详细一点的回答:

B+ 树索引是一种平衡多路搜索树，所有数据存储在叶子节点上，非叶子节点仅存储索引键。叶子节点通过指针连
接形成有序链表，天然支持排序。

并且支持范围查询、模糊查询，是 InnoDB 默认的索引结构 。
Hash 索引基于哈希函数将键值映射到固定长度的哈希值，通过哈希值定位数据存储的位置。

No. 1541302




## 第 155 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

完全无序，只支持等值查询，常见于 Memory 引擎。
--- 这部分是帮助大家理解 start，面试中可不背 ----
因为 B+ 树是 InnoDB 的默认索引类型，所以创建 B+ 树的时候不需要指定索引类型。

CRERTE TRBLE example_btree |!
id INT AUTO_INCREMENT PRIMRRY KEY，
name VRARCHRAR(255) ，
INDEX name_index (name)

) ENGINE=InnoDB》

可以通过 UNTouE HasH 创建哈希索引:

CRERATE TRBLE example_hash (
id INT AUTO_INCREMENT PRIMRRY KEY，
name VRARCHRAR(255) ，
UNIOUE HASH (name)

) ENGINE=MEMORY，

InnoDB 并不提供直接创建哈希索引的选项，因为 B+ 树索引能够很好地支持范围查询和等值查询，满足了大多光
数据库操作的需要。

不过，InnoDB 内部使用了一种名为"自适应哈希索引”(Adaptive Hash Index, AHI) 的技术，当某些索引值频繁访
问时，InnoDB 会在 B+ 树基础上自动创建哈希索引，兼具两者的优点。

可通过 SHOW VARIABLES LIKE 'innodb adaptive _hash index'; 查看自适应哈希索引的状态。

mysqL> SHOW VARIABLES LIKE 'innodb_adaptive_hash_index ' ;
+----------------------------+-------+

| VariabtLe_name

如果返回的值是 ON，说明自适应哈希索引是开启的。
--- 这部分是帮助大家理解and，面试中可不背 -…

1. Java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: 为什么不用hash索引

46.二聚族索引和非聚族索引有什么区别?

聚复索引的叶子节点存储了完整的数据行，数据和索引是在一起的。InnoDB 的主键索引就是聚簇索引，叶子节点
不仅存储了主键值，还存储了其他列的值，因此按照主键进行查询的速度会非常快。

No. 155 1 302




## 第 156 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

每个表只能有一个聚艇索引，通常由主键定义。如果没有显式指定主键，InnoDB 会隐式创建一个隐藏的主键索引

row_id。

非聚复索引的叶子节点只包含了主键值，需要通过回表按照主键去聚簇索引查找其他列的值，唯一索引、普通索引
等非主键索引都是非聚得索引。

No. 156 1 302




## 第 157 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

每个表都可以创建多个非聚复索引，如果不想回表的话，可以通过覆盖索引把要查询的字段也放到索引中 。
--- 这部分是帮助大家理解 start，面试中可不背 ----
一张表只能有一个聚簇索引。

CRERTE TARBLE user (
id INT PRIMRARY KEY，
name VRRCHRR(100) ，
age INT

) 7

主键 id 是聚复索引，B+ 树的叶子节点直接存储了 (id, name, age)。
一张表可以有多个非聚得索引。

CRERTE INDEX idx_name ON user(name) 7
CRERTE INDEX idx_age ON user(age) 1

idx_name 是非聚簇索引，叶子节点存的是 name -> id，查整行数据要回表。
idx_age 也是非聚簇索引，叶子节点存的是 age -> id，查整行数据也要回表。

No. 1571302




## 第 158 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

想要了解更多聚簇索引和非聚簇索引，推荐阅读:

e 大哥:      锅    么区别?

。 聚篮索引、非聚篮索引、联合索引、唯一索引
。 松哥: 再聊 MySQL 聚篮索引
---- 这部分是帮助大家理解and，面试中可不背 ---

1. java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: mysql: 聚簇索31和非聚簇索引区别

2. java 面试指南 (付费) 收录的支付宝面经同学 2 春招技术一面面试原题: 聚簇索引和非聚簇索引的区
别? B+树叶子节点除了存数据还有什么?

3. Java 面试指南 (付费) 收录的字节跳动面经同学 1 Java 后端技术一面面试原题: 聚簇索引是什么? 非
聚簇索引是什么?

4. java面试指南 (付费) 收录的腾讯云智面经同学 16 一面面试原题: 聚徐素引和非聚簇索引的区别?

5. Java 面试指南 (付费) 收录的快手面经同学 1 部门主站技术部面试原题: Mysql 的聚簇索引和非聚篮索
引的区别是什么?

6. Java 面试指南(付费) 收录的作业帮面经同学 1 Java 后端一面面试原题: mysql的聚复索引是什么
7. java 面试指南(付费) 收录的腾讯面经同学 29 java 后端一面原题: MySQL的索引怎么存储的? 每个素
引一个B+树，还是多个索引放一个B+树? 叶子节点中存的是什么数据?

memo: 2025年4月5 日修改至此，今天有拿到美团暑期实习的球友说，简历找二哥修改了两次，基本上不卡第
一学历的都有面，很棒。

No. 158 1 302




## 第 159 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

基本上不卡第一学历的都有面

咽咽

二哥改的好哈哈哈哈

就是找您改了两次

47.过回表了解吗?
当使用非聚复索引进行查询时，MySQL 需要先通过非聚徐索引找到主键值，然后再根据主键值回到聚簇索引中查
找完整数据行，这个过程称为回表。

ES                                                         E
EREE |攻                                                       图
去

假设现在有一张用户表 users:

No. 1591 302




## 第 160 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CRERTE TRBLE users |(
id INT PRIMRARY KEY，
name VRARCHRR(50) ，
age INT，
email VRARCHRAR(50)，
INDEX (name)

SELECT * FROM users WHERE name = “'王二'

查询过程如下:
。 第一步，MySQL 使用 name 列上的非聚簇索引查找所有 name = “'王二' 的主键id。
。 第二步，使用主键 id 到聚簇索引中查找完整记录。

回表的代价是什么?
回表通常需要访问额外的数据页，如果数据不在内存中，还需要从磁盘读取，增加 /O 开销。

No. 1601302




## 第 161 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

加 sa: mmeapmaw
辐 ar: pmzmameuse        oa GT交
 了it人和

ooaJ RARTTTT     De [Pa
图图图图|卡圈加国医  8园加| EEEE  [下图图于图|站图图图图
有ELELE 图贸国图图图 一上久久罚图下贺久久昌 EEE
enpnanerDeny |

下
县
国
国
昌
下|
国
国
帮
田
到
旨s
日
志
日
有
辐
有
二
田
日
田
田

本

可通过覆盖索引或者联合索引来避免回表。

-- 原表结构
CRERTE TARBLE users (
id INT PRIMRARY KEY，
name VRARCHRR(50) ，
age INT，
INDEX idx_name (name)

)

-- 需要查询name和age
SELECT name，age FROM Users WHERE name

-- 这会回表，因为age不在idx_name索引中

-- 优化方案1: 创建包含age的联合索引
RALTER TRBLE users ADD INDEX idx_name_age (name，age) 7

-- 现在同样的查询不需要回表

什么情况下会触发回表?

No. 1611 302




## 第 162 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

第一，当查询字段不在非聚簇索引中时，必须回表到主键索引获取数据。
第二，查询字段包含非索引列 (如 SELECT *) ，必然触发回表。
回表记录越多好吗?

回表记录越多，通常代表性能越差，因为每条记录都需要通过主键再查询一次完整数据。这个过程涉及内存访问或
磁盘 10，尤其当缓存命中率不高时，回表会严重影响查询效率。

了解 MRR 吗?
MRR 是 InnoDB 为了解决回表带来的大量随机 IO 问题而引入的一种优化策略。

索引0       reag_rmcl_buffer       reaegl_rmcl_buffer
=了          td=999             fg=9o2                           L9o2

索引区
L2
本

它会先把非聚簇素引查到的主键值列表进行排序，再按顺序去主键索引中批量回表，将随机 VO 转换为顺序 VO，
以减少磁盘寻道时间。

一- 这部分是帮助大家理解 start，面试中可不背 -…-

可通过 sHow VARIABLES LIKE 'optimizer_switch'; 查看 MRR 是否启用。

=                           十
| optimizer_switch | index_merg     n,index_merge_unioi     n,index_merge_sort_unio
n=on,index_merge_intersection=on,engine_condition_pushdown=on,index_condition_
pushdown=on,mrr=on,mrr_cost_based=on,bLock_nested_Loop=on,batched_key_access=0
ff,materiaLizatton=on,Semtjotn=son, [0osescan=on,firstmatch=on,dupLicateweedout=

on,Ssubquery_materialLization_cost_based=on,use_index_extensions=on,condition_fa
nout_fiLter=on,derived_merge=on,use_invisibte_indexes=off,skip_scan=on,hash_jo
in=on,Ssubquery_to_derived=off,prefer_ordering_index=on,hypergraph_optimizer=of
f,derived_condition_pushd      on,hash_set_operation

二----                                                              -

No. 162 1 302




## 第 163 页


面渣逆袭MySQL篇V2-让天下所有的面渣都仙

约

其中 mrr=on 表示启用 MRR，mrr_cost_based=on 表示基于成本决定使用 MRR。

另外可以通过 show variables like 'read _rnd buffer_size'; 查看 MRR 的缓冲区大小，默认是 256KB。

mysqL> Show variabtLes Like 'read_rnd_buffer_Ssize'

我们来创建一个表，插入一些数据，然后执行一个查询来演示 MRR 的效果。

CRERTE DRTRBASE IF NOT EXISTS mrr_test)

USE mrr_test)

CRERTE TRBLE IF NOT EXISTS orders (id INT AUTO_INCREMENT PRIMRARY KEY，user_id INT
order_date DRATE，amount DECIMAL(10,2)，status VRARCHAR(20) ，INDEX idx_user_date(user_id，
order_date));

DELIMITER //
CRERATE PROCEDURE generate_test_datal)
BEGIN
DECLRRE 半 INT DEFRAULT 17
WHILE 1 <= 100000 DO
INSERT INTO orders (user_id，order_date，amount，status)

VRALUES (
FLOOR(1 + RARND() * 1000)， -- Random user_id between 1 and 1000
DRTE_ADD('2023-01-01' ，INTERVRAL FLOOR(RRND() * 365) DRY)， -- Random date in
2023
ROUND(10 + RRND() * 990，2)， -- Random amount between 10 and 1000
ELT(1 + FLOOR(RRND() * 3)， "completed'， 'pending'， 'cancelled') -- Random
status
) 7
SET ii=I+li
END WHILE，
END //
DELIMITER )

CRLL generate_test_datal);
DROP PROCEDURE generate_test_datai"

查看 MRR 开启和关闭时的性能数据:

-- 确保MRR开启并设置足够大的缓冲区
SET SESSION optimizer_switch='mrr=onvmrr_cost_ based=off')
SET SESSION read_rnd buffer_size = 16*1024x*102417

No. 1631302




## 第 164 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

-- 清理缓存和状态
FLUSH STRTUS)
FLUSH TARBLES)

-- 强制使用二级索引并回表查询 (通过选择未被索引的列)

SELECT 'Raw data access pattern with MRR ON'， as test_casei

SELECT /*+ MRR(orders_mrr_ test) */ id，shipping_address，customer_name
FROM orders_mrr_test FORCE INDEX(idx_user_date)

WHERE user_iqd IN (100,200,300,400,500,600,700,800,900,1000)

RND order_date BETWEEN '2023-03-01'， RND '2023-04-01

LIMIT 157

-- 显示处理器状态
SHOW STATUS LIKE 'Handler S')
SHOW STATUS LIKE 'smrrg'

-- 对比: 关闭MRR

SET SESSION optimizer_switch='mrr=off,mrr_cost_based=off';
FLUSH STRTUS)

FLUSH TARBLES)

SELECT 'Raw data access pattern with MRR OFF，as test_case)
SELECT id，shipping_address，customer_name

FROM orders_mrr test FORCE INDEX(idx_user_date)

WHERE user_iqd IN (100,200,300,400,500,600,700,800,900,1000)
RND order_date BETNEEN '2023-03-01，RND '2023-04-01，

LIMIT 157

-- 显示处理器状态

SHOW STRTUS LIKE 'Handler g%')

SHOW STRTUS LIKE Smrrg')

-- 显示详细的执行计划

EXPLRAIN FORMRAT=TREE

SELECT /*+ MRR(orders_mrr_ test) */ id，shipping_address，customer_name
FROM orders_mrr_test FORCE INDEX(idx_user_date)

WHERE user_iqd IN (100,200,300,400,500,600,700,800,900,1000)

RND order_date BETWEEN '2023-03-01'， RND '2023-04-01 7"

可以看到 MRR 开启时的结果对比:

No. 1641 302




## 第 165 页


四
| test_case
|-

Customer
Customer
Customer
Customer
Address            Customer

|                                  Customer

|                                  Customer

|      124576                      Customer

|      123457                      Customer

|      162422 | Address            Customer

Address            Customer      |      184441 | Address            Customer
Address            Customer      |       60032 | Address            Customer
Address            Customer      |      186648 | Address            Customer
Address            Customer      |       52701 | Address            Customer
Address            Customer      |      181798 | Address            Customer
Customer      |                                  Customer

Customer      |                                  Customer

Customer      |                                  Customer

Customer      |                                  Customer

Customer      |                                  Customer

从测试结果中，我们可以观察到几个重要的现象 :

MRR开启时的访问模式:
id序列更加有序: 9929，13024，17198，19874，24086，24936 .….

HandtLer_read_rnd: 15 (表示进行了批量读取 )
HandtLer_read_next: 99 (表示在索引上的扫描)

MRR关闭时的访问模式:

id序列较随机: 47682，24086，124576，123457，162422 .
HandtLer_read_rnd: 0 (没有批量读取)
HandLer_read_next: 14 (较少的索引扫描)

这个结果实际上证明了MRR的工作原理:

当MRR开启时:
系统会先收集索引记录
对这些记录进行排序
然后按照主键顺序进行回表查询
这就解释了为什么我们看到更有序的ID序列

当MRR关闭时:

系统直接按照索引顺序访问记录
导致更随机的访问模式

这解释了为什么我们看到更混乱的ID序列

也可以在 explain 中确认 MRR 的使用情





## 第 166 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqtL> show create tabte orders_mrr_test\G;
太太大大亚太天大赤赤大大天太太赤灾大大赤赤六赤 “全 。 下ONW 去赤大夫天太太天太太天大赤赤灾大天天灵赤
Tabte: orders_mrr_test
Create TabLe: CREATE TABLE“`orders_mrr_test`”(
`id ”int NOT NULL AUTO_INCREMENT ，
“user_id ”int DEFAULT NULL，
"order_date`”date DEFAULT NULL，
“amount ”decimatL(10,2) DEFAULT NULL，
`status”varchar(20) DEFAULT NULL，
“product_id ”int DEFAULT NULL，
“quantity” int DEFAULT NULL，
“shipping_address”text，
“customer_name ”varchar(100) DEFAULT NULL，
“customer_emait ”varchar(100) DEFAULT NULL，

)              -_
1 row in set (0.00 sec)

ERROR:
No query specified

mysqt> EXPLAIN SELECT /x+ MRR(o) */ o.id，o.shipping_address，o.customer_name，o.amount FROM orders_m

rr_test 0 FORCE INDEX(idx_user_date) WHERE o.user_id BETWEEN 100 AND 500 AND o.order_date BETWEEN “20
23-03-01' AND “2023-06-0

---+        +-                          +
| id | setect_type | tabte | partitions | type | possibte_keys | key       | key_ten | ref 1

ws | fiLtered | Extra                  |
-+--
+

ranqe | idx_user_date | idx_user_date | 9     | NULL |

0
Using index condition; Using MRR

memo: 2025年4月6日修改至此，今天帮球友修改简历的时候，看到有球友写技术派到简历上，很不错，推荐
给大家。

项目经历                                                                         vv

开发者技术社区 - 地址 : http:/Ipaiww       =有HE (没有备案域名用内网穿透,首次访问较慢)                    2024年09月 - 2025年01月
技术栈: Spring Boot、Mybatis-Pum 。 由。 呈。 1dis、ElasticSearch、RabbitMQ、Docker

项目描述:“开发者技术社区" 是一个          里。 员，帮助开发者成长的内容分享平台。

责任描述: 作为核心研发人员，

核心技术:

=载情况下的最大响应时间降低 33% 。

。 将用户相条中-用了本IF

”通过缓存43二 本                      过示，使系统的平均响应速度提升了 20% 。

e 基于 Thre"qg mr" “下                ”用户    的数据库查询次数 。

ee 通过 AOP                                           、监控和诊断 。

ee 针对热点于                    中长从1000ms 提升至700ms，QPS 提升 25% 。

。 通过分析和了1村二9    吧朋      和      尼。 提升了系统的响应性能 。

e 使用Com 吃           4 分类信息由串行调用改造为并行加载，响应时间从 1s 降低至 0.2s 。
。

采用 自旋居2 "性 PTR 直人和 岂扩 . 思 -国卫癌进行同步，防止其失效时导致的缓存击穿 。

48.二联合索引了解吗? (补充)

No. 166 1 302




## 第 167 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

2024年11 月 22 日增补

联合索引就是把多个字段放在一个索引里，但必须遵守“最左前"原则，只有从第一个字段开始连续使用，索引才
会生效。

回面器面折
一 人
四     a     0         罗     多     四
1       As               ~
/          ~                                                wa
/                                                 和
|                、                                                    es
                  二                                                      es
EE9 -一司| |。         而| = |二| =
本| 雪| = |王| *         地| 半|切|四
1
Eee |这| m|朗|         于| s |王| 。
md oa mwlowa       valowal mmal oa
TAFE]          Se]
人                吉

联合索引会按字段顺序构建B+树。例如 (age，name) 索引会先按照 age 排序，age 相同则按照 name 排序，若
两者都相同则按主键排序，确保叶子节点无重复索引项。

创建 (A,B,c) 联合索引相当于同时创建了 (A) 、 (av,B) 和 (R,B,c) 三个索引。

-- 创建联合索引

CRERTE INDEX idx_order_user_product ON orders(user_id，product_id，create_time)

-- 高效查询

SELECT * FROM orders

WHERE user_id=1001 RND product_id=2002
ORDER BY create time DESC

联合索引底层的存储结构是怎样的?
联合索引在底层采用 B+ 树结构进行存储，这一点与单列索引相同。

No. 1671 302





## 第 168 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

与单列索引不同的是，联合索引的每个节点会存储所有索引列的值，而不仅仅是第一列的值。例如，对于联合索引
(avbvc) ，每个节点都包含a、b、< 三列的值。

非叶子节点示例:
[(a=1，b=2，c=3) ”子节点1，(a=5，b=3，c=1) ”子节点2]

叶子节点示例 (InnopB) ::

(a=1，b=2，c=3) ”PK=100 | (a=1，b=2，c=4) - PK=101
(通过指针连接形成双向链表)

联合索引的叶子节点存的什么内容?

联合索引属于非聚复索引，叶子节点存储的是联合索引各列的值和对应行的主键值，而不是完整的数据行。查询非
索引字段时，需要通过主键值回表到聚簇索引获取完整数据。

No. 168 1 302




## 第 169 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

磁盘块1/根节点

例如索引 (a，b) 的叶子节点会完整存储 (a，b) 的值，并按字段顺序排序 (如 a 优先，a 相同则按 b 排序) 。如
果主键是id，叶子节点会存储 (a，b，id) 的组合。

1. java 面试指南 (付费) 收录的百度同学 4 面试原题: 联合索引底层存储结构(和其他种类的索引存储结
构有什么区别?联合索引的叶子节点存的什么内容?

memo: 2025 年 04 月 07 日增补至此，今天有球友反馈说，加了二哥的星球，简历上写了技术派的项目后，拿到
了腾讯天美的 offer，真的太强了。

No. 1691302




## 第 170 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥您好，我的背景是 26 届本硕华科的 =皇呈”目前在准备暑期实习和
秋招，岗位都是后端，通过朋友推荐加入并学习了您的技术派项目，进行
了相关魔改应用，也是在暑期实习阶段拿到了几个 offer，因此特别感谢
二哥和您团队的付出，从您的星球中学到了很多，后续秋招也会持续关注
您的星球。

但是目前我本人的情况是: 暑期实习想去大三如BAT，秋招想["L .本
展，更偏向于“略时:1 ”二 征习对稳定，想问问二哥关于暑期实习如何选
择:

1. 腾讯天美后台开发base深圳，做的是具体射击游戏业务而不是中人台，

个人比较喜欢游戏所以投了ieg天美也是顺利oc 了，比较想去，但是也有
点担心如果不能转正的话，游戏业务和普通后端业务存在一定差距，不太
好找其他公司，个人打算是深挖公司文档转化为自己的知识能力，因为二
面的leader强调网络并发编程这一块，不知道可不可行

49.二覆盖索引了解吗?
覆盖索引指的是: 查询所需的字段全部都在索引中，不需要回表，从索引页就能直接返回结果。

[TREEEETED

辐 区CEEEEEEO        本本而面面面面面|                |
加
1                        人         NU
owzJ [FREERTTTT              oaJ REALREGTR

NS

 |回国

昌

| 过
[se可
本

Fi国国|一昌国国图国 WEEEE |国国国

empname 和job 两个字段是一个联合索引，而查询也恰好是这两个字段，这时候单次查询就可以达到有目
的，不需要回表。

可以将高频查询的字段 (如 WHERE 条件和 SELECT 列) 组合为联合索引，实现覆盖索引。
例如:

CRERTE INDEX idx_empname_job ON employeelempname，job);

这样查询的时候就可以走索引:

No. 1701302




## 第 171 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

SELECT empname，job FROM employee WHERE empname = '王二， AND job = “程序员'

普通索引只用于加速查询条件的匹配，而覆盖索引还能直接提供查询结果。

一个表 (name, sex,age,id) ，select age,id,name from tblname where
name='paicoding';怎么建索引

由于查询条件有 name 字段，所以最少应该为 name 字段添加一个索引。、
CRERTE INDEX idx_name ON tblname(name)

查询结果中还需要 age 、 id 字段，可以为这三个字段创建一个联合索引，利用覆盖索引，直接从索引中获取数
据，减少回表。

CRERTE INDEX idx_name_age _iqd ON tblname (name，age，id);

1. Java 面试指南 (付费)_收录的作业帮有面经同学 1 java 后端一面面试原题: 了解覆盖索引吗
2. java 面试指南 (付费) 收录的美团同学 9 一面面试原题: 覆盖索引，回表?
3. Java 面试指南 (付费) 收录的字节跳动面经同学 13 java 后端二面面试原题: 一个表 (name，

sexiage'id) ，select age,id,name from tblname where name='paicoding';怎么建索引

50.二什么是最左前缀原则?
最左前组原则指的是: MySQL 使用联合索引时，必须从最左边的字段开始匹配，才能命中索引。
假设有一个联合索引 (a，B，C) ，其生效条件如下:

No. 1711 302




## 第 172 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

查询条件                                      是否触发索引?         说明

WHEREA=1                     区是           使用索引的第一列
WHEREA=1ANDB=2             图是           使用索引的前两列
WHEREA=1ANDB=2ANDC=3       区是           使用索引的全部列

WHEREB = 2                    愉否           跳过左侧列 A，索引失效
WHEREB =2ANDC=3             X尺否           无左侧列，索引失效
WHEREA=1ANDC=3             种部分生效       仅用A列，C 列无法利用索引优化
WHEREA=1                    图是           使用索引的第一列
WHEREA=1ANDB=2              Y 园           使用索引的前两列
WHEREA=1ANDB=2ANDC=3      图是           使用索引全部列 (最理想情况)
WHEREB = 2                    愉否           跳过左侧列 A，索引失效
WHEREB=2ANDC=3             愉否           无左侧列，索引失效
WHEREA=1ANDC=3             惩 部分生效       仅用A列，C 列无法利用索引优化

如果排序或分组的列是最左前缀的一部分，索引还可以加速操作。

SOL
-- 索引(arb)
SELECT * FROM table WHERE a = 1 ORDER BY b; -- 可以利用索引排序
范围查询后的列还能用索引吗?
范围查询只能应用于最左前缀的最后一列。范围查询之后的列无法使用索引。
SOL
-- 索引(abyc)

SELECT * FROM table WHERE a = 1 RND b > 2 RND c = 37
-- 只能使用a和b，c无法使用索引

为什么不从最左开始查，就无法匹配呢?
一句话回答:

因为联合索引在 B+ 树中是按照最左字段优先排序构建的，如果跳过最左字段，MySQL 无法判断查找范围从哪里
开始，自然也就无法使用索引。

No. 172 1 302




## 第 173 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

(Cname,age) 组合索引

(张三，20) 。〈张三，30) 。〈李四，18) (地四,，36) 全   〈王五，10) 。《〈王五，28)

ID:5                       ID:8                       ID:9                      ID:10                                       ID:66                     ID:68

比如有一个 user 表，我们给 name 和 age 建立了一个联合索引 (name，age) 。
RLTER TARBLE user add INDEX comidx_name_phone (namevage) 1

联合索引在 B+ 树中按照从左到右的顺序依次建立搜索树，name 在左，age 在右。

当我们使用 where name=“'王二，and age = “20" 去查询的时候， B+ 树会优先比较 name 来确定下一步应该
搜索的方向，往左还是往右。

如果 name 相同的时候再比较 age。

但如果查询条件没有 name，就不知道应该怎么查了，因为 name 是 B+树中的前置条件，没有 name，索引就派
不上用场了。

联合索引 (a, b)，where a= 1 和 where b = 1，效果是一样的吗

不一样。

WHERE a = 1 能命中联合索引，因为 a 是联合索引的第一个字段，符合最左前组匹配原则。而 waERE b = 1 无
法命中联合索引，因为缺少 a 的匹配条件，MySQL 会全表扫描。

--- 这部分是帮助大家理解 start，面试中可不背 ----
我们来验证一下，假设有一个 ab 表，建立了联合索引 (a，b) :
CRERTE TARBLE ab (
a INT，
b INT，

INDEX ab_index (a，b)
)

插入数据:

INSERT INTO ab (a，b) VRLUES (1，2)，(1，3)，(2，1)，(3，3)，(2，2)7

No. 1731302




## 第 174 页


面渣逆效MySQL篇V2-让天下所有的面潮都能

mysqt> EXPLAIN SELECT *x FROM ab WHERE a = 1NG;        mysqL> EXPLAIN
天上上天“全 。 下OW 太夫守上宙灾着庆庆宙
炎炎                                     大雪大太夫

id: 1                               id:
setect_type: SIMPLE                        setect_type
tabte: ab                               tabte:
partitions: NULL                          partitions:
type: ref                           type: 1

possibte_keys: ab_index                       possibte_keys:
key: ab_index                    key:

key_ten: 5                    key_len

ref: const                    ref

rows: 2                      rows

100.00                                 fittered

: Using index                  Extra

SELECT * FROM ab WHERE b = 1NG;

太太赤南灾太页 全 。 三ON 六页直下太坟丰灾直赤灾页

工
SIMPLE

Using wherei Using index

，1 warning (9.00 sec)                1 row in set，1
通过 explain 可以看到， waERE a = 1 使用了联合索引，而 WHERE b =
一- 这部分是帮助大家理解 end，面试中可不背 -…-
假如有联合索引 abc，下面的 sql 怎么走的联合索引?

二    aa=2
二    b = 2
二  七  a> 2

第一条 SQL 语句包含条件 a = 2 和 b = 2，刚好符合联合索引的前两列。

mySqL> expLatn SelLect x from abc where a =

火火火火火火火火火火火火火火火火火火火火火大火火火火炎 1. FOW 大大大大大
tid: 工
seLect_type: SIMPLE
tabtLe: abc
partitions: NULL
type: ref
possibtLe_keys: abc_index

key: abc_index
key_ten: 10
ref: const ,const
rows: 1
fiLtered: 100.00
Extra: Using index
1 row in set，1 warning (0.00 sec)

第二条 SQL 语句由于未使用最左前中的 a，会触发全表扫描。

No. 174 1 302

warning (9.03 sec)

1 需要全表扫描，依次检查每一行。

2 and b=2 NG;

痰大大火大火火火火火火火火火火炎大大大大大大





## 第 175 页


mysqL> exptLain seLect * from abc where b =
痰火火火火大火火火火火大火火大火火火炎火炎大火炎火火大  1
id :
SeLect_type:
tabte :
partitions :
type:
possibLe_keys :
key :

key_Len:

ref :

rows :
fiLtered :
EXxtral

1 row in set，

第三条 SQL 语句在范围条件 a > 2 之后

MySQL篇V2-让天下所有的面

1

SIMPLE
abc

NULL
index
abc_index
abc_index
15

NULL

10

10.00

Using where; Using index
1 warning (0.01 sec)

索引后会停止匹配，b = 2 的条件需

2 and c=2 NG;
Fow  痰火大火火火火火火火火火火火火火火火大火火火炎火炎大

要额外过滤。

mysqtL> explLain setLect * from abc where a > 2 and b=2 \G;

痰大火火火火大火火火火火火火火火大火大火大火火大火大大
id :
SeLect_type :
tabltLe:
partitions :
type :
possibLe_keys :
key :

key_tLen:

ref :

rows :
fiLtered :
Extra:

1 row in set，

1

SIMPLE
abc

NULL
range
abc_index
abc_index
5

NULL

9

10.00

Using where; Using index
1 warning (0.00 sec)

六OW 大火炎火炎大火火火火火火火火火火火火火大火火火火大火大

(A,B,C) 联合索引 select * from tbn where a=? and b in (?,?) and c>?

走索引吗?

这个查询会命中联合索引，

则。

1. 对于 a=? : 这是一个精确匹配，并且是联合索引
属于多值匹配，并且是联合索引的第

2. 对于b IN (?，?)
引。

. 对于 c>? : 这是

因为 a 是等值匹配，b 是 IN 等值多匹配,5是 b 之后的范

价于 b=? OR b=?，

No. 1751302

索引。
个字段，所以也会命





## 第 176 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

部分是帮助大家理解 start，面试中可不背

来验证一下。
第一步，建表。

CRERTE TRABILE

第二步，创建索引。

CRERTE INDEX

第三步，插入数据。

mysqL> EXPLAIN SELECT *x FROM tbn WHERE A=1 AND B IN (2，3) AND C>3NOG

天火火火炎火炎火炎大火火火炎火火火大大火火克炎火火火炎一人 。 三OW 大火炎火炎火火炎天天火火炎大火火火炎火火炎大大火火类大

id :
SeLect_type:
tabltLe:
partitions :
type :
possibtLe_keys:

key :
key_tLen:
ref :

rows :
fiLtered :
Extral:

七bn

idx_abc ON tbn

(R INT，B INT，C INT，D TEXT

(AR，B，C) 7

3， "First') 7
4， "Second') 1

UES        "Thirad' ) 7
UES  2，3， "Fourth' ) 7
UES (2，3，4， "Fifth' ) 7

WHERE R=1 RND B IN

1
SIMPLE
tbn
NULL
range
idx_abc
idx_abc
15

NULL

2
100.00
Using index condition

1 row in set，1 warning (0.00 sec)

)

(2

3) RN

WD C>3\G

从 ExPLRIN 输出结果来看，我们可以得到 MySQL 是如何执行查询的一些关键信息:
。 type: 查询类型，这里是 range ，表示 MySQL 使用了范围查找，这是因为查询条件包含了 > 操作符。

。 possible_keys: 可能被用来执行查询的索引，              表示 MySQL 认为 idqx_abc 索引会用于查
询优化。
。 key: 实际用来执行查询的索引，

这里是 idqx_abc ,

这确定这条查询命中了联合索引。

也是 idqx_abc ，

No. 176 1 302




## 第 177 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

。 Extra: 提供了关于查询执行的额外信息。 using index condition 表示 MySQL 使用了索引下推 (Index
Condition Pushdown，ICP) ，这是 MySQL 的一个优化方式，它允许在索引层面过滤数据。

-- 这部分是帮助大家理解 and，面试中可不背 ---

联合索引的一个场景题: (a,b,c)联合索引，(b,c)是否会走索引吗?
2024年 04 月 06 日增补

根据最左前妇原则，(b,c) 查询不会走索引。

因为联合索引 (a,b,c) 中，a 是最左边的列，联合索引在创建索引树的时候需要先有 a，然后才会有 b 和 c。而查询
条件中没有包含 a，所以 MySQL 无法利用这个索引。

炎       tbn        B=1      C=1

mysqL> EXPLAIN SELECT * FROM tbn WHERE B=1 AND C=1NG
火火火火大火火火火火火火火火火火火火大火火火火火火火大 人 。 让OW 大大大火火炎大大火火火大火火火炎大火火炎大大大火大火大
id: 1
SeLect_type: SIMPLE
tabLe: tbn
partitions: NULL
type: ALL
possibLe_keys: NULL

key: NULL
key_Len: NULL
ref: NULL

rows: 5
fiLtered: 20.00
Extra: Using where
1 row in set，1 warning (0.00 sec)

建立联合索引(a,b,c)，where c = 5 是否会用到索引? 为什么?
2024年 04 月 08 日增补

不会。只有索引的第三列 c 被用作查询条件，而前两列 3 和 b 都没有被使用。这不符合最左前缀原则。

炎          tbn            C=5

No. 1771302




## 第 178 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

mysqL> EXPLAIN SELECT # FROM tbn WHERE C=5NG
来沙沙水冰冰冰冰沙沙炒沙冰冰沙阔炒阔冰冰冰冰炒阔六阔炒“荆。 和OW， 炒阔沙阔沙冰冰冰六炒水玉冰阔阔炒冰冰冰冰冰冰冰冰冰冰水
id: 1
SelLect_type: SIMPLE
tabLe: tbn
partitions: NULL
type: ALL
possibtLe_keys: NULL
key: NULL
key_tLen: NULL
ref: NULL
rows: 5
filLtered: 20.00
Extra: Using where
1 row in set，1 warning (0.00 sec)

sql中使用like，如果遵循最左前缀匹配，查询是不是一定会用到索引?
2024年11 月 04 日增补

如果查询模式是邱通配符 LIKE “prefixs' ，且该字段有索引，优化器通常会使用索引。否则即便是遵循最左
前缀匹配，LIKE 字段也无法命中索引 。

如 age = 18 and name LIKE 'sxxx' ，MySQL 会先使用联合索引 age_name 找到 age 符合条件的所有行，然
后再全表扫描进行 name 字段的过滤。

No. 178 1 302




## 第 179 页


MySQL篇V2-让天下所有的面渣都能

mysqL> SELECT * FROM test_tabtLe WHERE age = 18 AND name LIKE 's%王二1

1 row in set (0.00 sec)

mysqL> EXPLAIN SELECT * FROM test_tabLe WHERE age = 18 AND name LIKE
二1' NG;
xxx 全.。 FOW 大大大大大大大大大火火火大大大大大大火炎大大大大大大大
id: 1
SelLect_type: SIMPLE
tabtLe: test_tabltLe
partitions: NULL
type: ref
possibte_keys: age_name
key: age_name
key_tLen: 5
ref: const
rows: 3
fiLtered: 16.67
Extra: Using where; Using index
1 row in set，1 warning (0.00 sec)

TN2ERT、 INTO test_tablLe (age，name) VALUES
沉默王二1 )，
沉默
沉默
见默了
沉默
'沉默了
Query 0K， 6 rows affected (0.01 sec)
Records: 6 DupLicates: 0 Warnings: 0

甬配符，如 age = 18 and name LIKE    s' ，MySQL 会直接使用联合索引 age_name 找到所有符





## 第 180 页


面渣逆效MySQL篇V2-让天下所有的面潮都能

mysqL> SELECT x FROM test_tabtLe WHERE age = 18 AND name LIKE “'江岂蝎
+----+------+-----------
| id | age

3 rows in set (0.00 sec)

mysqL> EXPLAIN SELECT * FROM test_tabLe WHERE age = 18 AND name LIKE
痰大火火火火火大火火大火火火火火火大火大火火火大火大火 人 。 三OW 大火炎大火大火火火炎火炎大火大火火火大火火火火火炎火炎
id: 1
SelLect_type: SIMPLE
tabLe: test_tabltLe
partitions: NULL
type: range
possibtLe_keys: age_name
key: age_name
key_Len: 208
ref: NULL
rows: 3
fiLtered: 100.00
Extra: Using where; Using index
1 row in set，1 warning (0.00 sec)

type 为 range，表示 MySQL 使用了索引范围扫描， filtered 为 100.00s ，表示在扫描的行中，所有的行都满
足 WHERE 条件。

引 select * from tbn

2                的京东同学 10 后端实习一面的原题: 联合索引 abc，

a=1,c=1/b=1,c=1/a=1,cC=1,b=1 走不走索引

面丝     7 java 后端技术一
|

(ab,c)联合索:

Where C=5 和

设计原则

9                                 收录

和 where b = 1，效果是一样

10.              收录

贝壳找房后端技术

下面怎么走的

No. 1801 302




## 第 181 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

11. java 面试指南 (付费) 收录的滴滴面经同学 3 网约车后端开发一面原题: 联合索引 (a, b, 0，where b
=1，能走吗，where a = 1，能走吗

51.过什么是索引下推?

索引下推是指: MySQL 把 WHERE 条件尽可能“下推"到索引扫描阶段，在存储引擎层提前过滤掉不符合条件的记
录。

回表

(name，age) 组合索引                                           主键索引

name

张狗3

张狗6
张狗7

索引下推

(name，age) 组合索引                                           主键索引

name

张狗3

张狗6
张狗7

sq| 要求的 age = 38 ，张狗6 不符合，
索引下推排除掉，不再执行回表

当查询条件包含索引列但未完全匹配时，ICP 会在存储引擎层过滤非索引列条件，以减少回表次数。

传统的查询流程是，储引擎通过联合索引定位到符合最左前缀条件的主键 ID; 回表读取完整数据行并返回给
Server 层; Server 层对所有返回的行进行 WHERE 条件过滤。

有了 ICP 后，存储引擎在索引层直接过滤可下推的条件，仅对符合索引条件的记录回表读取数据，再返回给
Server 层进行剩余条件过滤。

No. 1811302




## 第 182 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-一这部分是帮助大家理解 start，面试中可不背 -一

例如有一张 user 表，建了一个联合索引 (name, age) ，查询语句: select * from user where name 1ike
'张sand age=10; ，没有索引下推优化的情况下:

MySQL 会使用索引 name 找到所有 name 1like “'张s， 的主键，根据这些主键，一条条回表查询整行数据，并在
Server 层过滤掉不符合 age=10 的数据行。

没有使用ICP

SefVet

id name “age “phome address

人

4      张猛     16     1666 。 深坊洞
十
|
age like '张%'and age=10
yy
(aameaga)                         存储引澡                        (潜入索引)          GCp2
name      age        id
张三        10         1
张猛        16         4
李四        12         2
玉五        10         3

启用 ICP 后，InnoD8B 会通过联合索引直接筛选出符合条件的主键ID (name like “'张sand age=10) ，然后
再回表查询整行数据。

No. 182 1 302




## 第 183 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

使用ICP
SefVet
ame age phone address
人
|                         |                                                                                        多
name Hike and age=10 乡

换句话说，假设 name like “'张%s， 找到 10000 行数据，age=10 只有其中 10 行，没有索引下推的情况下，
MySQL会回表 10000 次，读取 10000 行数据，然后在 Server 层过滤掉 9990 行。

而有了索引下推后，MySQL 只会回表 10 次，读取 10 行数据。
我们来验证一下。

No. 183 1302




## 第 184 页


L篇V2-让天下所有的面渣都

全 剧 工L1
SsHow VARIABLES LIK    s%Ccondition_pushdowns ' ;

-- 确保ICP开启
SET optimizer_switch='index_condition_pushdown=on ' ;

-- 使用EXPLAIN分析带有ICP的查询
EXPLAIN

SELECT x FROM orders_mrr_test
WHERE user_id > 100

AND user_id < 200

AND order_date LIKE '2023-01s5 ' ;

-- 关闭ICP再次分析

SET optimizer_switch='index_condition_pushdown=off ' ;
SELECT “With ICP OFF' as test_case;

EXPLAIN

SELECT x* FROM orders_mrr_test

WHERE user_id > 100

AND user_id < 200

AND order_date LIKE '2023-01s5 ' ;

-- 重新开启ICP

SET optimizer_switch='index_condition_pushdown=on ' ;
SELECT 'With ICP ON' as test_case;

EXPLAIN FORMAT=TREE

SELECT x FROM orders_mrr_test

WHERE user_id > 100

AND user_id < 200

AND order _ date LIKE '2023-01s5 ' ;”"

从结果中我们可以清楚地看到 ICP 的效果。ICP 开启时，Extra 列显示"Using index condition"，表有
下推到存储引擎层。

1ICP关闭时，Extra 列仅显示"Using where"，表明过滤条件在服务器层执行。





## 第 185 页


en | ref | rows | fittered | Extr

1 1 SIMPLE    1 orders_mrr_test | NULL     1 range | tdx_user_date     user_date | 5     | MULL | 34738 | 。 11.11 | Ustng tndex condttton |

WEth ICP OFF

ten | ref | rows | fittered | Extra

| NULL     1 range | idx_user_date                 1 AULL 1

x condition: ((orders_mrr_test.user_id > 199) and (ordei

-- 开启ICP

SET optimizer_switch:

'index_condition pushdown=on' 7

-- 清理状态
FLUSH STRTUS)

SELECT 'Performance test with ICP ON'， as test_casei
-- 执行查询并分析性能
EXPLRIN RNRLYZE
SELECT /x+ ICP_ON */ 办
FROM orders_mrr_test
WHERE user_iqd BETWEEN 100 RND 200
RND order_date >= '2023-01-01'
RND order_date < '2023-02-01'
RND order_date NOT LIKE '2023-01-158 "7

- 显示处理器状态
SHOW STATUS LIKE 'Handler_reads' 1?

-- 关闭ICP
SET optimizer_switch='index_condition pushdown=off

-- 清理状态
FLUSH STRTUS)

SELECT 'Performance test with ICP OFF'， as test_casey
-- 执行相同的查询
EXPLRIN RNRLYZE
SELECT *
FROM orders_mrr_test
WHERE user_iqd BETWEEN 100 RND 200
RND order_date >= '2023-01-01'
RND order_date < '2023-02-01'
RND order_date NOT LIKE '2023-01-158 "7

No. 1851302




## 第 186 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

实际的性能差距也很大。ICP 开启时，实际扫描行数: 1,649 行，执行时间: 约12.3 毫秒。
数: 19,959 行，执行时间: 约 32.1 毫秒。

关闭时，实际扫描行

--- 这部分是帮助大家理解 start，面试中可不背 ----

党

1. Java 面试指南 (付费) 收录的美团同学 9 一面面试原题: 索引

52.如何查看是否用到了索引? (补充)

2024年 03 月 15 日增补。

\推

可以通过 EXPLAIN 关键字来查看是否使用了索引。

EXPLRAIN SELECT * FROM table WHERE column        ?

如果使用了索引，结果中的 key 值会显示索引的名称。

mysqL> exptLain seLect * from students where id =9\G
火火火火火火火大火火火火火火大大火火火大火火炎大火炎大 人 。 三OW 大火炎大大大火炎大火火火火火火火炎大火炎大火火大大火炎
id: 1
SeLect_type: SIMPLE
tabLe: students
partitions: NULL

type:
possibtLe_keys :

key :
key_tLen:
ref :

rows :
fiLtered :
Extral:

Const
PRIMARY
PRIMARY
4

Const

1
100.00
NULL

1 row in set，1 warning (0.00 sec)

联合索引 abc，a=1,c=1/b=1,c=1/a=1,c=1,b=1 走不走索引?
2024年 03 月 19 日增补

ac 能用上索引，条件 a=1 符合最左前缀原则，触发索引的第一列 a; 由于跳过了中间列 b，c=1 无法直接利用索引
的有序性优化，但可通过索引下推在存储引擎层过滤 c 的条件，减少回表次数。

No. 186 1 302




## 第 187 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

bc 无法使用索引，只能全表扫描，因为不符合最左前缀原则;acb 虽然顺序是乱的，但 MySQL 优化器会自动重排
为 abc，所以能命中索引。

这部分是帮助大家理解 start，面试中可不背
我们通过实际的 SQL 来验证一下。
示例1 (a=1,c=1) :

炎       tbn        R=1      C=1

mySsqL> EXPLAIN SELECT x FROM tbn WHERE A=1 AND C=1NG
火炎火火火火火火火火火火火火大火火火火火火炎火炎火火在。 广OW 大大火火火火炎大火火火火火火大火火火火炎火炎火炎火炎大
tid: 1
SeLect_type: SIMPLE
tabtLe: tbn
partitions: NULL
type: ref

possibLe_keys: idx_abc
idx_abc
5

: Const
: 3
fiLtered: 20.00
Extra: Using index condition
1 row in set，1 warning (0.00 sec)

key 是 idx_abc，表明 a=1,c=1 会使用联合索引。 Extra: Using index condition 表示 ICP 生效。

示例 2 (b=1c=1) :

炎       tbn        B=1      C=1

No. 1871 302




## 第 188 页


L篇V2-让天下所有的面渣都能逆袭

mysqL> EXPLAIN SELECT * FROM tbn WHERE B=1 AND C=1NG
炎炎炎炎火炎火炎火炎火炎炎炎天火火炎火炎炎炎火火炎火炎全 。 三OW 大大大炎炎火炎火炎大火炎炎炎火炎火炎炎炎火炎炎炎大火大

tid: 1
SelLect_type: SIMPLE
tabtLe: tbn
partitions: NULL
type: ALL
possibtLe_keys: NULL
key: NULL
key_Len: NULL
ref: NULL
rows: 5
fiLtered: 20.00
Extra: Using where
1 row in set，1 warning (0.00 sec)

key 是 NULL，表明 b=1,c=1 不会使用联合索引。这      询条件没有遵循最左前

示例3 (a=1,c=1b=1) :
EXPLRAIN SELECT * FROM tbn WHERE R=1 RND C=1 RND B=1NG

优化器会自动调整条件顺序为 a=1 AND b=1 AND c=1。

mysqL> EXPLAIN SELECT x* FROM tbn WHERE A=1 AND C=1 AND B=1NG

痰火火火火火火大火炎大火火火火火火火火大大火大火火火炎 人 。 三OW 大火火火炎火炎火炎大火火火火火火火大大大大大火火火火类

id: 1
SeLect_type: SIMPLE
tabte: tbn
partitions: NULL
type: ref
possibLe_keys: idx_abc
key: idx_abc
key_Len: 15
ref: const,const,const
rows: 1
fiLtered: 100.00
Extra: NULL
1 row in set，1 warning (0.00 sec )

key 是 idx_abc，表明 a=1,c=1,b=1 会使用联合索引。

并且 rows=1，因为 MySQL 优化器会自动重排查询条件，以满足最左前缓原则，直接使用联合索引找出 a=1 AND
b=1 AND c=l 的行。

，拿到了鹅广和美团的暑期实习 offer，并且都已经 0C，





## 第 189 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

哈唆二哥，暑期目前拿了两个 offer，想看看能不
能听听你的建议，星球编号噶. 一，之前有找二
哥改过简历~

2140 国              划合四

<嘿-
暑期实习腾讯vs美团

节前还在痛苦面试进度条卡着不动，结果
今天突然来了两个offer砸脸上了，之前基

本上一直是Java相关的技术檬，求大佬帮
忙分析下去哪家会好一点orz。

1. 腾讯是CDG有圈讯广告的数据工程，主
Java数据开发相关的技术栈，主要是toB的
数据归因建模等 (下午先来的offer已经接
了,如果尝的话秋招会被拉黑吗)

2. 美国是广告引擎开发，主cpp副Java都
有，有toC场景，可能技术挑战和业务场景
吸引力会更大一些

base都在北京，薪资和背书感觉也都差不

多，需要学的也都挺多的，主要从转正以
及未来发展这两方面考虑。

09:06

锁

53.恰MySQL 中有哪几种锁?
MySQL 中有多种类型的锁，可以从不同维度来分类，按锁粒度划分的话，有表锁、行锁。
按照加锁机制划分的话，有乐观锁和悲观锁。按照兼容性划分的话，有共享锁和排他锁。

No. 189 1 302




## 第 190 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

间障锁

排他锁                                                                                                          next-key锁

-一这部分是帮助大家理解 start，面试中可不背 -一

表锁: 锁定整个表，资源开销小，加锁快，但并发度低，不会出现死锁; 适合查询为主、少量更新的场景 (如
MylISAM 引擎) 。

用户A                                   用户B                                                    NySQL

开始事务

SELECT * FRON table1 加读锁

基
ALTER TABLE table1 被阻塞
拓
提交事务
拓
执行ALTER
押
用户A                           用户B                                        NMySQL

再细分的话，有表共享读锁 (S锁) : 允许多个事务同时读，但阻塞写操作; 表独占写锁 (X锁) : 独占表，阻塞其
他事务的读写。

No. 1901302




## 第 191 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Lock Type CompatibiLity Matrix

行锁: 锁定单行或多行，开销大、加锁慢，可能出现死锁，但并发度高 (InnoDB 默认支持) 。

再细分的话，有记录锁 (Record Lock) : 锁定索引中的具体记录; 间隙锁 (Gap Lock) : 锁定索引记录之间的间
隙，防止幻读; 临键锁 (Next-Key Lock) : 结合记录锁和间隙锁，锁定一个左开右闭的区间 (如 (5，10]1) 。

共享锁 (S锁/读锁) ，多许多个事务同时读取数据，但阻塞写操作。语法: SELECT ..。 LOCK IN SHARE MODE
排他锁 (X锁/写锁) ，独占数据，阻塞其他事务的读写。语法: SELECT ..。 FOR UPDRTE 。

乐观锁假设冲突少，通过版本号或 CAs 机制检测冲突 (如 UPDRaTE SET version=version+1 WHERE

version=old_version ) 。

悲观锁假设并发冲突频繁，先加锁再操作 SELECT FOR UPDRTE 。

-一 这部分是帮助大家理解and，面试中可不背
1. java 面试指南 (付费) 收录的京东同学 4 云实习面试原题: mysql一共有哪些锁
2. java 面试指南 (付费) 收录的美团面经同学 15 点评后端技术面试原题: 问了一下mysql的锁和MVCC
3. java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题: MySQL锁

54.全局锁了解吗? (补充)

2024年07 月 15 日增补。

全局锁就是对整个数据库实例进行加锁，当执行全局锁定操作时，整个数据库将会处于只读状态，所有写操作都会
被阻塞，直到全局锁被释放。

在进行全库备份，或者数据迁移时，可以使用全局锁来保证数据的一致性。
在 MySQL 中，可以使用 FLUSsH TABLES WITH READ LOCK 命令来获取全局锁。
执行该命令后，所有表将被锁定为只读状态。记得在完成备份或迁移后，使用 UNLOcCK TABLES 命令释放全局锁。

No. 1911 302




## 第 192 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-- 锁定整个数据库

FLUSH TABLES WITH RERAD LOCK?

-- 执行备份操作
-- 例如使用 mysqldump 进行备份

! mysqldump -u username -p database_name > backup.sql

-- 释放全局锁定

UNLOCK TARBLES)

表锁了解吗?
了解。

表锁常见于 MylSAM 引擎，InnoDB 也可以手动通过 LocK TABLES 加锁。

Session 1

LOCK TABLES

SELCECT .…

Session 2

适合读多写少、全表扫描或者表结构变更的场景用。
表锁又可以细分为共享锁和排他锁。共享锁允许多个事务同时读表，但不允许写操作。

LOCK TABLES table_name RERD;  -- 显式加读锁
SELECT * FROM table_name)    -- 其他会话可读，不可写
UNLOCK TRBLES              -- 释放锁

排他锁只允许一个事务进行写操作，其他事务不能读也不能写。

LOCK TRBLES table_name WRITE; -- 显式加写锁
INSERT/UPDRTE/DELETE table_name; -- 其他会话读写均阻塞
UNLOCK TRBLES

MyISAM 在执行 SELECT 时会自动加读锁，执行 INSERT/UPDaATE/DELETE 时会加写锁。

对于InnoDB 引擎，无索引的 UPpaTE/DELETE 可能会导致锁升级为表锁。

No. 192 1 302




## 第 193 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

UPDRTE innodb_ table SET name='new” WHERE name='old'); -- 全表扫描，退化为表锁

执行 ALTER TABLE 时会自动加表锁，阻塞所有读写操作。

1. java 面试指南 (付费) 收录的美团面经同学 3 java 后端技术一面面试原题: 数据库中的全局锁 表锁行
级锁 每种锁的应用场景有哪些

2. Java 面试指南 (付费) 收录的同学 30 腾讯音乐面试原题: mysql的表级锁有几种
55.二说说 MySQL 的行锁?
行锁是 InnoDB 存储引擎中最细粒度的锁，它锁定表中的一行记录，人允许其他事务访问表中的其他行。

底层是通过给索引加锁实现的，这就意味着只有通过索引条件检索数据时，InnoDB 才能使用行级锁，否则会退化
为表锁。

二级素引

Alice                 Tony                Yamy

Alice | Bob             Alice | Bob

二级索引的时节点                                                                                         AN
包含主键值                                                                              愉

                    主欠索引

聚艇索引 : 叶节点即
包含主键也有数据行

行锁又可以细分为记录锁、间隙锁和临键锁三种形式。通过 SELECT . . . FOR UPDRTE 可以加排他锁。

No. 1931302




## 第 194 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

STRART TRANSRCTION 7

-- 加排他锁，锁定某一行
SELECT * FROM your_table WHERE id = 1 FOR UPDRATE)
-- 对该行进行操作

UPDRTE your_table SET columnl = 'new_value' WHERE id = 17

CoMMIT;
通过 SELECT ...LOCK IN SHARE MODE 可以加共享锁。

STRART TRANSRCTION 7

-- 加共享锁，锁定某一行
SELECT * FROM your_table WHERE id = 1 LOCK IN SHARE MODE7

-- 只能读取该行，不能修改

COMMIT;

select for update 有什么需要注意的?

第一，必须在事务中使用，否则锁会立即释放。

STRRT TRANSRCTION;
SELECT * FROM your_table WHERE id = 1 FOR UPDRATE)
-- 对该行进行操作

COMMIT;

第二，使用时必须注意是否命中索引，否则可能锁全表。

-- name 没有索引，会退化为表锁

SELECT * FROM user WHERE name = “'王二， FOR UPDRATE)

-一这部分是帮助大家理解 start，面试中可不背 -一
假设有一张名为 orders 的表，包含以下数据:

CRERTE TRBLE orders |(

id INT PRIMRARY KEY，

order_no VRRCHRAR(255) ，

amount DECIMRAL(10,2)，

status VRRCHRAR(50) ，

INDEX (order_no)  -- order_no 上有索引
)

表中的数据是这样的:

No. 1941 302




## 第 195 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

id                    order_no                                   amount                                 Status

1            10001                      50.00                     pending
2                   10002                                   75.00                                pending

3                   10003                                   100.00                               pending

4                  10004                                   150.00                               completed
5            10005                      200.00                    pending

如果我们通过主键索引执行 SELECT FOR UPDaTE ，确实只会锁定特定的行:

STRART TRANSRCTION 7
SELECT * FROM orders WHERE id = 1 FOR UPDRTE)

-- 对 id=1l 的行进行操作

COMMIT
由于 id 是主键，所以只会锁定 id=1 这行，不会影响其他行的操作。其他事务依然可以对 id = 2, 3, 4, 5 等行执行
更新操作，因为它们没有被锁定。
如果使用 order_no 这个普通索引执行 SELECT FOR UPDATE ，也只会锁定特定的行:
STRART TRRNSRACTION 7
SELECT * FROM orders WHERE order_no = "10001” FOR UPDRATE;
-- 对 order_no=10001 的行进行操作
COMMIT
因为 order_no 是唯一索引，所以只会锁定 order_no=10001 这行，不会影响其他行的操作。
但如果 WHERE 条件是 status='pending' ，而 status 上没有索引 :
STRART TRRNSRACTION 7
SELECT * FROM orders WHERE status = “pending' FOR UPDRTE;
-- 对 status=pending 的行进行操作
COMMIT
就会退化为表锁，因为在这种情况下，MySQL 需要全表扫描检查每一行的 status。
--- 这部分是帮助大家理解end，面试中可不背 ----

memo: 2025年4月9 日修改至此，今天有球友反馈说，拿到了美团的暑期实习 offer，并且特意感谢了面渣逆
袭，口碑+1。

No. 1951 302




## 第 196 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

图二哥美团offer也拿到了，感觉这周好幸运，
忆和于也到 HR面了

开完组会就发一下星球，虽然我的面试也算是运

气好，于下同."1
| 二
[|

11:40

SF的AS了，
多亏了二哥的面渣逆袭小

11:46

[| 二
说说记录锁吧?

记录锁是行锁最基本的表现形式，当我们使用唯一索引或者主键索引进行等值查询时，MySQL 会为该记录自动添
加排他锁，禁止其他事务读取或者修改锁定记录。

No. 1961302




## 第 197 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

TABLE: stock(id primary key, sku_id)

SQL: select * from stock where id = 3 for update;

Record Lock (X锁)

ID (到签索引)
记录 “1000001 1000002 1000003 1000004 1000005

TABLE: stock(id primary key, sku_id unique key)

SQL select * from stock where sku_id = 1000003 for update;

Record Lock (X锁)
UL 上二1 1000001|1000002 | 1000003 | 1000004 | 1000005

ID (到簇索引值)      1          2           3           4           5

<
w，
w，
w，

~               Record Lock (X锁)
an EM

记录 1000001 1000002 1000003 1000004 1000005

例如:
SELECT * FROM table WHERE id = 1 FOR UPDRTE; -- 加X锁
UPDRTE table SET name = '王二， WHERE id = 1 -- 隐式加x锁

间障锁了解吗? (补充)
2024年12月15 日增补。

间隙锁用于在范围查询时锁定记录之间的“间隙"，防止其他事务在该范围内插入新记录。仅在可重复读及以上的隔
离级别下生效，主要用于防止幻读。

No. 1971 302




## 第 198 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

Select* from a where c<= 7for update; RR隔离级别，c为普通索引
试想，如果没有Gap lock 3，那么其他session是可以插入7的

Gap lock 1               Gap lock 2              Gap lock 3

loce update 0

如果再次Select * from a where c<=7for update;
那么得到的记录就会多一条，幻读产生
InnoD8B的Gap lock就是用来防止幻读的
---- 这部分是帮助大家理解 start，面试中可不背 ----
例如事务 A 锁定了 (1000,2000) 区间，会阻止事务 B 在此区间插入新记录:
-- 事务A

BEGIN7
SELECT * FROM orders WHERE amount BETWEEN 1000 RND 2000 FOR UPDRTE/

-- 事务B尝试插入会被阻塞
INSERT INTO orders VRLUES(nul1,1500，'pending');  -- 阻塞

假设表 test_gaplock 有 id、age、name 三个字段，其中 id 是主键，age 上有索引，并插入了 4 条数据。

CRERTE TARBLE “test_gaplock` |(
”id int(11) NOT NULL，
”age” int(11) DEFRAULT NULL，
~name” varchar(20) DEFRULT NULL，
了PRIMARY KEY (~id ~)v
KEY age” (age )

) ENGINE=InnoDB》

insert into test_gaplock values(1,1，张三')，(6,6，吴老二')，(8,8，赵四'),(12,12，熊大')7

间隙锁会锁住:

No. 198 1 302




## 第 199 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

。 (-o，1) : 最小记录之前的间阶。
。 (1，6)、(6，8)、(8，12) : 记录之间的间隙。
。 (12，+wm) : 最大记录之后的间隙。

一一一              天-一-一一                          E                                      E                                              人

志
人

吴老二                       赵四                         能大

假设有两个事务，T1 执行以下语句 :

RT 了

SELECT * FROM test_gaplock WHERE age > 5 FOR U

T2 执行以下语句:

test_gaplock VALUES (7，7，     ;

T1 会锁住 (56，8) 的间隙，防止其他事务在这个范围内插入新记录。

T2 在插入 (7，7，“玉五') 时，会被阻塞，可以在另外一个会话中执行 sSHow ENGINE INNODB STATUS 查看到间

TRANSACTIONS
Trx id counter 16726
Purge done for trx's n:0 < 16724 undo n:o < 0 state: running but idte
History List Length 0
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 281480487310792，not started
0 Lock struct(S)，heap size 1128，0 row Lock(Ss)
---TRANSACTION 281480487308416，not started
0 Lock struct(S)，heap size 1128，0 row Lock(S)
---TRANSACTION 281480487307624，not started
0 Lock struct(S)，heap Size 1128，0 row Lock(S)
---TRANSACTION 281480487306832，not started
0 Lock struct(S)，heap Size 1128，0 row Lock(S)
---TRANSACTION 16725，ACTIVE 19 sec inserting
mysqtL tabLes in use 1，Locked 1
LOCK WAIT 2 Lock struct(s)，heap Size 1128，1 row Lock(s)，undo Log entries 1
MySQL thread id 1758，05 thread handtLe 13162229760，query id 521931 LocaLhost root update
INSERT INTO test_gaptLock VALUES (7，7，“王五")
一   --- TRX HAS BEEN WAITING 19 SEC FOR THIS LOCK T0 BE GRANTED :
RECORD LOCKS space id 347 page no 5 n bits 72 index age of tabLe“`itwanger` test_gaptLock
”trx id 16725 Lock_mode X Locks gap before rec insert intention waiting
Record Lock，heap no 4 PHYSICAL RECORD: n_fietds 2; compact format; info bits 0
Len 4; hex 80000008; asc     ;
: Len 4; hex 80000008; asc

推荐阅读: 六个宣

No. 1991302




## 第 200 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

执行什么命令会加上间隙锁?

在可重复读隔离级别下，执行 FOR UPDATE /LOCK IN SHARE MODE 等加锁语句，且查询条件是范围查询时，就
会自动加上间阶锁。

-- SELECT ..。 FOR UPDRATE + 范围查询
SELECT * FROM user WHERE score > 100 FOR UPDRTE;
-- SELECT ..。 LOCK IN SHARE MODE + 范围查询

SELECT * FROM user WHERE id BETNEEN 10 RND 20 LOCK IN SHARE MODE7
-- UPDRATE/DELETE + 范围查询
DELETE FROM user WHERE score < 50)

1. Java 面试指南 (付费) 收录的阿里云面经同学 22 面经: mysql的什么命令会加上间隐

56.临键锁了解吗?

临键锁是记录锁和间隙锁的结合体，锁住的是索引记录和索引记录之间的间隙。

DT gs
人@@ yuex 上 中<          1

next-key |ock
[2  2一           ey

临键锁 = 间隙锁 + 记录锁

和间隙锁不同，临键锁的间阶是一个左开右闭区间。例如 (1,3] 表示锁定大于 1 且小于等于 3 的所有记录。
当InnoDB 执行一个范围查询时，会使用临键锁来锁定满足条件的行数据以及该范围内的间阶。

No. 2001302




## 第 201 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

事务A                                                                            事务B                                                                                                             MySQL

START TRANSACTION

SELECT * FRON students WHERE id >= 1AND id <= 10

START TRANSACTION
INSERT INTO students (id, name) VALUES (7，David)
[es we]                 ]
COMNIT
人
插入成功
事务A                                                             事务B                                                                                       My5QL

比如说下面这条语句会锁定 id 在 5 到 10 之间的所有记录，以及这些记录之间的间阶。
SELECT * FROM table WHERE id BETWEEN 5 AND 10 FOR UPDRTE)

MySQL 默认的行锁类型就是临键锁。当使用唯一索引的等值查询匹配到一条记录时，临键锁会退化成记录锁; 如
果没有匹配到任何记录，会退化成间隙锁

memo: 2025年4月10 日修改至此，今天有
了。

拿到了滴滴的 sp offer，真的无敌啊，太能卷

二哥，来报个喜，滴泣上岸了，双非学院本sp人@ 优

部门还行，哈哈哈人
10:08

太牛了
等一手经验贴分享，发个红包，哈哈
57.意向锁是什么知道吗?

No. 2011 302




## 第 202 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

意向锁是一种表级锁，表示事务打算对表中的某些行数据加锁，但不会直接锁定数据行本身。

由InnoDB 自动管理，当事务需要添加行锁时，会先在表上添加意向锁。这样当要添加表锁的时候，可以通过查看
表上的意向锁，快速判断是否有冲突，而无需逐行检查，从而提高加锁效率。

原来大哥在呢，我等着

事务B
当执行 SELECT .. .LOCK IN SHARE MODE 时，会自动加意向共享锁; 当执行 SELECT ... FOR UPDaTE 时，会
自动加意向排他锁。

意向锁之间互相兼容，也不会与行锁冲突。

兼容关系                    意向共享锁                意向排他锁                共享锁(表级)                 拍他锁(表级)
意向共享锁                 兼容                           兼容                           兼容                              冲突
意向排他锁        兼容            兼容            冲突              冲突
S锁                             兼容                           冲突                           兼容                              冲突
X锁                            冲突                           冲突                           冲突                              冲突

意向锁的意义是什么?

在没有意向锁的情况下，当事务 A 持有某表的行锁时，如果事务 B 想添加表锁，InnoDB 必须检查表中每一行数据
是否被加锁，这种全表扫描的方式效率极低。

No. 2021302




## 第 203 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

用户A             用户B                NMySQL
开始事务
押
更新表部分行，加IX锁
押
尝试对整个表加写锁
押
检测到IlX锁，加写锁失败
坪
提交事务，释放IX锁
押
成功加写锁
押
用户A             用户B                NMySQL

有了意向锁之后，事务在加行锁前，先在表上加对应的意向锁; 其他事务加表锁时，只需检查表上的意向锁，无需
逐行检查。

-- 事务A获取某行的排他锁

BEGIN7

SELECT * FROM users WHERE id = 6 FOR UPDRTE;  -- 自动加IX锁和行x锁

-- 事务B尝试加表锁

LOCK TRBLES users RERD;  -- 发现表上有IX锁，与S锁冲突，直接阻塞而无需扫描全表

memo: 2025年4月11 日修改至此，今天拿到滴滴 offer 的球友反馈，MQ 部分主要看的面渣逆柳，比较全，这
不，口碑就来了。

No. 2031302




## 第 204 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

当时搞完就直接面了A义

MQ八股看的面渣@
有惊无险
口碑来了哈哈。
主要我看的几个八股都是结合起来的
然后MQ八股目前面渣比较全

58.二MySQL的乐观锁和悲观锁了解吗?

碍观锁是一种"先上锁再操作"的保守策略，它假设数据被外界访问时必然会产生冲突，因此在数据处理过程中全程
加锁，保证同一时间只有一个线程可以访问数据。

悲观锁
入

用户2 (事务2)

。 -AQ 入

用户3 (事务3)
用户1 (事务1)

和

用户4 (事务4)

MySQL 中的行锁和表锁都是赤观锁。

No. 2041 302




## 第 205 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

悲观锁
De
和        一

一品

线程加锁成功，执行更新拧作

乐观锁会假设并发操作不会总发生冲突，属于小概率事件，因此不会在读取数据时加锁，而是在提交更新时才检查
数据是否被其他事务修改过。

乐观锁并不是 MySQL 内置的锁机制，而是通过程序逻辑实现的，常见的实现方式有版本号机制和时间戳机制。通
过在表中增加 version 字段或者 timestamp 字段来实现。

-一这部分是帮助大家理解 start，面试中可不背 -一
当事务 A 已经上锁后，事务 B 会一直等竺事务 A 释放锁; 如果事务 A 长时间不释放锁，事务 B 就会报错 Lock

wait timeout exceeded; try restarting transaction 。

No. 2051302




## 第 206 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

及 上

事务B (用户B)           事务A (用户A)
select num                                                                    select num
fromt goods                                                                 fromt_goods
Whereid=2                                                           Whereid=2
forupdate                                                                           forupdate
义
此时id=2已经              id         name                      num
被事务A加锁 ，                                                                             id=:
事务B无法在对                     1 扮扮法式小面包                    1     此
其进行加信         上全       2 臭豆腐                         1       务A加锁

事务A已经给id=2的数据进行了加锁，那么在事务A未解锁之前，事
务B是无法再对其加锁操作

事务 A 和事务 B 同时读取同一个主键 ID 的数据，版本号为 0; 事务 A 将版本号 (version=1) 作为条件进行数据
更新，同时版本号 +1; 事务 B 也将 version=1 作为更新条件，发现版本号不匹配，更新失败。

人

事务B (用户B)

2. 梅num =1andversion =0
作为更新冬件加入到更新语句中

事务A(用|

和

户A)

1 select num from t_goods

whereid=2
获取库存 ( num=1 ) 和版本(version=0)

不 selectnum fomt_goods
Whereid= 2
获取库存 ( num=1 ) 和版本(version=0)

name         num   version
本vson有人     工了有污5而包      1     @
于生计用全芝训因为 放 2 号训          1      @

一- 这部分是帮助大家理解 end，面试中可不背 一
如何通过坊观锁和乐观锁解决库存超卖问题?

碍观锁通过 SELECT ..-

No. 2061302

2. 将num =1andversion =0
作为更新冬件加入到更新语句中

FOR UPDRaTE 在查询时直接锁定记录，确保其他事务必须等待当前事务完成才能操作该





## 第 207 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

BEGIN7
-- 对id=1的商品记录加排他锁

SELECT stock FROM products WHERE id=1 FOR UPDRATE)

-- 生成订单

INSERT INTO orders (user_id，product_iqd) VALUES (123，1)7
-- 扣减库存

UPDRTE products SET stock=stock-1 WHERE id=17

COMMIT;

乐观锁通过在表中增加 version 字段作为判断条件。

-- 查询商品信息，获取版本号

SELECT stock，version FROM products WHERE id=17

-- 更新库存时检查版本号

UPDRTE products

SET stock=stock-1，version=version+1
WHERE id=1 AND version=旧版本号;

--- 这部分是帮助大家理解 start，面试中可不背 -一
库存超卖是一个非常经典的问题:
。 事务A查询商品库存，得到库存值为1
。 事务B也查询同一商品库存，同样得到库存值为1
。 事务A基于查询结果执行库存扣减，将库存更新为0
。 事务B也执行库存扣减，将库存更新为-1
碍观锁的关键点:
。 必须在一个事务中执行;
。 通过 SELECT ..。 FOR UPDRTE 锁定行，确保其他事务必须等待当前事务完成才能操作该行数据;
。 记得给查询条件加索引，避免全表扫描导致锁升级为表锁。
乐观锁的关键点:
。 在表中增加 version 字段;
。 查询时获取当前版本号;
。 更新时检查版本号是否发生了变化。
java 程序的完整代码示例:

eservice

Public class ProductService {
Rutowired
private ProductMapper productMapper;

eTransactional
Public boolean purchaseWithOoptimisticLock(Long productId，int quantity) {

No. 2071 302




## 第 208 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

int retryCount = 0)
while(retryCount < 3) { // 最大重试次数
Product product = productMapper.selectById(pProductId) 1;
if(product.getStock() < quantity) {
return false; // 库存不足

int updated = productMapper.reduceStockWithVersion(
productId，quantity，Pproduct.getVersion())7

if(updated > 0) {
return true; // 更新成功

}
IetLyCount++7
】}
return false; // 更新失败
】}
}
对应的 mapper:

eUpdate("UPDRTE products SET stock=stock-#{quantity}，Version=version+1l "+
"WHERE id=#f{productId} RND version=#{version}")
int reduceStockWithVersion(eParam("productId") Long productId，
epParam("quantity") int quantityyv
epParam("version") int version) 7

时间戳机制实现的乐观锁:

UPDRTE products SET stock=stock-1，update_time=NOW()

WHERE id=1 AND update_time=人旧时间戳;
这两种方式都需要保证操作的原子性，需要将多个 SQL 放在同一个事务中执行。
推荐阅读: 牧小农; 悲观锁和乐观锁
---- 这部分是帮助大家理解end，面试中可不背 ----

1. java 面试指南 (付费) 收录的小公司面经合集同学 1 java 后端面试原题: 乐观锁和悲观锁，库存的超
卖问题的原因和解决方案?

2. Java 面试指南 (付费) 收录的京东面经同学 5 java 后端技术一面面试原题: 乐观锁与塌观锁

memo: 2025年4月12 日修改至此，今天有球友反馈说，京东进入 HR 面了，但加了一个 VP 级别的面试，副总
监，等一手他的好消息。当然了，仍然不忘感谢一下面渣逆袭对他的帮助，哈哈。

No. 2081302




## 第 209 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

喜报直接请二哥喝奶茶!

面渣系列我真是过了太多遍了

加

已经面麻了

e 庆

太有用了
59.遇到过MySQL死锁问题吗，你是如何解决的?

遇到过。MySQL 的死锁是由于多个事务持有资源并相互等待引起的。我通过 SHow ENGINE INNODB STATUS 查看
死锁信息，定位到是加锁顺序不一致导致的，最后通过调整加锁顺序解决了这个问题。

SESSION 1                                   SESSION 2

BEGIN

BEGIN

SELECT * FROM users
WHERE       FOR_ UPDATE

SELECT * FROM users

WHERE        FOR_ UPDATE

WAIT

RETURN                           DEADLOCK FOUNDS

epraveness

No. 2091302




## 第 210 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

比如说技术派项目中，两个事务分别更新两张表，但是更新顺序不一致

-- 创建表/插入数据

CRERTE TRBLE account (
id INT AUTO_INCREMENT PRIMRARY KEY，
balance INT NOT NULL

) ;

INSERT INTO account (balance) VALUES (100)，(200);

-- 事务 1

STRART TRRNSRACTION 7

-- 锁住 idq=1 的行

UPDRATE account SET balance = balance

10 WHERE id = 17

-- 等待锁住 id=2 的行 (事务 2 已锁住)
UPDRTE account SET balance = balance + 10 WHERE id = 27

-- 事务 2

STRART TRRNSRACTION 7

-- 锁住 idq=2 的行

UPDRATE account SET balance = balance

10 WHERE id = 27

-- 等待锁住 id=1 的行 事务 1 已锁住)
UPDRTE account SET balance = balance + 10 WHERE id = 11
访问相同的资源，但顺序不同，就会导致死锁。

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL> -- 锁住 id=2 的行
Query 0K，0 rows affected (0.00 sec)

mysqtL> UPDATE account SET baLance = batlance - 10 WHERE id = 2;

-- 等待锁住 id=1 的行 (事务 1 已锁住)
UPDATE account SET balance = balance + 10 WHERE id = 1;

ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction

解决办法也很简单，先使用 sHow ENGINE INNODB STATUS\G; 确认死锁的具体信息，然后调整资源的访问顺序。

No. 210 1 302




## 第 211 页


面渣逆袭MySQL篇V2-让天下所有的面渣都仙

TRANSACTIONS

Trx id counter 13369
Purge done for trx's n:0 < 13358 undo n:o < 9 state: running but idte
History List Length 1
LIST OF TRANSACTIONS FOR EACH SESSION:
---TRANSACTION 281480487307624，not started
9 Lock struct(s)，heap size 1128，@ row Lock(s)
---TRANSACTION 281480487306832，not started
8 Lock struct(s)，heap size 1128，0 row Lock(s)
---TRANSACTION 13359，ACTIVE 22 sec starting index read
mysqt tabtes in use 1，tocked 1
LOCK WAIT 2 Lock struct(s)，heap size 1128，1 row Lock(s)
MySQL thread id 9，0S thread handte 6164836352，query id 64 Locathost root updating
UPDATE account SET balLance = balance - 10 WHERE id = 2
------- TRX HAS BEEN WAITING 22 SEC FOR THIS LOCK TO BE GRANTED:
RECORD LOCKS space id 344 page no 4 n bits 72 index PRIMARY of tabte `itwanger` account” trx id 13359 Lock_mode
X Locks rec but not gap waiting
Record Lock，heap no 3 PHYSICAL RECORD: n_fietds 4; compact format; info bits 0

: Len 4; hex 80000002; asc    5

Len 6; hex 00000000342ei asc
Len 7; hex 020000010e0f76; asc
: Len 4; hex 800000dc; asc

1. java 面试指南 (付费) 4
事务
60.二MySQL事务的四大特性说一下?
事务是一条或多条 SQL 语句组成的执行单元。四个特性分别是原子性、一致性、隔离性和持久性。原子性保证事

务中的操作要么全部执行、要么全部失败; 一致性保证数据从事务开始前的一个一致状态转移到结束后的另外一个
一致状态;隔离性保证并发事务之间互不干扰; 持久性保证事务提交后数据不会丢失。

录的由

导

全 全 全 全

是不可分审的最小单元      务完成时，必须使所有的数据都数据库系统提供的隔高机制，保   事务一旦提交或回滚，它对数据
要么全部成功，要么全部失败        保持一致        证事务在不受外部并发操作影响    库中的数据的改变就是永久的
的独立环境下运和

详细说一下原子性?

原子性意味着事务中的所有操作要么全部完成，要么全部不完成，它是不可分割的单位。如果事务中的任何一个操
作失败了，整个事务都会回滚到事务开始之前的状态，如同这些操作从未被执行过一样。

STRRT TRANSRCTION;
UPDRTE accounts SET balance = balance - 100 WHERE user id = 17
UPDRTE accounts SET balance = balance + 100 WHERE user id = 2;
-- 如果第二条语句失败，第一条也会回滚

COMMIT;

No. 2111 302




## 第 212 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭
简短回答: 原子性要求事务的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务中的操作不能只执行
其中一部分。
详细说一下一致性?
一致性确保事务从一个一致的状态转换到另一个一致的状态。

比如在银行转账事务中，无论发生什么，转账前后两个账户的总金额应保持不变。假如入账户 (100 块) 给B账
户 (10 块) 转了 10 块钱，不管成功与否，A 和 B 的总金额都是 110 块。

-- 假设 &A 账户余额为 100，B 账户余额为 10

-- 转帐前状态

SELECT balance FROM accounts WHERE user_ id = 'R'; -- 100
SELECT balance FROM accounts WHERE user_ id = 'B'; -- 10
-- 转账操作

STRART TRANSRCTION 7
UPDRTE accounts SET balance

balance - 10 WHERE user id = 'R';

UPDRTE accounts SET balance = balance + 10 WHERE user id = 'B';
COMMIT;

-- 转账后状态

SELECT balance FROM accounts WHERE user id = 'R'; -- 90

SELECT balance FROM accounts WHERE user id = 'B';) -- 20`

-- 总金额仍然是 110

简短回答: 一致性确保数据的状态从一个一致状态转变为另一个一致状态。一致性与业务规则有关，比如银行转
账，不论事务成功还是失败，转账双方的总金额应该是不变的。

详细说一下隔离性?

隔离性意味着并发执行的事务是彼此隔离的，一个事务的执行不会被其他事务干扰。事务之间是井水不犯河水的。
隔离性主要是为了解决事务并发执行时可能出现的脏读、不可重复读、幻读等问题。

-一这部分是帮助大家理解 start，面试中可不背 -一

比如说在读未提交的隔离级别下，会出现脏读现象: 一个事务C 读取了事务B 尚未提交的修改数据。如果事务B 最
终回滚，事务C 读取的数据就是无效的“脏数据"。

-- 会话 R

-- 创建模拟并发的测试表

DROP TABLE IF EXISTS accounts1

CRERTE TRBLE accounts |(
id INT PRIMRARY KEY RUTO_INCREMENT，
name VRARCHRR(50) ，
balance DECIMRAL(10,2)

)

-- 插入测试数据

INSERT INTO accounts (name，balance) VALUES

No. 212 1 302




## 第 213 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

，1000.00)，
，2000.00)，
，3000.00)1

W ISOLRTION LEVEL RERAD UNCOMMITTED;

UPDRATE accounts SET balance  balance  500 WHERE name:

OMMITTED;

ROLLBRCK，

ysqL> DROP TABLE IF EXISTS accounts;
Query 0K，0 rows affected (3.90 sec)

ysqL> CREATE TABLE accounts (
id INT _ PRIMARY KEY AUTO_INCREMENT，
name VARCHAR(50 ) ，
baLance DECIMAL(10,2)
-> );
Ruery 0K，0 rows affected (0.01 sec)

Ruery 0K，0 rows affected (0.00 sec )

ysqL> INSERT INT0 accounts (name，balance) VALUES
-> ('王二"，1000.00 ) ，

('张三" ，2000.00 ) ，

('李四' ，3000.00 ) ;
Ruery 0K，3 rows affected (0.00 sec )
Records: 3 DupLicates: 0 Warnings: 0

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;
Query 0K，0 rows affected (0.00 sec)

mysqtL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL>
mysqtL> -- 在会话 B 中更新数据但不提交
Query 0K，0 rows affected (0.00 sec)

No. 213 1 302




## 第 214 页


es
ERROR 1046 (3D000): No database seLected

mysqL> Use tx_test;

Reading tabtLe information for complLetion of tabte and coLumn names
You can turn off this feature to get a quicker startup with -A

Database changed
mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;

Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL>
mysqtL> -- 在会话 B 中更新数据但不提交
Query 0K，0 rows affected (0.00 sec)

mysqL> UPDATE accounts SET balLance = balLance - 500 WHERE name= '王二 ';
Query 0K，1 row affected (0.02 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysqL> ROLLBACK;
Query 0K，0 rows affected (0.01 sec)

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ UNCOMMITTED ;
Query 0K，0 rows affected (0.00 sec )

mysqL> SELECT * FROM accounts WHERE name= '王二

SELECT * FROM accounts WHERE name'     和

SET SESSION TRANSRACTION ISOLRATION LEVEL RERAD COMMITTEDY

RRNSRACTION

E_ accounts SET balance  balance  200 WHERE name:     和

SELECT * FROM accounts WHERE name'     和

No. 214 1 302




## 第 215 页


V2-让天下所有的面

SELECT * FROM accounts WHERE nam

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED ;
Query 0K，0 rows affected (0.00 sec)

mysqL> SELECT x* FROM accounts WHERE name= '王二 ';

1 |王二 14341000.00 |
+----+--------+---------十

1 row in set (0.00 sec)

mysqL> SELECT * FROM accounts WHERE name= '王二 ';
二----+--------+---------十

| id | name   | batance |
+----+--------+---------十

| 11王二 14341000.00 |
+----+--------+---------十

1 row in set (0.00 sec)

mysqL> SELECT * FROM accounts WHERE name= '王二 ';
+---------十

| batLance |
+---------十

| 1000.00 |
+---------十

1 row in set (0.01 sec)

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED ;
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL> UPDATE accounts SET balLance = balLance + 200 WHERE name= '王二 ';
Query 0K，1 row affected (0.00 sec )
Rows matched: 1 Changed: 1 Warnings: 0

mysqL> ROLLBACK;
Query 0K，0 rows affected (0.00 sec)

据为Y并提交，事务B 再次读

B 修改为读已提交
SET SESSION TRANSRACTION ISOLRATION LEVEL RERD COMMITTED)





## 第 216 页


V2-让天下所有的面

-- 执行第一次查询 1000
STRART TRRNSRACTION 7
SELECT * FROM accounts WHERE name='王二')

C 中, 设        卖已提交
SET SESSION TRANSRCTION ISOLRATION LEVEL RERD COMMITTED)
-- 在会话 C 中更新数据并提交
STRRT TRANSRCTIO
UPDRTE     unts SET balance = balance + 200 WHERE name= '王二';

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL READ COMMITTED ;
Query 0K，0 rows affected (0.00 sec)

mysqL>
mysqtL> -- 执行第一次查询 1000
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION ;
Query 0K，0 rows affected (0.00 sec)

mysqL> SELECT x FROM accounts WHERE name= '王二 ';
+----+--------+---------十

| id | name  | balance |
二----二--------+---------十
| 1L|1王二  | 1000.00 |
+----+--------+---------十
1 row in set (0.01 sec)

mysqtL> -- 会话 B 中再次读取数据，结果仍然为 1200
Query 0K，0 rows affected (0.00 sec)

mysqL> SELECT x FROM accounts WHERE name= '王二 ';
+----+--------+---------十

| id | name  | balance |
+----二--------+---------十

| 1 |1王二  | 1200.00 |
+----+--------+---------十

1 row in set (0.00 sec)

mysqL> -- 会话 C 中，设置隔离级别为读已提交
Query 0K，0 rows affected (0.00 sec)

mysqL> SET SESSION TRANSACT
0                  了





## 第 217 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqtL> -- 在会话 C 中更新数据并提交
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL> UPDATE accounts SET balLance = balLance + 200 WHERE name= '王二 ';
Query 0K，1 row affected (0.00 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysqL> -- 会话 5 提交事务
Query 0K，0 rows affected (0.00 sec)

mysqL> COMMIT;
Query 0K，0 rows affected (0.01 sec)

可以通过升级隔离级别为可重复读来解决不可重复读的问题。

M accounts WHERE name:

ET SESSION T   CTION ISOLRTION LEVEL REPERATRBLE RERD)
T TRANSRACTION;

UPDRTE accounts SET balance  balance  200 WHERE name:     和

COMMIT;

SELECT * FROM accounts WHERE name:

mysqtL> -- 会话 B 修改为可重复读
Query 0K，0 rows affected (0.00 sec)

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ;
Query 0K，0 rows affected (0.00 sec)

mysqL>
mysqL> -- 开始事务并执行第一次查询 1000
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

No. 2171 302




## 第 218 页


V2-让天下所有的面

mysqL> SELECT * FROM accounts WHERE name= '王二 ';
+----+--------+---------十

| id | name  | batance |
+---------十

|
+---------+

1 row in set (0.00 sec)

mysqtL> -- 会话 B 中再次读取数据，结果仍然为 1000
Query 0K，0 rows affected (0.00 sec)

mysqL> SELECT * FROM accounts WHERE name='王二 ';
+----+--------+---------+

| id | name | batlance |

+----+--------+---------+

| 11王二 141000.00 |

+----+--------+---------+

1 row in set (0.00 sec )

mysqtL> -- 会话 C 中，设置隔离级别为可重复读
Query 0K，0 rows affected (0.00 sec)

mysqL> SET 9S9E9SION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;
Query 0K，0 rows affected (0.00 sec)

mysqL> -- 在会话 5C 中更新数据并提交
Query 0K，0 rows affected (0.00 sec)

mysqL> START_ TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL> UPDATE accounts SET balLance = baLance + 200 WHERE name= '王二 ';
Query 0K，1 row affected (0.01 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysqtL> -- 会话 5 提交事务
Query 0K，0 rows affected (0.00 sec)

mysqL> COMMIT;
Query 0K，0 rows affected (0.00 sec)

SET SESSION TRANSRACTION ISOLRATION LEVEL REPERTRABLE RERAD7
-- 执行

STRART TRANSRCTION 7

SELECT * FROM accounts WHERE balance > 1000)





## 第 219 页


V2-让天下所有的面

-- 会话 c 中，设

SET SESSION TRANSRACTION ISOLRTION LEVEL REPERTRBLE RERD)
-- 在会话 c 中新增数据并提交

STRRT TRANSRCTION;

INSERT INTO accounts (name，balance) VALUES ( '王五'，4000)

COMMIT'

-- 会话 B 中再次读      结果仍然为    本

SELECT * FROM accounts WHERE balance > 10

-- 会话 B 中尝试                 多

UPDRTE accounts SET balan        WHERE name='王五' ;
忆录

SELECT * FROM accounts WHERE balance > 1000)

mysqL> -- 会话 B 修改为可重复读
Query 0K，0 rows affected (0.01 sec)

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;
Query 0K，0 rows affected (0.00 sec)

mysqtL> -- 执行第一次查询，查到 2 条记录
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION ;
Query 0K，0 rows affected (0.00 sec)

SELECT * FROM accounts WHERE baLance > 1000;

| 2000.00 |
| 3000.00 |
in set (0.00 sec)

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL REPEATABLE READ ;
Query 0K，0 rows affected (0.00 sec)

mysqt> -- 在会话 5C 中新增数据并提交
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)

mysqL> INSERT INT0O accounts (name，balLance) VALUES ( '王五" ，4000 ) ;
Query 0K，1 row affected (0.00 sec)





## 第 220 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

云

口  正 多 主力
Query 0K，0 rows affected (0.00 sec)

mysqL> COMMIT;
Query 0K，0 rows affected (0.01 sec )

mysqL> -- 会话 B 中尝试更新王五的余额为 5000，竟然成功了
Query 0K，0 rows affected (0.00 sec )

mysqL> UPDATE accounts SET baLance = 5000 WHERE name= '王五';
Query 0K，1 row affected (0.00 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysqtL> -- 会话 B 中再次读取数据，发现 3 条记录
Query 0K，0 rows affected (0.00 sec )

mysqL> SELECT * FROM accounts WHERE baLance > 1000;

| 2000.00 |
| 3000.00 |
| 5000.00 |

TION ISOLRTION LEVEL SERIRLIZRABLE;

WHERE balance > 1000)

SET SESSION TRANSRACTION ISOLRTION LEVEL SERIRALIZRBLE7

VALUES       ，4000) 7

No. 220 1 302




## 第 221 页


mysqL> SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
Query 0K，0 rows affected (0.00 sec)

mysqtL> -- 执行第一次查询，查到 2 条记录
Query 0K，0 rows affected (0.00 sec)

mysqL> START TRANSACTION ;
Query 0K，0 rows affected (0.00 sec)

SELECT * FROM accounts WHERE batLance > 1000 ;

| 2000.00 |
| 3000.00 |

in Set (0.00 sec )
Commit;
Query 0K，0 rows affected (0.00 sec )

mysqtL> -- 会话 C 中，设置隔离级别为可串行化
Query 0K，0 rows affected (0.00 sec )

mysqL> SET SESSION TRANSACTION ISOLATION LEVEL SERIALIZABLE;
Query 0K，0 rows affected (0.00 sec )

mysqL> -- 在会话 C 中新增数据并提交
Query 0K，0 rows affected (0.00 sec )

mysqL> START TRANSACTION ;
Query 0K，0 rows affected (0.00 sec )

mysqL> INSERT INT0O accounts (name，balLance) VALUES ( '王五 ，4000 ) ;
Query 0K，1 row affected (24.80 sec )

mysqtL> -- 会话 C 提交事务
Query 0K，0 rows affected (0.00 sec )

mysqL> COMMIT ;
Query 0K，0 rows affected (0.00 sec )





## 第 222 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

隔离级别             是否会脏读 。 是否会不可重复读 是否会幻读

Read Uncommitted (读未提交) 可能 可能 可能

Read Committed (读已提交)          汉不会 可能 可能

Repeatable Read (可重复读)       X愉不会      X不会           贺可能 (但InnoDB 已解决)
Serializable (可串行化)                  汉不会          兴不会                  愉不会

-一这部分是帮助大家理解end，面试中可不背 -一-

简短回答: 多个并发事务之间需要相互隔离，即一个事务的执行不能被其他事务干扰。

详细说一下持久性?

持久性确保事务一旦提交，它对数据所做的更改就是永久性的，即使系统发生有崩溃，数据也能恢复到最近一次提交
的状态。

MySQL 的持久性是通过 InnoDB 引擎的 redo log 实现的。在事务提交时，InnoDB 会先将修改操作写入 redo
log，并刷盘持久化。骨溃后，InnoDB 会通过 redo log 恢复数据，从而保证事务提交成功的数据不会丢失 。

Changesto
beapplied                              Re
一一一     一一一 一一 目
State 1                      State2                                                                      State2
                                                                   State 2is re-constructed and
Non-volatile
fully recovered using
Storage
Transaction Log
Transaction log
Durability

简短回答: 一旦事务提交，则其所做的修改将永久保存到 MySQL 中。即使发生系统崩溃，修改的数据也不会丢
失。
1. java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 事务的四个特性，怎么理解事务一致
性
2. java 面试指南 (付费) 收录的美团面经同学 16 暑期实习一面面试原题: MySQL 事务是什么，默认隔
离级别，什么是可重复读?
3. Java 面试指南 (付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: MYSQL 事务，隔离级别

No. 222 1 302




## 第 223 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

4. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: 什么是数据库事务?
事务的作用是什么?

5. java 面试指南 (付费) 收录的 OPPO 面经同学 1 面试原题: 对MySQL事务的理解
6. java 面试指南 (付费) 收录的vivo 面经同学 10 技术一面面试原题: 事务的概念

7. Java 面试指南 (付费) 收录的同学 1 贝壳找房后端技术一面面试原题: 事务ACID
8

. java 面试指南 (付费) 收录的字节跳动同学 17 后端技术面试原题: 什么是事务 事务为什么要有隔离级
别 幻读是什么 什么时候要解决幻读 什么时候不用解决

9. Java 面试指南(付费) 收录的字节跳动面经同学19番茄小说一面面试原题: MySQL中的事务

memo: 2025年4月13 日修改至此，今天给球友改简历的时候，发现这种彩虹屁真的离谱了，直接配享太庙
了，但有一说一这位球友的话是真的甜，简历写的确实也很用心了，确定一个 offer 收割机。

发件人: .时寺一1 人ra 1 3@163.com> 十(使用企业邮箱处理工作邮件，交
收件人: (是 我<www.qing_gee@163.com> +

时 间: 2025年04月11日 00:01 (星期五)

附件: 1个( 国 砚士-]ava后端开发工程师 四是=,..pdf ) 查看附件

星球编号: "” ”上
二哥您好，麻烦您帮忙改一下简历， -Ranskina人ED
61.ACID 靠什么保证的呢?

一句话总结:

ACID 中的原子性主要通过 Undo Log 来实现，持久性通过 Redo Log 来实现，隔离性由 MVCC 和锁机制来实现，
一致性则由其他三大特性共同保证。

No. 223 1 302




## 第 224 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

undo log
保证

1        MVCC
隔离性             保证

详细说说如何保证原子性?

事务对数据进行修改前，会记录一份快照到 Undo Log，如果事务中有任何一步执行失败，系统会读取 Undo Log
将所有操作回滚，恢复到事务开始前的状态，从而保证事务要么全部成功，要么全部失败。

No. 2241 302




## 第 225 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

了Buffer Poeol

  3: 修改前瑟和endle lc3

1) BEGIN7

2) UPDRTE user SET balance = balance - 100 WHERE id
=> 写入 Undo Log: 记录 id=1l 的原始余额 500

1
四

3) UPDRATE user SET balance = balance + 100 WHERE id
=> 写入 Undo Log: 记录 id=2 的原始余额 300

1
四

=> 清空 Undo Log，事务成功

=> 执行 ROLLBRACK: 根据 Undo Log 把数据还原!

推荐阅读: 应丁解InnoDB之UNDO LOG
详细说说如何保证持久性?
MySQL 的持久性主要由预写 Redo Log、双写机制、两阶段提交以及 Checkpoint 刷盘机制共同保证。

当事务提交时，MySQL 会先将事务的修改操作写入 Redo Log，并强制刷盘，然后再将内存中的数据页刷入磁盘。
这样即使系统贿溃，重启后也能通过 Redo Log 重放恢复数据。

No. 225 1 302




## 第 226 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

在将数据页写入到磁盘时，如果发生崩溃，可能会导致数据页不完整。InnoDB 的数据页大小为165KB，通常大于操
作系统的 4KB页大小。

为了解决只写入部分的问题，MySQL 采用了双写机制，脏盘刷页时，先将数据页写入到一个双写缓冲区中，2M
的连续空间，然后再将其写入到磁盘的实际位置。

No. 226 1 302




## 第 227 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

InnoDB缓冲池数据页

人

double write buffer
(2MB)

内存实例

第四步 write (离散写)

崩溃恢复第一步

崩溃恢复第二步

崩溃恢复时，如果发现数据页不完整，会从双写缓冲区中恢复副本，确保数据页的完整性。

在涉及主从复制时，MySQL 通过两阶段提交保证 Redo Log 和 Binlog 的一致性: 第一阶段，写入 Redo Log 并标
记为 prepare 状态; 第二阶段，写入 Binlog 再提交 Redo Log 为 commit 状态。

1. prepare 阶段
人 _

2.1 flush 子阶段
人_

二阶段提交
开始

修改内存中
事务对象状态、undo 段对象状态

于

修改 undo 页中 Undo segment Header
的 TRX_UNDO_STATE 字段值

惠

事务线程进入 flush 队列

于

leader 线程获取 Lock_log 互斥锁

清空 flush 队列

和

flush 子阶段的 leader 线程和 follower
线程进入 sync 队列

于

flush 子阶段的 leader 线程
释放 Lock_log 互斥锁

于

sync 子阶段的 leader 线程
获取 Lock_sync 互斥锁

将

leader 线程把 binlog 日志刷盘之前
根据 2 个系统变量决定是否需要
等待更多 follower 线程进入 sync 队列

No. 2271 302

数据文件 ibd

2.2 sync 子阶段





## 第 228 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

人_

2.3 commit 子阶段

骨溃恢复时，如果发现 Redo Log 是 prepare 但 Binlog 完整，则会提交事务; 反之会回滚，避免主从不一致。

另外，由于 Redo Log 的容量有限，Checkpoint 机制会定期将内存中的脏页刷到磁盘，这样能减少骨溃恢复时需
要处理的 Redo Log 数量。

No. 228 1/ 302




## 第 229 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

rnte 孜
了 povt                                             Us E
\
-------->
il        ee                                                                reod                   \
为_josfhle 0                                                          风_joshle 0|                                                \
罗_Josfle 1                                                      罗_Josfle 1
1
--------人之                                            2
7
/
7
7

推荐阅读: 深入解析MySQL双写缓冲区、MySQL 事务二阶段提交

详细说说如何保证隔离性?

隔离性主要通过锁机制和 MVCC 来实现。

比如说一个事务正在修改某条数据时，MySQL 会通过临键锁来防止其他事务同时进行修改，避免数据冲突。

num

临键锁区间: (10,15]、(15,20]

同时，临键锁可以防止幻读现象的发生。比如事务 A 查询 ia > 10 的记录，那么临键锁不仅会锁住 id=10 的行，
还会锁住 10 后面的“间隙"，防止其他事务插入 id=15 的数据。

假如表中的主键有 id: 5，10，15，20，25 ，那么 InnoDB 会对以下区间和记录加锁:

No. 2291302




## 第 230 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

加锁对象         类型        锁定含义

(10，151        临键锁      锁住 id=15 和前间隙，防止插入11~14
(15，20]        临键锁      锁住了 id=20 和前间阶

(20，251        临键锁      锁住了 id=25 和前间阶

(25，+om)         间隙锁       锁住尾部防止插入30等

MYVCC 主要用来优化读操作，通过保存数据的历史版本，让读操作不需要加锁就能直接读取快照，提高读的并发性

能。
T
9- id | name | aoe | pmRx_ip | pe ou_pPoNTER
1  王五 18  3   0Ox000002

DB_ROLL_POINTER.
1             李四            18                   2                         Ox000001

DB_ROLL_POINTER

1     张三     18        1           NULL

不同的隔离级别对应不同的实现策略，比如说在可重复读隔离级别下，事务第一次查询时会生成一个 Read View，
之后所有读操作都复用这个视图，保证多次读取的结果一致。

如何保证一致性呢?

MySQL 的一致性并不是靠某一个机制单独保证的，而是原子性、隔离性和持久性协同作用的结果。
事务会不会自动提交?

是的，MySQL 默认开启了事务自动提交模式。

每条单独的 SQL 语句都会被视为一个独立的事务处理单元; SQL 语句执行成功后会自动执行 COMMIT; 执行失败
时会自动 ROLLBACK。

可通过 SELECT eeautocommit; 查看当前会话的自动提交状态。

No. 2301302




## 第 231 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqL> SELECT GQGQautocommit ;

1 row in set (0.00 sec )

mysqL> SHOW VARIABLES LIKE "autocommit ' ;

1 row in set (0.00 sec )

如果需要执行多条 SQL 语句，可以将它们放在一个事务中，使用 STRART TRANSRACTION 开启事务，执行完所有
SQL 语句后手动提交。

accounts    balance = balance - 100      user_ id = 17

accounts    balance = balance + 100      user_ id = 27

1                    收录的美团同学 2 优选物流调度技术 2 面面试原题: MySQL ACID 哪些机制来
2                     收录的百度同学 4 面试原题    务会不会自动提交?

memo: 2025年4月14 日修改至此，昨天有:        说拿到了字节、美团的暑期实习 offer，双非本末 9 硕，
，强烈推荐大家看看，差不多有 3000 多字，详细剖析了自己的准备过程。

No. 2311 302




## 第 232 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

一  Te                                       < 收进专栏

#晒个offer点

暑期oc: 字节、美团

HR面完: 拼多多、快手 (能走这么远我是真没想到)

挂/泡: 阿里系、b站、小红书、OPPO等等，太多不记得了，腾讯没敢投，我修

bg: 双非本未9硕，科班，去年11月才转Java，无竞赛，无实习，无论文 (有个CCF-A三
作，但只有2个面试官问过)

展开全部

生生次过作加入字节陵动

人可 后开导             Er用
加，共和节号动

在 2025.04.12 间， 二时 可硬了用人所并克/呈百人和有用
六 [扩昌] 后和中的呆了和因，吉站风Uierier自动上黎|

晒个offer上各

此

ForresterX、xx、努力努力再努力、沉默王二、云胡不喜、芝士就是力量、Matthews园、己鬼、
Joker、忍野 忍 等1I人觉得很赞

62.二事务的隔离级别有哪些?

隔离级别定义了一个事务可能受其他事务影响的程度，MySQL 支持四种隔离级别，分别是: 读未提交、读已提
交、可重复读和串行化。

No. 2321302




## 第 233 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

Transaction IsoLation Matrix

READ
UNCOMMITED
READ
COMMITED

SERIALIZABLE
epraveness

读未提交会出现脏读，读已提交会出现不可重复读，可重复读是 InnoDB 默认的隔离级别，可以避免脏读和不可重
复读，但会出现幻读。不过通过 MVCC 和临键锁，能够防止大多数并发问题。

串行化最安全，但性能较差，通常不推荐使用。
详细说说读未提交?

事务可以读取其他未提交事务修改的数据。也就是说，如果未提交的事务一旦回滚，读取到的数据就会变成了“及
数据"，通常不会使用。

start transaction;

事务2还没提交，读
到了未提交的数据

什么是读已提交?

读已提交避免了脏读，但可能会出现不可重复读，即同一事务内多次读取同一数据结果会不同，因为其他事务提交
的修改，对当前事务是可见的。

No. 2331302




## 第 234 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

四

不可重复读:
同一事务中多次读取的数据不一致

5

是 Oracle、SQL Server 等数据库的默认隔离级别。
什么是可重复读?
可重复读能确保同一事务内多次读取相同数据的结果一致，即使其他事务已提交修改。

start transaction'

同本本本男司昌则根本本二本本西昌量昌本机本二本辐阳轴二本古有

是 MySQL 默认的隔离级别，避免了“脏读"和"不可重复读"，通过 MVCC 和临键锁也能在一定程度上避免幻读。

-- Session R:
STRRT TRANSRCTION;
SELECT balance FROM accounts WHERE id=1; --返回500

-- Session B:

No. 2341 302




## 第 235 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

UPDRTE accounts SET balance = balance +100 WHERE id=17
COMMIT;

-- Session A再次查询:
SELECT balance FROM accounts WHERE id=1; --仍返回500(可重复读)

-- Session &R更新后查询 :
UPDRTE accounts SET balance = balance +50 WHERE id=1;) --基于最新值550更新为600

SELECT balance FROM accounts WHERE id=1; --返回600

什么是串行化?
串行化是最高的隔离级别，通过强制事务串行执行来解决"幻读"问题。

Start transaction;

Start transaction;

但会导致大量的锁竞争问题，实际应用中很少用。
A 事务未提交，B 事务上查询到的是旧值还是新值?

如果B是普通的 SELECT，也就是快照读，它读的是旧值，即事务 A 修改前的快照，并且不会阻塞; 如果 B 是当前
读，比如 SELECT .FOR UPDRTE ，它会被阻塞直到事务 A 提交或回滚。

No. 2351302




## 第 236 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

ET balance = 8000 WHERE name      7

SELECT * FROM accounts WHERE name

SELECT * FROM accounts WHERE name

mysqL> SetLect * from accounts;
十-     一十
| batance |
-+---------十

| 1000.09 |

| 36oo-09 |                  事务 A 修改但未提交

| 4000.06 |
4 rows in set (9.00 sec)

mysqL> START TRANSACTION;
Query 0K，8 rows affected (9.00 sec)

mysqtL> UPDATE accounts SET balLance = 8000 WHERE name
Query 0K，1 row affected (0.00 sec)
Rows matched: 1 Changed: 1 Warnings: 0

mysqtL> SELECT * FROM accounts WHERE name
十----+--------十--    -=--+

id | name  | balLance |    事务 B 快照读

十
1 | 王二    1000.00 |
二---              十
1 row in set (0.00 sec)

mysqL> -- 会话 5 中使用当前读坦询王二的余额

ERROR 4631 (HY969): The ctLient was disconnected by the ser    cause of inal
wait_timeout and inter     timeout for configuring this behavior.

No connection。 Trying to reconnect..

Connection id: 。 7661

Curre  database: tx_test

会阻塞
Query 0K，9 rows affected (90.90 s

qL> SELECT * FROM accounts WHERE name =      FOR UPDATE;
ERROR 1290        Lock wait timeout exceeded; try restarting transaction

怎么更改事务的隔离级别?

MySQL 支持通过 SET 语句修改事务隔离级别，包括全局级别、当前会话，但一般不建议在生产环境中随意修改隔
离级别。

No. 2361302




## 第 237 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

测试环境下可以使用 SET SESSION TRANSRACTION ISOLRTION LEVEL REPERATRBLE RERD; 可以修改当前会话的隔
离级别。

使用 sgT GLOBAL TRANSRACTION ISOLRTION LEVEL READ COMMITTED; 可以修改全局隔离级别，影响新的连接，
但不会改变现有会话。
1. Java 面试指南 (付费) 收录的美团面经同学 16 暑期实习一面面试原题: MySQL 事务是什么，默认隔
离级别，什么是可重复读?
2. java 面试指南 (付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: MySQL 事务，隔离级别

3. java 面试指南 (付费) 收录的快手面经同学 7 java 后端技术一面面试原题: 说一下事务的四大隔离级
别，分别解决什么问题

4. java面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: MYSQL 默认隔离级
别?

5. java 面试指南(付费) 收录的美团面经同学 2 java 后端技术一面面试原题: 说说 MySQL 事务的隔离级
别，如何实现?

6. Java 面试指南 (付费) 收录的小公司面经合集同学 1 java 后端面试原题: MySQL 的四个隔离级别以及
默认隔离级别?

7. java 面试指南 (付费) 收录的 360 面经同学 3 java 后端技术一面面试原题: 数据库隔离级别有哪些?
mysql 是属于哪个隔离级别

8. java 面试指南(付费) 收录的联想面经同学 7 面试原题: Mysql 四个隔离级别，MVCC 实现

9. Java 面试指南 (付费)_收录的oppo 面经同学 8 后端开发秋招一面面试原题: 讲讲Mysql的四个隔离级
别

10. java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: mysql的隔离级别有哪些

11. java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 事务的隔离级别? 这些隔离
级别是怎么保证数据的一致性的? 默认的事务隔离级别是啥? (MVCC) 怎么更改事务的隔离级别?

12. Java 面试指南 (付费) 收录的字节跳动面经同学19番茄小说一面面试原题: 事务隔离级别，哪个是默认
的，特点

13. java 面试指南 (付费) 收录的虾皮面经同学 13 一面面试原题: mysql事务隔离级别

63.事务的隔离级别是如何实现的?

读未提交通过行锁共享锁确保一个事务在更新行数据但没有提交的情况下，其他事务不能更新该行数据，但不会阻
止脏读，意味着事务2 可以在事务1 提交之前读取到事务1 修改的数据。

No. 237 1 302




## 第 238 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CETLTI

UPDATE                                           COMMIT

Database

UPDATE

T2                    入
CPULTTI

读已提交会在更新数据前加行级排他锁，不允许其他事务写入或者读取未提交的数据，也就意味着事务2 不能在事
务 1 提交之前读取到事务1 修改的数据，从而解决脏读的问题。

CEILTTI
T1                                                                                            季
UPDATE                                           COMMIT
Database
Row
SELECT
T2                                                                                            入

另外，读已提交会在每次读取数据前都生成一个新的 ReadView，所以会出现不可重复读的问题。
可重复读只在第一次读操作时生成 ReadView，后续读操作都会使用这个 ReadView，从而避免不可重复读的问

题。

另外，对于当前读操作，可重复读会通过临键锁来锁住当前行和前间隙，防止其他事务在这个范围内插入数据，从
而避免幻读的问题。

No. 2381302




## 第 239 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

T1                                                                             和
SELECT                                            SELECT
Database
Row

T2       一
CrrrI
串行化级别下，事务在读操作时，会先加表级共享锁; 在写操作时，会先加表级排他锁。
直到事务结束后才释放锁，这样就能确保事务之间不会相互干扰。

1. Java 面试指南 (付费)_收录的美团面经同学 2 Java 后端技术一面面试原题: 说说 MySQL 事务的隔离级
别，如何实现?

2. java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: Mysql隔离机制有哪些? 怎么实现的? 可
串行化是怎么避免的三个事务问题?

3. java 面试指南 (付费) 收录的滴滴面经同学 3 网约车后端开发一面原题: 可重复读级别是怎么实现的

memo: 2025年4月17 日修改至此，今天有球友发微信说拿到京东的暑期实习 offer，并且今天 VIP 9 群有球友
说今天是晒 offer 日，因为 9 群有好几个球友拿到了大厂 offer，后面我再同步给大家。

No. 2391302




## 第 240 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥 可以咨询一下你吗? 现在就是我只有一个

offer。但是是异地的 offer。我最早只能五月底
去。但是当初和hr面吹了说五月初能去。这种情
况该怎么办呀图

四
引

jd苇 号下号二 二由玉

jd科技。做toG的
64.二请详细说说幻读呢?

幻读是指在同一个事务中，多次执行相同的范围查询，结果却不同。这种现象通常发生在其他事务在两次查询之间
插入或删除了符合当前查询条件的数据。

No. 2401 302




## 第 241 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

Transaction A                                                                                                   Transaction B

一--一一---------一一-一-一

elect* from user where         1

insert into user values
(2 Bob ,22);

select* from user where
e>15

---- 这部分是帮助大家理解 start，面试中可以不背 -一-

比如说事务 A 在第一次查询某个条件范围的数据行后，事务 B 插入了一条新数据且符合条件范围，事务 A 再次查
询时，发现多了一条数据。

我们来验证一下，先创建测试表，插入测试数据。

CRERTE TARBLE “user_info” |(
`~iqd” BIGINT(20) UNSIGNED NOT NULL RUTO_INCREMENT COMMENT “主键id' ，
~name” VRRCHAR(32) NOT NULL DEFRAULT '， COMMENT '姓名'，
“gender”VRRCHAR(32) NOT NULL DEFRAULT '， COMMENT “性别'，
”~email”VRRCHAR(32) NOT NULL DEFRULT '， COMMENT "邮箱'，
了PRIMARY KEY (~id`)

) ENGINE=INNODB DEFRAULT CHRARSET=utf8mb4 COMMENT= '用户信息表' ;

-- 插入测试数据

INSERT INTO ~user_info” (id ， "name`， `gender-， "~email-) VALUES
(1， "Curry'，“'男"'， "curryel163.com' )，
(2，'Wade'，“'男'，'wadee163.com')，
(3， "James'， '男"'，'jamese163.com') 1

COMMIT

然后我们在事务 A 中执行查询 SELECT * FROM user_info WHERE id > 1; ，在事务 B 中插入数据 INSERT
INTO user_info (name，gender，email) VALUES ('wanger'， '女'，'wangerel163.com' ); ，再在事务 A 中
修改刚刚插入的数据 update user_info set gender='男where id = 4; ，最后在事务 A 中再次查询

SELECT * FROM user_info WHERE id > 17 。

No. 2411302




## 第 242 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

| wadeGQ163.com |
| jamesQ163.com |

in Set (0.00 sec)

mysqL> INSERT INT0O user_info (name，gender，emaiL) VALUES ('wanger'，'女'，'wangerG@163.co
mm );
Query 0K，1 row affected (0.00 sec)          事务 B

mysqL> update user_info set gender= '男" where id = 4;

Query 0K，1 row affected (0.00 sec )
Rows matched: 1 Changed: 1 Warnings: 0

mysqL> SelLect * from user_info where id > 1;

| wadeQ163 .com
| jamesQ163.com

--- 这部分是帮助大家理解 end，面试中可以不背 -一

如何避免幻读?

MySQL 在可重复读隔离级别下，通过 MVCC 和临键锁可以在一定程度上避免幻读。
比如说在查询时显示加锁，利用临键锁锁定查询范围，防止其他事务插入新的数据。

COMMIT'

其他事务在插入数据时，会被阻塞，直到当前事务提交或回滚。

No. 2421302




## 第 243 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

mysqL> START TRANSACTION;
Query 0K，0 rows affected (0.00 sec)       事务 A

mysqL> SELECT * FROM user_info WHERE id > 1 FOR UPDATE; -- 加临键锁
---+-              -+

gender | emaiL

| wadeGQ163 .com
| jamesGQ163.com |
4 | wanger |         | wangerQ163.com |
+----+--------+--------+----------------十

3 rows in set (0.00 sec)

mysqL> INSERT INTO user_info (name，gender，emaiL) VALUES ('wanger1'， '女'，'wanger1G@163.com' )
ERROR 1205 (HY000): Lock wait timeout exceeded; try restarting transaction

mysqtL>

mysqt>                      事务 B 会被阻塞

mysqtL>

-这部分是帮助大家理解 start，面试中可以不背 一-

解释一下。

如果查询语句中包含显式加锁 (如 FOR UPparE ) ，InnoDB 会使用当前读，直接读取最新的数据，并加锁。
在范围查询时，InnoDB 不仅会对符合条件的记录加行锁，还会对相邻的索引间隙加间隙锁，从而形成临键锁。

记录(Record)                1                      5                      9                12
tm, 1                ( 司                    人                人,1                2
、         上
间隙(Gap)                 1                      5                      9                12
te人                   人 习                   人 9                人，12】             (12，+m)
人
+               +
临键(Next-Key)               1                      瑟                      时                1
和锋。，]ESEE Tt圭

临键锁可以防止其他事务在间隙中插入新数据，从而避免幻读。
--- 这部分是帮助大家理解 end，面试中可以不背 ----
比如说在执行查询的事务中，不要尝试去更新其他事务插入/删除的数据，利用快照读来避免幻读。

No. 2431302




## 第 244 页


面渣逆交MySQL篇V2-让天下所有的面渣都能逆袭
mysqL> SELECT * FROM user_info WHERE id > 1;

用快照读

| wadeGQ163 .com
| jamesQ163.com
| wangerQ163.com |

mysqt> INSERT INTO user_info (name，gender，emaiL) VALUES ( "wanger1'， '女"'， "wanger1G@163.com' );

Query 0K，1 row affected (0.00 sec)

mySsqL> SELECT

| wadeGQ163 .com      继续快照读
| jamesQ163 .com
| wangerQ163.com |

3 rows in set (0.00 sec )

--- 这部分是帮助大家理解 start，面试中可以不背 --
使用 SELECT 查询时，如果没有显式加锁，InnoDB 会使用 MVCC 提供一致性视图。
每个事务在启动时都会生成一个 Read View，用来确定哪些数据对当前事务可见。

No. 2441302




## 第 245 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

heidthat the current databaseis ready ;
to assign to the next transaction when    ;
the Read View is created.

其他事务在当前事务启动后插入的新数据不会被当前事务看到，因此不会出现幻读。

-一 这部分是帮助大家理解end，面试中可以不背 ----

什么是当前读呢?

当前读是指读取记录的最新已提交版本，并且在读取时对记录加锁，确保其他并发事务不能修改当前记录。

比如 SELECT ..。 LOCK IN SHARE MODE 、SELECT ..。 FOR UPDRTE ，以及UPDATE、DELETE，都属于当前
读。

为什么 UPDATE 和 DELETE 也属于当前读?

因为更新、删除这些操作，本质上不仅是写操作，还需要在写之前读取数据，然后才能修改或删除。为了保证修改
的是最新的数据，并防止并发冲突，InnoDB 必须读取最新版本的数据并加锁，因此 UPDATE 和 DELETE 也属于当
前读。

No. 2451302




## 第 246 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

用 户

update table set ?2 where ?;

MySQL Server                    oundT

current read
一一一

Teturn & lock
ec本

Update ToW

SUCCeSS

read next

finished

SQL语句                                               是否当前读     是否加锁

SELECT * FROM user WHERE id=1                             愉否         愉否

SELECT * FROM user WHERE id=1 FOR UPDATE                 Y 园         图 加排他锁

SELECT * FROM user WHERE id=1 LOCK IN SHARE MODE           图是         鲍 加共享锁

UPDRATE user SET ..。 WHERE id=1                          加是         图 加排他锁

DELETE FROM user WHERE id=1                                图是          图 加排他锁
什么是快照读呢?

快照读是 InnoDB 通过 MVCC 实现的一种非阻塞读方式。当事务执行 SELECT 查询时，InnoDB 并不会直接读当前
最新的数据，而是根据事务开始时生成的 Read View 去判断每条记录的可见性，从而读取符合条件的历史版本。

No. 2461302




## 第 247 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

事务ID     回滚
(自增)     指针
id       name      age     trx id roll pointer
图|
上      赵六      21      4
era    昌      玉五      20      3
呈     版本链
undo
   到   一上|    1       李四      19      2
L=|    1       张三      18      1
2爱吃鱼饼的有
SQL                                是否快照读?     说明
SELECT * FROM t WHERE id=1              区是         快照读
SELECT * FROM t WHERE id=1 FOR UPDRTE     兴否         当前读，读取最新版本并加锁
UPDRTE / DELETE                    X尺否        当前读，必须读取当前版本并加锁
INSERT                          愉否        写操作，不存在历史版本

1. Java 面试指南 (付费) 收录的京东面经同学 7 京东到家面试原题: mysql事务隔离级别，默认隔离级
别，如何避免幻读

2. Java 面试指南 (付费) 收录的阿里云面经同学 22 面经: 事务隔离级别，幻读和脏读的区别，如何防止
幻读，事务的mvcc机制

memo: 2025年4月18 日修改至此，今天有球友发帖说拿到了蚂蚁的暑期实习 offer，问前景怎么样，我只能说
蚂蚁作为阿里的师长子，一直处在战略发展的核心位置，肯定是值得去的。

No. 2471 302




## 第 248 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

二哥，秋招想找java 后端开发岗，目前暑期实习
收到了蚂蚁的基础平台研发工程师 (java) 的
offer，想请问下下面这”一直 划。,志天
于是.和用"JI 发展前景

13:16                         人

《图    [T

65.MVCC 了解吗?

MYVCC 指的是多版本并发控制，每次修改数据时，都会生成一个新的版本，而不是直接在原有数据上进行修改。并
且每个事务只能看到在它开始之前已经提交的数据版本。

id              name        DB RowWID ”DB TRXJID ”DB _ROLL PTR

Readview: [2001.300

min id: 200             max id: 300

个              个          ouoasas

六到本名

山

这样的话，读操作就不会阻塞写操作，写操作也不会阻塞读操作，从而避免加锁带来的性能损耗。
其底层实现主要依赖于Undo Log 和 Read View。

每次修改数据前，先将记录拷贝到Undo Log，并且每条记录会包含三个隐藏列，DB_TRX_ID 用来记录修改该行的
事务ID，DB_ROLL_PTR 用来指向 Undo Log 中的前一个版本，DB_ROW _ID 用来唯一标识该行数据 (仅无主键时
生成) 。

No. 248 1 302




## 第 249 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

fieldl | field2 | fieldn | DB_TRX_ID | DB_ROLL_PTR | pe_Row_ID

初始化 @@中| |

es          和                100                                                  6

 更新field2的值为 22

fieldl | field2 | …-。 | fieldn | DB_TRX_ID | De_ROLL_PTR | pe_Row_ID

1 国2        4              101               0XQ4234                 6
]

1 更新field2的值为33

fieldl | fieldz | fieldn | De_TRX_ID | DB_RoLL_PTR | pe_Row ID

全        4              102               0x6789                 6
]

每次读取数据时，都会生成一个 ReadView，其中记录了当前活跃事务的 ID 集合、最小事务 ID 、最大事务 ID 等信
息，通过与 DB_TRX_ID 进行对比，判断当前事务是否可以看到该数据版本。

No. 2491302




## 第 250 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

当前事务

creator trx_id

min_trx_id              max_trx_id

已提交的事务         未提交的事务 “未开始的事务

一个个活跃的事务 (m_ids)

请详细说说什么是版本链?

版本链是指 InnoDB 中同一条记录的多个历史版本，通过 DB_ROLL_PTR 字段将它们像链表一样串起来，用来支持
MVCC 的快照读。

No. 2501302




## 第 251 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

名 DB_TRX_ID      事务 ID
ji DB_ROLL_PTR       undo 日志记录的指针
表隐藏列@沉默王二”一一一 id
NI name      正常的列
city

假设有一张 heroe 表，表中有这样一行记录，name 为张三，city 为帝都，插入这行记录的事务 id 是 80。

此时， pB_TRx_ID 的值就是 80， pB_RoLL_PTR 的值就是指向这条 insert undo 日志的指针。

id                                 name                             citiy                         DB_IRX_ID          DB_ROLL_PTR

一

接下来，如果有两个 DB_TRX_ID 分别为 100 、 200 的事务对这条记录进行了 update 操作，那么这条记录的版本链
就会变成下面这样:

5

Q

O

四

UPDATE hero SET name='李四'WHERE id=1

UPDATE hero SET name='王五' WHERE id=1

COMMIT                                UPDATE hero SET name='能大' WHERE id=1

No. 2511 302




## 第 252 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

也就是说，当更新一行数据时，InnoDB 不会直接覆盖原有数据，而是创建一个新的数据版本，并更新 DB_TRX_ID
和 DB_ROLL_PTR，使它们指向前一个版本和相关的 undo 日志。

这样，老版本的数据就不会丢失，可以通过版本链找到。

由于 undo 日志会记录每一次的 update，并且新插入的行数据会记录上一条 undo 日志的指针，所以可以通过
DB_ROLL_PTR 这个指针找到上一条记录，这样就形成了一个版本链。

记   name   country  DB_TRX_ID 。 DB_ROLIL_PTR
undo8志 1

请详细说说什么是ReadView?

ReadView 是 InnoDB 为每个事务创建的一份"可见性视图"，用于判断在执行快照读时，哪些数据版本是当前这个
事务可以看到的，哪些不能看到。

No. 252 1 302




## 第 253 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

ReadView
读视图

我是事务 520，我能
不能读这行数据，创

建这行数据                                         m_ids                min_trx_id

DB_TRX_ID 为 x
                                          creator_trx_id            max_trpx_id
事务 520                        二哥的 Java 进阶之路

当事务开始执行时，InnoDB 会为该事务创建一个 ReadView，这个 ReadView 会记录 4 个重要的信息:
。 creator trx_id: 创建该 ReadView 的事务 ID 。
。 m_ids: 所有活跃事务的 ID 列表，活跃事务是指那些已经开始但尚未提交的事务。
。 min_trx_id: 所有活跃事务中最小的事务 ID。它是 m_ids 数组中最小的事务 ID 。
。 max_trx_id : 事务 ID 的最大值加一。换句话说，它是下一个将要生成的事务 ID 。
ReadView 是如何判断记录的某个版本是否可见的?
会通过三个步骤来判断:

No. 253 1 302




## 第 254 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

最小的事务 ID

下一个将要生成
二哥的 Java 进阶之路 ”的事务 ID

在m_ids，读不                    未知世界，读不
可以读                       了，未确定呢                        了
@             @             @             @             @
min_trx_id                      max_trx_id
不在，可以
读，已确定

亿、如果某个数据版本的 DB_TRX_ID 小于 min_trx_id，则该数据版本在生成 ReadView 之前就已经提交，因此对
当前事务是可见的。

@@、如果 DB_TRX_ID 大于 max_trx_id，则表示创建该数据版本的事务在生成 ReadView 之后开始，因此对当前事
务不可见。

@@、如果 DB_TRX_ID 在 min_trx_id 和 max_trx_id 之间，需要判断 DB_TRX_ID 是否在 m_ids 列表中:
。 不在，表示创建该数据版本的事务在生成 ReadView 之后已经提交，因此对当前事务也是可见的。
。 在，表示事务仍然活跃，或者在当前事务生成 ReadView 之后才开始，因此是不可见的。

数据记录是当前事务更改的

trx_id 一 creatro_trx_id

事务已经提交

trx_id < min_trx_id

该事务是在ReckView生成后才开启的

trx_id > max_trx_id

事务已经被提交

jn_trx_id 三 trx_id 三 max_trx_jid

举个实际的例子。

读事务开启了一个 ReadView，这个 ReadView 里面记录了当前活跃事务的 ID 列表 (444、555、665) ，以及最
小事务 ID (444) 和最大事务 ID (666) 。当然还有自己的事务 ID 520，也就是 creator_trx_id。

它要读的这行数据的写事务 ID 是 x，也就是 DB_TRX_ID 。
。 如果x= 110，显然在 ReadView 生成之前就提交了，所以这行数据是可见的。

No. 2541 302




## 第 255 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

。 如果x = 667，显然是未知世界，所以这行数据对读操作是不可见的。

。 如果x= 519，虽然 519 大于 444 小于 666，但是 519 不在活跃事务列表里，所以这行数据是可见的。因为
519 是在 520 生成 ReadVview 之前就提交了。

。 如果x= 555，虽然 555 大于 444 小于 666，但是 555 在活跃事务列表里，所以这行数据是不可见的。因为
555 不确定有没有提交。

可重复读和读已提交在 ReadView 上的区别是什么?
可重复读: 在第一次读取数据时生成一个 ReadView，这个 ReadView 会一直保持到事务结束，这样可以保证在事
务中多次读取同一行数据时，读取到的数据是一致的。

Read Commited

select* from tbl_xXxxX Where id = xxx 一   [see |

select* from tbL_xox where id = xoox  本             ReadView

|
|

Repeated Read

|  select * from tbl_xxx Where id = XXX                                       ReadView

select * from tbl_XxxXx Where id = XXX

读已提交: 每次读取数据前都生成一个 ReadView，这样就能保证每次读取的数据都是最新的。
推荐阅读: 搞懂Mysql之InnoDB MVCC

No. 2551 302




## 第 256 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

如果两个 AB 事务并发修改一个变量，那么 A 读到的值是什么，怎么分析。

事务 A 在读取时是否能读到事务 B 的修改，取决于A 是快照读还是当前读。如果是快照读，InnoDB 会使用
MVCC 的 ReadView 判断记录版本是否可见，若事务 B 尚未提交或在 A 的视图不可见，则 A 会读到旧值; 如果是
当前读，则需要加锁，若 B 已提交可直接读取，否则 A 会阻塞直到 B 结束。

1. Java 面试指南 (付费)_收录的美团面经同学 2 java 后端技术一面面试原题: 说说 MVCC，解决了什么

问题?
2. Java 面试指南 (付费) 收录的小公司面经合集同学 1 java 后端面试原题: 了解的 MVCC 吗?

3. Java 面试指南 (付费) 收录的联想面经同学 7 面试原题: Mysql 四个隔离级别，MVCC 实现，如果两个
AB事务并发修改一个变量，那么A读到的值是什么，怎么分析，快照读的原理，读已提交和可重复读区
别，具体原理是什么。

4. java 面试指南 (付费) 收录的oppo 面经同学 8 后端开发秋招一面面试原题: 讲讲Mysql的MVCC机制

5. Java 面试指南 (付费) 收录的快手同学 2 一面面试原题: 事务隔离级别? MVCC机制介绍下? (版本
链) 版本链通过什么控制

6. Java 面试指南 (付费) 收录的美团面经同学 15 点评后端技术面试原题: 问了一下mysql的锁和MVCC
memo: 2025年4月19 日修改至此，今天有球友发帖说拿到了拼多多的 offer，这下真的是圆满了。

二哥! 拼多多 offer收到了!

之前信息采集时写的重中有芋日到岗，不知道现在
还能不能拖一拖转 想在7月初去，因为写简历会
方便些，正好到和Te .= "上昌，拼多多也能写
7-9月图

09:06
5
7本 “和
高可用
66.MySQL数据库读写分离了解吗?

读写分离就是把"写操作"交给主库处理,“读操作"分给多个从库处理，从而提升系统并发性能。

No. 2561302




## 第 257 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

于抽
|二
主库

司

从库

应用层通过中间件 (如 MyCat、ShardingSphere) 自动路由请求，将INSERT /UPDATE / DELETE 等写操作发送
给主库，将 SELECT 查询操作发送给从库。

// 示例: Java中通过不同数据源切换

Transactional

public void updateorder(Order order) {
masterDataSource.update(order); // 写操作走主库

】}

public order getorderById(Long id) {
return slaveDataSource.query(id); // 读操作走从库
】}

No. 2571 302




## 第 258 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

主库将数据变更通过 binlog 同步到从库，从而保持数据一致性。

主库 dump_thread 线程通过 TCP 将 binlog 推送给从库，从库 io_thread 线程，接收主库 binlog，写入 relay
log，从库 sql_thread 线程读取 relay log，并顺序执行 SQL 语句，更新从库数据。

67.读写分离的实现方式有哪些?

实现读写分离有三种方式: 最简单的是在应用层手动控制主从数据源，适用于小型项目，

No. 258 1 302




## 第 259 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

国
从库
读
和和民
写                       ED 为市
数据访问层                                                                             国
主库
读
业务服务器

从库

中等项目是通过 Spring + 多数据源插件、AOP 注解自动路由;
大型系统通常使用中间件，如 ShardingSphere、MyCat，支持自动路由、负载均衡、故障转移等功能。

No. 2591302




## 第 260 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

一
和

写
数据库中间件                    读

Mycat 的读写分离功能依赖于 MySQL 的主从复制架构:
。 writeHost: 表示主节点，负责处理所有的 DML SQL 语句，如 INSERT、UPDATE 和 DELETE。
。 readHost': 表示从节点，负责处理查询 SQL 语句 (如 SELECT) ，以实现读写分离。

正常情况下，Mycat 会将第一个配置的 writeHost 作为默认的写节点。所有的 DML SQL 语句会被发送到此默认写
节点执行。

No. 2601302




## 第 261 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

datahost

写节点完成数据写入后，通过 MySQL 的主从复制机制，将数据同步到所有从节点，确保主从数据一致性。

68.主从复制原理了解吗?

MySQL 的主从复制是一种数据同步机制，用于将数据从主数据库复制到一个或多个从数据库。

主库执行事务提交时，将数据变更以事件形式记录到 Binlog。从库通过 /O 线程从主库的 Binlog 中读取变更事
件，并将这些事件写入到本地的中继日志文件中，SQL 线程会实时监控中继日志的内容，按顺序读取并执行这些事
件，从而保证从库与主库数据一致

1. java 面试指南 (付费) 收录的腾讯云智面经同学 16 一面面试原题: MySQL 的主从复制过程

No. 2611 302




## 第 262 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

69.主从同步延迟怎么处理?

主从同步延迟是因为从库需要先接收 binlog，再执行 SQL 才能同步主库数据，在高并发写或网络拌动时容易出现
延迟，导致读写不一致。

第一种解决方案: 对一致性要求高的查询 (如支付结果查询) 可以直接走主库。

// 伪代码示例
Public Object query(String sql) {
if(isWriteouery(sq1) || needStrongConsistency(sql)) {
return masterDataSource.query(sql) 17
} else {
return slaveDataSource.query(sql);

】}

第二种解决方案: 对于非关键业务允许短暂数据不一致，可以提示用户“数据同步中，请稍后刷新"，然后借助异步
通知机制蔡代实时查询。

// 伪代码示例
Public Object query(String sql) {
if(isWriteOuery(sql)) {
return masterDataSource.query(sql) 17
} else {
// 异步通知用户数据已更新
notifyUser( "数据同步中，请稍后刷新")

return slaveDataSource.query(sdql) 7

第三种解决方案: 采用半同步复制，主库在事务提交时，要等至少一个从库确认收到 binlog (但不要求执行完
成) ，才算提交成功。

No. 2621302




## 第 263 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

半同步复制 :
等待一个slave写完relay log

master

了
RARRRRRIRRARRRRRRREER

请说说半同步复制的流程?
第一步，主库安装半同步插件:

INSTRALL PLUGIN rp1_semi_sync_master SONRAME 'semisync_master.so';
第二步，主库启用半同步复制并设置超时时间:

SET GLOBAL rpl_semi_sync_master_enabled = 17

SET GLOBAL rpl_semi_sync_master_timeout = 10000)
主库 my.cnf 配置示例:

[mysqld]

Plugin-load = "rpl_semi_sync_master=semisync_master.so"

rp1_semi_sync_master_enabled = 1
rp1_semi_sync_master_timeout = 10000
## MYySOL 5.7+建议使用无损模式

rp1_semi_sync_master_wait_point = RFTER_SYNC

第三步，从库安装半同步插件:

INSTRALL PLUGIN rp1_semi_sync_slave SONRME 'semisync_slave.so'
第四步，从库启用半同步复制 :

SET GLOBAL rpl_semi_sync_slave_enabled = 1;

No. 2631302




## 第 264 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

从库 my.cnf 配置示例:
[mysqld]
plugin-load = "rpl_semi_sync_slave=semisync_slave.so"

rp1_semi_sync_slave_enabled = 1

memo: 2025年4月 20 日修改至此，今天给球友修改简历时，碰到有球友说，把星球安利给了同门，进来后都
说好，口碑+1，很欣慰呢。

回复: 星球编5m 恒节= 刚: 呈-简历v3 口 己 加下 名安全浏览模式~                  精简信息人
发件人:于葬六本可:isLi4517

收件人: (多 沉默王二<www.qing_gee@163.com> 十

@qq.com> +

时 间: 2025年04月18日 23:16 (星期五)
附 件: 1个(国诗地旺门).pdf ) 查看附件

二哥好。这是我的第三版简历，主要是增加了实习经历，这个部分有一点拿不准，想让二哥帮有我把控一下。这一个多月基本
没闲着就疯狂学组里核心代码，然后有活的时候就争取能够写好。.鲜 和组里的人都很好，很乐意教，但是自己还是藏了一
个大厂梦，可能还是会g哈哈哈，还是很想挑战一下。不过还是很感谢二哥的付出，无论是星球项目还是交流群都让我学到不
少。安利了两个同门进来星球都说好hhh 。

70.二你们一般是怎么分库的呢?

分库的策略有两种，第一种是垂直分库: 按照业务模块将不同的表拆分到不同的库中，比如说用户、登录、权限等
表放在用户库中，商品、分类、库存放在商品库中，优惠券、满减、秒杀放在活动库中。

No. 264 1 302




## 第 265 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

加
加

第二种是水平分库: 按照一定的策略将一个表中的数据拆分到多个库中，比如哈希分片和范围分片，对用户 id 进
行取模运算或者范围划分，将数据分散到不同的库中。

No. 2651 302




## 第 266 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

贴一段使用 ShardingSphere 的inline 算法定义分片规则:

rules:
- !SHARDING
tables:
order:
actualDataNodes: db _${0..3}.order_${0..15)}
databaseStrategy:
standard:
shardingColumn: user_id
shardingRlgorithmName: db_hash mod
tableStrategy:
standard:
shardingCcolumn: order_ time
shardingRlgorithmName: table_interval_yearly
shardingRlgorithms :

db_hash_mod:
type: HRASH_MOD
props:
sharding-count: 4
table_interval_yearly:
type: INTERVRL
props:
datetime-pattern: 'yYyy-MM-dd HH:mm:ss
datetime-lower: '2024-01-01 00:00:00'
datetime-upper: '2025-01-01 00:00:00'
sharding-suffix-pattern: “yyyY'，

datetime-interval-amount: 1

No. 2661302




## 第 267 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

datetime-interval-unit: "Years

1. Java 面试指南(付费) 收录的快手面经同学 7java 后端技术一面面试原题: 分库分表了解吧
2. Java 面试指南付费) 收录的华为面经同学 8 技术二面面试原题: 说说分库分表的准则
71.二那你们是怎么分表的?

当单表超过 500 万条数据，就可以考虑水平分表了。比如说我们可以将文章表拆分成多个表，如 article_0、
article 9999、article_19999 等。

重直拆分

ID            name           age             Sex        nickname 。” desc

1

2

水平拆分                                                               >

999999
1000000
999999

了
在技术派实战项目中，我们将文章的基本信息和内容详情做了垂直分表处理，因为文章的内容会占用比较大的空

间，在只需要查看文章基本信息时把文章详情也带出来的话，就会占用更多的网络 IO 和内存导致查询变慢;而文
章的基本信息，如标题、作者、状态等信息占用的空间较小，很适合不需要查询文章详情的场景。

No. 2671 302




## 第 268 页


效MySQL篇V2-让天下所有的面渣都能逆袭

init_schema_221209.sql X

CREATE TABLE“

、id         int unsigned NOT NULL AUTO_INCREMENT COMMENT "主键ID'，
”user_id     int unsigned NOT NULL DEFAULT '9，COMMENT '用户ID
"articte_type”tinyint    NOT NULL DEFAULT '1' COMMENT '文章类型: 1-博文，2-问答'，
"titite      varchar(    NOT NULL DEFAULT '， COMMENT 文章标题'，
`short_titte” varchar(    NOT NULL DEFAULT '， COMMENT “短标题
"picture'”    varchar(    NOT NULL DEFAULT '， COMMENT “文章头图'，
summary    varchar(    NOT NULL DEFAULT '， COMMENT 文章摘要'，
"category_id`” int unsigned NOT NULL DEFAULT '9，COMMENT '类目ID
"source'     tinyint    NOT NULL DEFAULT '1，COMMENT       ，2-原创，3-翻译'，
"source_urt ”varchar(128) NOT NULL DEFAULT '1' COMMENT
”officat_stat ”int unsigned NOT NULL DEFAULT '9，COMMENT '官广    9-非官方，1-官方"，
"topping_stat ”int unsigned NOT NULL DEFAULT '9， COMMENT     态: 9-不置顶，1-置顶'，
"cream_stat” int unsigned NOT NULL DEFAULT '9，COMMENT '加精状态: 9-不加精，1-加精'，
status、      tinyint     NOT NULL DEFAULT '9，COMMENT
"deteted      tinyint     NOT NULL DEFAULT “9， COMMENT
"create_time” timestamp 。 NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT “创建时间'，
"update_time`” timestamp   NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT “最后更新时间'，
PRIMARY KEY (`id`)，
KEY       `idx_category_id” (category_id )，
KEY、idx_titte”(titte`)
KEY “idx_short_titte”(`short_titte'`)

ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='文章表

)
)
)
)

CREATE TABLE“

id         int unsigned NOT NULL AUTO_INCREMENT COMMENT ,主键ID，
articte_id” int unsigned NOT NULL DEFAULT "9，COMMENT "文章ID'，
version    int unsigned NOT NULL DEFAULT “9'， COMMENT “版本号'，
`“content    Longtext COMMENT “文章内容'，
"deteted    tinyint ”NOT NULL DEFAULT “9， COMMENT ,是否删除'，
"create_time”timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT “创建时间，，
”update_time”timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT ,最后更新时间'，
PRIMARY KEY (`id`)，
UNIQUE KEY `idx_articte_version” (articte_id' ，version )
ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COMMEN

1.                       收录的快手面经同学                               分库分表了解
2.                       收录的华                 二面面试原题:      分库分表的准则
3.                     收录的腾讯面经同学 29 java 后端一面原       满了之后怎么扩表?

72.水平分库分表的分片策略有哪几种?
常见的分片策略有三种，范围分片、Hash 分片和路由分片。
分片是根据某个字段的值范围进行水平拆分。适用于分片键具有连续性的场景。

No. 268 1 302




## 第 269 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

范围路由

原始大表

比如说将 user_id 作为分片键:

。 1-~10000一db1.user_1
。 10001~ 20000 一 db2.user_2

Hash 分片是指通过对分片键的值进行哈希取模，将数据均匀分布到多个库表中，适用于分片键具有离散性的场

曙
景。

哈希路由

比如说我们一开始规划好了 4 个表，那么就可以简单地通过取模来实现分表:

No. 2691302




## 第 270 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Public String getTableNameByHash(long userId) {
int tableIndex = (int) (userId s 4) 7
return "user_ ”+ tableIndex7

)}

路由分片是通过路由配置来确定数据应该存储在哪个库表，适用于分片键不规律的场景。

配置路由

比如说我们可以通过 order_router 表来确定订单数据存储在哪个表中:

order id                                                                          table _id
XXXX                                                                     table_1
yyyy                                                                     table_2
ZZZZ                                                                      table_3

1. Java 面试指南 (付费) 收录的腾讯面经同学 24 面试原题: 项目中的水平分表是怎么做的? 分片键具体

是怎么设置的?
2. java 面试指南 (付费) 收录的腾讯面经同学 29 java 后端一面原题: 分库分表具体的分片策略是怎么做
的?

memo: 2025年4月22 日修改至此，今天给辣到蚂蚁暑期实习的球友发了个红包，感谢他在星球的经验贴，这
些精华帖也会帮助到下一届的球友们，真的非常感谢。

音后开重2 21 丙坟归语章和玉生百人
eer，3.3入联、并双坦二前本为再实

本 两大站

No. 2701 302




## 第 271 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

二哥，之前的面经已经发在星球上
啦，能奖励个小红包嘛意

14:02

会
恭喜上发财，大吉大利      区

oa
四

提
虽

谢谢二哥，会继续努力的，身边有
相关的同学，也在建议他们来星
球!




## 第 272 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

图 .领取了你的红包
73.不停机扩容怎么实现?

第一个阶段: 新旧库同时写入，确保数据实时同步;可以借助消息队列实现异步补偿，畦等避免重复写入。读操作
仍然走旧库。

 ，        数据同步和校验

代码参考:

eTransactional

public void createOrder(Order order) {
oldpB.insert(order);  // 写入旧库
newDB.insert(order);  // 写入新扩容节点
kafka.send("data_sync"，order);  // 异步补偿通道

)}

第二个阶段，通过 Canal 或者自研脚本将旧库的历史数据同步到新库。关键业务在查询时同时查询新旧库，进行数
据校输，确保一致性。

No. 272 1 302




## 第 273 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Public List<Order> getOrders(Long userId) {
List<Order> orders = newDB.getOrders(userId))
List<Order> oldorders = oldDB.getOrders(userId) 1;
if (!orders.equals(oldorders)) {

// 数据不一致，进行补偿

kafka.send("data_sync"，oldorders))

第三个阶段，在确认新库数据一致性后，逐步将读请求切换到新库，然后下线旧库。

74.常用的分库分表中间件有了哪些?

常用的分库分表中间件有 ShardingSphere 和 Mycat。

修、SshardingSphere 最初由当当开源，后来贡献给了 Apache，其子项目 Sharding-JDBC 主要在java 的JDBC 层
提供额外的服务。无需额外部署和依赖，可理解为增强版的JDBC 驱动，完全兼容JDBC 和各种 ORM 框架。

No. 273 1 302




## 第 274 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

@@、Mycat 是由阿里巴巴的一款产品 Cobar 衍生而来，可以把它看作一个数据库代理。

PE;Ta，

剖册并光

No. 274 1 302





## 第 275 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

推荐阅读: mycat 介绍

75.你觉得分库分表会带来什么问题呢?

第一，跨库事务无法依赖单机 MySQL 的 ACID 特性，需要使用分布式事务解决方案，如 Seata 的 AT 模式、TCC
模式等。

口           全pmHub分布式事务Seata保证任务市批态到性 【上必看)                  四全8网 纯

国 来人offerpmhub 避           1                       站           一
和      男                                                                                              本
轴                                         和

和 首页                                        <                                                                       7
EEC2                                             分布式事务
蕊 上         G :                                                                    分布式事务角六案
pmHubmRRedislnlua                 整体机制                                                                                                                                                  -seata 人绍
proayitWin ao                                                                                                                                          上。 se是f么
Seata 支持 3 各模式，AT 模式、TCC 模式、Saga 模式                                                        可机制
人pmHub生记 sentnel0                                                                                                                                                  人
pmHub分布式事务Seata                                                                                                    日        Toc 机
onuranvuomdx、 “ER     oo
上       AT模式              自动补偿事务，通过代理自动管 易于使用，开发成本低，自动管 。 依灯     1 Seata
机                                   理事务的提交和回滚，适合简单 理事务               灵        T和
产品计和                                                                      场最                                                                                          建寻表
加人放量全       Tcc 各式              Tm-confim_Cancel，开发者 。 提供强一致性，适用于需要严格 。 实现       2
pmHub 天分析及可行                                                    手动实现业务运输的 Try、           事务管理的场景                     动管               机
一                                                                  -pmHub 交战 沽加任务事务管理
pmHub 项目和理半                          confim 和 Cancel 三个阶段
坝的-人                                                                           业务库添加undo_log 表
PHub 产品开设计                                                                                                                                                                    pmhub-_project 添加信和
nn                         Saga 模式                          长事务模式，通过一系列的子事。 无需全局锁，高性能，适用于长 。 需要               本时文件 pmhub_project_dev
本                                                              务来完成主事务，子事务之间独 。 事务场景                            证强               接口添加 @QGlobalTransactional
pmHub 可全 Nacos实                         立运全”加果昌个了事务中。                              机
pmHub 可人 Gateway                                                     则通过补偿事务进行回深                                                                 PmHub 实版-审批太新建/更
pmHub吾人 sentnel实                                                                                                                                             -pmHub 实版Seata 实测这3

图pmHub 吾人openFeion                                                                                                                                                 服务启动

四                                                                                         正党下各任条情形

第二，跨库后无法使用JOIN 联表查询。可以在业务层进行拼接，或者把需要联表查询的数据放到 Es 中。

// Java 代码示例
User user = userService.getUserById(1);
List<Order> orders = orderService.getOrdersByUserId(1);

第三，自增1D 在分片场景下容易冲突，需要使用全局唯一方案。

数据库表被切分后，不能再依赖数据库自身的主键生成机制，所以需要一些手段来保证全局主键唯一。比如说雪花
算法、京东的JD-hotkey。

No. 2751 302




## 第 276 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

Dashboard控制台
1查看各实例和各worker状;
2 查看、修改热key规则配置信息
3 音看各维度统计信息，如热key频 | | 。 mysql
PP      届                   率、已级存的数量
证生起天用光eny近放中            4 将需要持久化的数据，存和mysql
旨在基于突发热key状况，解决热点数
所时到存储导者难是
可在0.5-2秒内将扫数据，如redis热
key、时名单用户、相前接口、热接
口近测出来，并推送到JVM内
直接将扫数所在server居内存进行有
存，极大地减少对下游服务、redis、
mysql等的冲击。
各worker上报自己信息到
ETCD，并维持心跳
(save
docker1
分布式计简集
Sm)             9
单机QPS按16万
计算，根据每秒
1 拉职并监听各Worker的jp及变更                                         待测key族量来设
服务计各个实例              信息                                                              秆worker政量。
规模数二到数万                           2 监听热key规则配置变更信息，
来决定上报哪些key                                                      基于滑动窗口计
算 要据
dashboard里配
置的nile规则，进
1建立和各worker的长过                                                      Ce
基于nety

将要探测的key按hash算”一一 |
法，分发到不同的worker进
计算

你们项目中的分布式主键 id 是怎么生成的?

在技术派项目中，我们在雪花算法的基础上实现了一套自定义的 ID 生成方案，通过更改时间截单位、ID 长度、
workld 与 dataCenterld 的分配比例，ID 生成的延迟降低了 20%; 满足了分布式环境下 ID 的唯一性。

No. 276 1 302




## 第 277 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

国 nacoune ”man

Project

ngforum core

dExecutor((Runnabte m) ->{

雪花算法具体是怎么实现的?
雪花算法是 Twitter 开源的分布式 ID 生成算法，其核心思想是: 使用一个 64 位的数字来作为全局唯一ID。
。 第 1 位是符号位，永远是 0，表示正数。
。 接下来的 41 位是时间戳，记录的是当前时间戳减去一个固定的开始时间改，可以使用 69 年。
。 然后是 10 位的工作机器 ID。
。 最后是 12 位的序列号，每毫秒最多可生成 4096个ID。

No. 2771 302




## 第 278 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

加 ，个NoiR庄                回自定义雪花算法生成业务ID @@
血 技术二 e                       则、不规则。
十
和[首页                      1.2. 雪花算法
目录        人 :=
加技术派设计模式之抽象设.       雪花算法可以说是业界内生成全局唯一id的经典算法，其基本原理也比较简单
加技术派本地耗时性能优化
加技术派数据统计PV/UV
回自定义雪花算法生成业务ID                                      半
3
加技术派付费阅读方案设计，，
Snowfiake雪花生法
加技术派集成短信支付【出
加技术派向信支付解锁付费.                是高位        时间枉条秒)          机器标识         自于序列
加技术派束合WebSocket
1ok                      br                           ob                     1

加技术派整合 FastExcel

技术派MongoDB实现计数
技术派多数据源配置
~前端篇
加技术派图片背景色动态变更              Snowflake 以 64 bit 来存储组成 ID 的4 个部分:
加技术派Thymeleaf模板引擎
加技术派如何泻染 markdo,                1. 最高位占1 bit，值固定为 0，以保证生成的 ID 为正数;

2. 中位占 41 bit，值为毫秒级时间戳;
3. 中下位占 10 bit，值为机器标识id，值的上限为 1024;

加技术派中长整型精度丢失，

大致的实现代码如下所示:

public class SnowflakeIdGenerator {
private long datacenterId = 1L; // 数据中心ID
private long machineId = 1L;) // 机器ID
private long sequence = 0L; // 序列号

Private long lastTimestamp = -1L7

public synchronized long nextId() {
long timestamp = System.currentTimeMillis() 7
if (timestamp == lastTimestamp) {
sequence = (sequence + 1) & 40951;
if (sequence == 0) {
while (timestamp == lastTimestamp) {

timestamp = System.currentTimeMillis()7

}
} else {
sequence = 0;

lastTimestamp = timestamp)

No. 278 1 302




## 第 279 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

return ((timestamp - 1609459200000L) << 22) | (datacenterId << 17) | (machineId
<< 12) | sequence;
}
}

1. Java 面试指南 (付费) 收录的腾讯面经同学 29 java 后端一面原题: id是怎么生成的? (分布式自增主
键)

memo: 2025年4月23 日修改至此，今天有球友反馈说拿到了 vivo 的 offer，也是他第一个暑期实习 offer，真

《             二哥 VIP 10 群(444) CS              ..
志” 沉默王二-二哥: 面渣逆袭并发编程篇 2.0版下载…
|
今天收到vivo 暑期了

后  人

第一个offer

和 95条新消息

上午11:45

牛的，vivo 暑期是不是只有算法啊

No. 279 1 302




## 第 280 页


面渣逆交MySQL篇V2-让天下所有的面渣都能逆袭
运维
76.百万级别以上的数据如何删除?
在处理百万级别的数据删除时，大范围的 DELETE 语句往往会造成锁表时间长、事务日志膨胀等问题。
可以采用批量删除的方案，将删除操作分成多个小批次进行处理。
public void batchDelete(String tableName，String condition，int batchSize) {
// 1. 创建线程池
int threadCount = Runtime.getRuntime() .availableProcessors();

ExecutorService executor = Executors.newFixedThreadPool(threadCount);
CountDownLatch latch = new CountDownLatch(threadCount) 7

// 2 获取总记录数

long totalCount = getTotalCount(tableName，condition)7

// 3 计算每个线程处理的数据量

long perThreadCount = totalCount / threadCount;

// 4. 分配任务给线程池
for (int 研= 0; 1 < threadCount; i++) {

long startId = i * perThreadCount;

long endId = (i == threadCount - 1) ? totalCount : (startId + perThreadCount);
executor.execute(() -> {
try 1{

// 分批次删除数据
for (long j = startId; j < endId; j += batchSize) {
String deletesql = String.format(
”DELETE FROM SS WHERE 8S LIMIT %d"v
tableName，condition，batchSize

) 7

// 执行删除
jdqbcremplate.update(deletesql);
}
} finally {

latch.countDown() 7

)) 7

// 5. 等待所有线程完成
latch.await() 1
executor .shutdown() 7

也可以采用创建新表蔡换原表的方式，把需要保留的数据迁移到新表中，然后删除旧表。
简单的方案:

No. 2801302




## 第 281 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

-- 1. 创建新表结构(包含索引)

CRERTE TARBLE new_table LIKE large_table)

-- 2。 插入需要保留的数据
INSERT INTO new_table
SELECT * FROM Large _table WHERE conditiony

-- 3。 重命名表

RENRME TABLE large_table TO old table，new_table TO large_tablei

-- 4。 删除旧表
DROP TARBLE old_table7

加入检查表空间、分批导入数据、验证数据一致性等步骤:

-- 1. 在执行之前先检查空间是否足够
SELECT table_schemay
table_name，
round(((data_length + index_ length) / 1024 / 1024)，2) “Size in MB"

FROM information_schema.TRBLES
WHERE table_schema = DRATRBRASE( )
RND table_name = 'large table')

-- 2. 创建新表

CRERTE TARBLE new_table LIKE large_table)

-- 3. 分批导入数据(避免一次性导入过多数据)

SET ebatch = 17

SET ebatch_size = 10000;

SET etotal = (SELECT COUNT(*) FROM large_table WHERE condition) 7

REPERT
INSERT INTO new_table
SELECT * FROM Large_table
WHERE condition
LIMIT ebatch_sizey

SET ebatch = ebatch + 17
UNTIL 8@batch * ebatch_size > etotal END REPERAT7

-- 4。 验证数据一致性
SELECT COUNT(* ) FROM new_tabley
SELECT COUNT(*) FROM large_table WHERE conditiony

-- 5. 在业务低峰期执行表切换
RENRAME TRBLE large_table TO old_ table
new_table TO large_table)

-- 5.确认无误后再删除旧表 (建议不要立即删除
-- DROP TRBLE old_table

No. 2811 302




## 第 282 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

77.千万级大表如何添加字段?

在低版本的 MySQL 中，千万级数据量的表中添加字段时，直接使用 ALTER TABLE 命令会导致长时间锁表、甚至
数据库骨溃等。

可以使用 Percona Toolkit 的 ptronline-schema-change 来完成，它通过创建临时表、逐步同步数据并使用触发器
捕获变更来实现。

Pt-online-schema-change --alter "RDD COLUMN new_column datatype"”D=database,t=your_table

--execute

对于 MySQL 8.0+ 版本，可以直接通过 ALTER TABLE 来完成，因为加入了 INSTAN 算法，添加列并不会长时间锁
表。

RALTER TRBLE your_table RDD COLUMN new_column datatypey

如果没有指定 ALGORITHM=INSTANT 算法，MySQL 会先党试INSTANT 算法; 如果无法完成，会切换到INPLACE
算法; 如果仍然无法完成，会尝试 COPY 算法。

Instant DDL has been one of the most requested InnoDB features for avery longtime. With ever
larger and rapidly growing datasets the ability to do DDL instantly is a must have feature in any
web scale database. Developers constantly need to add new columns to meet the constantly
changing business requirements. The ability to add ADD COLUMNSs instantly is the first in a
series of DDL statements that we plan to do instantly. The move to a new transactional data
dictionary in MySQL 8.0 has made this task alot easier for us. Prior to MySQL 8.0 the meta-data
(data dictionary) was stored in flat files called .frm files. The .frm files arein an arcane format
that is long past its use by date.

即时 DDL 一直是 InnoDB 长期以来最受欢迎的功能之一。随着数据集的不断增大和快速增长，能够即

时执行 DDL 是任何网络规模数据库中必备的功能。 开发人员不断需要添加新列以满足不断变化的业务

This INSTANT ADD COLUMN patch was contributed by the Tencent Games DBA Team. We would
like to thank and acknowledge this important and timely contribution by Tencent Games.

这个即时添加列补丁由腾讯游戏 DBA 团队贡献。我们要感谢并承认腾讯游戏的重要和及时的贡献。

78.MySQL 导致 cpu 碳升的话，要怎么处理呢?

我通常先通过 top 命令确认是否是 mysqld 的进程占用。

No. 2821302




## 第 283 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

top

Processes: 868 totaL，2 running，866 stLeeping，5295 threads
: 1.56，2.69，2.77 CPU usage: 1.65% user，2.48% Sys，95.85% idte
haredLibs: 1350M resident，193M data，413M Linkedit .
emRegions: 0 totaL，0B resident，1623M private，216 shared .
PhysMem: 83G used (3842M wired，0B compressor)，45G unused .
M: 401T vsize，5430M framework vsize，0(0) swapins，0(0) swapouts.
etworks: packets: 49249175/55G6 in，38308695/36G out .
bisks: 13446779/4286 read，53453578/1528G written .

ID 。 COMMAND TIME    #TH jpQ #POR MEM  PURG CMPR PGRP PPID STATE   B00STS
和102 mysqtLd    0.1 09:54.17 47 0  72 454M0B 0B 680 680 steeping *0[1]

然后通过 sHow PROcESSLIST 和慢查询日志定位是否存在耗时 SQL，再配合 explain 和 performance_schema
分析 SQL 是否命中索引，是否存在临时表和排序。

-- 使用 EXPLRIN 分析SOL执行计划
EXPLRAIN SELECT * FROM large table WHERE conditiony

-- 查看表的索引使用情况

SHOW INDEX FROM table_name)

-- 查看InnoDB状态
SHOW ENGINE INNODB STATUS

-- 查看表的统计信息

RNRLYZE TRBLE table_namey

最终通过 SQL 优化、加索引、分批操作等手段逐步优化。
memo: 2025 年4月 24日修改至此，今天有球友反馈说拿到了小鹏汽车测试岗的 offer，真的苯喜啦洲:。

哥，小鹏汽车软件测试 base广州"了"有明 管中晚
两顿饭

你觉得咋样

SQL 题

No. 2831302




## 第 284 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

79.一张表: id，name，age，sex，class，sdql1 语句: 所有年龄为 18 的人
的名字? 找到每个班年龄大于 18 有多少人?找到每个班年龄排前两名的
人? (补充)

建议大家在本地建表，实操一下。 2024年 04 月 11 日增补。

第一步，建表:

CRERTE TRBLE students |(
id INT AUTO_INCREMENT PRIMRARY KEY，
name VRARCHRR(50) ，
age INT，
sex CHRAR(1) ，
class VRARCHRAR(50)

第二步，插入数据:

INSERT INTO students (name，age，sex，class) VRLUES

，18， "'女'，      )v
，20，“'男'，
，19， “'男'，      )v
"“，17，“'男"，      )v
，20， '女'，
，21，“'男'，
，18， '女'，     0

所有年龄为 18 的人的名字?
SELECT name FROM students WHERE age = 18;

这条 SQL 语句从表中选择 age 等于 18 的所有记录，并返回这些记录的 name 字段。

mySsqL> SELECT name FROM students WHERE age = 18;

沉默王二
沉默王七

2 rows in set (0.00 Sec )

如果可以的话，可以给 age 字段加上索引。

No. 2841302




## 第 285 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

students          age_index (age) 7
找到每个班年龄大于 18 有多少人?

class，           (x)       number_of_ students
Students
age > 18

classi

这条 SQL 语句先筛选出年龄大于 18 的记录，然后按 class 分组，并通过 count 统计每个班的学生数。

SELECT cLass，COUNT(*) AS number_of_students
FROM Students

WHERE age > 18

GROUP BY ctLass;

rows in set (0.00 sec)

找到每个班年龄排前两名的人?
这个查询稍微复杂一些，需要使用子查询和去重 DISTINcT 。

己    日    ，忆
students
(
(       Pb
Students b
b      = 昌         Pb    > 忆

忆       已           7

这条 SQL 语句首先从 students 表中选择 class 、 name 和 age 字段，然后使用子查询计算每个班级中年龄排前两
名的学生。

No. 2851 302




## 第 286 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

SELECT a.CLass，a.name，a.age
FROM students a
WHERE (人
SELECT COUNT(DISTINCT b.age)
FROM students
WHERE b.cLass = a.CLass AND b.age > a.age
) < 2
ORDER BY a.cLass，

name，age，

|每个班年

龄排前两

80.有一个查询需求，MySQL 中有两个表，一个表 1000W 数据，另一个表
只有几和王数据，要做一个关联查询，如何优化

第一步，为关联字段建立索引，确保 on 连接的字段都有索引。

big_table                 idx_small_ id(small id))
第二步，小表驱动大表，将小表放在 JOIN 的左边 (驱动表) ，大表放在右边。

加     small_table s
big_table b ON s.id = b

有一个查询需求，MySQL 中有
询，如何优化

No. 2861302




## 第 287 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

81.新建一个表结构，创建索引，将百万或千万级的数据使用 insert 导入该
表，新建一个表结构，将百万或千万级的数据使用 isnert 导入该表，再创建
索引，这两种效率哪个高呢? 或者说用时短呢?

先说结论:
在大数据量导入场景下，先导入数据，后建索引的效率显著高于先建索引，后导入数据的效率。
来，实操。

先创建一个表，然后创建索引，执行插入语句，来看看执行时间 (100 万数据在我本机上执行时间比较长，我们就
用 10 万条数据来测试) 。

CRERTE TRBLE test_table (
id BIGINT RUTO_INCREMENT PRIMRARY KEY，
name VRARCHRAR(255) NOT NULL，
emai1l VARCHAR(255) NOT NULL，
created_at DRTETIME NOT NULL
)
CRERTE INDEX idx_name ON test_tablelname) 7
DELIMITER //

CRERTE PROCEDURE insert_datal)
BEGIN
DECLRRE i INT DEFRAULT 07

WHILE 1 < 1000000 DO
INSERT INTO test_tablelname，email，created_at)

VRLUES (CONCRT('wanger',i)，CONCRT('email'，i， "eexample.com')，NOW()) 7
SET i=i+l;
END WHILE7
END //
DELIMITER )

CRLL insert_datal()7

总的时间 13.93+0.01+0.01+0.01=13.96 秒。

信息
Query                                                          Message
CREATE TABLE test_table (                                  OK, Time: 0.01sec
CREATE INDEX idx_name ON test_table(name)            OK, Time: 0.01sec
CREATE PROCEDURE insert_data()                          OK, Time: 0.01sec
CALL insert_datal()                                          OK, Time: 13.93sec

接下来，我们再创建一个表，执行插入操作，然后创建索引。

No. 2871 302




## 第 288 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

CRERTE TRBLE test_table_no_index |(
id BIGINT RUTO_INCREMENT PRIMRARY KEY，
name VRARCHRAR(255) NOT NULL，
emai1l VARCHAR(255) NOT NULL，
created_at DRTETIME NOT NULL

)

DELIMITER //

CRERTE PROCEDURE insert_data_no_index()
BEGIN
DECLRRE i INT DEFRAULT 07

WHILE 1 < 1000000 DO
INSERT INTO test_table_no_index(name，email，created_at)

VRLUES (CONCRT('wanger'，i)，CONCRT('email'，i， "eexample.com')，NOW()) 7
SET i=i+l;
END WHILE7
END //
DELIMITER )

CRLL insert_data_no_index() 7
CRERTE INDEX idx_name_no_index ON test_table_no_index(name) 7

来看一下总的时间，0.01+0.00+13.08+0.18=13.27 秒。

言息
Query                                                            Message
CREATE TABLE test_table_no_index (                        OK, Time: 0.01sec
CREATE PROCEDURE insert_data_no_index()              OK, Time: 0.00sec
CALL insert_data_no_index()                                OK, Time: 13.08sec
CREATE INDEX idx_name_no_index ON test_table_no. OK, Time: 0.18sec

先插入数据再创建索引的方式比先创建索引再插入数据要快一点。
然后时间差距很微小，主要是因为我们插入的数据少。说一下差别。
。 先插入数据再创建索引: 在没有索引的情况下插入数据，数据库不需要在每次插入时更新索引。

。 先创建索引再插入数据: 数据库需要在每次插入新记录时维护索引结构，随着数据量的增加，索引的维护会

导致额外的性能开销。

MySQL是先建立索引好还是先插入数据好?

如果是小批量插入，可以先建索引;但在大数据量数据导入场景下，推荐先插入数据再建索引。
因为索引是基于 B+ 树的，大量插入时如果提前建索引，会频繁触发页分裂和索引结构调整，影响性能。
插入完成后统一构建索引，MySQL 会按顺序批量生成索引结构，速度更快、资源消耗更低。

No. 288 1302




## 第 289 页


面尖逆区MySQL篇V2-让天下所有的面洁都能逆装
1. java 面试指南 (付费) 收录的农业银行面经同学 7java 后端面试原题: 数据库是先建立索引还是先插
入数据

memo: 2025年4月25 日修改至此，今天有家长发来感谢信，说孩子在加入星球后，整个人明显变得更加积极
了。说真的，家长的认可，更让我感到虚荣心得到了极大的满足。

老师您好，今天孩子和我通话语气都精神起来
了，她说感到有伴了，有老师带着一个群体在
学，学员也可以互相交流，老师对她挺好，自己
很开心，谢谢老师的帮助，您费心了，感谢感谢
会会全

进入四月以来，孩子情绪低落又焦虑，因为自己
没学完，压力很大，实习又开始投递，自己还没
开始，感到很难很无助，有时交流不畅都把我屏
融了，自己周边同学又不学这个，自己一个人孤
独的在学，课余每晚四个小时的在学，现在好了
和大家一起，就不会那么无助了，遇到您真的是

太好了! 再次感谢!
pw，

下 : 老师您好，今天孩子和我通话语气都精神起来
了，她说感到有伴了，有老师带着一个群体在学，… >

82.什么是深分页，select* from tbn limit 1000000000 这个有什么问
题，如果表大或者表小分别什么问题

No. 2891302




## 第 290 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

深分页是指在 MySQL 中获取比较靠后的数据页，比如第 1000 页、第 10000 页等。特别是使用 ZIMIT
offset,count 这种方式，当 offset 特别大，就会带来严重的性能问题。

对于 SELECT * FROM tbn LIMIT 1000000,10 ，这样的查询语句来说，MySQL会:

。 从表中读取第一条记录，判断是否满足 where 条件; 如果满足，计数器+1; 否则直到 计数器累计到
1000000 时才开始真正取数据
。 再继续获取 10 条数据，返回

性能会非常差，因为需要从头扫描，无法利用索引优化，并且需要抛弃大量不需要的数据，占用大量的内存和 CPU

可以借助主键索引分页进行优化:
SELECT * FROM tbn

WHERE id > (SELECT id FROM tbn ORDER BY id LIMIT 1000000，1)
LIMIT 10

或者记住上次分页的最大 ID，然后再查询:

SELECT * FROM tbn
WHERE id > last_page_max_ id
LIMIT 10

1. java 面试指南 (付费) 收录的字节跳动面经同学 13 java 后端二面面试原题: 什么是深分页，select *
from tbn limit 1000000000 这个有什么问题，如果表大或者表小分别什么问题

83.SQL 题: 一个学生成绩表，字段有学生姓名、班级、成绩，求各班前十
名

第一步，建表:

CRERTE TRBLE student_scores |
student_name VRARCHRR(100) ，
class VRARCHRAR(50)，
score INT

)
第二步，插入数据:

INSERT INTO student_scores (student_name，class，score) VALUES

( "沉默王二' ，       ，88)，
( "沉默王三'，       ，92)，
( "沉默王四'，       ，87)，
( "沉默王五 ，       ，85)，
( "沉默王六'，       90)，
( "沉默王七'，       ，95)，
( "沉默王八'，       ，82)，
( "沉默王九'，       ，78)，

No. 2901302




## 第 291 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

( "沉默王十三
( "沉默王十四'，
( "沉默王十五'，
( "沉默王十六'，
( "沉默王十七'，
( "沉默王十八'，
( "沉默王十九'，
( "沉默王二十'，
( "沉默王二十一'，

第三步，查询各班前十名。如果 MySQL 是 8.0 以下版本，不支持窗口函数，可以通过在查询中维护班级当前处理
状态和排名，实现分组内按成绩排序并打标号，再取前十名。

SET ecur class = NULL，ecur_rank = 0;

SELECT student_name，class，score
FROM 1(
SELECT
student_namey
class，

scorey

ecur_rank := IF(ecur _ class = class，ecur rank + 1，1) RS ranky

ecur_class := class
FROM student_scores
ORDER BY class，score DESC
) RS ranked
WHERE ranked.rank <= 107

步骤                              解释

@cur_class 变量                                            记录当前正在处理的班级

@cur_rank 变量                          记录当前班级的排名，默认0

IF(ecur_class = class，ecur_rank +     如果班级没变，就排名 +1; 如果换了新班级，排名从 1 重
1，1)                        新开始

ecur_class := class               更新当前班级变量，保持班级变化跟踪

必须先按班级升序、成绩降序排好，才能保证变量正确打
排名

ORDER BY class，score DESC

外层 waERE rank <= 10                 只取每班前十名加

No. 2911 302




## 第 292 页


mysqL> SET Gcur_class = NULL，Gcur_ran
Query 0K，0 rows affected (0.00 sec)

mysqL>
mySsqL> SELECT student_name，cLass，Sscore
FROM (
SELECT
student_name，
CLass，
score，
Gcur_rank      F(Gcur_ctLass   cLass，G@cur_rank + 1，1) AS rank，
Gcur_ctLass    CLass
FROM student_scores
ORDER BY ctLass，Sscore DESC
-> ) AS ranked
-> WHERE ranked.rank

如果是 MySQL 8.0+ 版本，可以使用窗口函数来完成:

SELECT student_name，class，score

4
SELECT
student_namey
class，
scorey
ROW_NUMBER( ) OVER (PARTITION BY class ORDER BY score DESC) RS rn

FROM student_scores

S tmp
WHERE rn    10;

No. 2921 302




## 第 293 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

SQL 用到的技术                                                                说明

ROW_NUMBER() OVER (PRRTITION BY class ORDER BY score

给每个班独立打排名，从 1 开始

DESC)

子查询 tmp                                              用来临时生成带有 rn (排名) 的数
据集

外层 wagRE rn <= 10                                   选出每个班排名前 10 的学生

ORDER BY score DESC                                成绩高排前面，符合常规排名逻辑

mysqL> SELECT student_name，CcCLass，Sscore
-> FROM (
SELECT
student_name，
CLass，
score，
ROW_NUMBER( ) OVER (PARTITION BY ctLass ORDER BY score DESC) AS rn
FROM student_scores
-> ) AS tmp
-> WHERE rn <= 10;

机机册册册册册册骨骨

1                 收

学生姓名、班级、成绩，求各班前十名

memo: 2025年4月26 日修改至此，今天有:                ，说他拿到了蚂蚁国际的 offer，并且多次感谢
星球对他实习的帮助，比身边朋友拿到了更多的面试机会，并且准备阶段只看二哥的专栏，都有一种精神洁癖了，
说实话，这种喜报我真的爱看，优 。

No. 2931302




## 第 294 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

【星球三5利上.录用喜报】 感谢二哥!       D 时 ， 外 安全浏览模式~             oo 优化阅读 | 精简信息
发件人: 帝<1307d42UULUGqq.com>
收件人: (所 www.qing_gee<www.qing_gee@163.com>

时 间: 2025年04月24日 23:14 (星期四)
【升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

感谢二哥! 先说结果! 拿到了蚂蚁国际的offer base杭州，接下来煽煽情聊聊心路历程。

经过两个月的靡战，终于顺利赶在银四的尾巴把offer拿到了，感觉一路走过来虽然从未跟二哥谋面，但是没有二哥的Pmhub
和面渣我是绝对不可能拿到offer的，再次感谢二哥的内容，加入二哥的星球感觉是我找实习阶段花的最值得的一笔钱，顺利
让我在一众外卖中脱颖而出，拿到了比身边朋友更多的面试机会。

感觉现在还能感受到上个月给您发邮件请您帮忙修改简历时心情的志所，不只是对未来的迷茫和不确定，更多的时恐恨和对
自己的质疑。但是二哥回复我的我觉得你肯定可以的，大胆放心地往前冲，我等一手你的喜报。"一直以来都给了我很大的支
持，感觉两个月来心理的折磨远胜于频繁的面试笔试带来的压力。

最后的最后，还是再次感谢二哥，我也相信二哥在看到一封又一封的喜报时内心也一定是充满了成就感哈哈哈哈!

其他的都觉得比不过二哥哈哈哈哈哈!

整整两个月，面渣逆袭 MySQL 篇第二版终于整理完了，这一版几乎可以说是重写了，每天耗费了大量的精力在上
面，可以说是改头换面，有一种士别俩月，当刮目相看的感觉。

S        全部

Apple Books
四 主页

书库

加人                          |潮|逆|获             |渣逆|殴          回国班图
和                  MySQL篇       并发编程篇         JVM篇

加 已读完
吕 醒书                                                 三分恶|沉默王二修订版              三分恶|沉默王二修订版              三分恶|沉默王二修订版              三分恶|沉默王二修订版

人 有声书
B poF
目 我的试读版

我的藏书
十 新建藏书

-                                 二哥的并发编
图图                           程进阶之路md
Java基础篇

三分恶|沉默王二修订版

No. 294 1 302




## 第 295 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

网上的八股其实不少，有些还是付费的，我觉得是一件好事，可以给大家提供更多的选择，但面渣逆袭的含金量懂
的都懂。

二哥编程星球VIP9群 (444) C                                .。

饼- 沉默王二-二哥: 面渣逆袭并发编程篇 2.0 .…

目   一                         人入 323 条新消息

我觉得二哥的面渣很适合中国宝宝体质

J国 …r
国         一互                  ne、
二哥的饭都喂到我嘴边了人局
面湾逆效第二版是在星球嘉宾三分恶的初版基础上，加入了二哥自己的思考，加入了 1000 多份真实面经之后的结

果，并且从 24 届到 25 届，再到 26 届，帮助了很多小伙伴。未来的 27、28 届，也将因此受益，从而拿到心仪的
offer。

能帮助到大家，我很欣慰，并且在重制面渣逆袭的过程中，我也成长了很多，很多薄弱的基础环节都得到了加强，
因此第二版的面渣逆袭不只是给大家的礼物，也是我在技术上昱变的记录。

No. 2951302




## 第 296 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

好滴!

谢谢二哥

我把你推荐给我们实验室的基本所有人了

他们的反馈都是八股看面渣

包稳的哈!

No. 2961302

Fa




## 第 297 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

二哥，来报个喜，滴泣上岸了，双非学院本sp人 仿)

部门还行，哈哈哈外3

太牛了

等一手经验贴分享，发个红包，哈哈

当时搞完就直接面了A
MQ八股看的面渣@)
有惊无险
口碑来了哈哈。
主要我看的几个八股都是结合起来的

然后MQ八股目前面渣比较全

No. 2971 302




## 第 298 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

革 =     哥, 下一本面渣 2.0 进度怎么样

了 大期待了， 这几本 2.0 的质量比

站 特别是将相关高频的
面经集中在一起, 看完一小部分可

以通过这些问题来自我拷打一下，

效果简直不要太好他侦久久邬

下午4:34

重 二哥加油加油加油， 好期待mysql
和redis 的2.0，太喜欢二哥的面渣
了， 看了市面上不少的八股 股，镶兜
转转还是二哥的最舒服

很多时候，我觉得自己是一个佛系的人，不愿意和别人争个高低，也不愿意去刻意宣传自己的作品。
我喜欢静待花开。

如果你觉得面渣逆袭还不错，可以告诉学弟学妹们有这样一份免费的学习资料，帮有我做个口碑。

我还会继续优化，也不确定第三版什么时候会来，但我会尽力。

愿大家都有一个光明的未来。

由于 PDF 没办法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】，或者扫描/长按识别下面的二维
码，关注二哥的公众号，回复【222】即可拉取最新版本。

No. 298 1302




## 第 299 页


面渣逆效MySQL篇V2-让天下所有的面渣都能逆获

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，上毕竟星球用户都付费过了，
我有必要让他们先享受到一点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

No. 2991302




## 第 300 页


面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

中                  wangpan                   污         杜” 由
名称                                          人 ，修改日期
己 二哥的 JVM 进阶之路.epub            2024年7月11日 14:0
忆 二哥的 JVM 进阶之路.md              2024年7月11日 14:0
哥的 JVM 进阶之路.pdf              2024年7月11日 14:0
60*13薪别说新疆 ，外派到伊拉克都行                                    “ 面淹逆获 Java 基础篇第二版.md                 2024年12月31日 08
品 面潮逆芍 JVM篇 V2.0.epub            2025年1月21日 14:2
面渣逆效 JVM篇 V2.0 (暗黑版).pdf        2025年1月21日 14:2
面渣逆效 JVM 篇第二版.md             2025年1月21日 14:2

面渣逆芍 MyBatis.md                 2024年7月11日 14:0
面渣逆袭 MyBatis.pdf                 2024年7月11日 14:0
面渣逆装 Redis 篇.md                2024年7月11日 14:0
面渣逆装 Redis 篇.pdf                2024年7月11日 14:0
面渣逆袭 Spring 篇.md                2024年7月11日 14:0
面渣逆袭 Spring 篇.pdf                2024年7月11日 14:0
面渣逆袭-分布式篇.md                         2024年7月11日 14:0
面渣逆袭-分布式篇.pdf                2024年7月11日 14:0
面渣逆袭并发编程篇第二版.md           2025年2月26日 11:3
面渣逆袭并发编程篇V2.0.epub           2025年2月26日 11:3
面渣逆袭并发编程篇V2.0.pdf            2025年2月26日 11:3
面渣逆袭并发编程篇V2.0 (暗黑版).pdf      2025年2月26日 11:3

最 夯尖地区+二哥的Java 进阶之路PDF，第二
版，GitHub 星标 13000+

驹中局回时各。本 rom 下mr
本

本本目电中。二 roeron mn mm
1

二哥的并发编程小册: https:/jiavabettercn/                       本 面渣逆袭操作系统.md                    2024年7月11日 14:0
thread/                                                      日 机地理                   2024年7月11日 14:0

一        、       ，     下                              口 面济逆获集合框架篇第二版.epub          2025年1月8日 18:3:

二可的 JVM 进阶之路: tpsViavabettercn/                             ”面渣逆效集合框架篇第二版.md                 2025年1月8日 18:26

jm/                                                                             面淹地赣集合框架篇V2.0.pdf                  2025年1月8日 18:27

面尖逆绪集合框架篇V2.0 (暗黑) .pdf          2025年1月8日 18:26

面渣逆效计算机网络.md                    2024年7月11日 14:0

   白 %-                                                          面淹逆赣计算机网络.pdf                   2024年7月11日 14:0

面渣逆袭微服务篇.md                        2024年7月11日 14:0
面渣逆袭微服务篇.pdf                        2024年7月11日 14:0
面渣逆效 Java基础篇V2.0.epub               2024年12月31日 09
面渣逆效Java基础篇V2.0.pdf              2024年12月30日 20
面渣逆效Java基础篇V2.0 (暗黑) .pdf        2024年12月30日 20
我把二哥的java 进阶之路、JVM 进阶之路、并发编程进阶之路，以及所有面渣逆袭的版本都放进来了，涵盖 Java
基础、jJava集合、java并发、JVM、Spring、MyBatis、计算机网络、操作系统、MySQL、Redis、RocketMQ 、分
布式、微服务、设计模式、Linux 等 16 个大的主题，共有 40 多万字，2000+张手绘图，可以说是诚意满满。

这次仍然是三个版本，亮白、暗黑和 epub 版本。给大家展示其中一个 epub 版本吧，有些小伙伴很急需这个版
本，所以也满足大家了。

222

No. 3001302




## 第 301 页


图文详解 83 道 MySQL 面试高频题，这次吊打面试官，我觉得稳了 (手动 dog)
接，作者: 三分恶，戳原文链接。

没有信么使我停留一一内了月的，幼伏涯六有政碗、有绽戎、有宁甫的

从索引类型上来说，MyISAM 为非聚簇索引，索
引和数据分开存储，索引保存的是数据文件的指针。

加

面渣逆袭MySQL篇V2-让天下所有的面潮都能逆袭

面渣逆装MySQL篇第二版

会扫描索引。
InnoDB的内存结构了解吗?
和             2025 年04 月04 月增喜

5

革

CE               log buffer。

[和

aa

oa

更细微的层面上来讲，MyYISAM 不支持外键，可
以没有主键，表的具体行数存储在表的属性中,查询

@21

系列内容:

昌

面渣逆袭jJava SE 篇 】

面渣逆效Java 集合框架篇 虽
面渣逆效Java 并发编程篇 虽

面渣逆次JVM 篇只
面渣逆人区 Spring篇哑
面渣逆袭 Redis 篇

面渣逆区 MyBatis 入 中

面渣逆交 MysQL 篇吨

面淹逆获 RocketMQ 篇听

341216页

No. 3011302

站
iD
目
目 日目折口@

Memon seuctures
eDBDB IE中
HIEEITD
目
日目

|

目目国目日

时可以直接返回; InnoDB 支持外键，必须有主键，
具体行数需要扫描整个表才能返回，有索引的情况下

InnoDB 的内存区域主要有两块，bufter Pool 和

buffer pool 用于缓存数据页和索引页 ，提升读写性
能; log buffer 用于缓存redo log，提升写入性能。

本
0
Si
Redo Log                  了
               ES
  四
人
人
本章还利181页

。整理: 沉默王二，戳转载链

渤，我是不系之月。




## 第 302 页


面渣逆袭MySQL篇V2-让天下所有的面渣都能逆袭

 面渣逆效设计模式篇 中

No. 3021302



