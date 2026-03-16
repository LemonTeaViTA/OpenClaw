# 面渣逆袭Redis篇V2.0

> 来源：面渣逆袭Redis篇V2.0.pdf

> OCR 解析时间：2026-03-14 17:35:17

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 261

- **文件大小**: 68.47 MB


---


## 第 1 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

合 ”二哥的Java进阶之路

三分恶

沉默王二修订版

No.11261




## 第 2 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

前言

4.6 万字 286 张手绘图，详解 57 道 Redis 面试高频题 (让天下没有难背的八股) ，面渣背会这些 Redis 八股文，
这次吊打面试官，我觉得稳了 (手动 dog) 。整理: 沉默王二，戳转载链接，作者: 三分恶，戳原文链接。

亮白版本更适合拿出来打印，这也是很多学生党喜欢的方式，打印出来背诵的效率会更高。

eee@ 加 上口回 2 CC 六 丁洁池妆Redis简V2.0pdf - 福昕阅读器 。〇 提索                                   而且@
文件 主页 注风 视加 表单 保护 共享 名且                                 名

到                   而洒进费MySQL逢V2.。。 面浊贰Redis简V2.… X

内
                             下

QQ 规

吕 计
= 口 关机
二 只 1这说说什么是Redis?

只3. Redis有前上数据关型
央 4这 Redis 为什么全?7
二只 5入详细说一下IO多路复用四?
只 Redis为什么时期计择单程
只 7Redis 80 使用多给是怎么加
二只 说说 Redis 的第用命令 (补充)
只 9间的Redis OpS 台到多14
。 只 持久化
* 只 商用
 只 组设计
二只29 以什么是组存击检?
二只 30. 这能训布过尖各加?
<。只3 尽 如何保证生存和数据库的
<网 32 如何保这本地经存和分布区
二 只 33什么是区key                    如果是秒杀接口，还可以使用 Lua 脚本来实现令牌桶算法，限制每秒只能处理 N 个请求。
只34更怎么处理码Key 呢?
只35怎么处理大 Key 机?              -- KEYs[11， 令牌桶的key
只 36扫丰怎么全?              -- ARcvI11: 桶容量
只 37 无度有问题听说这?如何时         -- ARev[21: 令牌生成速率《每秒)
+ 口 Reds 运维                     -- ARcvI31; 当前时间攻(秒)
。 口 Redis库用
+ 器居结攀                                                               tokens'，'timestanp')
。 口 #友                                                     or aRRcv0

多 《    14  ”1259 》》罗 嘎品                           国时上转黑一    <   十 15664% - 呈 于

2025 年 04 月 27 日开始着手第二版更新。
。 对于高频题，会标注在《java 面试指南(付费) 》中出现的位置，哪家公司，原题是什么，并且会加内，目
录一目了然; 如果你想节省时间的话，可以优先背诵这些题目，尽快做到知彼知己，百战不殖。
。 区分八股精华回答版本和原理底层解释，让大家知其然知其所以然，同时又能做到面试时的高效回答。
。 结合项目 (技术派、pmhub) 来组织语言，让面试官最大程度感受到你的诚意，而不是机械化的背诵。

。 修复第一版中出现的问题，包括球友们的私信反馈，网站留言区的评论，以及 GitHub 仓库中的issue，让这
份面试指南更加完善。

。 增加二哥编程星球的球友们拿到的一些 offer，对面渣逆袭的感谢，以及对简历修改的一些认可，以此来激励
大家，给大家更多信心。

。 优化排版，增加手绘图，重新组织答案，使其更加口语化，从而更贴近面试官的预期。

No. 21 261




## 第 3 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

日 SS         电RE
多 An updated version of GitHub Desktop is available and will be installed at the next launch. See wthat's new or restart GitHub Desktop，                                    x

Tchanged fle
Update redis.md

昌 mm王= .4daysago       docslsrclsidebarl .redismd 回   二
4123
拷细列表搞定                                    4224
和5               4125 4125
4126| +
427 +
4128 +
429|
Redis 面注                           438
S ms
431
球友 Empty 提醒，错误已修正                      二| :
晤 mmE= .as monm
并发编程
省 mmE- .2monthea                      433| +
434| +
Update javathread md
S mm-    hs                           本
并改编程错让下                         436
sa
437 +
4138| +
                      4139| +
buid: 2025年4月27日                    448|
当 mmE= .2zmonhsa
41
MySQL 篇最作版本                                                                          本
省 mmE= .2monthea                        2

由于 PDF 没?
码，关注二哥的公众号，回复【222】即可拉取最新版本。

他- 口

enelredis md

6 44123,38 88 typedef struct

使用两各结构，但它们会通过指针来共享相同元素的成员和分值，因此不会浪费要外的内存

4 你知道为什么Redis 7 .8要用Listpack来警代ziptistlg?

答: 主要是为了解决达列表的一个核心问题一连久更新。在压编列表中，每个节点都二要记录前一个节点的
长度信息
Menfh2e29,com，redis zipListlthttps://cdnvtobebetterjavaervcom/stutymore/redis

-29250607894736.png)

当揪入或到降一个;
们在
退化到“0(n

点时，如果这个操作导致寻个节点的长度发生了变化，那么后二的节点可能者要更新它
度"字段。最坏的情况下，一次反作可能击发整个链表的更新，时间复厅度会从

而 tistpack 的设计理念完全不同。
样就从根本上避免了连钙更新的问题

让每个:

录自己的长庆信息，不两依灯前一

虽凶要四间: Listpackl (https://cdn, tobebetterjavaer,com/stutymerey/redis-28248463165
313,png)

istpack 中的节间-                                          数据和和长度.

再保存其前一个节点的长度，而是保存当前节点的编权类型

1李宁间: Listpack 的元素](https://cdn,tobebetterjavaer,com/stutymore/redis-28249
483195754,png)

444 连钙更新是怎么发生的?

法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】 ，或者扫描/长按识别下面的二维

No. 31261




## 第 4 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

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

No. 41261




## 第 5 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

eeeg@ 品   局     忌。面潮逆装Redis篇V2.0 (暗黑版) .pdf - 福昕阅读器 。 〇 搜索                                 出及@
文件 主页 注释 视图 表单 保护 共享 帮助                                YY
有      而wySQLV2 而洒Redis笨V20_，。 而Redie昨V2.
m
中
永 让
33.什么是热Key?
岛
旬
<   人2

十 15664%

基础
1.过说说什么是 Redis?
Redis 是一种基于键值对的 NoSQL 数据库。

No. 51261




## 第 6 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

redis-server

27 Apr 2025 14     .962 * 0000o000o000o Redis is starting 00000000o000o
27 Apr 2025 14:    .962 * Redis version:    5，bits=64，commit=00000000，modified=0，pid=67692，just started

:C 27 Apr 2925 14:33:03.962 # Warning: no config fite specified，usting the defautt config，In order to specify a
Config file use redis-server /path/to/redis.conf
27 Apr 2925 14:33:03.962 * Increased maximum number of open fites to 19932 (it was originatty set to 2560).
27 Apr 29025 14     .962 * monotontc ctock:; POSIX ctock_gettime

Redis 7.2.5 (00000090/9) 64 bit

Running in standatone mode
Port: 6379
PID: 67692

https://redis.io

67692:M 27 Apr 2025 14:33:093.962 # WARNING: The TCP backtog setting of 511 cannot be enforced because kern.ipc.somaxco
nn is set to the Lower vatue of 128

67692:M 27 Apr 2025 14:33:03.963 * Server initiatized

67692:M 27 Apr 2025 14:33:93.963 * Ready to accept connections tcp

它主要的特点是把数据放在内存当中，相比直接访问磁盘的关系型数据库，读写速度会快很多，基本上能达到微秒
级的响应。

所以在一些对性能要求很高的场景，比如缓存热点数据、防止接口爆刷，都会用到 Redis。
不仅如此，Redis 还支持持久化，可以将内存中的数据异步落盘，以便服务宕机重启后能恢复数据。
Redis 和 MySQL 的区别?

Redis 属于非关系型数据库，数据是通过键值对的形式放在内存当中的; MySQL 属于关系型数据库，数据以行和
列的形式存储在磁盘当中。

No. 61261




## 第 7 页


滞

面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

。                           Web服务
沉默王二                                        直           人
?7 区
返回
缓存 Redis

|
未命中，查询 DB，写入缓存

xx

                            MySQL

实际开发中，会将 MySQL 作为主存储，Redis 作为缓存，通过先查 Redis，未命中再查 MySQL 并写回Redis 的方
式来提高系统的整体性能。

项目里哪里用到了 Redis?
在技术派实战项目当中，有很多地方都用到了 Redis，比如说用户活跃排行榜用到了 zset，作者白名单用到了

Set。

No.71261




## 第 8 页


目 技术派 已

让 首页
目录

加技术派整合MyBatis-Plus
加技术派多配置文件说明
加技术派请求参数解析

加技术派Redis实现用户活跃排行榜(…
加技术派Redis实现作者白名单 (志强-、

加技术派Redis实现计数统计

加技术派整合Redis(多Redis配置/Re
加技术派Redis的组存示例

加技术派Cacheable注解实现缓存
人加技术派Guava整合本地组存

加技术派Caffeine和整合本地缓存

加技术派Caffeine束合本地组存采坑
加技术派事务使用实例

加技术派使用事务的7条注意事项

人加技术派WEB三大组件之Filter

加技术派WEB三大组件之Serviet
加技术派WEB三大组件之Listener

面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

加技术派Redis实现用户活跃排行榜 《出强烈推荐) 外       富 3网吕
国技术派Redis实现用户活跃排行 入"
荐)                                                    1 场景说明

2. 方案设计

排行榜是一个很常见的需求场景了，当然对应的技术选型方案也可以说非常成雪，     了有7生

一个用户活跃度的排行榜，主要是基于redis的zset数据结构来实现，给大家实例溃
用的排行榜                                                          ~ 1. 更新用户活跃积分
11 寡等策略

1.2 檬单评分更新

1.3 具体实现

1.4 触发活跃度更新
2. 排行本查询
3. 小结

方案设计

在具体的代码介绍之前，先来了解一下业务场景

1. 场景说明

技术派中，提供了一个用户的活跃排行榜，当然作为一个博客社区，更应该实现的
参与感的目的，我们以用户活跃度来设计一个排行榜，区分日/月两个榜单

用户活跃度计算方式:

1. 用户每访问一个新的页面 +1分
2. 对于一篇文章，点黄、收藏 +2分;取消点更、取消收藏，将之前的活跃分收E
3. 文章评论 +3分

还有用户登录后的 session 、站点地图 SiteMap，分别用到了 Redis 的字符串和哈希表两种数据类型。

No. 81261

28

25




## 第 9 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

目录
加技术派多配置文件说明

加技术派请求参数解析

加技术派Redis实现用户活跃排行榜 (击强列推-.
加技术派Redis实现作者白名单 (才强列推荐)
加技术派Redis实现计数统计

加技术派整合Redis(多Redis配置/Redis集群)
加技术派Redis的缓存示例

加技术派Cacheable注解实现缓存

加技术派Guava整合本地缓存

加技术派Caffeine整合本地缓存

加技术派Caffeine整合本地缓存采坑实录

加技术派事务使用实例

加技术派使用事务的7条注意事项

加技术派wWEB三大组件之Fitter

加技术派WEB三大组件之Servlet

加技术派WEB三大组件之Listener

回技术派Redis的缓存示例 四

@ 人立 &S

缓存，提高应用程序的性能和响应速度。

Spring Boot 提供了 spring-boot-starter-data
Redis 变得非常容易。我们只需在 pom xml 文伯
件中增加一下 Redis 的连接信息就可以使用了 。

我们可以使用 RedisTemplate 来执行 Redis 命“
opsForvalue、opsForList、opsForHash、exec
Redis 命令。

在技术派中，我们使用 Redis 来缓存 session 和
符串和哈希表两种数据结构。像其他的数据结构
订阅、事务、Lua 脚本等，我们会在后续的源码

27 人点赞

楼仔 @ 2023-09-23 17
上 1 举报

IP 属地湖

No. 91261

关于 Redis
整合 Redis
 操作 Redis
字符串
型和
哈希
集合
有序集合
~ 技术派中的 Redis 实例
注入 RedisTemplate
 使用 RedisClient
我们先来看用户 session 这里。
再来看 sitemap 这里
关于 RedisTemplate 的 execute ..
小结

27

12

其中比较有挑战性的一个应用是，通过 Lua 脚本封装 Redis 的 setnex 命令来实现分布式锁，以保证在高并发场景
下，热点文章在短时间内的高频访问不会击穿 MySQL。




## 第 10 页


四，个人知识库                   加技术派Redis分布式锁 . @ 四 们
宣 技术派 8                                 因      return artlcte;
42 了
      业务远辑如下所示:

和 首页

E 目录                  母              线程4获取镇
人个则已BAyynabutumai地21基…                        _
加技术派消息队列Kafka (由强烈推荐)
加技术派MysqMRedis缓存一致性(由强烈推荐)                      线程4行业务
加技术派MysqMRedis缓存一臻性之Cannal (出.
加技术派canal实现MySQL和ES同步 (雪强列推                        加国生
加技术派ES实现查询 (由强烈推荐)
加技术派Redis分布式锁 (二强列推荐)     ，
加技术派wx-job实现定时任务 (地强列推荐)                        CN
发技术派服务监控之Actuator/Prometheus/Gra，                       Y
加技术派员口号冲突解决方案                         |
加技术派Fitter实现请求日志记录                                7
加技术派记录SQL执行日志             velve是否相等
园技术派深入理解DB连接池HikariCP                                是
加技术派异常日志报警通知                     往8       王厅 生
加技术派并行访问性能优化

面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

加技术派通用敏感词蔡换 (贞强烈推荐

部署过 Redis 吗?

第三种方式解决了误删他人锁的问题，但是还存在一个问题

底如何设置?

S 加 中

过期各放钙的同时
线程B区到锁

线程B秩取锁|

法     此时钠线程B拥有

主要远辑在这里

过期时间的值到

第一种回答版本:

我只在本地部署过单机版，下载 Redis 的安装包，解压后运行 redis-server 命令即可。

第二种回答版本:

我有在生产环境中部署单机版 Redis，从官网下载源码包解压后执行 make gg make install 编译安装。然后纺

辑 redis.conf 文件，开启远程访问、设置密码、限制内存、设置内存过期淘汰策略、开启 AOF 持久化等:

bind 0.0.0.0

requirepass your_password # 设置密码

maxmemory 4gb

maxmemory-policy allkeys-1lru

appendonly yes

第三种回答版本:

## 允许远程访问

## 限制内存，避免 OOM

# 开启 AOF 持久化

# 内存淘汰策略

我有使用 Docker 拉取 Redis 镜像后进行容器化部署。

docker run -qd --name redis -P 6379:6379 redis:7.0-alpine

No. 101261




## 第 11 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis 的高可用方案有部署过吗?

有部署过哨兵机制，这是一个相对成熟的高可用解决方案，我们生产环境部署的是一主两从的 Redis 实例，再加上
三个 Sentinel 节点监控它们。Sentinel 的配置相对简单，主要设置了故障转移的判定条件和超时赣值。

主节点配置:

Port 6379
appendonly yes

从节点配置:

replicaof 192.168.1.10 6379
哨兵节点配置:

sentinel monitor mymaster 192.168.1.10 6379 2
sentinel down-after-milliseconds mymaster 5000
sentinel failover-timeout mymaster 60000
sentinel parallel-syncs mymaster 1

当主节点发生故障时，Sentinel 能够自动检测并协商选出新的主节点，这个过程大概需要 10-15 秒。

另一个大型项目中，我们使用了 Redis Cluster 集群方案。该项目数据量大且增长快，需要水平扩展能力。我们部
署了 6 个主节点，每个主节点配备一个从节点，形成了一个 3主3从 的初始集群。Redis Cluster 的设置比 sentinel
复杂一些，需要正确配置集群节点间通信、分片映射等。

redis-server redis-7000.conf
redis-server redis-7001.conf

# 使用 redis-cli 创建集群

# Redis 会自动将 key 哈希到 16384 个槽位

关 主节点均分权位，从节点自动跟随

redis-cli --cluster create \
127.0.0.1:7000 127.0.0.1:7001 127.0.0.1:7002 \
127.0.0.1:7003 127.0.0.1:7004 127.0.0.1:7005 \
--cluster-replicas 1

Redis Cluster 最大的优势是数据自动分片，我们可以通过简单地增加节点来扩展集群容量。此外，它的故障转移
也很快，通常在几秒内就能完成。

对于一些轻量级应用，我也使用过主从复制加手动故障转移的方案。主节点负责读写操作，从节点负责读操作。手
动故障转移时，我们会先将从节点提升为主节点，然后重新配置其他从节点。

No.111261




## 第 12 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

# 1。 取消从节点身份

redis-cli -h <slave-ip> slaveof no one

# 2。 将其他从节点指向新的主节点

redis-cli -h <other-slave-ip> slaveof <new-master-ip> <port>

1. Java 面试指南(付费) 收录的华为一面原题: 说下 Redis 和 HashMap 的区别

2. java 面试指南 (付费) 收录的字节跳动商业化一面的原题: Redis 和 MySQL 的区别

3. java 面试指南 (付费) 收录的农业银行面经同学 7 java 后端面试原题: Redis 相关的基础知识

4. java 面试指南 (付费) 收录的华为 OD 面经同学 1 一面面试原题: Redis 的了解, 部署方案?

5. java 面试指南 (付费) 收录的农业银行面经同学 3 java 后端面试原题: 项目里哪里用到了 Redis

6. java 面试指南 (付费) 收录的 360 面经同学 3 java 后端技术一面面试原题: 用过 redis 吗 用来干什么
7. Java 面试指南 (付费) 收录的招商银行面经同学 6 招银网络科技面试原题: 了解 MySQL、Redis 吗?
8

.Java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习java 后端面试原题: 项目中什么地方使
用了 redis 缓存，redis 为什么快?

9. java 面试指南 (付费) 收录的国企零碎面经同学 9 面试原题: 数据库用什么多 (说了 Mysql 和 Redis)
10. java 面试指南(付费) 收录的荣耀面经同学 4 面试原题: Redis和MySQL的区别?

11. Java 面试指南 (付费) 收录的海康威视同学 4面试原题: Redis部署

12. java 面试指南(付费) 收录的华为 OD 面经同学 1 一面面试原题: Redis 的了解, 部署方案?

13. java 面试指南(付费) 收录的同学 30 腾讯音乐面试原题: redis的部署方式都有哪些呢，各自有什么优

2.Redis 可以用来干什么?

Redis 可以用来做缓存，比如说把高频访问的文章详情、商品信息、用户信息放入 Redis 当中，并通过设置过期时
间来保证数据一臻性，这样就可以减轻数据库的访问压力。

No. 121 261




## 第 13 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

web服务

用户

Redis 的 Zset 还可以用来实现积分榜、热搜榜，通过 score 字段进行排序，然后取前 N 个元素，就能实现 TOPN
的榜单功能。

No. 131261




## 第 14 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

月度活跃排行榜 >>>
 C1own        (579)
 勤奋的大神     (141)
 qiuyunduo     (8刀
简单的刺狂     (67)
Y            (60)
乐观的芝厅     (42)
认真的黑夜     (39)

865287370           (38)

利用 Redis 的 SETNX 命令或者 Redisson 还可以实现分布式锁，确保同一时间只有一个节点可以持有锁; 为了防
止出现死锁，可以给锁设置一个超时时间，到期后自动释放; 并且最好开启一个监听线程，当任务尚未完成时给锁
自动续期。

No. 141261




## 第 15 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

四 ，襄          加pmhub集成Redis分布式锁保障流程状态更新【由必看)   田窜SS加 名 3 目 国
来个offer-PmHub @
PmHub分布式锁业务流程
:               本        记 as |
多 首页                                  O
人母 :=                    人
回PmHub Gateway全局过
图PmHub整合Transmittab，                      了
回PmhHub用Docker Comp,                                                    新建项目
流程状态通知
回PmHub集成Redis分布…
加PmHub的性能监控和分                      YY                 |
国Pmhub实现Redis加Lua                     新建任务
回Pmhub自定义注解加和                                                                                              流程状态回调
回PmHub集成 Sentinel+O，                      由
司PH 分布事务Seeft            了王-ee 任务审批设置
回Pmhub和整合Rocketmq              等待锁释放
国PmHub如何保证缓存和                                                     于

”产品设计和
加人人都是产品经理，打造
回PmHub 需求分析及可行
添加依赖

加PmHub 项目管理流程
回Pmhub 产品原型设计

PmHub分布

如果是秒杀接口，还可以使用 Lua 脚本来实现令牌桶算法，限制每秒只能处理 N 个请求。

-- KEYS[1] : 仿牌桶的key

-- RARGV[1] : 桶容量

-- RARGV[2] : 令牌生成速率 (每秒)
-- RARGV[3]: 当前时间戳 (秒)

local bucket

local tokens

tonumber(bucket[1]) or RARGV[11]
local last_time = tonumber(bucket[2]) or RARGV[31]

local rate = tonumber(RRGV[2])
local capacity = tonumber(RRGV[1])
local now = tonumber(RRGV[3])

-- 计算新令牌数

local delta = math.max(0，now - last time)
local add tokens = delta * rate

tokens = math.min(capacity，tokens + add_tokens)
last_time = now

local allowed = 0

if tokens >= 1 then
tokens = tokens - 1

No.151261

redis.cal1('HMGET'，KEYS[1]， "tokens'，

"timestamp ')




## 第 16 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

allowed = 1

end
redis.cal1('HMSET'，KEYS[1]， 'tokens'，tokens， 'timestamp'，1ast_ time)
redis.cal1('EXPIRE'，KEYS[1]，3600) -- 过期时间可自定义

Feturn allowed

在Java 中调用 Lua 脚本:

// 令牌桶参数
int capacity = 10; // 桶容量
int rate = 27     // 每秒2个令牌

long now = System.currentTimeMillis() / 1000;
String key = "token bucket:user:123")

// 调用 Lua 脚本，返回 1 表示通过，0 表示被限流
Long allowed = (Long) redis.eval(luaScript，1，key，String.valueOf(capacity)，
String.valueOf(rate)，String.valueOf(now) )

1. Java 面试指南 (付费) 收录的农业银行面经同学 7 java 后端面试原题: Redis 相关的基础知识

2. java 面试指南 (付费) 收录的字节跳动同学 7 java 后端实习一面的原题: 讲一下为什么要用 Redis 去
存权限列表?

3. java 面试指南(付费) 收录的字节跳动同学 20 测开一面的原题: redis 有什么好处，为什么用 redis

memo: 2025年4月28 日修改至此，今天帮球友修改简历的时候，碰到一位东南大学本硕连读的球友，星球能
来这么多优秀的球友，真的很开心啊。

念 教育经历

东南大学              硕士”计算机科学与技术         计算机科学与工程学院
法国雷恩大学 ” 硕士” 计算机科学与技术 计算机科学与工程学院
东南大学              学士 ”计算机科学与技术         计算机科学与工程学院

3.愉Redis有哪些数据类型?
Redis 支持五种基本数据类型，分别是字符串、列表、哈希、集合和有序集合。

No. 16 1 261




## 第 17 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

隆

哈希

列表

集合

还有三种扩展数据类型，分别是用于位级操作的 Bitmap、用于基数估算的 HyperLogLog、支持存储和查询地理坐
标的 GEO 。

详细介绍下字符串?
字符串是最基本的数据类型，可以存储文本、数字或者二进制数据，最大容量是 512 MB。

No. 171261




## 第 18 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

适合缓存单个对象，比如验证码、token、计数器等。
详细介绍下列表?
列表是一个有序的元素集合，支持从头部或尾部插入/删除元素，常用于消息队列或任务列表。

Key                                                Value
lpush                                                          rpush
llen=5
Irange23
lpop                                                           rpop
详细介绍下哈希?

哈希是一个键值对集合，适合存储对象，如商品信息、用户信息等。比如说 value = {name: “沉默王二' ，age:
18) 。

No. 181261




## 第 19 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis String

Redis Hash

详细介绍下集合?
合是无序且不重复的，支持交集、并集操作，查询效率能达到 o(1) 级别，主要用于去重、标签、共同好友等场

曙
景。

No. 191261




## 第 20 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Key                                                       Value

详细介绍下有序集合?
有序集合的元素按分数进行排序，支持范围查询，适用于排行榜或优先级队列。

user:ranking

详细介绍下Bitmap?

Bitmap 可以把一组二进制位紧凑地存储在一块连续内存中，每一位代表一个对象的状态，比如是否签到、是否活
跃等。

No. 201261




## 第 21 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

RedisObjecf
元数据
| (89)
ptr 指针
(8B)                   区
free
0
buf攻帮]一中                    buf index = 0 对应的字节有 8 个 bif 位
buf

buf[1] = "\0" 表示结尾

比如用户 0 的已签到 1、用户 1 未签到 0、用户 2 已签到，Redis 就会把这些状态放进一个连续的二进制串 101 ，
1 亿用户签到仅需 100,000,000 / 8 / 1024 =~ 12MB 的空间，真的省到离谱。

详细介绍下HyperLogLog?

HyperLogLog 是一种用于基数统计的概率性数据结构，可以在仅有 12KB 的内存空间下，统计海量数据集中不重
复元素的个数，误差率仅 0.81%。

8 Bits Hashed Element                 ae Ne Binary [se |  Count

一

oool o[o]foo4Tol
ooll 1[1]olsT[o]
[olol 21ojlo6lz2
oil 3[o]jBa7To]

底层基于 LogLog 算法改进，先把每个元素哈希成一个二进制串，然后取前 14 位进行分组，放到 16384 个桶中，
记录每组最大的前导零数量，最后用一个近似公式推算出总体的基数。

No. 211 261




## 第 22 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

7177

__     沙洲
0全 一CO1IS1闵7117

.7=1

]
5再

所有桶估计值的调和平均数

$2^{14}$个桶，每个桶6 Bit，刚好 16384 * 6 /8 / 1024 K = 12KB ，8bit=1byte。

举个超简单的例子，假设有一个神奇的哈希函数，可以把元素散列成一个二进制数，比如:

元素                              哈希值                                                   前导零个数
userA                          000100101.…                                        3
userB             001010011.…                    2
userC             000000101.…                    6

可以发现，哈希值越长前导零越多，也就说明集合里的元素越多。
大型网站 UV 统计系统示例:

public class UVCounter {
private Jedis jedis;

public void recordVisit(String date，String userId) {
String key = "uv:" + datey
jedis.pfadd(key，userId)

}

public long getUV(String date) {

No. 221 261

|

每个桶的估计值




## 第 23 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

return jedis.pfcount("uv:" + date) 1;

】}

public long getUVBetween(String startDate，String endDate) {
List<String> keys = getDateKeys(startDate，endDate)
return jedis.pfcount(keys.toRrray(new String[0]))7

详细介绍下GEO?

GEO 用于存储和查询地理位置信息，可以用来计算两点之间的距离，查找某位置半径内的其他元素。
常见的应用场景包括: 附近的人或者商家、计算外卖员和商家的距离、判断用户是否进入某个区域等。
底层基于 ZSet 实现，通过 Geohash 算法把经纬度编码成 score。

reclis deo

底层数据结构

以 gechesh 字符串十进制作为 score
wep5e3cbbvuOEE直<4026346d4218685282

Basea2.

比如说查询附近的商家时，Redis 会根据中心点经纬度反推可能的 Geohash 范围，
在 ZSet 上做范围查询，拿到候选点后，用 Haversine 公式精确计算球面距离，筛选出最终符合要求的位置。

public class NearbyShopService {
Private Jedis jedisy
private static final String SHOP_KEY = "shops:geo")

// 添加商铺
public void addshop(String shopId，double longitude，double latitude) {
jeadis .geoadd(SHOP_KEY，1longitude，1latitude，shopId);

】}

No. 231261




## 第 24 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 查询附近的商铺
Public List<GeoRadiusResponse> getNearbyShops(
double longitude，
double Latitude
double radiusKm) {
return jedis.georadius (SHOP_KEY，
longitude，
latitude，
radiusKmy
GeoUnit .KM
GeoRadiusParam.geoRadiusParam()
-withCcoord()
-withDist()
-sortRscending()
-count(20) ) 7

// 计算两个商铺之间的距离
public double getShopDistance(String shoplId，String shop2Id) {
return jedis.geodist(SHOP_KEY，
shoplId，
shop2Id，
GeoUnit .KILOMETERS ) ;

为什么使用 hash 类型而不使用 string 类型序列化存储?
Hash 可以只读取或者修改革一个字段，而 String 需要一次性把整个对象取出来。

No. 241261




## 第 25 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

字符串类型存储用户的信息

user_id:1:name “一 >           沉默王二

User_id:1:age        -一>                 18

hash类型存储用户的信息

name “| 沉默王二

user_id:1                                   和

age              18

比如说有一个用户对象 user = {name: “沉默王二' ，age: 18} ，如果使用 Hash 存储，可以直接修改 age 字

段:

redis.hset("user:1l"，"age"，19) 7

如果使用 String 存储，需要先取出整个对象，修改后再存回去:

String userJson = redis.get("user:l') 17

User user = JSON.parseObject(userJson，User.class))
user.setRge(19) 1
redis.set("user:1"，JSON.toJSONString(user) ) 1;

1. Java 面试指南 (付费) 收录的字节跳动商业化一面的原题: 说说 Redis 的 zset，什么是跳表，插入一个
节点要构建几层索引

No. 251261




## 第 26 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

2. java 面试指南 (付费) 收录的字节跳动面经同学 9 飞书后端技术一面面试原题: Redis 的数据类型，

ZSet 的实现
3. Java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你对 Redis 了解多少，说说常见的数
据结构和应用场景

4. java 面试指南(付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: Redis 的数据类型

5. Java 面试指南 (付费) 收录的快手面经同学 7 Java 后端技术一面面试原题: 说一下 Redis 常用的数据
结构

6. Java 面试指南(付费) 收录的农业银行面经同学 7 java 后端面试原题: Redis 相关的基础知识

7. Java 面试指南 (付费) 收录的华为面经同学 11 面试原题: 项目中使用了 redis，redis 有哪些数据类
型? 分别使用的场景是什么? 什么使用 hash 类型而不使用 string 类型序列化存储?

8. java 面试指南 (付费) 收录的 OPPO 面经同学 1 面试原题: Redis常见数据结构
9. java 面试指南 (付费) 收录的美团同学 9 一面面试原题: redis的数据结构类型?
10. java 面试指南 (付费) 收录的阿里云面经同学 22 面经: redis高级数据结构的使用场景
11. Java 面试指南(付费) 收录的腾讯面经同学 29 java 后端一面原题: Redis保证incr命令原子性的原理是
什么?

memo: 2025年4月29 日修改至此，今天有球友发信息说拿到了亚马逊的 offer，工资还给的很高，问我要不要
选” 真的共喜了串 。

No. 261 261




## 第 27 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

你好王哥，想和您咨询一下两个正
式 offer的选择。目前我是在美国
留学刚毕业，找到了美国亚麻的工
作。国内有去年外 .日:实习转正
四 鸣 offer 以及二本 3 二的
offer。亚麻的工资大约是.富 【的两
倍多 ，但我不考虑长期留在美国，
最多两三年。如果从三年后跳槽竞
争力的角度上来看请问有什么建议
吗?

下午3:20

4.二Redis 为什么快呢?

No. 271261




## 第 28 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

第一，Redis 的所有数据都放在内存中，而内存的读写速度本身就比磁盘快几个数量级。

1ws | LiLcache

10 ws         L2 cache
100 ws         人RAM ncecess
”edicrad苇
1 ks
19 we [SWFAERDYR | Meneneheal send data overIGibps wetwore国
160 ks            read from ssP         -一-一ooesre road FE RocksDB
1 ms                Tatabase tsert            |一Postorescl fwsert 伸
10 ms                   HPP dlsR seeR
Remuote 乙D0m ca凡
100 ms         ?PacRet CA-> NL->CA                             局
人                                                       cirafana refresh lntervaL 必
10 s                  retrd/refresh fntervaL

第二，Redis 采用了基于1O 多路复用技术的事件驱动模型来处理客户端请求和执行 Redis 命令。

redis线程

CR                   |
1    1VO多路复用    aaE加1                 命令回复处理

 基| 事件分发器   各| 该
ae_writeble              |
|        条| 命令答应处理

连接

-了

其中的 IO 多路复用技术可以在只有一个线程的情况下，同时监听成千上万个客户端连接，解决传统 IO 模型中每个
连接都需要一个独立线程带来的性能开销。

吕

必

玛

治

着

[3
mm

AE REABLE

二-区E
四    AE WRITABL
Sodket
AE REABLE
4
本

队列 mse3 mse2msg1

No. 28 1 261




## 第 29 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

IO 多路复用会持续监听请求，然后把准备好的请求压入到一个队列当中，并将其有序地传递给文件事件分派器，
最后由事件处理器来执行对应的 accept、read 和 write 请求。

客户端N               客户端1             客户端2            客户端3
林
二                 二             二             轴
Socket               Socket1            Socket2           Socket3
SS 二
CR                                          Epoll
1. epollL_wait 发现事件

当彭闪类贱

Redis 进程
Redis 会根据操作系统选择最优的 IO 多路复用技术，比如 Linux 下使用epoll，macOs 下使用 kqueue 等。

// epol1l 的创建和使用
int epfd = epoll_create(1024); // 创建 epoll 实例
struct epol1l_event ev，events[MRX_EVENTS])7

// 添加监听事件

ev.events = EPOLLIN7

ev.data.fd = listen_sock)
epol1l_ctl(epfd，EPOLL_CTL ADD，1listen_sock，&ev);

// 等待事件发生

while (1) {
int nfds = epoll_wait(epfd，events，MRX_EVENTS，-1)7
for (int 夺= 0;)I< nftds;) i++) {

No. 291 261




## 第 30 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 处理就绪的文件描述符

在 Redis 6.0 之前，包括连接建立、请求读取、响应发送，以及命令执行都是在主线程中顺序执行的，这样可以避
免多线程环境下的锁竞争和上下文切换，因为 Redis 的绝大部分操作都是在内存中进行的，性能瓶颈主要是内存操
作和网络通信，而不是 CPU。

Redis 6 之前版本
并发处理socket链接               单线程串行处理IO
(C和_                           |                                           Redis main Thread
mm 十八               六       一      <
一个请求的三个阶段
get一全|           read   c2    write   read    ec3    writec | | reado    ol    wire
ec2    get    c2    c3|    set    3         incr    ]
人           |
3et            各行” “种行…” “各行|   品行   囊行” “于利… “刘行一间行…
kernel                    必              7/
缺点                     优势:
1、单线程无法利用多CPU                     合生和在久的问题
2、囊行操作，革个操作*出问题"会"阻
全的作                              2、址免线程间CPU切换
@小眼睛

为了进一步解决网络 IO 的性能瓶巴，Redis 6.0 引入了多线程机制，把网络 IO 和命令执行分开，网络 IO 交给线程
池来处理，而命令执行仍然在主线程中进行，这样就可以充分利用多核 CPU 的性能。

mm                                                        Redis IO Thread
kemel
read               read              write
c3                 cl                  c2
Redis IO Thread
read              write              write
c2                 c3                 cl

Redis6
并发处理socket链接                      多线程处理网络IO，单线程串行处理计算
人
后   so 二         读事件                        天
所
写事件

小眼睛

主线程专注于命令执行，网络IO 由其他线程分担，在多核 CPU 环境下，Redis 的性能可以得到显著提升。

主线程

No. 301261





## 第 31 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

AT
2

人

抒入[
加入等待队列       |下|
史

IO 多线程线程组

 可     -0线程开始执行-一卢

3

区过本

宇

阻塞等待 ro

    本 2            - -IO线程开始执行~一-十刘 将结果写回sockef

 3       - 主线程开始执行一~一 Z [|
2    1

s 对底层数据结构做了极致的优化，比如说 String 的底层数据结构动态字符串支持动态扩容、预分配允
二 可  估 拓 内存碎片和内存分配的开销。





## 第 32 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

证
让

数据类型和底层数据结构
Redis 3.0                                Redis 最新版本

SDs                   SDs
String  -一一           String  -一

双向链表                 quicklist
Lis+  -一            Lis+  一一

压缩列表                 listpack
Hash                  Hash
Se+                   Sef
ZSef+                  ZSe+

跳表

No. 321261





## 第 33 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

| why is Redis so fast?                    园 blog.bytebytego.com

100kQps

(人@)ro Muriplexing & single-fhreaded read/write

1. java 面试指南 (付费) 收录的腾讯 java 后端实习一面原题: Redis 为什么读写性能高?
2. java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: 为什么 redis 快，淘汰策略 持久化

3. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: 单线程的 Redis 为什
么这么快?

4. java 面试指南 (付费) 收录的微众银行同学 1 java 后端一面的原题: Redis 为什么这么快?

5. java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: 项目中什么地方使
用了 redis 缓存，redis 为什么快?

6. java 面试指南(付费) 收录的得物面经同学 8 一面面试原题: Redis 为什么快

7. java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: redis为什么能处理高并
发

memo: 2025 年4 月 30 日修改至此，今天有球友发信息说拿到了滴滴的实习 offer，真的恭喜了串。

No. 33 /261




## 第 34 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

好的好的谢谢二哥，我是最近才拿到了滴滴的时
期实习，估计要于号 十能开始实习，但是那边要
求至外 。"” 二 才可以发起转正

有下
5.能详细说一下10多路复用吗?

IO 多路复用是一种允许单个进程同时监视多个文件描述符的技术，使得程序能够高效处理多个并发连接而无需创
建大量线程。

MO Multiplexing Model

application                              kernel
广。 select          System call         no dataready _
process
blocks                                                                         wait
waiting for                                                                              for data
one of
many fds                                return readable
L_                  4 dataready 一
     fad          System call        copy data
copy data
Process                                                               from kernel
blocks                               returmn OK                                to user
process 4 人人， copycomplete-

一        data

10 多路复用的核心思想是: 让单个线程可以等待多个文件描述符就绪，然后对就绪的描述符进行操作。这样可以
在不使用多线程或多进程的情况下处理并发连接。

No. 341261




## 第 35 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Multithreaded Server

Eco 《pe Geco
PPO   worker

        加   一一一
Pool     Y (decode kompute (encode     threads

不                         =                    本

decod> 《ompuie (encode
queued tasks
主要的实现机制包括 select、poll、epoll、kqueue 和 IOCP 等。

请说说 select、poll、epoll、kqueue 和10CP 的区别?

select 的缺点是单个进程能监视的文件描述符数量有限，一般为 1024 个，且每次调用都需要将文件描述符集合从
用户态复制到内核态，然后遍历找出就绪的描述符，性能较差。

No. 351261




## 第 36 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// select 的基本使用
int select(int nfds，fd_set *readfds，fd_set *writefds，
fd_set *exceptfds，struct timeval *timeout)7

// 示例代码

fd_set readfds1i

FD_ZERO(&readfds)            // 清空集合

FD_SET(sockfd，&readfds);       // 添加监听套接字

select(sockfd + 1，&readfds，NULL，NULL，NULL) 7

if (FD_ISSET(sockfd，&readfds)) { // 检查是否就绪
// 处理读事件

poll 的优点是没有最大文件描述符数量的限制，但是每次调用仍然需要将文件描述符集合从用户态复制到内核态，
依然需要遍历，性能仍然较差。

// pol1 的基本使用

int poll(struct pollfd *fds，nfds_ t nfds，int timeout) 17

// 示例代码

struct pollfd fds[MAX_EVENTS])
fds[0].fd = sockfd;

fds[0] .events = POLLIN;    // 监听读事件
poll(fds，1，-1);

if (fds[0].revents & POLLIN) {

// 处理读事件

epoll 是 Linux 特有的 IO 多路复用机制，支持大规模并发连接，使用事件驱动模型，性能更高。其工作原理是将文
件描述符注册到内核中，然后通过事件通知机制来处理就绪的文件描述符，不需要轮询，也不需要数据拷贝，更没
有数量限制，所以性能非常高。

// epol1 的基本使用

int epoll_create(int size)7

int epoll_ctl(int epfd，int op，int fd，struct epoll_event *event);

int epoll wait(int epfd，struct epoll_event *events，int maxevents，int timeout) 7

// 示例代码

int epfd = epoll_create(1);

struct epoll_event ev，events[MRAX_EVENTS]17
ev.events = EPOLLIN7

ev.data.fd = sockfd;
epoll_ctl1(epfd，EPOLL_CTL ADD，sockfd，&ev);

while (1) {
int nfds = epoll_ wait(epfd，events，MRX_EVENTS，-1) 17
for (int 1 = 0) i< ntds; i++) {
if (events[i].data.fd ==- sockfd) {

// 处理读事件

No. 361261




## 第 37 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

kqueue 是 BSD/macOs 系统下的 IO 多路复用机制，类似于 epoll，支持大规模并发连接，使用事件驱动模型。

int kqueue(void);
int kevent(int kq，const struct kevent *changelist，int nchanges，struct kevent
*eVentlist，int nevents，const struct timespec x*timeout ) 7

IOCP 是 Windows 系统下的 IO 多路复用机制，使用使用完成端口模型而非事件通知。

HANDLE CreateIoCompletionPort(HANDLE FileHandle，HANDLE ExistingCompletionPort，ULONG_PTR
CompletionKey，DWORD NumberOfConcurrentThreads ) ;

举个例子说一下 10 多路复用?

比如说我是一名数学老师，上课时提出了一个问题:“今天谁来证明一下勾股定律?

同学小王举手，我就让小王回答; 小李举手，我就让小李回答; 小张举手，我就让小张回答。

这种模式就是 IO 多路复用，我只需要在讲台上等，谁举手谁回答，不需要一个一个去问。
Redis MO多路复用模型

socket-client                             IO多路复用程序                   file event dispatcher             事件处理器
王一一一”                                                                        event hangler

S3

Redis 就是使用epoll 这样的 1O 多路复用机制，在单线程模型下实现高效的网络 10，从而支持高并发的请求处
理。

举例子说一下阻塞10和 10 多路复用的差别?
假设我是一名老师，让学生解答一道题目。

我的第一种选择: 按顺序逐个检查，先检查 A同学，然后是 B，之后是 C、D。。。这中间如果有一个学生卡住，
全班都会被耽误。

No. 371 261




## 第 38 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

这种就是阻塞I0，不具有并发能力。

No. 381261




## 第 39 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

|              read请求
 等待数据到达
线程阻塞
『和read完成剧数据拷贝
|

监视Socket
Select

线程阻塞

等待数据到达
socket可读

read请求

数据拷贝

No. 391261




## 第 40 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

我的第二种选择，我站在讲台上等，谁举手我去检查谁。C、D 举手，我去检查 C、D 的答案，然后继续回到讲台
上等。此时 E、A 又举手，然后去处理E 和 A。

select、poll 和 epoll 的实现原理?
select 和 poll 都是通过把所有文件描述符传递给内核，由内核遍历判断哪些就绪。

select 将文件描述符 FD 通过 BitsMap 传入内核，轮询所有的 FD，通过调用 file->poll 函数查询是否有对应事件，
没有就将 task 加入 FD 对应 file 的待唤醒队列，等待事件来临被唤醒。

Te 、             U

人seeatnene Wetvade dat weld dseteceptds sameal tmeovg

poll 改进了连接数上限问题，不再用 BitsMap 来传入 FD，取而代之的是动态数组 pollfd，但本质上仍是线性遍
历，性能没有提升太多。

No. 401261




## 第 41 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

丽人名一

polL_freewait

User

人in poustuct potfd fds, nfds_tnfds nttmeoutb]

select和poll的模式都是，一次将参数拷贝到内核空间，等有结果了再一次拷贝出去。

epoll 将监听的 FD 注册进内核的红黑树，由内核在事件触发时将就绪的 FD 放入 ready list。应用程序通过
epollL_wait 获取就绪的 FD，从而避免遍历所有连接的开销。

Us

[EC 人 (nameprd sncteplLeventemne mmaeent mttmeoub

epoll 最大的优点是: 支持事件驱动 + 边缘触发，ADD 时拷贝一次，epolLwait 时利用 MMAP 和用户共享空间，
直接拷贝数据到用户空间，因此在高并发场景下性能远高于 select 和 poll。

1. Java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: io多路复用了解吗?

2. java 面试指南 (付费) 收录的快手同学 4 一面原题: IO多路复用中select/pollMepoll各自的实现原理和
区别?

No. 411 261




## 第 42 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

3. java 面试指南 (付费) 收录的字节跳动面经同学19番茄小说一面面试原题: Linux中的IO多路复用

memo: 2025年5月1日修改至此，今天帮球友修改简历时 时，碰到一名北京交通大学的同学，又一所 211 院
校，星球真的是人才济济，大家一起加油吧 (骄傲) 。

北京交通大学 211 - 电子科学与技术 硕士

北京交通大学 211 - 电子科学与技术 本科 GPA Rank : 7/45
科研经历 : 号洞晤产『和于必册四西方向,已在 /EEEL :em
荣誉奖项 : 研究生学业奖学金一等奖、"嘲 。国" 局几宁
6.Redis为什么早期选择单线程?

第一，单线程模型不需要考虑复杂的锁机制，不存在多线程环境下的死锁、竞态条件等问题，开发起来更快，也更
容易维护。

2二:发表一作文
优秀会员、北京交通大学和 站村

Redis文件事件处理器架构

文

去接字队列          全

I/O多路复用程序       SN |   | 52 | 51       件
分

A                             发

器

第二，Redis 是IO 密集型而非 CPU 密集型，主要受内存和网络 IO 限制，而非 CPU 的计算能力，单线程可以避免
线程上下文切换的开销。

哪怕我们在一个普通的 Linux 服务器上启动 Redis 服务，它也能在 1s 内处理 1000000 个用户请求。
第三，单线程可以保证命令执行的原子性，无需额外的同步机制。

Redis is single threaded. How can 1 exploit multiple CPU / cores?

Its not very frequent that CPU becomes your bottleneck with Redis, as usually Redis is either memory or network
bound. For instance, using pipelining Redis running on an average Linux system can deliver even 1 million requests
per second, so ifyour application mainly uses O(N) or O(log(N)) commands, itis hardly going to use too much CPU.
However to maximize CPU usage you can start multiple instances of Redis in the same box and treat them as
different servers. At some point a single box may not be enough anyway, so ifyou want to use multiple CPUs you can
start thinking of some way to shard earlier.

You can find more information about using multiple Redis instances in the Partitioning page.

However with Redis 4.0 we started to make Redis more threaded. For now this is limited to deleting objects in the
background, and to blocking commands implemented via Redis modules. For future releases, the plan is to make
Redis more and more threaded.

No. 421261




## 第 43 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis 虽然最初采用了单线程设计，但后续的版本中也在特定方面引入了多线程，比如说 Redis 4.0 就引异步多线
程，用于清理脏数据、释放无用连接、删除大 Key 等。

/* 从数据库中删除一个键、值以及相关的过期条目 (如果有的话) 。
* 如果释放值对象需要大量的内存分配操作，该对象可能会被放入
* 延迟释放列表中，而不是同步释放。延迟释放列表将在
* bio.c 的另一个线程中进行回收。 */
#define LRZYFREE_THRESHOLD 64
int dbasyncDpelete(redisDb *db，robj *key) {
/* 从过期字典中删除条目不会释放键的 sds，
* 因为它与主字典共享。 */
if (dictSize(db->expires) > 0) dictDelete(db->expires,key->ptr) 7

/* 如果值对象只包含少量的内存分配，使用延迟释放方式
* 实际上会更慢. . .所以在一定闭值以下，我们就直接
* 同步释放对象。 */
dictEntry *de = dictUnlink(db->dict,key->ptr) 7
if (de) {
robj *val = dictGetval(de) 1
// 计算value的回收收益

size _t free_effort = lazyfreeGetFreeEffort(val))

/* 如果释放对象的工作量太大，就通过将对象添加到延迟释放列表

* 在后台进行处理。

* 注意，如果对象是共享的，现在就回收它是不可能的。这种情况

* 很少发生，但是有时 Redis 核心的某些实现部分可能会调用

* incrRefCount () 来保护对象，然后调用 dbpelete( ) 。在这种

* 情况下，我们会继续执行并到达 dictFreeUnlinkedEntry()

* 调用，这相当于仅仅调用 decrRefCcount()。 */

// 只有回收收益超过一定值，才会执行异步删除，否则还是会退化到同步删除

让 (free_effort > LRZYFREE_THRESHOLD && Val->refcount == 1) {
atomicIncr(1azyfree_objects,1) 7
biocreateBackgroundJob(BIO_LRZY_FREE,Val,NULL,NULL) 7
dictSetVal(db->dict,de,NULL) ;

】}

/* 释放键值对，如果我们将 val 字段设置为 NULL 以便稍后
* 延迟释放，那么就只释放键。 */
if (de) {
dictFreeUnlinkedEntry(db->dictvde))
if (server.cluster_enabled) slotToKeyDel(key->ptr) 7
return 17
} else {
return 07

官方解释: https://redis,io/topics/faq

No. 431261




## 第 44 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

memo: 2025年5月2日修改至此，今天帮球友修改简历时 时，碰到一名同济大学的同学，让感觉自己的付出正
在越来越多被更多人看到，真的很开心。

同济大学 - 软件工程 (硕士)

实史国 。宣蕊 名研究 / 发表论文2篇 / 担任课程助教

同济大学 - 软件工程 (本科)

排名109% / 校优秀本科毕业生 / 一等奖学金 / 数学建模市一等奖/ 六级 597 分
7.Redis 6.0 使用多线程是怎么区
Redis 6.0 的多线程仅用于处理网络 IO0，包括网络数据的读取、写入，以及请求解析。

?

单线程执行命令

『                 1          [                              1
I/0线程1 | ~ |                                 |

IT/0线程2 | -| 主线程  |

I/0线程3 | 一 |                                 |
1                  |           1                                 1

而命令的执行依然是单线程，这种设计被称为"IO 线程化"，能够在高负载的情况下，最大限度地提升 Redis 的响应

并发处理socket连接                        单线程事行执行命令，多线程处理网络IO

-…-- 这部分面试中可以不背，方便大家理解 start 一-
这一变化主要是因为随着网络带宽和服务器性能的提升，Redis 的瓶颈从 CPU 逐渐转移到了网络 9:

No. 441261




## 第 45 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

。 带宽从 10Gbps 提升到 100Gbps，甚至更高。
。 请求的并发数从几千到几万，甚至几十万。

单线程在高负载场景下处理网络 IO 出现了明显的性能瓶颈，Redis 的开发团队通过研究发现，在处理大数据包
时，单线程 Redis 有超过 80% 的 CPU 时间花在网络 IO 上，而实际命令执行仅占 20% 左右。

Redis 6.0 的多线程 IO 模型主要包含三个核心步骤:
。 仍然由主线程负责接收客户端的连接请求。
。 主线程将连接请求分发给多个 IO 线程进行处理，主线程负责解析和执行命令。
。 命令执行完毕后，由多个 IO 线程将结果返回给客户端。

// Redis 主事件循环 (简化版)

void beforeSleep(struct aeEventLoop *eventLoop) {

// 1主线程分派读任务给 TI/O 线程
handleCclientsWithPendingReadsUsingThreads () 7

// 2. 等待 I/0 线程完成读取

waitForIOThreads()7

// 3。 主线程处理命令

ProcessInputBuffer() 17

No. 45 1 261




## 第 46 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 4主线程分派写任务给 TI/O 线程

handleclientsWithPendingWritesUsingThreads () 1?

Redis 6.0 默认仍然使用单线程模式，但可以通过配置文件或命令行参数启用多线程模式。

# 启用多线程模式

io-threads 4

## 启用多线程写入 (Redis 6.0 默认只开启多线程读取)
io-threads-do-reads yes
建议将 IO 线程数设置为 CPU 核心数的一半，一般不建议超过 8 个。

经过多次测试，Redis 6.0 在处理 1-200 字节的小数据包时，性能提升 1.5-2 倍; 在处理 1KB 以上的大数据包时提
升约3-5 倍。

-这部分面试中可以不背，方便大家理解 end 一-
1. Java 面试指南 (付费) 收录的同学 30 腾讯音乐面试原题: redis6.0引入的多线程用作什么地方

8.说说 Redis 的常用命令 (补充)
2024年 04 月11 日增补
一句话回答 (也不用全部都背，挑三个就行) :

Redis 支持多种数据结构，常用的命令也比较多，比如说操作字符串可以用 SET/GET/INCR ，操作哈希可以用
HSET/HGET/HGETALL ，操作列表可以用 LPUSH/LPOP/LRANGE ，操作集合可以用 Sapp/SISMEMBER ，操作有序集
合可以用 zapp/zRANGE/ZINCRBY 等，通用命令有 EXPIRE/DEL/KEYS 等。

一-这部分面试中可以不背，方便大家理解 start一-
中、操作字符串的命令有:

命令                             作用                   示例

SET key value                    设置字符串键值            SET name jack
GET key                           获取字符串值              GET name

INCR key                          数值自增 1                INCR count

DECR key                          数值自减 1                DECR stock
INCRBY key N                      增加N                   INCRBY views 10
RPPEND key value                  追加字符串               RPPEND log "done"
GETRANGE key start end            获取子串               GETRRANGE name 0 3
MSET kl v1 k2 v2                 批量设置多个键值         MSET a 1 b 2

No. 461261




## 第 47 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

@@、操作列表的命令有:

。 LPUSH key value : 将一个值插入到列表 key 的头部。

ee。 RPUSH key value : 将一个值插入到列表 key 的尾部。

es ，ILPOP key : 移除并返回列表 key 的头元素。

。。RPOP key : 移除并返回列表 key 的尾元素。

。 LIRRANGE key start stop : 获取列表 key 中指定范围内的元素。
图、操作集合的命令有:

。 SRADD key member : 向集合 key 添加一个元素。

。 SREM key member : 从集合 key 中移除一个元素。

。。SMEMBERS key : 返回集合 key 中的所有元素。
人儿、操作有序集合的命令有:

。 2ZRDD key score member : 向有序集合 key 添加一个成员，或更新其分数。

。 ZRRNGE key start stop [WITHSCORES] : 按照索引区间返回有序集合 key 中的成员，可选 WITHSCORES
参数返回分数。

ee ZREVRANGE key start stop [WITHSCORES] : 返回有序集合 key 中，指定区间内的成员，按分数递减。
。 2ZREM key member : 移除有序集合 key 中的一个或多个成员。
@@、操作哈希的命令有:
。 HSET key field value : 向键为 key 的哈希表中设置字段 field 的值为 value。
。 HGET key field : 获取键为 key 的哈希表中字段 field 的值。
。 HGETRALL key : 获取键为 key 的哈希表中所有的字段和值。
。 HDEL key field : 删除键为 key 的哈希表中的一个或多个字段。
详细说说 set 命令?
SET 命令用于设置字符串的 key，支持过期时间和条件写入，常用于设置缓存、实现分布式锁、延长 Session 等场

曙
景。

SET key value [EX seconds | PX milliseconds | EXRAT timestamp | PXRAT timestamp-
milliseconds | KEEPTTL] [NX | XXx] [GET]

默认情况下，SET 会覆盖键已有的值。
支持多种设置过期时间的方式，比如说 EX 设置秒级过期时间，PX 设置毫秒过期时间。
支持条件写入，使其可以实现原子性操作，比如说 NX 仅在键不存在时设置值，XX 仪在键存在时设置值。

No. 471261




## 第 48 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

127.0.0.1:          USsername "redis_user"

OK

127.0.0.1:          counter 10

OK

127.0.0.1:          counter 20

OK

127.0.0.1:          counter

"20"

127.0.0.1:          session:token "TOKENVALUE” EX 300
OK

127.0.0.1:          Login:otp "123456"”PX 30000

OK

127.0.0.1:          promo:deaL "HALFOFF” EXAT 1672531200
OK

127.0.0.1:          event :start "BEGUN"”PXAT 1672531200000
0K

127.0.0.1:          key "valLue1” EX 60

0K

127.0.0.1:          key "vaLue2”"” KEEPTTL

0K

127.0.0.1:          user:101 "wanger”NX

OK

127.0.0.1:          User:101 "sb”NX

(niL)

127.0.0.1:          counter 10

0K

127.0.0.1:          counter 20 GET

"10"

127.0.0.1:          nonexist "heLLo"” GET

(niL)

缓存实现:

SET user:profile:{fuserid} {JSON数据) EX 3600
实现分布式锁:

SET lock:resource_name {random value} EX 10 NX
存储 Session:

SET session:{fsessionid} {session data} EX 1800

sadd 命令的时间复杂度是多少?

SADD 支持一次添加多个元素，返回值为实际添加成功的元素数量，时间复杂度为 O(N)。

No. 48 1261




## 第 49 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

redis-cli SADD myset "apple” "banana"” "orange"

incr命令了解吗?

INCR 是一个原子命令，可以将指定键的值加 1，如果 key 不存在，会先将其设置为 0，再执行加 1 操作。

redits-cLi

127.0.0.1:6379> SET counter 10
OK

127.0.0.1:6379> INCR counter
(Linteger) 11

127.0.0.1:6379> INCR counter
(Lnteger) 12

127.0.0.1:6379> INCR newcounter
(integer) 1

127.0.0.1:6379> 目

常用于网站访问量、文章点赞数等计数器的实现; 结合过期时间实现限流器; 生成分布式唯一 ID; 库存扣减等。

# 限制用户每分钟最多访问10次
FUNCTION limit_api_call(user_id)
current = INCR("rate:"+user _ id)
IF current == 1 THEN
EXPIRE("rate:"+user_id，60)
END
IF current > 10 THEN
RETURN false # 超出限制
ELSE
RETURN true ，## 允许访问
END
END

说的那么好，Redis 设

value 的函数是啥

学 1 部门主站技术部面试原题: Redis 的 sadd 命令时间复杂

memo: 2025年5月3日修改至此，今天           说拿到了美的的软开暑期实习 offer，虽然他自己不满
意，但暂时没有其他更好的，我建议他先去试一下旷:。

No. 491261




## 第 50 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥，我也拿到了一个实习 offer了，今天下来的，美的的软开，前面面
大厂，癌吾E j音。辣具 志攻全都一面挂，感觉自己真的学的不

好。美的的软开可能也是看在我是本地人才招我的。我现在就想着拿这个
保底了，后面只面号了。我就想问如果拿到 ia实习，能加克己辐吗? 对
秋招会不会受影响?

可以去的

9.单线程的Redis QPSs 能到多少? (补充)
2024年4月14 日增补
根据官方的基准测试，一个普通服务器的 Redis 实例通常可以达到每秒十万左右的 QPS。

Requests per second

140000

120000

100000

80000

60000

40000

20000

0 +              -              -              :              1              ，
0             10000 20000 30000 40000 50000 60000 70000

一-这部分面试中可以不背，方便大家理解 start ---
Redis 的 QPS (每秒请求数) 性能取决于多种因素，包括硬件配置、网络延迟、数据结构、命令类型等。

可以通过 redis-benchmark 命令进行基准测试:

redis-benchmark -h 127.0.0.1 -P 6379 -c 50 -n 10000

。 -ah : 指定 Redis 服务器的地址，默认是 127.0.0.1。

No. 501261




## 第 51 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

。 -p : 指定 Redis 服务器的端口，默认是 6379。
。 -c : 并发连接数，即同时有多少个客户端在进行测试。

。 -na : 请求总数，即测试过程中总共要执行多少个请求。

2023 年前，我用的是一台 macOS，4 GHz 四核 Intel Core i7，32 GB 1867 MHz DDR3，测试结果如下:

~ git:(master)+上132 (4.892S )
芭redis-benchmark -h 127.0.0.1 -p 6379 -c 50 -n 10000

PING_INLINE ==
10000 requests comptLeted in 0.09 seconds
50 paraLtLetL cLients
3 bytes payLoad
keep alLive: 1
host configuration "save": 3600 1 300 100 60 10000
host configuration "appendonLy": no
muLti-thread: no

Latency by percentitLe distribution:

0.000%5 <= 0.103 miLLLiseconds (cumuLative count 1)
50.000% <= 0.223 miLLLiseconds (cumuLative count 5671)
75.000% <= 0.239 miLLLiseconds (cumuLative count 8104 )
87.500% <= 0.255 miLLLiseconds (cumuLative count 8988)

可以看得出，每秒能处理超过 10 万次请求。

OPS = 总请求数 / 总耗时 = 10000 / 0.09 = 111111 OPS

延迟也非常低，99% 的请求都在 0.3ms 以内完成了。
-一-这部分面试中可以不背，方便大家理解end ----
1. java 面试指南 (付费) 收录的:

跳动面经同学 1 java                       单线程 Redis 的 QPS

多少?

持久化
10.二Redis的持久化方式有了哪些?

主要有两种，RDB 和 AOF。RDB 通过创建时间点快照来实现持久化，AOF 通过记录每个写操作命令来实现持久
化。

No. 511261




## 第 52 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis持久化的两种方式

1.RDB

《

2.AOF

这两种方式可以单独使用，也可以同时使用。这样就可以保证 Redis 服务器在重启后不丢失数据，通过 RDB 和
AOF 文件来恢复内存中原有的数据。

No. 521261




## 第 53 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

RDB
(Redis DB)

Client        |                                      Client        |
Application 人                                               Application 人

cache
operation

人

\
1
1
1
1
1
1
1
1
1
上
1

1
record command

回  on 5

到

AOFfileon Disk /|                          RDF fle on Disk

详细说一下 RDB?

RDB 持久化机制可以在指定的时间间隔内将 Redis 某一时刻的数据保存到磁盘上的 RDB 文件中，当 Redis 重启
时，可以通过加载这个 RDB 文件来恢复数据。

No. 531261




## 第 54 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

fRecis Nemory view                     RDPB file

 Snepshot the jn-memory dota                                |
2. Save the dota in binery file Crdb)      一一过
Before Croshn
fecis  Newmory view                                      RDPB file

直 Restore the previous snapshet

1. Reod tke RPB file

4Pter Crosh                      Disk

RDB 持久化可以通过 save 和 bgsave 命令手动触发，也可以通过配置文件中的 save 指令自动触发。

No. 541261




## 第 55 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Save 命令会阻塞 Redis 进程，直到 RDB 文件创建完成。

127.0.0.1:6379> Save
OK

127.0.0.1:6379> bgsave
Background Saving started

bgsave 命令会在后台 fork 一个子进程来执行 RDB 持久化操作，主进程不会被阻塞。

No. 551 261




## 第 56 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

信号通知父进程

生成RDB文件
写入三盘

什么情况下会自动触发 RDB 持久化?

第一种，在 Redis 配置文件中设置 RDB 持久化参数 save <seconds> <changes> ，表示在指定时间间隔内，如
果有指定数量的键发生变化，就会自动触发 RDB 持久化。

save 900 1     # 900 秒 (15 分钟) 内有 1 个 key 发生变化，触发快照
save 300 10    # 300 秒 (5 分钟) 内有 10 个 key 发生变化，触发快照
save 60 10000 “## 60 秒内有 10000 个 key 发生变化，触发快照

第二种，主从复制时，当从节点第一次连接到主节点时，主节点会自动执行 bgsave 生成 RDB 文件，并将其发送

No. 561261




## 第 57 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

master                                                                   slave
SYNC
二
时间点下
一人         fork >
生成 RDB
exit
二
发送 RDB
接收 RDB
传播自时间点 T 起积压的命

接收命令
传播命令
因
传播命令
尖
Y                                                                        Y

第三种，如果没有开启 AOF，执行 shutdown 命令时，Redis 会自动保存一次 RDB 文件，以确保数据不会丢失 。

详细说一下 AOF?
AOF 通过记录每个写操作命令，并将其追加到 AOF 文件来实现持久化，Redis 服务器宕机后可以通过重新执行这
些命令来恢复数据。

No. 571261




## 第 58 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

4peenel-Only   File
(4OP)

        asks aakf aska
SADD fruits apple orone' -orange| <

当 Redis 执行写操作时，会将写命令追加到 AOF 缓冲区; Redis 会根据同步策略将缓冲区的数据写入到 AOF 文
件。

命令写入
1.append

*3NrNnS$3N\rVnset\r\vn$5NrNnhelloNr\vnS$5NrNvnworldNrNn

当AOF 文件过大时，Redis 会自动进行 AOF 重写，剔除多余的命令，比如说多次对同一个 key 的 set 和 del，生
成一个新的 AOF 文件; 当 Redis 重启时，读取 AOF 文件中的命令并重新执行，以恢复数据。

AOF 的刷盘策略了解吗?

Redis 将 AOF 缓冲区的数据写入到 AOF 文件时，涉及两个系统调用: write 将数据写入到操作系统的缓冲区，
fsync 将 05 缓冲区的数据刷新到磁盘。

这里的刷盘涉及到三种策略: always、everysec 和 no。

No. 581261




## 第 59 页


How do Big Keys Impact 铭 redis Persistence? 国 blog.bytebytego.com

面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Always

Redis Main
Thread

VO System Call
write()

Kernel Buffer
Cache

Kernel Initiated
Write
fsync()

EverySec

Redis Main
Thread

VO System Call
write()

Kernel Buffer

Cache

@

Async
Timer Task

Kernel Initiated
Write
fsync()

No

Redis Main
Thread

VO System Call
write()

Kernel Buffer
Cache

Kernel Initiated

Write
fsync()

3 】 OS decides

。 always: 每次写命令执行完，立即调用 fsync 同步到磁盘，这样可以保证数据不丢失，但性能较差。

。 everysec: 每秒调用一次 fsync，将多条命令一次性同步到磁盘，性能较好，数据丢失的时间窗口为 1 秒。
。 no: 不主动调用 fsync，由操作系统决定，性能最好，但数据丢失的时间窗口不确定，依赖于操作系统的缓存

策略，可能会丢失大量数据。

可以通过配置文件中的 appendfsync 参数进行设置。

appendfsync everysec

说说AOF的重写机制?

由于 AOF 文件会随着写操作的增加而不断增长，为了解决这个问题，

缩和优化。

# 每秒 fsync 一次

No. 591261

Redis 提供了重写机制来对 AOF 文件进行压





## 第 60 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Redis命令逐步操作            Redis内存中数据变化             Redis内存中最新数据

[Den

]

LPUSH u:list“A”，“B”  区                                   LPUSH u:list"N "CD”

LPUSH u:list“M”，“N”     区     , “Be“An]

RPOP u:list                      [IN      ,“B]           下路
RPOP u:list                      [EN", "M]

LPUSH u:list “C"，“D”         [ED”"“C",*N",“M]     AOF重写
RPOP    [FDCreN

重写前，AOF记录6条命令          最新数据                                                         重写后，AOF只记录1条命令

AOF 重写可以通过两种方式触发，第一种是手动执行 BSREWRITEAOF 命令，适用于需要立即减小AOF文件大小的
场景。

第二种是在 Redis 配置文件中设置自动重写参数，比如说 auto-aof-rewrite-percentage 和 auto-aof-
rewrite-min-size ，表示当 AOF 文件大小超过指定值时，自动触发重写。

auto-aof-rewrite-percentage 100 # 默认值100，表示当前AoF文件大小相比上次重写后大小增长了多少百分比
时触发重写
auto-aof-rewrite-min-size 64mb # 默认值64MB，表示AOF文件至少要达到这个大小才会考虑重写

AOF 重写的具体过程是怎样的?

Redis 在收到重写指令后，会创建一个子进程，并 fork 一份与父进程完全相同的数据副本，然后遍历内存中的所有
键值对，生成重建它们所需的最少命令。

比如说多个 RPUSH 命令可以合并为一个带有多个参数的 RPRUSH;
比如说一个键被设置后又被删除，这个键的所有操作都不会被写入新 AOF。

比如说使用 sapp key member1 member2 member3 代替多个单独的 saApp key memberx 。

No. 601261




## 第 61 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

子进程在执行 AOF 重写的同时，主进程可以继续处理来自客户端的命令。

为了保证数据一致性，Redis 使用了 AOF 重写缓冲区机制，主进程在执行写操作时，会将命令同时写入旧的 AOF
文件和重写缓冲区。

等子进程完成重写后，会向主进程发送一个信号，主进程收到后将重写缓冲区中的命令追加到新的 AOF 文件中，
然后调用操作系统的 rename，将旧的 AOF 文件替换为新的 AOF 文件。

主进程 (fork)
上 子进程 (生成新的 AOF 文件)
上 内存快照

上~ 写入临时 AoF 文件
| 通知主进程完成

上 主进程 追加缓冲区到新 aoF 文件)
上 蔡换旧 aoF 文件
上 重写完成

AOF 重写期间，Redis 服务器会处于特殊状态:
。 aof _child_pid 不为0，表示有子进程在执行 AOF 重写
。 aof_rewrite_buf_blocks 链表不为空，存储 AOF 重写缓冲区内容
如果在配置文件中设置 no-appendfsync-on-rewrite 为 yes，那么重写期间可能会暂停 AOF 文件的 fsync 操作。

appendonly yes               # 开启AOF
appendfilename "appendonly.aof" # ROF文件名
appendfsync everysec         # 写入磁盘策略

no-appendfsync-on-rewrite no ## 重写期间是否临时关闭fsync
auto-aof-rewrite-percentage 100 ，“ # ROF文件增长到原来多少百分比时触发重写
auto-aof-rewrite-min-size 64mb   ## ROF文件最小多大时才允许重写

AOF 文件存储的是什么类型的数据?
AOF 文件存储的是 Redis 服务器接收到的写命令数据，以 Redis 协议格式保存。

这种格式的特点是，每个命令以*开头，后跟参数的数量，每个参数前用 $ 符号，后跟参数字节长度，然后是参数
的实际内容。

No. 611 261




## 第 62 页


四     mys            i       十

Yourappis out of date and some features may not work as expected. Please update immediately.

itwanger2

AOF重写期间命令可能会写入两次，会造成什么影响?

AOF 重写期间命令会同时写入现有AOF文件和重    区，这种机制是
问题。





## 第 63 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

操作命令| 。 写日志

AOF组存                 AOF缓存
Redis数据                                                              Redis数据 | ;内存

因为新旧文件是分离的，现有命令写入当前 AOF 文件，重写缓冲区的命令最终写入新的 AOF 文件，完成后，新文
件通过原子性的 rename 操作替换旧文件。两个文件是完全分离的，不会导致同一个 AOF 文件中出现重复命

1. java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: 为什么 redis 快，淘汰策略 持久化

2. java 面试指南(付费) 收录的快手面经同学 7 Java 后端技术一面面试原题: 说一下 Redis 的持久化方
导
式

3. java 面试指南(付费) 收录的小公司面经合集同学 1 java 后端面试原题: Redis 的持久化方式? RDB
和 AOF 的区别? Redis 宕机哪种恢复的比较快?

4. java 面试指南 (付费) 收录的美团面经同学 18 成都到家面试原题: redis 持久化

5. Java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: redis持久化机制

6. java 面试指南 (付费) 收录的 OPPO 面经同学 1 面试原题: Redis持久化方案

7. java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: Redis的基本数据类型? Redis的持久化

8. java 面试指南(付费) 收录的滴滴面经同学 3 网约车后端开发一面原题: Redis持久化

9. Java 面试指南 (付费) 收录的快手面经同学 1 部门主站技术部面试原题: Redis数据的可靠性怎么保
证? AOF重写期间命令可能会写入两次，会造成什么影响?

memo: 2025年5月4日修改至此，今天有球友发信息说把并发编程和JVM 的面渣逆袭都打印成纸质版了，说实
话，这个封面的颜值我也很喜欢，哈哈。

No. 631261




## 第 64 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

) 并发编程篇

三分恶|沉默王二修订版

AN

还是看纸质版心里踏实

用

昨天 下午3:33

11.RDB 和AOF 各自有什么优缺点?

RDB 通过 fork 子进程在特定时间点对内存数据进行全量备份，生成二进制格式的快照文件。其最大优势在于备份
恢复效率高，文件紧凑，恢复速度快，适合大规模数据的备份和迁移场景。

No. 641261




## 第 65 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

缺点是可能丢失两次快照期间的所有数据变更。

KL_
snapshot    Persistent     光一 ，
一站 workctedb         9 or aof   三

failed instance
委  _ 234 3 IEEFEEDEETDI               ER
append only file              Persisted (aof)

new instance

AOF 会记录每一条修改数据的写命令。这种日志追加的方式让 AOF 能够提供接近实时的数据备份，数据丢失风险
可以控制在 1 秒内甚至完全避免。

缺点是文件体积较大，恢复速度慢。

来个表格对比一下:
对比项           RDB (快照)                                                    AOF (命令日志
数据完整性 六 可能丢失几分钟数据 最多雪 1 秒数据
恢复速度 快 (直接加载二进制快照)                                  汉慢 (逐条replay)
文件大小 小 (压缩后)                                       X 大 (命令追加)
性能影响 低 (fork 后保存)                                   兴 较高《每次写都记录)
写入方式         定期全量写                                                     每次写命令就记录
适用场景         冷备份，灾难恢复                                              实时持久化，数据安全
默认状态           默认启用                                                                       Redis 7 默认也启用
重写机制         无                                                              有 (BGREWRITEAOF)
混合支持         Redis 4.0 后支持结合使用 (aof-use-rdb-preamble)

1. Java 面试指南 (付费) 收录的小公司面经合集同学 1 java 后端面试原题: Redis 的持久化方式? RDB
和 AOF 的区别? Redis 宕机哪种恢复的比较快?

12.RDB 和 AOF 如何选择?

在选择 Redis 持久化方案时，我会从业务需求和技术特性两个维度来考虑。

如果是缓存场景，可以接受一定程度的数据丢失，我会倾向于选择 RDB 或者完全不使用持久化。RDB 的快照方式
对性能影响小，而且恢复速度快，非常适合这类场景。

No. 651261




## 第 66 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

缓存命中，                     请
下   | | 直接从Redig读取          和 | Rs

sx户 Redis                  sx户 Redis | ，缓存缺失后，
从数据库读取数据

MySQL                                                              MySQL

但如果是处理订单或者支付这样的核心业务，数据丢失将造成严重后果，那么 AOF 就成为必然选择。通过配置每
秒同步一次，可以将潜在的数据丢失风险限制在可接受范围内。

大量高并发请求，使用
Redis处理，保证原子性

1 成功下单的 青求量少，
! 使用数据库处理

No. 661261




## 第 67 页


面渣逆袭 Redis篇第二版-让天下所有的面洼都能地装
在实际的项目当中，我更偏向于使用 RDB + AOF 的混合模式。

appendon1ly yes # 开启 RAOF
appendfsync everysec # 每秒刷盘一次
aof-use-rdb-preamble yes # 开启混合持久化，重启时优先加载 RDB，RDB 作为冷备，AOF 作为实时同步

1. java 面试指南 (付费) 收录的美团面经同学 18 成都到家面试原题: 什么时候用 rdb 什么时候用 aof

13.Redis如何恢复数据?

当 Redis 服务重启时，它会优先查找 AOF 文件，如果存在就通过重放其中的命令来恢复数据; 如果不存在或未启
用 AOF，则会党试加载 RDB 文件，直接将二进制数据载入内存来恢复。

人

Redis启动

|
[ 开启AOF? 站

否一存在RDB? < 一否-一存在AOF?
是                                              四

和   和   和

启动成荔 < 是加载成功? 否 >。 启动失败

如果 AOF 文件损坏的话，Redis 会党试通过 redis-check-aof 工具来修复 AOF 文件，或者直接使用 --repair
参数来修复。

redis-check-aof --repair appendonly.aof

虽然 Redis 还提供了 redis-check-rdb 工具来检查 RDB 文件的完整性，但它并不支持修复 RDB 文件，只能用来
验证文件的完整性。

redis-check-rdb dump.rdb

1. java 面试指南 (付费) 收录的美团面经同学 4 一面面试原题: Redis 内存中数据丢失怎么解决

No. 671 261




## 第 68 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

memo: 2025年5月5日修改至此，今天给球友修改简历时，碰到一个华科本硕的球友，985 高校又+1，目前国
内的 985 高校有 39 所，希望不久的将来，能全部集齐。惫

华中科技大学                          |                    硕士
华中科技大学             机械设且国 避皮其自动化         本科
14.二Redis 4.0 的混合持久化了解吗?
是的。

混合持久化结合了 RDB 和 AOF 两种方式的优点，解决了它们各自的不足。在 Redis 4.0 之前，我们要么面临 RDB
可能丢失数据的风险，要么承受 AOF 恢复慢的问题，很难两全其美。

eolis Nemory view

RPB + 4oF

1 Snepshot the dota

混合持久化的工作原理非常巧妙: 在 AOF 重写期间，先以 RDB 格式将内存中的数据快照保存到 AOF 文件的开
头，再将重写期间的命令以 AOF 格式追加到文件未尾。

AOFlog

国轩硬硬夺硬夺目而夺目面轩而看和
了               上

No. 681261




## 第 69 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭
这样，当需要恢复数据时，Redis 先加载 RDB 格式的数据来快速恢复大部分的数据，然后通过重放命令恢复最近
的数据，这样就能在保证数据完整性的同时，提升恢复速度。
如何设置持久化模式?
启用混合持久化的方式非常简单，只需要在配置文件中设置 aof-use-rdb-preamble yes 就可以了。

aof-use-rdb-preamble yes

你在开发中是怎么配置 RDB 和 AOF 的?
对于大多数生产环境，我倾向于使用混合持久化方式，结合 RDB 和 AOF 的优点。

## 启用AOF
appendonly yes

# 使用混合持久化

aof-use-rdb-preamble yes

# 每秒同步一次AOF，平衡性能和安全性

appendfsync everysec

# ROF重写触发条件: 文件增长100$且至少达到64MB
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# RDB备份策略

save 900 1   # 15分钟内有1个修改
save 300 10 ， # 5分钟内有10个修改
save 60 10000 # 1分钟内有10000个修改

对于单纯的缓存场景，或者本地开发，我会只启用 RDB，关闭 AOF:

# 禁用AOF
appendonly no

# 较宽松的RDB策略
save 3600 1   # 1小时内有1个修改
save 300 100 ”## 5分钟内有100个修改

而对于金融类等高一致性的系统，我通常会在关键时间窗口动态将 appendfsync 设置为 always :

No. 691261




## 第 70 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

## 启用AOF
appendonly yes

# 使用混合持久化

aof-use-rdb-preamble yes

# 每个命令都同步(谨慎使用，性能影响大)
# 通常我会在关键时间窗口动态修改为always

appendfsync always

# 更频繁的RDB快昭
save 300 1    # 5分钟内有1个修改
save 60 100 ， ## 1分钟内有100个修改

另外，对于高并发场景，应该设置 no-appendfsync-on-rewrite yes ，避免 AOF 重写影响主进程性能; 对于大
型实例，也应该设置 rdb-save-incremental-fsync yes 来减少大型 RDB 保存对性能的影响。

# ROF重写期间不fsync，ROF 重写期间，主进程不会对新写入的 AOF 缓冲区执行 fsync 操作 (即不强制刷盘) ，而
是等重写结束后再统一刷盘。

no-appendfsync-on-rewrite yes

# RDB 快照保存时采用增量 fsync，即每写入一定量的数据就执行一次 fsync，将数据分批同步到磁盘。

rdb-save-incremental-fsync yes

1. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: Redis 的持久化机制?

2. java 面试指南(付费)_收录的小公司面经合集同学 1 java 后端面试原题: Redis 宕机哪种恢复的比较
快?

3. java 面试指南(付费) 收录的美团面经同学 18 成都到家面试原题: 如何设置持久化模式

4. java 面试指南 (付费) 收录的美团面经同学 4 一面面试原题: 业界使用哪一种数据持久化，两种持久化

方法的优缺点
5. java 面试指南 (付费) 收录的作业帮面经同学 1 java 后端一面面试原题: 两种 Redis持久化机制可以混
合使用吗

memo: 2025年5月6 日修改至此，今天在修改球友简历时，碰到一个东北大学硕合肥工业大学本的球友，真的
非常优秀，也希望大家能够通过星球这个平台彼此激励，共同进步。
教育背景
。 东北大学 (985，推免) | 硕士 | “二三
获校一等奖学金 (2023-2025)
。 合肥工业大学 (211) | 学士 |   LL里 。
获校优秀毕业生，国家奖学金 (2022) ，校一等奖学金 (2020-2022)，校三好学生 (2020-2022)，

高可用
15.主从复制了解吗?

No. 701261




## 第 71 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

主从复制允许从节点维护主节点的数据副本。在这种架构中，一个主节点可以连接多个从节点，从而形成一主多从
的结构。主节点负责处理写操作，从节点自动同步主节点的数据变更，并处理读请求，从而实现读写分离。

Redis主从复制
站 see 一replicate-> 哆 3
MaStcr
[ 5 Slave cats 0 Save ZZ
主从复制的主要作用是什么?

第一，主节点负责处理写请求，从节点负责处理读请求，从而实现读写分离，减轻主节点压力的同时提升系统的并
发能力。

写操作同步              写操作同步

第二，从节点可以作为主节点的数据备份，当主节点发生故障时，可以快速将从节点提升为新的主节点，从而保证
系统的高可用性。

No. 711261




## 第 72 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Sentinel2                                     Sentinel3

什么情况下会出现主从复制数据不一致?

Redis 的主从复制是异步进行的，因此在主节点宕机、网络波动或复制延迟较高时会出现从节点数据不同步的情
况。

No. 72 1 261




## 第 73 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

发送命令: SET

将命令追加到
AOF 缓冲区

将命令追加到
复制积压缓冲区

将命令追加到
slave 对应 client 的缓冲区

返回响应

从slave 对应 client的缓冲区
读取命令，发送命令

比如主节点写入数据后宕机，但从节点还未来得及复制，就会出现数据不一致。

时间线: ~

客户端”” 向主节点 SET user:1 二哥    -~ 主节点处理成功
二
正准备推送给从节点 (异步复制) . . 。但还没推送完 闪
二

一 突然主节点宕机 (机器死机、断网) 衣 一

上

Sentinel 监测到故障，failover: 将从节点提升为新主节点 钨

上

客户端继续请求: GET user:1 ? -，从节点返回: 空 尖 (数据没同步过来)

另一个容易被忽视的因素是主节点内存压力。当主节点内存接近上限并启用了淘汰策略时，某些键可能被自动删
除，而这些删除操作如果未能及时同步，就会造成从节点保留了主节点已经不存在的数据。

No. 731261




## 第 74 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Slave有效时间区间

主从复制数据不一致的解决方案有哪些?

首先是网络层面的优化，理想情况下，主从节点应该部署在同一个网络区域内，直免跨区域的网络延迟。

其次是配置层面的调整，比如说适当增大复制积压缓冲区的大小和存活时间，以便从节点重连后进行增量同步而不
是全量同步，以最大程度减少主从同步的延迟。

rep1-backlog-size lmb # 默认值 1MB，表示主节点的复制缓冲区大小
rep1-backlog-tt1 3600 # 默认值 3600 秒，表示主节点的复制缓冲区存活时间

第三是引入监控和自动修复机制，定期检查主从节点的数据一致性。

比如说通过比较主从的 offset 差值判断从库是否落后。一旦超过设定阔值，就将从节点剔除，并重新进行全量同
步。

No. 741261




## 第 75 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二
是
1. Java 面试指南 (付费) 收录的得物面经同学 1 面试原题: Redis 分布式，主从，一个节点挂掉怎么办

2. java 面试指南(付费) 收录的小米面经同学 F 面试原题: redis 的主从架构和主从哨兵区别

3. java 面试指南 (付费) 收录的收钱吧面经同学 1 java 后端一面面试原题: Redis解决单点故障主要靠什
么? 主从模式用的是异步还是同步?

memo: 2025年5月7 日修改至此，今天在修改球友简历时，收到了球友对简历修改的认可:“现在这份简历应该
比较完美了"，完美这个词我觉得襄奖的有点多了，哈哈，不过我还是很开心的。

Re:回复: 二哥求帮忙看看简历 门 户 〇 时 。 外安全浏览模式
发件人: 围巾 评"1aqq.com> 十

收件人: 入 沉默王二<www.qing_gee@163.com> +

时 间: 2025年05月07日 17:53 (星期三)

附 件: 1个( 250507 。忠w” 霹端工程师-]ava.pdf ) 查看附件

【升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

感谢二哥，前两天有些忙，没来得及改简历哈哈

型在这份简历应该比较完美了! 本来在想一个项目是不是有些少，但是现在一页已经放不下了哈哈，那也无所谓了。
导师最近事情还是有点小多，所以打算接下来一两个月找一找实习，争取7-9月完成一段三个月的实习。

再次感谢!

16.Redis主从有几种常见的拓扑结构?

No. 751261




## 第 76 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

主要有三种。

最基础的是一主一从，这种模式适合小型项目。一个主节点负责写入，一个从节点负责读和数据备份。这种结构虽
然简单，但维护成本低。

Redis-六

|

Redis-B
一主一从结构

随着业务增长，读请求增多，可以考虑扩展为一主多从结构。主节点负责写入，多个从节点还可以分摊压力。

Redigs-从         一一        Redis-E

Redis-B                          Redis-C                               Redis-D

一主多从《〈星形) 结构

在跨地域部署场景中，树状主从结构可以有效降低主节点负载和需要传送给从节点的数据量。通过引入复制中间
层，从节点不仅可以复制主节点数据，同时可以作为其他从节点的主节点继续向下层复制。

No. 761 261




## 第 77 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

及cdis-信

一个

Redis-B

忆

Redis-D                    Redis-己

Redis-C

树状主从结构

17.Redis的主从复制原理了解吗?

了解。

Redis 的主从复制是指通过异步复制将主节点的数据变更同步到从节点，从而实现数据备份和读写分离。这个过程
大致可以分为三个阶段: 建立连接、同步数据和传播命令。

主实例                            从实例
(172.16.19.3) 第一阶段: 建立连接，协商同步 《172.16.19.5)
psync ? -1                               执行 slaveof 172.16.19.3 6379
+FULLRESYNC {runlID} {offset}                       保存主节点信息
.人           第二阶段: 主库同步数据给从库
RDB                   _
发送RDB文件                               清空现有数据
加载RDB

第三阶段: 主库发送新写命令给从库
发送repl buffer

乓             加载repl buffer

在建立连接阶段，从节点通过执行 replicaof 命令连接到主节点。连接建立后，从节点向主节点发送 psync 命
令，请求数据同步。这时主节点会为该从节点创建一个连接和复制缓冲区。

No. 771261




## 第 78 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

同步数据阶段分为全量同步和增量同步。当从节点首次连接主节点时，会触发全量同步。

No. 781261




## 第 79 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

slave 收到 client 发送的命令:

SLAVEOF

slave
第1次
进行复制

Yes                                                                                           No

slave 向 master                                          slave 向 master
发送命令:                                                   发送命令:
PSYNC ?-1                                         PSYNC <run ID> <offset>
master
返回结果:
|下

+CONTINUE
?3

在这个过程中，主节点会 fork 一个子进程生成 RDB 文件，同时将文件生成期间收到的写命令缓存到复制缓冲区。
然后将 RDB 文件发送给从节点，从节点清空自己的数据并加载这个 RDB 文件。等 RDB 传输完成后，主节点再将
缓存的写命令发送给从节点执行，确保数据完全一致

No. 791261




## 第 80 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

主实例172.16.19.3

执行besave生成rdb

同时写入repl buffer和
replbacklog_buffer

repL_backlog_buffer

Psync? -

第一阶段: 建立连接，协商同步

从实例172.16.19.4

FUURESYNC{runid} foffset

发送rdb文件

第二阶段: 主库全量同步数据到从库

发送replication_buffer

第三阶段: 主库增量同步数据到从库

Psync? -

第一阶段: 建立连接，协商同步

FUURESYNC{munid} foffset

发送rdb文件

第二阶段: 主库全量同步数据到从库

发送replication_buffer

第三阶段: 主库增量同步数据到从库

执行eplicaof 172.16.19.3
|                                  保存主节点信息
芭|                                  清空现有数据，加载rdb
                                   加载repLbuffer

从实例172.16.19.5

执行eplicaof 172.16.19.3
芭                                  保存主节点信息
|                                  清空现有数据，加载rdb
|                                   加载replbuffer

主从完成全量同步后，主要依靠传播命令阶段来保持数据的增量同步。主节点会将每次执行的写命令实时发送给所

有从节点。

全量

}-

1 同步全令; SYNC

3 传痊RDB 文件

| ] mm 人

LU
1
1
1
1

反馈: RDB 文件加载完毕                  症

4 发庆缓冲区内的 write 命令[命令传潘)

1 CPU
.内存
IO

人 生成 RDB 文件: BGSA

启动绥站区记录从现在开始的所有 write 命令

1网络IO

Redis 2.8 版本后，主节点会为每个从节点维护一个复制积压缓冲区，用于存储最近的写命令。

No. 801261




## 第 81 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

增量复制时，主节点会把要同步的写命令暂存一份到复制积压缓冲区。这样当从节点和主节点发生网络断连，从节
点重新连接后，可以从复制积压缓冲区中复制尚未同步的写命令。

No. 811 261




## 第 82 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

《一>

主从同步
主库                                                                       从库
10.43.1100 《一一>》 10.431200
〇〇            一
repl_backlog_buffer                     <人一>
网络恢复

master_repl_offset                           psync runid offset                        Slave_repl_offset

continue

offset 有效

发送网络断开期间的写命令

memo: 2025年5月8日修改至此，今天有球友在星球里发
经，我看题目主要集中在技术派项目和MySQL、 计算机网络的八股上。

地                                                                                                二 收进专栏

腾讯CSIG实习offer

timeline:
4.9 投递”4.14 一面 4.16 二面” 4.22 三面 4.29 四面HR面”5.6 发offer

经见图片

18.详细说说全量同步和增量同步?

全量同步会将主节点的完整数据集传输给从节点，通常发生在从节点首次连接主节点时。

No. 82 1 261




## 第 83 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

1.psync?-1l
2.+FULLRESYNC
{renId}{foffset}
未
 save masterInfo
slavc
0             5 sendRDB
亏
6. send buffer

7. fush old dqata

然后 fork 一个子进程生成 RDB 文件，并将新的写命令存入复制缓冲区。

从库收到 RDB 文件后，清空旧数据并加载新的 RDB 文件。加载完成后，从节点会向主节点回复确认消息，主节点
再将复制缓冲区中的数据发送给从节点，确保从节点的数据与主节点一致。

全量同步的代价很高，因为完整的 RDB 文件在生成时会占用大量的 CPU 和磁盘 IO; 在网络传输时还会消耗掉不

二
少带宽。

于是 Redis 在 2.8 版本后引入了增量同步的概念，目的是在断线重连后避免全量同步。
增量依赖三个关键要素:

No. 831261




## 第 84 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭
亿、复制偏移量: 主从节点分别维护一个复制偏移量，记录传输的字节数。主节点每传输 N 个字节数据，自身的
复制偏移量就会增加 N; 从节点每收到 N 个字节数据，也会相应增加自己的偏移量。

@@、主节点1D: 每个主节点都有一个唯一ID，即复制 ID，用于标识主节点的数据版本。当主节点发生重启或者角
变化时，ID 会改变。

图、复制积压缓冲区: 主节点维护的一个固定长度的先进先出队列，默认大小为 1M。主节点在向从节点发送命令
的同时，也会将命令写入这个缓冲区。

当从节点与主节点断开重连后，会发送 psync{runId} {foffset} 命令，带上之前记录的主节点 ID 和复制偏移

_             1. Connection losr              | -人

3.Connection to mastet      >
slave             4. Psync {foffser frenid}   4

6380

5. CONTIINUE

6. send Partial data

主节点收到这个命令后，会检查 runld 和 offset:
如果主节点 ID 与从节点提供的 runld 不匹配，说明主节点已经变化，必须进行全量同步。
如果 ID 匹配，主节点会查找从节点请求的偏移量之后的数据是否还在复制积压缓冲区。

如果在，只发送从该偏移量开始的增量数据，这就是增量同步; 否则说明断线时间太长，积压缓冲区已经覆盖了这
部分数据，需要全量同步。

No. 841261




## 第 85 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Master                                   Slave
172.16.88.1                                172.16.88.2
风光站sr
repl_backlog 环形|   ，主有            frepl
重连后同时写入 replication                      全0509
“buffer 缕冲区                          多                               2 恢复连接
3.psync [runID] [offsef]
4.continue
6执行断开重连后
Feplicafion           5发送slave_repl_offset 之后的           的兽量命令
buffer:                操作
CUJNUUNUUNG

增量同步的优势显而易见: 只传输断线期间的命令数据，大大减少了网络传输量和主从节点的负载，从节点也不需
要清空重载数据，能更快地跟上主节点状态。

对于写入频繁或网络不稳定的环境，应该增大复制积压缓冲区的大小，确保短时间断线后能进行增量同步而不是全
量同步。

rep1-backlog-size lmb # 默认值 1MB，表示主节点的复制缓冲区大小
rep1-backlog-tt1 3600 # 默认值 3600 秒，表示主节点的复制缓冲区存活时间

memo: 2025年5月9 日修改至此，今天在修改球友简历时，碰到一个河北大学硕东华理工大学本的球友，希望
这个大家庭能给大家带来更多的帮助和支持。

教育背景

河北大学 计算机科学与技术                                                                                人
网络安全与计算机学院                                                                                                                 河北
GPA:3.5/4.0 个人荣誉 : 研究生三等奖学金喇s" 二4)

东华理工大学 - 通信工程                                        231127， :9F?
信息工程学院                                                                                                                             江西

个人荣誉 : 三等奖学金(只 ss2，信息技术大赛省二等奖，英语6级证书

19.主从复制存在哪些问题呢?

Redis 主从复制的最大挑战来自于它的异步特性，主节点处理完写命令后会立即响应客户端，而不会等待从节点确
认，这就导致在某些情况下可能出现数据不一致。

No. 851261




## 第 86 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

开始记录                               1 发送sync指令

站

2. 发送RPB文件

司令                                                                                                                                      3 应用到内存
Redis Master                                                                                               Redis slave

14.接收缓冲区命令                                             接收缓冲区

另一个常见问题是全量同步对系统的冲击。全量同步会占用大量的 CPU 和 IO 资源，尤其是在大数据量的情况下，
会导致主节点的性能下降。
脑裂问题了解吗?

在 Redis 的哨兵架构中，脑裂的典型表现为; 主节点与哨兵、从节点之间的网络发生故障了，但与客户端的连接是
正常的，就会出现两个"主节点"同时对外提供服务。

哨兵认为主节点已经下线了，于是会将一个从节点选举为新的主节点。但原主节点并不知情，仍然在继续处理客户
端的请求。

|
哨兵
T1
丢失数据< TH2 |                                                            0
重复忆入<一He一                               主从切换结束
T4
了

等主节点网络恢复正常了，发现已经有新的主节点了，于是原主节点会自动降级为从节点。在降级过程中，它需
与新主节点进行全量同步，此时原主节点的数据会被清空。导致客户端在原主节点故障期间写入的数据全部丢失。

No. 861261




## 第 87 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

EI E 到
时间

计  发生阻塞，不
响应哨兵心跳
判断客观下线，
t2                                                           开始主从切换
1 | 。 阻塞结束，客户
端又写入新数据
计4           升级为新主库    主从切换结束

t5 | 降级为从库，和新
主库全量同步，清
空本地数据库，t93
时新写数据丢失

为了防止这种数据丢失，Redis 提供了 min-slaves-to-write 和 min-slaves-max-lag 参数。
这两个参数可以设置最少需要多少个从节点在线，以及从节点的最大延迟时间。

# 设置主节点能进行数据同步的最少从节点数量
min-slaves-to-wLite 1
## 设置主从节点间进行数据同步时，从节点给主节点发送 AcK 消息的最大延迟 (以秒为单位)

min-slaves-max-lag 10
设置这两个参数后，如果主节点连接不到指定数量的从节点，或者从节点响应超时，主节点会拒绝写入请求，从而
避免脑裂期间的数据冲突。

具体来说，当网络分区发生，主节点与从节点、哨兵之间的连接断开，但主节点与客户端的连接正常时，由于主节
点无法再连接到任何从节点，或者延迟超过了设定值，比如说配置了 min-slaves-to-write 1 ，主节点就会自动
拒绝所有写请求。

同时在网络的另一侧，哨兵会检测到主节点"下线"，选举一个从节点成为新的主节点。由于原主节点已经停止接受
写入，所以不会产生新的数据变更，等网络恢复后，即使原主节点降级为从节点并进行全量同步，也不会丢失网络
分区期间的写入数据，因为根本就没有新的写入发生。

1. java 面试指南 (付费) 收录的同学 30 腾讯音乐面试原题: 主从复制有什么缺点呢? redis的脑裂问题

memo: 2025年5 月 10 日今天把新项目的前置环境也配的七七八了，还差一个 Kafka 的安装教程。日拱一
卒，争取秋招前给大家球友们见面。

No. 871 261




## 第 88 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

4拓陪明环境播建指南 (新人必看) 外                                                 DAsmS 29 本 em
2 。 export MINIO_ROOT_USER=minioadmin
3 。 export MINIO_ROOT_PASSWORD=minioadmin                                                 大用 @ :=
4
5 。 # 启动 MinI0 服务                                                             一、安装Java 17
6 minio server ~/minio/data 一consote-address ":9991"                                        Lan 的 macOS 安装步要
验证安装

二哥的 macOS 安装方式
二、安装 MySQL
* Lan 的 安装步对

访问 Minlo 控制台: http://192.168.0113.55624
使用凭据登录
。 用户名: minioadmin

验证安装
。宇码: minioadmin                                                        本
创建数据库和用户
创建 Minlo 的 Bucket                                                                                三、 安装 Elasticsearch
四安装Redis
五、安装Minlo
Minio 中的 Bucket (栖) 是对象存储的核心慨念之一，它相当于传统文件系统中的"文件实"或“目录"，是存储对象 (Object) 的容器 本的安装上
|    Lan 的安装步骤
我们可以创建一个 uploads 的概，它的名字和 yml 配置文件中 bucketName 相同就可以了-                                           创建 Minio 的 Bucket
安半Kafla
安装步对
冒 create eucket                                     一
下
Minlo uses buckets to ，     加网
vewauaatnanrgmuos                                                                        fllesystem, where each      1 创建数据库表结构          由

20.Redis哨兵机制了解吗?
Redis 中的哨兵用于监控主从集群的运行状态，并在主节点故障时自动进行故障转移。

Redis Sentinel

哨兵节点

Settine-

Redis服务节点
监毛/

核心功能包括监控、通知和自动故障转移。哨兵会定期检查主从节点是否按预期工作，当检测到主节点故障时，就
在从节点中选举出一个新的主节点，并通知客户端连接到新的主节点。

No. 881261




## 第 89 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

# 监控的主节点信息 + 多少个哨兵同意才算宕机
sentinel monitor mymaster 127.0.0.1 6379 2

# 多久不响应就标记为“主观下线”

Sentinel down-after-milliseconds mymaster 5000

# 故障转移超时时间

sentinel failover-timeout mymaster 60000
# 同时允许多少个从节点同步新主节点数据

sentinel parallel-syncs mymaster 1
1. Java 面试指南 (付费) 收录的比亚迪面经同学 1 面试原题: Redis 的哨兵机制了解吗?

21.Redis哨兵的工作原理知道吗?

哨兵的工作原理可以概括为 4 个关键步骤: 定时监控、主观下线、领导者选举和故障转移。

首先，哨兵会定期向所有 Redis 节点发送 PING 命令来检测它们是否可达。如果在指定时间内没有收到回复，哨兵
会将该节点标记为主观下线"。

“nn

、~<--------r----v-

人
1                                    Monitor                               1                                   oa
4                                         1                                       】
/                                                       1                          1
Monitor                                                                                              \                                               1
4                                                           下
7                                                                           Monitor                           〗
7                           、 client 》

1
，                      Replicate      Replicate                                                   S           7
《
4
4

当一个哨兵判断主节点主观下线后，会询问其他哨兵的意见，如果达到配置的法定人数，主节点会被标记为客观
下线"。

No. 891261




## 第 90 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

客观下线
主节点
主        Sentnel-B      |
|
Sentinel人“全询问”SentinelC 超过
quornums>
司

继续询问

然后开始故障转移，这个过程中，哨兵会先选举出一个领导者，领导者再从从节点中选择一个最适合的节点作为新
的主节点，选择标准包括复制偏移量、优先级等因素。

收到2?票: Sentinel 2、     选举sentinel1

Sentinel 1                                Sentinel 3                           本
收到1票: Sentinel1     选举sentinel1

Sentinel 2                                                                        交
收到o票                       选举Sentinel1

Sentinel 3                                                                        四

确定新主节点后，哨兵会向其发送 SLAVEOF NO ONE 命令使其升级为主节点，然后向其他从节点发送 SLAVEOF 命
令指向新主节点，最后通过发布/订阅机制通知客户端主节点已经发生变化。

Sentinel1                         Sentinel-2                           Sentinel-3

No. 901261




## 第 91 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

172.16.101.59                          ，                             172.16.101.58                           ，                              172.16.101.60
Replicate                                                                    Replicate

Slave_1:6379                                                                  Master:6379                                                                    Slave 2:6379

eaalw ite
                         3

Sentinel3

172.16.101.59                                             172.16.101.58                                              172.16.101.60

Replicate
Master6379                                                                slave 1:6379                                                                  slave 2:6379

Replicate

在实际部署中，为了保证哨兵机制的可靠性，通常建议至少部署三个哨兵节点，并且这些节点应分布在不同的物理
机器上，降低单点故障风险。

No. 911261




## 第 92 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

同时，法定人数的设置也非常关键，一般建议设置为哨兵数量的一半加一，既能确保在少数哨兵故障时系统仍能正
常工作，又能避免网络分区导致的脑裂问题。

1. Java 面试指南 (付费) 收录的 OPPO 面经同学 1 面试原题: Redis的Sentinel和Cluster怎么理解? 说一
下大概原理

memo: 贴一个读者对java 进阶之路的美赞吧，我也是人，也需要大家的情绪共鸣，哈哈，就让赞美多一点吧惫
E  Liouyi                                             号0
过了一遍菜鸟编程的java和w3c schoo的
java，再看二哥的java进阶之路的内容，写
的真好力轿响
曲 沉默王二                                      号0
哈哈，这种误奖我收了后

22.Redis领导者选举了解吗?

No. 92 1 261




## 第 93 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis 使用 Raft 算法实现领导者选举，目的是在主节点故障时，选出一个哨兵来负责执行故障转移操作。

时间            S1                  S2                 匀
我要成为领导者
几                                           给自己投一票，向
T1     S2、S3 发起投票
我要成为领导才                                      训
不同意                                    给自己投 1 票，向
S2、S3 发起投票
二哥的 Jdva 进阶之路              收到 S1 的投票回收到 S1的投票，
我要成为领导者              0
不同意                                                     T4 。”收到 S3 的投票， 收到 S3 的投票，
回复 N             回复 N
2票Y，1票 N，
T5       成为Leader                       1票N, 1票Y
选举过程是这样的:

人中、当一个哨兵确认主节点客观下线后，会向其他哨兵节点发送请求，表明希望由自己来执行主从切换，并让所有
其他哨兵进行投票。候选者会先给自己先投 1 票，然后等待其他哨兵节点的投票结果

// sentinel.c中的sentinelRAskMasterStateTootherSentine1s国数

void sentinelRskMasterStateToOtherSentinels(sentinelRedisInstance *master) {
dictIterator *di
dictEntry *dey

di = dictGetIterator(master->sentinels))
while((de = dictNext(di)) != NULL) {
sentinelRedisInstance *sentinel = dictGetVal(de) 7

int retval7

// 只有在进入领导者选举阶段才发送投票请求
让 (master->failover_state == SENTINEL_FRAILOVER_STRATE_SELECT LERADER) {
// 发送特殊的is-master-down-by-addr命令请求投票
retval = redisRsyncCommand(sentinel->ccy
sentinelReceiveVoteFromSentine1l，sentinel，
"SENTINEL is-master-down-by-addr %s sd 8l1lu ss"，
master->addr->ip，master->addr->port，
(unsigned long long)master->failover_epoch,
// 这里发送自己的runiqd请求投票
sentinelGetMyRunID() ) 1;
} else {
// 否则只询问主节点状态，不请求投票
retval = redisRAsyncCommand(Ssentinel->ccy
sentinelReceiveIsMasterDownReply，sentinel，
"SENTINEL is-master-down-by-addr ss sd &11u *"，
master->addr->ip，master->addr->port，
(unsigned long long)0)7

No. 931261




## 第 94 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

dictReleaseIterator(di) 7

@@、收到请求的哨兵节点进行判断，如果候选者的日志和自己的一样新，任期号也小于自己，且之前没有投票过，
就会投同意票 Y。否则回复 N。

// sentinel.c中的sentinelCommand函数部分(处理SENTINEL命令)
// 处理is-master-down-by-addr命令
else if (!strcasecmp(c->argv[1]->ptr, "is-master-down-by-addr")) {
V/x* SENTINEL IS-MASTER-DOWN-BY-ADDR <ip> <port> <current-epoch> <runid> */
sentinelRedisInstance *rii
char *master_ip = c->argv[2]->pPtr17
int master_port = atoi(c->argv[3]->Ptr) 7
long long req_epoch = strtoull(c->argv[4]->pPtr,NULL,10) 7
char *req_runid = c->argv[5]->ptr)
int isdown = 07
char xleader = “x"1
long long leader_epoch

1
1
己

ri = sentinelGetMasterByRddress(master_ip，master_port);
if (zi) {
isdown = ri->flags & SRI_S_DOWN;

// 判断是否是投票请
if (req_runid[0] !=  *') {
// 检查是否已经在当前配置纪元中投过票
if (req_epoch > sentinel.current_epoch) {
// 更新自己的配置纪元

sentinel.current_epoch = req_epoch;

// 如果我们觉得主节点下线了，且在这个epoch还没投过票，则投票
ifE (isdown && sentinel.current_epoch == req_epoch &&
sentinel.leader_epoch < req_epoch)

// 记录投票信息

sentinel.leader_epoch = req_epoch;
sentinel.leader =- sdsnew(req_runid) 1
leader = req_runiqd;

leader_epoch = req_epoch;

// 返回投票结果
addReplyMultiBulkLen(c,3) 7
addReplyLongLong(c，isdown) 7
addReplyBulkCString(c，1leader)
addReplyLongLong(c，1leader_epoch)

No. 941261




## 第 95 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

@@、候选者收到投票后会统计自己的得票数，如果获得了集群中超过半数节点的投票，它就会当选为领导者。

// sentinel.c中的sentinelReceiveVoteFromSentine1函数
void sentinelReceiveVoteFromSentinel(redisRsyncContext *c，void *reply，void *privdata) {
sentinelRedisInstance *sentinel = privdatay
sentinelRedisInstance *master = sentinel->master)
redisReply *r = reply;
char *leader = NULL7

// 处理回复

if (z->type == REDIS_REPLY _RRRRY && ->elements == 3) {
// 解析回复中的leader信息
if (z->element[1]->type == REDIS_REPLY_STRING)

leader = r->element[1]->str'

// 检查是否投给了我们
if (leader &g& strcmp(leader，sentinelGetMyRunID() )

// 记录获得一票
dictadd(master->sentinels_voted，sdsnew(sentinel->runid)，sentinel)7

0)

// 检查是否获得多数票
if (master->failover_state == SENTINEL_FRILOVER_STRTE_SELECT_ LEADER) {

int voters = dictSize(master->sentinels) + 1; // +1是因为包括自己
int votes = dictSize(master->sentinels_voted) + 1; // 自己也算一票

// 如果获得多数票(大于一半)

if (votes >= Voters/2+1) {
// 成为领导者，开始执行故障转移
SentinelEVent(LL_NWRRNING，"+elected-leader"，master， "se@") 7
master->failover_state = SENTINEL_FRAILOVER_STRTE_FRAILOVER_IN_PROGRESS)
sentinelFailoverSelectSlave(master);

@、如果没有哨兵在这一轮投票中获得超过半数的选票，这次选举就会失败，然后进行下一轮的选举。为了防止无
限制的选举失败，每个哨兵都会有一个选举超时时间，且是随机的。

// sentinel.c中的sentinelFailoverSelectLeader团数
void sentinelFailoverSelectLeader(sentinelRedisInstance *master) {

// 检查选举是否超时

mstime t election timeout = SENTINEL_ELECTION_TIMEOUT * 27

if (mstime() - master->failover_start_time > election timeout) {
// 选举超时，重置状态
sentinelEvent(LL_NRRNING，"-failover-abort-timeout"，master， "gs8@") 17

sentinelRbortFailover(master))
returny

No. 951261




## 第 96 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

. 。其他选举逻辑 .. .

// 如果没有足够票数且未超时，则继续等待
】}

这里 SENTINEL_ELECTION_TIMEOUT_MIN 通常为 0，SENTINEL_ELECTION_TIMEOUT_MAX 通常为 2000 毫秒。
这样每个哨兵会在 0-2 秒的随机时间后开始选举，减少选举冲突

推荐阅读: Raft算法的选主过程详解

1. java 面试指南 (付费) 收录的8 后端开发秋招一面面试原题: raft主节点挂了怎么选从节点
memo: 2025年5月12 日修改至此，今天有球友发微信说拿到了三个大厂的 offer，分别是蚂蚁、美团和腾讯，
真的是太优秀了呀。

又来麻烦您啦，帮忙看看

offer

我还是比较喜欢忽的，但是劝退的
人太多了感党

想听听二哥的见    解

15:50

No. 961261




## 第 97 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

|
攻a。 攻e

13:37

攻。 区

好哺好嘲二哥

23.新的主节点是怎样被挑选出来的?

哨兵在挑选新的主节点时，非常精细化。

No. 971 261




## 第 98 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

从节点列表

|

过泪

slave-PHOSt                        忆

有最拓节个               和

|

复制偏移得最
天第3 一 症一> 选择完竺

|

选绎runid最小的节点

首先，哨兵会对所有从节点进行一轮基础筛选，排除那些不满足基本条件的节点。比如说已下线的节点、网络连接
不稳定的节点，以及优先级设为 0 明确不参与挑选的节点。

// 第一轮筛选: 排除不满足基本条件的从节点
for (int i = 0;) 奔< numslaves; i++) {
sentinelRedisInstance *slave = slaves[il];

// 排除已下线的从节点
if (slave->flags & (SRI_S_DOWN|SRI_O_DOWN)) continuey
// 排除断开连接的从节点

if (slave->link->disconnected) continuei

// 排除近期 (5秒内) 断过连的从节点

if (mstime() - slave->link->last_avail time > 5000) continuey

// 排除未建立主从复制的节点

if (slave->slave_priority == 0) continuey
// 找到第一个满足条件的从节点

selected = ii
breaky

No. 981261




## 第 99 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

然后，哨兵会对剩下的从节点进行排序，选出最合适的主节点。

// sentinel.c中的compareSlaves团数
int compareSlaves(sentinelRedisInstance *a， SentinelRedisInstance *b) {
// 1. 首先比较用户设置的优先级，值越小优先级越高
if (a->slave_priority !=- b->slave_priority)
return (a->slave_priority < b->slave_priority) ? 1 : 2;

// 2如果优先级相同，比较复制偏移量，偏移量越大数据越新
if (a->slave_repl_offset > b->slave_repl_offset) return 17
else if (a->slave_repl_offset < b->slave_repl_offset) return 2)

// 3。 如果复制偏移量也相同，比较运行ID的字典序

return (strcmp(a->runid，b->runid) < 0) ? 1 : 21

排序的标准有三个:

人中、从节点优先级: slave-priority 的值越小优先级越高，优先级为 0 的从节点不会被选中。
人@、复制偏移量: 偏移量越大意味着从节点的数据越新，复制的越完整。

图、运行1D: 如果优先级和偏移量都相同，就比较运行 ID 的字典序，字典序小的优先。

选出新主节点后，哨兵会向其发送 SLAVEOF NO ONE 命令将其提升为主节点。

// sentinel.c中的sentinelFailoverPromoteSlave国数

void sentinelFailoverPromoteSlave(sentinelRedisInstance *master) {

// .. .选择最佳从节点的逻辑 ...

// 向选中的从节点发送SLAVEOF NO ONE命令，使其成为主节点

retval = redisRsyncCommand(slave->link->ccy
sentinelReceivePromotionResponseFromslave，master/
"SLRVEOF NO ONE") 7

// 更新状态
master->promoted slave = slavei
slave->flags |= SRI_PROMOTED)
// 记录日志

SentinelEVvent(LL_WRRNING， "+Promoted-slave"，Sslave，"S$@") 7
sentinelEvent (LL_WRRNING， "+failover-state-wait-promotion"，master，"se@") 7

之后，哨兵会等待新主节点的角色转换完成，通过发送 INFO 命令检查其角色是否已变为 master 来确认。确认成
功后，会更新所有从节点的复制目标，指向新的主节点。

SLRVEOF new-master-ip new-master-Port

memo: 2025 年5 月 13 日，今天有球友发微信说拿到了携程的 offer，携程现在也是第二梯队的互联网大厂了，
值得一手恭喜啊。

No. 991261




## 第 100 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥二哥，想请教下，携程的 硬”‖ 部门和华为

”让端手表线，咱选哇
2 有
=夺
E

om 圭

主要感觉华为算是核心部门图

还得谢谢二哥，全靠面渣逆袭

24.Redis集群了解吗?
主从复制实现了读写分离和数据备份，哨兵机制实现了主节点故障时自动进行故障转移。

No. 1001261




## 第 101 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

集群架构是对前两种方案的进一步扩展和完善，通过数据分片解决 Redis 单机内存大小的限制，当用户基数从百万
增长到千万级别时，我们只需简单地向集群中添加节点，就能轻松应对不断增长的数据量和访问压力。

比如说我们可以将单实例模式下的数据平均分为 5 份，然后启动 5 个 Redis 实例，每个实例保存 5G 的数据，从而
实现集群化。

实例1                   实例2              实例3                实例4            实例5

25.请详细说一说Redis Cluster? (补充)

2024年 04 月 26 日新增

Redis Cluster 是 Redis 官方提供的一种分布式集群解决方案。其核心理念是去中心化，采用 P2P 模式，没有中心
节点的概念。每个节点都保存着数据和整个集群的状态，节点之间通过 gossip 协议交换信息。

No. 1011 261




## 第 102 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Redis Cluster

read/write                            replication

在数据分片方面，Redis Cluster 使用哈希模机制将整个集群划分为 16384 个单元。

例如，如果我们有 4 个 Redis 实例，那么每个实例会负责 4000 多个哈希模。

No. 1021 261




## 第 103 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Slots                                                                                  Node

0-4095                                                                         Node #O
4096 - 8191                                                                    Node 拉
8.192 -12.287                                                                      Node #2
12,288 - 16,384                                                                      Node #3

在计算哈希槽编号时，Redis Cluster 会通过 CRC16 算法先计算出键的哈希值，再对这个哈希值进行取模运算，得
到一个0到 16383 之间的整数。

slot = CRC16(key) mod 16384

这种方式可以将数据均匀地分布到各个节点上，避免数据倾斜的问题。

L

当需要存储或查询一个键值对时，Redis Cluster 会先计算这个键的哈希权编号，然后根据哈希模编号找到对应的
节点进行操作。
推荐阅读: Redis Cluster

1. java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: Redis 切片集群? 数据
和实例之间的如何进行映射?

2. Java 面试指南 (付费) 收录的快手面经同学 1 部门主站技术部面试原题: Redis 的 cluster 集群如何实
现?

memo: 2025 年 5 月 14 日，今天有球友发微信说拿到了百度和美团的暑期实习 offer，果然五月也是一个开花结
果的季节。

No. 1031261




## 第 104 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

我友布了一篇笔记: 美团 or 百度
暑期实习版

期望询问下大家的意见! !

具体情况:          5
目前已经接了美团的offer，

26.集群中数据如何分区?

常见的数据分区有三种: 节点取余、一致性哈希和哈希槽。
节点取余分区简单明了，通过计算键的哈希值，然后对节点数量取余，结果就是目标节点的索引。

target_node = hash(key) %$ N  // N为节点数量

No. 1041261




## 第 105 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

缺点是增加一个新节点后，节点数量从 N 变为 N+1，几乎所有的取余结果都会改变，导致大部分缓存失效。
为了解决节点变化导致的大规模数据迁移问题，一致性哈希分区出现了: 它将整个哈希值空间想象成一个环，节点

这种设计的巧妙之处在于，当节点数量变化时，只有部分数据需要重新分配。比如说我们从 5 个节点扩容到 8 个节
点，理论上只有约 3/8 的数据需要迁移，大大减轻了扩容时的系统压力。

No. 1051 261




## 第 106 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

但一致性哈希仍然有一个问题: 数据分布不均匀。比如说在上面的例子中，节点 1 和节点 2 的数据量差不多，但节
点 3 的数据量却远远小于它们。

Redis Cluster 的哈希模分区在一致性哈希和节点取余的基础上，做了一些改进。

     AN   Reody wrte

Read / write            Read                                             Read

它将整个哈希值空间划分为 16384 个槽位，每个节点负责一部分槽，数据通过 CRC16 算法计算后对 16384 取
模，确定它属于哪个槽。

slot = CRC16(key) s 16384

No. 106 1 261




## 第 107 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

假设系统中有 4 个节点，为其分配了 16 个槽(0-15);
。 槽 0-3 位于节点 node1;
。 槽4-7 位于节点 node2;
。 槽8-11 位于节点 node3;
。 槽12-15 位于节点 node4。

如果此时删除 node2 ，只需要将槽 4-7 重新分配即可，例如将槽 4-5 分配给 nodel ，槽 6 分配给 node3 ，槽7
分配给 node4 ，数据在节点上的分布仍然较为均衡。

如果此时增加 node5，也只需要将一部分槽分配给 node5 即可，比如说将槽3、槽7、槽11、槽 15 迁移给
node5，节点上的其他模位保留。

因为槽的个数刚好是 2 的 14 次方，和 HashMap 中数组的长度必须是 2 的井次方有着异曲同工之妙。它能保证扩
容后，大部分数据停留在扩容前的位置，只有少部分数据需要迁移到新的槽上。

1. java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你知道 Redis 的一致性 hash 吗

2. Java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: Redis 扩容之后，哈希
槽的位置是否发生变化?

3. Java 面试指南 (付费) 收录的字节跳动面经同学 8 java 后端实习一面面试原题: redis 分片集群，如何
分片的，有什么好处

memo: 2025 年5 月 15 日，今天有球友发微信说加了星球后，算一算，踩着点拿到了滴滴的实习 offer，我看了
一下时间线，也就一个月时间不到，真的太强了。

No. 1071261




## 第 108 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

二哥我给您友了份简太”请您帮有我
看看，星球编号是

4月23日 下午13:40

加此

上午9:25

 感谢二哥 申 ，加了星球之后最后
一算踩着点进了最后一家滴滴，但
我现在犹玉是否还要等华为呢?

 是不是进滴滴后面秋招更容易去大
厂呢?

上午10:10

No. 1081261




## 第 109 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

IE
27 .能说说 Redis 集群的原理吗?

Redis 集群的搭建始于节点的添加和握手。每个节点通过设置 cluster-enabled yes 来开启集群模式。然后通过
CLUSTER MEET 进行握手，将对方添加到各自的节点列表中 。

这个过程设计的非常精巧: 节点 A 发送 MEET 消息，节点 B 回复 PONG 并发送 PING，节点A回复 PONG，于是
双向的通信和链路就建立完成了。

No. 1091261




## 第 110 页


<- meet B-ip B-port --

如果A是带 slot 的老节点

1

上

1
                     1
 认识B  gossippngB  认识 A

面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

                                              - 新实例启动

1
1
1

根据 link 信息

一gossip meetB 一> 更新自己的ip

or
|             gossip pongB                |

更新 B 看到的 A的 slots

|

有趣的是，由于采用了 Gossip 协议，我们不需要让每对节点都执行握手。在一个多节点集群的部署中，仅需要让
第一个节点与其他节点握手，其余节点就能通过信息传播自动发现并连接彼此。

No. 1101 261





## 第 111 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

令一> Master slave replication

Each Redis node communicates
through the cluster bus with every
other node

Clients will hit:
-~ masters, for read/write operations
- slaves, for read operations

握手完成后，可以通过 czUusTER ApDsLOTS 命令为主节点分配哈希模。当 16384 个模全部分配完毕，集群正式进

入就绪状态。

No. 1111261

元十，




## 第 112 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

分配模

<-cluster addslots {o...5461}

目

k一cluster addslots {o...5461}        6380

故障检测和恢复是保障 Redis 集群高可用的关键。每秒钟，节点会向一定数量的随机节点发送 PING 消息，当发现
某个节点长时间未响应 PING 消息，就会将其标记为主观下线。

主观下线

当半数以上的主节点都认为某节点主观下线时，这个节点就会被标记为"客观下线"。

No. 1121 261




## 第 113 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

如果下线的是主节点，它的从节点之一将被选举为新的主节点，接管原主节点负责的哈希槽。

5个主节点

部署 Redis 集群至少需要几个物理节点?

部署一个生产环境可用的 Redis 集群，从技术角度来说，至少需要 3 个物理节点。
这个最小节点数的设定并非 Redis 技术上的硬性要求，而是基于高可用原则的实践考量。

No. 1131 261




## 第 114 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

从实践角度看，最经典的 Redis 集群配置是 3 主 3 从，共 6 个 Redis 实例。考虑到需要 3 个主节点和 3 个从节
点，并且每对主从不能在同一物理机上，那么至少需要 3 个物理节点，每个物理节点上运行 1 个主节点和另一个主
节点的从节点。

。 物理节点1: 主节点A + 从节点B'
。 物理节点2: 主节点B + 从节点C'
。 物理节点3: 主节点C + 从节点A'

这种交错部署方式可以确保任何一个物理节点故障时，最多只影响一个主节点和一个不同主节点的从节点。

memo: 2025年5 月 16 日，今天在修改简历的时候，碰到一个河南理工本科，郑州大学硕士的球友，也是希望
这个社群能够帮助到更多的同学，无论来自哪里，都能在这里找回那个渴望进步，渴望拿到优质 offer 的自己。

郑州大学 (211 双一流) 硕士

计算机技术
” 荣誉奖项 : * 调目标检测软著、研究生学业奖学金二等奖 (Eu 几 、研究生学业奖学:

河南理工大学 本科
计算机科学与技术
28.说说Redis集群的动态伸缩?

Redis 集群动态伸缩的核心机制是通过重新分配哈希槽实现的。

No. 114 1261




## 第 115 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

GOO 本

加入

加入

当需要扩容时，首先通过 cLUSTER MEET 命令将新节点加入集群;然后使用 reshard 命令将部分哈希槽重新分配
给新节点。




## 第 116 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

一-这部分面试中可以不背start----
准备新的节点:

# redis .conf

Port 6382

cluster-enabled yes
cluster-config-file nodes-6382.conf
cluster-node-timeout 5000
appendonly yes

然后启动新的节点:

redis-serVer /path/to/redis-6382.conf

接下来，使用 cLUsTER MEET 命令将新节点加入集群:

redis-cli -P 6379 cluster meet 127.0.0.1 6382

检查新节点是否加入:

redis-cli -pP 6379 cluster nodes

然后，重新分配哈希模:

redis-cli --cluster reshard 127.0.0.1:6379

No. 116 1 261

SS

一

NS
mowesslots

novel

二





## 第 117 页


面渣逆袭 Redis篇第二版-让天下所有的面渣者能逆玖
在提示中输入要迁移的哈希槽范围。

# 输入要迁移的槽数量，比如 4096 (平均分配的话，16384/4=4096) 。

How many slots do you want to move (from 16384 total slots)? 4096
# 输入 6382 节点的 ID (可通过 cluster nodes 命令查到) 。

What is the receiving node ID? <6382的节点ID>

# 输入 al1 (表示从所有节点平均迁移) 。

Source node IDs? al1
# 输入 yes (表示确认迁移) 。

Do you want to proceed with the proposed reshard plan (yes/no)? yes
检查检查槽分配情况:
redis-cli -p 6379 cluster slots
验证集群的状态:
redis-cli -p 6382 cluster info
也可以直接一步到位:

redis-cli --cluster reshard 127.0.0.1:6379 --cluster-from all --cluster-to <6382的节点ID>
--cCluster-slots 4096 --Ccluster-yes

-一这部分面试中可以不背end-一-

缩容则是反向操作: 先将要下线节点负责的所有槽迁移到其他节点，再通过 CLUSTER FORGET 命令将节点从集群
中移除。

整个伸缩过程支持在线操作，无需停机，得益于 Redis 集群的 MOVED 和 ASK 重定向机制。当客户端访问的键不
在当前节点时，会收到重定向响应，指引它连接到正确的节点。

MOVED 和 ASK 重定向的区别?

MOVED 重定向反映的是哈希槽的永久性变更。当客户端请求一个键，但键所在的槽不在当前节点时，节点会返回
MOVED 响应，告诉客户端这个槽现在归属于哪个节点。通常发生在集群完成重新分片后，槽的分配关系已经稳

定

No. 1171261




## 第 118 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Redis集群
任意节点

2. 计算slot模
确定该Key对应的目标节点

Redis
客户端

3. 当前节点是否
为目标节点

4.B.1 返回MOVED重定向              N

4.A.1 执行命令
PT                                      执行命令

比如说某个槽从节点 A 移动到节点 B 后，如果客户端仍向节点 A 请求该槽中的键，会收到 MOVED 响应，提示应
该连接节点 B。

ASK 重定向出现在槽迁移过程中，表示请求的键可能已经从源节点迁移到了目标节点，但迁移尚未完成。

No. 1181261




## 第 119 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

A.1 查询键 phone
A.2 返回结果                               Source        | 该siot中待迁移Key |
-=                -       6                                               1                              |
节点         |    phone         pc      |
本 查拘键 cat             人
Redis                                                                         je
aa                      B.2 返回ASK重定向
客户端 上
B.3 发送Asking命令                                               人 该slot中已迁移K一       1
B.4 查询键 cat                              destination | |   该siot中已过移Key    |
节点         1 | cat          dog | |
|      |
B5返回结果
-

memo: 2025年 5 月 17 日，今天有球友发微信说拿到了一个国企子公司的 java 后端开发和一个小米安卓的
offer，问我该怎么选择?

二哥 不好意思这么晚打扰您，我想向您寻求点建
议。我现在在一个国企的子公司做 Java 后端开
发，最近有人小米安卓开发面的比较顺利，不是做
app的，类似中间价，也是 Java语言。现在不知
道怎么选择了，我秋招是想进国企的，不想卷大
厂了，然后尽量是走开发的，二哥你觉得怎么选
性价比更高啊

06:39

3

缓存设计

No. 1191261




## 第 120 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

29.二什么是缓存击穿?
全定时人关上上提组过有时 大量请求就会穿透缓存直接访问数据库，导臻数据库朋间承受的压力巨

昌 @

1 人                                                 1热点数据请求

Web 5

2 2
热点数据失效 y/                           5.返回数据

3.从数据库读取，
高并发

了肖 设置到
MySQL                                 缓存中

目                             MySQL

目

数据库压力激
增，芭比Q 了
fengkuinet

解决缓存击穿有两种常用的策略:
第一种是加互斥锁。当缓存失效时，第一个访问的线程先获取锁并负责重建缓存，其他线程等待或重试。

No. 1201 261




## 第 121 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

缓存击穿

这种策略虽然会导致部分请求延迟，但实现起来相对简单。在技术派实战项目中，我们就使用了 Redisson 的分布
式锁来确保只有一个服务实例能更新缓存。

String cacheKey = "product::" + productId)
RLock lock = redissonClient.getLock("lock::” + productId);
if (lock.tryLock(10，TimeUnit.SECONDS)) {
try
String result = cache.get(cacheKkey) 1;
if (result == null) {
result = database.queryProductById(productId) ;
cache.set(cachekey，result，60 * 1000); // 设置缓存

}
} finally {
lock.unlock();

】}

第二种是永不过期策略。缓存项本身不设置过期时间，也就是永不过期，但在缓存值中维护一个罗辑过期时间。当
缓存远辑上过期时，返回旧值的同时，异步启动一个线程去更新缓存。

public String getData(String key) {

No. 1211 261




## 第 122 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

CacheItem item = cache.get(key) 7

if (item == null) {

// 缓存不存在，同步加载
String data = db.query(key);

cache .set(key，new CacheItem(data，System.currentTimeMillis() + expireTime) )7
return datay
} else if (item.isLogicalExpired()) {
// 逻辑过期，异步刷新
asyncRefresh(key)

// 返回旧数据

return item.getData() 7

】}

return item.getDatal() 7
】}

// 异步刷新缓存

private void asyncRefresh(final String key) {

threadPool.execute(() -> {
// 重新查询数据库
String newData = db.query(key);
// 更新缓存

cache .set(key，new CacheItem(newData，System.currentTimeMillis() + expireTime) ) 7
)) 7

memo: 2025年5月18 日修改至此，今天给球友改简历时，碰到一个西北工业大学的球友，这又是一所 985 院
校，希望这个社群能把所有的 985 院校集齐，也希望去帮助到更多院校的同学，希望大家都能拿到一个满意的
offer。

西北工业大学 985 211 ，双一流

控制科学与工程 学硕 自动化学院
西北工业大学 985 211 ， 双一流
自动化 本科 自动化学院

什么是缓存穿透?

缓存穿透是指查询的数据在缓存中没有命中，因为数据压根不存在，所以请求会直接落到数据库上。如果这种查询
非常频繁，就会给数据库造成很大的压力。

No. 122 1 261




## 第 123 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

正常情况                   缓存穿透

@@

1 .数据读请求

Ce

和

MySQL                                  六          由
查询的数据
目                                               也不存在

缓存击穿是因为单个热点数据缓存失效导致的，而缓存穿透是因为查询的数据不存在，原因可能是自身的业务代码
有问题，或者是恶意攻击造成的，比如爬虫。

常用的解决方案有两种: 第一种是布隆过滤器，它是一种空间效率很高的数据结构，可以用来判断一个元素是否在
集合中。

我们可以将所有可能存在的数据哈希到布隆过滤器中，查询时先检查布隆过滤器，如果布隆过滤器认为该数据不存
在，就直接返回空，否则再去查询缓存，这样就可以避免无效的缓存查询。

3.大量请求打到数据库

No. 1231261




## 第 124 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

否，不存任把流量
前拦截香redis之前

代码示例:

public String getData(String key) {
// 缓存中不存在该key
String cacheResult = cache.get(key);
if (cacheResult != null) {
return cacheResult)

// 布隆过滤器判断key是否可能存在
if (!bloomFilter-mightContain(key)) {

return nul1; // 一定不存在，直接返回

// 可能存在，查询数据库
String dbResult = db.query(key);

// 将结果放入缓存，包括空值

cache .set(key，dbResult != nul1 ? dbResult : ""，expireTime) 1

No. 1241 261




## 第 125 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

return dbResult;

)
布隆过滤器存在误判，即可能会认为某个数据存在，但实际上并不存在。但绝不会漏判，即如果布隆过滤器认为某
个数据不存在，那它一定不存在。因此它可以有效拦截不存在的数据查询，减轻数据库压力。

第二种是缓存空值。对于不存在的数据，我们将空值写入缓存，并设置一个合理的过期时间。这样下次相同的查询
就能直接从缓存返回，而不再访问数据库。

代码示例:

public String getData(String key) {
String cacheResult = cache.get(key);

// 缓存命中，包括空值
if (cacheResult != null) {
// 特殊值表示空结果
if (cacheResult.equals("")) {
return nul17

】}

return cacheResult)

No. 1251 261




## 第 126 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 缓存未命中，查询数据库
String dbResult = db.query(key);

// 写入缓存，空值也缓存，但设置较短的过期时间
int expireTime = dbResult == null ? 了EMPTY_EXPIRE_TIME : NORMRL_EXPIRE_TIME 7
cache .set(key，dbResult != nul1 ? dbResult : ""，expireTime) 1

return dbResult;

缓存空值的方法实现起来比较简单，但需要给空值设置一个合理的过期时间，以免数据库中新增了这些数据后，缓
存仍然返回空值。

在实际的项目当中，还需要在接口层面做一些处理，比如说对参数进行校验，拦截明显不合理的请求; 或者对疑似
攻击的 IP 进行限流和封禁。

memo: 2025 年 5 月 19 日，今天有球友发微信说拿到了滴滴的测开实习 offer，目前还想继续找，问我该继续学
点什么，我的回复说，暑期能拿到 offer，秋招继续就行了，加上滴滴的实习经历就很硬核了。大家在准备暑期和
秋招的时候，也不要太焦虑，保持一个好的学习习惯，秋招没问题的。

No. 126 1 261




## 第 127 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

还有二哥我想请问一下，因为我现
在已经有了滴滴测开的 offer，然
后” 己的测开在泡池子，团期实习
以后，如果继续找测开的工作，这
个岗位的简历上都需要什么呢 (现
在是业务 + 轮子) ，我现在还需要
学习什么 (Java 四大件学的差不
多，之前有一段小广后端实习，写
了mydb)

上午6:30

什么是缓存雪册?

缓存雪崩是指在某一时间段，大量缓存同时失效或者缓存服务突然容机了，导致大量请求直接涌向数据库，导致数
据库压力剧增，甚至引发系统崩溃的现象。

No. 1271 261




## 第 128 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

key1||key2||……|| keyN
缓存大量过:

缓存down掉

缓存雪衣

缓存击穿是单个热点数据失效导致的，缓存穿透是因为请求不存在的数据，而缓存雪崩是因为大范围的缓存失效。
缓存雪崩主要有三种成因和应对策略。
第一种，大量缓存同时过期，解决方法是添加随机过期时间。

Public void setCache(String key，String value) {
// 基础过期时间，例如30分钟

int baseExpireSeconds = 1800)

// 增加随机过期时间，范围0-300秒

int randomSeconds = new Random() -nextInt(300) 1;

// 最终过期时间为基础时间加随机时间
cache.set(key，value，baseExpireSeconds + randomSeconds) 1;

)}

第二种，缓存服务崩溃，解决方法是使用高可用的缓存集群。
比如说使用 Redis Cluster 构建多节点集群，确保数据在多个节点上有备份，并且支持自动故障转移。

No. 128 1 261




## 第 129 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Redis Cluster

read/write                            replication                           read

对于一些高频关键数据，可以配置本地缓存作为二级缓存，缓解 Redis 的压力。在技术派实战项目中，我们就采用
了多级缓存的策略，其中就包括使用本地缓存 Caffeine 来作为二级缓存，当 Redis 出现问题时自动切换到本地组

口                                    加技术派Caffeine整合本

加技术派Caffeine整合本地缓
内 首页                         存

二 目录                          =
Caffeine作为当下本地缓存的王者被大量的应用在实际的项目中，可以有效

加技术派Redis实现计数统计           的提高服务的吞吐率、qps，降低rt。
国技术派整合Redis(多Redis配置/R，

加技术派Redis的缓存示例           在我们的【技术派】实战项目中，也同样使用了Caffeine作为本地缓存，用
于缓存侧边栏这种变动相对不频繁的信息

主要借助 Caffeine + @Cacheabte 来使用 如下

加技术派Cacheable注解实现缓存

加技术派Guava整合本地缓存

扩展癌读

加技术派Caffeine整合本地缓存
加技术派Caffeine整合本地缓存采
加技术派事务使用实例

加技术派使用事务的7条注意事项
加技术派WEB三大组件之Fiter

加技术派WEB三大组件之Servlet

加技术派WEB三。

组件之Listener

加技术派@Schedule注解实现定时

gj                                                 接下来给各位小伙伴看一下，我们一般怎么在实际的项目中使用缓存                                                              血

派整合邮件服务实现邮件发送
加技术派实时在线人数统计(单机版)                                                                                                                5
配置                                                                                                             丘

加技术派Spring事件监听机制及原理
加技术派如何实现图片上传至服务器          依赖

No. 1291 261




## 第 130 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

这个过程称为"缓存降级"，保证 Redis 发生故障时，系统能够继续提供服务。

LoadingCache<String，UserPermissions> permissionsCache = Caffeine.newBuilder()

maximumsize(1000)
.expireRAfterWrite(10，TimeUnit .MINUTES)
-build(this::loadPermissionsFromRedis))

Public UserPermissions loadPermissionsFromRedis(String userId) {

try {
return redisClient .getPermissions(userId) 1;

} catch (Exception ex) {
// Redis 异常处理，尝试从本地缓存获取

return permissionsCache.getIfPresent(userId);

第三种，缓存服务正常但并发请求量超过了缓存服务的承载能力，这种情况下可以采用限流和降级措施。

public String getData(String key) {
try {
// 尝试从缓存获取数据
return cache.get(key) 7
} catch (Exception e) {
// 缓存服务异常，触发熔断
if (circuitBreaker.shouldTrip()) {
// 直接从数据库获取，并进入降级模式
circuitBreaker.trip())
return getFromDbDirect1ly(key) 7

】}

throw ei

Private String getFromDbDirectly(String key) {
// 实施限流保护
if (!rateLimit.tryRcquire()) {
// 超过限流阔值，返回兜底数据或默认值

return getDefaultValue(key);

// 限流通过，从数据库查询
return db.query(key) 7

1. Java 面试指南 (付费) 收录的腾讯面经同学 22 暑期实习一面面试原题: 缓存雪骨，如何解决

2. Java 面试指南(付费) 收录的快手面经同学 7 java 后端技术一面面试原题: 说一下 缓存穿透、缓存击
穿、缓存雪崩

3. Java 面试指南(付费) 收录的字节跳动同学 7jJava 后端实习一面的原题: Redis 宕机会不会对权限系统
有影响?

No. 1301261




## 第 131 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

4. Java 面试指南 (付费)_收录的字节跳动同学 7 java 后端实习一面的原题: 说一下 Redis 雪骨、穿透、
击穿等场景的解决方案

5. java 面试指南 (付费) 收录的小米同学 F 面试原题: 缓存常见问题和解决方案 (引申到多级缓存) ，多
级缓存 (redis，nginx，本地缓存) 的实现思路

6. java 面试指南(付费) 收录的TP联洲同学 5 java 后端一面的原题: 如何解决缓存穿透
7. Java 面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题: 如何理解缓存雪崩、缓存击穿和缓存

穿透?

memo: 2025 年5 月 20 日，今天有球友发微信说项目用的技术派，八股背的面渣，春招拿到了四个 offer，其中
包括泰隆银行和交通银行，问我该怎么选择，说实话我看完后觉得挺难选的，例不过还是值得获喜一手。大家在
准备春招的时候也不要着急，付出总会有回报的。

邀请你加入群聊
"沉默王二"邀请你加入群聊二“”[T 大医
哥VIP8群"，进入可查看详情。 地 皮

虹 | 本

国站总

昨天 15:59

，打扰您，加入您的知识星
际 简历项目也是用的技术派
试看的面渣。现在春招 offer闷村
圈了，能请二哥您给出一些宝
建议吗。个人是单 2 硕计算机，
家是重让至4的，现在手上有这 3
个和一个递补的。现在不知道该如

4=T++h +又

No. 1311 261




## 第 132 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二乓盾。
国F 目 “SS ”=-昌          里供电有
站               中山
四            别 当地人
mm         知 应请
jn3r 和 me 四曲冲         四 天运维 1
很和 四 昌 mg汪汪 目          晶 上招考启
已时 柯订 PE,           在俊签
15:36

和钱的诉求强人
30.二能说说布隆过滤器吗?

布隆过滤器是一种空间效率极高的概率性数据结构，用于快速判断一个元素是否在一个集合中。它的特点是能够以
极小的内存消耗，判断一个元素"一定不在集合中"或"可能在集合中"，常用来解决 Redis 缓存穿透的问题。

hash10)
hash1

0     0     1     0     0     1     0     0     0     1     1     0     1     0     1     0     0

-这部分面试中可以不背start--
布隆过滤器的核心由一个很长的二进制向量和一系列哈希函数组成。
。 初始化的时候，创建一个长度为 m 的位数组，初始值全为 0，同时选择 k 个不同的哈希国数

No. 1321261




## 第 133 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

。 当添加一个元素时，用 k 个哈希函数计算出 k 个哈希值，然后对 m 取模，得到 k 个位置，将这些位置的二进
制位都设为 1

。 当需要判断一个元素是否在集合中时，同样用 k 个哈希函数计算出 k 个位置，如果这些位置的二进制位有任
何一个为 0，该元素一定不在集合中; 如果全部为 1，则该元素可能在集合中

Public class BloomFilter<T> {
private BitSet bitSet1
private int bitSetSizey
Private int numberOfHashFunctionsy

public BloomFilter(double falsePositiveProbability，int expectedNumberOfElements) {
// 根据预期元素数量和期望的误判率，计算最优的位数组大小和哈希函数个数
this.bitSetSize = calculateOptimalBitSetSize(expectedNumberOfElements，
falsePositiveProbability);
this.numberOfHashFunctions =
calculateOptimalNumberOfHashFunctions(expectedNumberOfElements，bitSetSize))
this.bitSet = new BitSet(bitSetSize))

public void add(T element) {
int[] hashes = createHashes(element))
for (int hash : hashes) {
bitSet .set(Math.abs(hash % bitSetSize)，true) 7

public boolean mightContain(T element) {
int[] hashes = createHashes(element))
for (int hash : hashes) {
if (!bitSet.get(Math.abs(hash % bitSetSize))) {

return false; // 如果任何一位为0，元素一定不存在

}
return true; // 所有位都为1，元素可能存在

// 其他辅助方法，如计算哈希值，计算最优参数等

一-这部分面试中可以不背end-…--
布隆过滤器存在误判吗?
是的，布隆过滤器存在误判。它可能会错误地认为某个元素在集合中，而元素实际上并不在集合中。

No. 1331 261




## 第 134 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

隆

hash3(x)9%8=7
hash1(x) %8=0

使用3个哈希函                          hash2(x)%8=4
数计算哈希值
1      1
0             1

bit 数组                    0  1
4

2  3

bit数组
位置编号

但如果布隆过滤器认为某个元素不存在于集合中，那么它一定不存在。

误判产生的原因是因为哈希冲突。在布隆过滤器中，多个不同的元素可能映射到相同的位置。随着向布隆过滤器中
添加的元素越来越多，位数组中的 1 也越来越多，发生哈希冲突的概率随之增加，误判率也就随之上升。

1                                                                       一“一 k=1,n=10M
一“一 k=3, n=10M
0.01                                                                       一“一 k=5, n=10M

一“一 k=8, n=10M

False positive probability (p)
引
世

100k            1M             10M           100M            1B

Size of bit array (mm)

误判率取决于以下 3 个因素:

1. 位数组的大小 (m) : m 决定了可以存储的标志位数量。如果位数组过小，那么哈希碰撞的几率就会增加，
从而导致更高的误判率。

No. 1341261




## 第 135 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

2，哈希函数的数量 (k) : k 决定了每个元素在位数组中标记的位数。哈希函数越多，碰撞的概率也会相应变
化。如果哈希函数太少，过滤器很快会变得不精确; 如果太多，误判率也会升高，效率下降。

3. 存入的元素数量 (n) : n 越多，哈希碰撞的几率越大，从而导致更高的误判率。
mA大
/内= (1-e全)                                     四

要降低误判率，可以增加位数组的大小或者减少插入的元素数量。
要彻底解决布隆过滤器的误判问题，可以在布隆过滤器返回"可能存在"时，再通过数据库进行二次确认。

布隆过滤器支持删除吗?

布隆过滤器并不支持删除操作，这是它的一个重要限制。

当我们添加一个元素时，会将位数组中的 k 个位置设置为 1。由于多个不同元素可能共享相同的位，如果我们尝试
删除一个元素，将其对应的 k 个位重置为 0，可能会错误地影响到其他元素的判断结果 。

例如，元素A 和元素 B 都将位置 5 设为 1，如果删除元素 A 时将位置 5 重置为0，那么对元素 B 的查询就会产生
错误的"不存在"结果，这违背了布隆过滤器的基本特性。

如果想要实现删除操作，可以使用计数布隆过滤器，它在每个位置上存储一个计数器而不是单一的位。这样可以通
过减少计数器的值来实现删除操作，但会增加内存开销。

public class CountingBloomFilter<T> {
private int[] counters)
Private int sizei
Private int hashFunctions;

public CountingBloomFilter(int size，int hashFunctions) {
this.size = sizey
this.hashFunctions = hashFunctions1;
this.counters = new int[size])

】}

public void add(T element) {
int[] positions = getHashPositions(element)
for (int position : positions) {
counters[position]++7
}
}

public void remove(T element) {
int[] positions = getHashPositions(element) 7
for (int position : positions) {
if (counters[position] > 0) {
counters[position]--;

)}

】}

public boolean mightContain(T element) {

int[] positions = getHashPositions(element) 7

No. 1351 261




## 第 136 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

for (int position : positions) {
if (counters[position] == 0) {
return falsei

)
】}

return truey

】}

Private int[] getHashPositions(T element) {
// 计算哈希位置的代码
}
)}

为什么不能用哈希表而是用布隆过滤器?

布隆过滤器最突出的优势是内存效率。

假如我们要判断 10 亿个用户 ID 是否曾经访问过特定页面，使用哈希表至少需要 10G 内存 (每个ID 至少需要8字
节) ，而使用布隆过滤器只需要 1.2G 内存。

m ~ -nxln(p)/ln(2)z ~ -10**ln(0.01)/ln(2)z = 9.6 billion bits ~ 1.2GB

1. Java 面试指南 (付费) 收录的字节跳动同学 7 Java 后端实习一面的原题: 有了解过布隆过滤器吗?

2. java 面试指南(付费) 收录的TP联洲同学 5 java 后端一面的原题: 布隆过滤器原理，这种方式下5%的
错误率可接受?

3. Java 面试指南 (付费) 收录的美团同学 9 一面面试原题: 布隆过滤器? 布隆过滤器优点? 为什么不能用
哈希表要用布隆过滤器?

4. Java面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题: 追问: 说明一下布隆过滤器
memo: 2025 年 5 月 20 日，今天有球友发贴说拿到了滴滴的暑期 offer，特意来感谢了一下面渣逆袭。

No. 1361261




## 第 137 页


面渣逆袭 Redis篇第二版-让天下所有的面潮都能地装
导  过引进…汪                                               < 收进专栏

晒个offer吧

滴滴暑期今天中午oc了，想分享一下自己的心路历程。

bg双九，但是自认为水平比较低，大学期间全程摆烂，课程挂了七门，都是最后一学期补考
过的。研究生也量几平塘线老讨。”帮窑生一年灶耻量由干虹师这冰放养，没任何产出，也是
摆了一年半，暗町上F-W习二，后三车 …画必三一同上拒，呈项二号沈没一点编程基础贸岛
真正开始准各过二二.一草本1 芝肝三避逢与5 .本 。 霹知后觉发现要准备暑期
实习了。这中国和HE症 月.站于让 攻庆下二 ”区=碾尘了下来，在4月10号左
右开始投递各 .

四月份一共西“一个.时 国志二汪汪与ET 。， 园昌六:到了五月份，此时已经感
觉找不到实研“

五月份五一人.1 声1于下 国土南 .P辐下富局访-再，假期重新整理了八股，
自己整理了交直 尽旦1号和上这 “一地种呆-坊工哇志肥刻的。再就是算法题，
在面试之前一天狠狠刷了60道数组链表二叉树的高频题。面试的时候突然就感觉如鱼得水
了，基本上全答上来了，手撕也很顺利。两天的时间速通了滴滴和招联金融。

最后，真的感谢二哥的八股，三月十号之后全程跟着二哥八股来的，真的全面，前期跟的
ma 中 和 芭多了根本学不进去。中间会参考一下十不。滴滴二面的手撕是手撕hashmap，
刚好二哥面渣上面有。

31.闪如何保证缓存和数据库的数据一致性?

在技术派实战项目中，对于文章标签这种允许短暂不一致的数据，我会采用 Cache Aside + TTL 过期机制来保证缓
存和数据库的一致性。

No. 1371261




## 第 138 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

办，个人知识库           加技术派MysqWRedis组存一致性(中强列推荐)                窑&殉路   分享  E3 目 国
宣 技术派 @            四       5. 先写 MySQL，再删除 Redis
大网 玛 ;=
十 理论知识
全 首页                      | 请求A    |  请求B  ]    |  Redis  ]    | MySQL ]              - 不好的方案
1 先写 MYSQL，再写 Redis
下 目录             三                                          RE           2.先写 Redis，再号 MySQL
技术泊消息队5IRabbitM                             |                          3 先而除 Redis，再写 MySQL
加技术派消息队列RabbitM               [| |mempio                            " 好的方案

4 先删除 Redis，再写 MYSQL,

加技术派消息队列Kafka (                                        前二次剖光| 查询缓存未命中                          |        5 先写 MysQL，再肌除 Redis
加技术派Mysq/Redis缓存…                                                           玖后SQL                6.先写 MySQL，通过 Binlog，
加技术演Mysq/Redis缓存                                                                     人                                               几种方案比较
加技术派Cancal实现WSQ                                                                                           了下和

                 对于上面这种情况，对于第一次查询，请求 B 查询的数据是 10，但是 MySQL          才扣机
园技术派ES实现查询 (过…                                                               数据获取

的数据是 11，只存在这一次不一臻的情况，对于不是强一臻性要求的业务，可以

国术尖Redis分布式镇       容忍。 (那什么情况下不能容忍呢，比如秒杀业务 、库存服务等。)                者有全
加技术汽od-job实现定时
加技术派服务监控之Actua          当请求 B 进行第二次查询时，因为没有命中 Redis，会重新查一次 DB，然后再
加技术派计口号冲突解决方案          回写到 Reids.

加技术派Filter实现请求日

加技术派记录SQL执行日志     | 请求A ]  | 请求B ] Redis ]  [wsar |

加技术派深入理解DB连接

加技术派异常日志报警通知                          -Pi和一| 查询组存未命中

加技术派并行访问性能优化

查询MySQL 10

具体做法是读取时先查 Redis，未命中再查 MySQL，同时为缓存设置一个合理的过期时间; 更新时先更新
MySQL，再删除 Redis 。

// 读取膛辑
Public UserInfo getUser(String userId) {

// 先查缓存
UserInfo user = cache.get("user:" + userId) 1
if (user != nul1l) {

return usery

// 缓存未命中，查数据库
user = database.selectUser(userId) 1;
if (user != nul1l) {

// 放入缓存，设置合理的过期时间

cache.set("user:”+ userId，user，3600)

return user)

// 更新逻辑
public void updateUser(UserInfo user) {

// 先更新数据库

database.updateUser(user) 7

No. 1381 261




## 第 139 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 删除缓存

cache.delete("user:" + user.getId());

)}

这种方式简单有效，适用于读多写少的场景。TTL 过期时间也能够保证即使更新操作失败，未能及时删除缓存，过
期时间也能确保数据最终一致。

那再来说说为什么要删除缓存而不是更新缓存?
最初设计缓存策略时，我也考虑过直接更新缓存，但通过实践发现，删除缓存是更优的选择。

EN ESN ES

                                                  >| MysQL 更新为 10

>| MysQL 更新为 1

一| Redis 更新为 11

Redis 更新为 10

最主要的原因是在并发环境下，假设我们有两个并发的更新操作，如果采用更新缓存的策略，就可能出现这样的时
序问题:

。 操作 A 和操作 B 同时发生，A 先更新 MySQL 将值改为 10，B 后更新 MySQL 将值改为 11。但在缓存更新
时，可能 B 先执行将缓存设为 11，然后A 才执行将缓存设为10。这样就会造成 MySQL是 11但 Redis是10
的不一致状态。

而采用删除策略，无论A 和 B 谁先删除缓存，后续的读取操作都会从 MySQL 获取最新值。
另外，相对而言，删除缓存的速度比更新缓存的速度快得多。

No. 1391261




## 第 140 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

人贸 。 刑除缓存                         更新缓存

因为删除操作只是简单的 DEL 命令，而更新可能需要重新序列化整个对象再写入缓存。

那再说说为什么要先更新数据库，再删除缓存?

这个操作顺序的选择也是我在实际项目中踩过坑才深刻理解的。假设我们采用先删缓存再更新数据库的策略，在高
并发场景下就可能出现这样的问题:

。 线程 A 要更新用户信息，先删除了缓存

。 线程 B 恰好此时要读取该用户信息，发现缓存为室，于是查询数据库，此时还是旧值

。 线程 B 将查到的旧值重新放入缓存

。 线程A 完成数据库更新
结果就是数据库是新的值，但缓存中还是旧值。

删除缓存 10

查询缓存未命中

查询 MySQL 10

回写缓存 10

而采用先更新数据库再删缓存的策略，即使出现类似的并发情况，最坏的情况也只是短暂地从缓存中读取到了旧
值，但缓存删除后的请求会直接从数据库中获取最新值。

No. 1401261




## 第 141 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

另外，如果先删缓存再更新数据库，当数据库更新失败时，缓存已经被删除了。这会导致短期内所有读请求都会穿
透到数据库，对数据库造成额外的压力。

国 。 型除缓存时间
国 更新数据库时间
贸

先更数据库后删缓存                 先更数据库后删缓存
而先更新数据库再删缓存，如果数据库更新失败，缓存保持原状，系统仍然能继续正常提供服务。

public void updateUser(User user) {

try {
// 先更新数据库

database.updateUser(user) 1

// 再删除缓存

cache.delete("user:" + user.getId());
} catch (DatabaseException e) {

// 数据库更新失败，缓存保持原状，系统仍可正常提供服务

log.error("Database update failed"，e);

throw ey
} catch (CacheException e) {

// 缓存删除失败，数据库已更新，数据会在rTL后自动一至

1og.warn("Cache deletion failed，wil1 be eventually consistent"，e))

// 可以选择不抛异常，因为有TTL兜底

】}

memo: 2025 年5 月 22 日，今天给球友修改简历时，碰到一个西北工业大学本、电子科技大学硕的球友，一下
子 985 高校又集齐了两所。如果球友们在星球里有所收获，也请给学弟学妹们一个口碑，让大家都能因此受益，

拿到更好的 offer。

No. 1411 261




## 第 142 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

教育背景

2023.09-2026.06                                电子科技大学 (985 工程)                                         砚士
GPA: 3.76/4 ( 成绩排名: 1%一59% )

2019.09-2023.06                                西北工业大学 (985 工程)                                          学士
GPA: 3.52/4 (成绩排名: 5%一20% )

那假如对缓存数据库一致性要求很高，该怎么办呢?

当业务对缓存与数据库的一致性要求很高时，比如支付系统、库存管理等场景，我会采用多种策略来保证强一至
性。

消息队列保证缓存被删除

数据库订阅+消息队列保证缓存被删除

@ 缓存一致性的解决方
案@沉默王二                  延时双删防止脏数据
设置缓存过期时间忽底

第一种，引入消息队列来保证缓存最终被删除，比如说在数据库更新的事务中插入一条本地消息记录，事务提交后
异步发送给 MQ 进行缓存删除。

-|更新雪据库

了| -天际用和>       人

= 一5重试出除>
4村要滑除的hey

即使缓存删除失败，消息队列的重试机制也能保证最终一致性。

No. 142 1 261




## 第 143 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Transactional
public void updateUser(UserInfo user) {

// 在事务中更新数据库

database.updateUser(user) 7

// 在同一事务中记录需要删除的缓存信息

LocalMessage message = new LocalMessage("CRCHE_ DELETE"，"user:" + user.getId()) 7

database.insertLocalMessage(message);

// 显式发布事件，供监听器捕获

eventPublisher.publishEvent(new UserUpdateEvent(this， "user:” + user.getId())) 7

// 事务提交后发送Mo消息

erTransactionalEventListener(Phase = TransactionPhase.RFTER_COMMIT)

public void sendCacheDeleteMessage(UserUpdateEvent event) {
messageOueue.send("cache-delete-topic"，event.getCacheKey()) 1;

第二种，使用 Canal 监听 MySQL 的 binlog，在数据更新时，将数据变更记录到消息队列中，消费者消息监听到变
更后去删除缓存。

人                     7.需要删除的key

6.如果删除失败，记录需要删除的key

<一5.删除缓存        和

8.重试删除操作

缓存                 4提取要操作的数据及key

Cam      妥

监听binlog服务

这种方案的优势是完全解耦了业务代码和缓存维护逻辑。

ecanalListener
public class CacheUpdateListener {

eEventHandler
public void handleUserUpdate(UserUpdateEvent event) {

No. 1431261




## 第 144 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 从binlog事件中提取变更信息

String userId = event.getUserId();

// 发送缓存删除消息

CacheDeleteMessage message = new CacheDeleteMessage();
message.setCacheKey("user:" + userId) 1
messageOueue.send("cache-delete-topic"，message) 7

}

}

// 消费者监听消息队列

eKafkaListener(topics = "cache-delete-topic")

Public void handleCacheDeleteMessage(CacheDpeleteMessage message) {
// 删除缓存
cache.delete(message.getCacheKey());

}

当然了，如果说业务比较简单，不需要上消息队列，可以通过延迟双删策略降低缓存和数据库不一致的时间窗口，
在第一次删除缓存之后，过一段时间之后，再次党试删除缓存。

No. 1441261




## 第 145 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

更新数据库

这种方式主要针对缓存不存在，但写入了脏数据的情况。

public void updateUser(UserInfo user) {
// 第一次删除缓存，减少不一致时间窗口

cache.delete("user:" + user.getId());

// 更新数据库

database.updateUser(user) 7

// 立即删除缓存

cache.delete("user:" + user.getId());

// 延时删除，应对可能的并发读取

No. 1451261




## 第 146 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

CompletableFuture.runRasync(() -> {
try {
Thread.sleep(1000); // 延时时间根据主从同步延迟调整
cache.deletel("user:" + user.getId());
} catch (InterruptedException e) {
Thread.currentThread() .interrupt()7

)) 7

最后，无论采用哪种策略，最好为缓存设置一个合理的过期时间作为最后的保障。即使所有的主动删除机制都失败
了，TTL 也能确保数据最终达到一致 :

// 根据数据的重要程度设置不同的rTL

Public void setCache(String key，Object value，DataImportance importance) {

int ttl7
switch (importance) {
case HIGH:     // 关键数据，短TTL
tt1 = 300;  // 5分钟
break;
case MEDIUM:    // 一般数据
tt1 = 1800; // 30分钟
break;
case LOW:      // 不太重要的数据
tt1 = 3600; // 1小时
break;

】}

cache .setWithTTL(key，value，ttl1) 7

)}

这种方式虽然简单，但能确保即使出现极端情况，数据不一致的影响也是可控的。
1. Java 面试指南 (付费) 收录的华为面经同学 8 技术二面面试原题: 怎样保证数据的最终一致性?
2. Java 面试指南(付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: 数据一致性问题

3. java 面试指南 (付费) 收录的微众银行同学 1 java 后端一面的原题: MYSQL 和缓存一致性问题了解
吗?

4. Java 面试指南 (付费) 收录的美团面经同学 3 java 后端技术一面面试原题: 如何保证 redis 缓存与数据
库的一致性，为什么这么设计

5. java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: 怎么解决redis和mysq|的缓存一
致性问题

6. Java 面试指南 (付费) 收录的字节跳动同学 17 后端技术面试原题; 双写一致性怎么解决的
7. java 面试指南(付费) 收录的京东面经同学 9 面试原题: redis的数据和缓存不一致应该处理

memo: 2025年5月 23 日修改至此，今天在修改球友简历时，看到一条非常温暖的感谢信，球友说改完后的简
历，每一句都比之前的好很多，真的很欣慰，感觉自己的付出得到了回报。和

No. 146 1 261




## 第 147 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Re:应聘岗位_姓名_学历 (6) 口 户 @ 于 。 外安全浏览模式
发件人: 本定wamoumer站qq.com>
收件人: 有 沉默王二<www.qing_gee@163.com>

时 间: 2025年05月22日 10:37 (星期四)

【升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

感谢二哥的指正，每一句都感觉比我的好很多，改完之后简历质量瞬间涨了不少，太感谢了

32.如何保证本地缓存和分布式缓存的一致?

在技术派实战项目中，为了减轻 Redis 的负载压力，我又追加了一层本地缓存 Caffeine。

No. 1471261




## 第 148 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

为了保证 Caffeine 和 Redis 缓存的一致性，我采用的策略是当数据更新时，通过 Redis 的 pub/sub 机制向所有应
用实例发送缓存更新通知，收到通知后的实例立即更新或者删除本地缓存。

No. 1481261




## 第 149 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

合适的过期时间
人| 未地组存

2              2

Private final RedisTemplate redisTemplate

eservice
public class Cacheservice {

Private final CaffeineCache localCache'

public void updateData(String key，oObject value) {

// 更新数据库

database.update(key，value);

// 更新分布式缓存

redisTemplate.opsForValue() .set(key，value，30，TimeUnit .MINUTES ) 7

// 发送缓存更新通知

CacheUpdateMessage message = new CacheUpdateMessage(key，"UPDRTE"，value) 1
redisTemplate.convertRandSend("cache-update-channel"，message);

EventListener
public void handlecacheUpdate(CacheUpdateMessage message) {
if ("UPDRTE" .equals(message.getRction())) {
localCache.put(message.getKey()，message.getValue())7

No. 1491261




## 第 150 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

} else if ("DELETE" .equals(message.getRhction())) {
localcache.invalidate(message.getKey()) 17

考虑到消息可能丢失，我还会引入版本号机制作为补充。每次从 Redis 获取数据时添加一个最新的版本号。从本地
缓存获取数据前，先检查自己的版本号是否是最新的，如果发现版本落后，就主动从 Redis 中获取最新数据。

ecomponent

public class VersionBasedCacheManager {

Rutowired

Private StringRedisTemplate redisTemplatey

// 使用 caffeine 构建本地缓存: 最多 1000 项，写入后 10 分钟过期

Private final Cache<String，VersionedData> localCache = Caffeine.newBuilder()
-maximumSize(1000)
.expireRAfterWrite(10，TimeUnit .MINUTES)

.build())
As
* 获取缓存数据，优先使用本地缓存，必要时从 Redis 加载
/

Public Object get(String key) {
VersionedData cached = localCache.getIfPresent(key); // 从本地缓存取出

// 从 Redis 获取版本号

String versionStr = redisTemplate.opsForValue().get(key + ":version'"))

// 如果 Redis 中没找到版本号，说明可能数据已失效，强制刷新
if (versionStr == null) {
return loadRndcache(key)

long remoteVersion = Long.parseLong(versionStr);

// 如果本地没有缓存，或版本落后于 Redis，强制刷新
if (cached == null || cached.getVersion() < remoteVersion) {
return loadandCache(key) 7

// 命中本地缓存且版本最新，直接返回

return cached.getData() 7

xx
* 从 Redis 加载数据和版本，并写入本地缓存
/
Private Object loadRndcache(String key) {
Object data = redisTemplate.opsForValue().get(key);

No. 1501 261




## 第 151 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

String versionStr = redisTemplate.opsForValue().get(key + ":version'"))
if (data != null && versionStr != null) {

long version = Long.parseLong(versionStr);
localcache.put(key，new VersionedData(data，version) ))

return datay

如果在项目中多个地方都要使用到二级缓存的届辑，如何设计这一块?

我的思路是将二级缓存抽象成一个统一的组件。设计一个 CacheManager 作为核心入口，提供 get、put、evict 等
基本操作，执行先查本地缓存，再查分布式缓存，最后查数据库的完整流程。

public class CacheManager {
private final LocalCache localCachei
Private final RedisCache redisCachei
private final Database databasei

public CacheManager(LocalCache localCache，RedisCache redisCache，Database database)

this.localCache

localcachei
this.redisCache

redisCachei
this.database = database)

public object get(String key) {
// 先查本地缓存
Object value = localCache.get(key);
if (value != null) {

return valuey

// 再查分布式缓存

value = redisCache.get(key);
if (value != null) {

// 更新本地缓存

localcache.put(key，value)
return valuey

// 最后查数据库

value = database.get(key);

if (value != null) {
// 更新分布式缓存和本地缓存
redisCache.put(key，value);
localcache.put(key，value)

No. 1511 261




## 第 152 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

return valuey

)}

本地缓存和 Redis 的区别了解吗?
Redis 可以部署在多个节点上，支持数据分片、主从复制和集群。而本地缓存只能在单个服务器上使用。

对于读取频率极高、数据相对稳定、允许短暂不一致的数据，我优先选择本地缓存。比如系统配置信息、用户权限
数据、商品分类信息等。

而对于需要实时同步、数据变化频繁、多个服务需要共享的数据，我会选择 Redis。比如用户会话信息、购物车数
据、实时统计信息等。

1. Java 面试指南 (付费)_收录的字节跳动同学 7 java 后端实习一面的原题: 怎么保证二级缓存和 Redis
缓存的数据一致性?

2. java 面试指南 (付费) 收录的华为面经同学 11 面试原题: 使用的 guava cache 和 redis 是如何组合使
用的? 如果在项目中多个地方都要使用到二级缓存的还辑，如何设计这一块?

3. java 面试指南(付费) 收录的去哪儿同学 1 技术二面的原题: redis 和本地缓存的区别，哪个效率高
4. java面试指南 (付费) 收录的拼多多面经同学 8 一面面试原题: 缓存一致性如何保证

33.什么是热Key?

所谓的热 Key，就是指在很短时间内被频繁访问的键。比如电商大促期间爆款商品的详情信息，流量明星爆瓜时的
个人资料、热门话题等，都可能成为热Key。

由于 Redis 是单线程模型，大量请求集中到同一个键会导致该 Redis 节点的 CPU 使用率闫升，响应时间变长。
在 Redis 集群环境下，热Key 还会导致数据分布不均衡，某个节点承受的压力过大而其他节点相对空闲。

No. 1521 261




## 第 153 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

更严重的情况是，当热Key 过期或被误删时，会引发缓存击穿问题。
那怎么监控热Key 呢?

临时的方案可以使用 redis-cli --hotkeys 命令来监控 Redis 中的热 Key。

redis-cli -h <address> -p <port> -a<password> -hotkey

No. 1531 261




## 第 154 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

热点数据发现

请求统计

或者在访问缓存时，在本地维护一个计数器，当某个键的访问次数在一分钟内超过设定阔值，就将其标记为热
Key。

ecomponent
Public class HotKeyDetector {
Private final ConcurrentHashMap<String，RtomicLong> accessCounter = new

ConcurrentHashMap<>();
private final int HOT_KEY_THRESHOLD = 10007

public boolean isHotKey(String key) {
long count = accessCounter.computeIfRbsent(key，Kk -> new RtomicLong(0) )
.incrementRndGet () 17
return count > HOT _KEY_THRESHOLD)

34.那怎么处理热Key 呢?
最有效的解决方法是增加本地缓存，将热 Key 缓存到本地内存中，这样请求就不需要访问 Redis 了。

No. 1541261




## 第 155 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

热key处理

对于一些特别热的 Key，可以将其拆分成多个子 Key，然后随机分布到不同的 Redis 节点上。比如将
hot_product:12345 拆分成 hot_product:12345:1 、hot_product:12345:2 等多个副本，读取时随机选择其
中一个。

key3#
key3#2
key3#S3
key3#4

[/               N      并发查询key3

忌
<CD?C2?国CC本CC

Public String getHotData(String key) {
if (isHotKey(key)) {
// 随机选择一个副本
int replica = ThreadLocalRandom.current() .nextInt(HOT_KEY_REPLICRS) 1?
return redis.get(key + ":"”+ Leplica) 17

】}

return redis.get(key)7

No. 155 / 261




## 第 156 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

35.怎么处理大 Key 呢?

大Key 是指占用内存空间较大的缓存键，比如超过 10M 的键值对。常见的大Key 类型包括: 包含大量元素的
List、Set、Hash 结构，存储大文件的 String 类型，以及包含复杂庶套对象的JSON 数据等。

在内存有限的情况下，可能导致 Redis 内存不足。另外，大Key 还会导致主从复制同步延迟，甚至引发网络拥塞。
可以通过 redis-cli --bigkeys 命令来监控 Redis 中的大 Key。
ee@ee 加            yusrlocaymysqlbin         mewaqngg                          (CUpdaewap ) Q_ 乡

/usr/LocaU/mysqUbin

redts-clLit --bigkeys

# Scanning the entire keyspace to find biggest keys as welLlL as
## average Sizes per key type， You can Use -it 0.1 to stLeep 0.1 sec
# per 1600 SCAN commands (not usuatty needed ) .

[00.00%] Biggest hash “ found so far '"pai_articte_statistic_171"' with 4 fieLds

[00.00%] Biggest hash ”found so far '"pai_user_statistic_950"' with 6 fieLds

[05.46%] Biggest hash ”found so far '"pai_visit_info_20231219"' with 36 fietds

[07.11%] Biggest hash “found so far '"pai_visit_info_20231127"' with 42 fietLds

[6@7.37s%] Biggest string found so far '"pai_eyJhbGciOt]IUzI1NtIsInR5cCI6IkpXVC]J9.ey]Jpc3MtOtJwYWLfY29
kaw5nIiwiZXhwIjoxNzEyMzg5MzIOLC]JzIjoiMDAwMDAwMDAuMTcwOTc5NzMyNDU3MS4zNzAxMDEwMDYiLLCJ1IjooMTE2fQ.iXP
0TgQLXBBkXM6E5I9GVA50sAYiXH]_8BuaZnuzUdg"' with 4 bytes

[17.56%] Biggest List ”found so far '"pai_chat.history.xun_fei_ai.3"' with 8 items

[21.27%] Biggest hash ”found so far '"pai_visit_info"' with 128 fietds

[31.08%] Biggest zset “found so far '"pai_activity_rank_202403"' with 1 members

[33.79%] Biggest Litst ”found so far '"pai_chat.history.pai_ait.943"' with 26 items

[52.64%] Biggest set    found so far '"pai_auth_articte_white_List"' with 1 members

[56.89%] Biggest zset found so far '"pai_activity_rank_202308"' with 2 members

[91.42%] Biggest string found so far '"test"' with 12 bytes

Summary

SamptLed 3883 keys in the keyspacel!
Totalt kev Lenath in bvtes is 89194 (avq Len 22.97)

Vusr/Locat/mysqtL/bin

或者编写脚本进行全量扫描:

ecomponent

public class BigKeyScanner {

private final RedisTemplate redisTemplatei
private final int BIG_KEY_THRESHOLD = 1024 * 1024;

public List<BigKeyInfo> scanBigKeys() {
List<BigKeyInfo> bigKeys = new RrrayList<>() 7

Scan0ptions options = Scan0ptions.scan0ptions().count(1000) .build();
Cursor<byte[]> cursor = redisTemplate.executeWithStickyConnection(
connection    connection.scan(options)

while (cursor.hasNext()) {

No. 1561 261




## 第 157 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

String key = new String(cursor.next());
long memory = getKeyMemoryUsage(key)

if (memory > BIG_KEY_THRESHOLD) {
bigKeys.add(new BigKeyInfo(key，memory，getKeyTYpe(key) ) ) 7

return bigKeysy

Private long getKeyMemoryUsage(String key) {

// 使用MEMORY USAGE命令获取键的内存占用
return redisTemplate.execute((RedisCallback<Long>) connection ->
connection.memoryUsage (key.getBytes())

) 7

对于大 Key 问题，最根本的解决方案是拆分大 Key，将其拆分成多个小 Key 存储。比如将一个包含大量用户信息
的 Hash 拆分成多个小 Hash。

大key处理

No. 1571261




## 第 158 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

public void splitBigKey(String bigKey) {
Map<String，String> bigData = redisTemplate.opsForHash() .entries(bigKey);

// 将大 Key 拆分成多个小 Key

for (Map.Entry<String，String> entry : bigData.entrySet()) {
String smallKey = bigKey + ":" + entry.getKey())
redisTemplate.opsForValue() .set(smallKey，entry.getValue()) 17

// 删除原始大 Key
redisTemplate.delete(bigKkey))

另外，对于JSON 数据，可以进行 Gzip 压缩后再存储，虽然会增加一些 CPU 开销，但在内存敏感的场景在是值得
的。

Public void setCompressedData(String key，Object data) {

try {
String json = objectMapper.writeValueRsString(data) 1

byte[] compressed = compress(json.getBytes());

redisTemplate.opsForValue() .set(key，compressed) 1;
} catch (Exception e) {

log.error("Failed to compress data"，e)7

Private byte[] compress(byte[] data) throws IOException {
ByteRrrayOutputStream out = new ByteRrrayOutputStream() 7
try (GZIPOutputStream gzip = new GZIPOutputStream(out)) {

gzip.write(data) 7

}
return out .toByteRrray();
}
推荐阅读:

e 阿里: 发现并处理 Redis 的大 Key 和热 Key
。 董宗敌: Redis 热 Key 发现以及解决办法

1. Java 面试指南 (付费)_收录的华为 OD 的面试中出现过该题: 讲一讲 Redis 的热 Key 和大 Key
memo: 2025 年 5 月 24 日，今天球友发私信说，拿到了荣耀通软的实习 offer，葵喜他! 闵:

No. 158 1 261




## 第 159 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥，荣耀的通软 和 畦需-…本和电呈司时发，您
觉得选哪个对秋招帮助大呀

SS

本

36.缓存预热怎么做呢?

库。

aenepata              Requests

庆 DATAOI                  DArAo3_] cw
Hall                     DATAOI |] cn
Te]                     DATAO4 | cM
人pull                     DArAo2 | cw

Cold and
Warm Cache

in System Design

ER                   DATA03 |] cn

CM cache Miss            间2: DATA 02                EAIA9 | c
                3 DATA03

CH Cache Hit            天全 DATA 04             DATAO2 |] cM

5:DATA05

缓存预热的方法有多种，在技术派实战项目中，我会在项目启动时将热门文章提前加载到 Redis 中，在每天凌晨定
时将最新的站点地图更新到 Redis中，以确保用户在第一次访问时就能获取到缓存数据，从而减轻数据库的压力。

xx
* 采用定时器方案，每天5 : 15分刷新站点地图，确保数据的一致性
+/
Scheduled(cron = "0 15 5 *x x ?")
public void autoRefreshCcache() {
log.info( "开始刷新sitemap .xml的ur1地址，避免出现数据不一致问题!" ) ;
refreshSitemap()7
1log.info( "刷新完成! ") ;
】}

eoverride
Public void refreshSitemap() {
initSiteMap() 7

No. 1591 261




## 第 160 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Private synchronized void initSiteMap() {

long lastId = 0L;
RedisClient .del(SITE_MRAP_CRCHE_KEY)
while (true) {
List<SimpleRrticleDTO> list =
articleDao.getBaseMapper() .1istRrticlesOrderById(lastId，SCRAN_SIZE) 7

// 刷新站点地图信息，放到 Redis 当中
Map<String，Long> map = list.stream() .collect(Collectors.toMap(s ->
String.valueOf(s.getId())，s -> s.getCreateTime().getTime()，(a，b) -> a));
RedisClient.hMSet(SITE_MRP_CRCHE_KEY，map);
if (list.size() < SCAN SIZE) {
break;

}
lastId = list.get(list.size() - 1).getId();

1. Java 面试指南 (付费) 收录的字节跳动面经同学 1 技术二面面试原题: 什么是缓存预
37.无底洞问题听说过吗? 如何解决?

无底洞问题的核心在于，随着缓存节点数量的增加，虽然总的存储容量和理论吞吐量都在增长，但是单个请求的响
应时间反而变长了。

这个问题的根本原因是网络通信开销的增加。当节点数量从几十个增长到几千个时，客户端需要与更多的节点进行
通信。

其次就是数据分布的碎片化。随着节点增多，数据分散得更加细碎，原本可以在一个节点获取的相关数据，现在可
能分散在多个节点上。

针对这个问题，可以采取以下几种解决方案:
第一，可以将同一节点的多个请求合并成一个批量请求，减少网络往返次数。

如何解决?

Public Map<String，Object> batchGet(List<String> keys) {

// 按节点分组keys
Map<String，List<String>> nodeKeysMap = groupKeysBYNode(keys))
Map<String，Object> results = new ConcurrentHashMap<>() 17

// 并发访问各个节点
List<CompletableFuture<Void>> futures = nodeKkeysMap.entrySet() .stream()
-map(entry -> CompletableFuture.runRsync(() -> {
String node = entry-getKey() 17
List<String> nodeKeys = entry-getValue() 1

// 批量获取该节点的数据
Map<String，Object> nodeResults = getFromNode(node，nodeKkeys)
results.putall(nodeResults);

}))

No. 1601261




## 第 161 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

.collect(Collectors.toList())7

// 等待所有请求完成

CompletableFuture.al10f(futures.toRrray(new CompletableFuture[0])) .join();

return results7

第二，可以使用一致性哈希算法来优化数据分布，减少数据迁移和重分布的开销。

public class LocalityRhwareSharding {

public String getNodeForKey(String key，String category) {

// 相同类别的数据尽量分配到相同节点
String shardKey = category + ":" + (key.hashCcode() 8 SHARDS_PER_CRTEGORY) 1
return consistentHash.getNode(shardKey);

】}

// 用户相关数据尽量在同一个节点

public String getUserDataNode(String userId) {
return "user_cluster_ "+ (userId.hashCode() 8 USER_CLUSTERS ) ;

Redis 运维
38.Redis 报内存不足怎么处理?

Redis 报内存不足时，通常是因为 Redis 占用的物理内存已经接近或者超过了配置的最大内存限制。这时可以采取
以下几种步骤来处理:

第一，使用 INFO memory 命令查看 Redis 的内存使用情况，看看是否真的达到了最大内存限制。

redis-cli INFO memory

No. 1611 261




## 第 162 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

w/DownLoads/Vkafka/kafka_2.13-3.9.0
redits-cLi

0
# Memory
Used_memory:1891856
Used_memory_human:1.80M
Used_memory_rss:8355840
Used_memory_rss_human:7.97M
Used_memory_peak:2110192
Used_memory_peak_human:2.01M
Used_memory_peak_perc:89.655
Used_memory_overhead :1109624
Used_memory_startup:1098896
Used_memory_dataset:782232
Used_memory_dataset_perc:98.655
aLLocator_aLtLocated:1874736
aLLocator_active:8324096
aLLocator_resident:8324096
totaL_system_memory:137438953472
totaL_system_memory_human:128.006
Used_memory_Lua:31744
Used_memory_vm_evaL:31744
used_memory_Lua_human:31.00K

-        0
第二，如果服务器还有可用内存的话，修改 reais .conf 中的 maxmemory 参数，增加 Redis 的最大内存限制。
比如将最大内存设置为 8GB:

maxmemory 8gb

第三，修改 maxmemory-policy 参数来调整内存淘汰策略。比如可以选择 allkeys-lru 策略，让 Redis 自动删
除最近最少使用的键。

maxmemory-policy allkeys-1lru

memo: 2025年5月25 日修改至此，今天在修改       时，磺到一个西安交通大学本、上海交通大学硕的球
友，985 本硕学历真的非常项了，我会竭尽所能去帮助他，在秋招中斩获一个 SSP offer，冲!

No. 1621 261




## 第 163 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

20mH9 革司5                               西安交通大学
专业成绩 : 加权平均分81.6/100 ( 前25%6 )

主修课程 : 高等数学、线性代数、概率统计、程序设计基础、数据结构、信和号
在校茉誉 : 获得4 呈皮 ，沁 =I年度校级三等奖学金、优秀学生表章
奖。

2-33 9至今                              上海交通大学
专业成绩 : 3.55/4

主修课程 : 矩阵理论、导波光学、光纤传感原理与应用、数字光纤通信。
39.Redis key过期策略有哪些?

Redis 主要采用了两种过期删除策略来保证过期的 key 能够被及时删除，包括惰性删除和定期删除。

如果访问 key 的时候发现过期了，就将其删除
情性删除   十   掉; 如果没有访问，可能就一直不会删除。

              定期删除
Redis 过期数据回收策略                                            每隔一段时间，Redis 都会随机测试一批 key，
并测试期中过期的 key。

沉默王二

惰性删除是最基本的策略，当客户端访问一个 key 时，Redis 会检查该 key 是否已过期，如果过期就会立即删除并
返回 nil。

// 模拟惰性删除的逻辑
Public Object get(String key) {
RedisKey redisKey = getKeyFromMemory(key) 7

if (redisKey != null && isExpired(redisKey)) {
// key已过期，删除并返回nul1
deleteKey(key) ;
return nul17

】}

return redisKey != null ? redisKey.getValue() : null7

)}

这种策略的优点是不会有额外的 CPU 开销，只在访问 key 时才检查。但问题是如果一个过期的 key 永远不被访
问，它就会一直占用内存。

No. 1631261




## 第 164 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

淘汰策略

volatile-lru

检音key的

半期时间
allkeys-lru

volatile
random，

allkeys:
random

volatile-t

noeviction

于是就有了定期删除策略，Redis 会定期随机选择一些设置了过期时间的 key 进行检
这个过程默认每秒执行 10 次，每次随机选择 20 个 key 进行检查。

甩

删除其中已过期的 key。

-这部分面试中可以不背 start---

可以通过 config get hz 命令查看 Redis 内部定时任务的频率。
~ gtit:(master)土132
rediLs-cLt

127.0.0.1:6379> config get hz

1)  "hz
2)  "10"
127.0.0.1:6379>

hz 的值为"10"意味着 Redis 每秒执行 10 次定时任务 。可以通过 coNFIG SET hz 20 进行调整。

No. 1641261




## 第 165 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

wm                       +           纺WarpAl            Resar 四 X
instance due to a bug in the ctient) wittL tead to unbound memory usage in          ee es
the query buffer，However you can configure it here if you have very special        Wan aer of ellents at en

needs，such us huge mutti/exec requests or atike.                               be connected at the Sane ttne
才 maxcttents ffnumber_of_ctients)]

cttent-query-buffer-timtt 1gb                                                                     ntfsnedts to parstst aata to dtk
VE 389

In the Redts protocoL，butk requests，that are，etements representing singte       mm 用

strings，are normatty Limited to 512 mb， However you can change thts Limit

here，but must be lmb or greater                                          4

nottce，varntng

set the path to the tog ftte
proto-max-buLk-ten 512mb                                                                  # ooftte ypatMto/redts'tog

Redis catts an internat function to perform many background tasks，tLike            do
ctLosing connections of ctLients in timeout，purging expired keys that are          后 regutrepass (fpassvord))
never requested，and so forth.                                         at (pand mty Fate) perstetenee
ppendftinine “appendonty .aof
Not att tasks are performed with the same frequency，but Redts checks for          st the ath to the MoF Tt
tasks to perform according to the specified “hz”vatue.                         dr 1patRXtorappenonty/dtrsctory
[人
By defautt "时”is set to 19， Raising the vatue witL use more CPU when
FedtSs TS idUe Dut at the same time wittLU make Redis more responsive when
there are many keys exptring at the same time，and timeouts may be
关 handted with more preciston-。
天                                                                                                                                                                                      Redis 的配时文件在什么位轩
养 The range is between 1 and 599，however a vatue over 199 is usuatty not
关 a good idea。Most users shoutd use the defautt of 19 and ratse this up to
亲 199 onty in environments where very Low Latency is requtred                     Sity

1ocated at /usr/tocat/etcyredts:conf on
hz 109                                                                二

钙

四 、生
Normatty it is usefut to have an HZ vatue whtch is proportionat to the

number of cttents connected. Thts is usefut in order，for instance，to

avotd too many cttents are processed for each background task invocation

in order to avotd Latency sptkes.

钙

Waseudltonety) (Showeanpls ) (NovdolR

Since the defautt HZ vatue by defautt is conservativety set to 19，Redis
offers，and enabtes by defautt，the abiLity to use an adaptive HZ vatue

-这部分面试中可以不背 end---
1. Java 面试指南 (付费) ，
2. java 面试指南 (付费)
3. java 面试指南 (付费) ，

40.二Redis有哪些内存淘汰策略?

当内存使用接近 maxmemory 限制时，Redis 会依据内存淘汰策略来决定删除哪些 key 以缓解内存压力。

录的
录的去
录的京东面经同学

1除策略

Redis key

redis 内存淘汰和过期策略

5Jjava 后端技

redis key过期策略

鲜 noerviction 不淘汰策略

volatile-random 随机删除过
据腾出空间

内存淘汰策略

volatile -ttl 油除剩余时间

鲜 设置了过期时间的数据进行淘汰
@ volatilelru 出除最近最少使用的刍
_                                                  volatile-lfu 删除访问次数最少的键

鲜 淘汰数据策略

allkeys-lru 保留最近使用的key; 删除最近最少
使用 (LRU) 键

@@ 淘汰所有数据        allkeys-lfu 保存常用键; 删除最不常用 (LEU) 键

allkeys-random 随机开除键为添加的新数据中

di由.

No. 1651 261




## 第 166 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

常用的内存淘汰策略有八种，分别是默认的 noeviction，内存不足时不会删除任何 key，直接返回错误信息，生产
环境下基本上不会使用。

然后是针对所有 key 的 allkeys-Iru、allkeys-lfu 和 allkeys-random 。lru 会删除最近最少使用的 key，在纯缓存场
景中最常用，能自动保留热点数据; lfu 会删除访问频率最低的 key，更适合长期运行的系统; random 会随机删
除一些 key，一般不推荐使用。

其次是针对设置了过期时间的 key，有 volatile-Iru、volatile-lfu、volatile-tt| 和 volatile-random。

Iru 在混合存储场景中经常使用。

eservice
public class HybridstorageService 1{

// 重要数据不设置过期时间，临时数据设置过期时间
Public void storeData(String key，Object data，DataImportance importance) {
if (importance == DataImportance.HIGH) {
// 重要数据不设置过期时间，在volatile-*策略下不会被淘汰
redisTemplate.opsForValue().set(key，data);
)} else {
// 临时数据设置过期时间，可以被volatile-*策略淘汰

redisTemplate.opsForValue() .set(key，data，Duration.ofHours(1)) 1

Ifu 适合需要保护某些重要数据不被淘汰的场景; ttl 优先删除即将过期的 key，在用户会话管理系统中推荐使用;
random 仍然很少用。

1. java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: 为什么 redis 快，淘汰策略 持久化
2. java 面试指南(付费) 收录的去哪儿面经同学 1 技术 2 面面试原题: redis 内存淘汰和过期策略
3. java 面试指南(付费) 收录的作业帮面经同学 1 Java 后端一面面试原题: redis内存淘汰策略

41.LRU 和 LFU 的区别是什么?
LRU 是 Least Recently Used 的缩写，基于时间维度，淘汰最近最少访问的键。
LFU 是 Least Frequently Used 的缩写，基于次数维度，淘汰访问频率最低的键。

假设缓存中有三个数据A、B、C，在 LRU 场景下，如果访问顺序是 A一B一C一A，那么此时的 LRU 顺序是
B一C一A，如果需要淘汰，会先删除 B。

但在 LFU 场景下，如果A被访问了 5 次，B 被访问了 2 次，C 被访问了 1 次，那么无论最近的访问顺序如何，都
会优先淘汰 C，因为它的访问频率最低。

LRU 更适合有了明显时间局部性的场景，比如在新闻网站中，用户更关心最新的新闻，而昨天的新闻访问量会急剧下
降。这种情况下，LRU 能很好地保留用户当前关心的热点内容。

LFU 则更适合有长期访问模式的场景，更强调热度"，比如在电商平台中，某些商品可能长期保持热销状态，即使
它们的访问时间间隔较长，但由于访问频率高，LFU 会优先保留这些商品的信息。

No. 1661 261




## 第 167 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

1. java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题: redis内存淘汰机制 延伸到LRU
LFU

memo: 2025 年 5 月 27 日，今天球友发私信说，拿到了哈吧和得物的实习 offer，恭喜他! 叫; 还特意感谢了一
下之前对他简历的修改和学习上的建议。

二哥! 目前有哈另和得物的,量引
0oc，想来问问您的意见

YY

都是-ii

得物是转正的，哈喝那个是boss投
的应该没有转正 (没标)

上次您帮忙修改了简历，还给了一
些学m-呈的建议

很有用

No. 1671 261




## 第 168 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

上午 6:28

42.Redis发生阻塞了怎么解决?

Redis 发生阻塞在生产环境中是比较严重的问题，当发现 Redis 变慢时，我会先通过 monitor 命令查看当前正在执

行的命令，或者使用 slowlog 命令查看慢查询日志。

# 查看当前正在执行的命令
redis-cli MONITOR

# 查看慢查询日志
redis-cli SLOWLOG GET 10

# 检查客户端连接状况

redis-cli CLIENT LIST

通常情况下，大Key 是导致 Redis 阻塞的主要原因之一。比如说直接 DEL 一个包含几百万个元素的 Set，就会导致

Redis 阻塞几秒钟甚至更久。
这时候可以用 UNLINK 命令替代 DEL 来异步删除，避免阻塞主线程。

## 使用 UNLINK 异步删除大 Key

redis-cli UNLINK big_key

对于非常大的集合，可以使用 SCAN 命令分批删除。

No. 1681 261




## 第 169 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Public void safeBatchProcess(String key) {
Scan0ptions options = Scan0ptions.scan0ptions().count(1000) .build();
Cursor<String> cursor = redisTemplate.opsForSet().scan(key，options);

while (cursor.hasNext()) {
String member = cursor.next() 1
// 分批处理，避免阻塞

ProcessElement (member) ;

另外，当 Redis 使用的内存超过物理内存时，操作系统会将部分内存交换到磁盘，这时候会导致 Redis 响应变慢。
我的处理方式是:

使用 free -h 检查内存的使用情况 ; 确认 Redis 的 maxmemory 设置是否合理; 如果发生了内存交换，立即调
整 maxmemory 并清理一些不重要的数据。

大量的客户端连接也可能会导致阻塞，这时候最好检查一下连接池的配置。

econfiguration
public class RedisConnectionConfig {

Bean
public JedisConnectionFactory jedisConnectionFactory() {
JedisPoolConfig poolConfig = new JedisPoolConfig();

poolconfig.setMaxTotal(200) 7       // 最大连接数
poolconfig.setMaxIdle(50)7        // 最大空闲连接
poolconfig.setMinIdle(10)7        // 最小空闲连接
poolconfig.setMaxWaitMillis(3000);  // 获取连接最大等待时间
poolconfig.setTestonBorrow(true); ，// 获取连接时检测有效性

return new JedisConnectionFactory(poolConfig);

Redis 应用
43.Redis如何实现异步消息队列?

Redis 实现异步消息队列是一个很实用的技术方案，最简单的方式是使用 List 配合 LPUSH 和 RPOP 命令。

No. 1691261




## 第 170 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Service

public class SimpleRedisoueue {

Private final RedisTemplate<String，Object> redisTemplate7

// 生产者: 向队列发送消息
public void sendMessage(String queueName，Object message) {
redisTemplate.opsForList() .leftPush(queueName，message) 7

// 消费者: 从队列获取消息
public Object receiveMessage(String queueName) {
return redisTemplate.opsForList() .rightPop(queueName);

// 阻塞式消费，避免轮询

public Object blockingReceive(String queueName，int timeoutSeconds) {
List<Object> result = redisTemplate.opsForList()
.rightPop(queueName，timeoutSeconds，TimeUnit.SECONDS))
return result != null &g& !result.isEmpty() ? result.get(0) : null7

另外就是用 Redis 的 Pub/Sub 来实现简单的消息广播和订阅。

Service

public class RedisPubSubService {

Private final RedisTemplate<String，Object> redisTemplate7

// 发布消息到指定频道
public void publish(String channel，Object message) {
redisTemplate.convertRndSend(channel，message))

// 订阅频道
PostConstruct
public void subscribe() {

redisTemplate.setMessageListener( (message，Ppattern) -> {

No. 1701261




## 第 171 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

System.out .println("Received message: "+ message)

)) 7

redisTemplate.getConnectionFactory() .getConnection().subscribel
new ChannelTopic( "myChannel" ) .getTopic() .getBytes()

) 7

)}

发布者将消息发布到指定的频道，订阅该频道的客户端就能收到消息。

家、
2
Leriper|

但是这两种方式都是不可靠的，因为没有ACK 机制所以不能保证订阅者一定能收到消息，也不支持消息持久化。
44.Redis如何实现延时消息队列?

延时消息队列在实际业务中很常见，比如订单超时取消、定时提醒等场景。Redis 虽然不是专业的消息队列，但可
以很好地实现延时队列功能。

[ceier|

核心思路是利用 ZSet 的有序特性，将消息作为 member，把消息的执行时间作为 score。这样消息就会按照执行
时间自动排序，我们只需要定期扫描当前时间之前的消息进行处理就可以了。

人 on GO
多 竺|
AN

aeService

public class DelayedMessageoueue {

No. 1711261




## 第 172 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Private final RedisTemplate<String，Object> redisTemplate7

// 发送延时消息
public void sendDelayedMessage(String queueName，Object message，1long delaySeconds) {
// 计算消息的执行时间

long executeTime = System.currentTimeMillis() + (delaySeconds * 1000);

// 将消息加入zsSet，以执行时间作为score

redisTemplate.opsForzSet() .add(queueName，message，executeTime)

1og.info( "发送延时消息: {}，延时: {}秒"，message，delaySeconds)

// 消费延时消息
escheduled(fixedDelay = 1000) // 每秒扫描一次
public void consumeDpelayedMessages() {

String queueName = "delayed:queue'")

long currentTime = System.currentTimeMillis())

// 获取已到期的消息 (score <= 当前时间)
Set<Object> messages = redisTemplate.opsForZSet()

.rangeByScore(queueName，0，currentTime) 7

for (Object message : messages) {

try {
// 处理消息

ProcessMessage(message))

// 处理成功后从队列中移除

redisTemplate.opsForZSet() .remove(queueName，message);

1og.info( "处理延时消息成功: {}"，message) 7;

} catch (Exception e) {
log.error("处理延时消息失败: {}"，message，e)7
// 可以实现重试机制

handleFailedMessage(queueName，message);

具体实现上，我会在生产者发送延时消息时，计算消息应该执行的时间戳，然后用 ZADD 命令将消息添加到 ZSet
中。

2ZRADD delay_queue 1617024000 taskl
消费者通过定时任务，使用 ZRANGEBYSCORE 命令获取当前时间之前的所有消息。

ZREMRANGEBYSCORE delay_queue -inf 1617024000

No. 1721 261




## 第 173 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

处理完成后再用 ZREM 删除消息。

ZREM delay_queue task1l

在技术派实战项目中，我就用这种方式实现了文章定时发布的功能。作者在发布文章时，可以选择一个未来的时间
节点，比如说 30 分钟后，系统就会向延时队列发送一条延时消息，然后定时任务就会在 30 分钟后将这条消息从
延时队列中取出并发布文章。

1. java 面试指南 (付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: Redis 实现延迟队列

2. java 面试指南(付费) 收录的字节跳动面经同学 8 java 后端实习一面面试原题: redis 数据结构，用什
么结构实现延迟消息队列

memo: 2025年5月28 日修改至此，今天有球友在 VIP群里发消息说拿到了荣耀的暑期实习 offer，虽然时间节
点已经不早了，但越是到这个时候，确实容易捡漏。

No. 1731261




## 第 174 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

二哥编程星球VIP9群 (443) (

希- 沉默王二-二哥: 面渣逆袭MyS..     共2条

作三年，个人感觉后面纯流水线了，学不到什么

东西
F    荣耀oc了蚀
避    最水的一集

还以为要0offer备战秋招了

在香蜜湖吗?

2有 思:荣耀cc了角

要不是二哥，我仅仅只是比本科毕业多了两张纸而
已

45.二Redis支持事务吗?

是的，Redis 支持简单的事务，可以将 multi、exec、discard 和 watch 命令打包，然后一次性的按顺序执行。

No. 1741261




## 第 175 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

服务器接到来自客户端的命令

命令是否
EXEC 、DISCARD 、
MULTI或 WATCH ?

基本流程是用 multi 开启事务，然后执行一系列命令，最后用 exec 提交。这些命令会被放入队列，在 exec 时批量
执行。

No. 1751261




## 第 176 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

127.0.0.1:6379> SET mycounter 0
OK

127.0.0.1:6379> WATCH mycounter
OK

127.0.0.1:6379> GET mycounter
10"

127.0.0.1:6379> MULTI

OK

127.0.0.1:6379(TX)> INCR mycounter
QUEUED

127.0.0.1:6379(TX)> EXEC

1) (integer) 1

当客户端处于非事务状态时，所有发送给 Redis 服务的命令都会立即执行; 但当客户端进入事务状态之后，这些命
令会被放入一个事务队列中，然后立即返回 QUEUED，表示命令已入队。

服务器接到来自客户端的命令

|

一                       客户端是否正处于事务状态?                         -一
将命令放进事务队列里            执行命令

/       、

向客户端到加QUEWED 字符各 。。 向客户端返回命令的执行结果

当 exec 命令执行时，Redis 会将事务队列中的所有命令按先进先出的顺序执行。当事务队列里的命令全部执行完
毕后，Redis 会返回一个数组，包含每个命令的执行结果。

discard 命令用于取消一个事务，它会清空事务队列并退出事务状态。

No. 1761 261




## 第 177 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

w“/DownLoads/kafka/kafka 2.13-3.9.0
redis-cLi

127.0.0.1:6379> Set "itwanger:age”18
OK

127.0.0.1:6379> mutLti
OK

127.0.0.1:6379(TX)> decr "itwanger:age"

QUEUED

127.0.0.1:6379(TX)> discard

OK

(2.37s )

127.0.0.1:6379> get "itwanger:age"
1 18 1

127.0.0.1:6379>

watch 命令用于监视一个或者多个 key，如果这个 key 在事务执行之前 被其他命令改动，那么事务将会被打断。

时间             客户端 A                         Redis 实例                       客户端 B
开始
一一一           WATCH order'books              监控 order:books
是否变化                   由
MULTI                        将A 的指令暂                |
DECR orderbooks                   存到命令队列

1. 执行 B 的指令将

|]
order:books 的值- 1。                DECR order:books
2. 记录 order:books 已      邓      Ru
经发生变化
jL                                  EXEC
NU                                                  放弃执行 A 的事务

但 Redis 的事务与 MySQL 的有很大不同，它并不支持回滚，也不支持隔离级别。

No. 1771261




## 第 178 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

说一下 Redis 事务的原理?
Redis 事务的原理并不复杂，核心就是一个"先排队，后执行"的机制。

Redis 事务工作流程

NULTI

当执行 MULTI 命令时，Redis 会给这个客户端打一个事务的标记，表示这个客户端后面发送的命令不会被立即执
行，而是被放到一个队列里排队等着。

广
Redis Transaction      人multicnd            robjx[3]
J
argv       Stringobject | String0bject | stringobject
"SET    "fanone"
argc 3
cmd
multiCmd[3]
~、
[三    [o]    旧玉  multiCmd      「       robjx[3]       ]
[1]             argv   六一一> | stringobject |String0bject | Stringobject
一一一   人_"sEm   "fantwo"    2
[2]             argc 3
人             人   cmd
fmulticnd 1     f    robjx[2]     ]
argv   三一一> | String0bject | String0bject
|  "ET    "fanone"   |
argc 2
cmd
\
绝 公众号 .

当 Redis 收到 EXEC 命令时，它会把队列里的命令一个个拿出来执行。因为 Redis 是单线程的，所以这个过程不会
被其他命令打断，这就保证了Redis 事务的原子性。

No. 1781 261




## 第 179 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Watched_keys

当执行 WATCH 命令时，Redis 会将 key 添加到全局监视字典中; 只要这些 key 在 EXEC 前被其他客户端修改，
Redis 就会给相关客户端打上脏标记，EXEC 时发现事务已被干扰就会直接取消整个事务。

// 全局监视字典
dict *watched_keys1

typedef struct watchedKey {
robj *keyy
redisDb *db)

} watchedKey)

DISCARD 做的事情很简单直接，首先检查客户端是否真的在事务状态，如果不在就报错; 如果在事务状态，就清
空事务队列并退出事务状态。

void discardCommand(client *c) {
if (!(c->flags & CLIENT _MULTI)) {
addRep1YError(c,"DISCRRD without MULTI") 7
returny
】}
discardTransaction(c) 17
addReply(c,shared.ok);

No. 1791 261




## 第 180 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

上

点?

局:

Redis 事务有哪些注

最重要的的一点是，Redis 事务不支持回滚，一旦 EXEC 命令被调用，所有命令都会被执行，即使有些命令可能执

Redis事务为什么不支持回滚?

Redis 的核心设计理念是简单、高效，而不是完整的 ACID 特性。而实现回滚需要在执行过程中保存大量的状态信
息，并在发生错误时逆向执行命令以恢复原始状态。这会增加 Redis 的复杂性和性能开销。

襄

What about rollbacks?

Redis does not support rollbacks of transactions since Supporting rollbacks would have a
Significant impact on the simplicity and performance of Redis.

Redis事务满足原子性吗? 要怎么改进?

Redis 的事务不能满足标准的原子性，因为它不支持事务回滚，也就是说，假如某个命令执行失败，整个事务并不
会自动回滚到初始状态。

// 一个转账事务

redisTemplate.multil()7

redisTemplate.opsForValue() .decrement("user:1:balance"，100); // 成功
redisTemplate.opsForList() .LeftPush("user:1:balance"，"1og");  // 类型错误，失败
redisTemplate.opsForValue() .increment("user:2:balance"，100);  // 还是会执行
List<Object> results = redisTemplate.exec();

// 结果: 用户1被扣了钱，用户2也收到了钱，但中间的日志操作失败了
// 这符合Redis的原子性定义，但不符合业务期望

可以使用 Lua 脚本来替代事务，脚本运行期间，Redis 不会处理其他命令，并且我们可以在脚本中处理整个业务还
辑，包括条件检查和错误处理，保证要么执行成功，要么保持最初的状态，不会出现一个命令执行失败、其他命令
执行成功的情况。

eservice
public class ImprovedTransactionService {

Public boolean atomicTransfer(String fromUser，String toUser，int amount) {
String luaScript =
"Local from_ key = KEYS[1] "+
"local to_key = KEYS[2] "+

"Local amount = tonumber(RRGV[1]) "+

// 检查转出账户余额
”local from_ balance = redis.call('GET'，from key) ”+

"iiE not from _ balance then Feturn -1 end ”+

"from_ balance = tonumber(from balance) ”+

No. 1801261




## 第 181 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

"iiE from _ balance < amount then return -2 end ”+

// 检查转入账户是否存在

"if redis.call('EXISTS'，to_key) == 0 then return -3 end "+

// 所有检查通过，执行转账

"redis.cal1('DECRBY'，from key，amount) "+
"redis.call1('INCRBY'，to_key，amount) "+

// 记录转帐日志

"local log = from key .. ':' ..to key .. ':' .， amount "+
"redis.call('LPUSH'， "transfer:1og'，1og) "+
"return 1"7

DefaultRedisScript<Long> script = new DefaultRedisScript<>() 7
script.setScriptText(luaScript))
script.setResultType(Long.class) 7

Long result = redisTemplate.execute(script，

Rrrays.asList("user:" + fromUser + ":balance"，"user:" + toUser +
":balance" )，

amount ) 7

Leturn result != nul1l && result ==

Redis 事务的 ACID 特性如何体现?

单个 Redis 命令的执行是原子性的，但 Redis 没有在事务上增加任何维持原子性的机制，所以 Redis 事务在执行过
程中如果某个命令失败了，其他命令还是会继续执行，不会回滚。

全部执行成功                                                                 全部执行失败
广                                            、\         厂                                           ”FF                                           六

No. 1811 261




## 第 182 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

一致性指的是，如果数据在执行事务之前是一致的，那么在事务执行之后，无论事务是否执行成功，数据也应该是
一致的。但 Redis 事务并不保证一致性，因为如果事务中的某个命令失败了，其他命令仍然会执行，就会出现数据
不一致的情况。

Redis 是单线程执行事务的，并且不会中断，直到执行完所有事务队列中的命令为止。因此，我认为 Redis 的事务
具有隔离性的特征。

Redis 事务的持久性完全依赖于 Redis 本身的持久化机制，如果开启了 AOF，那么事务中的命令会作为一个整体记
录到 AOF 文件中，当然也要看 AOF 的 fsync 策略。

如果只开启了 RDB，事务中的命令可能会在下次快照前丢失。如果两个都没有开启，肯定是不满足持久性的。

1. java 面试指南 (付费) 收录的华为一面原题: 说下 Redis 事务
2二哥编程星球球友枕云眼         试原题: 什么是 redis 的事务，它的 ACID 属性如何体现
3. java 面试指南(付费) 收录的快手同学 4 一面原题: Redis事务满足原子性吗? 要怎么改进?

memo: 2025 年5 月 29 日，今天给球友修改简历时，碰到一个东南大学本硕博 3 985 的球友，这也是我已知信
息中学历最高的球友了。

No. 182 1 261




## 第 183 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

收件人:   入  www.qing_gee<www.qing_gee@163.com>

时 间: 2025年05月28日 12:01 (星期三)
附 件: 1个(加简历 ; .时?9 4.docx ) 查看附件

【升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

一豆
一圳

您好! 我是刚加进星球的新人(星球编号是气例;寻求二哥的帮助，麻烦二哥帮有我改改简历。
我的情况是东南大学本硕博，都是计算机专业，算是3 985，但是博士没有毕业，想以硕士学友

46.有Lua脚本操作Redis的经验吗?

Lua 脚本是处理 Redis 复杂操作的首选方案，比如说原子扣减库存、分布式锁、限流等业务场景，都可以通过 Lua
脚本来实现。

Clients     Sentinels
co。    an居=思。    Redis Server

Redis"               1      |
Lua Scripts
Diagram

六 | 。 client clsendsatua scriptrequest

Script nunin progress server blods
训other requests

Scriptends (OK or ERR)
Everyone 党unblocked so everyone
Sees either no changes from the Script
orall changesfrom the Script

YYYY

目 ScaleGrid

在秒杀场景下，可以用 Lua 脚本把所有检查逻辑都写在一起: 先看库存够不够，再看用户有没有买过，所有条件都
满足才扣减库存。因为整个脚本是原子执行的，Redis 在执行期间不会处理其他命令，所以可以彻底解决超卖问

题。

No. 1831 261




## 第 184 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

// 这个秒杀脚本救了我的命
String luaScript =
"local stock

redis.call('GET'，KEYS[1]) ”+
"if not stock or tonumber(stock) < tonumber(RRGV[2]) then ”+
上   return -1 "+ // 库存不足

"end "+

"if redis.call1('SISMEMBER'，KEYS[2]，RRGV[1]) == 1 then ”上+
上   return -2 ”+ ，// 重复购买

"end "+

"redis.cal1('DECRBY'，KEYS[1]，RRGV[2]) ”+
"redis.cal1('SADD'，KEYS[2]，RARGV[1]) "+
"return 1"7

在分布式锁场景下，我一开始用的 SETNX 命令来实现，结果发现如果程序异常退出，锁就死掉了。后来加了过期
时间，但又发现可能误删其他线程的锁。最后还是用 Lua 脚本彻底解决了这个问题，确保只有锁的持有者才能释放
锁。

// 解锁脚本特别重要，必须验证是自己的锁才能删

Private final String UNLOCK_SCRIPT =
"if redis.call('GET'，FKEYS[1]) == RARGV[1] then "+
"    return redis.call('DEL'，KEYS[1]) ”+
"else "十

Teturn 0 ”十
wendv

甚至还可以用 Lua脚本实现滑动窗口限流器，一次性完成过期数据清理、计数检查、新记录添加三个操作，而且完
全原子化。

// 滑动窗口限流，逻辑清晰，性能还好

String luaScript =

KEYS[1] ”+
tonumber(RRGV[1]) "+
"Local window = tonumber(RRGV[2]) "+
"local limit = tonumber(RRGV[3]) ”+

"local key

"Local now

// 先清理过期记录
"redis .cal1('ZREMRRNGEBYSCORE'，key，0，now - window) "+

// 检查当前请求数
"local current = redis.cal1('ZCRRD'，key) "+

"if current < limit then ”十

reqdis.cal1('ZRDD'，key，now，now) "十
"    return 1 "二
"else "十

Teturn 0 ”十
wendv

memo: 2025年 5 月 30 日，今天有球友在星球里发消息说拿到了金山办公的 offer，问我该选 cpp 还是go，我的
建议大家可以看看符合是否合理，不管如何选择，真的恭喜球友!

No. 1841261




## 第 185 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥，现在真拿到金山办公的 offer 了

但是还是面临 cpp 和 go 的选择问题

主要是想知道这两个语言的后期发展趋势

cpp 是客户端开发，就是 wps 那套

qt 开发

golang 应该是云相关的

具体还没说

引膨杰与引上本读

想问问您的意见

47.Redis的管道Pipeline了解吗?

了解，Pipeline 允许客户端一次性向 Redis 服务器发送多个命令，而不必等待一个命令响应后才能发送下一个
Redis 服务器会按照命令的顺序依次执行，并将所有结果打包返回给客户端。

No. 1851261




## 第 186 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

TITTTTD
发送pipeline
pzztt
client
返回pipeline
结果
GANAA
CCLLLLLLG

正常情况下，每执行一个 Redis 命令都需要一次网络往返: 发送命令 -> 等待响应 -> 发送下一个命令。

客户端                    Redis服务器
|                                                              |

如果大量请求依次发送，网络延迟会显著增加请求的总执行时间，假如一次 RTT 的时间是 1 毫秒，3 个就是 3 毫
秒。有了 Pipeline 后，可以一次性发送 3 个命令，总时间就只需要 1 毫秒。

aeService

public class RedisBatchService {

Public void batchInsertUsers(List<User> users) {
// 不用Pipeline的错误做法 - 很慢
// for (User user : users) {

//    redisTemplate.opsForValue().set("user:" + user.getId()，user);
V// )}

// 使有pipeline的正确做法

redisTemplate.executePipelined(new RedisCallback<Object>() {
eoverride

No. 1861 261




## 第 187 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Public Object doInRedis(RedisConnection connection) throws
DataRccessException {
for (User user : users) {
String key = "user:”" + user.getId() 1;
byte[] keyBytes = key.getBytes();
byte[] valueBytes = serialize(user))

connection.set(keyBytes，valueBytes)

}
return nul1; // Pipeline不需要返回值

)) 7

当然了，Pipeline 不是越大越好，太大会占用过多内存，通常建议每个 Pipeline 包含 1000 到 5000 个命令。可以
根据实际情况调整。

public void smartBatchInsert(List<String> data) {

int batchsize = 1000; // 经验值，根据数据大小调整

for (int ii = 0;) 1<data.size();) i+= batchSsize) {
List<String> batch = data.subList(i，Math.min(i + batchSize，data.size()));

redisTemplate.executePipelined(new RedisCallback<Object>() {

eoverride
Public Object doInRedis(RedisConnection connection) throws
DataRccessException {
for (String item : batch) {
connection.set(item.getBytes()，item.getBytes()) 7

】}

return nul17

)) 7

什么场景下适合使用 Pipeline呢?

需要批量插入、更新或删除数据，或者需要执行大量相似的命令时。比如: 系统启动时的缓存预热 -> 批量加载执
点数据; 比如统计数据的批量更新;比如大批量数据的导入导出;比如批量删除过期或无效的缓存。

有了解过 Pipeline 的底层原理吗?

有，其实就是缓冲的思想。在技术派实战项目中，我就在 RedisClient 类中封装了一个 PipelineAction 内部类，用
来缓存命令。

No. 1871 261




## 第 188 页


 ForumCoreAutoConfig.java    Z RedisClientjava X                   人> 加
J-core) src/ main / java/ com/ github / paicoding / forum / core / cache / RedisClientjava / 名 RedisCclier

pubLic cLass                     工

pubLic static cLass            {
private    <|      > run = new ArrayList<>();

private                   connection;

pubLic             add       key，                      1    []> conml
run.add(() -> conn.accept(connection,         .keyBytes(key)));
return this;

pubLic            add      key，                     <|
run.add(() -> conn.accept(connection，         .keyBytes(key)，vaLBytes
return this;

pubLic      execute
tempLate.executePipeLined((         <    >) connection -> {
.this.connection = connection;
run.forEach       :Pun)
return

]);

add 方法将命令包装成 Runnable 对象，放入 List 中。当执行 execute 方法时，再调用 RedisTemplate 的
executePipelined 方法开启管道模式将多个命令发送到 Redis 服务端。

No. 1881 261





## 第 189 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

 ForumCoreAutoConfig.java     台 RedisClientjava     J RedisTemplate.class Xx         上

RedisTempLate<K，V>          RedisAccessor              Redis0perations<K

Qoverride
List<0bject>      Pipetil   RedisCaLLback<?> action，G@NULLabLe RedisSe

booLean pipeLinedCLosed = faLse;

0bject resutLt = action.doInRedis(connection) ;
(resutLt != nuLL) {
InvatLidData    sApiUsagei     ion(
aLLback cannot return a non-nuLL vaLue as it gets !

}

List<0bject> cLosePipeLine = Eornection.cLosePipeLine())
pipeLinedCLosed = true;
deseri   |   dResuLts(cLosePipeLine，resuLtSeriaLizer，hashl

(!pipeLinedCLosed)] {
Connection.cLosePipeLine();

Redis 服务端从输入缓冲区读到命令后，会按照 RESP 协议进行命令拆解，再依次执行这些命令。执行结果会写入
到输出缓冲区，最后再将所有结果一次性返回给客户端。

typedef struct client {

sds querybuf;         // 输入缓冲区
1ist *reply7         // 输出缓冲区链表
    qd long reply_bytes; // 输出缓冲区大小
} client;
1. java 面试指南 (付费) 收录的京东面经同学 8 面试原题: 对pipeline的理解，什么场

pipeline? 有了解过pipeline的

memo: 2025 年 6 月1 日，今天有球友在星球里发    竞拿到了百得思维的offer，他是民办二本，对这个结果很
满意，也很感谢面渣逆效和星球的实战项目，让他摆脱了浑浑焉垩的日子。恭喜他!

No. 1891261




## 第 190 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

本    1                                                                                二 收进专栏

#晒个offer点 二哥，你好，本人是一个民办二本，很感谢二哥的八股和学习资料，让我拿
下了百得思维的offer，对于我现在的水平我已经很开心了食 傅要不是你，我现在还浑浑下
蛋的混日子，超级超级超级感谢二哥党党

晒个offer鼻

48.二Redis能实现分布式锁吗?

分布式锁是一种用于控制多个不同进程在分布式系统中访问共享资源的锁机制。它能确保在同一时刻，只有一个节
点可以对资源进行访问，从而避免分布式场景下的并发问题。

可以使用 Redis 的 SETNX 命令实现简单的分布式锁。比如 sET key value NX PX 3000 就创建了一个锁名为

key 的分布式锁，锁的持有者为 value 。NX 保证只有在 key 不存在时才能创建成功，EX 设置过期时间用以防止
死锁。

Redis如何保证 SETNX 不会发生冲突?

当我们使用 SET key value NX EX 30 这个命令进行加锁时，Redis 会把整个操作当作一个原子指令来执行。因
为 Redis 的命令处理是单线程的，所以在同一时刻只能有一个命令在执行。

比如说两个客户端A和 B 同时请求同一个锁:

No. 1901261




## 第 191 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

客户端&A: SET lock_key uuid _a NX EX 30
客户端B: SET lock _key uuid b NX EX 30

虽然这两个请求可能几乎同时到达 Redis 服务器，但 Redis 会严格按照到达的先后顺序来处理。假设 A 的请求先
到，Redis 会先执行A的 SET 命令，这时 lock_key 被设置为 uuid_a。

当处理 B 的请求时，因为 lock_key 已经存在了，NX 条件不满足，所以 B 的 SET 命令会失败，返回 NULL。这样
就保证了只有和A 能获取到锁。

关键点在于 NX 的语义: Nom EXISTS ，只有在 key 不存在的时候才会设置成功。Redis 在执行这个命令时，会先
检查 key 是否存在，如果不存在才会设置值，这整个过程是原子的，不会被其他命令打断。
SETNX有什么问题，如何解决?

使用SETNX 创建分布式锁时，虽然可以通过设置过期时间来避免死锁，但会误删锁。比如线程 A 获取锁后，业务
执行时间比较长，锁过期了。这时线程 B 获取到锁，但线程 A 执行完业务逻辑后，会尝试删除锁，这时候删掉的
其实是线程 B 的锁。

线程4获取锁
线程4执行业务
过期释放锁的同时
AN
锁过期释放钞                           线程B获取锁

此时锁归线程B拥有
线程4继续执行业务

天
释放的是线程B的锁
线程4释放锁

No. 1911 261




## 第 192 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

可以通过锁的自动续期机制来解决锁过期的问题，比如 Redisson 的看门狗机制，在后台启动一个定时任务，每隔
一段时间就检查锁是否还被当前线程持有，如果是就自动延长过期时间。这样既避免了死锁，又防止了锁被提前释
放。

redisson处理逻辑

每10s检验是否持有
锁，如果持有则
延长锁的时间
蛙
                                                                                    Redis         [|         Redis
(Master)                            (Salve)

释放锁unlock

线程2

Redisson

while循环尝试加锁
(自旋锁)

否

memo: 2025年6月2 日修改至此，今天在帮一个学院本球友分析 offer 选择后，他又回复说多亏了星球才能一
路走到现在，很满足这个结果。看多了拿大厂 offer 球友的感谢，看到学院本也能取得满意的成绩，我也很开心。

=电 回复 沉默王二: 好听，谢谢二哥解惑，也是跟着二哥的星球一路走来才有了offer的，对
于学院本来说也已经很满足了
口 四

沉默王二 回复 也旺 : 继续加油!
让

Redisson了解多少?

Redisson 是一个基于 Redis 的java 客户端，它不只是对 Redis 的操作进行简单地封装，还提供了很多分布式的数
据结构和服务，比如最常用的分布式锁。

No. 1921 261




## 第 193 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

RLock lock = redisson.getLock("lock'"))
lock.lock() 7
try {
// do something
} finally {
lock-unlock();

Redisson 的分布式锁比 SETNX 完善的得多，它的看门狗机制可以让我们在获取锁的时候省去手动设置过期时间的
步骤，它在内部封装了一个定时任务，每隔 10 秒会检查一次，如果当前线程还持有锁就自动续期 30 秒。

Private Long tryRcquire(long waitTime，1long leaseTime，TimeUnit unit，1long threadId) {
return get(tryRcquireRsync(waitTime，1leaseTime，unit，threadId) ) ;

Private <T> RFuture<Long> tryRcquireRsync(long waitTime，1ong leaseTime，TimeUnit unit，
long threadId) {
REFuture<Long> ttlRemainingFuturey
if (leaseTime != -1) {
// 手动设置过期时间
ttlRemainingFuture = tryLockInnerRsync(waitTime，1leaseTime，unit，threadId，
RedisCommands .EVARL_LONG)
} else {
// 启用看门狗机制，使用默认的30秒过期时间
ttlRemainingFuture = tryLockInnerRsync(waitTime，internalLockLeaseTime，
TimeUnit .MILLISECONDS，threadId，RedisCommands .EVAL_LONG) 7

// 处理获取锁成功的情况
tt1RemainingFuture.onComplete((ttlRemaining，e) -> 1{
if (e != null) {

returny
}
// 如果获取锁成功且启用看门狗机制
if (ttlRemaining == null) {
if (leaseTime != -1) {
internalLockLeaseTime = unit.toMillis(leaseTime) 1;
} else {
scheduleExpirationRenewal(threadId); // 启动看门狗
】}
}

)) 7
return ttlRemainingFuturey

另外，Redisson 还提供了分布式限流器 RRateLimiter，基于令牌桶算法实现，用于控制分布式环境下的访问频

// RPI 接口限流
RestController

No. 1931261




## 第 194 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

public class Apicontroller {

8RAutowired
Private RedissonClient redissonClient;

eGetMapping("/api/data")

public ResponseEntity<?> getData() {
RRateLimiter limiter = redissonClient.getRateLimiter("api.data') 7
limiter.trySetRate(RateType.OVERALL，100，1，RateIntervalUnit .MINUTES) 7

if (limiter.tryRcquire()) {

// 处理请求

return ResponseEntity.ok(ProcessData()) 7
} else {

// 限流触发

return ResponseEntity.status(429) .body("Rate limit exceeded'");

详细说说Redisson的看门狗机制?
Redisson 的看门狗机制是一种自动续期机制，用于解决分布式锁的过期问题。

基本原理是这样的: 当调用 lock() 方法加锁时，如果没有显式设置过期时间，Redisson 会默认给锁加一个 30
秒的过期时间，同时启用一个名为"看门狗"的定时任务，每隔 10 秒 (默认是过期时间的 1/13) ，去检查一次锁是否

还被当前线程持有，如果是，就自动续期，将过期时间延长到 30 秒。

每隔10秒看下，如果还持有
锁，延长生存时间

while不停的尝试获取锁       执行lua脚本

// 伪代码展示核心逻辑
Private void renewExpiration() {
Timeout task = commandExecutor.getConnectionManager()
-newTimeout (new TimerTask() {
aoverride
public void run(Timeout timeout) {

// 用 Lua 脚本检查并续期

No. 1941261




## 第 195 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

if (redis.call("get"，1lockKey) == currentThreadId) {
redis.call("expire"，1lockKey，30) 1
// 递归调用，继续下一次续期
renewExpiration() 7

】}

}，10，TimeUnit .SECONDS) 7

续期的 Lua 脚本会检查锁的 value 是否匹配当前线程，如果匹配就延长过期时间。这样就能保证只有锁的真正持有
者才能续期。

当调用 unlock() 方法时，看门狗任务会被取消。或者如果业务罗辑执行完但忘记 unlock 了，看门狗也会帮有我们
自动检查锁，如果锁已经不属于当前线程了，也会自动停止续期。

这样我们就不用担心业务执行时间过长导致锁被提前释放，也避免了手动估算过期时间的麻烦，同时也解决了分布
式环境下的死锁问题。

看门狗机制中的检查锁过程是原子操作吗?
是的，Redisson 使用了 Lua 脚本来保证锁检查的原子性。

No. 1951 261




## 第 196 页


渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

在文件中查找                                                                                 文件掩码(A):
Q- tryLocklnnerAsync

在项目 (P) ”模块 (M) ”目录 (D) ”作用域(S)   所有位置

(leaseTime, unit, threadld, RedisCommands.EVAL_LONG);
RFuture<Long> ttlIRemainingFuture =                      (internalLockLeaseTime,
<T> RFuture<T>                        (long leaseTime, TimeUnit unit, long threadld, RedisSt RedissonSpinLockJjava 126
<T> RFuture<T>                     (long waitTime,      leaseTime, TimeUnit unit，      thn
ttlRemainingFuture =                    (waitTime, leaseTime, unit, threadld, RedisCcommands

ttIRemainingFuture =                                 (waitTime, internalLockLeaseTime,

ttlRemainingFuture =                    (waitTime, leaseTime, unit, threadld, RedisCommands

ttIRemainingFuture =                                 (waitTime, internalLockLeaseTime,

RedissonSpinLockJjava
1 局   <1> Frutures1> CryLuckxnnerasynmck    Leaselume，Iumeunt unuty

internaLLockLeaseTime = unit.toMiLLis(LeaseTime)

evaLWriteAsync(getRawName()，LongCcodec.INSTANCE，command
十

十

CoLLections.singLetonList(getRawName())，internaLLockLeaseTime，getLol

在新标签打开 (B)                                                                                                 打开查找窗口

Redis 在执行 Lua 脚本时，会把整个脚本当作一个命令来处理，期间不会执行其他命令。所以 hexists 检查和
expire 续期是原子执行的。

Redlock你了解多少?

Redlock 是 Redis 作者 antirez 提出的一种分布式锁算法，用于解决单个 Redis 实例作为分布式锁时存在的单点故

障问题。

Redlock 的核心思想是通过在多个完全独立的 Redis 实例上同时获取锁

No. 1961261





## 第 197 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

pubtLic clLass RedissonRedLocK extends RedissonMuttiLock {

pubtLic                    (CRLock... Locks)    super(Locks) ;

@override
protected ii            (0 return Locks.size() - minLocksAmount(Locks);

protected ii             (finaL List<RLock> Locks)   return Locks.size() /  十

Q@override
protected                (Long remainTime)] return Math.max(remainTime / Locks.size()，1);

@override
pubtic void       (0 unLockInner(Locks);

minLocksAmount 方法返回的 locks.size()/2 + 1 ，正是 Redlock 算法要求的少数服从多数原则。
failedLocksLimit 方法会计算允许失败的锁数量，确保即使部分实例失败，只要成功的实例数量超过一半就认为获
取锁成功。

红锁会党试依次向所有 Redis 实例获取锁，并记录成功获取的锁数量，当数量达到 minLocksAmount 时就认为获
取成功，否则释放已获取的锁并返回失败。

虽然 Redlock 存在一些和争议，比如说时钟漂移问题、网络分区导致的脑裂问题，但它仍然是一个相对成熟的分布式
锁解决方案。

红锁能不能保证百分百上锁?

不能，Redlock 无法保证百分百上锁成功，这是由分布式系统的本质特性决定的。

当有网络分区时，客户端可能无法与足够数量的 Redis 实例通信。比如在 5 个 Redis 实例的部署中，如果网络分区
导致客户端只能访问到 2 个实例，那么无论如何都无法满足红锁要求的少数服从多数原则，获取锁的时候必然失
败。

Public boolean tryLock(long waitTime，1long leaseTime，TimeUnit unit) thz

InterruptedException {

for (ListIterator<RLock> iterator = locks.1listIterator()) iterator.hasNext();) {
RLock lock = iterator.next()7
boolean lockRcquired;
try {
lockRcquired = lock.tryLock(awaitTime，newLeaseTime，TimeUnit.MILLISECONDS) ;

} catch (RedisResponseTimeoutException e) {

No. 1971 261




## 第 198 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

lockRcquired = false; // 网络超时导致失败
} catch (Exception e) {
lockRacquired = false; // 其他异常导致失败

】}

// 如果剩余可尝试的实例数量不足以达到多数派，直接退出
if (locks.size() - acquiredLocks.size() == failedLocksLimit()) {

break;

}
}

// 检查是否达到多数派要求
if (acquiredLocks.size() >= minLocksamount(locks)) {
return truey

} else {
unlockInner(acquiredLocks) 7

return false; // 未达到多数派，获取失败

时钟漂移也会影响成功率。即使所有实例都可达，如果各个 Redis 实例之间存在明显的时钟漂移，或者客户端在获
取锁的过程中耗时过长，比如网络延迟、GC 停顿等，都可能会导致锁在获取完成前就过期，从而获取失败。

在实际应用中，可以通过重试机制来提高锁的成功率。

for (int 1 = 0; 宇< maxRetries; i++) {
if (redLock.tryLock(waitTime，1leaseTime，TimeUnit .MILLISECONDS)) {
return truey

}
Thread.sleep(retryDelay) 7

)}

return falsei

项目中有用到分布式锁吗?

在PmHub项目中，我有使用 Redission 的分布式锁来确保流程状态的更新按顺序执行，且不被其他流程服务干
扰。

No. 1981 261




## 第 199 页


加，

面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

回Pmhub入成Redis分布式锁保障流程状态更新【号必看) 四          四人富 3 吏 名 E3 外

轴 来个offer-pm… 已 “和…
大网 @ =
Q                        十                                                                                         什么是锁? 本地锁的问题

中 计                                                                什么是分布式锁
9                               分布式锁特性

王 引入         旨汪                           一一                       分布式针的几种实现方式

加pmHub Gateway全局过                                                                                                                              Redission 分布式镇

加pmHub整全Transmittab                                                                                                        - 项目实战

Emomo                                             里                             | 业务漠理

mHub用Docker Comp.                                                                 一    添加依赖

回PmHub集成Redis分布…                                   新建项目                               添加配置

回PmHub的性能监控和分                                                                 流程 。。 RedissonConfg

加PmHub实现RedisjnLua,                                                                -一

里                                 定义定义IDistributedLock分布式锁

mhub自定义注册加人                                                                                                                                   IDistibutedLock实现类

回PmHub集成 Sentinel+O                                                                新建任务                                        [六一 定义DistrbutedLock注解

加PmHub分布式事务Seat. …                                                                流程    AOP切面控制

po                                                                            定义分布式锁启动元注解

Hub台人
mHub台全Rocketmq                                         ，                                  全用

加PmHub如何保证缓存和                                                                                    1启用分布式锁         工

~ 产品设计入                          更新设置一姑| 任务审批设置                        2、更新审批设秆接口添加注解”10
面试

回人人都是产品经理，打造…                     等待锁释放                                        本                 血

回PmHub 需求分析及可行                                                                                                                                                                                                               日

加PmHub 项目管理流各

回PmHub 产品原型设计

1.
2.

11.
12.

pmhu        4山科党理

java 面试指南(付费) 收录的腾讯 java 后端实习一面原题: 分布式锁用了 Redis 的什么数据结构

java 面试指南(付费)_收录的小公司面经合集同学 1 Java 后端面试原题: Redisson 的底层原理? 以及
与 SETNX 的区别?

.java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习java 后端面试原题: redis 分布式锁的

实现原理? setnx?

. java 面试指南 (付费) 收录的小米同学 F 面试原题: 自己实现 redis 分布式锁的坑 (主动提了

Redission)

、 java 面试指南 (付费) 收录的腾讯云智面经同学 20 二面面试原题: redission 的原理是什么? setnx +

lua 脚本?

. java 面试指南 (付费) 收录的收钱吧面经同学 1 java 后端一面面试原题: 系统里面分布式锁是怎么做

的? 你提到了redlock，那它机制是怎么样的? 红锁能不能保证百分百上锁?

. java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: 加分布式锁时redis如何

保证不会发生冲突? 分布式锁过期怎么办?

.java 面试指南 (付费) 收录的拼多多面经同学 8 一面面试原题: Redis分布式锁如何实现的
. java 面试指南 (付费) 收录的百度同学 4 面试原题: Setnx,知道吗? 用这个加锁有什么问题吗?怎么解

决?

. java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题: 分布式锁用redis实现思路

java 面试指南(付费) 收录的京东面经同学 9 面试原题: redis的分布式锁有了解过吗
java 面试指南(付费) 收录的同学 30 腾讯音乐面试原题: redis锁有几种实现方式

No. 1991261




## 第 200 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

memo: 2025年6月3 日修改至此，今天在修改球友的简历时，碰到一个 211 本科、北京大学软微学院的球友，
我只能说，星球的球友真是人才济济啊! 祝大家都有一个美好的未来。

名 教育经历

北京大学 985 211 双一流

生司"。” 硕士 软件与微电子学院

则虽。 类学 211 双一流
底层结构

49.二Redis都有哪些底层数据结构?

Redis 之所以快，除了基于内存读写之外，还有很重要的一点就是它精心设计的底层数据结构。Redis 总共有 8 种
核心的底层数据结构，我按照重要程度来说一下。

多xs Object

redisObject

底层数据结构
long类型整效
cembst编码sds
简单动态字竺束
字典
双滑链表
压缩列表
整教集合
跳紧表和字典

首先是 SDS，这是 Redis 自己实现的动态字符串，它保留了上 语言原生的字符串长度，所以获取长度的时间复杂
度是 o(1) ，在此基础上还支持动态扩容，以及存储二进制数据。

No. 2001261




## 第 201 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

sdshdr

2

0

了TeTETTTT

然后是字典，更底层是用数组+链表实现的哈希表。它的设计很巧妙，用了两个哈希表，平时用第一个，rehash 的
时候用第二个，这样可以渐进式地进行扩容，不会阻塞太久。

No. 2011 261




## 第 202 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

啥希表节点                                      叭项表                                       字典

dict

dt       妈
rpe   hr    tuble “上| dictEntr*团|/   dictEomy |
Pivdata 有 二        二 台  Dll
hr       二

旧
量
|
罗
|
六

cd                                                    世        > null

接下来压缩列表 ziplist，这个设计很有意思。Redis 为了节省内存，设计了这种紧凑型的数据结构，把所有元素连
续存储在一块内存里。但是它有个致命问题叫"连锁更新"，就是当我们修改一个元素的时候，可能会导致后面所有
的元素都要重新编码，性能会急剧下降。

No. 202 1 261




## 第 203 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Zlbytes                              ZIltail                        zllen

Empty Memory or used somewhere else

Zlend

为了解决压缩列表的问题，Redis 后来设计了 quicklist。这个设计思路很聪明，它把 ziplist 拆分成小块，然后用双
向链表把这些小块串起来。这样既保持了 ziplist 节省内存的优势，又避免了连锁更新的问题，因为每个小块的
ziplist 都不会太大。

No. 2031 261




## 第 204 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

再后来，Redis 又设计了 listpack，这个可以说是 ziplist 的完美奉代品。它最大的特点是每个元素只记录自己的长
度，不记录前一个元素的长度，这样就彻底解决了连锁更新的问题。Redis 5.0 已经用 listpack 替换了 ziplist。

listpack实
现结构

总字    有                              listpack元素

跳表skiplist 主要用在 Zset 中。它的设计很巧妙，通过多层指针来实现快速查找，平均时间复杂度是 o(log N) 。
相比红黑树，跳表的实现更简单，而且支持范围查询，这对 Redis 的有序集合来说很重要。

束聊表节点                                                                                                    束跃表

FsaipliseNodd
  0 null
2       站 0 mall
瑟   EapisANodqj >      5
动 二-到十一       四  0 2
0人   FSBisaNod:   再“| onul
隐形2下-有7和2  1中LI2 | 0- aol
| | 五 |” 2 十1  0 null
HR 上一    ES
au | 了    ZN   10
ol    22    3

还有整数集合intset，当 Set 中都是整数且元素数量较少时使用，内部是一个有序数组，查找用的二分法。

No. 2041 261




## 第 205 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

新创建的intset

contents

encoding                    iength

添加13, 5之后:

contents

encoding                         Ilength                     5               13

最后是双向链表LinkedList，早期版本的 Redis 会在 List 中用到，但 Redis 3.2 后就被 quicklist 替代了，因为纯链
表的问题是内存不连续，影响 CPU 缓存性能。

对象机制                             数据类型                                               编码类型                                       底层数据结构
本文要介绍的部分

0B]_ENCODING_RAW

String                                                                                         SDs
(代码t_string.c)                            0B]_ENCODING_INT

List                                0B]_ENCODING_EMBSTR                          ER
(代码t_listc)     ES                                                          (代码Ciedisto)
0B]_ENCODING_QUICKLIST
上文中介绍的对象                                                     二
(代码Lhash.c)                                                                                (代码ziplisto)

0BJ_ENCODING_ZIPLIST

redisObject
                        Set                                                                  HashTable
(代码Lsetc)                      0B]_ENCODING_HT                      (代码dicto)
IntSet
0B]_ENCODING_INTSET               (得meata)
0B]_ENCODING_SKIPLIST                  zskiplist
(Lzsetc中的zskiplist)
(代码tL_stream.c)
要    0B]_ENCODING_STREAM
pdai: 基于v6.0的源码                                                                               Radix Tree of listpack

(listpack.c和rax.c)

memo: 2025 年 6 月 4 日，令天有球友发喜报说拿到了京东零售的实习 offer，并且部门和业务还是挺不错的，
恭喜他! 6 月份还有机会，冲。

No. 2051261




## 第 206 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥，您好，目前我收到了京东的offer

是京东零售一吕扩四 电可-机上 梧部，
想咨询您对这个部门是否有了解

一面面试官说推荐算法后台开发

知生了本富丽
曾二是
0

扰- 可本史二个二和“开本山志本十同国图与六
EL 时有已uir蕊下由 十1a款星
二

外和"及卫导工科交工。全症丰丙蕊术地未
记” 站

简单介绍下链表?

Redis 的 linkedlist 是一个双向无环链表结构，和java 中的 LinkedList 类似。

No. 206 1 261




## 第 207 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

节点由 listNode 表示，每个节点都有指向其前置节点和后置节点的指针，头节点的前置和尾节点的后置均指向

null。

Dull

链表类型
list

listNode

VaTue

listNode
2       一人 null

人free

match

关于整数集合，能再详细说说吗?

整数集合是 Redis 中一个非常精巧的数据结构，当一个 Set 只包含整数元素，并且数量不多时，默认不超过 512

个，Redis 就会用 intset 来存储这些数据。

intset
CC
GZ
engtl
5

contents[

-6370

233 114632

intset 最有意思的地方是类型升级机制。它有三种编码方式: 16位、32位和 64位，会根据存储的整数大小动态调
整。比如原来存的都是小整数，用 16 位编码就够了，但突然插入了一个很大的数，超出了 16 位的范围，这时整
个数组会升级到 32 位编码。

No. 2071 261




## 第 208 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

typedef struct intset {
uint32_t encoding; 。// 编码方式: 16位、32位或64位

uint32 t lengthy    // 元素数量
int8_t contents[]; ，// 保存元素的数组
} intset)

当然了，这种升级是有代价的，因为需要重新分配内存并复制数据，并且是不可逆的，但它的好处是可以节省内存
空间，特别是在存储大量小整数时。

另外，所有元素在数组中按照从小到大的顺序排列，这样就可以使用二分查找来定位元素，时间复杂度为 o(1og

N) 。

说一下zset 的底层原理?
ZSet 是 Redis 最复杂的数据类型，它有两种底层实现方式: 压缩列表和跳表。

|        |

ziplist                                         redis.h/zset

j NA

dict.h/dict           redis.h/zskiplist

当保存的元素数量少于 128 个，且保存的所有元素大小都小于 64 字节时，Redis 会采用压缩列表的编码方式; 否
则就用跳表。

当然，这两个条件都可以通过参数进行调整。

选择压缩列表作为底层实现时，每个元素会使用两个紧挨在一起的节点来保存: 第一个节点保存元素的成员，第二
个节点保存元素的分值。

No. 208 1 261




## 第 209 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

分值最少的元素  分值排第二的元素  分值最大的元素

\   、\           1 N\          “和※ 1/
\   、、        /   \        网人
\成员 、分值   1    \       7    1
人     \      了      了     1
用  用  了  时  了  了
zlbytes | zltail | zllen | "banana'" | 5.0 | "cherry'" 6.0 | "apple" | 8.5 | zlend

图 8-15 有序集合元素在压缩列表中按分值从小到大排列

所有元素按分值从小到大有序排列，小的放在靠近表头的位置，大的放在靠近表尾的位置。
但跳表的缺点是查找只能按顺序进行，时间复杂度为 o(N) ，而且在最坏的情况下，插入和删除操作还可能会引起
连锁更新。

当元素数量较多或元素较大时，Redis 会使用 skiplist 的编码方式;这个设计非常的巧妙，同时使用了两种数据结
构:

typedef struct zset {
zskiplist *zs1;  // 跳跃表
dict *dict)     // 字典
} zset;

跳表按分数有序保存所有元素，且支持范围查询 (如 zRANGE 、 2RANGEBYSCORE ) ，平均时间复杂度为 o(1og
N) 。而哈希表则用来存储成员和分值的映射关系，查找时间复杂度为 o(1) 。

No. 2091 261




## 第 210 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

dictEntry

key | value

Zset
dict

zskiplist

虽然同时使用两种结构，但它们会通过指针来共享相同元素的成员和分值，
你知道为什么Redis 7.0要用listpack来替代ziplist吗?

答: 主要是为了解决压缩列表的一个核心问题一一连锁更新。在压缩列表中，每个节点都需要记录前一个节点的长

度信息。

ZIPLIST_BYTES           ZIPLIST_ENTRY_HEAD

因此不会浪费额外的内存。

ZIPLIST_ENTRY_END

;    ZIPUST_LENGTH           ZIPLIST_TAIL_OFFSET
戏
本杜 zlen: entry
了 :   number                      OxFF
zalbytes | zhtail | zlen | preven | encodng | enty-data  |] en
人   八   人  入            7   )
熙   熙   二       让
4bytes ”4bytes 2 bytes      entry1              1bytes ”所
zltail
熙
zlbytes

No. 210 1 261

ZIPLIST_END_SIZE




## 第 211 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

当插入或删除一个节点时，如果这个操作导致某个节点的长度发生了变化，那么后续的节点可能都需要更新它们存
储的"前一个节点长度"字段。最坏的情况下，一次操作可能触发整个链表的更新，时间复杂度会从 o(1) 退化到
on?) 。

而listpack 的设计理念完全不同。它让每个节点只记录自己的长度信息，不再依赖前一个节点的长度。这样就从根
本上避免了连锁更新的问题。

大小为                                     全浊                                  1
LP_HDR_SIZE                                              上                                                                               人
人
(《                                                       人               1                                                                     A
@@板客时间

listpack 中的节点不再保存其前一个节点的长度，而是保存当前节点的编码类型、数据和长度。

                                                         、

entry-encoding                entry-data                       entry-len
和@@极客时间

连锁更新是怎么发生的?

比如说我们有一个压缩列表，其中有几个节点的长度都是 253 个字节。在 ziplist 的编码中，如果前一个节点的长
度小于 254 字节，我们只需要 1 个字节来存储这个长度信息。

No. 2111 261




## 第 212 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

                                                 entry1         entry2
zlbytes         zltail          zlbytes         zllen        253字节 | 253字节                           zlend
                                              newentry | entry1         entry2
zlbytes           zltail           zlbytes           zllen          512字节 | 257字节 | 253字节             二                zlend

人

prelen 1->5
entry1 253-> 257

zlbytes           zltail           zlbytes           zllen          512字节

newentry | entry1         entry2

257字节 257字节                    zend

但如果在这些节点
字节来存储长度信息。

. java 面试指南 (付费) 收录的字节跳动商业化一面的原题: 说说 Redis 的 zset，什么是跳表，插入一个

NmUmn > ww

memo:

啊，惫

prelen 1->5
entry1 253-> 257             cspwehenoJety

那么原来只需要 1 个字节存储长度的节点现在需要 5 个
这就会导致后续所有节点的长度信息都需要更新。

节点要构建几层索引

java 面试指南(付费) 收录的字节跳动面经同学 9 飞书后端技术一面面试原题: Redis 的数据类型，
ZSet 的实现

java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你知道 Redis 的 zset 底层实现吗

Java 面试指南 (付费) 收录的腾讯面经同学 23 QQ 后台技术一面面试原题: zset 的底层原理

Java 面试指南 (付费) 收录的快手面经同学 7 java 后端技术一面面试原题: 说一下 ZSet 底层结构

java 面试指南 (付费) 收录的美团同学 9 一面面试原题: redis的数据结构底层原理?

java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题;: Zset的底层实现?

java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: Zset的底层如何实现?

2025年6月 5 日， 今天有球友在VIP群里咨询 offer 的选择，一个拼多多，一个快手，真让人羡慕的要死

No. 212 1 261




## 第 213 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥VIP10群 (442) (                              se
名- 沉默王二-二哥: 面渣逆袭MyS.…     共2条

中 国

于

快手陡介”候部，有类似于钉钉的学习平台，表
格啥的。北京
拼多多 中mu 类似于菜鸟，上海

有中国
” 拼多多TH
快手19E 扎 5
有  ba
” 该怎么取舍
E

|
50.Redis 为什么不用 C 语言的原生字符串?

第一，(C 语言的字符串其实就是字符数组，以\0 结尾，这意味着如果数据本身包含 \0 字节，就会被误认为字符
串结束。但 Redis 需要存储各种类型的数据，包括图片、序列化对象等二进制数据，这些数据中很可能包含 \0 。

No. 2131261




## 第 214 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

C语言字符串

| char# S 二 “Hel1lo所  |

第二，如果需要获取字符串长度，C 语言只能调用 strlen() 函数，时间复杂度是 o(N) ，因为要遍历整个字符串
直到遇到 \o 。

第三，(C 语言的字符串不会自动检查边界，如果往一个字符数组里写入超过其容量的数据，就会出现缓冲区溢出。
第四，'( 语言的字符串不支持动态扩容，如果需要修改内容，就必须重新分配内存并复制数据，开销很大。

sdqshdr

FToTaoTTOTIO

Redis 设计的 SDS 完美解决了这些问题，获取长度可以直接通过 len 字段，时间复杂度为 0(1) ; free 字段会
记录剩余空间，因此 Redis 可以根据预分配策略动态扩容，不用在追加数据时重新分配内存; 并且不依赖于 \0 结
尾，可以存储任意二进制数据。

struct sds {

int leni       // 字符串长度
int freei      // 剩余空间
char buf[]7     // 字符数组

)}

51.你研究过 Redis 的字典源码吗?

是的，有研究过。Redis 的字典分为三层，最外层是一个 dict 结构，包含两个哈希表 ht[0] 和 ht[1] ，用于存储
键值对。每个哈希表由一个数组和链表组成，数组用于快速定位，链表用于解决哈希冲突。

No. 2141 261




## 第 215 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

弛
dict                       dictht“
be                        able                             dictEnty*几| nal | dictEnery

Privdata          |         Se                                      0          1           四        可

加

1
TDashids               Sizcmask                     8了殉一
YY                                               了

|                        史                                            |一 deiEnm              dictEnery

5                         ET       证己[        null
hrfl      2

链地址法解决冲突

dicthr

rable
Size
东
Sizemask
了4

uscd
2

// 最外层的字典结构
typedef struct dict {

dictht ht[2]7      // 两个哈希表! 这是关键
long rehashidxy7    // rehash索引，-1表示没有进行rehash
/]]/

} dict;

// 哈希表结构

typedef struct dictht {
dictEntry *xtable;  // 哈希表数组
unsigned long size; // 哈希表大小
unsigned long sizemask; // 哈希表大小掩码，用于计算索引值
unsigned long used; // 该哈希表已有节点的数量

} dictht)

// 哈希表节点

typedef struct dictEntry {
void *key7            // 键
vi               // 值

struct dictEntry *next; // 指向下个哈希表节点，形成链表
} dictEntry)

字典最核心的特点是渐进式 rehash，这是我觉得最精彩的部分。传统的哈希表扩容都是一次性完成的，但 Redis
不是这样的。

当负载因子触发 rehash 条件时，Redis 会为哈希表1 分配新的空间，通常是哈希表 0 的两倍大小，然后将
rehashidx 设置为 0。

接下来的关键是，Redis 不会一次性把所有数据从哈希表0 迁移到哈希表1，而是每次操作字典时，顺便迁移哈希表
0 中 rehashidx 位置上的所有键值对。迁移完一个模位后，rehashidx 递增，直到整个哈希表0 迁移完毕。

No. 2151 261




## 第 216 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

AutL
NutL
Er
到村                                    要四]
(bucket)                                         0         ，
0                  NuuL                          和
                                              人一
   -cm                          全 _，
NULL
-本
AutL
utL
En
dictEntryyy       NULL                              eaal                四
pucket) [一                           2
5                                           1         AutL
NULL                                2   |
工                              rehash中
2   上一一                                  3
rehash前        上        NULL                                加   NS         NULL
1
日   aa                                  6
机                                           了
7

NULL
dictEntryey
ctEn
(bucket)
0        /一 NULL

rehash后

字典重新分配后

这种设计的巧妙之处在于把 rehash 的开销分摊到了每次操作中。假设有一个几百万键的哈希表，如果一次性
rehash 可能需要几百毫秒，这对单线程的 Redis 来说是灾难性的。但通过渐进式 rehash，每次操作只增加很少的
额外开销，用户基本感觉不到延迟。

在 rehash 期间，查找操作会先查 哈希表 0，没找到再查哈希表 1; 但是新插入的数据只会放到哈希表 1 中。这样
既可以保证数据的完整性，又能避免数据的重复。

遇到哈希冲突怎么办?

Redis 是通过链地址法来解决哈希冲突的，每个哈希表的槽位实际上是一个链表的头指针，当多个键的哈希值映射
到同一个槽位时，这些键会以链表的形式串联起来。

No. 216 1 261




## 第 217 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

NULL

具体实现上，Redis 会通过哈希表节点的 next 指针，指向下一个具有相同哈希值的节点。当发生冲突时，新的键
值对会插入到链表的头部，时间复杂度是 o(1) 。查找时需要人遍历整个链表，最坏的情况下时间复杂度为 on) ，
但通常链表都比较短。

另外，Redis 设计的哈希函数在分布上也比较均匀，人能够有效减少哈希冲突的发生。

/* MurmurHash2，by Rustin Rppleby

* Note - This code makes a few assumptions about how your machine behaves -
* 1。We can read a 4-byte value from any address without crashing

* 2。sizeof(int) ==

* Rnd it has a few limitations -

* 1。It will not work incrementally。
* 2。 It will not produce the same results on little-endian and big-endian
* machines .

unsigned int dictGenHashFunction(const void *key，int len) {

/x 'm' and 'r， are mixing constants generated offline-

They're not really 'magic'，they just happen to work well. */
uint32 t seed = dict_hash function_seed)
const uint32 t 御 = 0x5bdle995)

const int = 247

/* Initialize the hash to a 'random' value */
uint32 t h = seed ^ leni

/x* Mix 4 bytes at a time into the hash */
const unsigned char *data = (const unsigned char *)key)

while(len >= 4) {
uint32 七 k = *(uint32_ tx)datay

Kx mi
k “= k >> ri
Kx mi

No. 217 1 261




## 第 218 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

h x= my
h “= kr

data += 47
len -= 4;

】}

/* Handle the last few bytes of the input array */

switch(len) {

case 3: h “= data[2] << 167

case 2: h ^= data[1] << 8;

case 1: h “= data[0]) h *= mi

了

/* Do a few final mixes of the hash to ensure the last few
* bytes are well-incorporated。*/

h “= h >> 13;

h *= my

h “= h >> 15)

return (unsigned int)hy

)}

memo: 2025 年6月6 日， 今天有球友咨询去金山办公里期实习，要提前学点什么”又一个凭借java 这个载体拿
到 Go offer 的球友，说明大家在求职 Go 岗的时候，也不用说非要提前刻意去学习 Go，当然有一些基础是最好
的，我之前也整理过 Go 的学习路线在 Java 进阶之路上。

暑假实习是去金山办公进行go的服务端开发，go语言的学习需要学习云
原生吗

还是 go 服务端开发和云原生结合比较紧密，需要都学。

好的，谢谢二哥

我的提问帖子里面有，谢谢二哥

分

<
D

一般会有关联，你去了之后体验一下

No. 218 1 261




## 第 219 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

52.过你了解跳表吗?

跳表是一种非常巧妙的数据结构，它在有序链表的基础上建立了多层索引，最底层包含所有数据，每往上一层，节
点数量就减少一半。

中二云手量志

它的核心思想是"用空间换时间"，通过多层索引来跳过大量节点，从而提高查找效率。
skiblistNodd
132    0一null

NG 一一人人人 0 null

5                  Eapiswodg 一一                         L5

本|-了 有AS  可| oaul
要

skipblistNodd                    L3              0全 null
2

有
5
zskiblist            忌   | -|   1   |王1-计   LL     1-计   L2    人全 null
二:    上中    1让    0 null
”一  BY        HV_ 上|， 取
null                  12.0

o2

怎么往跳表插入节点呢?

No. 2191 261




## 第 220 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

首先是找到插入位置，从最高层的头节点开始，在每一层都找到应该插入位置的前驱节点，用一个 update 数组把
这些前驱节点记录下来。这个查找过程和普通查找一样，在每层向右移动直到下个节点的值大于要插入的值，然后
下降到下一层。

// 记录每层的插入位置
zskiplistNode *update[ZSKIPLIST_MRAXLEVEL])

zskiplistNode *xi
int i，1level;

// 从最高层开始查找
x = zs1->header1i
for (i = zs1->level-1l; 1 >= 0;) i--) {
// 在当前层水平移动，找到插入位置
while (x->level[i].forward &&
(x->level[i].forward->score < score ||
(x->lLevel[i].forward->score == Score &&
sdscmp(x->level[i]l.forward->ele，ele) < 0)))

x = x->level[i].forwardi

】}
update[i] = xi  // 记录每层的前驱节点

续往上，直到随机失败或达到最大层数限

接下来随机生成新节点的层数。通常用一个循环，每次有 50% 的概率
制。

// Redis 中的随机层数生成
int zslRandomLevel(void) {
int level = 1)
while ((zandom( )&0xFFFF) < (2SKIPLIST _P * 0xFFFEF))
level += 17
return (1]evel < 2SKIPLIST_MRAXLEVEL) ? level : 2SKIPLIST_MRAXLEVEL 7

)}

// 生成新节点的层数

level = zslRandomLevel() 1

创建新节点后，从底层开始到新节点的最高层，在每一层都进行标准的链表插入操作。这一步要利用之前记录的
update 数组，将新节点插入到正确位置，然后更新前后指针的连接关系。

// 更新前进指针

for (1 = 0;) < level; i++) {
x->level[i].forward = update[i]->level[i].forward)
update[i]->level[i].forward = xi

// 更新跨度信息

x->level[i]l.span = update[i]->level[i]l.span - (rank[0] - rank[i])7

update[i]->level[il.span = (rank[0] - rank[il) + 17

No. 2201 261




## 第 221 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 更新未涉及层的跨度
for (i = level; 1 < zsl->level; i++) {

update[i]->level[il].span++17

// 更新后退指针
x->backwarad = (update[0] == zs1->header) ? NULL : update[0]17
if (x->level[0].forward)
x->level[0].forward->backwarad = xi
else
zs1->tail = xj

// 更新跳表长度

zs1->Length++1

我们来模拟一个跳表的插入过程，假设插入的数据依次是 22、19、7、3、37、11、26。

No. 2211 261




## 第 222 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

msas 国-国
&交，国--国国-国

插入19，
随机层数=2

目夫 画书
=四言志

随机层数=4

插入3，
随机层数=1

插入37，
随机层数=3

插入11，       上          才 -
随机层数=1            四
器己    也加    区[3
和    虹             只 -
随机层数=1
回忆    回忆 E 区四一区四

那假如我们在一个已经分布了 1、14、27、31、44、56、63、70、80、91 的跳表中插入一个 67 的节点，插入过
程是这样的:

No. 222 / 261




## 第 223 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Inserting 67

Insert here

zset为什么要使用跳表呢?
第一，跳表天然就是有序的数据结构，查找、插入和删除都能保持 o(1og n) 的时间复杂度。

第二，跳表支持范围查询，找到起始位置后可以直接沿着底层链表顺序遍历，满足 ZRANGE 按排名获取元素，或
者 ZRANGEBYSCORE 按分值范围获取元素。

memo: 2025 年 6月7 日，今天给一个学院本球友修改简历的时候，他提到实习的同事，都拿到了 20k 以上的
offer，甚至还有 25k 携程 offer 的，自己并不比他们差，问在实习、项目和能力上还能怎么提高?

6 .目标规划: 二哥，比较真是偷走幸福的小偷，原本没毕业我觉得能有个月薪过万就够了，但是我看上段实习的25届同事 《学院本，双非) 都拿了20k
以上的offer。我觉得我不比他们差 实习，项目，能力) 什么的，但是也只是我自己主观觉得吧，他们可能有盔多更历害的地方，就也想我怎么也要
20k吧，他们俩个都是秋招时间段九月份的样子和我在上个地方实习，然后秋招就签了十几k的offer，但是春招，比如一个拿了水滴17k转手又签了携程

的25k，那我要不要也按这种，先秋招尽可能努力冲一个保底offer，春招再去努力拉高一下上限，合理吗。现实真的能这么好找工作吗，还是能找到个
工作就不错了。

我想说的是，这就是为什么很多人选择跑来卷互联网开发的原因啊，上线比其他行业高太多了，虽然互联网开发的
工作强度也大，但最起码能劳有所获。

跳表是如何定义的呢?

跳表本质上是一个多层链表，底层是一个包含所有元素的有序链表，上一层作为索引层，包含了下一层的部分节
点; 层数通过随机算法确定，理论上可以无限高。

No. 2231 261




## 第 224 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

zskiplist
header                                ai

加
Ilevel1T

避

ia                                aaRa
level[2]                                 本

四
Ievelt                        ZipIEINode
On

levelol

全

RISINGdE
四                                    包
ZiplistNode                       ZSIPISINode           SPIRINode
中             |          咱              |         [
S              可               本             二

跳表节点包含分值 score、成员对象 obj、一个后退指针 backward，以及一个层级数组 level。每个层级包含
forward 前进指针和 span 跨度信息。

四
头结点
NuuL

typedef struct skiplistNode {
double scorey                 // 分值 (用于排序)
robj *obj;                 // 数据对象
struct skiplistNode *backward; ，// 后退指针
struct skiplistLevel {

struct skiplistNode *forward; // 前进指针

unsigned int span7         // 跨度 (到下个节点的距离)
} level[];                // 层级数组
} skiplistNode;

跳表本身包含头尾节点指针、节点总数 length 和当前最大层数 level。

typedef struct skiplist {
struct skiplistNode *header，x*tail; // 头尾节点
unsigned long length7            // 节点数量

int level7                    // 最大层数
} skiplisti

span 跨度有什么用?

span 记录了当前节点到下一节点之间，底层到底跨越了几个节点，它的主要作用是快速找到 Zset 中某个分值的排
名。

No. 2241 261




## 第 225 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

Level2                                                                                                                  |
RankI                                                                                                         Ramw6 |
Span5                                                                                                            - span0
了
Level1        5                                                                                                        >|
RankI                                     Rank3                                                             Raw6|
”Span 2                                      Span 3                                                             - Span0

Lvel0          5                 :|     8           | 12                 -|           | 18    |           下    20
Rankl            Rank2             Rank3               Rank4             RankS                RanK6
Span1               Span1                 Span1                Span1                Span1                  Span0

比如说我们执行 zRANK 命令时，如果没有 span，就需要从头节点开始遍历每个节点，直到找到目标分值，这样时
间复杂度是 oln) 。

/ 没有span的排名查询 - oO(n)
int getRankWithoutSpan(skiplist *zs1，double score，zrobj *obj) {
skiplistNode xx = zs1->header->level[0].forwardi

int rank = 07

while (x) {
if (x->score == Score && equalStringobjects(x->obj，obj)) {
return rank + 1;  // 排名从1开始
}

工ank+二7
x = x->level[0].forwardi

】}

return 07

但有了 span，我们在从高层往低层搜索的时候，可以直接跳过一些节点，快速定位到目标分值所在的范围。这样
就能把时间复杂度降到 o(log n) 。

long skiplistGetRank(skiplist *zs1，double score，robj *obj) {
skiplistNode *x = zs1->header)
unsigned long rank = 0)

// 从最高层开始查找

for (int 1 = zsl->level - 1; 1 >= 0);

-)
while (x->level[i].forward &&
{(x->level[i]l.forward->score < score ||
(X->level[i]l.forward->score == Score &&
compareStringobjects(x->level[i].forward->obj，obj) < 0))) {

rank += x->level[i].span;  // 累加跨度

x = x->level[i].forwardi

// 找到目标节点
ifE (x->level[i]l.forward &&
X->1levVel[i]l.forward->score == Score &&

No. 225 1 261




## 第 226 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

equalStringObjects(x->level[i].forward->obj，obj)) {
rank += x->level[i].-span)

return rank

】}

return 07

)}

为什么跳表的范围查询效率比字典高?

字典是通过哈希函数将键值对分散存储的，元素在内存中是无序分布的，没有任何顺序关系。而跳表本身就是有序
的数据结构，所有元素按照分值从小到大排列。

按照score值升序排列存储              少

L2                                                                                                    null

     RE                   一 计          LT
2                                           ]        5

LO    |       说 工               刘                                   襄 4       |     |                演 nu

当需要进行范围查询时，字典必须遍历所有元素，逐个检查每个元素是否在指定范围内，时间复杂度是 on) 。比
如要找分值在 60 到 80 之间的所有元素，字典只能把整个哈希表扫描一遍，因为它无法知道符合条件的元素在哪

里。

而跳表的范围查询就高效多了。首先用 o(1og n) 时间找到范围的起始位置，然后沿着底层的有序链表顺序饥
历，直到超出范围为止。总时间复杂度是 o(1og n + k) ，其中k 是结果集的大小。这种效率差异在数据量大的

时候非常明显。

No. 226 1 261




## 第 227 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二-内
E               二 -内
    号          se | -wu
    E    天    sa 二 -mu
辐    5    |
本      区      区      E
下    3    JS    SS
     是     四
| 一
3         了                  ER    3    二
互
ojer    到    4
|os) EcoDIG_sSkIPusr|   了    岂
1     三
总                              | | Te] |
加
[下     EL             my     9     9
去     ET       <     赤     去
袜     =        国     3    3
             |    上= |
工   NUUL          mt
两     9     ;
总
下     3     :
se |m
均
和
人
二
总
和

这也是为什么 Redis 的 zset 要用跳表而不是纯哈希表的重要原因，因为 zset 经常需要 ZRANGE、
ZRANGEBYSCORE 这类范围操作。实际上 Redis 的 zset 是跳表和哈希表的组合: 跳表保证有序性支持范围查询，
哈希表保证 o(1) 的单点查找效率，两者互补。

1. java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 为什么 hash 表范围查询效率比跳表
低

2. java 面试指南 (付费) 收录的得物面经同学 8 一面面试原题: 跳表的结构
3. Java 面试指南 (付费) 收录的美团面经同学 4 一面面试原题: Redis 跳表
4. java 面试指南 (付费) 收录的阿里系面经同学 19 饿了么面试原题: 跳表了解吗

memo: 2025年6月 8 日，今天有球友发信息称赞Java 进阶之路的内容写得好，说实话，我是有这个自信的，基
本上所写的内容也都是我这些年从读到的所有书籍、视频、教程中提炼到的精华，把一些难懂隐涩的知识都用通俗
易懂的语言表达出来，配合手绘图，能让人更容易理解。

No. 2271 261




## 第 228 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

二哥，我感觉你这些知识点写的真不错，图之前
我看java基础那本书里的泛型介绍，差点没给我
看入土了

15:24

[SEE cb

都是精华

53.压缩列表了解吗?

答: 压缩列表是 Redis 为了节省内存而设计的一种紧凑型数据结构，它会把所有数据连续存储在一块内存当中。
整个结构包含头部信息，如总的字节数、尾部偏移量、节点数量，以及连续的节点数据。

[abwees  zlmail  zlen | sentvl  ent | EN  Zad

当list、hash 和 set 的数据量较小且值都不大时，底层会使用压缩列表来实现。

Configuration options for ziplist representation of different structures

。 list-max-ziplist-entries: 512

。 list-max-ziplist-value: 64
(Limits for ziplist usage with LISTs)

。 hash-max-ziplist-entries: 512

。 ”hash-max-ziplist-value: 64
(Limits for ziplist usage with HASHes; previous versions of Redis used different names and encodings forthis)

。 zset-max-ziplist-entries: 428

。 zset-max-ziplist-value: 64
(Limits for ziplist usage with ZSETSs]

通常情况在，每个节点包含三个部分: 前一个节点的长度、编码类型和实际的数据。

No. 228 1/ 261




## 第 229 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

entry                                                                                        entry
上
T
prevlen             encoding            entry-data             prevlen             encoding            entry-data
|
人                                                            J
T

前一个节点的长度是为了支持从后往前遍历;当前一个节点的长度小于 254 字节时，使用 1 字节存储; 否则用 5
字节存储，第一个字节设置为 254，后四个字节存储实际长度。

entry       1byte
人
|
prevlen   encoding   entry-data prevlen  encoding   entry-data
|
生               有
T
entry       1byte   4bytes
人
|一一r            1
prevlen   encoding   entry-data 加  | prevlen     encoding   entry-data
人              )
T
编码类型会根据数据的实际情况选择最紧凑的存储方式。
Bytes  FT | IE VGN  ZN  ZU  ZE
0x350    0s3c   0x3    0    22    2   0OxFF
]
了                       P+60

No. 229 1 261




## 第 230 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

但压缩列表有个致命问题，就是连锁更新。当插入或删除节点导致某个节点长度发生变化时，可能会影响后续所有
节点存储的“前一个节点长度"字段，最坏情况下时间复杂度会退化到 onz) 。

假设每个长度都等于253字节
假设每个长度都等于253字节
人
新插入的节点长度大于等于254 字节
假设每个长度都等于253字节

新插入的节点长度大于等于254 字节

节点1的 prevlen 只有一个字节，不够存储前面新增大于等于 254 字
节的新节点。

所以要对节点 1 的 prevlen 进行扩展为 5 字节，扩展后节点 1 超过了
254 字节。所以又要对节点 2 进行扩展。

一直扩展到最后一个节点 n。

假设每个长度都等于253字节
人

直至扩展到节点 n 结束，这就是连锁更新。

No. 2301 261




## 第 231 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

ziplist 的节点数量会超过 65535 吗?
不会

zllen 字段的类型是 uint16_t ，最大值为 65535，也就是 2 的 16次方，所以压缩列表的节点数量不会超过
65535。

当节点数量小于 65535 时，该字段会存储实际的数量; 否则该字段就固定为 65535，实际存储的数量需要逐个遍
历节点来计算。

ziplist 的编码类型了解多少?

ziplist 的编码类型设计得很精巧，主要分为字符串编码和整数编码两大类，目的是用最少的字节存储数据。
比如 0 到 12 这些小整数直接编码在 type 字段中，只需要 1 个字节。

编码                     长度             描述

11000000            1字节          int16 t类型整数，2 字节

11010000             1字节          int32_t类型整数，4 字节

11100000            1字节          int64 t类型整数，8 字节

11110000           1字节         24位有符号整数 ，3 字节

1111xxXxxX                   1字节               数据范围在[0-12]，数据包含在编码中

No. 2311 261




## 第 232 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

对于字符串编码，根据字符串长度有三种格式。长度小于 63 字节的用 00 开头的单字节编码，剩余 6 位存储长
度。长度在 63 到 16383 之间的用 01 开头的双字节编码，剩余 14 位存储长度。超过 16383 字节的用 10 开头，
后面跟 4 字节存储长度。

编码                                                         长度          描述

00pppppp                                                  1字节        0-63 字节的字符串

01pppppp qqqqqqqq                                     2字节        64-16383字节的字符串

10_ qqqqqqqq rrrrrrrr ssssssss tttttttt                   5字节          16384-4294967295字节的字符串

No. 232 1 261




## 第 233 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

1blt      人

oo| so           Entry data

o|;                                                             enty-data

5byte
由

1bit                 未用                                                   大喘序                                                                        ]E末

和

entry data

上国国国因国国盾            azbtien

-一
encoding

1. Java 面试指南 (付费) 收录的同学 30 腾讯音乐面试原题: 什么情况下使用压缩列表

memo: 2025年6月9 日修改至此，今天有球友特意发私信，感谢面渣逆袭对他的帮助。对，这么棒的内容，我
依然选择了免费，因为我相信知识是有价值的，只有诚恳的分享出来才能让更多人受益。

No. 2331 261




## 第 234 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

将 分享星球

|     之前是通过您编写的面试题了解到您的

你的面试题写的真的很棒，这么棒的内容居然还
是免费的

顺 assw
辆光一z二榴*生

国遇”日前忆经大=了
54.quicklist 了解吗?

No. 2341 261




## 第 235 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

quicklist 是 Redis 在 3.2 版本时引入的，专门用于 List 的底层实现，它实际上是一个混合型数据结构，结合了压缩

列表和双向链表的优点。
2     | quickistNode         quickIstNode         duickistNode
YIVX 和 22移               殉2                  到到踊           al
0                 7            区            AZ

encoding

encoding

T

旨

combress

在早期的版本中，List 会根据元素的数量和大小采用两种不同的底层数据结构，当元素较少或者较小时，会使用压

缩列表; 否则用双向链表。

但这种设计有个问题，就是当 List 中的元素数量较多时，压缩列表会因为连锁更新导致性能下降，而双向链表又会

占用更多内存。

quicklist 通过将 List 拆分为多个小的 ziplist，再通过指针链接成一个双向链表，巧妙的解决了这个问题。

head

quicklistNode

quicklist                tail

quicklistNode

quicklistNode        duicklistNode

默认情况下，每个 ziplist 可以存储 8KB 的数据，假如每个元素的大小恰好是 1KB，那么一个 quicklist 就可以存储
8 个元素。80 个这样的元素就会被分成 10 个 ziplist。

这样既保留了压缩列表的内存紧凑性，又减少了双向链表指针的数量，进一步降低了内存开销。

No. 2351 261




## 第 236 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

iuicklist

除此之外，quicklist 还有一个重要的特性，就是它的可配置性，可以通过填充因子控制每个 ziplist 节点的大小。
当填充因子为正数时，它还可以限制每个 ziplist 最多包含的元素数量。

# 填充因子，默认 -2 (8KB)

list-max-ziplist-size 10

如果想进一步节省内存，quicklist 还支持对中间节点进行 LZF 压缩，压缩深度为 1 时，表示除了首尾各 1 个节点
不压缩外，其他节点都压缩。

## 压缩深度，默认 0 (不压缩)

1ist-compress-depth 1

No. 2361 261




## 第 237 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

QUICKLIST STRUCT

Bbeihai

QuicktList    xhead    #tailL    count     1Len      fiLL compress

TIE     QuickListNode     QuickListNode     TIE

xprevV                      prevV                      xprev                      xprevV

xnext         |         炎neXt        疡|         xneXxt         |户         xneXxt         庆

大ZL                              大ZL
T                                   T
1                                   1
1                                   1
1                                   1
由                      由
LZF                          LZF
ZLbytes                           SZ                                SZ                           ZLbytes
ZLtailL                  compressed[]             compressed[]                  ZLtaitL
ZLLen                                                                                    zLLen
entry                                                                                                  entry
entry                                                                                                  entry
ZLend                                                                                                  ZLend

LZF 压缩算法了解吗?

LZF 是一种快速的无损压缩算法，主要用于减少数据存储空间。它的核心思想是通过查找重复数据来实现压缩，通
一个滑动窗口来查找重复的字节序列，并将这些序列替换为更短的引用。

输入数据: "hello world hello redis"

步骤1: 处理 "hello world "
- 建立字典，记录字节序列位置

步骤2 : 遇到重复的“hello"
- 在字典中找到之前的“hello” 位置
- 用 (距离，长度) 对替换: (12，5)

输出: "hello world "+ (12,5) + ”redis"

memo: 2025 年 6 月 10 日，今天有球友发信息说找我修改了简历后，又按照星球的学习资料好好学了一下之
后，拿到了字节跳动的 offer，并特意发了一个大红包来感谢。这种被认可被需要的感觉，真好!

No. 2371 261




## 第 238 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

= 二哥，我是之前发邮件请您修改简
历的让下环节的同学，我
按照星球里的资料好好修改学习了
一下之后最近也是收到字节跳动的
实习offer了，非常感谢二哥邮件
里真诚的建议，祝二哥的知识星球
以后越办越好，太感谢了!

No. 238 1 261




## 第 239 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

补充

55.假如 Redis 里面有 1 亿个 key，其中有 10w 个 key 是以某个固定的已
知的前缀开头的，如何将它们全部找出来?

我会使用 SCAN 命令配合 MATCH 参数来解决。

比如要找以 user: 开头的 key，可以执行 scaN 0 MATcH user:* COUNT 1000 。

SCAN 的优势在于它是基于游标的增量和迭代，每次只返回一小批结果，不会阻塞服务器。可以从游标 0 开始，每次
处理返回的 key 列表，然后用返回的下一个游标继续扫描，直到游标回到 0 表示扫描完成。

使用 Spring Data Redis 的代码示例:

eservice
public class RedisKeyService 1{

Rutowired
Private RedisTemplate<String，Object> redisTemplate

public List<String> scanKeysBYPrefix(String Prefix，int batchSsize) {
List<String> keys = new RrrayList<>() 7

Scan0ptions options = Scan0ptions.scanOptions()
.match(prefix + "*")
.count (batchSize)
.build() 7

try (Cursor<String> cursor = redisTemplate.scan(options)) {
while (cursor.hasNext()) {
keys.add(cursor.next()) 7
}
}

return keys1

千万不要用 KEYS 命令，因为 KEYS 会阻塞 Redis 服务器直到人遍历完所有 key，在生产环境中对 1 亿个 key 执行
KEYS 是非常危险的。

memo: 2025年6月11 日修改至此，今天有读者留言说，找实习的时候背了一个月的面渣逆代，然后快手和美
团都拿到 offer 了。能帮助到大家，也是我做技术博主最开心的一件事情了，也感谢读者给的口碑。

No. 2391 261




## 第 240 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

各  Epiphany                   内 … 让
”前几个月找实习的时候背了一个月的面渣，快手美团都
offer了，感谢二哥免费优质的资源

妃 沉默王二 作者                            四
恭喜洲'啊

56.Redis在秒杀场景下可以扮演什么角色?

秒杀是一种非常特殊的业务场景，它的特点是在极短时间内会有大量用户涌入系统，对系统的并发处理能力、响应
速度和数据一致性都提出了极高的要求。在这种场景下，Redis 作为一种高性能的内存数据库，能够发挥多方面的
关键作用。

比如说在秒杀开始前，我们可以将商品信息、库存数据等预先加载到 Redis 中，这样大量的用户读请求就可以直接
从 Redis 中获取响应，而不必每次都去访问数据库，这样就能大大减轻数据库的访问压力。

秒杀页面

CDN

强制刷新
静态Cache数据

静态数据回源

读数据    多种条件校验

| aa

需库存                                                                 秒杀答题提交

商品、库存系统

        秒杀交易系统集群

减库存                                               支付

其次，Redis 在库存控制方面具有得天独厚的优势。秒杀最核心的问题之一就是容易发生超卖。Redis 提供的原子
操作如 DECR、DECRBY 等命令，可以确保在高并发环境下库存计数的准确性。

No. 2401261




## 第 241 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

库存扣减入品
                                 一 4处理弹
防止超卖检验 | 写Redis     库存数量      | 一
Redis集群      |
En                |
            io       |
落任务库          | | 天一
         在和诛 (合吉库分和
|合页|] |使到| [使丙||
生                         ES
写数据成功                        业务库N

抗写 : Redis抗写+状态机异步写库 ( 支持数十万每秒高并发 )

更复杂的逻辑，可以通过 Lua 脚本来实现，因为 Lua 脚本在 Redis 中是原子执行的，所以可以包含复杂的判断和
操作逻辑，比如先检查库存是否充足，再进行扣减，这整个过程是不会被其他操作打断的。

第三点，Redis 的分布式锁可以确保多个用户同时抢购同一件商品时的操作是互扩的，保证数据一致性的同时，还
可以用来防止用户重复下单。

No. 2411 261




## 第 242 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

加过期时间

第四点，限流削峰。秒杀开始的瞬间，可能会有成千上万的请求同时到达，如果不加控制，很容易导致系统崩溃。
Redis 可以实现多种限流算法，比如简单的计数器限流、令牌桶或漏桶算法等。

No. 242 1 261




## 第 243 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

仿牌桶限流

来到的请求        而 按照每1/r秒的速度向桶中存放1令牌
重生                            继续发送
全人
TELL (人 -二* 便便|作|
合作
全人     拦夫器
一-一生瑚甸
存储量为b的令牌桶
合作| 捷齐
全全全
通过限流算法我们可以控制单位时间内系统能够处理的请求数量，超出部分可以排队或者直接拒绝，从而保护系统
的稳定运行。

memo: 2025年6月12 日修改至此，今天有球友发信息说，大二就拿下了美团的实习 offer，特意发来感谢，说

我的付出对他有着巨大的帮助，真的很感动，每一个懂得感恩的球友，你们也是我坚持下去的最强动力。

No. 2431261




## 第 244 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

|   首先谢谢二哥! 现在大二拿下美团 offer我从来没
想到过 在这里我非常郑重地感谢二哥您! 根据您
的面经我以他为框架 再自己额外扩展了一些 在每
次面试里面我都是信心十足! 您的面经对我的帮
助是无与伦比的! 感谢二哥的辛勤付出以及无形
之中对我的巨大帮助! 这种帮助只有自己经历的
才能明白! 最后再郑重的向您说一句感谢!! 痊
久久

圳   我会永远铭记在心!1

2
Redis具体如何实现削峰呢?

削峰的本质是将瞬时的高流量请求缓冲起来，通过排队、限流等机制，使系统以一个可承受的速度来处理请求。

那第一步就是缓存预热。在秒杀活动开始前，先把商品信息这些热点数据提前加载到 Redis 中。这样用户访问商品
页面时，可以直接从 Redis 读取，数据库基本上不会有压力。

本四                        数据库
这里查到数据就直接返回，
没查到就去访问数据库~
CSDN @陈亦康

No. 244 1 261




## 第 245 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

第二步是引入消息队列，特别是下单这种写操作，不能让用户等太久，但后端处理订单、扣库存这些操作又比较
重。所以可以用 Redis 的 List 做了个队列，或者直接用 RocketMQ 这种标准的消息中间件，用户下单后立即返

回"订单提交成功"，然后把订单数据丢到队列里，后台服务慢慢消费。这样既保证了用户体验，又避免了系统被瞬
时写请求压垮。

国园国国国 。 消息服务队列

Service B

国

第三步，可以在秒杀活动中加入答题环节，只有答对题目的用户才能参与秒杀活动，这样可以最大程度减少无效请

求。
创建订单                                支付订单
交易系统          支付系统
库存校验

库存缓存

一个比较完整的秒杀削峰处理方案:

aeService

public class SeckillServiceImpl implements SeckillService {

8RAutowired

Private RedisTemplate<String，String> redisTemplatei

8RAutowired

Private OrderService orderServicey

8RAutowired

No. 2451 261




## 第 246 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

Private CommodityService commodityServicey

As
* 秒杀请求入口
/
public Result seckil1(Long userId，Long commodityId) {
// 1。 用户请求频率限制
if (!countRateLimit("user:" + userId，5，60)) {
return Result .error("请求过于频繁" ) ;

// 2. 商品是否在秒杀时间内
if (!isInSeckillTime(commodityId)) {
return Result.error("秒杀未开始或已结束" ) ;

// 3。 是否还有库存(快速失败)
String stockKey = "seckil1:stock:"” + commodityId7;
Integer stock = Integer.valueOf(redisTemplate.opsForValue() .get(stockKey)) 1
if (stock != null && stock <= 0) {
return Result .error("商品已售志" ) ;

// 4. 全局限流
if (lacquireToken("global"，1000，100)) {
// 系统负载过高，将请求放入队列延迟处理

enqueueDelayedRequest(userId，commodityId);
return Result.success( "秒杀请求已受理，排队处理中" ) ;

// 5. 检查用户是否已购买
if (hasUserBought(userId，commodityId)) {
return Result.error("您已经购买过该商品" ) ;

// 6. 将请求放入队列，返回排队状态
String requestId = generateRequestId(userId，commodityId);

enqueueRequest(userId，commodityId，requestId) 1;

zeturn Result.success( "秒杀请求已提交，请等待结果" ，requestId) ;

As
异步处理秒杀请
/
escheduled(fixedRate = 50) // 每50ms处理一批
public void processSeckilloueue() {
String queueKey = "seckill:queue'

// 批量处理，控制处理速度
for (int = 0) < 10;) i++) 1{
String requestJson = redisTemplate.opsForList() .leftPop(queueKkey);

No. 2461261




## 第 247 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

if (requestJson == nul1) {
breaky

Seckil1Request request = JSON.parseObject(requestJson，SeckillRequest.class);
try 1{
// 执行秒杀核心膛辑
boolean success = doSeckill(request.getUserId()，
request .getCommodityId( ) ) 7

// 更新请求状态，便于用户查询

String statusKey = "seckill:status:”+ request.getRequestId();

redisTemplate.opsForValue() .set(statusKey，success ? "SUCCESS"”:
"FAILED"，1，TimeUnit .HOURS) ，

} catch (Exception e) {
log.error( "处理秒杀请求失败" ，e) ;
// 记录失败状态

String statusKey = "seckill:status:”+ request.getRequestId();
redisTemplate.opsForValue() .set(statusKey，"ERROR"，1，TimeUnit .HOURS))
】}
}

}

xx

* 秒杀核心逻辑

/

Private boolean doSeckil1(Long userId，Long commodityId) {
// 使用Lua脚本保证原子性操作
String script =
"-- 检查库存\n”+
"Local stockKey = KEYS[1]\n"” +
"local stock = tonumber(redis.call('get'，stockKey))\n" +
"if stock == nil or stock <= 0 then\n” +
”    return 0\n" +
"end\n" +
”An” 二
"-- 检查是否重复购买\n”+
"Local boughtKey = KEYS[2]\n” +
"local hasBought = redis.call('sismember'，boughtKey，RRGV[1])N\n" +
"if hasBought == 1 then\vn"” +
”    return -1\n" +
"end\n" +
”An” 二
"=-- 扣减库存并记录购买\n”+
"redis.call('decr'，stockKey)\n" +
"redis.call('sadd'，boughtKey，RRGV[1])\n” +
”An” 二
"-- 返回成功\n”+
"return 1"7

String stockKey = "seckil1:stock:”+ commodityIqd;

No. 2471 261




## 第 248 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

String boughtKey = "seckill:bought:”+ commodityId7

Long result = (Long) redisTemplate.executel
new DefaultRedisScript<>(script，Long.class)，
Rrrays.asList(stockKey，boughtKey)，
userId.toString()

) 7

if (result == 1) {
// 创建订单(可以进一步异步化)
createorder(userId，commodityId) ;
return truei

】}

return falsey

】}

// 其他辅助方法. . .

Redis如何做限流呢?
限流是为了控制系统的请求速率，防止系统被过多的请求压垮。

Redis 实现限流最简单的方法是基于计数器的固定窗口限流。比如限制用户每分钟最多访问 100 次，我们就用
INCR 命令给每个用户设个计数器，key 是 rate_limit :用户ID:分钟时间戳 ，每次请求就加 1，同时设置 60 秒过
期。如果计数超过 100 就拒绝请求。

// 伪代码
String key = “rate_limit:” + userId7
// 尝试获取当前计数
Long count = redis.get(key);
// 如果key不存在，设置为1并设置过期时间
if (count == null) {
redis .setex(key，60，"1")) // 60秒窗口期
return true; // 允许访问
}
// 如果计数未超过限制
if (count < maxRequests) {
redis_.incr(key)7
return true; // 允许访问

}
return false; // 拒绝访问

这种方法简单粗暴，但有个问题就是临界时间会有突刺，比如用户在第 59 秒访问了 100 次，第 61 秒又访问 100
次，相当于 2 秒内访问了 200 次。

第二种就是滑动窗口限流，通过 Redis 的 ZSET 来实现，把每次请求的时间戳作为 score 存进去，然后用
ZREMRANGEBYSCORE 删除窗口外的旧数据，再用 ZCARD 统计当前窗口内的请求数。这样限流就比较均匀了。

No. 248 1261




## 第 249 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

// 伪代码

String key = "sliding window:" + userId;
long now = System.currentTimeMillis()7

// 添加当前请求到有序集合，score为当前时间戳
redis.zadd(key，now，String.valueOf(now) ) 7
// 移除时间窗口之前的请求数据
redis.zremrangeByScore(key，0，now - windowSize);
// 设置key过期时间，避免冷用户持续占用内存
redis.expire(key，windowSize / 1000 + 1)7
// 获取当前窗口的请求数

Long count = redis.zcard(key) 7

return count <= maxRequests1i

在实际开发中，通常会采用令牌桶算法，它就像在帝都/魔都买车，摇到号才有资格，没摇到就只能等下一次

(钨) 。

可以在 Redis 里存两个值，一个是令牌数量，一个是上次更新时间。每次请求时用 Lua 脚本计算应该补充多

牌，然后判断是否有足够的令牌。

鳞
匀速添加令牌   由       由
令牌桶未满则固定速率                                      加

添加令牌，令牌桶已满 一天
则丢弃令牌

客户端

少

-- Redis Lua脚本实现令牌桶算法

local key = KEYS[1] -- 限流的key

local max_permits = tonumber(RRGV[1])  -- 最大令牌数

local permits_per_second = tonumber(RRGV[2])  -- 每秒产生的令牌数
local required_permits = tonumber(RRGV[3])  -- 请求的令牌数

-- 获取当前时间

local time = redis.call('time')

local now_micros = tonumber(time[1]) * 1000000 + tonumber(time[2])

-- 获取上次更新的时间和当前存储的令牌数

local last_micros = tonumber(redis.call('hget'，key，'1last_ micros') or 0)

No. 2491261

全
令




## 第 250 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

local stored_permits -= tonumber(redis.call('hget'，key， 'stored permits') or 0)

-- 计算时间间隔内新产生的令牌数

local interval_micros = now_micros - last_micros

local new_permits = interval _micros * permits_per_second / 1000000
stored_permits = math.min(max_permits，Sstored_permits + new_permits)

-- 判断令牌是否足够

local result = 0

if stored_permits >= required _permits then
-- 令牌足够，更新令牌数和时间
stored_permits = stored_permits - required _permits
result = 1

end

-- 更新Redis中的数据
redis.call('hset'，key，'1last_micros'，now_micros)
redis.call('hset'，key，'stored_permits'，stored_permits)

redis.call('expire'，key，10)  -- 设置过期时间，避免长期占用内存

return result

1. java 面试指南 (付费) 收录的农业银行面经同学 3java 后端面试原题: 秒杀问题 (错峰、削峰、前
端、流量控制)

2. java 面试指南(付费) 收录的滴滴面经同学 3 网约车后端开发一面原题: 限流算法

memo: 2025年6月13 日修改至此，今天在修改简历的过程中，碰到一位西安交通大学的球友，他整个校园经
历是比较丰富的，先去了新加坡国立大学做暑期交换生，然后又去了加州大学伯克利分校做学期交换生，希望大家
也都能在学校阶段尽量丰富自己的经历，争取多拿一些奖学金、实习经历，这样才能在毕业时有更强的竞争力。

西安交通大学 - Ti sm工'! 985 ”双一流                                                         2022.09 - 2026.06

数据库系统、面向对象程序设计、操作系统、计算机组成原理与体系结构、数据结构与算法

新加披国立大学 -暑期交换项目                                                                            2023.07 - 2023.08
UX设计学习
加州大学伯克利分校 - 学期交换项目                                                                     2025.01 - 2025.05

参与War ore iTapa交换项目,修读CS 161 Computer Security计算机安全与 CS 168 Introduction

to Internet Structure计算机网络

57.客户端宕机后 Redis 服务端如何感知到?

TCP 的 keepalive 是 Redis 用来检测客户端连接状态的主要机制，默认值为 300 秒。

## 针对低延迟场景，设置为60秒，表示每60秒发送一次keepalive探测
config set tcp-keepalive 60

No. 2501261




## 第 251 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

当客户端与服务器在指定时间内没有任何数据交互时，Redis 服务器会发送 TCP ACK 探测包，如果连续多次没有收
到响应，TCP 协议栈会通知 Redis 服务端连接已断开，之后，Redis 服务端会清理相关的连接资源，释放连接。

>“/D           51s )
redis-cLi CONFIG GET tcp-keepalLive

1) “tcp-keepaLive"
2) "300"

Loads
移 redis-ctLi CONFIG GET timeout

I'LL run the Redis CLI command to get the timeout configuration for you.
ww redis-cLi CONFIG GET timeout

CancetLtLed

D
redis-cLi CONFIG GET timeout

1) “timeout”
2) "0"

另外还有一个timeout 参数，用来控制客户端连接的空闲超时时间。

# 表示600秒内没有任何命令则断开连接

config set timeout 600
默认值为 0，表示永不断开连接; 当设置为非零值时，如果客户端在指定时间内没有发送任何命令，服务端会主动
断开连接。

Redis 服务器会定期检查空闲连接是否超时，检查频率由 hz 参数控制; 这将有助于释放那些客户端异常退出但
TCP 连接未正常关闭的资源。

不同的连接池也会有自己的连接检测机制，比如 Jedis 连接池可以通过设置 testonBorrow 和 testWhileIdle 来
启用连接检测 。

疯

spring.redis.jedis.pool.enabled=true

spring.redis.jedis.pool.max-active=200

spring.redis.jedis.pool.max-idle=200

spring.redis.jedis.pool.min-idle=50

spring.redis.jedis.pool.max-wait=3000

spring.redis.jedis.pool.time-between-eviction-runs=60000

No. 2511 261




## 第 252 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

1. Java 面试指南 (付费) 收录的字节跳动面经同学 21 拌音商城一面面试原题: 如果客户端宕机服务器如
何感知?

memo: 2025年6 月14 日修改至此，今天有球友在 VIP 群里发消息说，快手oc 了，堆喜他。球友们都太有实力
了。

二哥VIP 10 群 (444) CQ                      。

锡- 沉默王二-二哥: 面渣逆袭并发编程篇 2.0 …

从 53 条新消息

哥哥们，快手oc了，目前手里还有京东和夸克还
没有一面，大伙觉得还有必要面吗

所
/又

呈:   太有石粒辣

整整一个半月，面渣逆袭 Redis 篇第二版终于整理完了，这一版几乎可以说是重写了，每天耗费了大量的精力在上
面，可以说是改头换面，有一种士别俩月，当刮目相看的感觉 (从 1.8 万字暴涨到 4.6 万字，加餐的同时区分高频
低频版) 。

No. 252 1 261




## 第 253 页


Q

Apple Books
加 主页

书库

吻 全部

@@ 欲读清单
加 已恋完
加 图书

人有声书
目 PDF

目 我的试恋版
我的藏书

十新建书

个 马伟青

网上的八股其实不少，

的都懂。

面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

全部

国 | | 辐西昌图 | | 辐本到图
Redis篇           MySQL篇        并发编程篇           JVM篇

三分恶|沉默王二修订版              三分恶|沉默王二修订版              三分恶|沉默王二修订版              三分恶|沉默王二修订版

二哥的JVM          二哥的并发编
进阶之路.md           程进阶之路.md

_回四到四
Java基础篇

三分恶|沉默王二修订版

_回四到四
集合框架篇

三分恶|沉默王二修订版

有些还是付费的，我觉得是一件好事，可以给大家提供更多的选择，但面渣逆袭的含金量懂

No. 2531 261




## 第 254 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

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

No. 2541 261




## 第 255 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

好滴!

谢谢二哥

我把你推荐给我们实验室的基本所有人了

他们的反馈都是八股看面渣

包稳的哈!

No. 2551 261

Fa




## 第 256 页


面渣逆效 Redis篇第二版-让天下所有的面渣都能逆袭

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

No. 2561 261




## 第 257 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

革 =     哥, 下一本面渣 2.0 进度怎么样
了， 大期待了， 这几本 2.0 的质量比
1.0好太多了, 特别是将相关高频的

面经集中在一起, 看完一小部分可
以通过这些问题来自我拷打一下，
效果简直不要太好俩名外锅乌

下午4:34

重  二哥加油加油加油，好期待 mysql
和redis 的2.0，太喜欢二哥的面渣
了， 看了市面上不少的八股， 兜镶
转转还是二哥的最舒服

很多时候，我觉得自己是一个佛系的人，不愿意和别人争个高低，也不愿意去刻意宣传自己的作品。
我喜欢静待花开。

如果你觉得面渣逆袭还不错，可以告诉学弟学妹们有这样一份免费的学习资料，帮有我做个口碑。
我还会继续优化，也不确定第三版什么时候会来，但我会尽力。

愿大家都有一个光明的未来。

由于 PDF 没办法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】，或者扫描/长按识别下面的二维
码，关注二哥的公众号，回复【222】即可拉取最新版本。

No. 2571 261




## 第 258 页


面渣逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，上毕竟星球用户都付费过了，
我有必要让他们先享受到一点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

No. 258 / 261




## 第 259 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

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

No. 2591 261




## 第 260 页


图文详解 57 道 Redis 面试高频题，这次吊打面试官，我

面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

面渣逆鞭 Redis篇第二版

[了

要产量1         理庆庆2

LE目
ELEE

Redis 进程

Redis 会根据操作系统选择最优的 IO 多路复用技
术，比如 Linux 下使用 epoll ，macOS 下使用
kqueue 等。

// epol1 的创建和使用
int epfd = epoll_create(1024); // 创建 epol1 实阅
struct epoll_event ev，events[MRX_EVENTS];

// 添加改听事件

ev.events = EPOLLIN7

ev.data.fd = listen_sock)

epoll_ctl (epfd，EPOLL_CTL_ADD，1listen_sock，sev)

作者: 三分恶，戳原文链接。
没有什么使我个塘一丰了月的，维天岩六肥玫瑰、有绽芒、有宁鹏的港湾，我是不系之上舟。
系列内容:

e

e

昌

面渣逆袭Java SE 篇 】

面淹逆效Java 集合框架篇 虽
面渣逆效Java 并发编程篇 唾
面潮逆次JVM 篇吨
面渣逆效 Spring入吨
面渣逆袭 Redis 篇 下

面渣逆袭 MyBatis 篇 是
面潮逆次 MySQL复 吨

面渣逆区 RocketMQ 入中
面淹逆效分布式篇 虽

说和
觉得

在 Redis 6.0 之前，包括连接建立、请求读取、响
应发送，以及命令执行都是在主线程中顺序执行的，
这样可以避免多线程环境下的锁竞争和上下文切换，
因为 Redis 的绝大部分操作都是在内存中进行的，性
能瓶颈主要是内存操作和网络通信，而不是 CPU。

为了进一步解决网络 IO 的性能瓶颈，Redis 6.0 引
入了多线程机制，把网络 IO 和命令执行分开，网络
IO 交给线程池来处理，而命令执行仍然在主线程中
进行，这样就可以充分利用多核 CPU 的性能。

稳了 (手动 dog) 。整理: 沉默王二，戳转载链接，

No. 2601261




## 第 261 页


面潮逆袭 Redis篇第二版-让天下所有的面渣都能逆袭

。 面渣逆袭设计模式入中
。 面渣逆区 Linux 篇中

No. 2611 261



