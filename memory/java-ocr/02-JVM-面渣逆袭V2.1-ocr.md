# 02-JVM-面渣逆袭V2.1

> 来源：02-JVM-面渣逆袭V2.1.pdf

> OCR 解析时间：2026-03-14 17:12:08

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 95

- **文件大小**: 15.97 MB


---


## 第 1 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

合 ”二哥的Java进阶之路

三分恶

沉默王二修订版

No.1195




## 第 2 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

2.3 万字 115 张手绘图，详解 54 道 java 虚拟机面试高频题 (让天下没有难背的八股) ，面渣背会这些JVM 八股
文，这次吊打面试官，我觉得稳了 (手动 dog) 。整理: 沉默王二，戳转载链接，作者: 三分恶，戳原文链接。

亮白版本更适合拿出来打印，这也是很多学生党喜欢的方式，打印出来背诵的效率会更高。

eee 回 回 DC 立 面千地装JVM简 V2.0.pdf - 福昕阅读器 。〇 搜索                               出了及@

文件 主页 注释 视图 表单 保护 共享 帮助                           Y

开始                               面酒吉贰 JVM篇 V2.… XX
-aoggciaal

40.做过JVM 调优吗?
    LE                         四

JVM 调优是一个复杂的过程，调优的对象包括堆内存、垃圾收集器和JVM 运行时参数等.

JVM调优

= 只 三、 垃圾收集                                                           |
直 内 23.讲讲 JVM 的垃圾回收机制作                                                  |                      |
二”内 24.如何庆断对象仍然存活?
者 内 25.Java 中可作为 GC Roots 的3
只 26fiaize0广法了解加?                                                               内凑合用全
一
# 只 28Minor Gc、MaiorGc、Mied       实时监控            事后分析                        垃极回收频率
内 29yYoung Gc 什么时候甬发?
寺内 30 什么时候会角发 Full GC?
二 ”只31知道时些垃圾收集器?
市”内 32 能详细说一下 CMS 的垃圾收#
只 33 1 垃骂收入簿了解码?
内 34有了 CMS，为什么还要引入1

窜 只35你们线上用的什么垃圾收集和       如果堆内存设置过小，可能会导致频繁的垃圾回收。所以在技术泊实战项目中，启动JVM 的时候配置了 -xms 和

内36 .过级收集名应该如何选择7         -mx 参数，让堆内存最大可用内存为 2G (我用的丐版服务器) 。                                     1
5 内 四、JVM 调优

当”内 37用过电些性能监控的命令行工
二内 38.了角于此可视化的性能监控了                                          的
内 39.VN 的常见参数本村知道
风 40全过JVM 调估吧?
和站AD                                    机过半 JVN估和二后-让天下所有的西装

分析系统运行情况                                 确定 JVM 调优量化目标                 确定 JVM 调优拓数

二可的 Java 进阶之路

全 《  7 ”19 》》咱驻           国目围电一

2024年 12 月 30 日开始着手第二版更新。
。 对于高频题，会标注在 《java 面试指南 (付费) 》中出现的位置，哪家公司，原题是什么，并且会加居，目
录一目了然; 如果你想节省时间的话，可以优先背诵这些题目，尽快做到知彼知己，百战不殖。
。 区分八股精华回答版本和原理底层解释，让大家知其然知其所以然，同时又能做到面试时的高效回答。
。 结合项目 (技术派、pmhub) 来组织语言，让面试官最大程度感受到你的诚意，而不是机械化的背诵。

。 修复第一版中出现的问题，包括球友们的私信反馈，网站留言区的评论，以及 GitHub 仓库中的issue，让这
份面试指南更加完善。

。 增加二哥编程星球的球友们拿到的一些 offer，对面渣逆袭的感谢，以及对简历修改的一些认可，以此来激励
大家，给大家更多信心。

。 优化排版，增加手绘图，重新组织答案，使其更加口语化，从而更贴近面试官的预期。

吕

十 13765%

No.2195




## 第 3 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

日  toBeBetterJavaer                   master                      ww Last fetched 11 minutes agk

anfenejivm md                                               密- 口

-1Dpk 1.8m丰区域1(httpsi//cdn.tobebetterjavaer.con/tobebetterjavaer/images/sidebar/sanfene/jvm-8.png)
+ 5 为什么使用元空间符代永久代?

Changes 到       History     docslsi

 docslsr_/garbage-collectormd 回
238

双 docsjsrclsidebarsanf-ivmmd 回 jw 2

2 changed files

-84 5 .为什么使用元空间蔡代永久代作为方法区的实现?
+。 客观上，永久代会导致 Java 应用程序更容易出现内存涪出的问题，因为它要受到 ]JVM 内存大小的限制-

-Java 庶所机规范项定的方法区只是换入方式实现。有客观和主观两个原因
+ HotSpot 庶狼机的永久代大小可以通辽“-XX: MaxPermSize”杀数来设置，32 位机器默认的大小为 64N，64 位的机可风为 85H

一 守观上使用永久代来实现方法区的决定的设计导致了 ava 应用更容易深到内存溢出的问题(永久代有-XX: MaxPermSize 的上限，即使不设置
也有默认大小，而 ]9 和 Rockit 只要没有般碰到进程可用内存的上由，例如 32 位系统中的468 限制，就不会出问题)，而且有棚少数方法
(例如 Stringi; intern()) 会因表入代的原因而导到不同虚拟机下有不同的表现

，。 而 9 和 JRockit 虚拟机吉不存在这种了制，只要没有骸辜到进程可用的内存上限，例如 32 位系统中的 4GB 限制，就不会出问题

一 主观上当 0racte 收购 BEA 获得了 Rockit 的所有权后，准备把 JRockit 中的优秀功能，狠如 Java Miss1on Controt 管理工内，移
秆到 Hot5pot 虚拟机时，但因为两才对方法区实现的差昼而面请多国难。考虑到 Hot5pot 未来的发展, 在 JDK 6 的 时候 HotSpot 开发园

队就有放弃永久代，逐步改为采用本地内存 (Native Memory) 来实现方法区的计划了,到了 ]DK 7 的 HotSpot，已经反原本放在永久代的字符

中党量池、蒋态变量等移出，而到了 ]0DK 8，终于完全广弃了永久代的概念，改用与 ]Rockit、]9 一样在本地内存中实现的元空间 (Neta-space)
来代蔡， 把 ]DK 7 中永久代还利余的内容 【主要是类型信息) 全部移到元空间中-

vv      司”， 襄上, 当 oracte 履软 BEA 获租了 JRockit 的所有权后，就准备把 ]Rockit 中的优秀功能移植到 HotSpot 中
246 287

-4 6 .对象创建的过程了解加7
+如 Java Mission Controt 管理工具.

                          +。 但因为两个二所机时方法区实现有差异，导到这项工作才到了很多朋力。
De                    248 291
v 区 249       --当我们使用 new 关银字创奸一个对象的时候，]W 首先会检查 new 指人的多数是否能在第量中定位到一个类的特呈引用，然后检查这个符号引用
代表的类是否已科加埠、解折和轴妈化过如果没有，就和执行相应的类加夫这各
~      区 ， em hotspot aa未9呈展0K 6 的昌候，开发园了部打重放闻永久代了
Ar                              258 293
~区251      -如果已经加载，JWW 会为新生对象分本内存，内存分本完成之后，]W 将分本到的内存空间反化为办值 (成员变量，数信关型是9，布尔类型是 了

Ce                 se到并 ut，提下末对，对介时条理个区实到、有和的而、对多6C 分代年

ni 7 的时急“划法了一小上5各珈二的在交鲜休的字竺昌亿蝇演，共杰村和下动到了考中

，或者扫描/长按识别下面的二维

由于 PDF 没办法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二
码，关注二哥的公众号，回复【222】即可拉取最新版本。

No. 3195




## 第 4 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

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

No.4195




## 第 5 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

eee 品口避    忌“面尖逆闭 JVM简 V2.0 (中黑版) .pdf - 福昕阅读器 CQ 搜索
文件 主页 注释 视图 表单 保护 共享 帮助

开始                     面造逆贰 JVM篇 V2.0.       面秸逆闭 JVM匾 V2.… X
2
砚  了 贡
岛
6 .对象创建的过程了解吗?
银
寺
林
盖
二可的 Java 进阶之路
余《    23  "” 115 》罗咯                      国目转轴一       十 13765% ”总
一
一、引言
=
1.什么是JVM?

JVM，也就是java 虚拟机，它是java 实现跨平台的基石。
程序运行之前，需要先通过编译器将 Java 源代码文件编译成java 字节码文件;
程序运行时，JVM 会对字节码文件进行逐行解释，翻译成机器码指令，并交给对应的操作系统去执行。

No.5195




## 第 6 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

ZN 7/    2 K/硼
OO

CBN
                 所

这样就实现了 java 一次编译，处处运行的特性。

说说JVM 的其他特性?
@、JVM 可以自动管理内存，通过垃圾回收器回收不再使用的对象并释放内存空间。

@、JVM 包含一个即时编译器JIT，它可以在运行时将热点代码缓存到 codeCache 中，下次执行的时候不用再一行
一行的解释，而是直接执行缓存后的机器码，执行效率会大幅提高。

No.6195




## 第 7 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

马文件，

2 六“

EN    0

7
ZJ
OO

CA

YY     5
ZNNNMNMO 2
2 IN

为什么要学习JVM?




## 第 8 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

学习JVM 可以帮助我们开发者更好地优化程序性能、避免内存问题。
比如说了解JVM 的内存模型和垃圾回收机制，可以帮助我们更合理地配置内存、减少 GC 停顿。
比如说掌握JVM 的类加载机制可以帮助我们排查类加载冲突或异常。

再比如说，JVM 还提供了很多调试和监控工具，可以帮助我们分析内存和线程的使用情况，从而解决内存溢出内存
泄露等问题。

1. java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 有了解JVM 吗
2. java 面试指南(付费) 收录的字节跳动同学 20 测开一面的原题: 了解过JVM 么? 讲一下JVM 的特性
2.说说JVM 的组织架构 (补充)
增补于2024年03月08日。
推荐阅读: 大白话带你认识JVM
JVM 大致可以划分为三个部分: 类加载器、运行时数据区和执行引擎。

GD 类加载器，负责从文件系统、网络或其他来源加载 Class 文件，将 Class 文件中的二进制数据读入到内存当中。

No.8195




## 第 9 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

@) 运行时数据区，JVM 在执行Java 程序时，需要在内存中分配空间来处理各种数据，这些内存区域按照 Java 虚拟
机规范可以划分为方法区、堆、虚拟机栈、程序计数器和本地方法栈。

图执行引擎，也是JVM 的心脏，负责执行字节码。它包括一个虚拟处理器、即时编译器JIT 和垃圾回收器。
1. Java 面试指南 (付费)_收录的腾讯 java 后端实习一面原题: 说说JVM 的组织架构
2. java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: JVM的架构，具体冰述一下各个部分的功

能?

二、内存管理
3.去能说一下JVM 的内存

区域吗?

推荐阅读: 深入理解JVM 的运行时数据区
按照Java 虚拟机规范，JVM 的内存区域可以细分为 程序计数器 、 虚拟机栈 、 本地方法栈 、堆和 方法区 。

JVM内存区域介分

[2

帮所向全 | |本地方法

[ ，] 二有线程共椰的小据书

E玖  线程柄离的数据区

其中 方法区 和堆是线程共享的， 虚拟机栈 、 本地方法栈 和 程序计数器 是线程私有的。

No.9195




## 第 10 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

介绍一下程序计数器?

程序计数器也被称为 PC 寄存器，是一块较小的内存空间。它可以看作是当前线程所执行的字节码行号指示器。
介绍一下Java 虚拟机栈?

java 虚拟机栈的生命周期与线程相同。

当线程执行一个方法时，会创建一个对应的材赎，用于存储局部变量表、操作数栈、动态链接、方法出口等信息，
然后栈帧会被压入虚拟机栈中。当方法执行完毕后，栈帧会从虚拟机栈中移除。

上

妆| |短| |严
愉| |全| 过
公| |这
东| |全| 只
SS

四
四
|
|
|

CGIUAAAAAG AAA

|
SSsSSS

一个什么都没有的空方法，空的参数都没有，那局部变量表里有没有变量?
对于静态方法，由于不需要访问实例对象 this，因此在局部变量表中不会有任何变量。

No.10195




## 第 11 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效
对于非静态方法，即使是一个完全空的方法，局部变量表中也会有一个用于存储 this 引用的变量。this 引用指向当
前实例对象，在方法调用时被隐式传入。
详细解释一下
比如说有这样一段代码:

public void emptyMethod() {
// 什么都没有

public static void staticEmptyMethod() {

// 什么都没有

用 javap -v VarDemol 命令查看编译后的字节码，就可以在emptyMethod 中看到这样的内容:

pubLic void emptyMethod() ;
descriptor: ()V
fLags: ACC_PUBLIC
Code:
stack=6，LocaLs=1，args_size=1

9: return
LineNumberTabtLe:
TLine 6: 0
LocatLyvariabLeTabtLe:
Start Length  SLot Name Signature
9   1  9 this  Lcom/github/paicoding/forum/web/javabetter/jvm/VarDemo1;

这里的 locals=1 表示局部变量表有一个变量，即 this，slot 0 位置存储了 this 引用。

而在静态方法 staticEmptyMethod 中，你会看到这样的内容
pubLic static void staticEmptyMethod() ;
descriptor: ()V
fLags: ACC_PUBLIC，ACC_STATIC
Code :

stack=0，LocaLs=0，args_slize=0

0: retunrn
LineNumberTabtLe :
Line 10: 0

No.11195




## 第 12 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

这里的 locals=0 表示局部变量表为空，因为静态方法属于类级别方法，不需要 this 引用，也就没有局部变量。

介绍一下本地方法栈?

本地方法栈与虚拟机栈相似，区别在于虚拟机栈是为JVM 执行Java 编写的方法服务的，而本地方法栈是为 Java 调
用                服务的，通常由 C/C++ 编写 。

在本地方法栈中，主要存放了 native 方法的局部变量、动态链接和方法出口等信息。当一个Java 程序调用一个
native 方法时，JVM 会切换到本地方法栈来执行这个方法。

介绍一下本地方法栈的运行场景?

当java 应用需要与操作系统底层或硬件交互时，通常会用到本地方法栈。

比如调用操作系统的特定功能，如内存管理、文件操作、系统时间、系统调用等。

详细说明一下:

比如说获取系统时间的 system-currentrimeMillis() 方法就是调用本地方法，来获取操作系统当前时间的。
System {

curityManager

SecurityManager getSecurityManager()                 Securituyi

JtiL.Date

currentTimeMittLis() ;

再比如JVM 自身的一些底层功能也需要通过本地方法来实现。像 Object 类中的 hashcode() 方法、clone() 方
法等。

No.12195




## 第 13 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

native 方法解释一下?
推荐阅读: 手把手教你用语言实现 java native 本地方法

native 方法是在Java 中通过 native 关键字声明的，用于调用非 java 语言，如 C/C++ 编写的代码。java 可以通过
JNI，也就是Java Native Interface 与底层系统、硬件设备、或者本地库进行交互。

介绍一下java 堆?
扒是JVM 中最大的一块内存区域，被所有线程共享，在JVM 启动时创建，主要用来存储 new 出来的对象。

二哥的 JVM 进阶之路
方法参数
一一一”|            对象
对象引用
局部变量                                   字符串常量池
(基本数据类型)
栈                                              堆

No.13195




## 第 14 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

java 中"几乎"所有的对象都会在堆中分配，堆也是垃圾收集器管理的目标区域。
从内存回收的角度来看，由于垃圾收集器大部分都是基于分代收集理论设计的，所以堆又被细分为 新生代 、 老年

代 、 Eden空间 、From Survivor空间 、 To survivor空间等。

Java推: 从垃投收集角度划分

去                          Full GC                          和
所一inor 6一人>“一由jor GC一一一

二一一一一mm: 设置新生代大小一一一一
所 和s:设置堆内存最小值 -Xmx:设置堆内存最大值一 人

随着 JIT 编泽器的发展和逃逸技术的逐渐成熟,“所有的对象都会分配到堆上"就不再那么绝对了。

从JDK 7 开始,，JVM 默认开启了逃逸分析，意味着如果某些方法中的对象引用没有被返回或者没有在方法体外使
用，也就是未逃逸出去，那么对象可以直接在栈上分配内存。

堆和栈的区别是什么?

扒属于线程共享的内存区域，几乎所有 new 出来的对象都会堆上分配，生命周期不由单个方法调用所决定，可以
在方法调用结束后继续存在，直到不再被任何变量引用，最后被垃圾收集器回收。

栈属于线程私有的内存区域，主要存储局部变量、方法参数、对象引用等，通常随着方法调用的结束而自动释放，
不需要垃圾收集器处理。

介绍一下方法区?

方法区并不真实存在，属于java 虚拟机规范中的一个还辑概念，用于存储已被JVM 加载的类信息、常量、静态变
量、即时编译器编译后的代码缓存等。

在 HotSpot 虚拟机中，方法区的实现称为永久代 PermGen，但在Java 8 及之后的版本中，已经被元空间
Metaspace 所替代。

变量存在堆栈的什么位置?
对于局部变量，它存储在当前方法栈帧中的局部变量表中。当方法执行完毕，栈帧被回收，局部变量也会被释放。

public void method() {
int localvar = 100;  // 局部变量，存储在栈帧中的局部变量表里

)}

No. 14195




## 第 15 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

对于静态变量来说，它存储在 java 虚拟机规范中的方法区中，在java 7 中是永久带，在Javag8 及以后 是元空间。

Public class StaticVarDemo {
public static int staticVar = 100;  // 静态变量，存储在方法区中
》

1. java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 堆和栈的区别是什么
2. java 面试指南 (付费) 收录的比亚迪面经同学 3 java 技术一面面试原题: 介绍一下JVM 运行时数据区

3. java 面试指南 (付费) 收录的字节跳动面经同学 1 Java 后端技术一面面试原题: 讲一下JVM 内存结
构?

4. java 面试指南 (付费) 收录的京东面经同学 1 java 技术一面面试原题: 说说JVM 运行时数据区
5. java 面试指南 (付费) 收录的美团面经同学 2 java 后端技术一面面试原题: JVM 内存结构了解吗?
6. java 面试指南 (付费) 收录的快手面经同学 1 部门主站技术部面试原题: 请说一下java 的内存区域，

程序计数器等?
7. java 面试指南(付费) 收录的字节跳动面经同学 8 Java 后端实习一面面试原题: jvm 内存分布，有垃
圾回收的是哪些地方

8. java 面试指南 (付费) 收录的得物面经同学 8 一面面试原题: 说一说 jvm 内存区域

9. Java 面试指南 (付费) 收录的美团面经同学 3 java 后端技术一面面试原题: jmm 内存模型 栈 方法区存
放的是什么

10. Java 面试指南 (付费) 收录的收钱吧面经同学 1 Java 后端一面面试原题: 你提到了栈帧，那局部变量
表除了栈帧还有什么?一个什么都没有的空方法，完全空的参数什么都没有，那局部变量表里有没有变

量?
11. java 面试指南(付费) 收录的招银网络科技面经同学 9 java 后端技术一面面试原题: java堆内存和栈内
存的区别

12. java 面试指南 (付费) 收录的 OPPO 面经同学 1 面试原题: 说一下VM内存模型

13. java 面试指南 (付费) 收录的深信服面经同学 3 Java 后端线下一面面试原题: JVM变量存在堆栈的位
置?

14. java 面试指南 (付费) 收录的TP联洲同学 5 java 后端一面的原题: jvm内存区域，本地方法栈的运行场
景，Native方法解释一下

15. java 面试指南 (付费) 收录的字节跳动同学 17 后端技术面试原题: jvm结构 运行时数据区有什么结构
堆存什么

16. java 面试指南 (付费) 收录的腾讯面经同学 29 java 后端一面原题: new一个对象存放在哪里? (运行
时数据区) ，局部变量存在|VM哪里

4.说一下JDK 1.6、1.7、1.8 内存区域的变化?
JDK 1.6 使用永久代来实现方法区:

No.15195




## 第 16 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

JDK1.6

7

JDK 1.7 时仍然是永久带，但发生了一些细微变化，比如将字符串常量池、静态变量存放到了堆上。

8
丰上GZGEGN
| [斌簿让芝量地|
GO

JDK1.7

在JDK 1.8 时，直接在内存中划出了一块区域，叫元空间，来取代之前放在JVM 内存中的永久代，并将运行时常量
池、类常量池都移动到了元空间。

No.16195




## 第 17 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

JDK1.8

5.为什么使用元空间替代永久代?
客观上，永久代会导致Java 应用程序更容易出现内存溢出的问题，因为它要受到JVM 内存大小的限制。

Hotspot 虚拟机的永久代大小可以通过 -xx: MaxPermsize 参数来设置，32 位机器默认的大小为 64M，64 位的
机器则为 85M 。

而J9 和JRockit 虚拟机就不存在这种限制，只要没有触碰到进程可用的内存上限，例如 32 位系统中的 4GB 限制，
就不会出问题。

主观上，当 Oracle 收购 BEA 获得了JRockit 的所有权后，就准备把 JRockit 中的优秀功能移植到 HotSpot 中。
如java Mission Control 管理工具。

但因为两个虚拟机对方法区实现有差异，导致这项工作遇到了很多阻力。

考虑到 HotSpot 虚拟机未来的发展，JDK 6 的时候，开发团队就打算放弃永久代了。

JDK 7 的时候，前进了一小步，把原本放在永久代的字符串常量池、静态变量等移动到了堆中。

JDK 8 就终于完成了这项移出工作，这样的好处就是，元空间的大小不再受到JVM 内存的限制，而是可以像J9 和
JRockit 那样，只要系统内存足够，就可以一直用。

No. 17195




## 第 18 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

6.二对象创建的过程了解吗?

当我们使用 new 关键字创建一个对象时，JVM 首先会检查 new 指令的参数是否能在常量池中定位到类的符号引
用，然后检查这个符号引用代表的类是否已被加载、解析和初始化。如果没有，就先执行类加载。

new 一个对象

|     六
分配内存 ”|<
二哥的 Java 进阶之路
Auto
-| 对象内存初始化 广-| 设置对象头 “一>| 执行<init>方法

象类型是 null。
接下来会设置对象头，里面包含了对象是哪个类的实例、对象的哈希码、对象的 GC 分代年龄等信息。

最后，JVM 会执行构造方法 <init> 完成赋值操作，将成员变量赋值为预期的值，比如 int age = 18 ，这样一
个对象就创建完成了。

对象的销毁过程了解吗?

当对象不再被任何引用指向时，就会变成垃圾。垃圾收集器会通过可达性分析算法判断对象是否存活，如果对象不
可达，就会被回收。

垃圾收集器通过标记清除、标记复制、标记整理等算法来回收内存，将对象占用的内存空间释放出来。

可以通过 java -XX:+PrintCommandLineFlags -version 和 java -XX:+PrintGCDetails -version 命令查

看JVM 的 GC 收集器。

No.18195




## 第 19 页


逆袭 JVM篇第二版-让天下所有的面渣都能逆效

java -XX:+PrintCommandLineFLags -version

-XX:InitiaLHeapSize=2147483648 -XX:MaxHeapSize=32203866112 -XX:+printCommandLineFLags -XX:+UseCompressedC
TassPointers -XX:+UseCompressed0ops -XX:+UseParatLeLGC

openjdk version "1.8.0_412"

Open]DK Runtime Environment Corretto-8.412.08.1 (buttd 1.8.0_412-b08)

Open]DK 64-Bit Server VM Corretto-8.412.08.1 (buitd 25.412-b68，mixed mode)

java -XX:+PrintGCDetatLs -version

openjdk version "1.8.0_412"
0penJDK Runtime Environment Corretto-8.412.08.1 (buiLd 1.8.0_412-b08)
0penJDK 64-Bit Server VM Corretto-8.412.08.1 (buitLd 25.412-b098，mixed mode)
Heap
PSYoungGen    totalL 611840K，used 20992K [0x0000000800300000，0x000000082ad80000，0x0000000a80000000 )
eden space 524800K，4% Used [0x0000000800300000,0x0000000801780188 ,0x0000000820380000)
from space 87040K，0s% used [0x0000000825880000,0x0000000825880000,0x000000082ad80000)
to ”space 87040K，0% used [0x0000000820380000,0x0000000820380000,0x0000000825880000)
Par0LdGen     totaL 1398272K，used 0K [0x0000000300800000，0x0000000355d80000，0x0000000800300000)
object space 1398272K，0% used [0x0000000300800000,0x0000000300800000,0x0000000355d80000)
Metaspace     used 2227K，capacity 4480K，committed 4480K，reserved 1056768K
CLass Space   used 241K，capacity 384K，committed 384K，reserved 1048576K

可以看到，我本机安装的JDK 8 默认使用的是 Parallel Scavenge + Parallel old 。

不同参数代表对应的垃圾收集器表单 :

新生代                     老年代             JVM人参数
Serial                      Serial               -XX:+UseSserialGC
Parallel Scavenge         Serial             -XX:+UseParallelGC -XX:-UseParallelOldGC
Parallel Scavenge          Parallel Old         -XX:+UseParallelGC -XX:+UseParallelOldGC
Parallel New             CMS              -XX:+UseParNewGC -XX:+UseConcMarkSweepGC
G1                               -XX:+UseG1GC

1. java 面试指          录的比亚迪面经同学 3 java 技术

录的美团面经同学 2 java 后端技术一面面
经同学 1 java 后端技术一

CMS，G1 内存清理

7.堆内存是如何分配的?
在堆中为对象分配内存时，主要使用两种策略: 指针碰撞和空闲列表。

No. 19195




## 第 20 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

指针碰撞适用于管理简单、碎片化较少的内存区域，如年轻代; 而空闲列表适用于内存碎片化较严重或对象大小差
异较大的场景如老年代。

什么是指针碰撞?
假设推内存是一个连续的空间，分为两个部分，一部分是已经被使用的内存，另一部分是未被使用的内存。

在分配内存时，java 虚拟机会维护一个指针，指向下一个可用的内存地址，每次分配内存时，只需要将指针向后移
动一段距离，如果没有发生碰撞，就将这段内存分配给对象实例。

什么是空闲列表?
JVM 维护一个列表，记录堆中所有未占用的内存块，每个内存块都记录有大小和地址信息。
当有新的对象请求内存时，JVM 会遍历空闲列表，寻找足够大的空间来存放新对象。
分配后，如果选中的内存块未被完全利用，剩余的部分会作为一个新的内存块加入到空闲列表中。
1. java 面试指南 (付费)_收录的携程面经同学 1 java 后端技术一面面试原题: 对象创建到销毁，内存如
何分配的， (类加载和对象创建过程，CMS，G1 内存清理和分配)

No. 20195




## 第 21 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

memo: 2025年1月10 日修改到此

8.new 对象时，堆会发生抢占吗?

会
会。

Thread 1                                                                                                       Eden Space

E     String() ;                   光    String

入           ArrayList

Thread 2

ArrayList<String>();

new 对象时，指针会向右移动一个对象大小的距离，假如一个线程 A 正在给字符串对象 s 分配内存，另外一个线
程 B 同时为 ArrayList 对象 ! 分配内存，两个线程就发生了抢占。

JVM 怎么解决堆内存分配的竞争问题?

为了解决堆内存分配的竞争问题，jVM 为每个线程保留
冲区，用于存放该线程分配的对象。

一小块内存空间，被称为 TLAB，也就是线程本地分配缓

Eden Space
Thread1                                                                          TLAB1
=      String() ;                        ?|     String
Thread 2                                                                   TLAB 2
=      ArrayList<String>() ;           训
ArrayList

No. 21195




## 第 22 页


面洁闻获 JVM篇第二版-让天下所有的面洁都能地玖
当线程需要分配对象时，直接从 TLAB 中分配。只有当 TLAB 用尽或对象太大需要直接在堆中分配时，才会使用全
局分配指针。
这里简单测试一下 TLAB。
可以通过 java -xx:+PrintFlagsFinal -version | grep TLAB 命令查看当前JVM 是否开启了 TLAB。

java -xx:+PrintFLagsFinat -version | grep TLAB

boot FastTLABRefiLL                                                                  {product}
uintx MinTLABSize                                                         {product}
boot PrintTLAB                                                       {fproduct}
boot ResizeTLAB                                                          {pd product}
uintx TLABALLocationWeight                                                  {product}
uintx TLABRefiLLWasteFraction                                                {product}
uintx TLABSize                                                            {product}

boot TLABStats                                                           {product}

uintx TLABWasteIncrement                                                    {product}

uintx TLABWasteTargetPercent                                                {product}

boot UseTLAB                                                          {pd product}

boot ZeroTLAB                                                            {product}
openjdk version "1.8.0_412"

如果开启了 TLAB，会看到类似以下的输出，其中 bool UseTLAB 的值为 true。
我们编写一个简单的测试类，创建大量对象并强制触发垃圾回收，查看 TLAB 的使用情;

TLRABDemo 1{

Pub1l  static void main(String[] args) {
for (int ii= 0)i<10000000; i++) {
allocate() 7
】}
System.gc() 7
】}

private static void allocate() {

byte[] bytes = new byte[64];

在 VM 参数中添加 -XX:+UseTLRAB -XX:+PrintTLAB -XX:+PrintGCDetails -XX:+PrintGCDatestamps ，运行
后可以看到这样的内容:

gc thread: 6x999699612d6e7899 [id          19496KB            3 16   a   1.69699
gc thread: 6x999886612d6e6868 [id:    t      19496KB      8      : 167936B attoc: 1.99998
gc thread; 6x990869613c69a908 [id: 69     4      t      t   8: 167936B at   98669 。 52494KB
tats: thrds: 3 refitts: 5      attocs: 9 max             ax: 18       464B fast: 8B |
2625-61-11T11:16:36.809+6869    (System .gcCO) [PSYoung6en:                           ，         ] [Tines: us
5-91-11T11:16:39.861+9899: [FuLL 6C (System.gcC)) [PSYoung               [ParotdGen: 8K->21    8     2494K->2112K(2918]
Heap
PSYoungei       ，    2    [exg9669       ,8         6，       06066660)
eden space
from space 87646K，g% used [6xggl
to 。 space 87649K，g% used [6x9669969
Parotd6en     totat 1398272K，used 2112K [6x6869089399899969，6    9                 98899)
object space 1398272K，g% used [|   90396869666,9x996668|

Metaspace     used 3438K，capacity 4564K，committed

class space 。 used 367K，capacity

No. 22195




## 第 23 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

。 waste: 未使用的TLAB 空间。
。 alloc: 分配到TLAB 的空间。
。 refills: TLAB 被重新填充的次数。

可以看到，当前线程的 TLAB 目标大小为 10,496 KB ( desired_size: 10496KB ) ; 未发生慢分配 ( slow
allocs: 0) ; 分配效率直接拉满 (alloc: 1.00000 52494KB ) 。

当使用 -XX:-UseTLAB -xxX:+PrintGCDetails 关闭TLAB 时，会看到类似以下的输出:

98890688693666
)

直接出现了两次 GC，因为没有 TLAB，Eden 区更快被填满，导致年轻代 GC。年轻代 GC 频繁触发，一部分长生
命周期对象被晋升到老年代，间接导致老年代 GC 触发。

9.能说一下对象的内存布局吗?

好的。

对象的内存布局是由java 虚拟机规范定义的，但具体的实现细节各有不同，如 Hotspot 和 Openj9 就不一样。
就全我们常用的 Hotspot 来说吧。

对象在内存中包括三部分: 对象头、实例数据和对齐填充。

No. 23195




## 第 24 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

         哈希码
6GC分代年齿
6GC分代年苓
对象自身运行时数据
(Wark Word)       |      锁状态标志
对象头                 类型指针                        线程持有的锁
是数组，还有记录数组     偏向线程1D
对象                                         区浊      偏向时间戳
实例数据
对齐填充
对象的存储布局

说说对象头的作用?
对象头是对象存储在内存中的元信息，包含了Mark Word、类型指针等信息。

Mark Word 存储了对象的运行时状态信息，包括锁、哈希值、GC 标记等。在 64 位操作系统下占 8 个字节，32
位操作系统下占 4 个字节。

类型指针指向对象所属类的元数据，也就是 Class 对象，用来支持多态、方法调用等功能。
除此之外，如果对象是数组类型，还会有一个额外的数组长度字段。占 4 个字节。
类型指针会被压缩吗?

类型指针可能会被压缩，以节省内存空间。比如说在开启压缩指针的情况下占 4 个字节，否则占 8 个字节。在JDK
8 中，压缩指针默认是开启的。

可以通过 java -xx:+PrintFlagsFinal -version | grep Usecompressedoops 命令来查看JVM 是否开启了压
缩指针。

/usr/LocatL/mysqt/bin (0.341s )
java -XX:+PrintFLagsFinatL -version | grep UseCompressed0ops

bool                                            := true
{Lp64_product}
java version "1.8.0_301"
Java(TM) SE_ Runtime Environment (buitd 1.8.0_301-b09)
Java Hot9Spot(TM) 64-Bit Server VM (buiLd 25.301-b09，mixed mode)

No. 24195




## 第 25 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

如果压缩指针开启，输出结果中的 bool UseCompressedOops 值为 true。

实例数据了解吗?

了解一些。

实例数据是对象实际的字段值，也就是成员变量的值，按照字段在类中声明的顺序存储。

class ObjectDemo {
int age
String name1

)}

JVM 会对这些数据进行对齐/重排，以提高内存访问速度。
对齐填充了解吗?

由于JVM 的内存模型要求对象的起始地址是 8 字节对齐 (64 位JVM 中) ，因此对象的总大小必须是 8 字节的倍
数。

如果对象头和实例数据的总长度不是 8 的倍数，jVM 会通过填充额外的字节来对齐。
比如说，如果对象头 + 实例数据 = 14 字节，则需要填充 2 个字节，使总长度变为 16 字节。
为什么非要进行 8 字节对齐呢?

因为 CPU 进行内存访问时，一次寻址的指针大小是 8 字节，正好是 L1 缓存行的大小。如果不进行内存对齐，则可
能出现跨缓存行访问，导臻额外的缓存行加载，CPU 的访问效率就会降低。

L1 Cache

Object obj1 = new Object()                    Object obj2 = new Object()

比如说上图中 obj1 占 6 个字节，由于没有对齐，导致这一行缓存中多了 2 个字节 obj2 的数据，当 CPU 访问 obj2
的时候，就会导致缓存行刷新。

也就说，8 字节对齐，是为了效率的提高，以空间换时间的一种方案。

No. 25195




## 第 26 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

32 bit                                                  32 bit

29 bit            0       0       0一一一                            32 bit

: 一个java 对象占用多大内存

一般来说，目前的操作系统都是 64 位的，并且JDK 8 中的压缩指针是默认开启的，因此在 64 位的JVM 上， new
object () 的大小是 16 字节 (12 字节的对象头 + 4 字节的对齐填充) 。

Java 对象实例
64位操作系统
_mark:markOop          占 8 个字节
开启指针压缩占 4 个字节
对象头                    _klass:klassOop          未开启指针压缩占 8 个字节
数组对象专用字段

存储数组对象的长度，占 4个字节

对象实际

instance data

对齐填                             对齐填充仅仅起到占位符的作用

对象头的大小是固定的，在 32 位JVM 上是 8 字节，在 64 位JVM 上是 16 字节; 如果开启了压缩指针，就是 12
字节。

实例数据的大小取决于对象的成员变量和它们的类型。对于 new Object () 来说，由于默认没有成员变量，因此我
们可以认为此时的实例数据大小是 0。

No. 26195




## 第 27 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

假如 MyObject 对象有三个成员变量，分别是 int、long 和 byte 类型，那么它们占用的内存大小分别是4 字节、8
字节和 1 字节。

class MYyObject {

int ay       // 4 字节
long by;      // 8 字节
byte cy      // 1 字节

考虑到对齐填充，MyObject 对象的总大小为 12 (对象头) +4 (aj +8 (b) +1 (c) +7 (填充) =32字节。

用过JOL 查看对象的内存布局吗?
用过。
JOL 是一款分析JVM 对象布局的工具。
第一步，在 pom.xml 中引入JOL 依赖:
<dependency>
<groupId>org.openjdk.jol</groupId>
<artifactId>jol-core</artifactId>

<version>0.9</version>
</dependency>

第二步，使用JOL 编写代码示例:

Public class JOLSample {
public static void main(String[] args) {
// 打印JIVM详细信息 (可选)

System.out .println(VM.current() .details());

// 创建object实例
Object obj = new Object();

// 打印object实例的内存布局

String layout = ClassLayout.parseInstance(obj) .toPrintable() 7
System.out .println(layout) 7

第三步，运行代码，查看输出结果:

No. 27195




## 第 28 页


逆效 JVM篇第二版-让天下所有的面渣都能逆袭

器prolect        6     阅 一全wmrtetam
OFE

public class
pubtic static void main(     [] args) {

CW.   ().
obj =- new object()

0                             tayout                .
example1                           .out        (Layout)

Run。 司 JoLsample

 Running 64-bit Hotspot VW。
1 9 Using compressed oop with 3-bit shift.
4 Using conmpressed ktass with 3-bit shift。
## WARNING | Compressed references base/shifts are guessed by the experiment1
# WARNING | Therefore，computed addresses are just guesses，and ARE NOT RELIABLE.
## WARNING | Make sure to attach Serviceabitity Agent to get the retiabte addresses。
# Objects are 8 bytes atigned。
关 FieLd sizes by fl    4 1，1，2，2，4，4，8，8 [bytes]
## Array eLement sizes: 4，1，1，2，   4，8，8 [bytes]

java.tang.object object internats:
OFFSET SIZE 。 TYPE DESCRIPTION                        vaLuE

(object header)                    61 969 99 68 (609000001 90000000 96900008 96660009) (1)

(object header)                    0 66 99 98 (98000060 00000000 00000009 96660000) (9)

(object header)                    e5 91 9 f8 (11109191 90099901 9990008 11111909) (-134217243)

(toss due to the next object atignment)

6 bytes

Space tosses: 9 bytes internat * 4 bytes externat 。 4 bytes totat

Qpnd 证 @peben
避 suid cmpeu   uly with

可以看到有 OFFSET、SIZE、TYPE DESCRIPTION、VALUE 这几个信息
。 OFFSET: 偏移地址，单位字节;
。 SIZE: 占用的内存大小，单位字节;
。 TYPE DESCRIPTION: 类型描述，其中 object header 为对象头;
。 VALUE: 对应内存中当前存储的值，二进制 32 位;

从上面的结果能看到，对象头是 12 个字节，还有 4 个字节的 padding， new object() 一共 16 个字节。
对象的引用大小了解吗?
推荐阅读:

在 64 位JVM 上，未开启压缩指针时，对象引用占用 8 字节; 开启压缩指针时，对象引用会被压缩到 4 字节。
Hotspeot 虚拟机默认是开启压缩指针的。

No. 28 195




## 第 29 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

hotspot实现的64位虚拟机
对条头
mark word
二| sByte
实例对旬
所                                                       klass pointer
byte 1Byte                                     object header                          上 | w| sByte (开记
short 2Byte                                                                                                        压统类指针后
int 4Byte                                                                                                            占4Byte)
long 8Byte
float 4Byte
double 8Byte                                               实例数据
char2Byte |                          instance data                                                ngihfeld
boolean 1Byte                                                                                              上| RE对
对全引用 8Byte                                                                                                         全7全)
(开启压缩对旬                                      对六填充
指针后占4Byte)                                       padding
(将实例对象填
充至8Byte的莹                              dijia478
数信)

我们来验证一下:

class ReferenceSizeExample {
Private static class ReferenceHolder {
Object referencey

public static void main(String[] args) {
System.out .println(VM.current() .details());

System.out .println(ClassLayout.parseClass(ReferenceHolder.class) .toPrintable());

运行代码，查看输出结

No. 29195




## 第 30 页


逆效 JVM篇第二版-让天下所有的面渣都能逆袭

ohhub ) paicoding ) foum ) test ) javabeter ) km ) 夺
器prolect

import
import

pubtic cl1ass
Private st

】}

public static void main(     [] args) {
CW.      ().      (0O)
(         -        (            .cl1as5)。

:4 Running 64-bit Notspot VM.
4 Using compressed oop with 3-bit shift。
4 Using compressed ktass with 3-bit shift。
革 WARNING | Compressed references base/shifts are guessed by the experiment1
## WARNING | Therefore，computed addresses are just guesses，and ARE NOT RELIABLE.
## WARNING | Make sure to attach Serviceabitity Agent to get the retiabte addresses，
## Objects are 8 bytes atigned.
## Fietd sizes by type: 4，1，1，
#i Array etement sizes: 4，1，1

4 8，8 [bytes]
全 8，8 [bytes]

2，2
2，2，

全
全

com.github.paicoding.forum test.javabetter.jvm.ReferencesizeExampLe$ReferenceHotder object internats:
OFFSET SIZE          PE DESCRIPTION                  VALUE
9 12               (object header)                     MA
12 4 java.tang.0bject ReferenceHotder.reference             MA
Instance size: 16 bytes
Space Losses: 9 bytes internat + 9 bytes externat 。 9 bytes totat

QFnd 证 @pebans 了二      本      506 二         clSle 名 service
shed mi                      25 chwa tf urra 4spaces 以nan 全 二 国

ReferenceHolder.reference 的大小为 4 字节。

1.                        收录的帆软同学 3 java 后端一面的原题: Object a = new object()的大小，对象
引用占多少大小?

2.                 收录的去哪儿面经同学 1 技术二面面试原题: Object 底层的数据结构 (蒙了)

memo: 2025年1月11 日修改到此
10JVM 怎么访问对象的?

主流的方式有两种: 句柄和直接指针。

两种方式的区别在于，句柄是通过一个中间的句柄表来定位对象的，而直接指针则是通过引用直接指向对象的内存
地址。

优点是，对象被移动时只需要修改句柄表中的指针，而不需要修改对象引用本身。

No. 30195




## 第 31 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

句杨池
5                                                 避鸡多实创北站的4 | AT
Short                                               到对象才型堵据的指针
reference                                                                                   2

通过句柄访问对象

在直接指针访问中，引用直接存储对象的内存地址; 对象的实例数据和类型信息都存储在堆中固定的内存区域。
优点是访问速度更快，因为少了一次句柄的寻址操作。缺点是如果对象在内存中移动，引用需要更新为新的地址。

Java                                          Java扒
本地查量春
和                          到对铺娄型的指针
3S6写   一一   对铺实倒数所
reference
double.
floot.

通过直接指针访问对象

HotSpeot 虚拟机主要使用直接指针来进行对象访问。

11.说一下对象有哪几种引用?

四种，分别是强引用、软引用、弱引用和虚引用。

No. 31195




## 第 32 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

强引用是java 中最常见的引用类型。使用 new 关键字赋值的引用就是强引用，只要强引用关联着对象，垃圾收集
器就不会回收这部分对象，即使内存不足。

// str 就是一个强引用
String str = new String("沉默王二") ;

软引用于描述一些非必须对象，通过 SoftReference 类实现。软引用的对象在内存不足时会被回收。

// softRef 就是一个软引用
SoftReference<String> softRef = new SoftReference<>(new String( "沉默王二" ) ) ;

弱引用用于描述一些短生命周期的非必须对象，如 ThreadLocal 中的 Entry，就是通过 WeakReference 类实现
的。弱引用的对象会在下一次垃圾回收时会被回收，不论内存是否充足。

No. 32195




## 第 33 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

static class Entry extends WeakReference<ThreadLocal<?>> {
/xx The value associated with this ThreadLocal。*/
Object valuey

//节点类
Entry(ThreadLocal<?> k，Object v) {
/V/key赋值
super(k) 7
//Vvalue赠值
value = vi

虚引用主要用来跟踪对象被垃圾回收的过程，通过 PhantomReference 类实现。虚引用的对象在任何时候都可能
被回收。

// phantomRef 就是一个虚引用

PhantomReference<String> phantomRef = new PhantomReference<>(new String("沉默王二" ) ，new
Referenceoueue<>()) 7

1. java 面试指南(付费) 收录的京东同学 4 云实习面试原题: 四个引用(强软弱虚)

12.Java 堆的内存分区了解吗?

了解。java 堆被划分为新生代和老年代两个区域。

罗       [因加加
因因加      国

三den                                                 Survivors

新生代     老年代

新生代又被划分为 Eden 空间和两个 Survivor 空间 (From 和To) 。

新创建的对象会被分配到 Eden 空间。当 Eden 区填满时，会触发一次 Minor GC，清除不再使用的对象。存活下
来的对象会从 Eden 区移动到 Survivor 区。

对象在新生代中经历多次 GC 后，如果仍然存活，会被移动到老年代。当老年代内存不足时，会触发 Major GC，
对整个堆进行垃圾回收。

1. Java 面试指南 (付费) 收录的得物面经同学 8 一面面试原题: java 中堆内存怎么组织的

2. java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 怎么来区分对象是属于哪个
代的?

No. 33195




## 第 34 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

13.说一下新生代的区域划分?

新生代的垃圾收集主要采用标记-复制算法，因为新生代的存活对象比较少，每次复制少量的存活对象效率比较
局。
基于这种算法，虚拟机将内存分为一块较大的 Eden 空间和两块较小的 Survivor 空间，每次分配内存只使用 Eden

和其中一块 Survivor。发生垃圾收集时，将 Eden 和 Survivor 中仍然存活的对象一次性复制到另外一块 Survivor
空间上，然后直接清理掉 Eden 和已用过的那块 Survivor 空间。默认 Eden 和 Survivor 的大小比例是 8:1。

新生代   (Young Generdadtion )

14.愉 对象什么时候会进入老年代?

对象通常会在年轻代中分配，随着时间的推移和垃圾收集的进程，某些满足条件的对象会进入到老年代中，如长期
存活的对象。

印 长期存活的对象

进入老年代的对象 “一-一人@@ 大对象

鲍 动态年龄判断

长期存活的对象如何判断?

JVM 会为对象维护一个“年龄计数器，记录对象在新生代中经历 Minor G5C 的次数。每次 GC 未被回收的对象，其
年龄会加1。

当超过一个特定阔值，默认值是 15，就会被认为老对象了，需要重点关照。这个年龄阔值可以通过JVM 参数 -

xxX:MaxTenuringThreshold 来设置。

No. 34195




## 第 35 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

可以通过 jinfo -flag MaxTenuringThreshold $(jps | grep -i nacos | awk '{print $1}') 来查看当前
JVM 的年龄阔值。

D'  oadsVnac     S/bi  0.4335

iinfo -fLag MaxTenuringThreshoLd $(jps | grep -iL nacos | awk “'{print $1}  )

XX:MaxTenuringThreshoLd=15

1如果应用中的对象存活时间较短，可以适当调大这个值，让对象在新生代多待一会儿

2如果对象存活时间较长，可以适当调小这个值，让对象更快进入老年代，减少在新生代的复制次当
大对象如何判断?
大对象是指占用内存较大的对象，如大数组、长字符串等。

int[] array = new int[1000000]7
String str = new String(new char[1000000])?

其大小由JVM 参数 -XX:PretenuresizeThreshold 控制，但在JDK 8 中，默认值为 0，也就是说默认情况下，对
象仅根据 GC 存活的次数来判断是否进入老年代。

[rootGVM-8-2-openctoudos ~]# java -XX:+PrintFLagsFinat -version | grep PretenureSizeThreshotd

Uintx                                         = 0                                  {fproduct}
ppenjdk version "1.8.0_432”"

ppenJDK Runtime Environment (Tencent Kona 8.0.20) (buitd 1.8.0_432-1)
DpenJDK 64-Bit Server VM (Tencent Kona 8.0.20) (buiLd 25.432-b1，mixed mode，sharing)

G1 垃圾收集器中，大对象会直接分配到 HUMONGOUS 区域。当对象大小超过一个 Region 容量的 50% 时，会被
认为是大对象。

G1收集器                                                     空白内存
@author 有臣的肥韦

Region 的大小可以通过JVM 参数 -xx:GlHeapRegionsize 来设置，默认情况下从 1MB 到 32MB 不等，会根据
堆内存大小动态调整。

可以通过 java -xx:+UseGlGC -XX:+PrintGCDetails -version 查看 G1 垃圾收集器的相关信息。

No. 35195




## 第 36 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

java -XX:+UseG16GC -XX:+PrintGCDetaitLs -version

openjdk version "1.8.0_412"

0pen]JDK Runtime Environment Corretto-8.412.08.1 (buitLd 1.8.0_412-b08)

0penJDK 64-Bit Server VM Corretto-8.412.08.1 (buitLd 25.412-b08，mixed mode)

Heap

garbage-first heap ”total 2097152K，used 0K [0x0000000300800000，0x0000000300c010

00，0x0000000a7e800000 )
region size 4096K，1 young (4096K)，0 survivors (0K)

Metaspace     used 2227K，capacity 4480K，committed 4480K，reserved 1056768K
CLass Space   Used 241K，capacity 384K，committed 384K，reserved 1048576K

从结果上来看，我本机上 G1 的堆大小为 256B，Region 的大小为 4MB。
动态年龄判定了解吗?

如果 Survivor 区中所有对象的总大小超过了一定比例，通常是 Survivor 区的一半，那么年龄较小的对象也可能会
被提前晋升到老年代。

这是因为如果年龄较小的对象在 Survivor 区中占用了较大的空间，会导致 Survivor 区中的对象复制次数增多，影
响垃圾回收的效率。

1. java 面试指南 (付费) 收录的阿里面经同学 5 阿里妈妈ja

会进入老年代?

2. java 面试指南 (付费) 收录的京东面经同学 7 java 后端技术一面面试原题: 新生代
的条件

3. java 面试指南 (付费) 收录的拼多多面经

memo: 2025年1月13日修改到此

15.STW 了解吗?
了解。

JVM 进行垃圾回收的过程中，会涉及到对象的移动，为了保证对象引用在移动过程中不被修改，必须暂停所有的用
户线程，像这样的停顿，我们称之为 Stop The world 。简称 STW。

如何暂停线程呢?

JVM 会使用一个名为安全点 (Safe Point) 的机制来确保线程能够被安全地暂停，其过程包括四个步骤:
JVM 发出暂停信号;

线程执行到安全点后，挂起自身并等待垃圾收集完成;

哪些情况下对象

专移到老年代

学 4 技术一面面试原题: 对象什么时候进入老年代

。 垃圾回收器完成 GC 操作;
。 线程恢复执行。
什么是安全点?

安全点是JVM 的一种机制，常用于垃圾回收的 STW 操作，用于让线程在执行到某些特定位置时，可以被安全地暂

品

通常位于方法调用、循环跳转、异常处理等位置，以保证线程暂停时数据的一致性。

No. 36195




## 第 37 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

用个通俗的比喻，老王去拉车，车上的东西很重，老王昧的汗流添背，但是老王不能在上坡或者下坡时休息，只能
在平地上停下来擦擦汗，喝口水。

老王拉车只能在平路休息

推荐大家看看这个HotSpotJVM Deep Dive - Safepoint，对 safe point 有一个比较深入地解释。

JavaThread state machine         四          属国 = Mutable thread state, unsafe

败丽 = Immutable thread state, safe

需国 = Transition thread state

here it has cost the link here
它已经花费了

HotSpot JVM Deep Dive - Safepoint

16.对象一定分配在堆中吗?

不一定。

默认情况下，java 对象是在堆中分配的，但JVM 会进行逃逸分析，来判断对象的生命周期是否只在方法内部，如
果是的话，这个对象可以在栈上分配。

举例来说，下面的代码中，对象 new Person() 的生命周期只在 testSstackallocation 方法内部，因此JVM 会
将这个对象分配在栈上。

No. 37195




## 第 38 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

public void testStackRllocation() {

Person P = new Person();  // 对象可能分配在栈上
P.name = “沉默王二是只狗";

page = 181

System.out .println(p-name )

什么是逃逸分析?
逃逸分析是一种JVM 优化技术，用来分析对象的作用域和生命周期，判断对象是否逃锡出方法或线程。

可以通过分析对象的引用流向，判断对象是否被方法返回、赋值到全局变量、传递到其他线程等，来确定对象是否
逃逸。

如果对象没有逃逸，就可以进行栈上分配、同步消除、标量替换等优化，以提高程序的性能

可以通过 java -xx:+PrintFlagsFinal -version | grep DoEscapeanalysis 来确认JVM 是否开启了逃逸分

java -XX: :+PrintFLagsFinat -version | grep DoEscapeAnaLysis

bool                                          = true
{C2 productT
openjdk version "1.8.0_412"
0penJDK Runtime Environment Corretto-8.412.08.1 (buiLd 1.8.0_412-b08)
0penJDK 64-Bit Server VM Corretto-8.412.08.1 (buiLd 25.412-b08，mixed
mode )

逃逸具体是指什么?
根据对象逃逸的范围，可以分为方法逃逸和线程逃逸。
当对象被方法外部的代码引用，生命周期超出了方法

围，那么对象就必须分配在堆中，由垃圾收集器管理

public Person createPerson() {
return new Person(); // 对象逃逸出方法
】}

比如说 new ?Person() 创建的对象被返回，那么这个对象就逃逸出当前方法了。

No. 38195




## 第 39 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

林逃逸
public static      TeturnStr () [{
User user = new User() ;
User. setId(1) ;
User. setName(“张三) ;
. SetAge (18) ;                           2       -     -
由上                      局部对象user未被外部调用

public static        returnStr () {
User user = new User() ;
user. setId(1) ;
User. setName (“张三 ) ;
user. setAge(18) ;

Teturn User. toString () ;//这里User要实现get，set方法，还要实现toString方法

public static User returnStr () {
User user = new User() ;

user. setId(1) ;                     局部对象user可能会被外部调用

User. setName(“张三”) ;
user. setAge (18) :

Teturn User;//这里User要实现get，set方法

再比如说，对象被另外一个线程引用，生命周期超出了当前线程，那么对象就必须分配在堆中，并且线程之间需要
同步。

public void threadEscapeExample() {

Person P = new Person(); // 对象逃逸到另一个线程
new Thread(() -> {

System.out .println(P) 7
}) .start()7

对象 new Person() 被另外一个线程引用了，发生了线程逃逸。
逃逸分析会带来什么好处?
主要有三个。

第一，如果确定一个对象不会逃逸，那么就可以考虑栈上分配，对象占用的内存随着栈帧出栈后销毁，这样一来，
垃圾收集的压力就降低很多。

第二，线程同步需要加锁，加锁就要占用系统资源，如果逃逸分析能够确定一个对象不会逃逸出线程，那么这个对
象就不用加锁，从而减少线程同步的开销。

No. 39195




## 第 40 页


面洁逆袭 JVM篇第二版-让天下所有的面洁都能地袭
第三，如果对象的字段在方法中独立使用，JVM 可以将对象分解为标量变量，避免对象分配。

Public void scalarReplacementExample() {
Point P = new Point(1，2) 17
System.out.println(p.getX() + p.getY())7

如果 Point 对象未逃逸，JVM 可以优化为:

int y
System.out.println(x + Y) 7

1. Java 面试指南 (付费) 收录的收钱吧面经同学 1 Java 后端一面面试原题: 所有对象都在堆上对不对?

17.内存溢出和内存泄漏了解吗?

内存溢出，俗称 OOM，是指当程序请求分配内存时，由于没有足够的内存空间，从而抛出 OutOfMemoryError。

List<String> list = new RrrayList<>() 1
while (true) {

list.add("OutOfMemory".repeat(1000)); // 无限增加内存
}

可能是因为堆、元空间、栈或直接内存不足导致的。可以通过优化内存配置、减少对象分配来解决。

内存泄漏是指程序在使用完内存后，未能及时释放，导致占用的内存无法再被使用。随着时间的推移，内存泄漏会
导致可用内存逐潮减少，最终导致内存溢出。

内存泄漏通常是因为长期存活的对象持有短期存活对象的引用，又没有及时释放，从而导致短期存活对象无法被回
收而导致的。

class MemoryLeakExample {
Private static List<Object> staticList = new RrrayList<>()7
public void addobject() {
staticList.add(new Object()); // 对象不会被回收
}

用一个比较有味道的比喻来形容就是，内存溢出是排队去蹲坑，发现没填了; 内存泄漏，就是有人占着茅坑不拉
屎，导致坑位不够用。

No. 40195




## 第 41 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

正常情况                 内存泄漏                   内存溢出

全
四

力

罗

熏
Se
四

goO9o09

入
国 鲍
入

图|

让

1. java面试指南 (付费) 收录的京东面经同学 1 java 技术一面面试原题: 说说 OOM 的原因
2. java 面试指南 (付费) 收录的快手面经同学 1 部门主站技术部面试原题: 了解 OOM 吗?

18.能手写内存溢出的例子吗?
可以。

我就拿最常见的堆内存溢出来完成吧，堆内存溢出通常是因为创建了大量的对象，且长时间无法被垃圾收集器回
收，导致的。

class HeapSpaceErrorGenerator {
public static void main(String[] args) {
// 第一步，创建一个大的容器
List<byte[]> bigobjects = new RrrayList<>() 7
try 1{
// 第二步，循环写入数据
while (true) {
// 第三步，创建一个大对象，一个大约 10M 的数组
byte[] bigobject = new byte[10 * 1024 * 1024]7
// 第四步，将大对象添加到容器中
bigobjects.add(bigobject) 7
}
} catch (OutOfMemoryError e) {
System.out .println("OutOfMemoryETLOF 发生在 "+ bigobjects.size() + ”对象后" ) ;

throw e7

很快就会发生内存溢出。
这就相当于一个房子里，不断堆积不能被回收的杂物，那么房子很快就会被堆满了。
也可以通过 VM 参数设置堆内存大小为 -xmx128M ，然后运行程序，出现的内存溢出的时间会更快。

No. 41195




## 第 42 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

                                               Name: 。 HeapSpaceErrorGenerator                                                       Store as project fle
口Application

Run on: 会Local machine              Manage targets..
HeapSpaceErrorGenerator

Spring Boot                   Build and run                                             Modify options

java 8                                            paicoding-web
-Xmx128H

com.github.paicoding.forum.test.jal              ceErrorGenerator

Working directory:          /Users/twanger/Documents/Github/paicoding

Environment variables:

Open run/debug tool window when started

Code Coverage

Packages and classes to include in coverage data

Edit configuration templates.…                                  十

可以看到，堆内存溢出发生在 11 个对象后。

Out0ofMemoryError 发生在 11

ErrorGenerator

Process finished with exit code

1.             收录的京东面经同学 1 Java 技术一面面试原题: 说说 OOM 的局

2.             收录的快手面经同学 1 部门主站技术部面试原题: java 哪些内存区域会发生
OOM? 为什么?

memo: 2025年1月14日修改到此

19.内存泄漏可能由哪些原因导致呢?
比如说:

中、静态的集合中添加的对象越来越多，但却没有及时清理; 静态变量的生命周期与应用程序相同，如果静态变量
持有对象的引用，这些对象将无法被 GC 回收。

No. 42195




## 第 43 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

class OOM {
static List list = new RrrayList() 7

Public void oomTests(){
Object obj = new Object();

1list.add(obj);
}

@、单例模式下对象持有的外部引用无法及时释放; 单例对象在整个应用程序的生命周期中存活，如果单例对象持
有其他对象的引用，这些对象将无法被回收。

class Singleton {
Private static final Singleton INSTANCE = new Singleton() 7
Private List<Object> objects = new RrrayList<>() 17

public static Singleton getInstance() {
return INSTRNCE7

没有及时关闭;

@@、数据库、IO、Socket 等连接;

try {
Connection conn = null;
Class.forName("com.mysql.jdbc.Driver") 7
conn = DriverManager.getConnection("url"，""，"");
Statement stmt = conn.createStatement()7
ResultSet rs = stmt.executeOuery("....");

) catch (Exception e) {
)}finally {
//不关闭连接
@@、    ThreadLocal 的引用未被清理，线程退出后仍然持有对象引用; 在线程执行完后，要调用 ThreadLocal

的 remove 方法进行清理。

ThreadLocal<Object> threadLocal = new ThreadLocal<>();
threadLocal.set(new Object()); // 未清理

20.有没有处理过内存泄漏问题?
推荐阅读:

1. 二次内

2. JVM 性能监控     命令行

No. 43195




## 第 44 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

3. JVM 性能监控工具之可视化篇
有。
当时在做技术派项目的时候，由于 ThreadLocal 没有及时清理导致出现了内存泄漏问题。
我用可视化的监控工具 VisualVM，配合JDK 自带的 jstack 等命令行工具进行了排查。
大致的过程我回想了一下，主要有 7 个步骤:

第一步，使用 jps -1 查看运行的java 进程 ID。

[ rootGVM-0-5-tencentos ~]## jps -1L
391195 palicoding-web-0.0.1-SNAPSH0T. jar
4170448 Sun.tooLs,.jps.Jps

第二步，使用top -p [pid] 查看进程使用CPU 和内存占用情况。

top - 09:00:43 up 270 days，21:29， 1 user， Load average: 0.01，0.02，0.00
Tasks:   1 totaL， 6 running，   1 stLeeping， 8 stopped， 98 zombie

s%Cpu(s): 0.0 us， 0.0 Sy， 60.0 ni,100.0 id， 0.0 wa， 0.0 hi， 0.0 Si， 0.0 st
MiB Mem : 3670.2 totalt   210.3 free， 2429.9 used，   1030.0 buff/cache
MiB Swap:      0.6 totat      0.6 free，     0.0 used,    753.4 avaitL Mem

PID USER    PR NI   VIRT   RES   SHR S %CPU EM   TIME+ COMMAND
391195 admin    20 6 4281324 1.0g9 16052 S 0.0 27.9 19:53.58 java

第三步，使用 top -Hp [pid] 查看进程下的所有线程占用 CPU 和内存情况。

No. 44195




## 第 45 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

top - 09:01:55 up 276 days，21:30， 1 user， Load average: 0.00，0.01，
Threads: 52 totaL， 8 running， 52 stLeeping， 8 stopped， 8 zombie
%Cpu(sS): 0.0 us，3.3 sy， 6.0 ni，96.7 id， 6.0 wa， 0.0 hi， 0.0 si

0.00

0.0 st

MiB Mem :   3676.2 totalt    209.3 free，   2430.7 used，   1030.2 buff/cache

MiB Swap:     8.0 total     60.0 free，     .0 used .    752.6 avait Mem
PID USER     PR_ NI    VIRT    RES    SHR S %CPU 嗣IEM    TIME+ COMMAND

391195 admin    20 0 4281324 1.0g9 16052S 0.0 27.9 0:00.00 java

391196 admin    20 0 4281324 1.0g 16052S 0.0 27.9 0:13.78 java

391197 admin    20 0 4281324 1.0g 16052S 0.0 27.9 0:06.05 GC task thread#
391198 admin    20 0 4281324 1.0g9 16052S 0.0 27.9 0:06.12 GC task thread#
391199 admin    20 0 4281324 1.0g 16052S 0.0 27.9 0:20.28 VM Thread
391200 admin    20 0 4281324 1.0g 16052S 0.0 27.9 0:00.03 Reference HandL
391201 admin    20 0 4281324 1.0g9 16052S 0.0 27.9 0:00.04 FinaLizer
391202 admin    20 0 4281324 1.0g9 16052S 0.0 27.9 0:00.00 Signal Dispatch
391203 admin    20 0 4281324 1.0g 16052 S 0.0 27.9 1:53.88 C2 CompiterThre
391204 admin    20 0 4281324 1.0g9 16052 S 0.0 27.9 0:21.92 C1 CompilerThre
391205 admin    20 0 4281324 1.0g 16052 5 0.0 27.9 0:00.00 Service Thread
391206 admin    20 0 4281324 1.0g 16052S 0.0 27.9 2:09.43 VM Periodic Tas
391281 admin    20 0 4281324 1.0g9 16052 S 0.0 27.9 0:06.82 mysqtL-cj-abando
391292 admin    20 0 4281324 1.0g9 16052 S 0.0 27.9 0:08.83 pooL-1-thread-1
391293 admin    20 0 4281324 1.0g9 16052 5S 0.0 27.9 0:08.62 I/0 dispatcher
391294 admin    20 0 4281324 1.0g9 16052S 0.0 27.9 0:08.87 I/0 dispatcher
391295 admin    20 0 4281324 1.0q 16052S 0.0 27.9 0:18.74 CataLina-utitLit

第四步，抓取线程栈: jstack -F 29452 > 29452.txt ，可以多抓几次做个对比。
29452 为 pid，顺带作为文件名。

[rootGVM-0-5-tencentos Logs]# jstack -F 391197 >
[rootGVM-0-5-tencentos Logs]# LSs
391197.txt arthas arthas-cache

看看有没有线程死锁、死循环或长时间等待这些问题。

No. 45195

391197.tXxt




## 第 46 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

有taching te process ID 391197，ptease wait,，
Debugger attached successfutty。

Server compiter detected。

JW version is 25.382-b05

peadtock Detection:

No deadtLocks found.

Thread 4180746: (state = BLOCKED)

- sunmisc.Unsafe.park(bootean，tLong) @bci=9 (Compited frame; information may be imprecise)

- java.utit,concurrent,tocks.LockSsupport.park(java.tang.0bject) ebci=14，tine=175 (Compited frame)

- java.utit.concurrent.SynchronousQueue$TransferStack.awaitFutfitt(java.utit.concurrent.SynchronousQueue$TransferS
e，bootean，tong) ebci=144，tine=458 (Compited frame)

- java.utit.concurrent.Synchronousqueue$TransferStack.transfer(java.tang.0bject，bootean，tong) ebci=192，Line=362
d frame)

- java.utit,concurrent.SynchronousQueue.take() @bci=7，tLine=924 (Compited frame)

- java.utit,concurrent.ThreadPootExecutor.getTask() ebci=149，tine=1074 (Compited frame)

- java,utit,concurrent,ThreadPootExecutor.runWorker(java,utit,concurrent,ThreadPootExecutor$worker) ebci=26，tine=
pited frame)

- java.utit.concurrent.ThreadPootExecutor4worker.run() ebci=5，tine=624 (Compited frame)

- javavlang,Thread.run() ebci=11，Line=756 (Compited frame)

Thread 4186745: (state = BLOCKED)
- sunmisc.Unsafe.park(bootean，tLong) @bci=9 (Compited frame; information may be imprecise)
- java.utit,concurrent,tocks.LockSupport.park(java.tang,0bject) @bci=14，tine=175 (Compited frame)

第五步，可以使用 jstat -gcutil [pid] 5000 10 每隔 5 秒输出 GC 信息，输出 10 次，查看 YGC 和 Full GC

次数。

[rootGVM-0-5-tencentos Logs]# jstat -gcutiL 391195 5000 10
5S0    5S1    E     0     M    CCS5   YGC    YGCT   FGC   FGCT    GCT
0.00 58.10 11.39 20.53 92.52 89.51   981   7.433    4   0.789   8.222
0.00 58.10 11.40 20.53 92.52 89.51   981   7.433    4   0.789   8.222
0.00 58.10 11.40 20.53 92.52 89.51   981.   7.433    4   0.789   8.222

通常会出现 YGC 不增加或增加缓慢，而 Full GC 增加很快。
或使用 jstat -gccause [pid] 5000 输出 GC 摘要信息。

[rootGVM-0-5-tencentos Logs]# jstat -gccause 391195 5000
5S0     5S1     E      0      NM     CCS    YGC     YGCT    FGC    FGCT     GCT    LGCC                GCC
0.00 58.10 34.32 20.53 92.52 89.51   981   7.433    4   0.789   8.222 ALLocation FaiLure ”No 6GC
0.00 58.10 34.33 20.53 92.52 89.51   981   7.433    4   0.789   8.222 ALLocation FaiLure ”No GC
0.00 58.10 34.33 20.53 92.52 89.51   981   7.433    4   9.789   8.222 ALLocation Faiture ”No GC

或使用 jmap -heap [pid] 查看堆的摘要信息，关注老年代内存使用是否达到阔值，若达到阀值就会执行 Full
GC。

No. 46195




## 第 47 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

^C[rootGVM-0-5-tencentos Logs]# jmap -heap 391195
Attaching to process ID 391195，ptLease wait,. . .
Debugger attached successfuLtLy，

Server compiter detected

JVM version is 25.382-b05

using thread-LocaL object aLLocation，
ParatLtLetL GC with 2 thread(s)

Heap Configuration:

MinHeapFreeRatio         = 0

MaxHeapFreeRatio         = 100

MaxHeapSize              = 1610612736 (1536.0MB)
NewSize                 = 268435456 (256.0MB)
MaxNewSize               = 268435456 (256.0MB)
0LdSize                              = 1342177280 (1280.0MB)
NewRatio                  = 2

SurvivorRatio            = 8

MetaspaceSize            = 21807104 (20.796875MB)

CompressedCLassSpaceSize = 1073741824 (1024.0MB)

MaxMetaspaceSize         = 17592186044415 MB
G1HeapRegionSize         = 0 (0.0MB)
Heap Usage:

PS Young Generation
如果发现 Full ec 次数太多，就很大概率存在内存泄漏了。
第六步，生成 dump 文件，然后借助可视化工具分析哪个对象非常多，基本就能定位到问题根源了。

执行命令 jmap -dump:format=b,file=heap.hprof 10025 会输出进程 10025 的堆快照信息，保存到文件
heap.hprof 中。

No. 47195




## 第 48 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

ocuments/GitHub/HeLLowortLd git:(master) +127 (0.318s )

/Library/Java/JavavVirtuaLMachines/jdk-11.0.8.jdk/Contents/Home/bin/
jmap -dump:format=b,fiLe=heap.hprof 10025

Heap dump fiLe created

w/Documents/GitHub/HeLLowortLd git:(master) +127 (0.083s )
Ls

ExampLe.cLass HeLLowortd.imt JDK11.java     JDK8. java      out
ExamptLe.java “ JDK11.cLass    JDK8 .ctLass     heap .hprof     Src

第七步，使用图形化工具分析，如jJDK 自带的 VisualVM，从菜单 > 文件 > 装入 dump 文件。

eee                                                   VisualvM 217
记      鲁名智和佑和企
Applications X                                加| starspage | 所 com okhub paicodingforumweb,QuickFforumApplication (pid 28966) x                        ED 加 口)
局 Local                                      国overview 了鸯Monitor 司Threads 只Sampler 加profller 图[heapdump]下午133:56 x
了vasuavM
扫 me IDEA pid 63831)               C com.github.paicoding.forum.web.QuickForumApplication (pid 28966)
上息LocalApplcaton pid 768)        Ri                                         下
-on .orhub.paicodine.forum.web,QuickForumy

图 heapdump] 下午1:33:56

自 orgjetbrainsjpsemdline Launcher pid 3909| Profile      所员      和晶wy 目)oe       国o       人Sop
二Remote                                     Status:。 profiling running (2,165 methods instrumented)
功 coredumps
僵JFR Snapshots                                     Profiling results                                              CPU settings ，Memory settings | JDBC settings        X
图 snapshots                                                 加          区            外国民 图
                 ToalTime CPU        四
22.986 ms               7.27 ms
ge
710 ms               65.4ms
户       70.8 ms               65.3 ms
0.125 ms           0.115 ms
0.060 ms             0.057 ms
0.012 ms            0.012 ms

然后在结果观察内存占用最多的对象，找到内存泄漏的源头。
1. java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题

内存泄露
java 哪些内存区域会发生

OOM?

3. java 面试指南 (付费) 收录的美团面经
21.有没有处理过内存溢出问题?
有。

当时在做技术派的时候，由于上传的文件过大，没有正确处理，导致一下子撑爆了内存，程序直接崩溃
我记得是通过导出堆转储文件进行分析发现的。
一步，使用jmap 命令手动生成 Heap Dump 文件:

No. 48195




## 第 49 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

jmap -dump:format=b,file=heap.hprof <pid>

然后使用 MAT、jJProfiler 等工具进行分析，查看内存中的对象占用情况。
一般来说:
如果生产环境的内存还有很多空余，可以适当增大堆内存大小来解决，例如 -xmx4g 参数。
或者检查代码中是否存在内存泄漏，如未关闭的资源、长生命周期的对象等。
之后，在本地进行压力测试，模拟高负载情况下的内存表现，确保修改有效，且没有引入新的问题。
1. Java 面试指南(付费) 收录的华为面经同学 9 java 通用软件开发一面面试原题: 如何排查OOM?
2. Java 面试指南 (付费) 收录的荣溜面经同学 4 面试原题: 有没遇到内存泄露，溢出的情况，怎么发生和
处理的?

22.什么情况下会发生栈溢出? (补充)
2024年10 月 16 日增补
栈溢出发生在程序调用栈的深度超过JVM 允许的最大深度时。
栈溢出的本质是因为线程的栈空间不足，导致无法再为新的栈帧分配内存。

二哥的 JVM 进阶之路      当前线程   线程1   线程2
局部变量表               当前栈帧    栈帧 N    栈帧 N
操作数栈   |
站                栈帧2    栈帧2    栈帧 2
方法返回链接

栈帧1     栈帧1     栈帧1

当一个方法被调用时，JVM 会在栈中分配一个栈帧，用于存储该方法的执行信息。如果方法调用钳套太深，栈帧不
打压入栈中，最终会导致栈空间耗尽，抛出 StackOverflowError。

最常见的栈溢出场景就是递归调用，尤其是没有正确的终止条件下，会导致递归无限进行。

革

No. 49195




## 第 50 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

class StackOverflowExample {
public static void recursiveMethod() {
// 没有终止条件的递归调用
recursiveMethod() 7

】}

public static void main(String[] args) {
recursiveMethod();  // 导致栈溢出
}

另外，如果方法中定义了特别大的局部变量，栈帧会变得很大，导致栈空间更容易耗尽。

public class LargeLocalVariables {
public static void method() {
int[] largearray = new int[1000000];  // 大量局部变量
method();  // 递归调用
}

public static void main(String[] args) {
method(); /人/ 导致栈溢出
}

1. Java 面试指南【付费) 收录的 OPPO 面经同学 1 面试原题: 什么情况下会发生栈滋出?
三、垃圾收集
23.二讲讲JVM 的垃圾回收机制 (补充)

深入理解JVM 的垃圾回收机制
垃圾回收就是对内存堆中已经死亡的或者长时间没有使用的对象进行清除或回收。
JVM 在做 GC 之前，会先搞清楚什么是垃圾，什么不是垃圾，通常会通过可达性分析算法来判断对象是否存活。

本题是增补的内容，by 2024年 03 月 09 日;

No. 50195




## 第 51 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

对象2

对象5

GC Root
沉默王二是个沙雕从
时
对象1

|             |

对象3                        对象6
里

对象4

对象7

在确定了哪些垃圾可以被回收后，垃圾收集器 (如 CMS、G1、ZGC) 要做的事情就是进行垃圾回收，可以采用标
记清除算法、复制算法、标记整理算法、分代收集算法等。

技术派项目使用的JDK 8，采用的是 CMS 垃圾收集器。

java

:+UseConcMarkSweepGC \
:+UseParNewGC \
:CMSInitiatingOccupancyFraction=75 \
:+UseCMSInitiatingOccupancyOn1y \

-jar your-application.jar

垃圾回收的过程是什么?

java 的垃圾回收过程主要分为标记存活对象、清除无用对象、以及内存压缩/整理三个阶段。不同的垃圾回收器在
执行这些步骤时会采用不同的策略和算法。

六Un > ww

道吗?

java 面试指南(付费) 收录的腾讯面经同学 26 暑期实习微信支付面试原题: JVM 垃圾删除
Java 面试指南(付费) 收录的得物面经同学 8 一面面试原题: java 中垃圾回收的原理

java 面试指南(付费) 收录的快手同学 2 一面面试原题: JVM了解吗? 内存回收机制说一下?
Java 面试指南(付费) 收录的 OPPO 面经同学 1 面试原题: 垃圾回收的过程是什么?

java 面试指南(付费) 收录的vivo 面经同学 10 技术一面面试原题:

No. 51195

.java 面试指南 (付费) 收录的华为 OD 技术一面遇到的一道原题。
java 面试指南(付费) 收录的美团面经同学 2 java 后端技术一面面试原题:

说一下GC，有哪些方法

了解 GC 吗? 不可达判断知




## 第 52 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

8. java 面试指南 (付费) 收录的荣耀面经同学 4 面试原题: 对垃圾回收的理解?

9. java 面试指南 (付费) 收录的字节跳动同学 17 后端技术面试原题: 垃圾回收机制 为什么要学jvm 内存
泄漏场景

10. java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: GC? 怎么样去识别垃圾?
11. java 面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题: 说说你对GC的了解?
12. java 面试指南 (付费) 收录的腾讯面经同学 29 java 后端一面原题: JVM垃圾回收机制?

24.过如何判断对象仍然存活?
java 通过可达性分析算法来判断一个对象是否还存活。
通过一组名为“GC Roots' 的根对象，进行递归扫描，无法从根对象到达的对象就是"垃起"，可以被回收。

抱2
2二

二] [荆

思] 剂这可回收的对多

GC Root Set

这也是 G1、CMS 等主流垃圾收集器使用的主要算法。
什么是引用计数法?
每个对象有一个引用计数器，记录引用它的次数。当计数器为零时，对象可以被回收。

No. 52195




## 第 53 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

引用计数法无法解决循环引用的问题。例如，两个对象互相引用，但不再被其他对象引用，它们的引用计数都不为
零，因此不会被回收。

做可达性分析的时候，应该有哪些前置性的操作?
在进行垃圾回收之前，JVM 会暂停所有正在执行的应用线程。

这是因为可达性分析过程必须确保在执行分析时，内存中的对象关系不会被应用线程修改。如果不暂停应用线程，
可能会出现对象引用的改变，导致垃圾回收过程中判断对象是否可达的结果不一致，从而引发严重的内存错误或数
据丢失。

1. Java 面试指南 (付费) 收录的京东面经同学 7 京东到家面试原题: 如何判断一个对象是否可以回收

2. java 面试指南(付费) 收录的快手同学 2 一面面试原题: 做可达性分析的时候，应该有哪些前置性的操
作?

3. java 面试指南 (付费) 收录的京东面经同学 9 面试原题: 什么样的对象算作垃圾对象

4. java 面试指南 (付费) 收录的同学 D 小米一面原题: gc中判断对象可回收的方式有哪些

25.jJava 中可作为 GC Roots 的引用有哪几种?

是一切引用链的源头。在java 中，GC

Roots 包括以下几种:

。 虚拟机栈中的引用 (方法的参数、局部变量等)
。 本地方法栈中JNI 的引用

         恋量
。 类静态变量

。 运行时常量池中的常量 (String 或 Class 类型)

No. 53195




## 第 54 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

运行时数据区
堆
Java 虚拟机栈            本地方法栈
字符串常量池                                                           程序计数器
三哥 JVM进阶之路
元空间
运行时常量池

说说虚拟机栈中的引用?
来看下面这段代码:

public class StackReference {
public void greet() {

Object localVar = new Object(); // 这里的 localVar 是一个局部变量，存在于虚拟机栈中
System.out .println(LlocalVar.toString())7

】}

public static void main(String[] args) {
new StackReference() .greet() 7

】}

在 greet 方法中，localVar 是一个局部变量，存在于虚拟机栈中，可以被认为是 GC Roots。
在 greet 方法执行期间，localVar 引用的对象是活跃的，因为它是从 GC Roots 可达的。

当 greet 方法执行完毕后，localVar 的作用域结束，localVar 引用的 Object 对象不再由任何 GC Roots 引用 (假设

没有其他引用指向这个对象) ，因此它将有资格作为垃圾被回收掉 僚。
说说本地方法栈中JNI 的引用?
java 通过JINI 提供了一种机制，允许Java 代码调用本地代码 (通常是 5 或 C++ 编写的代码) 。

当调用 java 方法时，虚拟机会创建一个栈帧并压入虚拟机栈，而当它调用本地方法时，虚拟机会通过动态链接直

接调用指定的本地方法。

No. 54195




## 第 55 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

当前线程

当前栈祯

局部变量表

动态链接

方法返回地址

         地方法

栈帧 1

JNI 引用是在 Java 本地接口代码中创建的引用，这些引用可以指向 java 堆中的对象。

// 假设的JNI方法

Public native void nativeMethod();

// 假设在c/c++中实现的本地方法

As
* Class:    NativeExample

* Method:    nativeMethod

* Signature: ()V

JNIEXPORT void JNICRALL Java_NativeExample_nativeMethod(JNIEnv *enVv，jobject thisobj) {

jobject localRef = (*env)->NewObject(env，...); // 在本地方法栈中创建INI引用
// localRef 引用的Java对象在本地方法执行期间是活跃的

在本地代码中，localRef 是对Java 对象的一个JNI 引用，它在本地方法执行期间保持 java 对象活跃，可以被认为

是 GC Roots。

一旦JNI 方法执行完毕，除非这个引用是全局的，否则它指向的对象将会被作为垃圾回收掉 (假设没有其他地方再
引用这个对象) 。

说说类静态变量?
来看下面这段代码:

No. 55195




## 第 56 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

public class StaticFieldReference {
private static Object staticVar = new Object(); // 类静态变量

public static void main(String[] args) {
System.out .Println(staticVar.toString())7
}

StaticFieldReference 类中的 staticVar 引用了一个 Object 对象，这个引用存储在元空间，可以被认为是 GC
Roots 。

只要 StaticFieldReference 类未被卸载，staticVar 引用的对象都不会被垃圾回收。如果 StaticFieldReference 类被
卸载 (这通常发生在其类加载器被垃圾回收时) ，那么 staticVar 引用的对象也将有资格被垃圾回收 (如果没有其
他引用指向这个对象) 。

说运行时常量池中的常量?
来看这段代码:
class ConstantPoolReference {

public static final String CONSTRNT_STRING = "Hello，World"; // 常量，存在于运行时常量池中
Public static final Class<?> CONSTANT_ CLASS = Object.class) // 类类型常量

public static void main(String[] args) {
System.out .Println(CONSTRNT_STRING)
System.out .Println(CONSTRNT_CLASS .getName() ) 7

在 ConstantPoolReference 中，CONSTANT_STRING 和 CONSTANT_CLASS 作为常量存储在运行时常量池。它们
可以用来作为 GC Roots。

这些常量引用的对象 (字符串"Hello, World"和 Object.class 类对象) 在常量池中，只要包含这些常
ConstantPoolReference 类未被卸载，这些对象就不会被垃圾回收。

1. Java 面试指南 (付费) 收录的帆软同学 3 java 后端一面的原题: 哪些对象可以作为 GC Roots
2. Java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: GC Root?
3. java 面试指南(付费) 收录的同学 D 小米一面原题: 那些对象可以作为gc root

26.finalize()方法了解吗?

垃圾回收就是古代的秋后问斩， finalize() 就是刀下留人，在人犯被处决之前，还要做最后一次审计，青天大老
爷会看看有没有什么铭情，需不需要刀下留

的

直

No. 56195




## 第 57 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

垃圾收集                                   finalize

如果对象在进行可达性分析后发现没有与 GC Roots 相连接的引用链，那它将会被第一次标记，随后进行一次得
选。

筛选的条件是对象是否有必要执行 finalize() 方法。

如果对象在 finalize() 中成功拯救自己一一只要重新与引用链上的任何一个对象建立关联即可。

警如把自己 (this 关键字) 赋值给某个类变量或者对象的成员变量，那在第二次标记时它就"逃过一劫*，但是如果
没有抓住这个机会，那么对象就真的要被回收了 。

27.二垃圾收集算法了解吗?
垃圾收集算法主要有三种，分别是标记-清除算法、标记-复制算法和标记-整理算法。
说说标记-清除算法?
标记-清除 算法分为两个阶段:
。 标记: 标记所有需要回收的对象
。 清除: 回收所有被标记的对象

No. 57195




## 第 58 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

标记-清除算法

回收前

加加 国国 二 国国
回收后
四      国

优点是实现简单，缺点是回收过程中会产生内存碎片。

说说标记-复制算法?

标记-复制 算法可以解决标记-清除算法的内存碎片问题，因为它将内存空间划分为两块，每次只使用其中一块。当
这一块的内存用完了，就将还存活着的对象复制到另外一块上面，然后清理掉这一块。

标记-复制算法

回收后                             -一

缺点是浪费了一半的内存空间。
说说标记-整理算法?

No. 58195




## 第 59 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

标记-整理 算法是标记-清除复制算法的升级版，它不再划分内存空间，而是将存活的对象向内存的一端移动，然后
清理边界以外的内存。

标记-整理算法
回收后
缺点是移动对象的成本比较高。
说说分代收集算法?

分代收集 算法是目前主流的垃圾收集算法，它根据对象存活周期的不同将内存划分为几块，一般分为新生代和老年
代。

Survivor 区
eden              S0            S1                            Tenured
新生代                                     老年代

新生代用复制算法，因为大部分对象生命周期短。老年代用标记-整理算法，因为对象存活率较高。
为什么要用分代收集呢?
分代收集算法的核心思想是根据对象的生命周期优化垃圾回收。

No. 59195




## 第 60 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

新生代的对象生命周期短，使用复制算法可以快速回收。老年代的对象生命周期长，使用标记-整理算法可以减少
移动对象的成本。
标记复制的标记过程和复制过程会不会停顿?
在标记-复制算法 中，标记阶段和复制阶段都会触发STW。
。 标记阶段停顿是为了保证对象的引用关系不被修改。
。 复制阶段停顿是防止对象在复制过程中被修改。
1. Java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: 垃圾回收算法了解多

少
2. Java 面试指南 (付费) 收录的小米面经同学 F 面试原题: 垃圾回收的算法及详细介绍

3. java 面试指南 (付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: 回收的方法? 分代收集算法
里面具体是怎么回收的? 为什么要用分代收集呢?

4. Java 面试指南 (付费) 收录的百度同学 4 面试原题: Gc 算法有哪些?

5. Java 面试指南 (付费) 收录的京东面经同学 9 面试原题: 问了垃圾回收算法，针对问了每个算法的优缺
点

6. Java 面试指南《付费) 收录的同学 D 小米一面原题: gc垃圾回收算法有哪些
28.Minor GC、Major GC、Mixed GC、Full GC 都是什么意思?

Minor GC 也称为 Young GC，是指发生在年轻代的垃圾收集。年轻代包含 Eden 区以及两个 Survivor 区。

Survivor 区
eden            S0           S1                         Tenured
己                   T                                           T
新生代                                         老年代

Major GC 也称为 Old GC，主要指的是发生在老年代的垃圾收集。是 CMS 的特有行为。

Mixed GC 是 G1 垃圾收集器特有的一种 GC 类型，它在一次 GC 中同时清理年轻代和部分老年代。

Full GC 是最彻底的垃圾收集，涉及整个java 堆和方法区。它是最耗时的 GC，通常在JVM 压力很大时发生。
FULL gc怎么去清理的?

Full GC 会从 GC Root 出发，标记所有可达对象。新生代使用复制算法，清空 Eden 区。老年代使用标记-整理算
法，回收对象并消除碎片。

No. 60195




## 第 61 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

停顿时间较长，会影响系统响应性能。

1. Java 面试指南 (付费)_收录的阿里面经同学 5 阿里妈妈 java 后端技术一面面试原题: full gc和young
gc 的区别

2. java 面试指南(付费) 收录的腾讯面经同学 27 云后台技术一面面试原题: FULL 8g5怎么去清理的?

29.Young GC 什么时候触发?
如果 Eden 区没有足够的空间时，就会触发 Young GC 来清理新生代。
1. Java 面试指南付费) 收录的百度同学 4 面试原题: 什么时候会触发 GC?

30.什么时候会触发 Full GC?

在进行 Young GC 的时候，如果发现 老年代可用的连续内存空间 < 新生代历次 Young GC 后升入老年代的对象总和的
平均大小 ，说明本次 Young G5C 后升入老年代的对象大小，可能超过了老年代当前可用的内存空间，就会触发 Full
GC。

执行 Young GC 后老年代没有足够的内存空间存放转入的对象，会立即触发一次 Full GC。
System.gc() 、jmap -dump 等命令会触发 full gc。
空间分配担保是什么?

空间分配担保是指在进行 Minor GC 前，JVM 会确保老年代有足够的空间存放从新生代晋升的对象。如果老年代空
间不足，可能会触发 Full GC。

1. java 面试指南 (付费) 收录的快手同学 4 一面原题: 如何判断死亡对象” GC Roots有哪些? 空间分配
担保是什么?

31.二知道哪些垃圾收集器?
推荐阅读: 深入理解JVM 的垃圾收集器: CMSs、G1、ZGC

JVM 的垃圾收集器主要分为两大类: 分代收集器和分区收集器，分代收集器的代表是 CMS，分区收集器的代表是
G1 和ZGC。

No. 61195




## 第 62 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

新生代
                                                                          Prallel

Serial                              ParNew                        2

标刀-清除
[ ] 标妈-复吉                                                                                                                                               了器
PN
JDK9
局光                                                                   G1
Prallel old
CMS                             7
Serial old
老年代

CMS 是第一个关注 GC 停顿时间的垃圾收集器， JDK 1.5 时引入，JDK9 被标记弃用，JDK14 被移除。
G1在JDK1.7时引入,在JDK 9 时取代 CMS 成为了默认的垃圾收集器。

ZGC是JDK11 推出的一款低延迟垃圾收集器，适用于大内存低延迟服务的内存管理和回收，在 128G 的大堆下，
最大停顿时间才 1.68 ms，性能远胜于 G1 和 CMS。

说说 Serial 收集器?
Serial 收集器是最基础、历史最悠久的收集器。

如同它的名字 (串行) ，它是一个单线程工作的收集器，使用一个处理器或一条收集线程去完成垃圾收集工作。
且进行垃圾收集时，必须暂停其他所有工作线程，直到垃圾收集结束一一这就是所谓的"stop The World"。

Serial/Serial Old 收集器的运行过程如图:

Serial/Selial Old收集器运行示意图

TO   IOIOGGOZ

和4 CA

CPUo EDDDZDZZDZZZ                                                                                                          GAN

GC和线程“下
交手 20NNNNOONNNNNAN

儿
自

人一

CPU1 二 01                                                 NO DDN

ONNNNN   一     乡    走年代条取标         zz了
CPU2 到                                                                                            |     怒一整理竺法
暂停所有用户                                 》
CPU3                                                                           OO                         线程                    300

No. 62195




## 第 63 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

说说 ParNew 收集器?

ParNew 收集器实质上是 Serial 收集器的多线程并行版本，使用多条线程进行垃圾收集。
ParNew/Serial Old 收集器运行示意图如下:

了ParNew/Serial Old收集器运行示意图

用户线程1

cpPuo   |                                    产汉|                                       zz仿
CPUI1                                                                                                      眶                               换 隐
4        -志
CPU2 EZZ                                                                                    赔|     刀一整理算法
-|    暂停所有用户
CPUas                                            2Z凡1     线程        人
厂程                和                          才|

说说 Parallel scavenge 收集器?
Parallel Scavenge 收集器是一款新生代收集器，基于标记-复制算法实现，也能够并行收集。和 ParNew 有些类

似，但 Parallel Scavenge 主要关注的是垃圾收集的吞吐量一一所谓吞吐量，就是 CPU 用于运行用户代码的时间和

总消耗时间的比值，比值越大，说明垃圾收集的占比越小。

运行用户代码的时间
运行坊瓜收集时间 。” 四国 运行用户代码的时间

EE33 -

根据对象存活周期的不同会将内存划分为几块，一般是把 Java 堆分为新生代和老年代，这样就可以根据各个年代
的特点采用最适当的收集算法。

说说 Serial Old 收集器?
Serial Old 是 Serial 收集器的老年代版本，它同样是一个单线程收集器，使用标记-整理算法。
说说 Parallel Old 收集器?

Parallel Old 是 Parallel Scavenge 收集器的老年代版本，基于标记-整理算法实现，使用多条 GC 线程在 STW 期间
同时进行垃圾回收。

No. 63195




## 第 64 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

Parallel scavenge/Parallel Old收集器运行示意图

GC和线程1
户一人|

CPUO FE

GC和线程2
线程2
CPU1 |             DZDDTDDZZ      多
1有) 全全3   ccefa 中   | sa ||
CPU2     本 中 zzPZ2ZZ77Y PDT
GC线程4

CPU3                                                                                                               NUNNANVNNNNNN

幼
克

OO

Safepoint                                                Safepoint

说说 CMS 收集器?
CMS 在JDK 1.5 时引入，JDK 9 时被标记弃用，JDK 14 时被移除。

CMS 是一种低延迟的垃圾收集器，采用标记-清除算法，分为初始标记、并发标记、重新标记和并发清除四个阶
段，优点是垃圾回收线程和应用线程同时运行，停顿时间短，适合延迟敏感的应用，但容易产生内存碎片，可能触
发Full GC。

CMS运行示意图

SafePoint                   SafePoint                      SafePoint                      SafePoint                     SafePoint

说说 G1 收集器?
G1 在JDK 1.7 时引入，在JDK 9 时取代 CMSs 成为默认的垃圾收集器。

G1 是一种面向大内存、高吞吐场景的垃圾收集器，它将堆划分为多个小的 Region，通过标记-整理算法，避免了
内存碎片问题。优点是停顿时间可控，适合大堆场景，但调优较复杂。

No. 64195




## 第 65 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

说说 ZGC 收集器?

ZGC是JDK 11 时引入的一款低延迟的垃圾收集器，最大特点是将垃圾收集的停顿时间控制在 10ms 以内，即使在
TB 级别的堆内存下也能保持较低的停顿时间。

它通过并发标记和重定位来避免大部分 Stop-The-World 停顿，主要依赖指针染色来管理对象状态。

,人之后，活跃对象地址视

aa为bemapped ;  | 李 和2和bnmamienmaiag et
    ob

  MGcE
转移阶段

标记阶段

站 标记之后，放对旬地址视 。 不活跃对象地址视图人为MO
!      M1

。 标记对象的可达性: 通过在指针上增加标记位，不需要额外的标记位即可判断对象的存活状态。
。 重定位状态: 在对象被移动时，可以通过指针染色来更新对象的引用，而不需要等待全局同步。

适用于需要超低延迟的场景，比如爹融交易系统、电商平台。
垃圾回收器的作用是什么?

垃圾回收器的核心作用是自动管理 java 应用程序的运行时内存。它负责识别哪些内存是不再被应用程序使用的，
并释放这些内存以便重新使用。

这一过程减少了程序员手动管理内存的负担，降低了内存泄漏和溢出错误的风险。

1. java 面试指南 (付费) 收录的滴滴同学 2 技术二面的原题: 了解哪些垃圾回收器，只能回收一个代 (新
生代、老年代) 吗，使用的 jdk 版本

2. java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 垃圾回收器的作用是什么

No. 65195




## 第 66 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

3. java 面试指南 (付费) 收录的携程面经同学 10 java 暑期实习一面面试原题: 有哪些垃圾回收器，选一
个讲一下垃圾回收的流程

4. Java 面试指南 (付费) 收录的京东同学 4 云实习面试原题: 常见的7个 GC 回收器

5. Java 面试指南 (付费) 收录的美团面经同学 15 点评后端技术面试原题: 讲一下知道的垃圾回收器，问
知不知道ZGC回收器 (不知道)

6. java 面试指南 (付费) 收录的阿里云面经同学 22 面经: cms和81的区别

7. Java 面试指南(付费) 收录的京东面经同学 9 面试原题: 怎么理解并发和并行，Parallel Old和CMS有
什么区别?

32.二能详细说一下 CMS 的垃圾收集过程吗?

CMS收集器运行示意图

CPUO 区2                                            乡
>                                        重新标记             用户线程2
CPU1   5                                                2

CPU2 ED

CPua

Safepoint                  safepoint           Safepoint                 Safepoint

CMS 使用标记-清除算法进行垃圾收集，分 4 大步:
。 初始标记: 标记所有从 GC Roots 直接可达的对象，这个阶段需要 STW，但速度很快。
。 并发标记: 从初始标记的对象出发，遍历所有对象，标记所有可达的对象。这个阶段是并发进行的。
。 重新标记: 完成剩余的标记工作，包括处理并发阶段遗留下来的少量变动，这个阶段通常需要短暂的 STW 停

。 并发清除: 清除未被标记的对象，回收它们占用的内存空间。

你提到了remark，那它remark具体是怎么执行的? 三色标记法?

是的，remark 阶段通常会结合三色标记法来执行，确保在并发标记期间所有存活对象都被正确标记。目的是修正
并发标记阶段中可能透漏的对象引用变化。

在 remark 阶段，垃圾收集器会停止应用线程，以确保在这个阶段不会有引用关系的进一步变化。这种暂停通常很
短暂。remark 阶段主要包括以下操作:

1处理写屏障记录的引用变化: 在并发标记阶段，应用程序可能会更新对象的引用 (比如一个黑色对象新增了
对一个白色对象的引用) ，这些变化通过写屏障记录下来。在 remark 阶段，GC 会处理这些记录，确保所有
可达对象都正确地标记为灰色或黑色。

2 扫描灰色对象: 再次遍历灰色对象，处理它们的所有引用，确保引用的对象正确标记为灰色或黑色。

3, 清理: 确保所有引用关系正确处理后，灰色对象标记为黑色，和白色对象保持不变。这一步完成后，所有存活
对象都应当是黑色的。

No. 66195




## 第 67 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

什么是三色标记法?

GC Roots                                                           GCRoos                                                                 GCRoots

三色标记法用于标记对象的存活状态，它将对象分为三类:

1. 和白色 (White) : 尚未访问的对象。垃圾回收结束后，仍然为白色的对象会被认为是不可达的对象，可以回
收。

2. 灰色 (Gray) : 已经访问到但未标记完其引用的对象。灰色对象是需要进一步处理的。

3 黑色 (Black) : 已经访问到并且其所有引用对象都已经标记过。黑色对象是完全处理过的，不需要再处理。
三色标记法的工作流程:
外、初始标记 (Initial Marking) : 从 GC Roots 开始，标记所有直接可达的对象为灰色 。

@、并发标记 (Concurrent Marking) : 在此阶段，标记所有灰色对象引用的对象为灰色，然后将灰色对象自身
标记为黑色。这个过程是并发的，和应用线程同时进行
此阶段的一个问题是，应用线程可能在并发标记期间修改对象的引用关系，导致一些对象的标记状态不准确。

图、重新标记 (Remarking) : 重新标记阶段的目标是处理并发标记阶段遗漏的引用变化。为了确保所有存活对象
都被正确标记，remark 需要在 STW 暂停期间执行。

@、使用写屏障 (Write Barrier) 来捕捉并发标记阶段应用线程对对象引用的更新。通过人遍历这些更新的引用来修
正标记状态，确保和遗漏的对象不会被错误地回收。

推荐阅读: 小道哥的三色标记

1. Java 面试指南 (付费) 收录的携程面经同学 10 java 暑期实习一面面试原题: 有哪些垃圾回收器，选一
个讲一下垃圾回收的流程

2. Java 面试指南 (付费) 收录的携程面经同学 1 java 后端技术一面面试原题: 对象创建到销毁，内存如
何分配的， (类加载和对象创建过程，CMS，G1 内存清理和分配)

3. java 面试指南 (付费) 收录的收钱吧面经同学 1 java 后端一面面试原题: CMS用了什么垃圾回收算
法? 你提到了remark，那它remark具体是怎么执行的? 三色标记法?

4. java 面试指南 (付费) 收录的京东面经同学 9 面试原题: 问了CMS垃圾回收器

33.愉 G1 垃圾收集器了解吗?

G1在JDK1.7时引入,在JDK 9 时取代 CMS 成为默认的垃圾收集器。

No. 67195




## 第 68 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

G1 把 java 堆划分为多个大小相等的独立区域Region，每个区域都可以扮演新生代或老年代的角色。
同时，G1 还有一个专门为大对象设计的 Region，叫 Humongous 区。

大对象的判定规则是，如果一个大对象超过了一个 Region 大小的 50%，比如每个 Region 是 2M，只要一个
对象超过了 1M，就会被放入 Humongous 中。

这种区域化管理使得 G1 可以更灵活地进行垃圾收集，只回收部分区域而不是整个新生代或老年代。
G1 收集器的运行过程大致可划分为这几个步骤:

外、并发标记，G1 通过并发标记的方式找出堆中的垃圾对象。并发标记阶段与应用线程同时执行，不会导致应用
线程暂停。

@@、混合收集，在并发标记完成后，G1 会计算出哪些区域的回收价值最高 (也就是包含最多垃圾的区域) ，然后
优先回收这些区域。这种回收方式包括了部分新生代区域和老年代区域。

选择回收成本低而收益高的区域进行回收，可以提高回收效率和减少停顿时间。

图、可预测的停顿，G1 在垃圾回收期间仍然需要 TStop the Worldj 。不过，G1 在停顿时间上添加了预测机制，
用户可以JVM 启动时指定期望停顿时间，G1 会尽可能地在这个时间内完成垃圾回收。

G1收集器运行示意图

2 内        隐 22222  重用帮志    算迄回收     用户和各1
CPUO

网胃四         了谷村相   芒 a0         最络标妃        算迄回上          用户线程2
cpu pzzzt                 让|

用户生程3          7     关发标      最弥标妃     径迄回收      用户线程3
CPU2 FEZDDDDDTN

用户线程4                 用户线程3      最维桂纪     1  用户线程3 东
cpus 一|          |记                                    z罗

2
Safepoint      Safepoint    Safepoint      Safepoint    Safepoint

1. java 面试指南 (付费) 收录的京东面经同学 1 java 技术一面面试原题: 说说 G1 垃圾回收器的原理

No. 68195




## 第 69 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

2. Java 面试指南 (付费) 收录
何分配的， (类加载和对象
3. Java 面试指南(付费) 收录的
4. java 面试指南 (付费) 收录

34.有了 CMS，为什么还要引入 G1?

经同学 1 Java 后端技术一面面试原题: 对象创建到销毁，内存如
过程，CMS，G1 内存清理和分配)

度同学4面       G1 垃圾回收器了解吗?

车面经同学 2 一面面试原题: 了解过G1垃圾回收器吗?

特性            CMS                            G1

设计目标         低停顿时间                        可预测的停顿时间

并发性           是                              是

内存碎片        是，容易产生碎片                否，通过区域划分和压缩减少碎片
收集代数        年轻代和老年代                 整个堆，但区分年轻代和老年代
并发阶段         并发标记、并发清理                 并发标记、并发清理、并发回收
停顿时间预测      较难预测                         可配置停顿时间目标

容易出现的问题        内存碎片、Concurrent Mode Failure          较少出现长时间停顿

CMS 适用于对延迟敏感的应用场景，主要目标是减少停顿时间，但容易产生内存碎片。
G1 则提供了更好的停顿时间预测和内存压缩能力，适用于大内存和多核处理器环境。

所

1. Java 面试指南 (付费) 收录的快手面经同学 5 面试原题: CMS 垃圾收集器和 G1 垃圾收集器什么区别

35.你们线上用的什么垃圾收集器?

我们生产环境中采用了设计比较优秀的 G1 垃圾收集器，因为它不仅能满足低停顿的要求，而且解决了 CMS 的浮
动垃圾问题、内存碎片问题。

G1 非常适合大内存、多核处理器的环境。

以上是比较符合面试官预期的回答，但实际上，大多数情况下我们可能还是使用的JDK 8 默认垃

可以通过以下命令查看当前JVM 的垃圾收集器:

收集器。

java -XX:+PrintCommandLineFlags -version

v (0.3s)

java -XX:+PrintCommandLineFLags -version

-XX:InitiaLHeapSize=268435456 -XX:MaxHeapSize=4294967296 -XX:+PrintCommandLineFLags -X
X:+UseCompressedCLassPointers -XX:+UseCompressed0ops -XX:+UseParatlelGC

java version "1.8.0_301"

Java(TM) SE Runtime Environment (buitLd 1.8.0_301-b09)

Java HotSpot(TM) 64-Bit Server VM (buitLd 25.301-b09，mixed mode)

No. 69195




## 第 70 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭
UseparallelGC = parallel Scavenge + Parallel 01d ，表示新生代用 Parallel scavenge 收集器，老年代
使用Parallel old 收集器。
因此你也可以这样回答:

我们系统的业务相对复杂，但并发量并不是特别高，所以我们选择了适用于多核处理器、能够并行处理垃圾回收任
务，且能提供高吞吐量的 Parallel Gc 。

但这个说法不讨喜，你也可以回答:
我们系统采用的是 CMS 收集器，能够最大限度减少应用暂停时间。
工作中项目使用的什么垃圾回收算法?

我们生产环境中采用了设计比较优秀的 G1 垃圾收集器，G1 采用的是分区式标记-整理算法，将堆划分为多个区
域，按需回收，适用于大内存和多核环境，能够同时考虑吞吐量和暂停时间。

或者:

我们系统采用的是 CMS 收集器，CMS 采用的是标记-清除算法，能够并发标记和清除垃圾，减少暂停时间，适用
于对延迟敏感的应用。

再或者:

我们系统采用的是 Parallel 收集器，Parallel 采用的是年轻代使用复制算法，老年代使用标记-整理算法，适用于高
吞吐量要求的应用。

1. Java 面试指南 付费) 收录的华为 OD 面经同学 3 技术二面面试原题: 工作中项目使用的什么垃圾回收
算法
36.垃圾收集器应该如何选择?

如果应用程序只需要一个很小的内存空间 (大约 100 MB) ，或者对停顿时间没有特殊的要求，可以选择 Serial 收
集器。

如果优先考虑应用程序的峰值性能，并且没有时间要求，或者可以接受 1 秒或更长的停顿时间，可以选择 Parallel
收集器。

如果响应时间比吞吐量优先级高，或者垃圾收集暂停必须保持在大约 1 秒以内，可以选择 CMS/ G1 收集器。
如果响应时间是高优先级的，或者堆空间比较大，可以选择 ZGC 收集器。
memo: 2025年1月16 日修改至此。

四、JVM 调优

37.用过哪些性能监控的命令行工具?

操作系统层面，我用过 top、vmstat、iostat、netstat 等命令，可以监控系统整体的资源使用情况，比如说内存、
CPU、IO 使用情况、网络使用情况。

JDK 自带的命令行工具层面，我用过 jps、jstat、jinfo、jmap、jhat、jstack、jcmd 等，可以查看JVM 运行时信
息、内存使用情况、堆栈信息等。

你一般都怎么用map?

No. 70195




## 第 71 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

人中、我一般会使用 jmap -heap <pid> 查看堆内存摘要，包括新生代、老年代、元空间等。

^C[rootGVM-0-5-tencentos Logs]# jmap -heap 391195
Attaching to process ID 391195，ptLease wait. . .
Debugger attached successfuLtLy，

Server compiter detected

JVM version is 25.382-b05

Using thread-LocalL object aLLocation。
ParatLtLetL GC with 2 thread(Ss)

Heap Configuration:

MinHeapFreeRatio         = 0

MaxHeapFreeRatio         = 100

MaxHeapSize              = 1610612736 (1536,.0MB)
NewSize                 = 268435456 (256.0MB)
MaxNewSize               = 268435456 (256.0MB)
0LdSize                   = 1342177286 (1280.0MB)
NewRatio                  = 2

SurvivorRatio            = 8

MetaspaceSize            = 21807104 (20.796875MB)

1073741824 (1024.0MB)

CompressedCLassSpaceSize

MaxMetaspaceSize         = 17592186044415 MB
G1HeapRegionSize         = 0 (0.0MB)
Heap Usage:

PS Young Generation
@、或者使用 jmap -histo <pid> 查看对象分布。

No. 71195




## 第 72 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

/Library/Java/JavaVirtuaLMachines/jdk-11.0.8.jdk/Contents/Home/bin/jmap -histo 10025
num     #instances                 ctLass name (modute)

2392376 [I (java.baseG11.0.8)
548304 [B (java.baseG11.0.8)
192912 ”java.tang.String (java.baseG11.0.8)
150816 java.utiL.HashMap$Node (java.baseG11.0.8)
121328 [Ljava.Lang.0bject; (java.baseG11.0.8)
105264 java.Lang.CLass (java.baseG11.0.8)
77576 [Ljava.utilL.HashMap$Node; (java.baseG11.0.8)
56200 [C (java.baseG11.0.8)
41408 java.utitL.concurrent.ConcurrentHashMap$Node (java.baseGl11.0.8)
34616 [Ljava.Lang.String; (java.baseG11.0.8)
28728 jdk.internaL.org.objectweb.asm.Item (java.baseG11.0.8)
24560 java.utiL.LinkedHashMap$Entry (java.baseG11.0.8)
18960 [Ljava.utiL.concurrent.ConcurrentHashMap$Node; (java.baseG11.0.8)
17184 java.utiL.HashMap (java.baseG11.0.8)
16800 [Ljdk.internat.org.objectweb.asm.Item; (java.baseG@11.0.8)
12128 java.Lang.invoke.MethodType$ConcurrentwWeakInternSet$weakEntry (ja

17:                        10608 java.tang.invoke.MemberName (java.baseG11.0.8)
18:                        10440 java.tLang.invoke.MethodType (java.baseG11.
19:                        10368                               .baseG@11.0.8)

还有生成堆转储文件: jmap -dump:format=b,file=<path> <pid> 。

ocuments/GitHub/HeLLowortLd git:(master) +127 (0.318s )

/Library/Java/JavavVirtuaLMachines/jdk-11.0.8.jdk/Contents/Home/bin/
jmap -dump:format=b,fiLe=heap.hprof 10025

Heap dump fiLe created

<“/Documents/GitHub/yHeLLowortLd git:(master) +127 (0.083Ss)
Ls

ExamptLe.cLass HeLLowWortLd.imt JDK11.java     JDK8 .java
ExamptLe.java “ JDK11.cLass    JDK8.cLass     heap .hprof

1                                 收录的哗哩哗哩

38.了解哪些可视化的性能监控工具?
我自己用过的可视化工具主要有:

中、jJConsole: JDK 自带的监控工具，可以用来监视Java 应用程序的运行状态，包括内存使用、线程状态、类加
载、GC等。

No. 72195




## 第 73 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

国 Java 监视和管理控制台 - pid: 5004 cn fighter3.DemojavaApplication                                                                                                                - DO x
国 iaO 赣Dw RH                                                                                            二[六
梳交|内存 线程 类 叶 概要 em                                                                                  二
时间55转(人          加
增内存使用量                                                                            细
200 用                                                                                     可
有
3o 到                                                                                                                                                         “
加大
如到                                                                                     加
TREE                       TREE
PP: e 加 忆昌交: 4939 陨 最大，3.8 号                        适动 妈。。 赋汗，杂总计-102
大                                                                                     cp 占用率
20.000                                                                                   2 om
1
Doo0                                                                                   1 ov
            1
0.po0           mv                     人                                            四
TREETRETIETTETERET                       TREETCRETIETTETS
io莫: 10.和5 PP间载，1 。。。 癌计-， 1045                                                        em 上用说:0 鸣

@、VisualVM: 一个基于 NetBeans 的可视化工具，在很长一段时间内，VisualVM 都是 Oracle 官方主推的故障
处理工具。集成了多个JDK 命令行工具的功能，非常友好。

轩

更新 可用插件 (18) 已下载| 已安装 设置

|_ 检查最新版本@) |                                                                                  搜索(3):
1
VisualViFrGlassfish
口。闪sualmFExtensions                           呵          社区提供的插件
口 startup Profiler           Profiling       授   抢     区提供的插
口。Bprace Workbeneh           Profiling       谷 ||友本: 15
口”巧sualmEseeurity           Seeurity        办 ||作者: Jaroslav Bacherik
口 isual cc                    Tools            俗 || 日期: 16-11-7
口 。isualmFrBufferMoniter        Tools            办 || 着: Java isualwa 插件中心
口。 Threads Inspeeter         Tools         伍||主页: https.Lvisnalvm 上ithub ie
口 ”WisualmrJconsole             Tools            办
口 VisualmPiBeans              Tools            鱼        。
口 KillApplication              Tools            例 “||打件撒述
口 ”Tracer-Jvastat Probes         Tracer           输 | :mple plugin Eiving mm overvier of advanced monitering capabilities of
口。 rracer3toniter Probes         Tracer           例 || Yisnalwmt Enhanees monitoring of Glasspish spplication server by adding
口 ”Tracer-Sving Probes          Tracer           蚁    Specialized overview，mnew tah for monitoring HTTP Service and the ability
口 “reee-Io Probes            ace          僵||te visaally select and moniter any of the deployed webh spplications
口 “racerCellections Probes      Tracer           办
口 ”Tracer-JWL Probes              Tracer             鱼
口 0oQL Syntas Support             开                 饮
安装(IT)

No. 73195




## 第 74 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

图、Java Mission Control: JMC 最初是JRockit VM 中的诊断工具，但在 OracleJDK7 Update 40 以后，就绑定到
了 HotSspot VM 中。不过后来又被 Oracle 开源出来作为了一个单独的产品。

图 oracle Java Mission Control
文件(F) 编辑 窗口W) 帮助(H)

图JVM 浏览器党事件类型|  ” 品

全跑四
> 踢 [1.8.0 202-release] -Xms128r
>咀[1.8.0 221] cnfighter3.Demoj

全MEean 有 飞人    2 MBean 服务器可用于自测和控制运行的JVM 的各个方面

> 踢 [1.8.0 221] cnfighter3.testBT
> 踢 [1.8.0 221] orgjetbrainsjps.cl
> 踢 [1.8.0 221] orgjetbrains.kotli
> 加 [1.8.0 221] 运行 Mission Cont

用过哪些第三方的工具?

人@、MAT: 一个java 堆内存分析工具，主要用于分析和查找 java 堆中的内存泄漏和内存消耗问题; 可以从java
堆转储文件中分析内存使用情况，并提供丰富的报告，如内存泄漏疑点、最大对象和 GC 根信息; 支持通过图形界
面查询对象，以及检查对象间的引用关系。

@@、GChisto: GC 日志分析工具，可以帮助我们优化垃圾收集行为和调整 GC 性能。
@@、jJpProfiler: 一个全功能的商业化java 性能分析工具，提供 CPU、 内存和线程的实时分析。

儿、arthas: 阿里巴巴开源的java 诊断工具，主要用于线上的应用诊断; 支持在不停机的情况下进行诊断; 可以
提供包括JVM 信息查看、监控、Trace 命令、反编译等功能。

@@、async-profiler: 一个低开销的性能分析工具，支持生成火焰图，适用于复杂性能问题的分析。
1. Java 面试指南 (付费) 收录的华为面经同学 9java 通用软件开发一面面试原题: 如何查看当前java 程
序里哪些对象正在使用，哪些对象已经被释放

39.JVM 的常见参数配置知道哪些?
配置堆内存大小的参数有哪些?

。 -xms : 初始堆大小

。 -xmx : 最大堆大小

。 -XX:NewSize=n : 设置年轻代大小

。 -xx:NewRatio=n : 设置年轻代和年老代的比值。如: mn 为 3 表示年轻代和年老代比值为 1: 3，年轻代占总
和的 1/4

。 -XX:SurvivorRatio=n : 年轻代中 Eden 区与两个 Survivor 区的比值。如 n=3 表示 Eden 占 3 Survivor 占
2，一个 Survivor 区占整个年轻代的 1/5

No. 74195




## 第 75 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

配置 GC 收集器的参数有哪些?

。 -xxX:+UseserialGc : 设置串行收集器
。 -xxX:+UseParallelGC : 设置并行收集器

e。 -xxX:+UseParalled101dGC : 设置并行老年代收集器

ee -XX:+UseConcMarkSweepGc : 设置并发收集器

配置并行收集的参数有哪些?
。 -XX:MaxGCPauseMillis=n : 设置最大垃圾回收停顿时间
。 -XX:GCTimeRatio=n ; 设置垃圾回收时间占程序运行时间的比例
。 -XX:+CMSIncrementalMode : 设置增量模式，适合单 CPU 环境

。 -xxX:ParallelGCThreads=n : 设置并行收集器的线程数
打印 GC 回收的过程日志信息的参数有哪些?

。 -xxX:+PrintGc : 输出 GC 日志
。 -XX:+PrintGCDetails : 输出 GC 详细日志
。 -XX:+PrintGCTimestamps : 输出 GC 的时间戳 (以基准时间的形式)

。 -xloggc:filename : 日志文件的输出路径

40.做过JVM 调优吗?
JVM 调优是一个复杂的过程，调优的对象包括堆内存、垃圾收集器和JVM 运行时参数等。

JVM调优
|
|
分析系统运行情况                 网网网关         确定 JVM 调优参数
广一一                                     | 尽 内存使用情况
实时监控          事后分析                   科衣加收闫      对比前后调优的差异
怀 Linux 命令行    上 :ec B二9
JDK 命令                                                 二哥的 Java 进阶之路                            跟踪

实时监控平台

如果堆内存设置过小，可能会导致频繁的垃圾回收。所以在技术派实战项目中，启动JVM 的时候配置了 -xms 和
-xmx 参数，让堆内存最大可用内存为 2G (我用的丐版服务器) 。

No.75195




## 第 76 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭
在项目运行期间，我会使用JVisualVM 定期观察和分析 GC 日志，如果发现频繁的 Full GC，我会特意关注一下老
年代的使用情况。
接着，通过分析 Heap dump 寻找内存泄漏的源头，看看是否有未关闭的资源，长生命周期的大对象等。
之后进行代码优化，比如说减少大对象的创建、优化数据结构的使用方式、减少不必要的对象持有等。
1. Java 面试指南 (付费) 收录

9面经同学 6java 通用软件开发一面面试原题          M 调优的

41.CPU 占用过高怎么排查?

CPU地高排查

top       top -Hp 1D      printf "%xNvn”PID      jstack PID

二 筷

首先，使用 top 命令查看 CPU 占用情况，找到占用 CPU 较高的进程 ID 。

top

top - 97:27:65 up 1:57， 3 users， 1oad average: 9.99，6.99，96.99

Tasks: 156 totat， 1 running，149 stLeeping， 9 stopped， 6 zombie

Cpu(S): 06.9sus， 9.3$sy，   gsni，99.7%id，   gswa， 9.9$hi， 6.9%5Ss1I1， 6.9%St
Mem: ”1963626k totaL， 899346k used， 19636896k free，   22248k buffers

Swap: ”29631612k total，     536k used， 2631076k free,，

PR_ NI _VIRT                              U                        COMMAND
2                                   5                                       vmtooLsd
top
init
kthreadd
mlgrat1lon
ksoftirqd/6
stopper/9
watchdog/6
ents/9
ents/9
ents_Long/9

1
2
3
4
5
6
7
8

接着，使用 jstack 命令查看对应进程的线程堆栈信息。

No. 76195




## 第 77 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

jstack -1 <pid> > thread-dump.txt

所有线程的堆#    输出到 thread-dump.txt 文件中

然后再使用 top 命令查看进程中线程的占用情况，找到占用 CPU 较高的线程ID 。

top -H -pP <pid>

[root@19test ~]# top -H -pP 31357
top - 23:13:44 up 113 days， 9:23，          1oad average: 0.00，0.00，0.00
84 totaLl， 0 runni     84 slLeeping，              0 zombie
0.1%us， 0.0Xsy， 0.0ni，99.9X%id， 0.0wa， 0.        0OXsi， 0.0Xst
8061376k total1， 7914040k used， ”147336k free，   142232k
3145720k totaL， 1167148k used， 1978572k free， 706504k cached

%CPU XMEM

忆

Geoeosceoscceccscecscecseoeseaseeseaseae
Geececccccceoeceaceeceaeaeaeaca
Seeseseseseseseseseeseasa
oonnonononoononoonononcnonocnone
Geoeocecoccecccecccecaeoeeaeeseaecsa

SSSFSNSSSSRBR1

@@
on

注意，top 命令显示的线程ID 是十进制的，而 jstack 输出的是十六进制的，所以需

Printf        PID

接着在 jstack 的输出中搜索这个十六进制的线程ID，找到对应的堆栈信息。

java.lang.Thread.State: RUNNRABLE
at com.example.MYyClass.myMethod(MyClass.java:123)
at

No. 77195





## 第 78 页


面洁逆袭 JVM篇第二版-让天下所有的面洁都能地袭
最后，根据堆栈信息定位到具体的业务方法，查看是否有死循环、频繁的垃圾回收、资源竞争导致的上下文频繁切
换等问题。

收录的阿里面经同学 1 闲鱼后端一面的原题: 上线的业务出了问题怎么调试，比
么看堆    息

8的CPU占用持续升高，有哪些排查问题的手
里?

42.内存毅高问题怎么排查?

内存飚高一般是因为创建了大量的java 对象导致的，如果持续秋高则说明垃圾回收跟不上对象创建的速度，或者
内存泄漏导致对象无法回收。

排查的方法主要分为以下几步:

第一，先观察垃圾回收的情况，可以通过 jstat -gc PID 1000 查看 GC 次数和时间。
或者使用 jmap -histo PID | head -20 查看堆内存占用空间最大的前 20 个对象类型。
第二步，通过jmap 命令 dump 出堆内存信息。

w/Documents/GitHub/HeLLowWortLd git:(master) +127 (0.318s )

/Library/Java/JavaVirtuaLMachines/jdk-11.0.8.jdk/Contents/Home/bin/
jmap -dump:format=b,fiLe=heap.hprof 10025

Heap dump fiLe created

w/Documents/GitHub/HeLLowortLd git:(master) +127 (0.083s )
Ls

ExampLe.cLass HeLLowortd.imt JDK11.java     JDK8. java      out
ExamptLe.java “ JDK11.cLass    JDK8 .ctLass     heap .hprof     Src

第三步，使用可视化工具分析 dump 文件，比如说 VisualVM，找到占用内存高的对象，再找到创建该对象的业务
代码位置，从代码和业务场景中定位具体问题。

No. 78195




## 第 79 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

VisualVM 2.1.7
灸久久知名
Applcauons x                    Se | 写 comghvbpacodngforumweb QucNorumAppicavon id 78966)
晶 Lecal                         国Overiew 因Monitor 于Threads 品Sampler 思OpProfller 图[heapdump]下午1:33:56 x
vsuavM
me iDEA (pid 63831)                    CO com.github.paicoding.forum.web.QuickForumApplication (pid 28966)
息 LocalApplication (pid 768)                   Profiler Settings
com ohhub paicodmn      nweb.QuickForumy|
图 Iheapdump] 下午1.33:56
下aojabaiejpsandneUinieid50引 monle OOcu 局 目px 轩ode 国so
惫Remote                                       Status:。 profiling running (2,165 methods instrumented)
男vM coredumps
晤JPR Snapshots            Profiling results               CPU settings | Memory settings | JDBC settings   x
图 snapshots                        加 了 固     四 转 民 ”Profile classes
Te          TICPU)     只 on:github.paicoding.forum web.林
国四22.986 ms (100%   7.27 ms (100%
[四 7aom。 aoo| 54ms aoox| |
国 710ms (009 65.4ms (100‰
L    70.8 ms (99.7虽    65.3 ms 199.7跑
0.125 ms (0.2和 0.115 ms 0290
0060ms 0O19 0057ms (01%      Include outgoing calls。 Exclude outgoing calls
0.012ms (OOM 0012ms (0     二， 50于， SU和
.xz，appte.awt.tr，comappte .tk，
ORBA.*+#，org.omg,CosNaming.##，COM。rsa.t
Preset Default               Edit

1. Java 面试指南(付费) 收录的联想面经同学 7 面试原题: 怎么定位线上的内存问题。
43.频繁 minor gc 怎么办?

频繁的 Minor GC 通常意味着新生代中的对象频繁地被垃圾回收，可能是因为新生代空间设置的过小，或者是因为

程序中存在大量的短生命周期对象 (如临时变量) 。
可以使用 GC 日志进行分析，查看 GC 的频率和耗时，找到频繁 GC 的原因。

-XX:+PLintGCDetails -Xloggc:gc.1og

或者使用监控工具查看堆内存的使用情况，特别是新生代 (Eden 和 Survivor 区) 的使用情况。
如果是因为新生代空间不足，可以通过 -xmn 增加新生代的大小，减缓新生代的填满速度。

java -xmn256m your-app.jar

如果对象需要长期存活，但频繁从 Survivor 区晋升到老年代，可以通过 -xx:sSurvivorRatio 参数调整 Eden 和

Survivor 的比例。默认比例是 8:1，表示 8 个空间用于 Eden，1 个空间用于 Survivor 区。

-XX:SurvivorRatio=6

调整为 6 的话，会减少 Eden 区的大小，增加 Survivor 区的大小，以确保对象在 Survivor 区中存活的时间足够

长，避免过早晋升到老年代。

1. Java 面试指南 (付费) 收录的京东面经同学 8 面试原题: young GC频繁如何排查? 修改哪些参数?

44.频繁 Full GC 怎么办?

No. 79195





## 第 80 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

频繁的 Full GC 通常意味着老年代中的对象频繁地被垃圾回收，可能是因为老年代空间设置的过小，或者是因为程
序中存在大量的长生命周期对象。

该怎么排查 Full GC 频繁问题?
我厂会通过专门的性能监控系统，查看 GC 的频率和堆内存的使用情况，然后根据监控数据分析 GC 的原因。
如果是小厂，可以这么回复。
我一般会使用JDK 的自带工具，包括jmap 、jstat 等。
# 查看堆内存各区域的使用率以及Gc情况
jstat -gcutil -h20 pid 1000
# 查看堆内存中的存活对象，并按空间排序
jmap -histo pid | head -n20
# dump堆内存文件
jmap -dump:format=b,file=heap pid
或者使用一些可视化的工具，比如 VisualVM、jJConsole 等，查看堆内存的使用情况。

假如是因为大对象直接分配到老年代导致的 Full GC 频繁，可以通过 -xx:PretenuresizeThreshold 参数设置大
对象直接进入老年代的阔值。

或者将大对象拆分成小对象，减少大对象的创建。比如说分页。

假如是因为内存泄漏导致的频繁 Full GC，可以通过分析堆内存 dump 文件找到内存泄漏的对象，再找到内存泄漏
的代码位置。

假如是因为长生命周期的对象进入到了老年代，要及时释放资源，比如说 ThreadLocal、数据库连接、IO 资源
等。

假如是因为 GC 参数配置不合理导致的频繁 Full GC，可以通过调整 GC 参数来优化 GC 行为。或者直接更换更适合
的 GC 收集器，如 G1、ZGC 等。

1. Java 面试指南 (付费) 收录的得物面经同学 8 一面面试原题: java 中 full gc 频繁，有哪些原因

五、类加载机制
45.恰了解类的加载机制吗? (补充)

2024年 03 月 29 日增补
了解。
JVM 的操作对象是 Class 文件，JVM 把 Class 文件中描述类的数据结构加载到内存中，并对数据进行校输、解析和
初始化，最终转化成可以被JVM 直接使用的类型，这个过程被称为类加载机制。
其中最重要的三个概念就是: 类加载器、类加载过程和双亲委派模型。
。 类加载器: 负责加载类文件，将类文件加载到内存中，生成 Class 对象。
。 类加载过程: 包括加载、验证、准备、解析和初始化等步骤。
。 双亲委派模型: 当一个类加载器接收到类加载请求时，它会把请求委派给父一一类加载器去完成，依次弟
归，直到最顶层的类加载器，如果父一一类加载器无法完成加载请求，子类加载器才会尝试自己去加载。

No. 80195




## 第 81 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

1. java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你了解类的加载机制吗?

2. Java 面试指南(付费) 收录的美团面经同学 3 java 后端技术一面面试原题: java 的类加载机制 双亲委
派机制 这样设计的原因是什么

46.类加载器有哪些?

主要有四种:
人中、启动类加载器，负责加载JVM 的核心类库，如 rtjar 和其他核心库位于 JAVA_HOME/jre/lib 目录下的类。
人@、扩展类加载器，负责加载 JAVAa_HoME/jre/lLib/ext 目录下，或者由系统属性 java.ext.dirs 指定位置的类

库，由sun.misc.LauncherSExtCclassLoader 实现。
余、应用程序类加载器，负责加载 classpath 的类库，由 sun.misc.LauncherSappClassLoader 实现。
我们编写的任何类都是由应用程序类加载器加载的，除非显式使用自定义类加载器。

鲜、用户自定义类加载器，通常用于加载网络上的类、执行热部署 (动态加载和蔡换应用程序的组件) ，或者为了
安全考虑，从不同的源加载类。

通过继承 java. lang.ClassLoader 类来实现。
47.能说一下类的生命周期吗?

一个类从被加载到虚拟机内存中开始，到从内存中和卸载，整个生命周期需要经过七个阶段: 加载 、验证、准备、
解析、初始化、使用和逢载。

-连接
|                        Linking
加载      己> 有      验证               准备               解析
Loading               国 Verification            Preparation             Resolution

孝载                         初始化

Unioading                     Initialization

48.六类装载的过程知道吗?

推荐阅读: 一文彻底搞懂jJava 类加载机制
知道
类装载过程包括三个阶段: 载入、链接和初始化。
@D、载入: 将类的二进制字节码加载到内存中。

No. 81195




## 第 82 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

@@、链接可以细分为三个小的阶段:
。 验证: 检查类文件格式是否符合JVM 规范
。 准备: 为类的静态变量分配内存并设置默认值。
。 解析: 将符号引用替换为直接引用。

图、初始化: 执行静态代码块和静态变量初始化。

在准备阶段，静态变量已经被赋过默认初始值了，在初始化阶段，静态变量将被赋值为代码期望赋的值。比如说
static int a = 1; ，在准备阶段，a 的值为0，在初始化阶段，a 的值为 1。

换名话说，初始化阶段是在执行类的构造方法，也就是javap 中看到的 <clinit>() 。
载入过程JVM 会做什么?

>

结构化静态存储结构

Y

在内存中生成Class对象

。 1) 通过一个类的全限定名来获取定义此类的二进制字节流。
。 2) 将这个字节流所代表的静态存储结构转化为方法区的运行时数据结构。
。 3) 在内存中生成一个代表这个类的 java.lang.Cclass 对象，作为这个类的访问入口。
1. Java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你了解类的加载机制吗?

2. java 面试指南(付费) 收录的美团面经同学 16 暑期实习一面面试原题: 讲一下类加载过程，双亲委派
模型，双亲委派的好处

3. java 面试指南(付费) 收录的美团面经同学 18 成都到家面试原题; 类加载过程

4. java 面试指南 (付费) 收录的快手同学 4 一面原题: 类装载的执行过程? 双亲委派模式是什么? 为什么
使用这种模式?

memo: 2025年1月17 日修改至此。

No. 82195




## 第 83 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

49.闪什么是双亲委派模型?

双亲委派模型要求类加载器在加载类时，先委托父加载器尝试加载，只有父加载器无法加载时，子加载器才会加
载。

启动类加载器
Bootstrap Class Loader

<JAVA_HOME>\iib
-Xbootclasspath指定获径

<JAVA_HOME>NI1ib\ext

可局并必暑所

用户类品径〈ClassPath)

自定义类加载器

User Class Loader             User Class Loader

  自定义类加载器

这个过程会一直向上递归，也就是说，从子加载器到父加载器，再到更上层的加载器，一直到最顶层的启动类加载
器。

启动类加载器会党试加载这个类。如果它能够加载这个类，就直接返回; 如果它不能加载这个类，就会将加载任务
返回给委托它的子加载器。

子加载器尝试加载这个类。如果子加载器也无法加载这个类，它就会继续向下传递这个加载任务，依此类推。
直到某个加载器能够加载这个类，或者所有加载器都无法加载这个类，最终抛出 ClassNotFoundException。
1. java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 你了解类的加载机制吗?
2. java 面试指南 (付费) 收录的阿里云面经同学 22 面经: 双亲委派机制

49.为什么要用双亲委派模型?

人@、避免类的重复加载: 父加载器加载的类，子加载器无需重复加载。
@@、保证核心类库的安全性: 如 java.lang.* 只能由 Bootstrap ClassLoader 加载，防止被算改。

1. java 面试指南 (付费) 收录的美团面经同学 16 暑期实习一面面试原题: 讲一下类加载过程，双亲委派
模型，双亲委派的好处

50.如何破坏双亲委派机制?

No. 83195




## 第 84 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

重写 ClassLoader 的 loadclass() 方法。

如果不想打破双亲委派模型，就重写 ClassLoader 类中的 findclass() 方法，那些无法被父类加载器加载的类最
终会通过这个方法被加载。

memo: 2025年1月18 日修改至此。
51.有哪些破坏双亲委派模型的典型例子?
我了解的有两种:

。 第一种: SPI 机制加载JDBC 驱动。
。 第二种: 热部署框架。

JDBC
=                   父类                                                                                                  思扑， <JAVA_HOME>NIib
findClass()                                       ee                   -Xbootclasspath指定路径
loadclass0                                 x       雪闪了天

0            SN
重写即破坏双亲委派机制                             | Apllication
                             吕|关现 ) 加载 | Classloader

ClassPath

第一次破坏: 向下兼容祖传代码              第二次破坏: 加载各厂商spi实现

0SG1存在很多平级委派的情形     第三次破坏: 实现热部署/热蔡换

说说SPI 机制?
SPI 是java 的一种扩展机制，用于加载和注册第三方类库，常见于JDBC、JNDI 等框架。
双亲委派模型会优先让父类加载器加载类，而 SPI 需要动态加载子类加载器中的实现。

根据双亲委派模型， java. sq1.Driver 类应该由父加载器加载，但父类加载器无法加载由子类加载器定义的驱动
类，如 MySQL 的 com.mysql.cj.jdbc.Driver 。

那么只能使用 SPI 机制通过 META-INF/services 文件指定服务提供者的实现类。

ClassLoader cl = Thread.currentThread() .getContextClassLoader();

Enumeration<Driver> drivers = ServiceLoader.load(Driver.class，cl) .iterator() 1;

DriverManager 使用了线程上下文类加载器来加载 SPI 的实现类，从而允许子类加载器加载具体的JDBC 驱动。
说说热部署?

No. 84195




## 第 85 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

热部署是指在不重启服务器的情况下更新应用程序代码，需要蔡换旧版本的类，但旧版本的类可能由父加载器加
载。

如 Spring Boot 的 DevTools 通常会自定义类加载器，优先加载新的类版本。
memo: 2025年1月19 日修改至此。

52.Tomcat 的类加载机制了解吗?

了解。
Tomcat 基于双亲委派模型进行了一些扩展，主要的类加载器有:
。 Bootstrap ClassLoader: 加载Java 的核心类库;
。 Catalina ClassLoader: 加载 Tomcat 的核心类库;
。 Shared ClassLoader: 加载共享类库，允许多个 Web 应用共享某些类库;

。 WebApp ClassLoader: 加载 Web 应用程序的类库，支持多应用隔离和优先加载应用自定义的类库 (破坏了
双亲委派模型) 。

Shared类加载器
Shared Class Loader

Catalina类加载器
Catalina Class Loader

53.你觉得应该怎么实现一个热部署功能?

No. 85195




## 第 86 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

热部署是指在不重启服务器的情况下，动态加载、更新或卸载应用程序的组件，比如类、配置文件等。
需要在类加载器的基础上，实现类的重新加载。

我的思路是
第一步，使用文件监控机制，如 java NIO 的 WatchService 来监控类文件或配置文件的变化。当监控到文件变
时，触发热部署流程。

class Filewatcher {

public static void watchDirectoryPath(Path path) {

// 检查路径是否是有效目录

if (!isDirectory(path)) {

System.err.println("Provided path is not a directory: "+ path) 1
returny

}

System.out .println("Starting to watch path: " + path) 7

// 获取文件系统的 WatchService

try (WatchService watchService = path.getFileSystem( ) .newWatchService()) {

// 注册目录监听服务，监听创建、修改和删除事件

Path.register(watchService，ENTRY_ CRERTE，ENTRY_MODIFY，ENTRY_ DELETE ) ?

while (true) {
WatchKey key)

try {
// 阻塞直到有事件发生
key = watchService.take() 17

} catch (InterruptedException e) {
System.out .println("WatchService interrupted，stopping directory

watch.") 7
Thread.currentThread() .interrupt() 17
breaky

}
// 处理事件

for (WatchEvent<?> event : key.pollEvents()) {
ProcessEvent(event) 7

// 重置 key，如果失败则退出

if (!key.reset()) {
System.out .println("matchKey no longer valid。. Exiting watch loop.");

breaky

】}
} catch (IOException e) {
System.err.println("Rn error occurred while setting upP the WatchService: "+

e.getMessage()) 1
eprintStackTrace() 7

No. 86195




## 第 87 页


渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

Private static boolean isDirectory(Path path) {
return Files.isDirectory(path，LinkOption.NOFOLLOW_LINKS)

Private static void processEvent (WatchEvent<?> event) {
WatchEvent .Kind<?> kind = event.kind()7

// 处理事件类型
if (kind == OVERFLOW) {
System.out .println("Event overflow occurred。 Some events might have been

lost.") 7
returny
}
esuppressWarnings("unchecked")
Path fileName = ((WatchEvent<Path>) event) .context();
System.out .println("Event: " + kind.name() + "，File affected: "+ fileName)7
}

public static void main(String[] args) {
// 设置监控路径为当前目录
Path pathToWatch = Paths.get(".
watchDirectoryPath(PpathToWatch) 7

第二步，创建一个自定义类加载器，继承 java. lang.classLoader ，并重写 findclass() 方法，用来加载新的类
文件。

class HotSwapClassLoader extends ClassLoader {
public HotSwapClassLoader() {
super(ClassLoader.getSystemCclassLoader());

eoverride
Protected Class<?> findClass(String name) throws ClassNotFoundException {
// 加载指定路径下的类文件字节码
byte[] classBytes = loadClassData(name);
if (classBytes == nul1) {
throw new ClassNotFoundException(name)

}
// 调用defineclass将字节码转换为Class对象

return defineclass(name，classBytes，0，classBytes.length))

Private byte[] loadclassData(String name) {
// 实现从文件系统或其他来源加载类文件的字节码
LV

No. 87195




## 第 88 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

return nul17

)}

友情提示: Intellj IDEA 提供了热部署功能，当我们修改了代码后，IDEA 会自动保存并编译，如果是 Web 项目，
还可以在 Chrome 浏览器中装一个 LiveReload 插件，一旦编译完成，页面就会自动刷新看到最新的效果。对于测
试或者调试来说，非常方便。

1. java 面试指南 (付费) 收录的小米暑期实习同学 E 一面面试原题: 那你知道类的热更新的?

54.说说解释执行和编译执行的区别 (补充)
2024年 03 月 08 日增补
先说解释和编译的区别:

。 解释: 将源代码逐行转换为机器码。
。 编译: 将源代码一次性转换为机器码。

一个是逐行，一个是一次性，再来说说解释执行和编译执行的区别:
。 解释执行; 程序运行时，将源代码逐行转换为机器码，然后执行。
。 编译执行; 程序运行前，将源代码一次性转换为机器码，然后执行。

java 一般被称为"解释型语言"，因为 java 代码在执行前，需要先将源代码编译成字节码，然后在运行时，再由
JVM 的解释器“逐行"将字节码转换为机器码，然后执行。

这也是Java 被诉病"慢"的主要原因。

但JIT 的出现打破了这种刻板印象，JVM 会将热点代码 〈即运行频率高的代码) 编译后放入 CodeCache，当下次执
行再遇到这段代码时，会从 CodeCache 中直接读取机器码，然后执行。

因此，java 的执行效率得到了大幅提升。

No. 88195




## 第 89 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

| 1. Java 面试指南 (付费) 收录的腾讯 java 后端实习一面原题: 说说java 解释执行的流程。
memo: 2025年1月21 日修改至此。

面渣逆袭JVM 篇第二版终于整理完了，说一点心里话。

No. 89195




## 第 90 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

昌上日@
全部

Apple Books
国 主页

三分恶|沉默王二修订版    三分恶|沉默王二修订版    三分恶|沉默王二修订版

未知作者

我的藏书
十 新建藏书

二哥的并发编                “     二哥的             哥的

| 程进阶之路.md                                     j            .                  Java进阶之路

未知作者           ECSU      未知作者
马伟青

网上的八股其实不少，这样可以给大家提供更多的选择，但面渣逆袭的含金量懂的都懂。

二哥您好, 我限制开始面试, 发现
就是这些题目90% 来自面渣

面渣逆袭第二版是在星球嘉宾三分恶的初版基础上，加入了二哥自己的思考，加入了 1000 多份真实面经之后的结
果，并且从从 24 届到 25 届，帮助了很多小伙伴。未来的 26、27 届，也将因此受益，从而拿到心仪的 offer。

能帮助到大家，我很次奈，并且在重制面渣逆袭的过程中，我也成长了很多，很多薄弱的基础环节都得到了加强。

No. 90195




## 第 91 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

过 花舞洛伊人 名 进阶牛

八股文看谁的
如题，javaguide，二哥面渣，小林code，看谁的国

全 银行究极大孝子 罗 大情已定 “3汝万仙大

全是广告哥，我觉得二哥面渣/小林就很够了，你不一定要只看一家，一个八股问题，
看其他博客，集百家之长

由36 回回复 口分享 发布于09-03 14:44江苏

和 1589494222 人 出岳牛“3于广领航者楼主”回复
中肯的
中1 加回复 发布于09-03 20:55北京 来自Android客户端
全  流连~ 园 习贰肝达
一
二哥的面渣逆袭，还有掘金竹子爱熊猫的专栏，个人感觉还是不错的

由32 辕回复 加分享 发布于09-0114:46广东 来自Android客户端

No. 91195




## 第 92 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

HE                                          站 … 下7
双非硕测开开了17X15拒了图二哥八股文无敌
号 沉默王二 作者                           四

感谢认可，八股是不是吊打面试官芒

久吓 :                   上四 1

回复 沉默王二: 包吊打的号

很多时候，我觉得自己是一个佛系的人，不愿意和别人争个高低，也不愿意去刻
我喜欢静待花开。

如果你觉得面渣逆袭还不错，可以告诉学弟学妹们有这样一份免费的学习资料，帮有我做个口碑。
我还会继续优化，也不确定第三版什么时候会来，但我会尽力。

愿大家都有一个光明的未来。

这次仍然是三个版本，亮白、暗黑和 epub 版本。给大家展示其中一个 epub 版本吧，有些小伙伴很急需这个版
本，所以也满足大家了。

传自己的作品。

味
叫

No. 92195




## 第 93 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆袭

面渣逆贰 JVM 篇第二版

介绍一下方法区?
ee 提朋人
an             方法区并不真实存在，属于 Java 虚拟机规范中的一
<           个逻辑概念用于存储已被 JVM 加载的类信息、常
量、尊态变量、即时编译器编译后的代码缓存等。
在 HotSpot 虚拟机中，方法区的实现称为永久代

PermGen，但在 Java 8 及之后的版本中，已经被元

Eee
< 认内丰虹小全“inr 设时地内存最大全>       空间 Metaspace 所替代。

随着 JIT 编译器的发展和逃逸技术的逐渐成熟，     变量存在堆栈的什么位置?

“所有的对象都会分配到堆上"就不再那么绝对了。

从JDK7 开始，JVM 默认开启了逃旭分析，写味     对于局部变量，它存储在当前方法栈帧中的局部变量
着如果某些方法中的对象引用没有被返回或者没有在     表中。当方法执行完尘，栈由被回收，局部变量也会
方法体外使用，也就是未逃逸出去，那么对象可以直      被释放。

接在栈上分配内存。                                  alae void nethodt

int localVar = 100;             熏，存角在花骨中的

堆和栈的区别是什么?
对于静态变量来说，它存储在 Java 虚拟机规范中

堆属于线程共享的内存区域，几乎所有 new 出来的      前方法区中。在Java 7 中是永久带、在Javag 及以后

对象都会堆上分配，生命周期不由单个方法调用所决

定，可以在方法调用结束后继续存在，直到不再被任     是元空间。

何变量引用，最后被垃圾收集器回收。                Public class Statici    mo
栈属于线程私有的内存区域，主要存储局部变量、         ，   Public static int staticVar   1007;     属坊变

方法参数、对象引用等，通常随着方法调用的结束而

自动释放，不需要垃圾收集器处理。                    1 Jaon 面试将下 〈付玫) 收录的真攻同学10

后疯实习一历的厦题: 舱径配的区草是佬

由于 PDF 没办法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】，或者扫描/长按识别下面的二维
码，关注二哥的公众号，回复【222】即可拉取最新版本。

No. 93195




## 第 94 页


面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，毕竟星球用户都付费过了，
我有必要让他们先享受到一点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

《 公众号                         沉默王二                                    久                  wangpan                   江人         于 由
名称                                          x
和                          蕊 二哥的 JVM 进阶之路.epub            2024年7月11日 14:0
        镶” 与                            二哥的 JVM 进阶之路.md              2024年7月11日 14:0
一                                                 二哥的 JVM 进阶之路.pdf              2024年7月11日 14:0
60*13某别说新疆 ，外派到伊拉克都行                                    “” 面渣逆效 Java 基础篇第二版.md                 2024年12月31日 08
总 面渣逆效 JVM篇 V2.0.epub             2025年1月21日 14:2
目 面渣地芍 JVM篇 V2.0.pdf             1
渣逆效 JVM篇 V2.0 (上暗黑版).pdf        2025年1月21日 14:2

“ 面渣逆费 JVM篇第二版.md             2025年1月21日 14:2
' 面渣逆芍 MyBatis.md                          2024年7月11日 14:0
面渣逆装 MyBatis.pdf                2024年7月11日 14:0
面渣逆装 Redis 篇.md                2024年7月11日 14:0

一           3                  一                               面渣逆袭 Redis 篇.pdf                       2024年7月11日 14:0
全   面济闻费+二哥的 Java 进阶之路 PDF，第二                        点 面渣逆袭 Spring 篇.md                    2024年7月11日 14:0
版，GitHub 星标13000+                                                台面潮逆装 Spring 篇.pdf                       2024年7月11日 14:0
忆 面渣逆闭-分布式篇.md                  2024年7月11日 14:0
而叶司国用和二 Tree 了                           呈 面渣逆闭-分布式篇.pdf                  2024年7月11日 14:0
ea                                               忆 面淹逆效并发编程篇第二版.md             2025年2月26日11.3
本本本加也丰。 本 rar 可中 rm PP                       口 面渣逆袭并发编程篇V2.0.epub            2025年2月26日1
1 1                                                    日 面渣逆闭并发编程篇V2.0.pdf               2025年2月26日1
扩 面淹逆效并发编程篇V2.0 (暗黑版) .pdf       2025年2月26日 11:3
二哥的并发编程小册: https:/iavabettercn/                        面法闻六操作系统.md                   2024年7月1日 14:0
thread/                                                                         机过宇和  到                     2024年7月11日 14:0
二         1       ，                                   渣i    合;      二版.epub           2025年1月8日 18:33
二哥的 JVYM 进阶之路: httpsyiavabettercn/                            ， 面渣逆袭集合框架篇第二版.md                2025年1月8日 18:26
jvm/                                                                             面潮逆装集合框架篇V2.0.pdf                  2025年1月8日 18:27
面渣逆袭集合框架篇 V2.0 (暗黑) .pdf            2025年1月8日 18:26
* 面渣逆获计算机网络.md               2024年7月11日 14:0
   白 %-                                                          面渣逆获计算机网络.pdf                   2024年7月11日 14:0

'” 面渣逆效微服务篇.md                 2024年7月11日 14:0
面渣逆著微服务篇.pdf                 2024年7月11日 14:0
面渣逆效 Java基础篇V2.0.epub          2024年12月31日 09
面渣逆效Java基础篇V2.0.pdf           2024年12月30日 20
外 面渣逆芍Java基础篇V2.0 (暗黑) .pdf       2024年12月30日 20

我把二哥的java 进阶之路、JVM 进阶之路、并发编程进阶之路，以及所有面渣逆袭的版本都放进来了，涵盖 Java
基础、jJava集合、java并发、JVM、Spring、MyBatis、计算机网络、操作系统、MySQL、Redis、RocketMQ 、分
布式、微服务、设计模式、Linux 等 16 个大的主题，共有 40 多万字，2000+张手绘图，可以说是诚意满满。

222

图文详解 54 道 java 虚拟机高频面试题，这次面试，一定吊打面试官，整理: 沉默王二，玲转载链接，作者: 三分

没有从么使我停留_一队了月的，缴天岩六有玫瑞、有绿稍、有宁竞的溢湾，我是不冬之舟。
系列内容:
。 面渣逆获Java SE 篇 唱
e 面渣逆袭 java 集合框架篇 吃
面渣逆效Java 并发编程篇
画淹逆获JVM 篇只

No. 94195




## 第 95 页


e

面洼地区 Spring篇吨
面渣逆区 Redis 入号

面渣逆区 MyBatis 算是
面酒逆区 MySQL 简 只
面渣逆效操作系统篇 中
面渣逆效计算机网络篇 唱
面淹逆获 RocketMQ 篇啤
面淹逆获分布式篇 吨

面渣逆效微服务篇 成

面尖逆效设计模式篇吕
面渣逆区 Linux入号

面渣逆袭 JVM篇第二版-让天下所有的面渣都能逆效

No. 95195



