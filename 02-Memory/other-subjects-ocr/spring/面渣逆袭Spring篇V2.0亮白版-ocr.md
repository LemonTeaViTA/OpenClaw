# 面渣逆袭Spring篇V2.0亮白版

> 来源：面渣逆袭Spring篇V2.0亮白版.pdf

> OCR 解析时间：2026-03-14 17:41:02

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 180

- **文件大小**: 47.65 MB


---


## 第 1 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

合 ”二哥的Java进阶之路

三分恶

沉默王二修订版

No.11180




## 第 2 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

3.3 万字 180 张手绘图，详解 41 道 Spring 面试高频题 (让天下没有难背的八股) ，面渣背会这些 Spring 八股
文，这次吊打面试官，我觉得稳了 (手动 dog) 。整理: 沉默王二，戳转载链接，作者: 三分恶，戳原文链接。

亮白版本更适合拿出来打印，这也是很多学生党喜欢的方式，打印出来背诵的效率会更高。

@e@@ 思 癌 加 CC 二 而半地费Spring篇V2.0亮自乒pdf - 福昕阅读器 | C〇 搜索                              出有四
文件 主页 注得 视加 表单 保护 共享 玫助
开始   我的简.   印进华_.  我的简历.  后庙简历，   肛-硕.  刘宇闭的.  Java简,   9756-、   罗水平的  刘瑞-通.  星球编号  面淹逆.   面淹.， X 了
书签
内                       loC
轩 凡入大
   CE                 6.志说一说什么是loC?
包                       推荐阅读: loC 要二                                             1
只 前言
 sn 站                     1oc 的全称是 Inversion of Control，也就是控制反转。这里的"控制 指的是对象创建和依赖关系管理的控制权。
= nc
刻 同6.说说一说什么是loc?
口 7能说一下loC的实现机制吧?                           Inversion of Control

虽说BeanFactony和Applicantl
击 内 9.民 项目启动时Spring的loC会人
。口1你是每理解Bean的?
由 只 11.计能说一下Bean的生命周期下
直口 12 .为什么IDEA不推荐使用@Autc4
上 1aeAutowired的实现原理了角
击 内 14.什么是自动装配?
只 15.Bean的作用域有哪些?
。吕16 spring中的单出Bean全存在
只 人什么是和环依赖?
。央 18 寺 Spring怎么解决和环人
中 1 为什么需要三级引而不是两                  《
= op                               k    Application     >    Framework
后 内 20.计说说什么是 AOP?
只 Spring AOP 有哪些核心概念
只 spring AOp 织入有用站种方           以前我们写代码的时候，如果A类需要用到 B 类，我们就在A类里面直接 new 一个 B 对象出来，这样 A类就控
唱 Aspect 是什么?                  制了B 类对象的创建。
唱 spring AOp 有卫些通知方式
贿 spring AOP 发生在什么时候*
人 《  3 /ao>》》是品           斩具明明一

2025 年 06 月 15 日开始着手第二版更新，历经两个月，主要是中间有段时间把精力放到了派聪明 RAG 这个项目
的教程撰写上，第二版，我们升级了很多内容。

。 对于高频题，会标注在《Java 面试指南 (付费) 》中出现的位置，哪家公司，原题是什么，并且会加尖，目
录一目了然; 如果你想节省时间的话，可以优先背诵这些题目，尽快做到知彼知己，百战不列。

。 区分八股精华回答版本和原理底层解释，让大家知其然知其所以然，同时又能做到面试时的高效回答。

。 结合项目 (技术派、pmhub) 来组织语言，让面试官最大程度感受到你的诚意，而不是机械化的背诵。

。 修复第一版中出现的问题，包括球友们的私信反馈，网站留言区的评论，以及 GitHub 仓库中的issue，让这
份面试指南更加完善。

。 增加二哥编程星球的球友们拿到的一些 offer，对面渣逆袭的感谢，以及对简历修改的一些认可，以此来激励
大家，给大家更多信心。

。 优化排版，增加手绘图，重新组织答案，使其更加口语化，从而更贴近面试官的预期。

0

十138.66%

No. 21180




## 第 3 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Current Braneh     Fetchorgin
时 master             个 tastetchedjustnow

Changes           History        Update mapmd 革

2 和      718da83d0 加 +61 -61
Branch to Compare    7   0 四 +61 -6

hixingqiulmap.md                                            密:- 口

Tchanged file           docslsr

Update mysqlmd

4

docslsrcjzhishixin_jmap md 回

人mmE= .is
14 14
Updee Spring Bootend sioroeery…                   15 。 315。 +非沉于友的认可和赤持+             为了方便案引，我格于友们之有的    7
和   da                               总分类，相  可以根据自己的人          请善用 Ctrt+F   工程量巨大，因为星球
update mapmd                                已经沉汗了太多优质的习资源和          多时间了，所以你需要的资源，通到的问题这
mpE= .15dmysaoo                                                 于可有答案
16 16
下buld                           17       地址: httpsi/lsnusyuque.comlitvanger/ydx8ln/gtygui5tdvvsgdndl thttps:y/wwsyuq
本   二了                                    ue.com/itwanger/ydx8lp/gtygui5tdvvs8dmd)
2025年7月31日build                                            18
mm     岂                                 19       如果你是第一次使用知识星球，请攻『[新人必看] (https;//www.yuque comy itwanger/ydx81p/mfhql
Snar8wbf66e) | 这个和项志帖，149 示后你就如鱼竺了。我会按下面这样一个素引来整理
Update testimonials and statein                    17 | + 如果你是第-次使用知识必球，请是 上[新人必乔](https://tzsxq,com/91hpx)) 这个时顶雪帖，159
二                                         水了。 我会按照下面这样一个索引来整理，
完善自定义 Spring Boot Starter 教程                    26 18
省 mw   0   oo                   214 19                模板6实战项目5我在B站上大学5球友分训
2 28
Update Spring and resdme docsw                     2 2                      6o 语言.Python 操作系统、大娄据、计算机考研、测开/到
了
Merge pull request 4169 from beta                 24        :和5检招5o1fe 选择5考研6实习86专升本6用
晤 ma王= . 23 daysago                    25 23    工f    择5轩行5求职6职业规划
26           星球专栏 [强烈推荐语难阅读] (https;//t,zsxqvcom/6iuzn6I)); ]ava面试指南、技术派教程、编
docs: Update Java SE switch state                                                         REG
四bn    24daysa                         4。 ，。 -五个实记项目r4个付费专栏[基地址+到到对了方式(https://t,zsxq, comyBFRqz)): 逝了明 RA

an 增加一个续手项目                                                        5、和前后记分元技术派、德服务 PmHub、校招活、]ava面试指南、编程哺实战笔记、二可的LeetCode肌归和

由于 PDF 没办法自我更新，所以需要最新版的小伙伴，可以微信搜 【沉默王二】，或者扫描/长按识别下面的二维
码，关注二哥的公众号，回复【222】即可拉取最新版本。

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，毕竟星球用户都付费过了，
我有必要让他们先训   受到一点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

No. 31180




## 第 4 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

60*13薪别说新疆 ，外派到伊拉克都行

面渣逆袭+二哥的 Java 进阶之路 PDF，第二
版，GitHub 星标 13000+

驹中局回时各。本 rom 下mr
本

本本目电中。二 roeron mn mm
1

二哥的并发编程小册: https:/lavabettercn/
thread/

二哥的 JVM 进阶之路: https:/lavabetter cn/
jvm/

四 暂 %*

222

wangpan                 注人            v 由

名称                                    和^ | 修改日期

总 二哥的 JVM 进阶之路.epub
心 二哥的 JVM 进阶之路.md

哥的 JVM 进阶之路.pdf

所 面渣逆赣 Java 基础篇第二版.md                  2024年12月31日 08
地装 JVM篇 V2.0.epub            2025年1月21日 14:2
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
面淹逆袭并发编程篇V2.0 (暗黑版).pdf      2025年2月26日 11:3

2024年7月11日 14:0
2024年7月11日 14:0
2024年7月11日 14:0

所 面渣逆缆操作系统.md                        2024年7月11日 14:0
 面淹逆效操作系统.pdf                    2024年7月11日 14:0
口 面济逆获集合框架篇第二版.epub              2025年1月8日 18:3:

2025年1月8日 18:26
2025年1月8日 18:27
2025年1月8日 18:26
2024年7月11日 14:0
2024年7月11日 14:0
2024年7月11日 14:0
2024年7月11日 14:0
2024年12月31日 09
2024年12月30日 20
2024年12月30日 20

“ 面渣逆袭集合框架篇第二版.md

面渣逆袭集合框架篇 V2.0.pdf

面淹逆效集合框架篇V2.0 (暗黑) .pdf
面淹逆闭计算机网络.md

面渣逆袭计算机网络.pdf

面渣逆袭微服务篇.md

面渣逆袭微服务篇.pdf

面渣逆费Java基础篇V2.0.epub

面淹逆绪Java基础篇V2.0.pdf

面渣逆获 Java基础篇V2.0 (暗黑).pdf

我把二哥的java 进阶之路、JVM 进阶之路、并发编程进阶之路，以及所有面渣逆袭的版本都放进来了，涵盖 Java
基础、jJava集合、java并发、JVM、Spring、MyBatis、计算机网络、操作系统、MySQL、Redis、RocketMQ 、分
布式、微服务、设计模式、Linux 等 16 个大的主题，共有 40 多万字，2000+张手绘图，可以说是诚意满满。

展示一下暗黑版本的 PDF 吧，排版清晰，字体优雅，更加适合夜服，晚上看会更舒服一点。

No. 41180




## 第 5 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

局

文件 主页 注释 视图 表单 保护 共享 帮助

AbstractApplicationContext                              AbstractBeanFactory

refresh            finishBeanFactoryInitialization                            getBean

只 前言                                                   gcetBean
由 口 基础
吕 ec
由 状 6.癌说一说什么是ooc?
由 门 7能说一下loc的实现机制吗?
只 8说说BeanFactory和Applicantt
由 品 9 党项目启动时Spring的loC会人
内 10 你是怎么理解Bean的?
党

13.@Autowired的实现原理了解]
口 14.什么是自动堵配?
15 Bean的作用城有子些?
16 Spring中的单例Bean会存在结
7什么是独环信赖?
1 党Spring怎么解决和环依划0
缓存而不是两

由 内 Spring Boot
由 间 Spring Cloud

由 只 补              CacheBuilder .newBuilderC) .maximumsizei        CacheLoader<lLong，

1413

基础
1.Spring是什么?

Spring 是一个Java 后端开发框架，其最核心的作用是帮我们管理java 对象。

No. 51180




## 第 6 页


效Spring篇V2-让天下所有的面渣都能逆效

其最重要的特性就是 1oC，也就是控制反转。以前我们要使用一个对象时，都要自己先 new 出来。但有了 Spring
之后，我们只需要告诉 Spring 我们需要什么对象，它就会自动帮有我们创建好并注入到 Spring 容器当中。

比如我在一个 Service 类里需要用到 Dao 对象，只需要加个 aautowired 注解，Spring 就会自动把 Dao 克
入到 Spring 容器当中，这样就不需要我们手动去管理这些对象之问的依赖关系了。

回 "aicodne
资源管理器                        上     ) 更新日志    台 LoginServicelmpljava x

Y 文件

paicoding-service

srcjmain

javalcom/github/Jpaicodingjforum

sidebar
@author

sitemap                                                     edate

statistics
user                                        5

converter                                                     攻

repository                                 4 pubtic class                     impLements

service                                   5
让                        6     private       user0ao;
conf

private         UserAiDao7

help
relation

user

@

private               UserSessionHeLper;
台 RegisterServicelmpljava              13        四

 LoginServicelmpljava

台 Userservicelmpljava             4        private                starNumberHetper';
userfoot

whitelist                               66        @
 AuthorWhiteListServicejava          private                    registerService;

另外，Spring 还提供了 AOP，也就是面向切面编程，在我们需要做一些通用功能的时候特别有用，比如说日志记
录、权限校验、事务管理这些，我们不用在每个方法里都写重复的代码，直接用 AOP 就能统一处理。

 LoginServicelmpljava X                                    >> 加
?my/ github / paicoding/ forum / service/ user/ service / user / LoginServicelImpljava/ { com.git

34    pubLic cLass                    impLements               {

61      @

62      @           (roLLbackFor =        .CcLasS)

63     pubtLic    autoRegisterWxUserInfo(     Uuid) {

64                  req = new UserSaveReq() .setLoginType(LoginType:0) .setThird|
65             UserId = register0rGetUserInfo(Creq) ;

66                 .getReqInfo() .setUserId(userId) ;

67         return UserId;

68

Spring 的生态也特别丰富，像 Spring Boot 能让我们快速搭建项目，Spring MVC 能帮有我们处理 web 请求，
Spring Data 能帮有我们简化数据库操作，Spring Cloud 能帮有我们做微服务架构等等。

Spring有哪些特性?

No. 61180





## 第 7 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Spring 的特性还是挺多的，我按照在实际工作/学习中用得最多的几个来说吧。

10C和D1支持

AOP编程支持

   声明式事务支持

快捷测试支持

Spring特性

复杂AP1模板封装

首先最核心的就是 IoC 控制反转和 DI 依赖注入。这个我前面也提到了，就是 Spring 能帮有我们管理对象的创建和依

比如我写一个 UserService，需要用到 UserDao，以前得自己 new 一个 UserDao 出来，现在只要在 UserService
上加个 aservice 注解，在 UserDao 字段上加个 aautowired ，Spring 就会自动帮我们处理好这些依赖关系。

这样代码的耦合度就大大降低了，测试的时候也更容易 mock。

第二个就是 AOP 面向切面编程。这个在我们处理一些横切关注点的时候特别有用，比如说我们要给某些
Controller 方法都加上权限控制，如果没有 AOP 的话，每个方法都要写一遍加权代码，维护起来很麻烦。

No.71180




## 第 8 页


eee 加"icone
资源管理器

Y 文件

paicoding-web
src
main

javalcom/github1paicoding1fo.

component
config
error
front
article
extra
rest
view
ArticleListviewController
ArticleviewControll.， 3
ColumnviewControllerjava
vo
 ArticleDetailvojava
 ArticleEditvojava
 ArticleListvojava

 Columnvojava

pubtic ctass

效Spring篇V2-让天下所有的面渣都能逆效

 ArticleViewControllerjava x

(Crote
(Cpath
edit(@i           required
W ArticLeEdityo
articteId
articte = articLeService.queryDetaitArticteII
vo.setArticte(articte);
if (!      .equats(articte.getAuthor()，

modeL.addAttribute(attribute
return

<        > categoryList = categoryService.LoadAH
categoryList.forEach(s -> {
S.setSeLected(s.getCategoryId().equaLs(articLe.getC才
D;
Vvo.setCategories(categoryList)7
vo.setTags(articLe.getTags(C)) 7

<        > categoryList = categoryService.LoadAL
,SetCategories(categoryList)7
:SetTags((|         .emptyList())7

modeL.addAttribute(attributeNal     ，vo);

return

用了 AOP 之后，我们只需要写一个切面类，定义好切点和通知，就能统一处理了。事务管理也是同样的道理，加

个 arransactional 注解就搞定了。

还有就是 Spring 对各种企业级功能的集成支持也特别好。比如数据库访问，不管我们用JDBC、MyBatis-Plus 还
是 Hibernate，Spring 都能很好地集成。消息队列、缓存、安全认证这些， Spring 都有对应的模块来支持。

No. 81180




## 第 9 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eee 加"aicodno

资源管理器         9 pomxml x

Y 文件                  aicodi      pom.

paicoding-core                                           <project xmLns=

<dependencies>

<dependency>
<scope>compiLe</scope>

srcjmain

javaJjcom/githubJpaicodingjforu

ws                                                        </dependency>

 ForumCoreAutoConfigjava

 package-infojava

<dependency>
resources
<groupId>org.etasticsearch</groupId>

<artifactId>eLasticsearch</artifactId>
9 pom.xml                                                                   j
<version>6.8.2</version>

</dependency>

<dependency>
<groupId>org.eLasticsearch.cLient</groupId>
paicoding-ui                                                                                   <artifactId>eLasticsearch-rest-ctient</artifactId>
<version>6.8.2</version>
</dependency>
<dependency>
<groupId>org.eLasticsearch.cLient</groupId>
<artifactId>eLasticsearch-rest-high-LeveL-cLient</artif;

paicoding-web

src

9 pomxml
README.md
中 .gitattributes

》 大纲

<version>6.8.2</version>
</dependency>

<dependency>
， 时间线                                        <groupTd>cn.hutoot</groupTd>

<artifactId>hutooL-aLL</artifactId>
》 Java Projects                                 </dependency>

另外 Spring 的配置也很灵活，既支持 XML配置，也支持注解配置，现在我们基本都用注解了，写起来更简洁。
Spring Boot 出来之后就更方便了，约定大于配置，很多东西都是开箱即用的。

简单说一下什么是AOP和loCc?

AOP 面向切面编程，简单点说就是把一些通用的功能从业务代码里抽取出来，统一处理。比如说技术派中的
eMdcpot 注解的作用是配合 AOP 在日志中加入 MDSC 信息，方便进行日志追踪。

No. 91180




## 第 10 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

吕 ArticleRestControllerjava x                           Tae McpP   智能体   模型     个义外>

2. MDC信息添加: 通过 加 MdcAspect 切面类实现。
pubtie ctass                                              在被注解的方法执行前，会调用“GO addMdcCode 方法。

该方法会获取 @NMdcDot 注解的 bizcode 属性值。
6de 属性支持SpEL表达式，可以从方法的参数中动态
攻取值。例如，你提供的代码中“bizCode =
"articteTd” 表示从名为 articteId 的方法参数中获

articteId                                       到值

pg                                      获取到的 bizCode 会以键值对"bizCode"，vatue)

本                                     的形式添加到MDC中，通过 |加 MdcUtiladd 实现。

3. 日志记录与清理
(path =          编辑 :添加到对话                 在方法执行后 (无论成功或失败) ，切面会记录方法的执行耗
(bizcode =          ]                                 时。
<          > recommend (人                        如果成功添加了MDC信息 (即 hasiag 为 [ErUg )，则在
                       natty 块中调用 |画 MdcUtilLreset 来清理MDC中的信
                   息，站免对后续日志产生影响。

TIWTLLabLetSize) orELse                总结: BhdcDot(bizCode = “#articteId*j 注解的作用是在

执行被注解的方法时，将方法参数 ,articLeId 的值作为业务标识

(bizCode ) 添加到日志的MDC上下文中。这样，在查看日志时，

可以根据这个 bizCode 快速定位和筛选特定业务操作的日志，非常
有助于问题排查和系统监控

相关文件

。 注解定义: 忌 MdcDotjava

min(sizey
<        > artictes = articLeRecommendService.re
htmL = tempLateEngineHeLper.renderToVo(temptate
,ok(new NextPageHtmLVo(htmL，articLes,getHasNore

loC 控制反转是一种设计思想，它的主要作用是将对象的创建和对象之间的调用过程交给 Spring 容器来管理。比
如说在技术派项目当中， epostconstruct 注解表明这个方法由 Spring 容器在 Bean 初始化完成后自动调用，我
们不需要手动调用 init 方

 ArticleRestControllerjava     Z CategoryServicelmpljava X       > 加

Fum / service 1/ article / service / imply/ 台 CategoryServicelImpljava / 名 CategoryServicelmr

27    ILic cLass                       impLements                  {
39

40    @

pubLic     init() {
42       categoryCaches =          .newBuiLder() .maximumSize(maximumSs
45          @
44          pubLic          1Load(@      Long categoryId) throws
45                      category = categoryDao.getById(categoryId) ;
46            if (category ==     11 category.getDeLeted()
47                 return          .EMPTY;
48
49             return new CategoryDT0(categoryId，category.getCategory
50
51
52

Spring源码看过吗?

No. 10 1180





## 第 11 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

看过一些，主要是带着问题去看的，比如遇到一些技术难点或者想深入理解某个功能的时候。

我重点看过的是 loc 容器的初始化过程，特别是 ApplicationContext 的启动流程。从 refresh() 方法开始，包
括 Bean 的定义和加载、Bean 工厂的准备、Bean 的实例化和初始化这些关键步骤。

三级缓存执行流程
图解源码

Spring 循环依赖
为什么要有 3 级缓存?

能干掉第二级缓存么?

Bean 生命周期执行流程
一 Bean 生命周期       扩展方法
图解源码

三 什么是 AOP?

Spring 源码解析

Spring AOP 一- AOP 工作流程

~ 图解源码

三 基础知识
Spring 事务 一|- 事务工作流程

~ 图解源码

下[ 什么是IOC?
一 Spring IOC      IOC 执行流程

L 图解源码
看源码的时候发现 Spring 用了很多设计模式，比如工厂模式、单例模式、模板方法模式等等，这对我平时写代码
也很有启发。

还有就是 Spring 的 Bean 生命周期，从 BeanDefinition 的创建到 Bean 的实例化、属性注入、初始化回调，再到
最后的销毁，整个过程还是挺复杂的。看了源码之后对 epostconstruct 、&PreDestroy 这些注解的执行时机就
更清楚了。

不过说实话，Spring 的源码确实比较难哺，涉及的概念和技术点太多了。我一般是结合一些技术博客和 Claude 一
起看，这样理解起来会相对容易一些。

PS: 关于这份小册的 PDF 版本，目前只有星球的用户可以获取，后续会考虑开放给大家。

No.111180




## 第 12 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

洛  到ET                                                                                      < 收进专栏

##球友提问从”二哥好，之前在技术派上看到楼仔写了一本《Spring 源码解析手册》，之前的微信链接已经失效了
他说后续会放到知识星球中，但我在星球中还没有找到，请问现在放到星球中了吗。

球友提问全

四

@@asCeGGG3

人 澳默王二: 置责 这个: 链接: 9 https://pan.baidu.com/s/ImGkHxsWQPOIlvSIZm7i9FbA?pw.… 提取码: "mr
1. Java 面试指南 (付费) 收录的京东面经同学 5 java 后端技术一面面试原题: IOC与AOP

memo: 2025年6月15 日修改至此，今天在帮球友们修改简历的时候，碰到一个中山大学本硕的球友，校园荣
誉基本上拉满了，非常优秀，那我也希望能够帮助到更多的球友们，帮他们拿到更好的 offer。

中山大学”985                                           LE 6月
8 9 TFI SI | 可册rr                                 广东深圳
@ 荣誉奖项: 焉迎丰:全:后中山大学优秀研究生奖助金 - 一等奖

中山大学 ”985                                  14Lai .5 上月
河 1 ij- 旦:了 环则Ti 1于L.                        广东深圳

@ ”荣誉奖项: 口sJ -ET于 Lu F中山大学优秀大学生奖学金 二等奖
“王仁着四必学生数学建模 一 F 奖; 总写 于二司大学生数学建模 - 国家二等奖，省一等奖
"Jr "1 工。”竹全国大学生数学竞赛 - 广东省二等奖

2.Spring有哪些模块呢?
我按照平时工作/学习中接触的频率来说一下。

首先是 Spring Core 模块，这是整个 Spring 框架的基础，包含了 locC 容器和依赖注入等核心功能。还有 Spring
Beans 模块，负责 Bean 的配置和管理。这两个模块基本上是其他所有模块的基础，不管用 Spring 的哪个功能都

会用到。

No. 12 1180




## 第 13 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

WebSocket

-人

Transactiol

然后是 Spring Context 上下文模块，它在 Core 的基础上提供了更多企业级的功能，比如国际化、事件传播、资源
加载这些。ApplicationContext 就是在这个模块里面的。

SpringBootaAppPl1ication
public class Application {
Public static void main(String[] args) {
// Spring Boot会自动创建app1icationContext
RpplicationCcontext context = SpringRpplication.run(RPpplication.class，args) 1

Spring AOP 模块提供了面向切面编程的支持，我们用的 arransactional 、自定义切面这些都是基于这个模块。

Web 开发方面，Spring Web 模块提供了基础的 Web 功能，Spring WebMVC 就是我们常用的 MVC 框架，用来处
理 HTTP 请求和响应。现在还有 Spring WebFlux，支持响应式编程。

比如说技术派项目中， GlobalExceptionHandler 类就使用了 eRestcontrolleradvice 来实现统一的异常处
理。

No. 13 1180




## 第 14 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

RestControlleradvice
Public class GlobalExceptionHandler {

eExceptionHandler(Value = ForumRdviceException.class)

public ResVo<String> handleForumRdviceException(ForumRhdviceException e) {

return ResVo.fail(e.getStatus()) 7

数据访问方面，SpringJDBC 简化了jJDBC 的使用，在技术派项目中，我们就 dbcremplate 来检查表是否存在、

执行数据库初始化脚本。

ee 回aicodne

Y 文件                                                  forum    b /config
ForumDataSourceInitiaLizer {
booLean needInit(DataSource dataSource

ing-sen
9 pomxml
paicoding-ui

JdbcTemptLate jdbcTemptate     dbcTemptate(dataSource) ;
luLiquibaseEnabte) {

ithub/paicoding/fo，        8            List List = jdbcTempLate.queryForList("SELECT tabLe_name
admir                      8                  CoLLectionUtitLs.isEmpty(List);
common

component

List<Map<String，0bject>> record = jdbcTemptate.q

6                                CotLectionUtits .isEmpty(record

台 ForumDataSourcelnitia
true;
 GlobalviewConfigjava
台 PaiWebConfigjava
error

front                             0bjects.equats(record           ey:"MD5SUM") ，

jdbcTempLate.update(sqL:"update DATABASECHANGELOG set MD

Spring ORM 提供了对 MyBatis-Plus 等 ORM 框架的集成支持。在技术派项目中，我们就用了 emrableName 、
erableField 等注解进行对象关系映射，通过继承 BaseMapper 来获取通用的 CRUD 能力。

No. 141180




## 第 15 页


面渣逆袭Spring篇

paicoding

资源管理器

github

Y 文件

CategoryDaojava
ColumnArticleDaojava
ColumnDaojava
TagDaojava

口 entity

外 mapper

ArticleDetailMapperjava
ArticleMapperjava

ArticlePayRecordMapperjava

ArticleragMapperjava

CategoryMapperjava

ColumnArticleMapperjava

ColumninfoMapperjava

ReadCountMapperjava

TagMapperjava

V2-让天下所有的面渣都能逆效

ArticleMapperjava x

pubtic interface ArticLeMapper extends BaseHapper<ArticLeD0>

@param

@paranm

@param

Breturn
List<ReadCountD0>                                        (eparam("
@Paranm("
@Param("

ategoryI

gs") Lis

@param
@return

List<YearArticteDT0>              (GParam("userId") Lon

)
am") Pa

List<ArticLeAdminDT0>                         (@Param("

@Paranmf"

(@Param("searchParams") SearchArticLePa

Spring Test 模块提供了测试支持，可以很方便地进行单元测试和集成测试。我们写测试用例的时候经常用

espringBootTest 这些注解。比如说在:    项目

文，进行集成测试。

esSlf4j
espringBootTest(classes

eRunwith(SpringJUnit4C1assRunner.class
{

Public

)}

ouickForumapplication.c

中，我们就用 espringBootTest 注解来加载 Spring 上下

还有一些其他的模块，比如 Spring Security 负责安全认证，Spring Batch 处理批处理任务等等。

现在我们基本都是用 Spring Boot 来开发，它把这些:

模块都整合好了，用起来更方便。

No. 151180




## 第 16 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ee。 日nacoan

加 半天和各                          怠 预疙README.md x

https
和WEB容器实现

Spring应用简化集成

https:JIspringjiolprojectsjspring-boot
开                               记         yjproj
mybatis        数据库orm

mybatis-plus 。 数据库orm杠

件

近实时文本搜索

rabbitmq
mongodb

pomxml

README.md

urlsbdt             docker  应用容器      wdockercom

mn           了                        inxorg

hikaricP    数据库连接            ithub corybrettwooldridgejHikaric

对象存储                help alyun comldocument
，大网                                         0
hp      证书           hpsJhetsencryptorgl
， 时间线
jwt       n重录         hapsJiwtio
， Java projects
                                                      ombok                峭强库        httpsyiprojectlombok org
Naven                                          google开源的java工

eooze

memo: 2025年6月16 日修改至此，今天在帮球友们修改简历的时候，碰到一个大连海事大学硕河南理工大学

本的球友，他荣誉奖项里提到的优秀研究生、奖学金、英语四六级，我希望看到的同学也都能争取一下，不要把这

些荣誉拱手让人，或者压根就不知道，或者不悄于去参加，到时候你简历上这一栏就会比较苍白。

大连海事大学                                                             村
世人一

“荣誉奖项: 中国研究生电子设计大赛技术类竞赛东北赛区一等奖 、目 -
兰业网学爹冰

学业

:优秀研究生、一等

1
级 (509) 、
3.Spring有哪些常用注解呢?

Spring 的注解挺多的，我按照不同的功能分类来说一下平时用得最多的那些。

首先是 Bean 管理相关的注解。 ecomponent 是最基础的，用来标识一个类是 Spring 组件。像 eservice 、
eRepository 、econtroller 这些都是 ecomponent 的特化版本，分别用在服务层、数据访问层和控制器层。

(540) 、全国大学生英语竞赛二等奖

No. 16 1180




## 第 17 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

@Controller

@RestController
@GetMapping

@PostMapping

@RequestMapping

@PutMapping
@DeleteMapping
@ResponseBody
@RequestBody
@Pathvariable

@RestController

@Component
@service

@Repository

@Autowired

@Qualifier

Spring常用注解

@Configuration

@Before
@Around

@PointCut

@Transactional

依赖注入方面， eautowired 是用得最多的，可以标注在字段、setter 方法或者构造方法上。 eoualifier 在有多
个同类型 Bean 的时候用来指定具体注入哪一个。 eResource 和 eautowired 功能差不多，不过它是按名称注入
的。

No. 171180




## 第 18 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ArticleWjriteServicelmpljava x

Service/ src/ main/ java/ com/ github/ paicoding/ forum / service / article / service / im

43   pubLic cLass ArticLeWriteServiceImpL impLements ArticLeWriteService
44

45       private finaL ArticLeDao articLeDao;

46

47       private finaL ArticLeTagDao articLeTagDao;

48

49      QAutowired

50      private CoLumnSettingService coLumnSettingService;
51

52      QAutowired

535      private UserFootService UserFootService;

54

55      QAutowired

56      private ImageService imageService;

57

58      Q@Resource

59       private TransactionTempLate transactionTempLate;

配置相关的注解也很常用。 econfiguration 标识配置类， eBean 用来定义 Bean， evalue 用来注入配置文件
中的属性值。我们项目里的数据库连接信息、Redis 配置这些都是用 evalue 来注入的。 apropertySsource 用来
指定配置文件的位置。

No. 18 1180




## 第 19 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eee 加icodno

搜索

evalue

在凡加各中打开
吕 DynamicConfigContainerjava        2
“bean先加载，此时全大对应的成员属性直.
.加此我们训自定义的配置加吉完之后                   v                   articteReadService;
中 SpringValueprocessorjava pai     3 6
“配置变更注册,找到 本辐且注解修做的配置
“* 成员变量上添加 加1 方式绵定的配轩
gister 有 on field
“通过 加W有有 修饰方法的方式，通过
Jiregister 硬硬硬 on method

userServicei
artictepayDao;

Ilog errorf'ignore 硬硬硬 setter (0, expecti
台 ArticlepayServicelmpljava pai        1
(stview she hosthttpsJipaico ， >
ER    2 1                    payServiceFactory;
(stelasticsearch opentalsej")
v 吕 AbsChatservicejava paicoding-servicel 1

(staimaxNum historyContextCnt10                              Wasperadtuamg mdala，      wento 《

号 DoubaoConfigjava              和                              dbRecord = artictepayDao.queryRecordByhrticteldarticte，ecurrentuerTd);

stdoubaoapi-key)")                              dbRecord ==
(stdoubao aprhosb7)                          return
(stdoubaoend-pono")

~ 吕 shontLinkserviceimpljava         2
本有("sview she hosthttpsipaicoding c.                                  getStatus() .equats(dbRecord .getpayStatus()
硬且面(sfstshor-inkwhielistj'spla()))

台 SitemapServicelmpljava paicoding-ser-， 1

本(stview site hosthttpsipaicoding <

6oosoe

Web 开发的注解就更多了。 eRestcontroller 相当于 econtroller 加 eResponseBody ，用来做 RESTful 接
口。

eee 加icodno

搜索                C 向四品目 有NO

@Restcontroller                     名本六

在凡加各中打开       站
台 AdminLoginControllerjava paicodin- 1 了

@RestController                 xx

吕 ArticlesettingRestControllerjava paico-，1
@RestController

台 AuthorWhiteListControllerjava paica                  priva           userservice
@RestController

台 CategorySettingRestControllerjava pal
@RestController

吕 columnsettingRestControllerjava
@RestController

吕 configSettingrRestControllerjava                                              CR
@RestController

台 GlobalconfigRestControllerjava
@RestController

v 吕 statisticsSettingRestControlerjav。 2                 eparan request

(path = 1

pubtie ctass

togingutservice;

@RestController                   aranm response
吕 TagSettingRestControllerjava paicodi

@RestController
(path                )

> togin                  request，

台 UserSettingRestControllerjava pal
@RestController
response)
v 吕 zsxqwhieListcontrollerjava p
@RestController
台 DictcommonControlerjava
@RestController

台 ImageRestControllerjava p

Usernane = request.getparaneteri

pmd = request.getPparameter|             ;

session = LogingutService.LoginByUserpwdCusername，pwd);
isNotBLank(session)

eoosoe

No. 191180





## 第 20 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eRequestMapping 及其变体 ecGetMapping 、epostMapping 、eputMapping 、8peleteMapping 用来映射

HTTP 请求。 epathvVariable 获取路径参数，

据。
AOP 相关的注解，

型。

easpect 定义切面，

paicoding

搜索

hspect

eReduestParam 获取请求参数，

epPointcut 定义切点，eBefore 、

28 。 EEE

econponent
pubtie ctass AsyncExecutehspect impLements AppLicationContexthmare

eparan
paran

return

throws Throwabte

hround(     ta
pubtic gbject
f 0

(ProceedingJoinPoint
)

returm
]

try 工

return AsyneUtit
tmy
return
)} catch (Throwabte e) {
throw new

1

eaRfter 、

eRequestBody 接收JSON 数

earound 这些定义通知类

) throws Throwabte

不过我们用得最多的还是 erransactional ，基本上 Service 层需要保证事务原子性的方法都会加上这个注解。

生命周期相关的，

espringBootTest 也经常用到。

epPostConstruct 在 Bean 初始化后执行，

No. 201180

epreDpestroy 在 Bean 销毁前执行。测试的时候




## 第 21 页


袭Spring篇V2-让天下所有的面渣都能

eee 加icodno

搜索                C 向目避日 【ORG

@postconstruct                         证 六

在凡加各中打开

吕 ForumCoreAutoConfigjava paicod    1
@postConstruct

吕 DynamicConfigContainerjava
@PostConstruct

台 SensitiveServicejava pa
@PostConstruct

吕 categoryServicelmpljava
@PostConstruct

吕 chatGptintegrationjava
@PostConstruct
@PostConstruct

吕 peepSeekintegration java                                initkeyO 1
@Postconstruct                   cachestream =      newBuitder() .expirehfterWirite

v 吕 XunFeiintegrationjava                                    buitd (new CacheLoadera
@PostConstruct  ，
吕 Notfyservicelmpljava

@PostConstruct
台 PaiWebConfigjava
@PostConstruct

initO {
infoi                                config);

eparam routingkey
Bretun

还有一些 Spring Boot 特有的注解，比如 espringBootapplication 这个启动类注解，
econditionalonProperty 做条件装配， egnableautoconfiguration 开启自动配置等等。

eee 加icodno

搜索                C 所四避日 ERARCRRR

@condiionalonproperty                证 六
impor

import
在凡加各中打开

吕 patasourcecConfigjava          1 1            inpor
ECanidiiianialonipiopany(prefix = "spr，x                  import

台 ElasticsearchConfigjava paicoding-ser-， 1
CHaiiiaialgiipiGBEH(prefi = "elasticse

中 RabbitMaAutoConfigjava paicodi       1
ECGNdiiiaialghipIGDEHB(value = rabbitmaq

台 WxpayConfigjava paicodin           1
CNdiiiaialghipiGpEH(value =- "wxpayen.

prerix

environment;

pubtic patasourceconfig(        environment) {
this.environment = environment
infoi

[
pubtic       dshspectO
return new DshAspect(7

No. 211180





## 第 22 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

memo: 2025年6月17 日修改至此，今天在帮球友们修改简历的时候，碰到一个学院本的球友，他的荣誉奖项
还是 OK的，态度也非常好，之前有学院本球友拿到滴滴 SP offer 的，希望这位球友也能够成为星球里新的榜样。

闽江学院                                                                1
和                                           福建-福州
专业成绩:专业排名前15% (大一16/42;大二6/42) 。

专业课程:数据结构课程设计、JavaEE开发进阶、计算机网络技术、软件测试、数据库课程设计 (MySql、
Oracle) 等7门核心课程均80分以上。

荣誉奖项

全国大学生市场调查与分析大赛 省赛二等奖

优秀学生干部

国家励志奖学金

优秀奖学金三等奖

闽江学院"青年马克思主义者培养工程大学生骨干培训班结业证

4.愉Spring用了哪些设计模式?
Spring 框架里面确实用了很多设计模式，我从平时工作中能观察到的几个来说说。

首先是工厂模式，这个在 Spring 里用得非常多。BeanFactory 就是一个典型的工厂，它负责创建和管理所有的
Bean 对象。我们平时用的 ApplicationContext 其实也是 BeanFactory 的一个实现。当我们通过 eautowired 获
取一个 Bean 的时候，底层就是通过工厂模式来创建和获取对象的。

No. 221180




## 第 23 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Spring用到的设计模式

观察者模式

单例模式也是 Spring 的默认行为。默认情况下，Spring 容器中的 Bean 都是单例的，整个应用中只会有一个实
例。这样可以节省内存，提高性能。当然我们也可以通过 escope 注解来改变 Bean 的作用域，比如设置为
prototype 就是每次获取都创建新实例。

No. 231180




## 第 24 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

({ELementType.TYPE，ELementType.METHOD})
(RetentionPoLicy.RUNTINME)

String vaLue()

SCOPE_:    LETON

Configur  e      ory.SCOPE_PROTOTYPE
PE_SIN6LETON
.Conte
COPE_SESSION

)

String scopeName()

代理模式在 AOP 中用得特别多。Spring AOP 的底层实现就是基于动态代理的，对于实现了接口的类用JDK 动态代
理，没有实现接口的类用 CGLIB 代理。比如我们用 erransactional 注解的时候，Spring 会为我们的类创建一个
代理对象，在方法执行前后添加事务处理逻辑。

模板方法模式在 Spring 里也很常见，比如jdbcTemplate。它定义了数据库操作的基本流程: 获取连接、执行
SQL、处理结果、关闭连接，但是具体的 SQL 语句和结果处理逻辑由我们来实现。

No. 241180




## 第 25 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

> 加
icoding/ forum/ web/ config/ init   ForumDataSourcelnitializer.java   ForumDataSourcelnitializer / @O_ ne
34 Jic cLass ForumDataSourceInitiaLizer

74    private booLean       (DataSource        ) {

75       讨〔             ) 攻

76           return true;

77

78

79       JdbcTempLate

89       if (!LiquibaseEnabLe) {

81

82          List     =          站          "SELECT tabLe_name FROM information
85           return CoLLectionUtitLs .

84

85

86

87      List<Map<String，0bject>>                。         (sqL:"seLect * fr
88       if (CoLLectionuUtitLs.

89

99           return true;

92

935

94      if (0bjects .         。  (Cindex:0) .  (key:"MD5SUM")，b:"8:a1a2d9945b746ad
95

96                  。     sqL:"update DATABASECHAN6GEL06 set MD5SUM='8:bb81b67a5了3
97      }

98       return faLse;

观察者模式在 Spring 的事件机制中有所体现。我们可以通过 ApplicationEvent 和 ApplicationListener 来实现事
件的发布和监听。比如用户注册成功后，我们可以发布一个用户注册事件，然后有多个监听器来处理后续的业务逻
辑，比如发送邮件、记录日志等。

No. 251180





## 第 26 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

paicoding

搜索                                                ConfigRefreshEventListenerjava x

》 。 ApplicationListener        也         jithub

2 文件中有 4 个结果 。。 在编辑器中打开

v 台 ConfigRefreshEventListen.，2             author
org.springframework.context 局         5       edate
-ConfigRefreshEventList
v 台 NotifyMsgListenerjava pa.，2        service
-org.springframework.context 局      6。 pubtic ctLass ConfigRefreshEventListener impLements RES 国cconfiokefrej
NotifyMsgListener<T> implem                      BAutowired
private DynamicConfigContainer dynamicConfigContainer;

@param

Boverride

编辑 关| 添加到对话

pubtic void                      (ConfigRefr-
dynamicConfigContainer.
SpringVaLueRegistry-        (

这些设计模式的应用让 Spring 框架既灵活又强大，也让我在实际的开发中学到很多经典的设计思想。
Spring如何实现单例模式?

传统的单例模式是在类的内部控制只能创建一个实例，比如用 private 构造方法加 static getInstance() 这种
方式。但是 Spring 的单例是容器级别的，同一个 Bean 在整个 Spring 容器中只会有一个实例。

具体的实现机制是这样的: Spring 在启动的时候会把所有的 Bean 定义信息加载进来，然后在
DefaultSingletonBeanRegistry 这个类里面维护了一个叫 singletonObjects 的 ConcurrentHashMap，这个 Map
就是用来存储单例 Bean 的。key 是 Bean 的名称，value 就是 Bean 的实例对象。

No. 26 1180




## 第 27 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

国 nacoduno

回 mm

Hap<string，0bject> ENGIEENODE

当我们第一次获取某个 Bean 的时候，Spring 会先检查 singletonObjects 这个 Map 里面有没有这个 Bean，如果
没有就会创建一个新的实例，然后放到 Map 里面。后面再获取同一个 Bean 的时候，直接从 Map 里面取就行了，
这样就保证了单例。

No. 271180




## 第 28 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

SingletonBeanRegistryjava       ImplicitlyAppearedSingletonException,       @ DefaultsingletonBeanRegistryjava

Q- singletonObjects    局 ce W

DefautLtSingLetonBeanRegistry         SimpLeALiasRegistry           SingLeto 。 阅读器模式

registerSingLeton(String beanName，0bject singLeton0bject)      ILLegatLStateExceptiol

Assert .notNuLL(beanName，，                           )
Assert.notNuLL(singLeton0bject，                                )
(this.EGGGUEEGnObjectg) {
0bject oLd0bject =    .SingUeton0bjects.get(beanName);

(oLd0bject !=    ) 荆
ILLegatLStateException(                         singLeton0bject +
+ beanName +                          + oLd0bject

】

addSingLeton(beanName，singLeton0bject);

beanName
singteton0bject

addSingteton(String beanName，0bject singteton0bject) {
(this.Singteton0bjects) {
.SangUetonobjects.put(beanName，singLeton0bject);
.singLetonFactories.remove(beanName) 1
mLySingUeton0bjects.remove(beanName
gisteredSingLetons.add(beanName) ;

还有一个细节就是 Spring 为了解决循环依赖的问题，还用了三级缓存。除了 singletonObjects 这个一级缓存，还
有 earlySingletonObjects 二级缓存和 singletonFactories 三级缓存。这样即使有循环依赖，Spring 也能正确处
理。

而且 Spring 的单例是线程安全的，因为用的是 ConcurrentHashMap，多线程访问不会有问题。

1.                    收录的携程面经同学 10 java 暑期实习一面面试原题: Spring loC 的设计模式，
AOP 的设计模式

2.                       收录的小公司面经合集同学 1 Java |             : Spring 框架使用到的设计模
式?

3.                   收录的同学 1 贝壳找房后端技术一面面试     Spring用了什么设计模式?

4.                       收录的快手同学 4 一面原题: Spring中使用了哪些设计模式，以其中一种模式举
例说明? Spring如何实现单例模式?

memo: 2025年6月 20 日修改至此，今天             的时候，有碰到重庆邮电大学本，电子科技大学硕的

球友，期间还有过清华大学科研项目的经历，基本上也是把学历这块拉的满中满了，那希望星球能帮助到更多院校
的同学，不管是工作党还是学生党，都希望大家都拿到更好的 offer。

No. 28 1180




## 第 29 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

 国-- 。                                        电子科技大学 (全日制)
通信与信息系统 | 硕士

mm                                                 清华大学 (科研项目)
通信与信息系统 | 硕士

有                                         重庆邮电大学 (全日制)
通信工程 | 本科

5.Spring容器和Web容器之间的区别知道吗? (补充)
2024年7月11 日增补

首先从概念上来说，Spring 容器是一个 loC 容器，主要负责管理 java 对象的生命周期和依赖关系。而 Web 容
器，比如 Tomcat、Jetty 这些，是用来运行 Web 应用的容器，负责处理 HTTP 请求和响应，管理 Servlet 的生命
周期。

xx
* SpringUtil.java
* 用于获取 Spring 容器中的 Bean，技术派源码: https://github .com/itwanger/paicoding
+/
ecomponent
public class SpringUtil implements RARpplicationContextaware {

private volatile static APPLicationContext context1

eoverride
public void setRApplicationContext(RPplicationContext applicationContext) {
SpringUtil.context = applicationContext;

】}

public static <T> T getBean(Class<T> bean) {
return context .getBean(bean) 7

】}

从功能上看，Spring 容器专注于业务逻辑层面的对象管理，比如我们的 Service、Dao、Controller 这些 Bean 都
是由 Spring 容器来创建和管理的。而 Web 容器主要处理网络通信，比如接收 HTTP 请求、解析请求参数、调用相
应的 Servlet，然后把响应返回给客户端。

No. 291180




## 第 30 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

HTTP服务器     ”加       办                  HTTP服务器                                        Servlet接口

问

在实际项目中，这两个容器是相辅相成的。我们的 Web 项目部署在 Tomcat 上的时候，Tomcat 会负责接收 HTTP
请求，然后把请求交给 DispatcherServlet 处理，而 DispatcherServlet 又会去 Spring 容器中查找相应的
Controller 来处理业务逻辑。

xx

* GlobalViewInterceptor.java

* 用于全局拦截器，技术派源码: https://github.com/itwanger/paicoding
二/

ecomponent

public class GlobalViewInterceptor implements HandlerInterceptor {
8Rutowired

Private GlobalInitService globalInitService1

8override
public boolean preHandle(HttpServletRequest request，
HttpServletResponse response，
Object handler) {
// Web 容器的 HTTP 请求 + Spring 容器的业务服务

还有一个重要的区别是生命周期。Web 容器的生命周期跟 Web 应用程序的部署和卸载相关，而 Spring 容器的生
命周期是在 Web 应用启动的时候初始化，应用关闭的时候销毁。

现在我们都用 Spring Boot 了，Spring Boot 内置了Tomcat，把 Web 容器和 Spring 容器都整合在一起了，我们
只需要运行一个jar 包就可以了。

SpringBootRApplication
public class OuickForumRpplication {
public static void main(String[] args) {

Springapplication.run(OuickForumRpplication.class，args) 1

No. 301180




## 第 31 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效
1. Java 面试指南 (付费) 收录的去哪儿同学 1 技术二面原题: spring的容器、web容器、springmvc的容
器之间的区别

memo: 2024年7月11 日修改至此，今天在帮球友们修改简历的时候，磋到北京交通大学本，北京航空航天大
学硕的球友，她的简历上有很多校园荣誉奖项，像优秀学生、奖学金、英语四六级等，这些都是非常好的加分项。

北京航空航天大学 ( 保研) 985                           ie
开本网 ,| 4六荐 硕士 国汪 严一三下是                                        北京
荣誉奖项 : 北航研究生一等学业奖学金 1 ” 5瑟

北京交通大学 211                                                    1088 加 .imr 本
站下目la-, 本科 T ITPE王                                     北京

GPA : 3.83 / 4.00 ”专业排名 : 2/121 ( 前1.6% ) “CET-4 : 528 CET-6 : 474
荣誉奖项 : 国家励志奖学金 北京市优秀毕业生 一等学习优秀奖学金”优秀共青团干部

1oC
6.志说一说什么是loC?

推荐阅读: loC 扫让
loc 的全称是 Inversion of Control，也就是控制反转。这里的“控制'指的是对象创建和依赖关系管理的控制权。

Inversion of Control

k一        Application          一>一         Framework         一外

以前我们写代码的时候，如果 A 类需要用到 B 类，我们就在 A 类里面直接 new 一个 B 对象出来，这样 A 类就控
制了 B 类对象的创建。

No. 311180




## 第 32 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 传统方式: 对象主动创建依赖
Public class UserService {
Private UserDao userDao)

public UserService() {
// 主动创建依赖对象

this.userDao = new UserDaoImp1();

有了 loC 之后，这个控制权就"反转"了，不再由 A 类来控制 B 对象的创建，而是交给外部的容器来管理。

xx
* 使用 Spring IocC 容器来管理 UserDao 的创建和注入
* 技术派源码: https ://github.com/itwanger/paicoding
+/
eservice
public class UserServiceImp1 implements UserService {
8Rutowired
Private UserDao userDao)

// 不需要主动创建 UserDao，由 Spring 容器注入
public BaseUserInfoDTO getandUpdateUserIPInfoBySessionTId(String session，String

clientIP) {
// 直接使用注入的 userDao

return userDao.getBySessionId(session) 7

一-这部分面试中可以不背 start一-
没有1oC 之前:

我需要一个女朋友，刚好大街上突然看到了一个小姐姐，人很好看，于是我就自己主动上去搭训，要她的微
信号，找机会聊天关心她，然后约她出来吃饭，打听她的爱好，三观。。。

有了loc 之后:

我需要一个女朋友，于是我就去找婚介所，告诉婚介所，我需要一个长的像赵露思的，会打 Dota2 的，于是
婚介所在它的人才库里开始找，找不到它就直接说没有，找到它就直接介绍给我

婚介所就相当于一个 IoC 容器，我就是一个对象，我需要的女朋友就是另一个对象，我不用关心女朋友是怎么来
的，我只需要告诉婚介所我需要什么样的女朋友，婚介所就帮我去找。

No. 321180




## 第 33 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

引入10C之前，做饭一一自己买菜、烧火、孝人饭                引入10C之后，饭来张口

-一这部分面试中可以不背 end---

DI和1loC的区别了解吗?

loc 的思想是把对象创建和依赖关系的控制权由业务代码转移给 Spring 容器。这是一个比较抽象的概念，告诉我

们应该怎么去设计系统架构。
"Dependency injection is atechnique in which an object receives other objects
thatit depends on. These other objects are called dependencies.Inthetypical
using' relationship, the receiving object is called a client and the passed (that is，
'injected") object is called a service."

而 D，也就是依赖注入，它是实现 loC 这种思想的具体技术手段。在 Spring 里，我们用 eautowired 注解就是在
使用 DI 的字段注入方式。

eservice

public class RrticleReadServiceImp1 implements RrticleReadService {
Rutowired
private RrticleDao articleDao;  // 字段注入

Rutowired
Private UserDao userDao)

从实现角度来看，DI 除了字段注入，还有构造方法注入和 Setter 方法注入等方式。在做技术派项目的时候，我就
尝试过构造方法注入的方式。

No. 331180




## 第 34 页


paicoding

资源管理器

Y 文件

@SLf人
service
pubtic ctass ArticteWriteServiceImpL impLements ArticLeWriteService

private finat ArticLeDao articte0aoi

|     |      ，          CoLumnsettingService coLumnSettingService
private finat ArticLeTagDao a              上

，                            coLumnSettingService
BAutowired
ArticlePayServi.-                          private CoLumnSettingService COLUmnSettingSer

BAutowired

ArticlesettingS-。                          private UserFootService userFootServicei

ArticlewriteSe
BAutowired

private ImageService imageServicei

BResource

Coumnsetting-                 private TransactionTempLate transactionTempLate

TagServicelmpl…
TagSettingServ…               BAutowired
ArticlePayService.                 private AuthorWhiteListService articLeWhiteListService
大纲
pubtic                        (CArtictepao           ，ArticteTagDao
》 时间线                                                        .articLeDao               ;

.articteTagDao
， Java Projects

然了，DI 并不是实现 loC 的唯一方式，还有 Service Locator 模式，可以通过实现 ApplicationContextAware 接
口来获取 Spring 容器中的 Bean 。

No. 341180




## 第 35 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

paicoding

[六 。 资源管理器       ”swWriteServicelmpljava e
G 国基        CD GED) FE

16 。 @Component
pubtic ctass SpringUtit impLements ApptLicationContextAware，EnvironmenthAware
private votLatite static AppLicationContext context;
private votatite static Environment environment;

Md5Utiljava                  private static Binder binder;

MdImgLoaderjava

override
NumuUtiljava                                 ji

pubtic void                      (CAppticationContext
PriceUtiljava
RandUtiljava                               SpringuUtiL.context =

SessionUtiljava

eoverride
StopWatchUtiljava                      pubtic void                  (Environment
StrUtiljava

TransactionUtiljava
pubtic static AppLicationContext

return contexti

品 ws

ForumCoreAutoConfigj

package-infojava

resources                                                     |

5      pubtic static <T> T      (Cuass<T>
>大纲                      2        if (context != nuLU) {
return context .
} eLse {
throw new

》 时间线
》 Java Projects

》 Maven

之所以ID 后成为 loC 的首选实现方式，是

为代码更清晰、可读性更高。

IoC (控制反转)

|一 pI (依赖注入)         + 主要实现方式
|一 构造器注入
|一 字段注入
[一 setter注入

|一 服务定位器模式

|一 工厂模式

[一 其他实现方式

为什么要使用 loc 呢?
在日常开发中，如果我们需要实现某一个功能，可能至少需要两个以上的对象来协助完成，在没有 Spring 之前，

每个对象在需要它的合作对象时，需要自己 new 一个，比如说 A 要使用 B，A 就对B 产生了依赖，也就是A和B
之间存在了一种耦合关系。

No. 351180




## 第 36 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 传统方式: 对象自己创建依赖

Public class UserService {
private UserDao userDao = new UserDaoImpl1(); // 硬编码依赖

public User getUser(Long id) {
return userDao.findById(id) 7

】}

有了 Spring 之后，创建 B 的工作交给了 Spring 来完成，Spring 创建好了 B 对象后就放到容器中，A 告诉 Spring
我需要 B，Spring 就从容器中取出 B 交给 A来使用。

// Ioc 方式: 依赖由外部注入

aeService

public class UserServiceImp1 implements UserService {
8Rutowired

Private UserDao userDao; // 依赖注入，不关心具体实现

public User getUser(Long id) {
return userDao.findById(id) 7

】}

至于B 是怎么来的，A 就不再关心了，Spring 容器想通过 newnew 创建 B 还是 new 创建 B，无所谓。

这就是 loc 的好处，它降低了对象之间的耦合度，让每个对象只关注自己的业务实现，不关心其他对象是怎么创建
的。

推荐阅读: 孤傲苍狼; 谈谈对 Spring IOC 的理解
. java 面试指南(付费)_收录的小米 25 届日常实习一面原题: 说说你对AOP 和 loc 的理解。
2. java 面试指南 (付费) 收录的小公司面经合集同学 1 Java 后端面试原题: 介绍 Spring loC 和 AOP?

.java 面试指南 (付费) 收录的招商银行面经同学 6 招银网络科技面试原题: SpringBoot框架的AOP、
IOC/DI?

4. Java 面试指南 (付费) 收录的京东面经同学 8 面试原题: IO0C，AOP

.java 面试指南(付费) 收录的快手同学 4 一面原题: 解释下什么是IOC和AOP? 分别解决了什么问题?
IOC和DI的区别?

Wu

mn

memo: 2025年6 月 22 日修改至此，今天有球友发喜报说拿到了两个 offer，一个是做 B 端电商的，另一个是外
企，主要做 Power BlI 的低代码开发，我的建议是去外企，因为实习最重要的是混个 title，有更多的时间，可以去
学习星球里的项目，其实会更实在。

No. 361180




## 第 37 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

二哥，目前拿到了两个offer。第一个是做b端电
商平台，java全栈，好处是离学校很近，不好的
是要实习半年以上。第二个是外企，用微软的
power bi做低代码开发，说是做到了亚太top。
好处是有完整的培训，有外企的特点 (加班和福
利)。下周一还有一个面试，也是做java的，公司
比较大，但是离学校远，拿到了可能得在外面租
房。

觉得第一个比较符合我后面的求职，但是公司
太小，很多dirty work对秋招没什么用处。

所以想请二哥分析一下，该如何选择可以让实习
对秋招的帮助最大

7.能说一下loC的实现机制吗?

好的，Spring loc 的实现机制还是比较复杂的，我尽量用比较通俗的方式来解释一下整个流程。

No. 371180

Pa




## 第 38 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

习 订单 “Bean定义)     山 工厂 (Spring容器) 仓库 (HashMap)
注册       定色           Spring
注册               定义                        rin
Register        Bean              容器                |

资源加载 “实例乔建
获取                    单例                         _            _
Get                 Singleton                    单例        实例缓店

步是加载 Bean 的定义信息。Spring 会扫描我们配置的包路径，找到所有标注了 ecomponent 、eservice 、
eRepository 这些注解的类，然后把这些类的元信息封装成 BeanDefinition 对象。

// Bean定义信息
public class BeanDefinition {

ring beanClassName)    // 类名

ring scope1          // 作用域

lazyInity     // 是否懒加载

] dependson;     // 依赖的Bean

private ConstructorRrgumentValues constructorRrgumentValues; // 构造参数

private

private
Private bool

private

private MutablePropertyValues propertyValues; // 属性值

第二步是 Bean 工厂的准备。Spring 会创建一个 DefaultListableBeanFactory 作为 Bean 工厂来负责 Bean 的创
建和管理。

ee 国oacoano pman                                    uickrorumApplication

efauntistable              wa            piication-config

UserFootMapperxml                有jectp

UserRelationMapperamml

aatchingBeans -put(beanllane，(T) be

paicoding-ui             tream = matehingBeans vatuesC) .strea

paicoding-web                                           lerConparator (matchingBean'

comgihub paicodingforumweb
四admin
回common

回component           amedBeanHotdercTy ni   =        ype，args，nenUniquehshutt

nanedBean |

readobjectlObjectinputstreamj: void        arent = getparentBeanFactory

reReplace0: Object             Defal
javaxnjectprovidercla                                  auttListabteBeanj      ar      ji(requiredrype，args，nonuniquehswutD ;
ableFactories

DefiniuonNames: ListcSting> = new Arrayt

manualsingletonNa                > -=newtink

No. 38 1180




## 第 39 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

第三步是 Bean 的实例化和初始化。这个过程比较复杂，Spring 会根据 BeanDefinition 来创建 Bean 实例。

Bean Initialization Steps

TD    全   foreach bean.…  -1
1          1                                     1
                                                   1          1                     ，
@@一下   Bean Definations                    Post Process        1         1           Instantiate           |
Loaded                      Bean Definitions      1        1             Beans            1
          1                                     ，
|         了      !
"----------   Load Bean Definitions |---------:                                        ，
Dependency                                 Setters              1
Whatyouveseen                                                          Jniection                                                   Called                      1
                                     1
1                                     1
-----------------，                                    1
1                                                                            1
O                   Bean Ready        4                BPP | .| nitializer |二| epp            1
foruse             1                                                                 1
|                         Bean Post Processor                      |
1                                                                            1
站  Createand Initialize Beans | 一
SCALER

Topres

对于单例 Bean，Spring 会先检查缓存中是否已经存在，如果不存在就创建新实例。创建实例的时候会通过反射调
用构造方法，然后进行属性注入，最后执行初始化回调方法。

// 简化的Bean创建流程

public class AbstractBeanFactory {

protected Object createBean(String beanName，BeanDefinition bd) {
// 1. 实例化前处理
Object bean = resolveBeforeInstantiation(beanName，bd) 1;
if (bean != null) {
return beany

// 2 实际创建Bean
return doCreateBean(beanName，bd);

Protected Object docreateBean(String beanName，BeanDefinition bd) {

// 2.1 实例化
Object bean = createBeanInstance(beanName，bd) 1;

// 2.2 属性填充 (依赖注入)

populateBean(beanName，bd，bean) ;

// 2.3 初始化

No. 391180




## 第 40 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Object exposedobject = initializeBean(beanName，bean，bd) 1;
Teturn exposedobject;

】}

依赖注入的实现主要是通过反射来完成的。比如我们用 eautowired 标注了一个字段，Spring 在创建 Bean 的时
候会扫描这个字段，然后从容器中找到对应类型的 Bean，通过反射的方式设置到这个字段上。

你是怎么理解 Spring loc 的?
loC 本质上一个超级工矿，这个工厂的产品就是各种 Bean 对象。

No. 401180




## 第 41 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

调库存

注解告诉工厂: “我要生产什么样的产品，这个产品有什么特性，需要什

我们通过 ecomponent 、eservice 这出
么原材料"。

然后工厂里各种生产线，在 Spring 中就是各种 BeanPostProcessor。比如

RAutowiredRnnotationBeanPostProcessor 专门负责处理 eautowired 注解。

工厂里还有各种缓存机制用来存放产品，比如说 singletonObjects 是成品仓库，存放完工的单例 Bean;
earlySingletonObjects 是半成品仓库，用来解决循环依赖问题。

// Spring单例Bean注册表
public class DefaultSingletonBeanRegistry {

// 一级缓存: 完成初始化的单例Bean

Private final Map<String，Object> singletonObjects = new ConcurrentHashMap<>(256)7

// 二级缓存: 早期暴露的单例Bean (解决循环依赖)

Private final Map<String，Object> earlySingletonObjects = new HashMap<>(16) 7

// 三级缓存: 单例Bean工厂

Private final Map<String，ObjectFactory<?>> singletonFactories = new HashMap<>(16) 17

public object getSingleton(String beanName) {
Object singletonObject = this.singletonObjects.get(beanName) 17
if (singletonObject == null) {
singletonObject = this.earlySingletonObjects.get(beanName);
if (singletonobject == null) {

No. 411180




## 第 42 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ObjectFactory<?> singletonFactory =
this.singletonFactories.get(beanName) 1;
if (singletonFactory != null) {
singletonObject = singletonFactory.getObject();
this.earlySingletonObjects.put(beanName，singletonObject);
this.singletonFactories.remove(beanName))

】}

return singletonObject;

最有意思的是，这个工厂还很智能，它知道产品之间的依赖关系。它会根据依赖关系来决定 Bean 的创建顺序。如
果发现循环依赖，它还会用三级缓存机制来巧妙地解决。

能手写一个简单的 loC 容器吗?
1、首先定义基础的注解，比如说 acomponent 、aautowired 等。

// 组件注解
eTarget(ElementType.TYPE)
eRetention(RetentionPolicy.RUNTIME )
public einterface Component {

)}

// 自动注入注解
eTarget(ElementType.FIELD)
eRetention(RetentionPolicy.RUNTIME )
public einterface Rutowired {

2、核心的 loC 容器类，负责扫描包路径，创建 Bean 实例，并处理依赖注入。

public class SimpleIoc {
// Bean容器
private Map<Class<?>，Object> beans = new HashMap<>())

As
* 注册Bean
/
public void registerBean(Class<?> clazz) {
try {
// 创建实例
Object instance = clazz.getDeclaredConstructor() .newInstance())
beans .put(clazz，instance);
} catch (Exception e) {
throw new RuntimeException( "创建Bean失败: "+ clazz.getName()，e) 7
}
}

No. 421180




## 第 43 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ax

* 获取Bean

*/

esuppressWarnings("unchecked'")

public <T> T getBean(Class<T> clazz) {
return (T) beans.get(clazz);

As
* 依赖注入
/
public void inject() {
for (Object bean : beans.values()) {
injectFields(bean) 1

ax
* 字段注入
*/
Private void injectFields(Object bean) {
Field[] fields = bean.getClass().getDeclaredFields();
for (Field field : fields) {
if (field.isRAnnotationPresent(Rutowired.class)) {
try {
field.setRccessible(true);
Object dependency = getBean(field.getTypel()) 1
field.set(bean，dependency);
} catch (Exception e) {
throw new RuntimeException("注入失败: ”+ field.getName()，e);

3、使用示例，定义一些 Bean 类，并注册到 loc 容器中。

// DRo层
ecomponent
class UserDao 1{
public void save(String user) {

System.out .println("保存用户: ”+ user);

// Service层

ecomponent

class UserService {
8Rutowired
private UserDao userDaoi

No. 431180




## 第 44 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

public void createUser(String name) {
userDao.save(name) 1
System.out .println( "用户创建完成") ;

// 测试
public class Test {
public static void main(String[] args) {
SimpleIoc ioc = new SimpleIoc();

// 注册Bean
ioc.registerBean(UserDao.class))
ioc.registerBean(UserService.class) 1

// 依赖注入

ioc.inject())
// 使用

UserService userService = ioc.getBean(UserService.class) 1

userService.createUser("王二")

4、可以加上组件扫描。

import java.lang.reflect.Field)

import java.util.

public class SimpleIoc {
Private Map<Class<?>，Object> beans = new HashMap<>();

As
* 扫描并注册组件

/

public void scan(String packageName) {

// 简化版: 手动添加需要扫描的类

List<Class<?>> classes = getClassesInPackage(PackageName) )

for (Class<?> clazz : classes) {
if (clazz.isRnnotationPresent(Component.class)) {
registerBean(clazz) 7

】}
}
// 依赖注入
inject() 7
}
xx

No. 441180




## 第 45 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

* 获取包下的类 (简化实现)

/

Private List<Class<?>> getClassesInPackage(String packageName) {
// 面试时可以说: "实际实现需要扫描classpath，这里简化处理"

return Rrrays.asList(UserDao.class，UserService.class) 7

private void registerBean(Class<?> clazz) {
try {
Object instance = clazz.getDeclaredConstructor() .newInstance())
beans .put(clazz，instance);
} catch (Exception e) {
throw new RuntimeException( "创建Bean失败"，e);

esuppressWarnings("unchecked'")
public <T> T getBean(Class<T> clazz) {
return (T) beans.get(clazz) 7

private void inject() {
for (Object bean : beans.values()) {
Field[] fields =- bean.getClass().getDeclaredFields()1
for (Field field : fields) {
if (field.isRnnotationPresent(Rutowired.class)) {
try {
field. setRccessible(true))
Object dependency = getBean(field.getType() );
field.set(bean，dependency) 1;
} catch (Exception e) {
throw new RuntimeException("注入失败"，e) ;

locC 容器的核心是管理对象和依赖注入，首先定义注解，然后实现容器的三个核心方法
依赖注入;关键是用反射创建对象和注入依赖。

注册Bean、获取Bean、

memo: 2025年6月23 日修改至此，今天有球友发喜报说拿到了京东的社招 offer，这真的要恭喜他，也希望所
有看到这里的小伙伴都能有一个好的结果。

No. 451180




## 第 46 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

同音耿一 @丛信                                                机

《                                            ]
京东录用通知
日2     7

东子的下来了饼)

恭喜啊

8.说说BeanFactory和ApplicantContext的区别?

BeanFactory 算是 Spring 的心脏"，而 ApplicantContext 可以说是 Spring 的完整"身躯"。

No. 46 1180




## 第 47 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

BeanFactory 提供了最基本的 loC 能力。它就像是一个 Bean 工厂，负责 Bean 的创建和管理。他采用的是懒加载
的方式，也就是说只有当我们真正去获取某个 Bean 的时候，它才会去创建这个 Bean 。

No. 471180




## 第 48 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

运行期向容器注册单实例
 Bean的方法

inferfacen

SingletionBeanRegistry
个

父子级联IOC容器的接口

interfacey
HierarchicalBeanFactery

让当  增强

inferfacey

ConfigurableBeanFactery
企

inferfacey
ListableBeanFacfory

动装配的方法            ;
inferfacew
AutewireCapbleBeanFactery
本

向容器注册Bean定义

interfacey

winterfacey

ConfigurableListableBeanFactory

clasey
XmlBeanFactory

它最主要的方法就是 getBean() ，负责从容器中返回特定名称或者类型的 Bean 实例。

public class BeanFactoryExample {
Public static void main(String[] args) {
// 创建 BeanFactory
DefaultListableBeanFactory beanFactory = new DefaultListableBeanFactory() 1

// 手动注册 Bean 定义
BeanDefinition beanDefinition = new RootBeanDefinition(UserService.class)1
beanFactory.registerBeanDefinition("userService"，beanDefinition) 7

// 懒加载: 此时才创建 Bean 实例

UserService userService = beanFactory.getBean("userService"，UserService.class))

ApplicationContext 是 BeanFactory 的子接口，在 BeanFactory 的基础上扩展了很多企业级的功能。它不仅包含
了 BeanFactory 的所有功能，还提供了国际化支持、事件发布机制、AOP、JDBC、ORM 框架集成等等。

No. 48 1180




## 第 49 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

让容器拥有冯布应用上
下文事件的功能
inferfacey                                                                                                                                  inferfacey
ApplicafionEventPublisher                                                                                                                       ResourceLoader

interfacey
| 为应用提供isn国际化消                  HierarchicalBeanFactory       |  证二   四
壹件政径某义配置文件

息访问的功|
winterface                                                                                                                                  interfacey
Message5ource                                                                                                                        ResourcepPatternResolver

winterfacew                                                            个

ApplicationContext
人

可用于控制异步处理过程
具有启动、惠新和关闭应用                                                                        本
上于坟的能力                                                                    2
Cr                                                  人
ConglgurableApplicarionConfext
不

ApplicationContext 采用的是饿加载的方式，容器启动的时候就会把所有的单例 Bean 都创建好，虽然这样会导致
启动时间长一点，但运行时性能更好。

econfiguration
public class AppConfig {
eBean
Public UserService userService() {
return new UserService())

public class ApplicationContextExample {
public static void main(String[] args) {
// 创建 ApplicationContext，启动时就创建所有 Bean
RpplicationContext context = new
RnnotationConfigRpplicationContext(RPpConfig.class) 1

// 获取 Bean

UserService userService = context.getBean(UserService.class) 1

// 发布事件

context .publishEvent(new CustomEvent("Hello World"));

No. 49 1180




## 第 50 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

从使用场景来说，实际开发中用得最多的是 ApplicationContext。像 AnnotationConfigApplicationContext、
WebApplicationContext 这些都是ApplicationContext 的实现类。

另外一个重要的区别是生命周期管理。ApplicationContext 会自动调用 Bean 的初始化和销毁方法，而
BeanFactory 需要我们手动管理。

在 Spring Boot 项目中，我们可以通过 aautowired 注入 ApplicationContext，或者通过实现
ApplicationContextAware 接口来获取 ApplicationContext。

paicoding

口 。 资源管理器

Q ~ 文件           github ，paicoding ，forum /core ，autocel  DynamicConfigC   va ， 1) comgithub.paicodingforur

朵    白                        Component
牟 docs                     8 。 pubtic ctass DynamicConfigContainer impLenents EnvironmentAware，AppticationContexthAware，Command
襄                          39       private ConfigurabteEnvironment environment;

忆                                 private AppticationContext appticationContext;

cetter
pubtic Map<String，0bject> cache;

白                         7        private DynamicConfigBinder binder;
ConfigRefreshEve

DynamicConfigBin

cetter
private Map<CLass，RunnabLe> refreshCaLUback = Haps

common

Boverride
pubtic void            (Environment
-environment = (ConfigurabLeEnvironment)
permission
Boverride
pubtic void                 (AppticationContext               ) throws BeansExceptio
appticationContext =

1.                         收录的美团同学 2 优选物流调度技术 2 面面试原题: BeanFactory和
ApplicationContext
memo: 2025年6月25 日修改至此，今天给一个华科本硕研 0 的           后，发来这样的感慨，要是早点
知道你的网站和星球就好了，       不比外卖强多了? 再次感谢二哥。

显 沉蒜王二

非常感谢二哥的建议，我会修改在简历上的。实习方面，因为算法刷的不是很熟，所以优先想到的是中小厂，而且个人感觉
现在时间非常晚，有地方能实习也不错了哈哈哈。对于这个方面，您觉得呢? 总的来说还是开始的太晚，并且之前走了太多|
弯路，要是早点知道您的网站和星球就好了，技术派不比外卖点评强多了? 再次感谢二哥。

9.去项目启动时Spring的IloC会做什么?

第一件事是扫描和注册 Bean。locC 容器会根据我们的配置，比如ecomponentscan 指定的包路径，去扫描所有标
注了 ecomponent 、eservice 、econtroller 这些注解的类。然后把这些类的元信息包装成 BeanDefinition 对
象，注册到容器的 BeanDefinitionRegistry 中。这个阶段只是收集信息，还没有真正创建对象 。

No. 50 1180




## 第 51 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ResourceLoader                   ooxApPlicationContext

BeanDefigitationReader

第二件事是 Bean 的实例化和注入。这是最核心的过程，IoC 容器会按照依赖关系的顺序开始创建 Bean 实例。对
于单例 Bean，容器会通过反射调用构造方法创建实例，然后进行属性注入，最后执行初始化回调方法。

在依赖注入时，容器会根据 eautowired 、eResource 这些注解，把相应的依赖对象注入到目标 Bean 中。比如
Userservice 需要 UserDao，容器就会把 UserDao 的实例注入到 UserService 中。

说说Spring的Bean实例化方式?

Spring 提供了 4 种方式来实例化 Bean，以满足不同场景下的需求。

第一种是通过构造方法实例化，这是最常用的方式。当我们用 ecomponent 、eservice 这些注解标注类的时候，
Spring 默认通过无参构造器来创建实例的。如果类只有一个有参构造方法，Spring 会自动进行构造方法注入。

No. 511180




## 第 52 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eservice
public class UserService {
private UserDao userDaoi

public UserService(UserDao userDao) {  // 构造方法注入
this.userDao = userDao)

第二种是通过静态工厂方法实例化。有时候对象的创建比较复杂，我们会写一个静态工厂方法来创建，然后用
eBean 注解来标注这个方法。Spring 会调用这个静态方法来获取 Bean 实例。

econfiguration
public class Appconfig {
eBean
public static DataSource createDataSource() {
// 复杂的pataSource创建罗辑

return new HikariDataSource() 1

第三种是通过实例工厂方法实例化。这种方式是先创建工厂对象，然后通过工厂对象的方法来创建Bean ::

econfiguration
Public class Appconfig {
Bean
Public ConnectionFactory connectionFactory() {
return new ConnectionFactory();

Bean
public Connection createConnection(ConnectionFactory factory) {
return factory.createConnection() 7

第四种是通过 FactoryBean 接口实例化。这是 Spring 提供的一个特殊接口，当我们需要创建复杂对象的时候特别
有用:

No. 52 1180




## 第 53 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ecomponent

public class MYFactoryBean implements FactoryBean<MyObject> {
eoverride
public MyObject getobject() throws Exception {

// 复杂的对象创建逻辑

return new MyObject() 7

】}

eoverride
public class<?> getObjectType() {
return MyObject.class1
}
}

在实际工作中，用得最多的还是构造方法实例化，因为简单直接。工厂方法一般用在需要复杂初始化远辑的场景，
比如数据库连接池、消息队列连接这些。FactoryBean 主要是在框架开发或者需要动态创建对象的时候使用。

Spring 在实例化的时候会根据 Bean 的定义自动选择合适的方式，我们作为开发者主要是通过注解和配置来告诉
Spring 应该怎么创建对象。

1. Java 面试指南 (付费) 收录的华为面经同学 8 技术二面面试原题: 说说 Spring 的 Bean 实例化方式

2. java 面试指南 (付费) 收录的美团同学 2 优选物流调度技术 2 面面试原题: bean加工有哪些方法?

memo: 2025年6月27 日修改至此，今天看到有球友发的 offer 选择提问贴，其中一个是杭州六小龙群核科技，
我个人认为还是非常值得去的，毕竟是杭州的独角兽公司，薪资待遇都不错。

本，  wo                                                              区 收进专栏

人3 #了晒个offer点

二哥和球友们您好，我是本二qs50硕，因为找工作开始的晚加上祸"*:交鲍了，准备不充
分，导致手里的offer不太好，想请您帮忙选一下offer:

1. 杭州六小龙，群核科技，base杭州，后端开发，酷家乐后台核心组，薪资nx14+期权 (每
年回购能有5万，且公司计划上市了) ，弹性打卡10-7-5。技术栈属于主流java技术栈，公
司也往Al上靠拢，最近看公司动作很多，感觉公司可能希望在ai时代做出一些改变。可能对
未来个人技术栈有好处，并且个人也很喜欢计算机图形学和演染方面的。听说公司开发氛围
融洽。缺点是过去人员变动比较大，而且不确定公司未来发展如何，平台不知道能不能有背
书

10.你是怎么理解Bean的?

在我看来，Bean 本质上就是由 Spring 容器管理的java 对象，但它和普通的 Java 对象有很大区别。普通的 java
对象我们是通过 new 关键字创建的。而 Bean 是交给 Spring 容器来管理的，从创建到销毁都由容器负责。

No. 53 1180




## 第 54 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Bean Initialization Steps

foreachbean |

-              Post Process 国宝

|

@ 。                  Bean     ”。
DeHmitions      “

"Load Bean Definitions "7    9

Dependency    "

What you've seen before                     Jnjection        全

从实际使用的角度来说，我们项目里的 Service、Dao、Controller 这些都是 Bean。比如 UserService 被标注了
eservice 注解，它就成了一个 Bean，Spring 会自动创建它的实例，管理它的依赖关系，当其他地方需要用到
UserService 的时候，Spring 就会把这个实例注入进去。

Q@ControLLer

G@RequestMapping(path = "articLe")

BaseViewControLLer 并
G@Autowired
ArticLeReadService

G@Autowired

CategoryService

Q@Autowired
TagService

G@Autowired

UserService

这种依赖注入的方式让对象之间的关系变得松耦合。
Spring 提供了多种 Bean 的配置方式，基于注解的方式是最常用的。

No. 54 1180




## 第 55 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

基于注册
( @Ccomponent)

基于XML配置的方式在 Spring Boot 项目中已经不怎么用了。Jjava 配置类的方式则可以用来解决一些比较复杂的
场景，比如说主从数据源，我们可以用 eprimary 注解标注主数据源，用 eoualifier 来指定备用数据源。

econfiguration
public class AppConfig {

eBean

eprimary  // 主要候选者

Public DataSource primaryDataSource() {
return new HikariDataSourcel();

eBean
eoualifier("secondary")
public DataSource secondaryDataSource() {

return new BasicDataSource() 7

那在使用的时候，当我们直接用 eautowired 注解注入 DataSource 时，Spring 默认会使用 HikariDataSource;
当加上 eoualifier("secondary") 注解时，Spring 则会注入 BasicDataSource。

Rutowired
Private DataSource dataSource; // 会注入 primaryDataSource (因为有 eprimary)

Rutowired
eoualifier("secondary")
Private DataSource secondaryDataSource;

@Component 和@Bean 有什么区别?

No. 55 1180




## 第 56 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

首先从使用上来说， ecomponent 是标注在类上的，而 eaBean 是标注在方法上的。 ecomponent 告诉 Spring 这
个类是一个组件，请把它注册为 Bean，而 eBean 则告诉 Spring 请将这个方法返回的对象注册为 Bean 。

全夫定

ecomponent
public class UserService {
8Rutowired

Private UserDao userDao

econfiguration
public class AppConfig {
eBean

Public DataSource dataSource() {

HikariDataSource ds = new HikariDataSource();
ds.setJdbcUr1l(                                                          ) 7
ds .setUsername           ) 7

ds .setPassword(              ) 7

return ds)

从控制权的角度来说， ecomponent 是由 Spring 自动创建和管理的。
回 "aicodino

资源管理器                                   人          台 UserPwaEncoderjava x

v 文件          ding-ser  rc main /jav

paicoding-service

srcjmain
java/jcom/github/p
@author

statistics
statistics                      edate

service
user                                      @
converter                          pubtic
repository
service
ai
conf                                            @         (
help                                private
台 StarNumber.
己 UserpwdEnc.

台 UserRandom.

@         (
private       SaLtIndex;

豆 UserSessio

pubtic      match     puainpwd      encPwd) {
Telation         28        return      .equaLs(encPwd(pLainPwd] ，encPwd);

而 eBean 则是由我们手动创建的，然后再交给 Spring 管理，我们对对象的创建过程有完全的控制权。

No. 56 1180




## 第 57 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ee 加"aicodno

资源管理器               人     ? ElasticsearchConfigjava e@
Y 文件

stf全
enata
configuration

BConditionaLOnProperty(prefix    asticsearch"，name = ”open
BConfigurationProperties(       etasticsearch)

TagServicejava                                                                    ;
ELasticsearchConfig {

TagSettingServi                   四

[WE   "restHighLeveLCLient"
ResthighLeveLCLient resthighl
7 ElasticsearchC.-

repository
String host = hosts.            [6];

String port = hosts.            [1];
HttpHost httpHost = new HttpHostChost，Integer.parseInt(port));

security
service

constant

RestCtientBuitder buitder = RestCLient.buitder(httpHost);

》
j                                                 CredentiaLsProvider credentiatLsProvidei

             et a  ler .setCredentiaLs(AuthScope.ANY
时间线                             credentiaLsProvider.setCredt      Authscope .ANY，

>》 Java Projects

buitder   questConfigCaLLback(requestConfigBuitder

1. Java 面试措
@Bean 的区别

(付费) 收录的京东面经同学 9 面试原题: 怎么理解spring的bean，@Component 和

memo: 2025年6月28 日修改至此，今天在帮球友修改简历的时候，又碰到一个杭电本硕的球友。我这里想说
的一点是，杭电的计算机专业非常强，虽然他只是一所双非，如果能把项目经历、专业技能好好写的话，拿个大厂

的顶级 offer 是完全没问题的。

杭州电子科技大学 (硕士)                     计算机技术                                    2023-09~至今
杭州电子科技大学 (本科)                 计算机科学与技术                           2019-09~2023-07

11.闪能说一下Bean的生命周期吗?
推荐阅读: 三分恶: Spring Bean 生命周期
好的。

Bean 的生命周期可以分为 5 个主要阶段，我按照实际的执行顺序来说一下。

No. 571180




## 第 58 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

Bean生命周期

实例化                                使用中      销毁

第一个阶段是实例化。Spring 容器会根据 BeanDefinition，通过反射调用 Bean 的构造方法创建对象实例。如果
有多个构造方法，Spring 会根据依赖注入的规则选择合适的构造方法。

|                                         三: Initialization

一: instamtiate

实例化

实例化Bean

注册Destruction相关回
调接口

4、BeanPostProcessor 前

置处理
四: Desturction
销毁
5、是否实现                                     |
JInitailizinBean接口                                                                                                   1
是 间    可

DisposableBean接口

2、设置对象属性

了
EGRhoa                                             10. 是否配置自定义的

dcstory-method

7、BeanPostProcessor
后秆处理                                              人

No. 581180




## 第 59 页


面:

第二阶段是属性赋值。这个阶段 Spring 会给 Bean 的属性黑值，包括通过 eautowired 、eResource 这内

入的依赖对象，以及通过 evalue 注入的配置值。

上 Maven
Maven，
Ma

用 Maven
Mav

星 Ma，

有 Maven

ork bootspring
en               ork datal
en               orkplugin:
orkcplugin:sprin
orkcspring-aoi

ring-plugin-c
plugin-mets

有 Maven

目 spring-bean:
有 META-INF

ingframework beans

nDefinitionBuild;
nDefinitionDefault
全BeanDefinitionOverrideException
记BeanDefinitionReade
但BeanpefinitionRead

记BeanDefinitionRegi

全BeanDefinitionR
Rie                          Exception
全BeanDefinitionvalueResolver

initionValidati

rator

glnstantiationsStrat

。 apostconstruct 标注的方法
。 InitializingBean 接口的 afterPropertiesSet 方:
。 通过 epean 的 initMethod 指定的初始化方法

效Spring篇V2-让天下所有的面渣都能逆效

a [Maven: org.springframeworkcspring-bean

G G -册肌
e

beanName
mbd
args

BeanCreationException

protected         beanName，

throws                                                  {

BeanWrapper instanceWrapper = nu11
if (mbd。          () T

instanceWrapper - this.factoryBeanInstanceCache.
}

if (instanceWrapper
instanceWrapper

mol
(beanName，mbd，arg 名
}
bean =- instanceWrapper.             ()
beanType =- instanceWrapper .
i7 (beanType          .class) {

mbd.resotvedTargetType - beanType

()
}

synchronized (mbd.postProcessingLock) {
if (!mbd.postProcessed) {
try 于

】
catch 《        ex) 工
throw new BeanCreationException(mbd.

No. 591180




## 第 60 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

AbstractApplicationContext                                         AbsttactBeanFactory

四 fnishBeanFactoryInitialization

el(beanName，mbd，a

.populateBean(beanName ，mbd，instanceW

我在项目中经常用 epostconstruct 来做一些初始化工作，比如缓存预加载、DB 配置等等。

// categoryServiceImp1中的缓存初始化
PostConstruct
public void init() {
categoryCaches = CacheBuilder.newBuilder() -maximumsize(300) .build(new

CacheLoader<Long，CategoryDTO>() {
eoverride
public CategoryDTO load(eNotNul1 Long categoryId) throws Exception {

CategoryDO category = categoryDao.getById(categoryId);
/1

)) 7

// Dynamicconfigcontainer中的配置初始化
BePostConstruct
public void init() {
cache = Maps.newHashMap())
bindBeansFromLocalCache("dbconfig"，cache);

初始化后，Spring 还会调用所有注册的 BeanPostProcessor 后置处理方法。这个阶段经常用来创建代理对象，比
如 AOP 代理。

第五阶段是使用 Bean。比如我们的 Controller 调用 Service，Service 调用 DAO 。

// Usercontroller中的使用示例

No. 601180




## 第 61 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Rutowired

Private UserService userServicey

eGetMapping("/users/{fid}")

Public UserDTO getUser(epathVariable Long id) {
return userService.getUserById(id))

}

// UserService中的使用示例

eautowired

private UserDao userDao

public UserDTO getUserById(Long id) {
return userDao.getById(iad) 17

}
// UserDao中的使用示例
Rutowired
private JdbcTemplate jdbcTemplatey
public UserDTo getById(Long id) {
String sql = "SELECT * FROM users WHERE id = ?"1
return jdbcTemplate.queryForObject(sql，new Object[]{fid}，new UserRowMapper()) 7

最后是销毁阶段。当容器关闭或者 Bean 被移除的时候，会依次执行:
epPreDpestroy 标注的方法
。 DisposableBean 接口的 destroy 方法
。 通过 eBean 的 destroyMethod 指定的销毁方法

No. 611180




## 第 62 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ationContextjava [Mavens org.springframework:spring-context:5

context ) suppert ) 中            leeearmast v        -用 邮

Wardownhook
aoverride
public void cLose() { [CompIEXI

synchronized (this.startupShutdownMonitor) {

9

有Maven: or
目 spring

MET
if (this.shutdownHook 关 nuLD) 并

try 并

()，                (this.sh呈
}
catch《

}

/deprecationy
protected void doctoseq() {

if (tnis.active.get()    this.cLosed，

if (Logger.             () 工
1ogger     (            this)

人GEmbedd
各Fi
后GenericApp

竺

())

Ron
口 Auo feicns fmshed                                   8    UrF-8 4spaces_ 了man

Aware 类型的接口有什么作用?

Aware 接口在 Spring 中是一个很有意思的设计，它们的作用是让 Bean 能够感知到 Spring 容器的一些内部组件。

从设计理念来说，Aware 接口实现了一种"回调"机制。正常情况下，Bean 不应该直接依赖 Spring 容器，这样可以
保持代码的独立性。但有些时候，Bean 确实需要获取容器的一些信息或者组件，Aware 接口就提供了这样一个能
力。

我最常用的 Aware 接口是 ApplicationContextAware，它可以让 Bean 获取到 ApplicationContext 容器本身。

No. 621180




## 第 63 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

paicoding

v 文件

conponent
Pubtie cuass BE inptaaants Mppticetioncantaxthwarey EnViranaenthaars
private votatite static Appticationcontext context;
private votatite statie Enviranaant enviranaeant:

Md5Utiljava
MadimgLoaderjava              private static Binder binder)

Numutiljava
override

pubtic void                (CAppticationContext             ) throws BeansException {

PriceUtiljava
RandUtiljava

onUtiHjava
ENDUER .cotext -

了
Springutiljava

StopWatchutiljava               override
Strutijava                      pubtic void             (Environment
Transactionutiljava                 STREILenvironnent -

日 we                           binder = Binder.get(        5

ForumCoreAutoconfigj
package-infojava

return

时间线
pubtic static AppticationContext

Java Projects                                            return context

Maven

在             中，我就通过实现 ApplicationContextAware 和 EnvironmentAware 接口封装了一个 SpringUtil 工
具类，通过 getBean 和 getProperty 方法来获取 Bean 和配置属性。

// 静态方法获取Bean，方便在非Spring管理的类中使用

public     > <T> 了      (Class<T> clazz) {

hn context .getBean(clazz) 1

// 获取配置属性

Public

tatic String         (String key) {
return environment .getProperty(key) 7

如果配置了 init-method 和 destroy-method，Sspring 会在什么时候调用其配置的方法?

init-method 指定的初始化方法会在 Bean 的初始化阶段被调用，具体的执行顺序是:
。 先执行 epostConstruct 标注的方法

es。 然后执行 InitializingBean 接口的 afterPropertiesset() 方法

。 最后再执行 init-method 指定的方法

也就是说，init-method 是在所有其他初始化方法之后执行的。

ecomponent

public c

Rutowired

No. 631180




## 第 64 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Private UserDao userDao)

PostConstruct
Public void postConstruct() {
System.out .println("1. 6PostConstruct执行") 7?

public void customInit() { // 通过eaBean的initMethod指定
System.out .println("3。 init-method执行") ;

econfiguration
Public class Appconfig {
eBean (initMethod = "customInit")
public MyService myService() {
return new MyService() 7

destroy-method 会在 Bean 销毁阶段被调用。

ecomponent
Public class MyService {
PreDestroy
public void preDestroy() {
System.out .println("1. 6PreDestroy执行") 7

Public void customDestroy() { // 通过eBean的destroyMethod指定
System.out .println("3。. destroy-method执行") ;

不过在实际开发中，通常用 epostconstruct 和 epreDpestroy 就够了，它们更简洁。

1. java 面试指南 (付费) 收录的小米 25 届日常实习一面原题: 说说 Bean 的生命周期

2. java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: Spring中bean生
命周期

3. Java 面试指南 (付费) 收录的8 后端开发秋招一面面试原题: 讲一下Spring Bean的生命周期
4. java 面试指南 (付费) 收录的同学 1 贝壳找房后端技术一面面试原题: bean生命周期

5. java 面试指南 (付费) 收录的快手同学 4 一面原题: 介绍下Bean的生命周期? Aware类型接口的作
用? 如果配置了init-method和destroy-method，Spring会在什么时候调用其配置的方法?

memo: 2025年6月30 日修改至此。昨天有读者发消息说有三个 offer     ，中科大读博、中海油、商飞北
研，问我该怎么选择? 说实话，这三个都是非常优质的选择，我个人的建议是优先考虑中科大读博，毕竟是国内顶
尖学府，博士毕业后可以选择在高校任教，会更符合他的家庭条件，当然了，我深知，读博的产出压力非常大。

No. 641180




## 第 65 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

求小红书的朋友们给点建议

辆中科大人了 让5 时硬-7 -四

回中海油 全于 Fn   四
南，做智能化征王中。 用于计FE开本让一
硕士正常待遇

回商飞北厂，有IEES “0 -1 上
五年服务期, fw” 。 到"

我帮 国生下” 一生 导电相 ”9 一时各
期。且。 国 三

中 且帮本本.国。 国”请时了 “出
去，有9 国下”中"二2

咏e 一国半二国辐有PE” .晶是这

个等让 .9 本上用 忆-9 吕-“二=二实在
是周呈 上 < -PE 二有FE JI 差，

不知 国有上服量国有.属” 腿王 昌叶得

我人 JE 人” 国有隔用呈和且弃向
我习

这 上 上站“晤HE .1 “吉我和
我女朋友真的纠结死了，还求各位大佬给点意见网

二哥，这是我找工作的情况，很着急，您能帮有我
参考下吗

昨天 14:48

哇二哥，回我了

我家里父母都是老师，对我的选择都很支持，没
有顾虑
12.为什么IDEA不推荐使用@Autowired注解注入Bean?

No. 651180




## 第 66 页


前情提要:

pubtic ctas
Autowi

prival

eov
pubti
R
t

面;

逆袭Spring篇V2-让天下所有的面渣都能逆袭

当使用 eautowired 注解注入 Bean 时，IDEA 会提示"Field injection is not recommended"。

SS RequestCountServiceImpL impLements RequestCountSer

Field injection is not recommended

Documented
pubtic @interface Autowired
extends java.Lang.annotation.Annotation

Marks a constructor, field, setter method, or config method as to be autowired by Spring's dependency injection facilities. This is an

alternative to the JSR-330 javaxinject Inject annotation, adding required-vs-optional semantics
Autowired Constructors

Only one constructor of any given bean class may declare this annotation with the              attribute set to trus ,indicating the
constructor to autowire when used as a Spring bean. Furthermore,ifthe required attributeis setto true ,only a single constructor may
be annotated with BRUtowired . If multiple non-required constructors declare the annotation, they will be considered as candidates for
autowiring. The constructor with the greatest number of dependencies that can be satisfied by matching beans in the Spring container will
be chosen.If none of the candidates can be satisfied, then a primaryjdefault constructor (if present) will be used,. Similarly ifa class declares
multiple constructors but none of them is annotated with BRUtoWired , then a primary/default constructor (if present) will be used.ifa class
only declares a single constructor to begin with it will aways be used, evenif not annotated. An annotated constructor does not have to be
public.

Autowired Fields
Fields are injected right after construction of a bean, before any config methods are invoked. Such a col

Autowired Methods

面试回答:
主要有几个原
第一个是字段注入不利于单元测试。字段注入需要使用反射或 Spring 容器才能注入依赖，测试更复杂; 而构造方

法注入可以

Test

直接通过构造方法传入 Mock 对象，测试起来更简单 。

Public void testUserService() {

UserService userService = new UserService() 1

ReflectionTestUtils.setField(userServicey

Mockito.mock(UserRepository.class)) 7

userService.doSomething() 7

Test

Public void testUserService() {

UserRepository mockRepository = Mockito.mock(UserRepository.class))

UserService userService = new UserService (mockRepository) 7

No. 66 1180




## 第 67 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

第二个是字段注入会隐藏循环依赖问题，而构造方法注入会在项目启动时就去检查依赖关系，能更早发现问题。
第三个是构造方法注入可以使用 final 字段确保依赖在对象创建时就被初始化，避免了后续修改的风险。
在技术派项目中，我们已经在使用构造方法注入的方式来管理依赖关系。
@SLf4]j
Service
CountServiceImp1L            CountService f
UserFootDao            ;
CountServiceImpL(UserFootDao UserFootDao) 攻
= USerFootDao ;

不过话说回来， eautowired 的字段注入方式在一些简单的场景下还是可以用的，主要看团队的编码规范吧。
@Autowired 和 @Resource 注解的区别?

涡，eautowired 是 Spring 框架提供的注解，而 aeResource 是java EE 标准提供的注解。换句话
说，eResource 是JDK 自带的，而 eautowired 是 Spring 特有的。

虽然 IDEA 不推荐使用 aautowired ，但对 aeResource 注解却没有任何提示。
QQResource

UserReLationDao

QResource

ArticLeDao

QResource

CommentReadService

GResource

照类型，也就是 byType 进行注入，而 eResource 默认按照名称，也就是

No. 671180





## 第 68 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

当容器中存在多个相同类型的 Bean， 比如说有两个 UserRepository 的实现类，直接用 aautowired 注入
UserRepository 时就会报错，因为 Spring 容器不知道该注入哪个实现类。

ecomponent
public class UserRepository21 implements UserRepository2 {]}

ecomponent
public class UserRepository22 implements UserRepository2 {]}

ecomponent
public class UserService2 {
8Rutowired

private UserRepository2 userRepository; // 冲突

这时候，有两种解决方案，第一种是使用 aautowired + eoualifier 指定具体的 Bean 名称来解决冲突。

ecomponent ( "userRepository21")
public class UserRepository21 implements UserRepository2 {

)}

ecomponent ( "userRepository22")
public class UserRepository22 implements UserRepository2 {

)}

eautowired
eoualifier("userRepository22")
private UserRepository2 userRepository221

第二种是使用 eResource 注解按名称进行注入。

eResource(name = "userRepository21")
Private UserRepository2 userRepository2117

1. java 面试指南 (付费) 收录的京东面经同学 9 面试原题: 依赖注入的时候，直接Autowired比较直接，
为什么推荐构造方法注入呢

memo: 2025年7月1 日修改至此，今天在帮球友修改简历的时候，碰到一个郑州大学本硕的球友，这也是我们
河南省最好的大学了，但也仅仅是一所 211，所以希望所有河南的同学都能加把劲，证明自己的实力，去拿到更好
的 offer，为校争光。

硕士 : 郑州大学(211)                计算机技术

GPA: 4.04/4.3                            GPA排名: 前10%

所获荣誉 : 中国研究生人工智能创新大赛全国三等奖、郑州大学研究生-
本科 : 郑州大学(211)                计算机科学与技术

GPA: 3.51/4.0                          GPA排名: 前15%

所获荣誉 : 郑州大学三好学生包下着、郑州大学优秀学生奖学金古林-

No. 681180





## 第 69 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

13.@Autowired的实现原理了解吗?

eautowired 是 Spring 实现依赖注入的核心注解，其实现原理基于反射机制和 BeanPostProcessor 接口。

整个过程分为两个主要阶段。第一个阶段是依赖收集阶段，发生在 Bean 实例化之后、属性赋值之前。 Autowired
的 Processor 会扫描 Bean 的所有字段、方法和构造方法，找出标注了 eautowired 注解的地方，然后把这些信
息封装成 Injection 元数据对象缓存起来。这个过程用到了大量的反射操作，需要分析类的结构、
等。

Ce                        LE
[二
人
EE二- ==一
EEE
世 <                            二

固
第二个阶段是依赖注入阶段，Spring 会取出之前缓存的 Injection 元数据对象，然后逐个处理每个注入点。对于
每个 eautowired 标注的字段或方法，Spring 会根据类型去容器中查找匹配的 Bean。

// 1. 按类型查找 (byType)

Map<String，Object> matchingBeans = BeanFactoryUtils.beansOfTYyYpeIncludingRncestors1
this.beanFactory，type) 1

// 2. 如果找到多个候选者，按名称筛选(byName)

String autowiredBeanName = determinehutowireCandidate(matchingBeans，descriptor) 1

// 3. 考虑aprimary和epPriority注解
// 4。 最后按照字段名或参数名匹配

在具体的注入过程中，Spring 会使用反射来设置字段的值或者调用 setter 方法。比如对于字段注入，会调用
Field.set() 方法; 对于 setter 注入，会调用 Method.invoke() 方法。

14.什么是自动装配?

自动装配的本质就是让 Spring 容器自动帮有我们完成 Bean 之间的依赖关系注入，而不需要我们手动去指定每个依
赖。简单来说，就是“我们不用告诉 Spring 具体怎么注入，Spring 自己会想办法找到合适的 Bean 注入进来"。

自动装配的工作原理简单来说就是，Spring 容器在启动时自动扫描 ecomponentscan 指定包路径下的所有类，然
后根据类上的注解，比如 eautowired 、eResource 等，来判断哪些 Bean 需要被自动装配。

No. 691180




## 第 70 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

econfiguration

ecomponentScan("com.github.paicoding.forum.service")

eMapperScan(basePackages = {
"com.github.paicoding.forum.service.article.repository.mapper"，
"com.github.paicoding.forum.service.user.repository.mapper'"

// ..。 更多包路径
))

public class ServiceRutoConfig {
// Spring自动扫描指定包下的所有组件并注册为Bean
】}

之后分析每个 Bean 的依赖关系，在创建 Bean 的时候，根据装配规则自动找到合适的依赖 Bean，最后根据反射
将这些依赖注入到目标 Bean 中。

Spring提供了哪几种自动装配类型?

Spring 的自动装配方式有好几种，在 XML 配置时代，主要有 byName、byType、constructor 和 autodetect 四
种方式。

byIType

ConsttfuUctot

到了注解驱动时代，用得最多的是 eautowired 注解，默认按照类型装配。

eservice
public class UserService {

eautowired  // 按类型自动装配

private UserRepository userRepository)

其次还有 eResource 注解，它默认按照名称装配，如果找不到对应名称的 Bean，就会按类型装配。

No. 701180




## 第 71 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

Spring Boot 的自动装配还有一套更高级的机制，通过 egnableautoconfiguration 和各种econditional 注解
来实现，这个是框架级别的自动装配，会根据 classpath 中的类和配置来自动配置 Bean。

|         @SpringBootApplication
@ComponentScan                                   @EnableAutoConfiguration                               @SpringBootConfiguration
扫描类在的package                                                                                                                                标注当前类是配置类

@Import(AutoConfigurationImportSelector.class)

站

AutoConfigurationImportSelector#selectlImports()

时
spring.factories 四几天，           SpringFactoriesLoader#loadFactoryNames
个                     根据factories文件加载配置类到容器

memo: 2025年7月2 日修改至此，今天在帮球友修改简历的时候，碰到一个北京航空航天大学的球友，他在邮
件中说到: 在星球里学到了好多东西，目前正在准备技术派和 MYDB，打算好好冲秋招，能帮助到大家我真的很欣

奈。

时 间: 2025年06月20日 15:26 (星期五)
附 件: 1个(贺 于-4 志 北京航空航天大学.pdf ) 查看附件

【升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

二哥好哇! 首先感谢你呐，在星球真的学到了好多东西。 En
目前的计划是好好学习技术派和MYDB，好好冲秋招，不管是中小
15.Bean的作用域有哪些?

Bean 的作用域决定了 Bean 实例的生命周期和创建策略，singleton 是默认的作用域。整个 Spring 容器中只会
一个 Bean 实例。不管在多少个地方注入这个 Bean，拿到的都是同一个对象。

No. 711180




## 第 72 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

ecomponent “// 默认就是singleton
public class UserService {
// 整个应用中只有一个Userservice实例

)}

命周期和 Spring 容器相同，容器启动时创建，容器销毁时销毁。
实际开发中，像 Service、Dao 这些业务组件基本都是单例的，因为单例既能节省内存，又能提高性能。
当把 scope 设置为 prototype 时，每次从容器中获取 Bean 的时候都会创建一个新的实例。

ecomponent

escope("prototype")

Public class OrderProcessor {
// 每次注入或获取都是新的实例

}

当需要处理一些有状态的 Bean 时会用到 prototype，比如每个订单处理器需要维护不同的状态信息。

需要注意的是，在 singleton Bean 中注入 prototype Bean 时要小心，因为 singleton Bean 只创建一次，所以
prototype Bean 也只会注入一次。这时候可以用 erookup 注解或者 ApplicationContext 来动态获取。

ecomponent
public class SingletonService 1{
// 错误的做法，prototypeBean只会注入一次
Rutowired
Private PrototypeBean prototypeBeanyi

// 正确的做法，每次调用都获取新实例

eLookup

Public PrototypeBean getPrototypeBean() {
return nul1;  // Spring会重写这个方法

}

除了 singleton 和 prototype，Spring 还支持其他作用域，比如 request、session、application 和 websocket。

No. 721180




## 第 73 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

singleton

prototype

Spring Bean作用域 |

request

Session

global-session

如果作用于是 request，表示在 Web 应用中，每个 HTTP 请求都会创建一个新的 Bean 实例，请求结束后 Bean 就

ecomponent
escope( "request'")
public class RequestContext {

// 每个HTTP请求都有自己的实例
》

如果作用于是 session，表示在 Web 应用中，每个 HTTP 会话都会创建一个新的 Bean 实例，会话结束后 Bean 被
销毁。

ecomponent

escope("session")

public class UserSession {
// 每个用户会话都有自己的实例

】}

典型的使用场景是购物车、用户登录状态这些需要在整个会话期间保持的信息。

application 作用域表示在整个应用中只有一个 Bean 实例，类似于 singleton，但它的生命周期与 ServletContext
绑定。

No. 731180




## 第 74 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ecomponent
escope("application")
Public class Appconfig {

// 整个应用中只有一个实例
}

websocket 作用域表示在 WebSocket 会话中每个连接都有自己的 Bean 实例。WebSocket 连接建立时创建，连接
关闭时销毁。

ecomponent
escope("websocket")
public class WebSocketHandler {

// 每个WebSsocket连接都有自己的实例
)}

1. Java 面试指南(付费) 收录的同学 1 贝壳找房后端技术一面面试原题: bean是单例还是多例的，具体
怎么修改

memo: 2025 年7 月 3 日修改至此，今天在帮球友修改简历的时候，础到一个郑州大学硕，河北师范大学本的球
友，整体在校的经历非党出色，奖学金、论文期刊基本上都拉满了。那这么多优秀的球友选择来到这里，也是对旺
球的又一次认可和肯定，我也一定会继续努力，提供更多优质的内容和服务。
郑州大学 (推免) - 网络与信息安全
参与国家级项目1项 ; 发表论文2篇 ; 发明型专利1项 ; 参与撰写网络弹性相关书籍一册。
河北师范大学 - 信息安全
成绩优异，排名前59% ; 获得1次国家级奖学金，2次专业奖学金 ; 多次被评为院级三好学生。

16.Spring中的单例Bean会存在线程安全问题吗?

首先要明确一点。Spring 容器本身保证了 Bean 创建过程的线程安全，也就是说不会出现多个线程同时创建同一个
单例 Bean 的情况。但是 Bean 创建完成后的使用过程，Spring 就不管了。

换句话说，单例 Bean 在被创建后，如果它的内部状态是可变的，那么在多线程环境下就可能会出现线程安全问
题。

No. 741180




## 第 75 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

二二

Fighter3Controller

比如说在技术派项目中，有一个敏感词过滤的 Bean，我们就需要使用 volatile 关键字来保证多线程环境下的可见
性。

aeService
public class Sensitiveservice 1{
Private Volatile SensitiveWordBs sensitiveWordBs; // 使用volatile保证可见性

8PostConstruct
public void refresh() {
// 重新初始化sensitivewWordBs

者成员变量都是不可变的，final 修饰的，那么就不存在线程安全问题。

加

如果 Bean 中没有成员变量，

eservice
public class UserServiceImp1 implements UserService {

eResource
Private UserDao userDao)
Rutowired

Private CountService countServicey

// 只有依赖注入的无状态字段

eservice
public class ConfigSservice {
private final String appName;  // final修饰，不可变

Public ConfigService(evValue("${fapp.name}") String apPpName) {

No. 751180




## 第 76 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

this.appName = appNamey

单例Bean的线程安全问题怎么解决呢?
第一种，使用局部变量，也就是使用无状态的单例 Bean，把所有状态都通过方法参数传递:

eservice
public class UserService {
8Rutowired

Private UserDao userDao)

// 无状态方法，所有数据通过参数传递
public User processUser(Long userId，String operation) {
User user = userDao.findById(userId);

// 处理逻辑.. .

return useri

第二种，当确实需要维护线程相关的状态时，可以使用 ThreadLocal 来保存状态。ThreadLocal 可以保证每个线程
都有自己的变量副本，互不干扰。

eservice
public class UserContextService {

Private static final ThreadLocal<User> userThreadLocal = new ThreadLocal<>() 1;

public void setCurrentUser(User user) {
userThreadLocal.set(user);

public User getCurrentUser() {
return userThreadLocal.get() 7

public void clear() {
userThreadLocal.remove(); // 防止内存泄漏

第三种，如果需要缓存数据或者计数，使用JUC 包下的线程安全类，比如说 Atomiclnteger、
ConcurrentHashMap、CopyOnwWriteArrayList 等。

No. 761180




## 第 77 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆:
Service

public class Cacheservice {

// 使用线程安全的集合

Private final ConcurrentHashMap<String，Object> cache
Private final RtomicLong counter

new RtomicLong(0) 7

new ConcurrentHashMap<>() 1
public void put(String key，object value) {

cache.put(key，value) 7

counter .incrementRndGet())
}

第四种，对于复杂的状态操作，可以使用 synchronized 或 Lock:

eservice
public class Cacheservice {

Private final Map<String，Object> cache

Private final ReentrantLock Lock

new HashMap<>()7

new ReentrantLock() 17
public void put(String key，object value) {
lock.lock();

try {

cache.put(key，value)
} finally {

lock.unlock();

第五种，如果 Bean 确实需要维护状态，可以考虑将其改为 prototype 作用域，
例，避免了多线程共享同一个实例的问题。
aservice

这样每次注入都会创建一个新的实
escope("prototype") // 每次注入都创建新实例
public class StatefulService 1{

private String state; // 现在每个实例都有独立状态

this .state

public void setState(String state) {

state1

或者使用 request 作用域，这样每个 HTTP 请求都会创建一个新的实例。

No. 771180




## 第 78 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eservice

escope( "request'")

public class RequestScopedService {
Private String requestDatai

// 每个请求都有独立的实例

1. java 面试指南 (付费) 收录的阿里面经同学 1 闲鱼后端一面的原题: spring的bean的并发安全问题

memo: 2025年7月4日修改至此，今天在帮球友修改简历的时候，磋到一个武汉理工大学本硕的球友。说真
的，和武汉理工大学挺有缘的，2023 年去武汉，就线下见了一名武理的球友，他当时签约的是小米，非常优秀。

2023.09-2026.06 ”武汉理工大学 E
信息与通信工程     硕士“”GPA: 4.09/5.00 人(专

2019.09-2023.06 ”武汉理工大学 Ea
通信工程         本科   GPA: 3.98/5.00 人(专

17.什么是循环依赖?
简单来说就是两个或多个 Bean 相互依赖，比如说 A 依赖 B，B 依赖A，或者 C 依赖 5，就成了循环依赖。

No. 781180




## 第 79 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

@Component                                  @Component

public class A                                 public class B
@Autowired                                   @Autowired
private B b;                                  privafe A a:

人A

@Component
public class C

@Autowired
private C c:

C

18.二Spring怎么解决循环依赖呢?

Spring 通过三级缓存机制来解决循环依赖:
1一级缓存: 存放完全初始化好的单例 Bean。
2二级缓存: 存放提前暴露的 Bean，实例化完成，但未初始化完成。
3三级缓存: 存放 Bean 工厂，用于生成提前暴露的 Bean 。

No. 791180




## 第 80 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

一级缓存           Map<String'Object> singletonObjcces        一> 实例化、注入、初始化完成的bean实例

以A、B 两个类发生循环依赖为例:

第1 步: 开始创建 Bean A。

。 Spring 调用A 的构造方法，创建 A 的实例。此时 A 对象已存在，但 b属性还是 null。
。 将A的对象工三放入三级缓存。
。 开始进行A的属性注入。

一级缓存
Map<StingObject> singletonObjects

No. 801180




## 第 81 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

第 2 步: A 需要注入B，开始创建 Bean B。
。 发现需要 B，但 B 还不存在，所以开始创建 B。
。 调用 B 的构造方法，创建 B 的实例。此时 B 对象已存在，但 a 属性还是 null。
。 将B 的对象工厂放入三级缓存。
。 开始进行 B 的属性注入。
第3 步: B 需要注入A，从缓存中获取A。
* B 需要注入 A，先从一级缓存找 A，没找到。
。 再从二级缓存找 A，也没找到。
。 最后从三级缓存找 A，找到了 A 的对象工厂。
。 调用A 的对象工厂得到 A 的实例。这时 A 已经实例化了，虽然还没完全初始化。
。 将A从三级缓存移到二级缓存。
。 B 拿到A的引用，完成属性注入。

一级缓存
Map<StingObject> singletonObjects

A实例化完成
未初始化

第4步: B 完成初始化。
。 B 的属性注入完成，执行 epostconstruct 等初始化远辑。
。 B 完全创建完成，从三级缓存移除，放入一级缓存。

第5 步: A完成初始化。
。 回到和A 的创建过程，A 拿到完整的 B 实例，完成属性注入。
。 A执行初始化逻辑，创建完成。
。 A 从二级缓存移除，放入一级缓存。

No. 811180




## 第 82 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

了B实例化、初
始化完成

一级缓存                       A实例化、谦
Map<Sting'Object> singletonObjects

用代码来模拟这个过程，是这样的:

// 模拟Spring的解决过程

Public class CircularDependencyDemo {
// 三级缓存
Map<String，Object> singletonObjects = new HashMap<>()7
Map<String，Object> earlySingletonObjects = new HashMap<>() 7
Map<String，ObjectFactory> singletonFactories = new HashMap<>()7

public object getBean(String beanName) {

// 先从一级缓存获取
Object bean = singletonObjects.get(beanName);
if (bean != nul1) return beany

// 再从二级缓存获取
bean = earlySingletonObjects.get(beanName);
if (bean != nul1) return beanj

// 最后从三级缓存获取

ObjectFactory factory = singletonFactories.get(beanName) 1;

if (factory != null) {
bean -= factory.getObject();
ear1ySingletonObjects.put(beanName，bean);  // 移到二级缓存
singletonFactories.remove(beanName) 1;                // 从三级缓存移除

return beani7

No. 821180




## 第 83 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

哪些情况下Spring无法解决循环依赖?
Spring 虽然能解决大部分循环依赖问题，但确实有几种情况是无法处理的，我来详细说说。

循环依赖

   E

依赖

A中注入的B为setter注入，B中注入的A为构造器注入

           ER   Et

第一种，构造方法的循环依赖，这种情况 Spring 会直接抛出 BeanCurrentlylInCreationException 异常。

ecomponent
public class R {
private B b)

Public RA(B b) { // 构造方法注入
this.b = b;
}
】}

ecomponent
public class B {

Private R ay

Public B(R a) { // 构造方法注入
this.a = af
}
】}

因为构造方法注入发生在实例化阶段，创建 A 的时候必须先有 B，但创建 B又必须先有 A，这时候两个对象都还没
创建出来，无法提前暴露到缓存中。

第二种，prototype 作用域的循环依赖。prototype 作用域的 Bean 每次获取都会创建新实例，Spring 无法缓存这
些实例，所以也无法解决循环依赖。

No. 831180




## 第 84 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

一-面试中可以不背，方便大家理解 start-…--

我们来看一个实例，先是 PrototypeBeanA:

ecomponent
escope("prototype")
public class PrototypeBeanR {
private final PrototypeBeanB prototypeBeanB1i

Rutowired
Public PrototypeBeanR(PrototypeBeanB prototypeBeanB) {
this.prototypeBeanB = prototypeBeanB)

然后是 PrototypeBeanB:

ecomponent
escope("prototype")
Public class PrototypeBeanB {
private final PrototypeBeanR prototypeBeanRi

Rutowired
Public PrototypeBeanB(PrototypeBeanR prototypeBeanR) {
this.prototypeBeanR = PrototypeBeanRy

再然后是测试:

SpringBootRApplication
public class DemoRpplication {

public static void main(String[] args) {

Springapplication.run(Demohpplication.class，args)7

Bean

CommandLineRunner commandLineRunner(RpplicationContext ctx) {
return args -> {

// 尝试获取PrototypeBeana的实例
PrototypeBeanR beanR =- ctx.getBean(PrototypeBeanR.class);

No. 841180




## 第 85 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

机认放宙宙宙宙
APPLICATION FAILED TO START

Description:

The dependencies of some of the beans in the appLication context form a cycte:

prototypeBeanA defined in fite [/Users/maweiqing/Documents/GitHub/paicoding/paicoding-web/target/test-ctasses/com/github

|

T vY
| prototypeBeanB defined in fite [/Users/maweiqing/Documents/GitHub/paicoding/paicoding-web/target/test-ctasses/com/github，
L 一

Action:

Despite circutar references being attowed，the dependency cycte between beans coutd not be broken. Update your apptication

一-面试中可以不背，方便大家理解 end

1. Java 面试指南 (付费) 收录的小米 25 届日常实习一面原题: 如何解决循环依赖?

2. java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: Spring如何解决循
环依赖?

3. java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: Spring源码看过吗? Spring的三级缓存知
道吗?

4. Java 面试指南 (付费)_收录的阿里云面经同学 22 面经: spring三级缓存解决循环依赖问题

memo: 2025年7月5日修改至此。今天VIP 群来了非常多的球友，不知不觉我们已经 12 群了，也是一个大家
了，希望大家都能在这里找到自己的归属感，我们一起学习，一起进步。

No. 851180




## 第 86 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

二哥VIP12 群 (119)

鲍- 沉默王二: 重要通知: 面渣逆袭 Red.，”移除

昨大 16.15
你邀请' 中 sme玫"加入了群聊 撤销
qi 一“一司群里其他人都不是朋友关系，请注意隐私安全
昨天 16:29
你邀语" .0入了群聊 撤销
ia :与群里其他人都不是朋友关系，请注意隐私安全

你邀请“8     加入了群聊 撤销

与群里其他人都不是朋友关系，请注意隐私安全

昨天 16:39
你邀请"1一“加入了和群聊 撤销

“ea "与群里其他人都不是朋友关系，请注意隐私安全

昨天 19:47

你邀请' 辐。 "加入了群聊 撤销

Rs 与群里其他人都不是朋友关系，请注意隐私安全

19.为什么需要三级缓存而不是两级?
Spring 设计三级缓存主要是为了解决 AOP 代理的问题。

我举个具体的例子来说明一下。假设我们有 A 和 B 两个类相互依赖，A 的某个方法上面还标注了
erransactional 注解，这意味着 A 最终需要被 Spring 创建成一个代理对象。

No. 861180




## 第 87 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ecomponent

public class R {
Rutowired
Private B bi

eTransactional “ // R需要被AoP代理
public void doSomething() {
// 业务罗辑

ecomponent

public class B {
Rutowired
Private R ai

如果只有二级缓存的话，当创建 A 的时候，我们需要把 A 的原始对象提前放到缓存里面，然后 B 在创建的时候从
缓存中拿到A 的原始对象。

// 假设只有两级缓存
Map<String，Object> singletonObjects = new HashMap<>() 1;     // 完整Bean
Map<String，Object> earlySingletonObjects = new HashMap<>(); // 半成品Bean

但是问题来了，A 完成初始化后，由于有 erransactional 注解，Spring 会把 A 包装成一个代理对象放到容器
中。这样就出现了一个很严重的问题: B 里面持有的是 A 的原始对象，而容器中存的是 A 的代理对象，同一个
Bean 居然有两个不同的实例，这肯定是不对的。

co

三级缓存就是为了解决这个问题而设计的。三级缓存里面存放的不是 Bean 的实例，而是一个对象工厂，这是一个
函数式接口。

当B 需要A 的时候，会调用这个对象工厂的 getObject 方法，这个方法里面会判断 A 是否需要被代理。如果需要
代理，就创建 A 的代理对象返回给 B; 如果不需要代理，就返回 A 的原始对象。这样就保证了 B 拿到的 A 和最终
放入容器的A是同一个对象。

Map<String，ObjectFactory<?>> singletonFactories = new HashMap<>())
// Spring源码中的逻辑
addsingletonFactory(beanName，() -> getEarlyBeanReference(beanName，mbd，bean) ) 7
Protected Object getEarlyBeanReference(String beanName，RootBeanDefinition mbd，Object
bean) {

Object exposedobject = bean;

if (!mbd.isSynthetic() sg& hasInstantiationRhwareBeanPostProcessors()) {

for (BeanPostProcessor bp : getBeanPostProcessors()) {

if (bp instanceof SmartInstantiationRwareBeanPostProcessor) {

No. 871180




## 第 88 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

SmartInstantiationRwareBeanPostProcessor ibp =
(SmartInstantiationRwareBeanPostProcessor) bp;
// 关键: 如果需要代理，这里会创建代理对象

exposedObject = ibp.getEarlyBeanReference(exposedObject，beanName);

}
}

return exposedObject)

简单来说，三级缓存的核心作用就是延迟决策。它让 Spring 在真正需要 Bean 的时候才决定返回原始对象还是代
理对象，这样就避免了对象不一致的问题。如果没有三级缓存，Spring 要么无法在循环依赖的情况下支持 AOP，
要么就会出现同一个 Bean 有多个实例的问题，这些都是不可接受的。

No. 88 1180




## 第 89 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Spring中的循环依赖和三级缓存

循环依赖类型

_A依赖B~、

-A依赖B、、    2
6 D69 6:
Te              <依赖A @@生              Se
直接依赖                           自我依赖

间接依赖

Spring的三级缓存

Spring解决循环依赖的核心机制是通过使用三级缓存。

* 一级缓存 (singletonObjects) : 存储完全初始化好的Bean。

* 二级缓存 (earlySingletonObjects) : 存储原始实例，即还未完全初始化的Bean。

级缓存 (singletonFactories) : 存储ObjectFactory，用于生成Bean的代理对象或原始对象 。

依赖注入       ---划依赖注入 | 。,----站 BeanA注入
BeanB                               BeanA                              BeanB实例

初始化

---世|
BeanA

从一级缓存中找到
BeanB实例        |

|                                   过        BeanA完成属性填充

                 三   中移除      完     |

卫                 全全生生     执行完初始化并放入|
创建实例       创建实例                          |
(未初始化)      (未初始化)

Say中心cheasen

把不完整的BeanA
注入到BeanB中

记
着----
硅

四 放入第三级缓存 国二国 放入第三级组存 四2

BeanB完成属性填充
执行    始化并放入

如果缺少二级缓存会有什么问题?
二级缓存 earlySingletonObjects 主要是用来存放那些已经通过三级缓存的对象工厂创建出来的早期 Bean 引用。

No. 891180




## 第 90 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

Spring三级缓存

YY
N
纪和有                             Y
ie 上put                                     <一到三级月
式
执lamada
谁训注NB                                                                        Er
-<                       到险A的三级缉
YY

假设我位有A、B、C 三个Bean，A 依赖B和C，B 和 C 都依赖A，形成了一个复杂的循环依赖。在没有二级缓存
的情况下，每次B 或者 C 需要获取 A 的时候，都需要调用三级缓存中A 的 objectFactory.getobject() 方法。
这意味着如果 A 需要被代理的话，代理对象可能会被重复创建多次，这显然是不合理的。

// 没有二级缓存的伪代码
public Object getSingleton(String beanName) {
Object singletonObject = singletonObjects.get(beanName) 1;

if (singletonObject == null gg isSingletonCurrent1yInCreation(beanName)) {
// 直接从三级缓存获取
ObjectFactory<?> singletonFactory =- singletonFactories.get(beanName))
if (singletonFactory != nul1) {
return singletonFactory.getObject(); // 每次都会创建新的代理对象!
}
}

return singletonObject;

我举个具体的例子。比如A 有 ezransactional 注解需要被 AOP 代理，B 在初始化的时候需要 A，会调用一次对
象工厂创建 A 的代理对象。接着 C 在初始化的时候也需要 A，又会调用一次对象工厂，可能又创建了一个A的代
理对象。这样 B 和 拿到的可能就是两个不同的 A 代理对象，这就违反了单例 Bean 的语义。

No. 901180




## 第 91 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

eservice

Public class ServiceR {
Rutowired
Private ServiceB serviceB;

eTransactional  // 需要 AMoP 代理
public void methodR() {
// 业务罗辑
}
}

aeService
public class ServiceB {
Rutowired
private ServiceR serviceR;  // 获得代理对象 Al

Rutowired
Private ServiceC servicecy

)}

eservice
public class Servicec 1{
8Rutowired
private ServiceR serviceR;  // 可能获得代理对象 A2

二级缓存就是为了解决这个问题。当第一次通过对象工厂创建了 A 的早期引用之后，就把这个引用放到二级缓存
中，同时从三级缓存中移除对象工厂。

// 第一次获取

ObjectFactory<R> factory = singletonFactories .get("serviceR'") 1;
Object proxyR = factory.getObject(); // 创建代理
ear1lySingletonobjects.put("serviceRA"，PproxyR); // 缓存代理
singletonFactories .remove("serviceR'" ) 1;

// 第二次获取
Object cachedR = earlySingletonObjects.get("servicea'"); // 直接返回缓存的代理
// ProxyR == cachedR v

后续如果再有其他 Bean 需要 A，就直接从二级缓存中获取，不需要再调用对象工矿了。

1. java 面试指南(付费) 收录的快手同学 4 一面原题: 循环依赖有了解过吗? 出现循环依赖的原因? 三大
缓存存储内容的区别? 如何解决循环依赖? 如果缺少第二级缓存会有什么问题?

memo: 2025年7月6 日修改至此，今天在星球里看到一个球友的秋招打卡，已经持续 30 天了，按照他这个节
奏下去，互联网大厂的 offer 基本上就算是锁定了。并且还有准备 RAG MCP 的八股，很棒。

No. 911180




## 第 92 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

生 加二. 目

秋招沉淀day30

1. hot100 * 10

2. 大厂笔试题 * 10

3. 大模型rag八股，mcp八股，redis中的分布式锁
4. 科研论文搜索

AOP

20.二说说什么是AOP?

AOP，也就是面向切面编程，简单点说，AOP 就是把一些业务逻辑中的相同代码抽取到一个独立的模块中，让业
务轴辑更加清爽。

一-这部分面试中可以不背，方便大家理解 start一-

举个简单的例子，假设我们有很多个 Service 方法，每个方法都需要记录执行日志、检查权限、管理事务等等。如
果没有 AOP 的话，我们可能需要在每个方法里都写这样的代码:

No. 921180




## 第 93 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

public void createUser(User user) {
log.info( "开始执行createUser方法");

// 权限检查

if (!hasPermission()) {
throw new SecurityException("无权限") 7

}

// 开启事务

transactionManager.begin();

try 1{

// 真正的业务罗辑
userDao.save(user) 1
transactionManager .commit() 7
1og.info("createUser方法执行成功" ) ;

} catch (Exception e) {
transactionManager.rollback())
log.error("createUser方法执行失败"，e) ;
throw ey

如果每个方法都这样写，代码就会变得非常脐肿，AOP 就是为了解决这个问题，它可以让我们把这些横切关注点
(如日志、权限、事务等) 从业务代码中抽取出来。

这样，我们就可以定义一个切面，在切面中统一处理这些横切关注点:

aspect
ecomponent
public class Loggingaspect {
8Before("execution(* com.example.service.*.x(..))")
public void logBefore(JoinPoint joinPoint) {
1og.info( "开始执行方法: ”+ joinPoint.getSignature() .getName())17
}
8RfterReturning("execution(* com.example.service.*.x(..))")
public void logafterReturning(JoinPoint joinPoint) {
1og.info( "方法执行成功: " + joinPoint .getSignature() .getName())7
}
8RfterThrowing(pointcut

"execution(* com.example.service*.x(..))"，

throwing = "ex'")
public void logRfterThrowing(JoinPoint joinPoint，Throwable ex) {
log.error( "方法执行失败: ”+ joinPoint.getSignature() .getName()，ex) 7

然后，业务代码就变得非常干净了:

Public void createUser(User user) {
// 只需要关注业务逻辑，不需要关心日志、权限、事务等

userDao.save(user);

No. 931180




## 第 94 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

---面试中可以不背，方便大家理解 end----

从技术实现上来说，AOP 主要是通过动态代理来实现的。如果目标类实现了接口，就用JDK 动态代理; 如果没有
实现接口，就用 CGLIB 来创建子类代理。代理对象会在方法执行前后插入我们定义的切面逻辑。

JDK vs CGLib Proxies

。 ]DK Proxy

- Interface based

implements           implements

Spring Proxy            |                  沁
贺

SS

Spring AOP 有哪些核心概念?

。 CGLib Proxy

- subclass based

Target
一一
qi

Spring AOP 是 AOP 的一个具体实现，我按照在工作/学习中理解的重要程度来说一下:

No. 94 1180




## 第 95 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

Spring AOP Terminologies

Aspect              全

Advice

Pointcut             全

Weaving

、切面: 我们定义的一个类，包含了要在什么时候、什么地方执行什么逻辑。比如我们定义一个日志切面，专门
责记录方法的执行情况。在 Spring 中，我们会用 easpect 注解来标识一个切面类。

@、切点: 定义了在哪些地方应用切面逻辑。说白了就是告诉 Spring，我这个切面要在哪些方法上生效。比如我
们可以定义一个切点表达式，让它匹配所有 Service 层的方法，或者匹配某个特定包下的所有方法。在 Spring 中
用 epointcut 注解来定义，通常会写一些表达式，比如 execution( com.example.service..x*(..)) 这样
的。

@
负

图、通知: 是切面中具体要执行的代码逻辑。它有几种类型: eBefore 是在方法执行前执行，eafter 是在方法
执行后执行， earounad 是环绕通知，可以在方法执行前后都执行， eafterReturning 是在方法正常返回后执
行，eafterThrowing 是在方法抛出异常后执行。我一般用得最多的是 earound ，因为它最灵活，可以控制方法

是否执行，也可以修改参数和返回值。

@、连接点: 被拦截到的点，因为 Spring 只支持方法类型的连接点，所以在 Spring 中，连接点指的是被拦截到的
方法，实际上连接点还可以是字段或者构造方法。

No. 951180




## 第 96 页


面渣逆袭Spring篇V2-让天下所有的面洒都能着装
@@、织入: 是把切面逻辑应用到目标对象的过程。Spring AOP 是在运行时通过动态代理来实现织入的，当我们从
Spring 容器中获取 Bean 的时候，如果这个 Bean 需要被切面处理，Spring 就会返回一个代理对象给我们。

人@@、目标对象: 被切面处理的对象，也就是我们平时写的 Service、Controller 等类。Spring AOP 会在目标对象上
织入切面逻辑。

它们之间的逻辑关系图是这样的:

切面 (Aspect)
上 切入点 (Pointcut) 一 定义在哪里执行
[一 通知 (Advice) 一- 定义何时执行什么
|一 epefore
上一 eRfter
|一 eafterReturning
|一 eafterThrowing
[一 earound

目标对象 (Target) 一 代理对象 (Proxy) 一 织入 (weaving)
了个                               了

连接点 (Join Point)                                  客户端调用

Spring AOP 织入有哪几种方式?
织入有三种主要方式，我按照它们的执行时机来说一下。

No. 961180




## 第 97 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

AOP - Weaving

。 Compile time
。 Class Load Time
。 Runtime - Springs way

Wwww.java9s.com

编译期织入是在编译java 源码的时候就把切面罗辑织入到目标类中。这种方式最典型的实现就是 Aspect| 编译
器。它会在编译的时候直接修改字节码，把切面的逻辑插入到目标方法中。

// 源代码
Raspect
Public class Loggingaspect 1{
Before("execution(* com.example.service.*.x*(..))")
public void logBefore(JoinPoint joinPoint) {
System.out .println("方法执行前: ”+ joinPoint .getSignature() .getName()) 7
}
》

8Service
public class UserService {
public void saveUser(String username) {
System.out .Println("保存用户: ”+ username) 7
}
》

这样生成的 class 文件就已经包含了切面逻辑，运行时不需要额外的代理机制。

No. 971180




## 第 98 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 编译器自动生成的代码
public class UserService {
public void saveUser(String username) {
// 织入的切面代码
System.out .println( "方法执行前: saveUser'") 7

// 原始业务代码
System.out .println( "保存用户: ”+ username ) 7

编译期织入的优点是性能最好，因为没有代理的开销，但缺点是需要使用特殊的编译器，而且比较复杂，在
Spring 项目中用得不多。

类加载期织入是在JVM 加载 class 文件的时候进行织入。这种方式通过java 的 Instrumentation API 或者自定义
的 ClassLoader 来实现，在类被加载到JVM 之前修改字节码。

public class WeavingClassLoader extends ClassLoader {
eoverride
Protected Class<?> findClass(String name) throws ClassNotFoundException {
byte[] classBytes = loadClassBytes(name))

// 在这里进行字节码织入

byte[] wovenBytes = weaveRspects(classBytes);

return defineclass(name，wovenBytes，0，wovenBytes.length);

Private byte[] weaveRspects(byte[] classBytes) {
// 使用 ASM 或其他字节码操作库进行织入

return classBytes)

Aspectj 的 Load-Time Weaving 就是这种方式的典型实现。它比编译期织入更灵活一些，但是配置相对复杂，需
要在JVM 启动参数中指定Java agent，在 Spring 中也有支持，但用得不是特别多。

# JVM 启动参数

java -javaagent:aspectjweaver.jar -jar myapp.jar

运行时织入是我们在 Spring 中最常见的方式，也就是通过动态代理来实现。Spring AOP 采用的就是这种方式。当
Spring 容器启动的时候，如果发现某个 Bean 需要被切面处理，就会为这个 Bean 创建一个代理对象。如果目标类
实现了接口，Spring 会使用JDK 的动态代理技术。

// 接口
Public interface UserService {
void saveUser(String username) 7

No. 981180




## 第 99 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 实现类
eservice
public class UserServiceImp1 implements UserService {

eoverride
Public void saveUser(String username) {
System.out .println( "保存用户: ”+ username ) 7

// Spring 自动创建的代理 (伪代码)

public class UserServiceProxy implements UserService {
Private UserService target1
Private List<Rdvisor> advisors1

eoverride
public void saveUser(String username) {
// 执行前置通知
for (Rdvisor advisor : advisors) {
if (advisor.getPointcut() .matches(this.getClass() .getMethod("saveUser'"/

String.class))) {
advisor.getahdvice().before();

// 执行目标方法

target .saveUser(username) ;

// 执行后置通知
for (Rdvisor advisor : advisors) {
advisor.getadvice().after() 7

如果目标类没有实现接口，就会使用 CGLIB 来创建一个子类作为代理。运行时织入的优点是实现简单，不需要下
殊的编译器或JVM 配置，缺点是有一定的性能开销，因为每次方法调用都要经过代理。

// 没有接口的类
eService
public class OrderService {
public void createOrder(String orderId) {
System.out .println( "创建订单: ”+ orderId)

// cGLIB 生成的代理子类 (伪代码)
public class OrderServiceS$S$EnhancerByCGLIBS$S$12345 extends OrderService {
private MethodInterceptor interceptori

aoverride
public void createorder(String orderId) {

No. 991180




## 第 100 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 通过 MethodInterceptor 执行切面逻辑
interceptor.intercept(this，getMethod("createOrder")，new Object[]{orderId}，
new MethodProxy() {
eoverride
public Object invokeSuper(Object obj，object[] args) {
return OrderService.super.createOrder((String)

args[0])7

])

Spring AOP 默认的织入方式就是运行时织入，使用起来非常简单，只需要加个 easpect 注解和相应的通知注解
就可以了。虽和然性能上不如编译期织入，但是对于大部分业务场景来说，这点性能开销是完全可以接受的。

// Spring RAOP 的代理创建过程

econfiguration

eEnableRspectJRutoProxy  // 启用 AoP 自动代理
public class RopCconfig {

)}

// Spring 内部的代理创建逮辑 (简化版)

Public class DefaulthopProxyFactory implements RopProxyFactory {

eoverride
public RopProxy createhopProxy(RdvisedSupport config) {
if (config.isOptimize() || config.isProxyTargetClass() ||
hasNoUserSuppliedProxyInterfaces(config)) {

// 使用 cGLIB 代理

return new CglibRopProxy(config);
)} else {
// 使用 JDK 动态代理

return new JdkDynamicRopProxy(config) 7

Aspectj 是什么?

Aspectj 是一个 AOP 框架，它可以做很多 Spring AOP 干不了的事情，比如说编译时、编译后和类加载时织入切
面。并且提供了很多复杂的切点表达式和通知类型。

No. 1001180




## 第 101 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

(ECLIPSE             Psds supponers colabonsions Resource TheFaundaion

FOUNDATION

aspedjg                                   aspectj enables
aseamless aspectoriented extensiontothe 。 。clean modularization of crosscutting
Javam programming anguage             concems such as error checking and
Java platform compatble                    handng Synchronization contextsensttive
easytoleam and use                            behavior performance optimizations，

monitoring and logging debugging support
and multrobject protocols

Quick Links

。For Eclipse development AJDT: The Aspecty Development Tools
。Blog: Aspecty Programming Blog

。Popular Aspecty downloads: Latest development build |Latest stable release | More downloads，
。Popular Aspecty docs AspectJ 5 Developers Notebook | Programming Guide | More docs.

。 Eclipse AspectJ: the book by some ofthe leading Aspecty committers

News and Events

。 older news have been purged Ifany we are going to post more recent ones here
posted 14Feb-2024

Recent Books and Articles

。Aspect in Action Second Edition
March 2009

by Ramnivas Laddad

Spring AOP 只支持方法级别的拦截，而且只能拦截 Spring 容器管理的 Bean。但是
象的方法调用、字段访问、构造方法执行、异常处理等等。

// Spring RAOP 只能做到这些

Rspect

acomponent

public class SpringRopRspect {
// 图 可以拦截: public 方法调用
8RAround("execution(pPublic * com.example.service.x*.xr(..))")
public Object aroundPub1licMethod(ProceedingJoinPoint pjp) {

return pjp.proceed();

】}

// 共 无法拦截: 字段访问
构造函数
: 私有方法
: 静态方法

Spring AOP 有哪些通知方式?

AspectJ

AboutThis Project
Team
Users

Downloads

Mailng lists

Developers

Source co

Mai

Aspectj 可以拦截任何java 对

Spring AOP 提供了多种通知方式，允许我们在方法执行的不同阶段插入逻辑。常用的通知方式有:

。 前置通知 (@Before)

。 返回通知 (@AfterReturning)
。 异常通知 (@AfterThrowing)
。 后置通知 (@Aften)

No. 1011180




## 第 102 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

。 环绕通知 (@Around)

前置通知是在目标方法执行之前执行的通知。这种通知比较简单，主要用来做一些准备工作，比如参数校验、权限
检查、记录方法开始执行的日志等等。前置通知无法阻止目标方法的执行，也无法修改方法的参数，它只能在方法
执行前做一些额外的操作。我们在项目中经常用它来记录操作日志，比如记录谁在什么时候调用了什么方法。

aspect

ecomponent

public class Loggingaspect {
8Before("execution(* com.example.service.*.x(..))")
public void logBefore(JoinPoint joinPoint) {

// 打印方法名和参数
System.out .println("调用方法: ”+ joinPoint.getSignature().getName())7
System.out .println( "参数: "+ Rrrays.toString(joinPoint.getRrgs())) 7

)}

后置通知是在目标方法执行完成后执行的，不管方法是正常返回还是抛出异常都会执行。这种通知主要用来做一些
清理工作，比如释放资源、记录方法执行完成的日志等等。需要注意的是，后置通知拿不到方法的返回值，也捕获
不到异常信息，它就是纯粹的在方法执行后做一些收尾工作。

No. 1021180




## 第 103 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

aspect
ecomponent
public class Loggingaspect {
8Rfter("execution(* com.example.service.xr.x(..))")
public void logafter(JoinPoint joinPoint) {
// 打印方法执行完成的日志

System.out .Println("方法执行完成: ”+ joinPoint.getSignature() .getName()) 7

返回通知是在目标方法正常返回后执行的。这种通知可以获取到方法的返回值，我们可以在注解中指定 returning
参数来接收返回值。返回通知经常用来做一些基于返回结果的后续处理，比如缓存方法的返回结果、根据返回值发
送通知等等。如果方法抛出异常的话，返回通知是不会执行的。

Raspect
ecomponent
public class LoggingRspect {
AfterReturning(Pointcut = "execution(* com.example.service.*.*(..))"，returning =
"result")
public void LogRfterReturning(JoinPoint joinPoint，Object result) {
// 打印方法执行完成的日志
System.out .Println("方法执行完成: ”+ joinPoint.getSignature() .getName()) 7
// 打印方法返回值
System.out .println("返回值: ”+ result) 7

异常通知是在目标方法抛出异常后执行的。我们可以在注解中指定 throwing 参数来接收异常对象。异常通知主要
用来做异常处理和记录，比如记录错误日志、发送告警、异常统计等等。需要注意的是，异常通知不能处理异常，
异常还是会继续向上抛出。

Raspect
ecomponent
public class LoggingRspect {
AfterThrowing(pointcut = "execution(* com.example.service.*.x(..))"，
throwing = "ex")
public void logRfterThrowing(JoinPoint joinPoint，Throwable ex) {
// 打印方法名和异常信息
System.out .Println("方法执行异常: ”+ joinPoint.getSignature() .getName()) 17

System.out .println("异常信息:

+ ex.getMessage()) 7

环绕通知是最强大也是我们用得最多的一种通知。它可以在方法执行前后都执行逻辑，而且可以控制目标方法是否
执行，还可以修改方法的参数和返回值。环绕通知的方法必须接收一个 ProceedingjoinPoint 参数，通过调用其
proceed() 方法来执行目标方法。

技术派 项目中就主要是通过环绕通知来实现切面。

No. 103 1180




## 第 104 页


效Spring篇V2-让天下所有的面渣都能逆效

eee 回"aicodns

Explorer                   和 SpringUtiljava AsyncExecuteAspectjava      Ds4spectjava X

~ Folder        src/ main ，间    hub ，paicoding ，forum core/ dal/ 吕 D:  t

paicoding-core
src/main
Edit 3 Add to Chat
javalcom/githubJpaic
autoconf
 DynamicConfigBinde，
 DynamicConfigC，
cache

common
pubtic       pointcut()

】

config
dal
台 DatasourceConfi..            ，                                  )

@
站
DuidcheckutUjms            pubtic      around((              proceedingJoinPoint) thro

DSJjava            2            ds = getDsAno(proceedingJoinPoint);
 DsAnojava              28           try
DsAspectjava   1     29          if (ds !=    8&R& (|        .isNotBLank(ds.ds()) 11 ds.vaLue

DsContextHolderjava                                                                 ，
DsPropertiesjava                                  .set(        .isNoneBLank(ds.ds()) ? ds.0

DsSelectExecutorjava                    了
33             return proceedingJoinPoint.proceed();

MasterslaveDsEnum
MyRoutingDatasourc                         finatty

 SqlStatelnterceptorj
if (ds !=    ) 工

Outline
Timeline
Java Projects

Maven                                 private      getDsAno(                 proceedingJoinPoint) {

如果有多个切面，还可以通过 eoradezr 注解指定先后顺序，数字越小，优先级越高。代码示例如下:

aspect
ecomponent

public class WebLogaspect {

Private final static Logger logger = LoggerFactory.getLogger(WebLogRspect.class);

Pointcut(                                        )
public void webLog() {}

eBeforel            )

public void doBefore(JoinPoint joinPoint) throws Throwable {

ServletRequestRttributes attributes = (ServletRequestRttributes)
RedquestContextHolder.getRequestRttributes()7
HttpServletRequest request = attributes.getRequest();

logger.info(
) 7

logger.info(                                          ，request.getRequestURL() .toString()) 7

No. 1041180




## 第 105 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 打印 Http method

logger.info("HTTP Method   : {}"，request.getMethod()) 17
// 打印调用 controller 的全路径以及执行方法
logger.info("class Method  : {}.{}"，
joinPoint .getSignature() .getDeclaringTypeName()，joinPoint.getSignature() .getName() );
// 打印请求的 IP
logger.info("IP                  : {}"，request.getRemoteaddr()) 7
// 打印请求入参
logger.info("Request Rrgs 。 : {}"vnew

ObjectMapper() .writeValuehsString(joinPoint.getRrgs()));
}

eRfter("webLog()")
public void doRfter() throws Throwable {
// 结束后打个分隔线，方便查看

logger.info("                                                                       End

earound("webLog()")
public object doaround(ProceedingJoinPoint proceedingJoinPoint) throws Throwable {
//开始时间

long startTime = System.currentTimeMillis() 7

Object result = proceedingJoinPoint.proceed();

// 打印出参
logger.info("Response Rrgs  : {}"，new
ObjectMapper() .writeValueRhsString(result) )
// 执行耗时
logger.info("Time-Consuming : {} ms"，System.currentTimeMillis() - startTime) 7

return result;

Spring AOP 发生在什么时候?
Spring AOP 是在 Bean 的初始化阶段发生的，具体来说是在 Bean 生命周期的后置处理阶段。

在 Bean 实例化完成、属性注入完成之后，Spring 会调用所有 BeanPostProcessor 的
postProcessAfterlnitialization 方法，AOP 代理的创建就是在这个阶段完成的。

No. 1051180




## 第 106 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

同 paicoding   和 main    <              字     QuickForumApplication 、 匡生     口

project                钙                   ing-aopyxsd 加 Springvaluep        rjava          BeanPostprocessorjava

他 AbstractFactoryBean                                              BeanPostProcessor
AutowireCapableBeanFactory
旬 AutowiredpropertyMarker
BeanDefinition
BeanDefinitionCustomizer
G BeanpDefinitionHolder
eanDefinitionVisitor
eanExpressionContext
BeanExpressionResolver

BeanFactoryPostProcessor

Beanpostprocessor                     0bject postProcessBeforeInitiatLization(0bject bean，$|

加
BeanReference                                                                           ;

ConfigurableBeanFactory

Structure
afterpropertie

BeanPostprocessor
postProcessBeforelnitialization(Obj
postprocessAfterinitialization(Objet

instanceof FactoryBean

springframework

简单总结一下 AOP

AOP，也就是面向切面编程，是一种编程范式，旨在提高代码的模块化。比如说可以将日志记录、事务管理等分离
出来，来提高代码的可重用性。

AOP 的核心概念包括切面、连接点、通知、切点和织入等

人D 像日志打印、事务管理等都可以抽离为切面，可以声明在类的方法上。像 erransactional 注解，就是一个典
型的 AOP 应用，它就是通过 AOP 来实现事务管理的。我们只需要在方法上添加 erransactional 注解，Spring
就会在方法执行前后添加事务管理的逻辑。

@) Spring AOP 是基于代理的，它默认使用JDK 动态代理和 CGLIB 代理来实现 AOP。
@ Spring AOP 的织入方式是运行时织入，而 Aspectj 支持编译时织入、类加载时织

AOP和 OOP 的关系?

AOP 和 OOP 是互补的编程思想:

，OOP 通过类和对象封装数据和行为，专注于核心业务逻辑。
2. AOP 提供了解决横切关注点 (如日志、权限、事务等) 的机制，将这些逻辑集中管理。
1.                    收录的腾讯 java 后端实习一面原题: 说说 AOP 的原理。

No. 1061180




## 第 107 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

2. java 面试指南 (付费) 收录的小米 25 届日常实习一面原题: 说说你对AOP 和 loCc 的理解。

3. java 面试指南 (付费) 收录的快手面经同学 7 java 后端技术一面面试原题: 说一下 Spring AOP 的实现
原理

4. java 面试指南 (付费) 收录的小公司面经合集同学 1 java 后端面试原题: 介绍 Spring loC 和 AOP?

5. java 面试指南 (付费) 收录的招商银行面经同学 6 招银网络科技面试原题: SpringBoot框架的AOP、
IOC/DI?

6. java 面试指南 (付费) 收录的美团面经同学 4 一面面试原题: Spring AOP发生在什么时候

7. java 面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题: Spring AOP的概念了解吗? AOP和
OOP 的关系?

memo: 2025年7月7 日修改至此，有球友提问要一个详细版的学习计划表，我用了一个早上的时间整理了一个
三个月的冲刺计划，包括八股、算法、项目的安排，已经放在了.java 面试指南中，需要的小伙伴可以自取做个参
考。

加 ，个人ni库         3个月冲刺计划 ”加                                     富 ，
加 Java面试指南 8 ~   加

-中上四- 民

QQ 搜索   x+ +

网 首页              2
二 目录          @
面试准备篇

3个月冲刺计划

如何准备面试 《完结)

如何写好简历? 《完结)
如何找到一份实习工作? 《…

时本 放让攻

如何投递简历? 完结)

什么是三方协议? 《完结)

全       一服怎么       和一个月如果说有JSVG 基友的话，你本|
而试问亲友中”一般惩各。 9 | 时间共存上评、共要外车短

21.二AOP的应用场景有哪些?

答: AOP 在实际工作/编码学习中有很多应用场景，我按照使用频率来说说几个主要的。

事务管理是用得最多的场景，基本上每个项目都会用到。只需要在 Service 方法上加个 erransactional 注解，
Spring 就会自动帮有我们管理事务的开启、提交和回滚。

1
弛| a站

No. 1071180




## 第 108 页


ee 回paicodne

Search

Transactional

kt                    Openin editor

ArticlePayServicelmpljav.。 4
-springframework.transaction.…
QTSNSSCHGNSl(rollbackFo， x
QINSEEHGNSi(rolbackFor = E-

ESSEEGi本(rolbackror =E
? ColumnSettingServicelml
springframework.transaction
QiESESEENGNSI(rolbackFor = E-
QiENSEGNGNSrolbackFor=E
QiESESEENGNSIrolbackFor = E-
QINSSEHGHSi(rolbackFor=E
? TagSettingServicelmpljav
springframework.transaction
QiESESEENGNSi(rolbackFor=E
QTSESSEENGHS(rolbackFor = E-
CommentWriteServicelmp.… 3
.springframework.transactio
QiEEESEEEGNSI(rolbackFor = E-
ESGEGNSl(rolbackFor = E..
ThirdPayHandlerjava paic-，3
-springframework.transactiol
@Transactional
Transactional
Ab       gra

.Springframeworktransaction…

日志记录也是一
间，方便后期 bug 溯源和性能调优。

个很常见的应用。在技术派实战项目中，

逆袭Spring篇V2-让天下所有的面渣都能逆效

ctjava     呈 ArticleviewControllerjava     袜 ArticlepayServicelmpljava x

|  rur    article  rvice impl/ 己 Ar  yServicelimplj

ArtictePayServiceImptL          ArticLePayService {

currentUserId

SECrouu   r = Exception.
ArticLePayInfoDT0 toPay(Long articteId，Long currentUserId，Str
ArticLePayRecordD0 dbRecord
bootLean recordChanged = falL
muttL

articLePayDao.queryRe

dbRecord = createpPayRecord(articteId，currentUserId，notes)];

recordChanged = true;

dbRecord = artictLePayDao.seLectForUpdate(dbRecord       ;

ThirdPayWayEnum payWay = ThirdPayWayEnum.ofPay(dbRecord.getPayWay(

0bjects.equats(dbRecord.getPayStatu
11 0bjects.equaLs(dbRecord.get
recordChanged = fatse;

Objects.equatLs(dbRecord .getPa

，PayStatusEnum.SUCCEED.
yStatus()，PayStatusEnum.P

Status() ，PayStatusEnum.F
dbRecord .setVerifyCode(IdUtiL.genPay
dbRecord .   tifyTime(   YTime:nutU) 7
dbRecord .setPayStatus(PayStatusEnum.NOT_PAY.get
recordChanged = true;
dbRecord    repayE

payWay，dbRecord .

Time()
is(O)

nutL

11 System.currentTimeil      dbRecord .8

就利用了 AOP 来打印接口的入参和出参日志、执行时

No. 1081180




## 第 109 页


= 目录
加技术沃API文档之Knife4j
加技术派MVC分层架构《
加技术源实体对象DO/DT，
名技术派AOP实现切面日志
加技术浙整合MyBatis-Plus
加技术派多配置文件说明

加技术派请求参数解析
加技术派Redis实现用户活
加技术派Redis实现作者白
加技术派Redis实现计数统计
加技术派整合Redis(多Redi
加技术派Redis的缓存示例
加技术派Cacheable注解实
加技术派Guava整合本地缓存
加技术派Caffeine整合本地.

加技

必Caffeine整合本地

疯二六泊二科信田实全

面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

加技术派AOP实现切面日志                                                 空

国技术派AOP实现切面日志

大家好，我是二哥呀。今天由我来给大家讲一下《技术派是如何通过 AOP 实现切
我们也会借这个机会深入探讨一下 Spring 中的 AOP 机制，毕
道很常见的面试题，简历中写专业技能的时候，一般会也写上"深入了解

过 Spring 的 AOP 机制"，这样写也会给 HR / 面试官一个不错的印象。

技术派中关于 AOP 切面的应用目前有两处，一处是 MdcAspect 用于方法执行耗时
统计，另外一处是 DsAspect 用于动态切换数:    本节关注的重点是第一处，第
二处会在"动态切换数据源"中详细讲解。

我会结合技术派的源码来帮大家彻底摘清楚 AOP，不仅能让你掌握 AOP 实现切面
志的方式，还能让你理解其原理。

什么是 AOP?

AOP，也就是 Aspect-oriented Programming，译为面向切面编程，是计算机科学

一-这部分面试可以不背，方便大家理解 start---

第一步，定义 aeMdcpot 注解:

eTarget({ElementType.METHOD，ElementType.TYPE})
eRetention(RetentionPolicy.RUNTIME )

Documented

public einterface MdcDot {

String bizCcode() default ""7

a4由2 生攻en

大网 码 ;=

什么是 AOP?

AoP

的相关术语

AOP 记录接口访问日志

SelfTraceldGenerat

为什么需要 traceid 呢?
Mdcutil

MdcDot

MdcAspect

第二步，配置 MdcAspect 切面，拦截带有 edcpot 注解的方法或类，在方法执行前后进行 MDC 操作，记录方法

执行耗时。

No. 1091180




## 第 110 页


关闭

ee@                                      paicoding - MdcAspectjava [paicoding-core

的   hhub ) paicoding ) fomum      Madchspect 台-    chainpademDemo               ei     Q@obxaQa@e

四proiect v                    Deselectexecutorjava    Mastersiav                  w     MadcDotjam    Ndcaspectjav x vv
人 paicoding-api
有 paicoding-core
v 上src
有 main
v” 四 com.github paicoding forum.core
四async                                                                {

， 站ao                                            RaKSSX      SpeLExpressionparser()

四common                                          PRKRRSERENanRDiSCOXSFSE     DefauttPars
中config
四dal                        (7aannotation(MdcDot) || awithin(MdcDpot) 7)

DatasourceConfig                                    () {

DruidcheckUtil

ps

DshAno

DsAspect                      ("getLogAnnotation())

pscontenhalder        全                   (

DaProperties                      Start       .CuUrrentTimeMil1is()

DsSelectExecutor                                      hasTag                (            )

王 pulReques

MasterslaveDsEnum
MyRoutingDataSource
Sqlstatelnterceptor                                          。       (0)

四mde
MdcAspect
MdcDot
MdcuUtil
SelrmaceldGenerator                                                                              (0
SkywalkingmraceldGenerator                                              。               (0).

四net                                     ,currentTimeillis()

闻 permission                                         (hasTag) {

四mabbtma
reset
器region                                                                                           0)

中 senstive
util
ForumCoreAutocConfig
时package-infojava
上eresources                                                                    (

signature
中    pomxml                                   method - signature.
号上epaicoding-service                                                              dot =- method

(dot       ) 工

GE GPar 可Spine 国fwmia 下1T000 人Bud 要Dopendonde -CnecSoe 人@
避 Auofeicnefmshed pminutesago)                          加301g LU urFe 4spaces 了nan 生僻 因10wup-o-date samevhuispz

MdcAspectjava            DsAspectjava            ArticleRestControllerjava

全19

Q@RequestMapping(path =
@MdcDot (bizCode =
pubtLic ResVo<NextPageHtmLVo>          (B@RequestParam(vaLue =            ) Long artictLeId
Q@RequestParam(name =        ) Long page，
@RequestParam(name =       ，required = faLse) Long 引
size = 0ptionaL.ofNuLLabLe(Ssize) .orELse(PageParam.DEFAULT_PA4GE_STZE);
size = Math.min(size，PageParam.DEFAULT_PA6E_SIZE);
PageListVo<ArticteDT0> artictes = articLeRecommendService.reLatedRecommend(articLeId，Pal
String htmL = tempLateEngineHeLper.renderToVo(
return ResVo.ok(new NextPageHtmLVo(htmL，articLes.getHasMore()));

，当接口被调用时，就可以看到对应的执行日志。

No. 1101180





## 第 111 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

2023-06-16 11:06:13,008 [http-nio-8080-exec-3] INFO
100000000.1686884772947.468581113|101|c.g.p.forum.core.mdc.Mdcaspect.handle(MdcRspect.jav
ax:47) - 方法执行耗时:

com. github.paicoding.forum.web.front.article.rest.RArticleRestController#recommend = 47

---面试可以不背，方便大家理解end---

除此之外，还有权限控制、性能监控、缓存处理等场景。总的来说，任何需要在多个地方重复执行的通用逻辑，都
可以考虑用 AOP 来实现。

1. Java 面试指南 (付费) 收录的京东面经同学 5 java 后端技术一面面试原题: AOP应用场景
2. java 面试指南(付费) 收录的理想汽车面经同学 2 一面面试原题: AOP的使用场景有哪些?
3. java 面试指南 (付费) 收录的京东面经同学 9 面试原题: 项目中的AOP是怎么用到的

memo: 2025年7月8 日修改至此，今天在星球的 VIP 群里又看到在吹画渣逆效的，球友说美团、小红书八股都
没问题，看二哥的足够。

二哥VIP12 群 (135)

二 沉默王二: 重要通知: 面渣逆袭 Red.，”移除

我基本上美团 小红书八股没啥问题 看二哥的足够

挑着看的，什么设计模式啥的都没看

档
E      设计模式我也被问了杰多

?: 挑着看的，什么设计模式啥的都没

No. 1111180




## 第 112 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

22.说说 Spring AOP 和 Aspectj 区别?

Spring AOP 只支持方法级别的织入，而且只能拦截 Spring 容器管理的 Bean。但是 Aspectj 几乎可以织入任何地
方，包括方法、字段、构造方法、异常处理等等。

六亚
夕遇

Ca一
仅支持方法级编织          可编织字段、方法、构造函数、静态初始值等
只可在Spring管理的Bean上实现             可在所有域对象实现

仅支持方法执行切入点                                         支持所有切入点

ET
创建目标对象的代理，切面在代理中执行    执行程序前，各方面直接织入代码中

从实现机制上来说，Spring AOP 是基于动态代理实现的，在运行时为目标对象创建代理，通过代理来执行切面罗
辑。而 Aspect| 是通过字节码织入来实现的，它直接修改目标类的字节码，把切面逻辑编织到目标方法中。

在实际项目中，我们大部分时候用的都是 Spring AOP，因为它能满足绝大多数需求，而且使用简单。只有在遇到
Spring AOP 无法解决的问题时，比如需要织入第三方 jar 包中的方法，或者监控字段才会考虑引入 Aspectj。

Spring AOP 借鉴了很多 Aspectj 的概念和注解，我们在 Spring 中使用的 easpect 、 epointcut 这些注解，其实
都是 Aspect| 定义的。

23.说说 AOP 和反射的区别? (补充)
2024年7月27 日增补。

反射主要是为了让程序能够检查和操作自身的结构，比如获取类的信息、调用方法、访问字段等等。而 AOP 则是
为了在不修改业务代码的前提下，动态地为方法添加额外的行为，比如日志记录、事务管理等。

从技术实现来说，反射是java 语言本身提供的功能，通过 java.lang.reflect 包下的 API来实现。而 AOP 通常
需要框架支持，比如 Spring AOP 是通过动态代理实现的，而动态代理又是基于反射实现的。

1. Java 面试指南 (付费) 收录的得物面经同学 9 面试题目原题: 抛开Spring，讲讲反射和动态代理? 那三
种代理模式怎么实现的?

24.二说说JDK动态代理和CGLIB代理的区别?
JDK 动态代理和 CGLIB 代理是 Spring AOP 用来创建代理对象的两种方式。

No. 1121180




## 第 113 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

JDK Proxy                                                CGLib Proxy
"Interface based                                        *。Subclass based

TransferService

TransferService

Extends

Implements 一 | Implements
一

Spring Proxy

| |      TransferServicelmpl

从使用条件来说，JDK 动态代理要求目标类必须实现至少一个接口，因为它是基于接口来创建代理的。而 CGLIB 代
理不需要目标类实现接口，它是通过继承目标类来创建代理的。

这是两者最根本的区别。比如我们有一个 TransferService 接口和 TransferServicelmpl 实现类，如果用jJDK 动态
代理，创建的代理对象会实现 TransferService 接口;

iterface EN  国poy | er

<= <                                           转 handler       人   11mD/ememt5
~               ao              转 bean rm
xy                                     N
(               1 一一 (人               1
N           /                        \           7

Am     Am

jzmplemenzs、~ ~ pro

如果用 CGLIB，代理对象会继承 TransferServicelmpl 类。

No. 1131180




## 第 114 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

Class 上>                      国 orow      Class
转 handler      了  extemas
extemas                  愉               国 bean              sq

( 1 一一 (人 1

Am     Am

从实现原理来说，jJDK 动态代理是Java 原生支持的，它通过反射机制在运行时动态创建一个实现了指定接口的代
理类。当我们调用代理对象的方法时，会被转发到 InvocationHandler 的 invoke 方法中，我们可以在这个方法里
插入切面逻辑，然后再通过反射调用目标对象的真实方法。

Public class JdkProxyExample {
public static void main(String[] args) {
UserService target = new UserServiceImpl())

UserService proxy = (UserService) Proxy.newProxyInstancel

target .getClass() .getClassLoader()，

target .getClass() .getInterfaces()，

(Proxy1，method，argsl) -> {
System.out .println("Before method: "+ method.getName()) 7
Object result = method.invoke(target，argsl) 1
System.out .println("Rfter method: "+ method.getName());
return resulty

) 7

Proxy.findUser(1lL) 7

CGLIB 则是一个第三方的字节码生成库，它通过 AsM 字节码框架动态生成目标类的子类，然后重写父类的方法来
插入切面逻辑。

public class CglibProxyExample 1{
public static void main(String[] args) {
Enhancer enhancer = new Enhancer() 17
enhancer.setSuperclass(UserController.class);
enhancer.setCallback(new MethodInterceptor() {
eoverride
Public Object intercept(Object obj，Method method，Object[] args，MethodProxy
Proxy) throws Throwable {
System.out .println("Before method: "+ method.getName()) 7
Object result = proxy.invokeSuper(obj，args);

No. 114 1180




## 第 115 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

System.out .println("Rfter method: ”+ method.getName()))
return resulti
}
)) 7
UserController proxy = (UserController) enhancer.create() 1

Proxy.getUser(1L) 7

选择 CGLIB 还是JDK 动态代理?
如果目标对象没有实现任何接口，就只能使用 CGLIB 代理，就比如说 Controller 层的类。

// 没有实现接口的controller
BeRestControl1Ler
public class Rrticlecontroller {
8MqdcDot (bizCcode = "article.create")
Public ResponseVo<String> create(8RequestBody RrticleReq req) {

// 业务逻辑

如果目标对象实现了接口，通常首选JDK 动态代理，比如说 Service 层的类，一般都会先定义接口，再实现接口。

// 接口定义
Public interface RrticleService {
void saveRrticle(Rrticle article);

// 实现类

eservice

public class RrticleServiceImpl implements RrticleService {
eTransactional(rollbackFor = Exception.class)
aoverride
public void saveRrticle(Rrticle article) {

// 业务逻辑

在Spring Boot 2.0 之后，Spring AOP 默认使用 CGLIB 代理。这是因为 Spring Boot 作为一个追求"约定优于配置”
的框架，选择 CGLIB，可以简化开发者的心智负担，避免因为忘记实现接口而导致 AOP 不生效的问题。

No. 1151180




## 第 116 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

utoConfiguration

      rty(prefix =          ，name =     ，havingvatue =     ，matchIfNissing = true)
pubtLic ctLass opAutoConfiguration {

@Configuration(proxyBeanMethods = fatLse)
@conditionaLOnCLass(Advice.cLass)
static cLass AspectJAutoProxyingConfiguration {

Configuration(proxyBeanMethods = fatLse)
@EnabLeAspectJAutoProxy(proxyTargetCLass = faLse)

LOnProperty(prefix =                              ，havingvatLue =
static clLass JdkDynamicAutoProxyConfiguration

ass = true)
ConditionaLOnProperty(pref:            ，name =               ，havingvatLue =
matchIfMissing = true)
static clLass CgLibAutoProxyConfiguration {

你会用JDK 动态代理吗?

我们可以用JDK 动态代理来实现这个场景。JDK 动态代理的核心是通过反射机制在运行时创建一个实现了指定接口
的代理类。

No. 116 1180




## 第 117 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

<</nierf和ce>>
IlSolver

+ Solve()

第一步，创建接口。

public interface ISolver {
void solve())

第二步，实现接口。

public class Solver implements ISolver {
aoverride

public void solve() {

System.out .println("疯狂掉头发解决问题…"”) ?

第三步，使用用反射生成目标对象的代理，这里用了一个匿名内部类方式重写 InvocationHandler 方法。
public class ProxyFactory {

// 维护一个目标对象

Private Object target1

public ProxyFactory(Object target) {
this.target = target1i

// 为目标对象生成代理对象
public Object getProxyInstance() {

return Proxy.newProxyInstance(target.getClass().getClassLoader()，
target .getClass().getInterfaces()，

No. 1171180




## 第 118 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

new InvocationHandler() {
aoverride
public Object invoke(Object proxy，Method method，object[] args)

throws Throwable {
Systemout .println("请问有什么可以帮到您? ") ?

// 调用目标对象方法

Object returnValue = method.invoke(target，args) 1

System.out .println( "问题已经解决啦! ")?
return nul17

})7

第四步，生成一个代理对象实例，通过代理对象调用目标对象方法。

public class Client {
public static void main(String[] args) {
//目标对象 :程序员
ISolver developer = new Solver() 7
//代理: 客服小姐姐
ISolver csProxy = (ISolver) new ProxyFactory(developer) .getProxyInstance() 1;
//目标方法; 解决问题

csProxy.solve() 17

你会用 CGLIB 动态代理吗?

会的。

No. 118 1180




## 第 119 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

第一步: 定义目标类 Solver，定义 solve 方法，模拟解决问题的行为。目标类不需要实现任何接口，这与 jDK 动态
代理的要求不同。

public class Solver {

public void solve() {

System.out .println("疯狂掉头发解决问题

第二步: 创建代理工厂 ProxyFactory，使用 CGLIB 的 Enhancer 类来生成目标类的子类 (代理对象) 。CGLIB 允
许我们在运行时动态创建一个继承自目标类的代理类，并重写目标方法。

Public class ProxyFactory implements MethodInterceptor {

//维护一个目标对象

Private Object target1

public ProxyFactory(Object target) {
this.target = target1i

}

//为目标对象生成代理对象

public Object getProxyInstance() {
//工具类
Enhancer en = new Enhancer() 7
//设置父类
en.setSuperclass(target.getClass());
//设置回调函数
en.setCallback(this);
//创建子类对象代理
return en.create() 7

}

eoverride

public Object intercept(Object obj，Method method，object[] args，MethodProxy proxy)
throws Throwable 1{

System.out .println( "请问有什么可以帮到您? ") ;

// 执行目标对象的方法

Object returnValue = method.invoke(target，args) 1
System.out .println("问题已经解决啦! ")?

return nul17

第三步: 创建客户端 Client，获取代理对象并调用目标方法。

No. 1191180




## 第 120 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

public class Client {
public static void main(String[] args) {
//目标对象:程序员
Solver developer = new Solver() 7

//代理: 客服小姐姐

Solver csProxy = (Solver) new ProxyFactory(developer) .getProxyInstance() 7
//目标方法; 解决问题

csProxy.solve() 17

1. java 面试指南 (付费) 收录的帆软同学 3 java 后端一面的原题: cglib 的原理
java 面试指南 (付费) 收录的腾讯面经同学 22 暑期实习一面面试原题: Spring AOP 实现原理
java 面试指南 (付费) 收录的小米面经同学 F 面试原题: 两种动态代理的区别

java 面试指南 (付费) 收录的字节跳动面经同学 8 java 后端实习一面面试原题: spring的aop是如何实
现的

5. Java 面试指南 (付费) 收录的腾讯云智面经同学 20 二面面试原题: spring aop的底层原理是什么?

6. Java 面试指南 (付费) 收录的美团面经同学 3 java 后端技术一面面试原题: java的反射机制，反射的应
用场景AOP的实现原理是什么，与动态代理和反射有什么区别

7. java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: 代理介绍一下，jdk和cglib的区
别

8. Java 面试指南 (付费) 收录的快手同学 4 一面原题: Spring AOP的实现原理? JDK动态代理和CGLib动
态代理的各自实现及其区别? 现在需要统计方法的具体执行时间，说下如何使用AOP来实现?

9. java 面试指南 (付费) 收录的理想汽车面经同学 2 一面面试原题: 了解AOP底层是怎么做的吗?

memo: 2025年7月10 日修改至此，今天在给球友修改简历的时候碰到一个对星球非常认可的球友，他在我的

帮助下也顺利找到了实习，并且大家也可以看到，他提到的这些路线规划问题、简历书写问题、秋招准备问题、项
目问题，都可以在星球里找到答案。

上 册

No. 1201180




## 第 121 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

附 件: 1个(国平必 .简历.pdf ) 查看附件
[升级】邮箱会员，更安全的邮箱体验，更大的存储空间，提高办公效率!

二哥你好，半个月之前在星球第一次向你咨询了一下，确实受益很多。现在我已经实习了半个多月了，秋招也准备了不少了，但还
是有一些疑问，希望二哥可以再指导一二。

1. 按照星球上简历教程的指示，我大概完成了一个简历框架，但中间的实习部分有点犯难。主要是因为是日常实习，所以不太能接
触到业务核心代码，还是会分配到一些开发工作，但是大多数都是写自动化脚本然后封装。所以我在简历上如实填写还是用实习
title包装项目呢。(当然其他描述措辞方面也是会修改的)

2. 关于八股文，我现在面渣的高频题基本上已经看了两三遍了，没有标高频的我就简单过了一遍，但是我看像Spring、
RocketMQ、计网之类的也很重要，所以需要再强化过一下这些没标高频的内容吗。

3. 算法方面，hot100重新写了有1/3了，掌握hot100差不多就够了吗

4. 项目方面，我现在简历里用的是技术派tpmhub。然后是只看简历上写的内容，但是我还是比较害怕到时候面试官问的太深入我
答不上来的，所以我现在应该怎样去学习这两个项目呢

5. 秋招方面，秋招差不多也要开始了，想问问星球的秋招汇总什么时候更新，或者有没有推荐的秋招汇总网站，另一方面呢我之
前春招的时候发现我有点难应付笔试，有没有什么准备笔试的方法呢。

6. 心态方面，现在比之前咨询二哥的时候好多了，但是还是会处于一种自信-自卑的转换状态，因为我也经常在b站上刷到别人面
试的视频，有时候感觉能答出一二，但是有时候感觉压力很大。主要还是没有面试经验，所以我计划秋招先投点中小厂找找感觉，
再投目标大厂，可行吗

说实话，其实我心里还是很想冲一把的。我看到其他同学拿到谷歌亚麻特斯拉还有其他金融公司的offer，其实还是很不甘心的，
也想准备好后秋招再冲一次北美市场。心情复杂，不知道该怎么表达，但无论如何，还是很感谢二哥和星球能提供一个学习的平台
的。希望是亡羊补牢，为时未晚。

事务

25.六说说你对Spring事务的理解?

Spring 提供了两种事务管理方式，编程式事务和声明式事务。编程式事务就是我们要手动调用事务的开始、提
交、回滚这些操作，虽和然灵活但是代码比较繁珊。声明式事务只需要在需要事务的方法上加上 erransactional
注解就好了，Spring 会帮有我们自动处理事务的整个生命周期。

玫

create
Transaction
getTopPosts()              于
getTransaction()      Necessary()
creates
invocation
.proceed()      |                                      |                  findAlByScore()

一-这部分可以不背，方便大家理解 start-…-

编程式事务可以使用TransactionTemplate 和 PlatformTransactionManager 来实现，允许我们在代码中直接控
制事务的边界。

public class AccountService {

No. 1211180




## 第 122 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

Private TransactionTemplate transactionTemplatey

public void setTransactionTemplate(TransactionTemplate transactionTemplate) {
this.transactionTemplate = transactionTemplatei

public void transfer(final String out，final String in，final Double money) {
transactionTemplate.execute(new TransactionCallbackWithoutResult() {
eoverride
Protected void doInTransactionWithoutResult(TransactionStatus status) {
7/ 转出
accountDao .outMoney(out，money) 7

// 转入

accountDao.inMoney(in，money) 7

)) 7

一-这部分可以不背，方便大家理解 end----

Spring 事务的底层实现是通过 AOP 来完成的。当我们在方法上加 erransactional 注解后，Spring 会为这个
Bean 创建代理对象，在方法执行前开启事务，方法正常返回时提交事务，如果方法抛出异常就回滚事务。

声明式事务的优点是不需要在业务逻辑代码中挨杂事务管理的代码，缺点是，最细粒度只能到方法级别，无法到代
码块级别。

eservice

Public class RccountService {
Rutowired
Private RccountDao accountDao

eTransactional
public void transfer(String out，String in，Double money) {

// 转出
accountDao .outMoney(out，money);
// 转入
accountDao .inMoney(in，money) 1
}
}

1. Java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: Spring 事务怎么实现的

2. java 面试指南(付费) 收录的农业银行面经同学 7java 后端面试原题: Spring 如何保证事务

3. java 面试指南 (付费) 收录的比亚迪面经同学 12 java 技术面试原题: Spring的事务用过吗，在项目里

面怎么使用的
4. Java 面试指南 (付费) 收录的虾皮面经同学 13 一面面试原题: spring事务
5. java 面试指南 (付费) 收录的阿里云面经同学 22 面经: 如何使用spring实现事务

No. 122 1180




## 第 123 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

memo: 2025年7月11 日修改至此，今天有球友在 VIP 群里讲，面渣逆袭的 Redis、MySQL、JVM 篇非常强;
另外一个球友也是继续口碑说，面过几次全包过。惫

二哥VIP12 群 (135)

上

鲍” 沉默王
量-蝇

面渣逆效 Red.… 移除

|四
Un
彰
谨
闪
二
四

没学过操作系统和计算机网络

二哥的八股 redis跟mysqljvm 非常强

怎么办

赞同，面过几次全包含

26.声明式事务的实现原理了解吗?
Spring 的声明式事务管理是通过 AOP 和代理机制实现的，大至可以分为两个阶段。

第一个阶段发生在 Spring 容器启动时，它会扫描所有的 Bean。如果发现某个 Bean 的方法上标注了
erransactional 注解，Spring 不会直接返回这个原始的 Bean 实例。而是为这个 Bean 创建一个代理对象。这
个代理对象拥有和原始对象完全相同的方法，但在内部悄悄地包惠了事务处理的逻辑。

No. 123 1180




## 第 124 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

 ArticlePayServicelmpljava x                             >    凸

comy/ github/ paicoding/ forum/ service 1/ _ article / service/ imply 台 ArticlePayServicelmpl|jj

45  pubt  Lass ArticLePayServiceImpL impLements ArticLePayService {
7曲

param articLeId
param currentUserId

QTransactionaL(CroLLbackFor = Exception.
)UbLic ArticLePayInfoDT0 toPay(Long articLeId，Long currentUserId，

ArticLePayRecordD0 dbRecord = articLePayDao.queryRecordByArtictLel
booLean recordChanged = faLse;
if (dbRecord == nuLL) {

dbRecord = createPayRecord(articLeId，currentUserId，notes) ;
recordChanged = true;

第二个阶段发生在方法调用的运行阶段，当我们的代码调用那个被 erransactional 注解修饰的方法时，实际上
调用的是 Spring 创建的那个代理对象的方法。

TransactionAspectSupport

-transactionlnfoHolder : ThreadLocal<Transactionlnfo>

#invokeWithinTransaction(Method method, Class<?> targetClass, final InvocationCallback invocation) : Object

#commitTransactionAfterReturning(Transactionlnfo txlnfo) : void
# completeTransactionAfterThrowing(Transactionlnfo txlnfo, Throwable ex) : void

cinterfacev

Transactionlnterceptor                                                               Methodlnterceptor

+invoke(final Methodlnvocation invocation) : Object

事务拦截器会在代理对象执行真正的业务逻辑之前，根据 erransactional 注解的配置获取事务属性，比如传播
行为、隔离级别等，然后通过事务管理器来开启一个新的事务。并从数据库连接池获取一个连接，关闭其自动提

Public class TransactionInterceptor implements MethodInterceptor {

aoverride

No. 1241180




## 第 125 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

public Object invoke(MethodInvocation invocation) throws Throwable 1{

// 获取事务属性

TransactionRttribute txRttr = getTransactionRttribute(invocation.getMethod()，
invocation.getThis().getClass()) 17

// 开始事务

TransactionStatus status = transactionManager.getTransaction(txRttr) 1;

try 1{
// 执行目标方法
Object retVal = invocation.proceed();
// 提交事务
transactionManager .commit(status) 7
return retVal;

} catch (Throwable ex) {
// 回滚事务
transactionManager.rollback(status) 7

throw ex7

接着，代理对象会调用原始 Bean 实例中真正的业务方法，如果业务方法顺利执行完毕，没有抛出任何异常，那么
拦截器就会通过事务管理器提交事务，将之前的所有数据库操作永久保存。

如果业务方法抛出了异常，拦截器会捕获到这个异常，并通过事务管理器回滚事务，将之前的所有数据库操作撤
销。
最后，无论事务是提交还是回滚，拦截器都会释放数据库连接。

1. Java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: Spring 事务怎么实现的

memo: 2025年7月15 日修改至此，今天在给球友修改简历时，看到球友说简历修改后拿到了星环科技内推的
实习机会，也学到了很多，并且真诚的感谢了 java 方面的八股面试题对他的帮助。讲真，能看到大家最真实的反
饥，我挺开心的。

No. 1251180




## 第 126 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

简历修改 - 星球编号zU5D      D         安全浏览模式“                                       = 优化阅读 | 精简信息和
发件人: 国有四局.JJ ..@qq.com>

收件人: 电 沉默王二<www.qing_gee@163.com>

时 间: 2025年07月14日 16:42 (星期一)

附 件: 1个( 国 时时-后端开发   pdf ) 查看附件

二哥好，去年十二月的时候麻烦您修改了一下简历，之后通过之前同事内推去星环实习了六个且，学了不少东西。星环这边有说七月

份会给我意向，十二月份开奖。但是还是打算参加一下秋招，看看是不是能有更好一点的发展，麻烦您再修改一下简历。

星环前三个月主要是在做无涯内部一些模块和熟悉项目，后面三个月在做一个toB的项目，这个项目有点类似于外包，针对客户的要求
在主项目基础上进行定制化开发，人比较少，一个前端、一个算法、一个项目经理、一个产品经理，除掉这些人以外我基本上包揽了

后端开发、部署、运维等等其他的活，从今年四月开始做，到五月中有一版上线测试环境，之后又增加了一些内容，六月中过了poc部
署到正式环境中。整个实习对于组里主项目参与的不多，感觉简历上比较难写突出贡献。目前我对简历有这样几个问题:

1、整体掌握和学习的内容和技术栈比较杂，由于我之前是做devops开发的，在星环的技术栈也是python 、java五五开的状态，是否有
必要在简历上注明java开发，还是比较笼统的写一个后端开发就行了，或者根据岗位来，岗位如果是笼统的后端开发我就只标注后端开
发。我个人实际上在求职方面是没有倾向性的，使用哪种语言都可以，八股文方面java更扎实一些，具体实操两者都差不多，还得感谢
各您这边java方面的统计和整理。

2、星环方面的实习是否要把toB项目单列出来强调，和主项目采用一个同级的排版方式，还是按照目前这样?

3、toB项目是否有一些其他比较合适的量化数据能写上去，我这边只能想到日增数据量和查询时间?

谢谢二哥。

27.@Transactional在哪些情况下会失效?

erransactional 虽然用起来很方便，但确实有一些"坑"，如果使用不当是会导致事务失效的。根据我的理解和实
践，主要有以下几种常见情况:

第一种，erransactional 注解用在非 public 修饰的方法上。

Spring 的 AOP 代理机制决定了它无法代理 private 方法。因为 private 方法在子类中是不可见的，代理类无法覆
盖它。因此，在 private 方法上加 erransactional 注解是完全无效的。同理，protected 和 default 权限的方法
也应避免使用。

Protected TransactionRttribute computeTransactionRttribute(Method methoqd，
Class<?> targetClass) {
// Don't allow no-public methodqs as required.
if (allowPublicMethodsonly() &s& !Modifier.isPublic(method.getModifiers())) {

return nul17

第二种，方法内部调用，这也是最容易被忽略的一种失效场景。如果在一个类的方法 A 中，直接调用本类的另外一
个加了 erransactional 的方法 B，那么方法 B 的事务是不会生效的。

这是因为方法 A 调用方法 B 时，使用的是 this 引用，直接访问原始对象的方法，绕过了 Spring 的代理对象，也就
导致代理对象中的事务逻辑没有机会执行。

No. 126 1180




## 第 127 页


逆袭Spring篇V2-让天下所有的面渣都能逆效

public class UserService {
Transactional

public void createUser(User user) {

saveUser(user)

private void saveUser(User user) {

解决方法是把当前类作为一个 Bean 注入到自己中，然后通过这个注入的 Bean 来调用方法 B。
PaiSmart

Explorer

Y Folder

src
main
pubti
javalcom/yizhaoqilsmartpai                 P

nn            g
FileTypevalidationServicejava                            Prdivete                              testEntityRepository7
HybridSearchServicejava
orgTagcacheservicejava
parseservicejava                  private              于
Uploadservicejava
UserServicejava                       pubtic     testprotectedTransaction() {
VectorizationService.java
test                              protectedTransactionaLMethod(name
dto

 TestEntityjava

pubtic    testProtectedTransactionWithSeLfProxy() 并

 TestEntityRepositoryjava
 TransactionTestControllerjava
ERSTRESESSSTES                 seLf.protectedTransactionatMethod (nal
utils

 GenerateJwtkeyjava                                             @

Jatutlsjava                            protected     protectedTransactionaLMethod(
Logutilsjava                                      entity = new TestEntity
PasswordUtijava                          entity.setName name)];
台 SmartPaiApplicationjava                       testEntityRepository.save(entity);
resources                                    throw new RuntimeException(messai

》 outline

第三种，如果在事务方法内部用 try-catch 捕获了异常，但没有在 catch 块中将异常重新抛出，或者抛出一个新的
能触发回滚的异常，那么 Spring 的事务拦截器就无法感知到异常的发生，也就没办法回滚。

No. 1271180




## 第 128 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Transactional
public void process() {
try 1{
// 业务罗辑
} catch (Exception e) {
// 捕获异常但没有重新抛出
// 事务不会回滚

第四种，Spring 事务默认只对 RuntimeException 和 Error 类型的异常进行回滚。如果在代码中抛出的是一个
Checked Exception，是 Exception 的子类但不是 RuntimeException 的子类，又没有通过
erransactional(rollbackFor = Exception.class) 指定事务回归的异常类型，那么事务同样不会回滚。

eTransactional
public void process() throws Exception {
// 抛出一个 checked Exception
throw new SOLException( "This is a checked exception") 7

Throwable

1. Java 面试指南 (付费)_收录的小米春招同学 K 一面面试原题: 事务传播，protected 和 private 加事务
会生效吗,还有那些不生效的情况

memo: 2025年7月16 日修改至此，今天在给球友修改简历时，看到一个中国海洋大学本，四川大学硕的球
友，非常优秀，基本上校园经历和荣誉奖项算是拉满了。能帮助到这么多优秀的球友，我也很开心。

No. 128 1180




## 第 129 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

四川大学 (985, 推荐免试) - 志一:二和时平= - 硕士

专业排名 : 前10% ; 连续两年校级二等学业奖学金，校级优秀研究生

中国海洋大学 (985) . 吧胃一Hd- 学十

专业排名 : 前15% ; 连续三年校级二等、三等学业奖学金，校级优秀学生

28.说说Spring事务的隔离级别?

事务的隔离级别定义了一个事务可以受其他并发事务影响的程度。SQL 标准定义的四个隔离级别，Spring 都支
持，定义在 TransactionDefinition 接口中。

@
外
@
加
外
且
委
全
多
全
全
外
局
全
委
全
委
外

PROPAGATION_REQUIRED = 0

Spring 在标准的隔离级别上定义了五个隔离级别:

其中 DEFAULT 表示使用底层数据库的默认隔离级别。比如说对于 MySQL 来说，默认的隔离级别是可重复读，那
就用可重复读; 对于 Oracle 来说，默认是读已提交，那就用读已提交。在实际项目中，我们也通常都用
DEFAULT，让数据库自己决定合适的隔离级别。

读未提交是最低的隔离级别，允许读取未提交的数据。这种级别会出现脏读问题，也就是一个事务可能会读到另一
个事务还没提交的数据。比如 A 事务修改了一条数据但还没提交，B 事务就能读到这个修改后的值，如果 A 事务后
来回滚了，B 事务读到的就是脏数据。这个级别在实际项目中基本不会使用，因为数据一致性无法保证。

读已提交解决了脏读问题，但会出现不可重复读问题，也就是在同一个事务中多次读取同一条数据，可能得到不同
的结果。比如 A 事务先读了一条数据，然后 B 事务修改并提交了这条数据，A 事务再次读取时就会发现数据变了。

No. 1291180




## 第 130 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

可重复读保证在同一个事务中多次读取同一条数据的结果是一致的，解决了不可重复读问题。但是会出现幻读问
题，也就是在同一个事务中多次执行同一个查询，可能会看到不同数量的记录。比如 A 事务查询某个条件的记录数
是 10 条，然后 B 事务插入了一条符合条件的记录并提交，A 事务再次查询时可能会看到 11 条记录。MySQL的
InnoDB 存储引擎通过临键锁在很大程度上解决了幻读问题。

串行化是最高的隔离级别，完全串行化执行事务，可以解决所有并发问题，包括脏读、不可重复读和幻读。但是性
能是最差的，因为事务基本上是排队执行的。在实际项目中很少使用，除非对数据一致性有极高的要求。

在 Spring 中设置隔离级别也很简单，可以在 erransactional 注解中通过 isolation 属性来指定。

eTransactional(isolation = Isolation-.RERAD_UNCOMMITTED)
public void someMethod() {

// 业务逻辑
}

不过在实际项目中，我们很少手动设置隔离级别，通常都是使用数据库的默认级别，只有在遇到特定的并发问题时
才会考虑调整。

1. java 面试指南 (付费) 收录的华为面经同学 8 技术二面面试原题: Spring 中的事务的隔离级别，事务
的传播行为?

2. java 面试指南 (付费) 收录的小米面经同学 E 第二个部门 java 后端技术一面面试原题: spring 的隔离
机制，默认是哪一种

memo: 2025年7月13 日修改至此，今天在帮球友修改简历时，碰到一个电子科技大学硕士、华中科技大学本
的球友，他说到，自己也在推荐星球给师弟们，真的非常欣慰，能有这样的口碑，很感动，必须要感谢球友们的支
持。

时 间: 2025年07月12日 17:31 (星期六)
附 件: 1个(辆 已下本:电子科技大学-硕士-有实习.pdf ) 查看附件

二哥您好，想咨询一下目前简历上的东西够不够，项目还需要增加吗?

我现在的简历有什么地方是需要简化或者详细说明的呢?

另外实习中的MQ和Redis部分是我自己编的，是不是需要一些数据才能更真实一点呢?
感谢二哥! 祝星球越来越好，自己也在推荐给师弟们。

29.六说说Spring的事务传播机制?

简单来说，当一个事务方法 A 调用另一个事务方法 B 时，方法 B 的事务应该如何运行? 是加入方法 A 的现有事
务，还是开启一个新事务，或者以非事务方式运行? 这就是事务传播机制要解决的问题。

Spring 定义了七种事务传播行为，其中 REQUIRED 是默认的传播行为，表示如果当前存在事务，则加入该事务;
如果当前没有事务，则创建一个新的事务。

No. 1301180




## 第 131 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

7种事务传播机制

QUIERD     默认，如果没有当前事务，就新建一个事务，如果存在一个事务，就加入到这个事务中

            支持当前事务，如果没有当前事务，就以非事务方法执行
              使用当前事务，如果没有当前事务，就抛出异常

新建事务，如果存在当前事务，就把当前事务挂起

以非事务方式执行操作，如果当前事务存在则抛出异常

如果当前存在事务，则在事务内执行，如果当前没有事务，则执行与REQUIRED类似操作

比如说在技术派实战项目中，一个用户解锁付费文章的操作，会涉及到创建支付订单、更新订单状态等好几个数据
库操作。

No. 1311180




## 第 132 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

@paranm
@param

Q@TransactionatL(         = Exception.cLass)
pubtLic ArticLePayInfoDT0    (Long       ，Long
ArticLePayRecordD0         = articLePayDao.

bootLean             = fatLse;

if (         == nuLU) {
忆 Edit 3 Add to Chat

= articLePay0ao .                (
ThirdPayWayEnum        = ThirdPayWayEnum.

if (0bjects .           。         ()，PayStatusEnum.SUCCEED .
11 0bjects .          。        ()，PayStatusEnum.PAYING .
= faLse)

} elLse if (0bjects.           。         ()，PayStatusEnum.FAIL
private ArticLePayRecordD0            (Long        ，Long

ArtictLeD0          = articLeReadService.               (

话 (       == nuLL) {

throw ExceptionUtitL.   StatusEnum.RECORDS_NOT_EXISTS，

ThirdPayWayEnum         = ThirdPayWayEnum .

if (     == nuLL) {

throw ExceptionUtitL.     StatusEnum.UNEXPECT_ERROR，

8&& 0bjects.        SpringUtilt。

throw ExceptionUtitL.   StatusEnum.UNEXPECT_ERROR，

ArticLePayRecordD0

不同操作的方法就可以放在一个 ezransactional 注解的方法里，它们就自动在同一个事务里了，要么一起
成功，要么一起失败。

当然，还有一些特殊情况。比如，    希望      时人日志，但不想因为主业务失败导致日志回滚。这时候
REQUIRES_NEW 就派上用场了。它不管当前有没有事务，都重新开启一个全新的、独立的事务来执行。这样，日
志保存的事务和主业务的事务就互不干扰，即使主业务失败回滚，日志也能妥有地保存下来。

No. 132 1180





## 第 133 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

另外，还有像 SUPPORTS、 NOT_SUPPORTED 这些。SUPPORTS 比较佛系，有事务就用，没事务就不用，适合
一些不重要的更新操作。而 NOT_SUPPORTED 则更干脆，它会把当前的事务挂起，以非事务的方式去执行。比如
说我们的事务里需要调用一个第三方的、响应很慢的接口，如果这个调用也包含在事务里，就会长时间占用数据库
连接。把它用 NOT_SUPPORTED 包起来，就可以避免这个问题。

eTransactional(propagation = Propagation.NOT_SUPPORTED)
public void callExternalRpi() {

// 调用第三方接口
}

最后还有一个比较特殊的 NESTED，族套事务。它有点像 RRQUIRES_NEW，但又不完全一样。NESTED 是父事务
的一个子事务，父事务回滚，它肯定也得回滚。但它自己回滚，却不会影响到父事务。这个特性在处理一些批量操
作，希望能部分回滚的场景下特别有用。不过它需要数据库支持 Savepoint 功能，MySQL 就支持。
事务能在新线程中传播吗?
事务传播机制是通过 ThreadLocal 实现的，所以，如果调用的方法是在新线程中，事务传播就会失效。
BTransactional
public void parentMethod() {

new Thread(() -> childMethod()).start()7
}

public void childMethod() {
// 这里的操作将不会在 parentMethod 的事务范围内执行
}
protected 和 private 方法加事务会生效吗?

我的理解是: 在 private 方法上加事务是肯定不会生效的，而 protected 方法在特定的代理模式下是可能生效的，
但这两种用法都应该避免，不是推荐的使用方式。

这背后涉及到 Spring AOP 的代理机制。

我先说一下JDK 动态代理，它要求目标类必须实现一个或者多个接口。也就意味着代理只能拦截接口中声明的方
法，而 protected 和 private 方法并不能在接口中声明，因此在JDK 动态代理下，这些方法的事务注解是会被直接
忽略的。

那 Spring Boot 2.0 之后，Spring AOP 默认使用的是 CGLIB 代理。CGLIB 代理是通过继承目标类来创建代理对象
的。

那对于 private 方法来说，由于无法被子类重写，所以 CGLIB 代理也无法拦截，事务也就无法生效。对于
protected 方法来说，因为它可以被子类重写，所以理论上事务是生效的。

一-这部分可以不背，方便大家理解 start-…-

我们创建一个 protected 方法，名为 protectedTransactionalMethod ，它被 arransactional 注解标记。这
个方法会先向数据库中插入一条记录 (一个 TestEntity 实例) 。紧接着，它会立即抛出一个 RuntimeException 。

No. 133 1180




## 第 134 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Q@Service
TransactionTestService {

GAutowired
TestEntityRepository testEntityRepository;

QLazy
QAutowired
TransactionTestService SeLf;

ction

hod(name:"test-protected"

Vvoid testPro   tedTransactionWi   eLfProxy

SeLf.protec                   hod(     "test-protected-proxy") ;

QTransactionatL
void protectedTransactionaLMethod(String name.
TestEntity entity        TestEntity() ;
entity.s   ame(name) ;
testEntityRepository.s:   (entity) ;
Runtimel     tion(       :"RoLLback test for protected method

。 如果事务生效: 当 RuntimeException 抛出时，Spring 的事务管理器会捕获它，并触发事务回滚。这意味
着，之前插入数据库的那条记录会被撤销。最终，数据库里不会留下这条记录 。
。 如果事务失效: 即使 RuntimeException 被抛出，由于没有事务管理，已经执行的数据库插入操作不会被撤
销。最终，数据库里会留下这条记录。
我们创建了一个 public 方法 testProtectedTransaction ，它通过 this.protectedTransactionalMethod()

的方式直接调用了那个 protected 方法。接着我们访问 /api/vl/test/transaction/protected 来触发这个调
用。

结果: 数据库中会留下一条名为 test-protected' 的记录。这证明了由于是内部调用，绕过了 Spring AOP 代理，
erransactional 注解没有生效。

我们创建了另一个 public 方法 testprotectedTransactionWithSselfProxy 。在这个方法里，我们通过一个"自
注入"的代理对象 self 来调用 self.protectedTransactionalMethod() 。接着我们通过访问
/api/vl/test/transaction/protected/proxy 来触发这个调用。

结果: 数据库中不会留下名为 test-protected-proxy' 的记录。这证明通过代理对象的调用，Spring AOP 成功拦截
并开启了事务，最终在异常发生时正确地回滚了事务。

No. 1341180




## 第 135 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

上 我的连接                            总        对象 | X 习 命令列界面 - MySQL (127.        卫 test_entity@paismart (1.
”加127oo01
、                       ,
局 information_schema                国 忆忆后     世夫图 晤由
羽 mysql                                     id             name
局 pai_coding                               并 bigint      nBc varchar(255)
羽 pai_codin91                              4 test-protected
v 力 paismart

v 卫表
了 chunk_info
了 conversations

6 test-protected

了 document_vectors
了fie_upload

卫 organization_tags
了 test_entity

了 users

一-这部分可以不背，方便大家理解 end----

1. Java 面试指南 (付费) 收录的京东同学 10 后端实习一面的原题: 事务的传播机制

2. Java 面试指南 (付费) 收录的小米春招同学 K 一面面试原题: 事务传播，protected 和 private 加事务
会生效吗,还有那些不生效的情况

3. java 面试指南 (付费) 收录的华为面经同学 8 技术二面面试原题: Spring 中的事务的隔离级别，事务

的传播行为?
4. java 面试指南 (付费) 收录的oppo 面经同学 8 后端开发秋招一面面试原题: 讲一下Spring事务传播机
制

5. java 面试指南(付费) 收录的阿里云面经同学 22 面经: 介绍事务传播模型
memo: 2025年7月14 日修改至此，今天在帮球友修改简历时，一个浙江大学硕士的球友不仅拿到了腾讯 WXG
的实习 offer，秋招也开始同步进行了，我只能说优秀的球友真的赶早不赶晚啊!
星球编号 草E] 简历 口 户 @ 忆 。 名安全浏览模式                                   精简信息
发件人: 9 Li dd1.Ggmailcom> 十
收件人: (电 沉默王二<www.qing_gee@163.com> +
时 间: 2025年07月13日 18:20 (星期日)
附 件: 1个(国 main.pdf ) 查看附件          浙大硕

|一哥您好，这周未我把简历大致改了一下，主要添加了暑期实习的经历，因为我还没离职所以mentor可能还会给我一些新的
活，到时候我再补进去，麻烦您现在先看一下。   、
腾讯 WXG 实习

另外我想请问下:
还能这么早准备秋招
1、有没有必要把目前的这个业务透视项目换成一个RAG项目?

PP、今年秋招开得特别早，我本来打算八月中旬离职之后复习一下八股文再开始投简历，但似乎七月初就陆续有企业开秋招了，
目前八股文、项目、算法这些想再准备起来的话还需要一定时间，按目前的情况来看什么时候投简历会比较合适?

No. 1351180




## 第 136 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

MVC

30.Spring MVC 的核心组件有哪些?

Spring MVC 作为 Spring 框架中处理 Web 请求的核心模块，它的设计遵循了经典的 MVC 模式，根据我的理解，
它的核心组件主要包括:

前端控制器 DispatcherServlet，这是 Spring MVC 的入口和核心调度器。当一个 HTTP 请求到达服务器时，首先
由 DispatcherServlet 接收。它负责将请求分发到合适的处理器，也就是 Controller 中的方法，并协调其他组件的
工作。

1 Hander                                                                                                       TH给一有有二求

2 同人同性

1组克                                                                                    Ta

3他人

4去和定居

4作为天

DispatcherServet 前置控      E

四

2 扣抽行和pn
1522着Hangerg用                                                                         22 andonuappng
2所                                                                                                                      12关执

3 昌江post                                                                                                                                                                                     123 hanathaapier

4后果站理                                                                         24天林站果

ER                                                                   具体业和办

2                                                                           2 seveteaon
一一一| smeoe                                         2
an                                                        .13不地到

.14全有

ET

apeauesapprgranaenaaoner                                                                                                                                                  21关Conboler二|

nappequestanaeaaapter                                                                                                                                        22 天RapRequestanger
1                                                      2

3使用

aa smeecomolenangehaapner

eao

1224是

Spring MVC

1                                                                                                                                              auRLEiEshangr

2生病和
内                                                                                  2

ET

4

zandera果                                                                                                                                                                                  SReaueatvappngranaietecomg

T22 pepaichnwsevealst                                                                                                                                                                                  22 Beannameunranaervappng

2处理和                                                                                                                   2

723人昌sweoesovw                                                                                                                                              23smeeurkanaerveopr

4                                                                                                                                              24poueunctonwappng

1 理和虽                                                                                                                        phanaa)

2 去名术|                                                                    2 RE理 Iposptanaa)

一|                                             一

ET                                                                                                                 3六昌 anerConplton)
区                                                                    1414下
memahesoucaanResover                                                                    121

22 mynaeavewpesoner
一| wma                                                      7]

coneneootangveopeaove

在Spring Boot 项目中，DispatcherServlet 的启动是通过自动配置完成的。Spring Boot 会自动注册一个默认的
DispatcherServlet，并将其映射到 / 。

eBean
Public ServletRegistrationBean<DispatcherServlet>
dispatcherServletRegistration(DispatcherServlet dispatcherServlet) {
ServletRegistrationBean<DispatcherServlet> registration = new
ServletRegistrationBean<>(dispatcherServlet，"/"); // 默认映射路径为“/"
registration.setName("dispatcherServlet'") 7

return registrationy

No. 1361180




## 第 137 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

处理器映射 HandlerMapping，当一个请求进来时，前端控制器会询问处理器映射:“这个 URL 应该由哪个
Controller 的哪个方法来处理? “然后它就会根据 eaRequestMapping 、eGetMapping 这些注解来匹配请求。

回 "aicodne

Explorer                                                        的 ArticleListRestControllerjava x

Y Folder                                                   由

@RequestMapping(path = "articte/api/List")
RestControttLer
GlobalviewConfigjava                ArticLeListRestControLLer     BaseViewControtLtef|

PaiWebConfigjava                               @Autowired

error                                     ArticteReadService articteServicei

Q@Autowired
TempLateEngineHeLper tempLateEngineHeLper';

front
article
extra
rest
 ArticleListRestController-

categoryId
ticleRestCont                                        page
ColumnRestControllerjava                              size

6GetMapping(path = "data/category/{categoryj"

i          el      categol
串 columnviewcontrollerjava               ResVo<PageListVo<ArticLeDT0>>     r

vo

Outine                                         Pageparam pageParam = builtdl      am(page，size);

PageListVo<ArticLeDT0> List = articLeService.ql
ResVo.ok(List) 7

Timeline
Java projects

Maven

@o9  @

处理器 Handler，实际上就是我们写的 Controller 方法，这是真正处理业务逻辑的地方。

处理器适配器 HandlerAdapter，负责调用该处理器的方法，并处理参数绑定、类型转换等。
同的类型，比如注解方式、实现接口方式等，处理器适配器就是为了统一调用方式。

视图解析器 ViewResolver，处理完业务罗辑后，如果需要泻染视图，ViewResolver 会根据返回的视图名称解析实
际的视图对象，比如 Thymeleaf。在前后端分离的项目中，这个组件更多用于返回JSON 数据。

处理器可能有不

No. 1371180




## 第 138 页


渣逆袭Spring篇V2-让天下所有的面渣都能逆效

Q6etMapping("/data/detaiL/{farticLeId}y")

pubLic ResVo<ArticLeDetaiLVo>

ArticLeDetaiLVo

ArticLeDT0

BaseUserInfoDT0

return ResVo.ok(vo) ;

GQ@Permission(
GQ6etMapping(
pubLic String

(GPathVvariabtLe(

new                  (1;

= articLeService.
(MarkdownConverter .

);

= UserService.

(

UserRoLe.LOGIN)
"edit")
(G@RequestParam(

ArticLeEditVo
if (
} elLse {

new
!= nuLL) {

(attributeName:"vo

return "Views/articLe-edit/index" ;

异常处理器 HandlerExceptionResolver，捕获并处理请求处理过程中抛出的异常。通常，我们可以
econtrolleradvice 和 eExceptionHandler 来自定义异常处理逻辑，确保返回友好的错误响应。

Y 回global

》回vo
@ BaseviewController
回 ForumExceptionHandler
上 GlobalExceptionHandler
@ Globalnitservice
回 SeolnjectService

回 hook

回integration

回javabetter

加leetcode

)        :=
(ForumAdviceException e)

(vatue = ForumAdviceException.
ResVo<String>
ResVo.fail(e.getStatus());

还有文件上传解析器
处理前后执行一些额外的逻辑，比如权限校验、日志

MultipartResolver，用于处理文件上传请求; 拦截器 Handlerlnterceptor，用于

No. 1381180





## 第 139 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

memo: 2025年7月17 日修改至此，昨天有球友说手写了一个 Redis 的轮子项目，用的 Go 语言，我今天去看了
一下 doc 和代码，写得非常好，代码注释很清晰，doc 写得很详细，能看得出球友的用心。手写轮子是非常考验一
个人的能力的，我看他实现的功能有: 字符串和散列的数据类型、RESP 协议解析器、使用goroutine 来同时处理
多个连接、持久化 AOF 协议等，非常强。

3和。 Leafer                                                                                                                   3 收进专栏
We

球友们好呀，这是我学习的时候用 Golang 从 0 写的一个轮子项目，实现的 Redis ，从搭项目到压测都写在文档里了，如
果大家感兴趣可以看下点点 Star (求求，互相学习全

如果能贡献就更好了仿
终GitHub - inannan423/redigo: 使用 Go 语言复刻 Redis 的部分功能…

31.二Spring MVC 的工作流程了解吗?

简单来说，Spring MVC 是一个基于 Servlet 的请求处理框架，核心流程可以概括为; 请求接收 一 路由分发 一 控
制器处理 一 视图解析。

一一一2. 请求查找Handler一一

一一.Request请求一一>                                                                                  HandlerMapping
返回一个执行链一处理          器
<一11. Response响应                                    3.返回一个执行链                     器哆和
10. 视图泻染
4. 请求适配器执行Handler
8. 请求进行视图解析                             6. ae
9. 返回view                                                                        5 执行

7. 返回ModelAndVi SN
HandlerAdapter
本

No. 1391180




## 第 140 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

村

《servle     e>-Sservlet. xml

总
Dispatcherserviet 咕:                     HandlierAdapter

ModelAndView

HttpMessageConveter

ViewResolver

是否配置            有配置
<mvcdefault- servlet-
handler/>?_

若| 返回目标资源

1.发送请求URL

13.最后执行拦截器的
afterCompletion方法

4 .返回对应的执行链包含 (Handler处理器对
12 党染视图，填充数据                               象、Handlerlnterceptor处理器拦器对
HandlerException组     (processDispatchResult方法)                                        象)
件处理异常并得到新的
ModelAndVview
8 返回ModelAndView模型视图对象
ModelAndview
和                                 冯:          5根据Handler对象找到
HandlerExecutiohchain对象       人
的applyPostHadle()方法        合适的处理器适配器
和在异常?               10.调用Handlerlnterceptor拦                                                一
是               截器的postHandle方法检查异常                                             6执行handlle方法

用户发起的 HTTP 请求，首先会被 Dispatcherservlet 捕获，这是 Spring MVC 的“前端控制器"，负责拦截所有请
求，起到统一入口的作用。

DispatcherServlet 接收到请求后，会根据 URL、请求方法等信息，交给 HandlerMapping 进行路由匹配，查找对
应的处理器，也就是 Controller 中的具体方法。

No. 1401180




## 第 141 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

G@param articLeId
Qreturn

G          (rotLe =
Q            (path =
pubtLic        edit(Q@             required               articLeId，
vo = new ArticLeEditVo
if (articLeId !=
eLSe
modeL.addAttribute(attributeName :
return

找到对应 Controller 方法后，DispatcherServlet 会委托给处理器适配器 HandlerAdapter 进行调用。处理器适配
器负责执行方法本身，并处理参数绑定、数据类型转换等。在注解驱动开发中，常用的是
RequestMappingHandlerAdapter。这一层会把请求参数自动注入到方法形参中，并调用 Co

业务逻辑。

国 nacodne 。 ”man                                       QuickForumApplication v

图2 X        ResolverRegistrarjava      RequestMappingHandlerAdapterjava      AsyncExecuteAspectjava
口mwe
四annotation                   口 pupbtic class RequestHappingHandLerhdapter extends AbstractHandLerWethodAdapter
串condion                            impLements BeanFactoryhAware，InitiatizingBean
丫method
“下ameation                                   spring xm.ignore
AbstractMappingJacksonRe
AbstractMessageConverter
AbstractMessageConverter
AmmamsskMethodnetuma            private static finaL booLean shouldIgnoreXnt = SpringProperties.getFLag(
CalableMethodReturnvaiue
ContinuationHandlerMethoc
DeferredResutMethodRetul

ExceptionHandlerException

pubtic static finat WethodFitter INIT_BIWNDER_HETHODS =      method ->

AnnotatedELementUtitLs.hashnnotation(method，TnitBinder-ctass);
ExtendedServletRequestDa

HttpEntityMethodprocessor
HttpHeadersReturnvalueHa

JsorViewRequestBodyAdvit      GE     pubtic static finat MethodFi

JsonViewResponseBodyAd                ClAnnotatedE         4     ，Requesthapping.ctass) 让
MatriwvariableMapMethodA                      Annotete                               bwte .ctess)
MatrivariableMethodArgun
ModelAndviewMethodRetu
ModelAndviewResolverMet
MvcuricomponentsBuilder
package-info
PathvariableMapMethodArg
PathvariableMethodArgume

tt                   tMappingl            下 多 到

private ListcHandLerWethodArgumentResotver> customArgumentResotvers;

WuLLabte
private HandLerWethodArgumentResoUverConposite argumentResotvers

Controller 方法最终会返回结果，比如视图名称、ModelAndView 或直接返回JSON 数据。

No. 1411180





## 第 142 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

当 Controller 方法返回视图名时，DispatcherServlet 会调用 ViewResolver 将其解析为实际的 View 对象，比如
Thymeleaf 页面。在前后端分离的接口项目中，这一步则通常是返回JSON 数据。

最后，由 View 对象完成泻染，或者将JSON 结果直接通过 DispatcherServlet 返回给客户端。
为什么还需要 HandlerAdapter?

Spring MVC 支持多种风格的处理器，比如基于 econtroller 注解的处理器、实现了 Controller 接口的处理器
等。如果没有处理器适配器，DispatcherServlet 就需要硬编码每种处理器的调用方式，框架就会变得非常僵硬
一一新增一种 Controller 类型，就必须改 DispatcherServlet 的代码。

因此，Spring 引入了 HandlerAdapter 作为适配器，屏蔽不同控制器的差异，给 DispatcherServlet 提供一个统一
的调用入口。

比如说，如果是实现了 Controller 接口的处理器，DispatcherServlet 会使用 SimpleControllerHandlerAdapter
来适配它。

public class SimpleCcontrollerHandleradapter implements HandlerRdapter {

eoverride
public boolean supports(Object handler) {
return (handler instanceof Controller))

eoverride

eNullable

Public ModelandView handle(HttpServletRequest request，HttpServletResponse responsey
Object handler)

throws Exception {

return ((Controller) handler) .handleRequest(request，response) 1;

// .…. .省略一个无关方法 ..-

如果是使用 eaRequestMapping 注解的处理器，DispatcherServlet 则会使用 RequestMappingHandlerAdapter
来适配。

public class ReqduestMappingHandlerRdapter implements HandlerRhdapter {
aoverride
public boolean supports(Object handler) {
return (handler instanceof HandlerMethod))

}

eoverride

eNullable

public ModelRndView handle(HttpServletRequest request，HttpServletResponse response，
Object handler)

throws Exception 1{
HandlerMethod handlerMethod = (HandlerMethod) handler';
// 执行方法并返回 ModelandView

No. 142 1180




## 第 143 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

return invokeHandlerMethod(handlerMethod，request，response) 1

1. java 面试指南 (付费) 收录的腾讯 java 后端实习一面原题: 说说前端发起请求到 SpringMVC 的整个处
理流程。

2. java 面试指南 (付费) 收录的国企面试原题: 说说 SpringMVC 的流程吧

3. Java 面试指南 (付费) 收录的小公司面经同学 5 java 后端面试原题: springMVC 工作流程 我大概就是
按面渣逆袭里答的，答到一半打断我: 然后会有个 Handler，这个 Handler 是什么东西啊。前面
Handler 不是已经知道 controller 了吗，我直接执行不就行了，为什么还要 Adapter 呢。

4. Java 面试指南 (付费) 收录的京东面经同学 8 面试原题: SpringMVC框架
5. Java 面试指南 (付费) 收录的字节跳动同学 17 后端技术面试原题: springmvc执行流程

memo: 2025年7月18 日修改至此，今天在帮球友修改简历时，碰到一个荣誉奖项基本拉满的球友，国家励志
奖学金、省级比赛、校级三好学生等，那这里也是温韦提醒一下大家，学校的荣誉奖项如果你有能力争取，有时间
争取，还是尽量争取一下的，尤其是求职央国企的时候，会非常有用。

。本科”GPA : 3.851/43   专业排名: 前 4%

。英语 “CET-6: 519 / CET-4: 591

。 ( 国家级 ) 国家奖学金

。( 校级 ) 优秀毕业生、校一等奖学金、校二等奖学金x2

。( 省级 ) 信息安全竞赛二等奖、大学生物理学术竞赛一等奖

。( 国家级 ) 大学生英语竞赛二等奖、三等奖

。( 校级 ) 互联网加人金奖、数学竞赛二等奖、数学建模竞赛二等奖

32.SpringMVC Restful 风格的接口流程是什么样的呢?

在传统的 MVC 中，Controller 方法通常返回一个视图名称或者 ModelAndView 对象，然后由视图解析器
ViewResolver 解析并泻染成 HTML 页面。但在 RESTful 架构中，通常返回的是JSON 或XML，不再是一个完整的
页面。

其中很重要的两个注解: eaRestcontroller 相当于 econtroller 和 eResponseBody 的结合。当在一个类上使
用 eRestcontroller 时，它会告诉 Spring 这个类中所有方法的返回值都应该被直接写入 HTTP 响应体中，而不
再被解析为视图。

eResponseBody 可以用在方法级别，作用相同。它标志着该方法的返回值将作为响应体内容，Spring 会跳过视图
解析的步骤。

HttpMessageConverter 是实现 RESTful 风格的关键。当 Spring 检测到 eaResponseBody 注解时，它会使用
HttpMessageConverter 来将 Controller 方法返回的 java 对象序列化成指定的格式，如JSON。

默认情况下，如果类路径下有 jackson 库，Spring Boot 会自动配置 Mappinglackson2HttpMessageConverter
来处理JSON 的转换。相应的，对于带有 eRequestBody 注解的方法参数，它也会用这个转换器将请求体中的
JSON 数据反序列化成Java 对象。

No. 1431180




## 第 144 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

MappingHandlerAdaplerjava     paiwebCanfigjava

所以，RESTful 接口的流程可以概括为: 请求到达前端控制器 DispatcherServlet 一 通过 HandlerMapping 找到对
应的 Controller 方法 一 执行方法并返回数据 一 使用 HttpMessageConverter 将数据转换为JSON 或 XML 格式 一
直接写入 HTTP 响应体。

Handlerllapping
处理呈映射加
2蒜取处理器
划寻sriccnadlispRespoose实多
1 Request请求
4                      和                         andleryethodReturnValueHiandler          xyxktottz II
方法返回值处理器
.Resnpaem应前是控制                            Controller                                 对生入响应的人进行on亩到化
|                                           ServletInvocableliandleriethod
瑟入只应内册流中

6. 返回ModelAndView (nul1)
3. 请求适配器执行Handler

和执行

了返回ModelAndView null)

Handlerhdapter
处理器适配器

总结来说，RESTful 接口的流程通过 eRestcontroller 和 HttpMessageConverter “抄了近道"，省略了

ViewResolver 和 View 的渲染过程，直接将数据转换为指定的格式返回，非常适合前后端分离的应用场景。

memo: 2025年7月19 日修改至此，今天有球友私信我说，拿到了京东的实习 offer，问接下来的秋招该怎么准
备? 那 7 月份实习 Offer 确实会比较少，但仍然有一部分，如果这个阶段还想要冲实习的话，确实可以捡漏。

No. 1441180




## 第 145 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

二哥，您好。我最近拿到了京东后端开发的实习
offer，但据我了解，实习期要满三个月，也就是
下4.H点正
大量吕站 四如对-”。 。让“错过
和-WE
万 下下Ti。几乎
江让所7 ET和有 呈 辣一下一可，
上 一人一

Spring Boot

33.二介绍一下 SpringBoot?
Spring Boot 可以说是 Spring 生态的一个重大突破，它极大地简化了 Spring 应用的开发和部署过程。

以前我们用 Spring 开发项目的时候，需要配置一大堆 XML 文件，包括 Bean 的定义、数据源配置、事务配置等
等，非常繁珊。而且还要手动管理各种 jar 包的依赖关系，很容易出现版本冲突的问题。部署的时候还要单独搭建
Tomcat 服务器，整个过程很复杂。Spring Boot 就是为了解决这些痛点而生的。

“约定大于配置"是 Spring Boot 最核心的理念。它预设了很多默认配置，比如默认使用内风的 Tomcat 服务器，默
认的日志框架是 Logback 等等。这样，我们开发者就只需要关注业务罗辑，不用再纠结于各种配置细节。

No. 1451180




## 第 146 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

自动装配也是 Spring Boot 的一大特色，它会根据项目中引入的依赖自动配置合适的 Bean。比如说，我们引入了
Spring DatajJPA，Spring Boot 就会自动配置数据源; 比如说，我们引入了 Spring Security，Spring Boot 就会自
动配置安全相关的 Bean。

Spring Boot 还提供了很多开箱即用的功能，比如 Actuator 监控、DevTools 开发工具、Spring Boot Starter 等
等。Actuator 可以让我们轻松监控应用的健康状态、性能指标等; DevTools 可以加快开发效率，比如自动重启、
热部署等; Spring Boot Starter 则是一些预配置好的依赖集合，让我们可以快速引入某些常用的功能。

Spring Boot常用注解有哪些?
Spring Boot 的注解很多，我就挑两个说一下吧。

。 espringBootaApplication : 这是 Spring Boot 的核心注解，它是一个组合注解，包含了
econfiguration 、Enableautoconfiguration 和 ecomponentscan 。它标志着一个 Spring Boot 应用

的入口。
。 espringBootTest : 用于测试 Spring Boot 应用的注解，它会加载整个 Spring 上下文，适合集成测试。
1. Java 面试指南 (付费) 收录的华为 OD 面经中出现过该题: 讲讲 Spring Boot 的特性。

2. Java 面试指南 (付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: SpringBoot基本
原理

3. Java 面试指南 (付费) 收录的国企零碎面经同学 9 面试原题: Springboot基于Spring的配置有哪几种
4. java 面试指南 (付费) 收录的阿里云面经同学 22 面经: springboot常用注解

memo: 2025年7月 20 日修改至此，今天又有球友发私信说，后悔没有早一点加入星球，加入星球后，才发现
大家早早就为自己的未来去拼搏了。很真实，好吧，这就是星球的价值所在，100 多块钱的门票就能提供学校几万
学费给你不了的东西。

No. 146 1180




## 第 147 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

14:45

融 咽咽，谢谢二哥 里

看到二哥你的消息的时候我在想如果干一个月怎
么规划，所以没有及时回消息，虽然现在也还没
想好图

真后悔没有早点加入星球，加入星球后，才发现
大家早早就为了自己的未来去拼搏，我也明白学
好一门技术是需要长期去积累的。

然后就是没有早点去实习，实习后看到了很多不
一样的东西，也逐渐明白了为啥哪些拿大厂 offer
的人最后会选择去体制内。

34.二Spring Boot的自动装配原理了解吗?

在 Spring Boot 中，开启自动装配的注解是 aenableautoconfiguration 。这个注解会告诉 Spring 去扫描所有可
用的自动配置类。

No. 1471180




## 第 148 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

paicoding - EnableAutoConfiguration.java [Maven: org.springframework.boot:spring-boot-autoconfigure:2.7.1]
EnableAutoConfiguration 县~           ThreadLocalExample               G                            b 六 Q  和

语auickrorumApplicationjava       & springBootApplicationjava EnableAutoconfigurationjava         Reqinfocontextjava ThreadLocaljava        v

Reader Mode

ENABLED_OVERRIDE_PROPERTY

于 PulRequests
aseqelea 图

elea6口

困 Bookmarks

QFnd Run @Bproblems pct 人@profiler 查Ssprng 国Teminal 汉TOD0 人Buid 压Dependencies   Checkstyle ”人@@ services 。 师 Event Log
器 Auto fetch: fnished (9 minutes ago)                             加 as518 LF urr-8 4spaces 刷man 侈 因22wof1+ 器

Spring Boot 为了进一步简化，把这个注解包含到了 espringBootapplication 注解中。也就是说，当我们在主
上使用 espringBootapplication 注解时，实际上就已经开启了自动装

当 main 方法运行的时候，Spring 会去类路径下找 spring.factories 这个文件，读取里面配置的自动配置类列
表。比如在我们的技术派项目中，paicoding-core 和 paicoding-service 模块里都有 spring.factories，分别注册
了 ForumCoreAutoConfig 和 ServiceAutoConfig，这两个配置类就会在项目启动的时候被自动加载。

项目                                                                    RabbitmqServicelmpljava         WxCallbackRestControllerjava

[TITTT

Y 加paicoding [paicoding-forum]
org.springframework.boot.autoconfigure.EnabLeAutoConfiguration=\

白 .github
外idea
自 vscode
白docs

com.github.paicoding.forum.core.ForumCoreAutoConfig

外ogs
CO paicoding-api
局 paicoding-core
~ 四sr

白main

Djava

resources
Y 白 META-INF
pring.factories

然后每个自动配置类内部，通常会有一个 econfiguration 注解，同时结合各种 econditional 注解来做条件控
制。像技术派的 RabbitMqAutoConfig 类，就用了 econditionalonProperty 注解来判断配置文件里有没有开启
rabbitmq.switchFlag，来决定是否初始化 RabbitMQ 消费线程。

No. 1481180





## 第 149 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

喇paicodine Ipaicoding-foruml

pring factores

另外一个常见的场景是自动注入 Bean，比如       的 ServiceAutoConfig 中就用了 ecomponentscan 来扫描
service 包，eMapperscan 扫描 MyBatis 的 mapper 接口，实现业务层和 DAO 层的自动装配。

具体的执行过程可以总结为: Spring Boot 项目在启动时加载所有的自动配置类，然后逐个检查它们的生效条件，
当条件满足时就实例化并创建相应的 Bean。

SpringBoot自动配置原理
AutoConfi   ionImportSel
SpringBoot注解             Spring类导入                        0 OO Po ee
读取META-INF/spring factorics，
获取自动配置类路径
改全导入类

自动装配的执行时机是在 Spring 容器启动的时候。具体来说是在 ConfigurationClassPostProcessor 这个
BeanPostProcessor 中处理的，它会解析 econfiguration 类，包括通过 ermport 导入的自动配置类。

Protected RutoConfigurationEntry                                                      (RnnotationMetadata

annotationMetadata) {

// 检查自动配置是否启用。如果econditionalonCclass等条件注解使得自动配置不适用于当前环境，则返回一个
空的配置条目。

if (!isEnabled(annotationMetadata)) {
return EMPTY_ENTRY7

】}

// 获取启动类上的eaEnableautoconfiguration注解的属性，这可能包括对特定自动配置类的排除。

RnnotationRttributes attributes = getRttributes(annotationMetadata) 7

No. 1491180




## 第 150 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 从spring.factories中获取所有候选的自动配置类。这是通过加载META-INF/spring.factories文件中对

应的条目来实现的。

List<String> configurations = getCandidateConfigurations(annotationMetadatay

attributes)

6.

memo

何选择

// 移除配置列表中的重复项，确保每个自动配置类只被考虑一次。

configurations = removeDuplicates(configurations))

// 根据注解属性解析出需要排除的自动配置类。

Set<String> exclusions = getExclusions(annotationMetadata，attributes) 7

// 检查排除的类是否存在于候选配置中，如果存在，则抛出异常。

checkExcludedClasses (configurations，exclusions) 1

// 从候选配置中移除排除的类。

configurations .removeRll(exclusions);
// 应用过滤器进一步筛选自动配置类。过滤器可能基于条件注解如econditionalOnBean等来排除特定的配置
configurations = getConfigurationClassFilter().filter(configurations)7

// 触发自动配置导入事件，允许监听器对自动配置过程进行干预。

fireRutoConfigurationImportEvents(configurations，exclusions))

// 创建并返回一个包含最终确定的自动配置类和排除的配置类的autoconfigurationEntry对象。

return new RutoCconfigurationEntry(configurations，exclusions))

.java 面试指南 (付费) 收录的滴滴同学 2 技术二面的原题: SpringBoot 启动时为什么能够自动装配
. java 面试指南 (付费) 收录的腾讯面经同学 22 暑期实习一面面试原题: Spring Boot 如何做到启动的

时候注入一些 bean

.java 面试指南(付费) 收录的比亚迪面经同学 3 java 技术一面面试原题: 说一下 Spring Boot 的自动

装配原理
java 面试指南 (付费) 收录的农业银行同学 1 面试原题: spring boot 的自动装配

.java 面试指南(付费) 收录的百度面经同学 1 文心一言 25 实习 java 后端面试原题: SpringBoot如何

实现自动装配
java 面试指南(付费) 收录的 OPPO 面经同学 1 面试原题: 自动配置怎么实现的?

: 2025年7月21 日修改至此，今天有球友发私信说，拿到了亚信科技+新石器无人车的 offer，问我该如
，如果是你，你会如何选择呢?

No. 1501180




## 第 151 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

二哥你好，想咨询一个offer问题。24 届留子，
回国第一份工作。北京亚信科技总部的Al产品策
划，3*虽的总包。薪资很有诱惑力但是我看网上
风评不好，其他也查不到太多的信息。谢谢八

还有一个offer就比较低了，新石器无人车。也是
产品方向，31 四总包

没有别的offer了

35.盖如何自定义一个 SpringBoot Starter?

第一步，SpringBoot 官方建议第三方 starter 的命名格式是 xxx-spring-boot-starter，所以我们可以创建一个名为
my-spring-boot-startez 的项目，一共包括两个模块，一个是 autoconfigure 模块，包含自动配置逻辑; 一个
是 starter 模块，只包含依赖声明。

<properties>
<spring.boot.version>2.3.1.RELEASE</spring.boot.version>
</properties>

<dependencies>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-autoconfigure</artifactId>
<version>${fspring.boot.version}</version>

</dependency>

<dependency>
<groupId>org.springframework.boot</groupId>
<artifactId>spring-boot-starter</artifactId>

<version>${fspring.boot.version}</version>
</dependency>
</dependencies>

第二步，创建一个自动配置类，通常在 autoconfigure 包下，该类的作用是根据配置文件中的属性来创建和配置

Bean。

No. 1511180




## 第 152 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

econfiguration
egnableConfigurationProperties(MYyStarterProperties.class)
Public class MyServiceRAutoConfiguration {

Bean
econditionalOnMissingBean

Public MyService myService(MYyStarterProperties properties) {
return new MyService(Properties.getMessage());

第三步，创建一个配置属性类，用于读取配置文件中的属性。通常使用 econfigurationProperties 注解来标记

这个类。

econfigurationProperties(prefix = "mystarter")

public class MyStarterProperties {
Private String message = "二哥的 Java 进阶之路不错啊!";
public String getMessage() {

return message)

public void setMessage(String message) {
this.message = message;

第四步，创建一个简单的服务类，用于提供业务逻辑。

public class MyService {

private final String message)

public MyService(String message) {
this.message = message;

public String getMessage() {
return messagey

第五步，在 src/main/resources/METR-INF 目录下创建一个名为 spring.factories 文件，告诉 SpringBoot 在启
动时要加载我们的自动配置类。

org.springframework.boot .autoconfigure.EnableRutoConfiguration=\

com.itwanger.mystarter.autoconfigure.MyServiceRutoCconfiguration

第六步，使用 Maven 打包这个项目。

No. 1521180




## 第 153 页


效Spring篇V2-让天下所有的面渣都能逆效

mvn clean instal1l

第七步，在其他的 Spring Boot 项目中，通过 Maven 来添加这个自定义的 Starter 依赖，并通过
application.properties 配置信息:

mystarter.message=javabetter.cn

然后就可以在 Spring Boot 项目中注入 MyStarterProperties 来使用它。

ieBoot =    w       helaspringBoot ) 说Halos
蝇pmoject ~

证 -四helospringBoot                                    package
下mdea

人名 aspringBootApptication
om cmowerhellospringBoo         aRestControtter
了                       public class
HellospringBootApplication
aResource
myStarterproperties

aRequestMapping(@v      )
Pub1ic      hetto() 萎

idonors                                      return myStarterProperties .

HELPmd                   22        引

Public static void main(     [] args) {
(                  .class，args)

册 一

024-94-99 11:37:28.                     main] org     catatina.co           e : starting Servtet engine: [Apache
2924-94-99 11:37:28.                    main] oa    ITomcat] .              : Initiatizing Spring embedded Web

2024-94-99 11:                        main]                         3 Root WebAppticationContext: init:
2624-94-99 11:37:29                   main] 0.5.s     e    a    as       : Initiatizing ExecutorService "apl
2024-94-99 11:     .:                       main]           :                    : Exposing 2 endpoint(s) beneath bi
20924-94-99 1     区                       main] 0           -     。             : Tomcat started on port(5): 8081 1
2624-84-09 1      -                [         main]     。                     Started HeLLospringBootAppticatil
2624-94-09 1      -               [on(2)-127.6.9.1] 。             -。                 : Initiatizing Spring Dispatchersel
2624-84-89 11:37:29.             Ton(2)-127.9.9.1]         t.Dispatcher          : Initiatizing Servtet "dispatcher

2624-94-69 11:37:29.             [on(2)-127.9.9.1] .s.web.servile     t      : Compteted initiatization in 3 ms

克Javaentepriss   。      cneckstw    人         中    "           Gem

启动项目，然后在浏览器中输入 localhost :8081/hello ，就可以看到返回的内容是 javabetter.cn ，说明我
们的自定义 Starter 已经成功工作了。

No. 1531180




## 第 154 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

和 > CO G@O Ilocalhost:8081/hello

下 技术派 “党 二哥的Java进阶之路(CC) 知识星球1

javabetter.cn

Spring Boot Starter 的原理了解吗?

Starter 的核心思想是把相关的依赖打包在一起，让开发者只需要引入一个 starter 依赖，就能获得完整的功能模
块。

当我们在 pom.xml 中引入一个 starter 时，Maven 就会自动解析这个 starter 的依赖村，把所有需要的jar 包都下
载下来。

每个 starter 都会包含对应的自动配置类，这些配置类通过条件注解来判断是否应该生效。比如当我们引入了
spring-boot-starter-web ，它会自动配置 Spring MVC、内炭的 Tomcat 服务器等。

spring.factories 文件是 Spring Boot 自动装配的核心，它位于每个 starter 的 METRA-INF 目录下。这个文件列出
了所有的自动配置类，Spring Boot 在启动时会读取这个文件，加载对应的配置类。

org.springframework.boot.autoconfigure.EnableRutoConfiguration=\
com.example.demo.autoconfigure.DemoRutoConfigurationyv\
com.example.demo.autoconfigure.RnotherRutoconfiguration

1. Java 面试指南 (付费) 收录的字节跳动面经同学 1 java 后端技术一面面试原题: 你封装过 springboot
Starter 吗?
2. Java 面试指南 (付费) 收录的腾讯云智面经同学 20 二面面试原题: Spring Boot Starter 的原理了解
吗?
3. java 面试指南 (付费) 收录的快手同学 4 一面原题: 为什么使用SpringBoot? SpringBoot自动装配的
原理及流程? @lmport的作用? 如果想让SpringBoot对自定义的jar包进行自动配置的话，需要怎么
做?
memo: 2025年7 月 22 日修改至此，今天有球友在 VIP 群时聊天，发现两个人都在小红书，有缘分的很，那能
去小红书实习，基本上秋招就算是稳如老狗了仿，这家独角兽的实习含金量还是非常高的。

No. 154 1180




## 第 155 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

二哥VIP 11群 (447) (CC                               ooo
锡- 沉默王二-二哥: 重要通知: 面渣..，。” 共2条

加                                                                          从 17 条新消息

高学历的人太多了

“有是 ! 一个本硕都是清北，一个清本南洋理工的硕士

xhs第一天实习，和一个非开发岗位复旦本科生
交流，一问已经实习了数不清多少段了刨

他说在券商实习都不发工资

有

我也在 xhs

一上: xhs第一天实习，和一个非开发岗位复旦本科生交
流，一问已经实习了数不清多少段了蚀

36.愉Spring Boot 启动原理了解吗?

Spring Boot 的启动主要围绕两个核心展开，一个是 espringBootapplication 注解，一个是
Springapplication.run() 方法。

No. 1551180




## 第 156 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

黄色区域: 为实例化加载区域        口 | 于
红色区域: 为run方法执行区域       和
| 加可所有可用初好化
第二步         半
ETY 7 new sprngAppllcatlon0)    Ha闻| inir加和    |
第步
L__ | 坟时所有采用和和
2 实例对象.rum
有         和训       失果并设置win方法     getspringFactoresins
headleaa            [一~
属性设轩
要配环顶要了              step2 |    补给化攻折可                   acroriesInstances
DefaultApplicationArgus |中一一step4一    ep:       getRunListeners (args)           底层依旧采用     l
pl
              ap    ep3                  通过糯加载各获取
8 factories文
|     2                   打印banner
图案
创建配置环境     3
web/atandard                           FT
由              的鉴折拓
加载属性资源           上下文区域  司
ap61
L    根据类型创建
hepe               veb/standard上下文
了
准备上下文愉
本            op                芝| 。 党报告右                .底层依旧采用factoriesInstances
时         1    站              证| es |
bean工 《通过工厂 《刷新生                      和一
厂加载    生产Bean    命周期
environment     altialize初纺
环境设置       二设量汪打展      查源蓝取并load
上下文后时结束处理
7                                   芝| 。 afterRefresh
ap
                        | 交布应用上下
文启完成    |
aap12
         ET

我先说一下 aspringBootApplication 注解，它是一个组合注解，包含了 espringBootCconfiguration 、
eEnableautoconfiguration 和 ecomponentscan ，这三个注解的作用分别是:

espringBootConfiguration : 标记这个类是一个 Spring Boot 配置类，相当于一个 Spring 配置文件。

egnableRutoconfiguration : 告诉 Spring Boot 可以进行自动配置。比如说，项目引入了 Spring MVC 的

依赖，那么 Spring Boot 就会自动配置 DispatcherServlet、HandlerMapping 等组件。

No. 1561180

acomponentscan : 扫描当前包及其子包下的组件，注册为 Bean。




## 第 157 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

”SmartPaiApplication.java x   J SpringApplication.class     襄

zhaoqi 》 smartpai 》 台 SmartPaiApplicationjava 》 Language Support for Java(TM) by

package com.yizhaoqi.smartpai;

import org.springframework.boot.SpringAppLication;
import org.springframework.boot.autoconfigure.SpringBootAppLication;

QSspringBootAppLication
pubLic cLass SmartPaiAppLication

Rur    9
pubtLic static void    (String[]
SpringAppLication.   (primarySo    :SmartPaiAppLication.cLass，    );

好，接下来我再说一下 Springapplication.run() 方法，它是 Spring Boot 项目的启动入口，内部流程大致可
以分为 5 个步骤:

人中、创建 SpringApplication 实例，并识别应用类型，比如说是标准的 Servlet Web 还是响应式的 WebFlux，人然后
准备监听器和初始化监听容器。

创建并准备 ApplicationContext，将主类作为配置源进行加载。
刷新 Spring 上下文，触发 Bean 的实例化，比如说扫描并注册 ecomponentscan 指定路径下的 Bean 。

余、触发自动配置，在 Spring Boot 2.7 及之前是通过 spring.factories 加载的，3.x 是通过读取
Rutoconfiguration.imports ，并结合 econditionalon 系列注解依据条件注册 Bean 。

如果引入了 Web 相关依赖，会创建并启动 Tomcat 容器，完成 HTTP 端口监听。

关键的代码逻辑如下:

public ConfigurableApplicationContext   (String..。 args) {

// 1. 创建启动时的监听器并触发启动事件

SpringapplicationRunListeners listeners = getRunListeners(args) 7

listeners .starting() 17

// 2. 准备运行环境
ConfigurableEnvironment environment = prepareEnvironment(1isteners))

configureIgnoreBeanInfo(environment) 7

// 3. 创建上下文

ConfigurableRpplicationContext context = createRpplicationContext();
try {
// 4. 准备上下文

PrepareContext (Context，environment，1isteners，args);

No. 1571180




## 第 158 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

// 5. 刷新上下文，完成 Bean 初始化和装配

refreshContext (Context) 7

// 56. 调用运行器
afterRefresh(context，args) 7

// 7. 触发启动完成事件

listeners.started(context) 7
} catch (Exception ex) {
handleRunFailure(context，ex，1isteners))

return context1

为什么 Spring Boot 在启动的时候能够找到 main 方法上的@SspringBootApplication 注
解?

其实 Spring Boot 并不是自己找到 aspringBootapplication 注解的，而是我们通过程序告诉它的。

espringBootRApPPlication
Public class MYRPPlication {
public static void main(String[] args) {
Springapplication.run(MYRPPlication.class，args) 7

我们把 Application.class 作为参数传给了 run 方法。这个 Application 类标注了 espringBootapplication
注解，用来告诉 Spring Boot: 请用这个类作为配置类来启动。

然后，SpringApplication 在运行时就会把这个类注册到 Spring 容器中。
Spring Boot 默认的包扫描路径是什么?

Spring Boot 默认的包扫描路径是主类所在的包及其子包。

比如说在技术派实战项目中，启动类 ouickForumapplication 所在的包是

com.github.paicoding.forum.web ，那么 Spring Boot 默认会扫描 com.github.paicoding.forum.web 包及

其子包下的所有组件。

No. 158 1180




## 第 159 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

paicoding - QuickForumApplication java [paicoding-web
paicoding 》forum    QuickForumApplicaton 。 旺-    RN   Example    ce-         eht     GobaQg@g

日poject ~  龟    ntHashMapjava X 人 CatalogEntyjava x 人 Aionicntegerjava x 全 Unsafeal   kroumwpplcatonjavs x

paicoding [paicoding-forum]
肥 .github

astf人

BEnabteAsync
coding-api                    BEnabtescheduting
coding-core                   BEnabteCaching
Coding-service                  aservLetComponentScan

coding-ui                                       :
[ER                    柜pringBootApptication|

ET

四                        入 pubiic class                    implements WebMvcConfigurer，
有 main                       aaLue("8080' )
private       webPort

n.github.paicoding.forum

BResource
四 component             private             gLobatviewInterceptor
加config
aoverride
四global                  Public void addInterceptors(               registry) {f
mn                       registry.          (gLobatviewInterceptor) .

说QuickForumApplication             了
aoverride

public void configureHandterExceptionResotvers(List<HandLerExcept
resoLvers .add(     ，mew ForumExceptionHandter())

和

public static void main(     [] args) {

所Buid

1.                        收录的滴滴同学 2 技术二面的原题: 为什么 Spring Boot 启动时能找到 Main 类
上面的注解

2.                          收录的腾讯面经同学 22 暑期实习一面面试原题: Spring Boot 默认的包扫描路
径?

3                        收录的微众银行同学 1 Java 后端一面的原题: @SspringBootApplication 注解了
解吗?

4.                        收录的国企零碎面经同学 9 面试原题: Springboot的工作原理?

5.                  收录的京东面经同学 5 java 后端技术一面面试原题: SpringBoot启动流程 (忘
了)

6.                         收录的哗哩哗哩同学 1 二面面试原题: springBoot启动机制，启动之后做了哪

memo: 2025年8 月 10 日修改至此，今天在        的时候，很感动，因为有球友说，他给周围很多人安
利了二哥的编程星球，并且反向很不错。真的很感谢，球友们的口碑，没有大家，真走不到现在。

No. 1591180




## 第 160 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

附 件: 1个(圈 LU8重-]ava后端开发.pdf ) 查看附件

二哥好:

时隔三个月才来得及继续搞这个简历，中间因为老师让准备AAAI耽搁了。
针对您第一次提出的问题做了初步的修改，这段时间也找到了第二个实习
算后续慢慢接着补充。

另外这个实习主管和我说让我写一个软著或者专利，以便后续转正，但他;
18w-25w之间，大概是15k*14往上，在合肥这个薪资我个人觉得还算可必
有点想冲一下，所以问一下二哥您的建议。

祝二哥生活顺利，越长越帅!

已经跟周围很多人安利二哥的项目了，反响很不错!

37.说一下 SpringBoot 和 SpringMVc 的区别? (补充)

2024年 04 月 04 日增补

SpringMVC 是 Spring 的一个模块，专门用来做 Web 开发，处理 HTTP 请求和响应。而Spring Boot 的目标是简化
Spring 应用的开发过程，可以通过 starter 的方式快速集成 SpringMVC。

传统的 Web 项目通常需要手动配置很多东西，比如 Dispatcherservlet、ViewResolver、HandlerMapping 等
等。而 Spring Boot 则通过自动装配的方式，帮我们省去了这些繁琐的配置。

Spring Boot 还内置了一个嵌入式的 Servlet 容器，比如 Tomcat，这样我们就不需要像传统的 Web 项目那样需要
配置Tomcat 容器，然后导出 war 包再运行。只需要打包成一个JAR 文件，就可以直接通过 java -jar 命令运
行。
1. Java 面试指南 (付费) 收录的滴滴同学 2 技术二面的原题: SpringBoot 和 SpringMVC 的区别
2. Java 面试指南 (付费) 收录的京东面经同学 5 java 后端技术一面面试原题: SpringBoot与SpringMVC
区别

38.Spring Boot 和 Spring 有什么区别? (补充)

2024年 07 月 09 日新增

从定位上来说，Spring 是一个完整的应用开发框架，提供了 locC 容器、AOP 等各种功能模块。Spring Boot 不是
一个独立的框架，而是基于 Spring 框架的脚手架，它的目标是让 Spring 应用的开发和部署变得简单高效。

Spring 项目需要我们手动管理每个 jar 包的版本，经常会遇到版本冲突的问题。比如我们要用 Spring MVC，需要
引入 spring-webmvc、jackson-databind、hibernate-validator 等一堆依赖，还要确保版本兼容。Spring Boot

通过 starter 机制解决了这个问题，只需要引入 spring-boot-starter-web 这一个依赖就可以了，它包含了所有相
关的 jar 包，而且版本都是测试过的，可以兼容的。

No. 1601180




## 第 161 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆袭

1. java 面试指南 (付费) 收录的小米同学 F 面试原题: Spring Boot 和 Spring 的区别
2. java 面试指南(付费) 收录的 OPPO 面经同学 1 面试原题: 说一下Spring和Springboot之间有什么差

异?

memo: 2025年8 月11 日修改至此，今天有球友在 VIP 群里交流说，用二哥的项目，轻松过大厂的简历初得，
包括小米和美团。

二哥VIP 11群(448) (必                             ”

坪- 沉默王二- 二哥: 派聪.。 共3条                      &

一   昌                                               入 115条新消息

吃:业 闸由大佬简历写的啥项目呀

对的，题目我都发上面了，你可以翻一
下

1 lsau : 听说美团第一道题让用 ai来编程

就二哥的项目
小米的题有点变态
Spring Cloud

39.对 SpringCloud 了解多少?

Spring Cloud 其实是一套基于 Spring Boot 的微服务全家桶，帮有我们把分布式系统里的基础设施做了一个"拿来即
用"的封装，比如服务注册与发现、配置管理、负载均衡、熔断限流、链路追踪这些。

我自己用得比较多的是 Spring Cloud Alibaba 这一套，PmHub 这个项目就是一个例子，比如:

No. 1611180




## 第 162 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

。 我们使用 Nacos 做服务注册和配置中心，并且将配置信息持久化到了 MySQL 中，这样就可以统一管理注册
信息和配置信息，还支持动态刷新配置。

。 使用 Gateway 做 AP 网关，支持路由转发、全局过滤器、限流等功能。

。 使用 Sentinel 做熔断、限流、降级策略，结合业务自定义规则比较方便。

。 使用OpenFeign 做服务间的声明式调用，比 RestTemplate 更省代码，也更清晰可维护。
。 使用 Seata 处理分布式事务，这个在订单支付、审批流场景中用得比较多。

站和

1                            1

总                   去

1                            1

1                            1
\---------------:

-- 】-一、 Lvstkeepalived+Nginx
;        LVs-Keepalived       负役的人全玫

1 1    伟 传     APl Gateway 集群               l

中

1

中

1

1                                     (Spring Cloud Gateway)          1
  Node2   1 =-----------T-------- “
1        |     Dubbo负载均衡Sentine|限流过新降级    OAuth2树一举录打。 seat  三
中

1      |

   、

1

-一一一 玫-~------且------                旦__             权(Spring cloud                  直人
Security)

目目目

ELK ELK ELK
日志采集分析集群

目 效

1              1    1                  1    1               1
              |                  |
1    1                      1
1              1    1                  1    1               1
              1    1                  1    1               1
    1    1 全       布式任务调度 上
1 Mysql    Redis集群。 1                  1    1分布式文件丰储分布式任务调度 1
1              1    1   Grafana    SkyWalking    1    1               1
              |
1    1                      1
|              |                  |         浴太 ，
1   Zabbix    prometheus
1 TipB集群。 Elasticsearch集群                           1      上分布式全局ID生成 RocketMq集群  1
1              孝所存储              K8S 服务监控和保护                  1                  基础服务                  1
上                                   1                   上

我觉得 Spring Cloud 最大的价值是统一了技术栈和编程模型，不需要我们去自己从零实现注册中心、熔断器这些
基础设施。

什么是微服务?

No. 1621180




## 第 163 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

微服务就是把一个大的、复杂的单体应用，拆成一个个围绕业务功能独立部署的小服务，每个服务维护自己的数据
和罗辑，服务之间通过轻量级的通信机制 (比如 gRPC) 来协作。

Springcloud

7                              下          ”

将

wereaormem

微服务的核心价值我认为是: 业务之间的边界更清晰了，不同团队可以独立开发、部署、扩展某个功能，不会因为
一个小的改动就要把整套系统重新上线。

像PmHub 这个项目 就是从单体拆分成微服务的，包括启动网关、认证、流程、项目管理、代码生成等多个服
务。

No. 1631180




## 第 164 页


-让天下所有的面渣都能逆袭

PmHub 系统架构图

前端架构

多

1. Java 面试指南    《录的比   同学 1 面试

memo: 2025年8月1     至此，今天帮球友修改简历的时候，碰到一个天       哥对我简历的修
，觉得自己做的事情确实有意义

No. 1641180





## 第 165 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

二哥晚上好，谢谢您春招时对我简历的修改，没有二哥我绝对进不了字节。

补充
40.SpringTask 了解吗?

SpringTask 是 Spring 框架提供的一个轻量级的任务调度框架，它允许我们开发者通过简单的注解来配置和管理定
时任务。

使用起来也非常方便，首先使用 egnablescheduling 开启定时任务的支持。

paicoding - QuickForumApplicationjava [paicodin

ng-web ) sre ) main ) ia    github   县-

DG-                 QQ@o5交Q@人
从 一，护ouickroumApplicationjaa x 人守

回 project ~                   四

pringBootApplicationjava x 《vv

时 Project

名admin

packase
国common

名 component                       import
器 config

BSLf人4

DaEnabLeAsync

DEnabLeScheduLing

证nabteCaching

DSservLetComponentScan

BSpringBootAppLication

public class
DayValLue("8080")

中sprng 国Teminal 三TOD0 人Buid

implements WebMvcCo吕

然后在需要定时任务的方法上加上 escheduled 注解，支持 fixedRate、fixedDelay 和 cron 表达式。
中，就使用过 cron 表达式在每天凌晨定时刷新文章的 sitemap 。

escheduled(cron = "0 15 5 * * ?")
public void             () {

log.info( "开始刷新sitemap.xml的ur1地址，避免出现数据不一致问题!" ) ;

refreshSitemap())
log.info( "刷新完成! ") ;

No. 1651180




## 第 166 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

用SpringTask资源占用太高，有什么其他的方式解决? (补充)
2024年05月27日新增
首先我们需要分析一下 SpringTask 资源占用高的原因。

默认情况下，SpringTask 会使用单线程执行所有定时任务，如果某个任务执行时间长或者任务数量多，就会造成
阻塞。而且它是基于内存的，所有任务信息都保存在JVM 中，应用重启后任务状态就丢失了 。

那我们可以通过配置线程池来解决这个问题。

econfiguration
egnablescheduling
public class Scheduleconfig implements SchedulingConfigurer {
aoverride
public void configureTasks(ScheduledTaskRegistrar taskRegistrar) {
taskRegistrar.setScheduler(Executors.newScheduledThreadPool(10));

】}

另外，就是可以将 SpringTask 迁移到其他的任务调度框架，比如 Quartz、XXLJOB 等。

Quartz 功能更强大，支持集群、持久化、灵活的调度策略。还可以把任务信息持久化到数据库，支持集群部署，
一个节点挂了其他节点可以接管任务。

使用 XXL-JOB 是分布式场景下更彻底的解决方案，有独立的调度中心，任务配置和执行可以分离; 支持分片执行，
大任务可以拆分成多个子任务并行处理。

As
* 2、分片广播任务
/

exxlJob("shardingJobHandler")

public void shardingJobHandler() throws Exception {
// 分片参数

int shardIndex

com.xx1.job.core.context.XxlJobHelper.getShardIndex();

int shardTotal

com.xx1.job.core.context.XxlJobHelper.getShardTotal();

logger.info( "分片广播任务开始执行，当前分片序号 = {} ，总分片数 = {}"，shardIndex，
shardTotal)

// 业务逻辑处理，根据分片参数处理不同的数据
for (int 1 = shardIndex; 1i < 100;) 1 += shardTotal) {
logger.info("第{}片，处理数据: {}"，shardIndex，i) 7

// 模拟处理数据的时间

TimeUnit.MILLISECONDS .sleep(100)7
}

logger.info( "分片广播任务执行完成") 7

1. java 面试指南 (付费) 收录的微众银行同学 1 Java 后端一面的原题: SpringTask 了解吗?

No. 1661180




## 第 167 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

2. java 面试指南 (付费) 收录的阿里面经同学 1 闲鱼后端一面的原题: 订单超时，用springtask资源占用
太高，有什么其他的方式解决?

memo: 2025年 8 月16 日修改至此，今天帮球友修改简历的时候，碰到一个球友说: 暑期实习的时候使用了技
本派，也找二哥修改了简历，最后拿到了哈吧的实习，非常感谢。那说实话每次碰到球友这样的反馈，都挺开心
的。

麻烦二哥简历修改-~星球号mW 35 门户 @〇 于 。 外安全浏览模式~                                       精简信息
发件人: 生 加amalpihis@126.com> 十
收件人   人 我<www.qing_gee@163.com> 十

时 间: 2025年08月15日 15:51 (星期五)
附 件: 1个( 国 4让-东南大学硕士应届_后端开发.pdf ) 查看附件

二哥好，之前暑期实习的时候用了技术派也找您修改了简历，拿到哈另实习了，非常感谢! 现在又到秋招了，加了实习经
态，把新的rag项目也加上去了，麻烦您再看看有没有需要修改的地方呀。顺便关于rag的项目想问您一下，如果面试官问道
为什么不用langchain4j或者spring ai去实现，要怎么答好呢?

非常感谢二哥!

41.Spring Cache 了解吗?

Spring Cache 是 Spring 框架提供的一套缓存抽象，它通过提供统一的接口来支持多种缓存实现，如 Redis、
Caffeine 等。

No. 1671180




## 第 168 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

6象rvice

pubLic cLass UserService |

Q@Resource
private UserDao UserDao;

Q@CcacheabLe(vaLue =         ，Kkey = "所serId")
pubtLic UserInfoD0         (Long userId) {

return UserDao.getByUserId(userId) ;

G@CachePut(vaLue =         ，Kkey = "大Sser.id")
pubLic booLean        (UserInfoD0 user) {
return UserDao.updateById(user) ;

Q@CacheEvict(vaLue =         ，key = "所serId'")
pubLic void         (Long userId)] {
UserDao.removeById(userId) ;

我们只需要在方法上加几个注解，Spring 就会自动处理缓存的存取，这种声明式的缓存使用方式让业务代码和缓
存遇辑能够完全分离。

最常用的注解是 ecacheable ，用来标识方法的返回值需要被缓存。

ecacheable(value                 ，key             )

Public User getUserById(Long id) {
return userDao.findById(id) 7

)}

方法在第一次执行后会把结果缓存起来，后续的调用就直接从缓存中返回，不再执行方法体。
还有 ecachegvict 注解，用于在方法执行前或执行后清除缓存。

No. 1681180




## 第 169 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

ecacheEvict(value = "users'"，key = “"##id")
public void deleteUserById(Long id) {
userDao.deleteById(id) ;

Spring Cache 是基于 AOP 实现的，通过拦截方法调用，在调用前后插入缓存远辑。需要我们在配置中先启用缓存
功能。

econfiguration
egnablecaching
public class Cacheconfig {
eBean
public CacheManager cacheManager() {
RedisCacheManager.Builder builder =- RedisCacheManager
.RedisCacheManagerBuilder
.fromConnectionFactory(redisConnectionFactory())
.cacheDefaults(cacheconfiguration());
return builder.build();

Spring Cache 和 Redis 有什么区别?

Spring Cache 和 Redis 的区别其实是抽象层和具体实现的区别。Spring Cache 只是提供了一套统一的接口和注解
来管理缓存，本身并不提供缓存能力，而 Redis 是具体的缓存实现。

在使用层面上，Spring Cache 更简单，只需要在方法上添加注解就行，框架会帮有我们自动处理。

ecacheable("users")
Public User getUser(Long id) {
return userDao.findById(id) 7

如果用 Redis 则需要我们手动处理缓存逻辑:

Public User getUser(Long id) {

String key = "user:" + idy
User user = (User) redisTemplate.opsForValue().get(key) 1;
if (user == nul1l) {

user = userDao.findById(id);
redisTemplate.opsForValue() .set(key，user，30，TimeUnit .MINUTES ) 7

】}

return user)

在实际的项目当中，我通常会选择使用 Spring Cache 来处理一些简单的缓存业务，但对于一些复杂的业务场景，
对于复杂的业务逻辑，比如分布式锁、计数器、排行榜等，我会直接用 Redis。

有了 Redis 为什么还需要 Spring Cache?

No. 1691180




## 第 170 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

虽然 Redis 非常强大，但 Spring Cache 可以简化缓存的管理。我们直接在方法上加注解就能实现缓存逻辑，减少
了手动操作 Redis 的代码量。

ecacheable("users")
Public User getUser(Long id) {
return userDao.findById(id) 7

)}

此外，Spring Cache 还能灵活切换底层的缓存实现，比如说从 Redis 切换到 Caffeine。
说说 Spring Cache 的底层原理?

Spring Cache 的底层是通过 AOP 实现的。当我们在方法上标注了 ecacheable 注解时，Spring 会在项目启动的
时候扫描这些注解，并创建代理对象。代理对象会拦截所有的方法调用，在方法执行前后插入缓存相关的逻辑。

Spring-bootstartercache                     spring-context-support
-3
CaffeineCacheManager    caffeinecache |]
Spring-bootrautoconfigure
可       <
攻    |
本 二     1 conditionalonMissingBean                  |
;   -Conditiona    9                     hp
Cachecondition    SimpleCachecConfiguration               Spring-context         |
-vv
CacheManager       Cache
CacheConfigurationc| 人-党|
1十寸conamentMapcachewanager | | concurentvapcache
Conditionalonclass              -3
com_github.ben-manescaffeine/caffeine
Cache          Caffeine       @Cacheable  加EnableCaching  人@Cacheput

具体的执行流程是这样的:
当用户调用一个被缓存注解标注的方法时，实际上调用的是代理对象而不是原始对象。

代理对象中的 Cachelnterceptor 拦截器会先解析方法上的缓存注解，获取缓存名称、key 生成规则、过期时间这
些配置信息。然后根据注解的类型执行不同的缓存策略，比如ecacheable 会先去缓存中查找数据，如果找到就
直接返回，不执行原方法; 如果没找到，就执行原方法获取结果，然后将结果存入缓存再返回。

缓存 key 的生成是通过 KeyGenerator 组件完成的，默认情况下会根据方法的参数来生成 key。如果我们在注解中
指定了 key 属性，Spring 会使用 SpEL 表达式引擎来解析这个表达式，结合方法参数、返回值等上下文信息计算出
具体的 key 值。

底层的缓存存储是通过 CacheManager 和 Cache 这两个抽象接口来管理的。CacheManager 负责管理多个缓存区
域，每个 Cache 实例对应一个具体的缓存区域。

不管我们使用 Redis、Caffeine 还是其他缓存技术，都需要实现这两个接口。这样 Spring Cache 就能以统一的方
式操作不同的缓存实现，实现了很好的解耦。

No. 1701180




## 第 171 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

1. Java 面试指南 (付费) 收录的美团同学 9 一面面试原题: 介绍一下springcache 和redis? Spring
cache和redis之间的各应用在什么场景? 有了redis为什么还要用springcahe? springcache 底层原理，
基于什么实现的?

memo: 今天在给球友们修改简历的时候，有球友说，找实习的时候也找二哥修改了简历，最后也顺利找到了，我
很喜欢这种反馈，说明我付出的心血是有回报的，也感谢同学们每一次的口碑。
简历修改，二哥帮忙看看，非常感谢，我的星球编号是WasLL 门户 〇 虽 外安全浏览
发件人:| 轩r 莉1-  icom> +

收件人: 人 163.com> 十

时 间: 2025年08月16日 17:31 (星期六)
附 件: 1个(加 测开.pdf ) 查看附件

hello 二哥,
上次也麻烦你帮有我看了找实习的简历，也是顺利找到了实习一
眼看秋招已经开始，打算最近离职了，更新了一版简历，麻烦二哥帮有我看看。

整整两个月，面渣逆袭 Spring 篇第二版终于整理完了，这一版几乎可以说是重写了，每天耗费了大量的精力在上
面，可以说是改头换面，有一种士别俩月，当刮目相看的感觉 (从 1.3 万字暴涨到 3.4 万字，加餐的同时区分高频
低频版) 。

No. 1711180




## 第 172 页


面渣逆效Spring篇V2-让天下所有的面渣都能逆效

@e@                                     名

Apple Books
加 主页

书库                           2
员 人和                       面洼逆|获          面酒逆|绑
@ 鲍读清单                  Spring篇      Java基础篇

加 已读完
加 图书

人有声书

外 PDF

目 我的试恋版

_辐因阳图
JVM篇

三分恶|沉默王二修订版

_回四轿国
集合框架篇

三分恶|沉默王二修订版

三分恶|沉默王二修订版              三分恶|沉默王二修订版

我的藏书
十 新建藏书

_回本四图
MySQL篇

三分恶|沉默王二修订版

_回四昌国
Redis篇

三分恶|沉默王二修订版

并发编程篇

三分恶|沉默王二修订版

加mm     是    本

网上的八股其实不少，有些还是付费的，我觉得是一件好事，可以给大家提供更多的选择，但面渣逆袭的含金量懂
的都懂。

No. 172 1180




## 第 173 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

E 。 面沽逆袭RocketMQ篇.pdf                             5M
    面渣逆效并发编程篇V2.0.pdf                          26.4M      日             9       加

    面济逆装计算机网络.pdf                               79M
    面渣逆袭集合框架篇V2.1.pdf                          13.1M

    面酒逆装-分布式篇.pdf                            19M
    面渣逆效Redis篇V2.0.pdf                             68.5M

    面济地交操作系统.pdf                             3.3M
    面洁逆袭Java基础篇V2.1.pdf                          118M

    面淹逆获 MyBatis.pdf                             3.2M
     面潮逆袭 JVM篇 V2.1.pdf                               16M    和                             本

面淹逆约MySQL篇V2.2.pdf                                53.6M    二哥的 Java 进阶之路亮白版.pdf                       345M

二哥VIP12 群 (135)

者 沉默王二: 重要通知: 面渣了逆袭 Red..，”移除

没学过操作系统和计算机网络

轧。 面过几次八股全中

怎么办

赞同，面过几次全包含

面渣逆袭第二版是在星球嘉宾三分恶的初版基础上，加入了二哥自己的思考，加入了 1000 多份真实面经之后的结
果，并且从 24 届到 25 届，再到 26 届，帮助了很多小伙伴。未来的 27、28 届，也将因此受益，从而拿到心仪的

offer。

能帮助到大家，我很欣慰，并且在重制面渣逆袭的过程中，我也成长了很多，很多薄弱的基础环节都得到了加强，
因此第二版的面渣逆袭不只是给大家的礼物，也是我在技术上昱变的记录。

No. 173 1180




## 第 174 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

好滴!

谢谢二哥

我把你推荐给我们实验室的基本所有人了

他们的反馈都是八股看面渣

包稳的哈!

No. 1741180

Fa




## 第 175 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

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

No. 1751180




## 第 176 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

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

No. 1761180




## 第 177 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

当然了，请允许我的一点点私心，那就是星球的 PDF 版本会比公众号早一个月时间，上毕竟星球用户都付费过了，
我有必要让他们先享受到一点点福利。相信大家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
等等都是需要成本的。

更别说我付出的时间和精力了，大家觉得有帮助还请给个口碑，让你身边的同事、同学都能受益到。

No. 1771180




## 第 178 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

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

No. 1781180




## 第 179 页


图文详解 41 道 Spring 面试高频题，这次吊打面试官，我

面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

面渣逆贰Spring篇V2.0

=
aa

Spring 循环信球一|
什么要有3 级

二扫基二纯么?

ean 生人出行得
Bean 生命周期-扩大方注

mu

人和是 AP

Spring 源码解析

Spring AOP 一 op FaR查

[1
am

Spring 事务 “| 事工人和
mw
cr

Spring oc -| oc ma
nm

看源码的时候发现 Spring 用了很多设计模式，比
如工厂模式、单例模式、模板方法模式等等，这对我
平时写代码也很有启发。

还有就是 Spring 的 Bean 生命周期，从 BeanDefi-
mition 的创建到 Bean 的实例化、属性注入、初始化
回调，再到最后的销毁，整个过程还是挺复杂的。看
了源码之后对 ePostConstruct、@PreDestroy
这些注解的执行时机就更清楚了。

不过说实话，Spring 的源码确实比较难哨，涉及

作者: 三分恶，戳原文链接。
没有从么使我信留一一由了户的，幼伏央六有政确、有绽戎、有宁静的溢涯，我是不系之肯。
系列内容:

e

昌

昌

面渣逆袭Java SE 篇 】

面潮逆化Java 集合框如篇 虽
面渣逆效Java 并发编程篇 唾
面渣逆次JVM 篇吨
面渣逆效 Spring入吨

面淹逆获 Redis 篇只

面渣逆区 MyBatis 篇 是
面潮逆次 MySQL复 吨

画渣逆歼操作系统篇 虽
面法逆效计算机网络篇
面渣逆获 RocketMQ 复哗
面渣逆获分布式简吓

的概念和技术点太多了。我一般是结合一些技术博客
和 Claude 一起看，这样理解起来会相对容易一些。

了PS: 关于这份小册的 PDF 版本，目前只有星球的
用户可以获取，后续会考虑开放给大家。

二:一                                    二

二而拯，之前在技术关上和要件写了一本《Spring 浊折手胡) 之前的入拉夫
他训后志和基识旺球中，但我在王球中还没有找到，请各明在到星球中了区-

GOsCenEGeG172

人     这个: 愉GO ItpejlpanbaiaucomartmaltaWgPohaD

rpo_ 后

1 Ja 历试将让 〈付珊) 收录的京东面经局
学5 Jara 后问花术一面面试厦题: IOC与
4OP

memo: 2025年6月15 日修改至此，今天在帮球
友们修改简历的时候，碰到一个中山大学本硕的球
友,， 校园荣誉基本上拉满了，非常优秀，那我也希望
能够帮助到更多的球友们，帮他们拿到更好的

offer。

中山大学“国末
ar
荣光，世芝几了 FF中大学全研究生区 一等
中山大学
FI Pa: 了
和交大- 已-1 UP中由学人于大学生区学人 等
1    刘全一“次。 直下3大学生于横 -国家二等交省
1 1 Li 下全国大学生学机 - 三东和二等交

:RCI
区

alt 月

ie                      7列

10

觉得稳了 (手动 dog) 。整理: 沉默王二，玲转载链接，

No. 179 1180




## 第 180 页


面渣逆袭Spring篇V2-让天下所有的面渣都能逆效

。 面渣逆袭设计模式入中
。 面渣逆区 Linux 篇中

No. 1801180



