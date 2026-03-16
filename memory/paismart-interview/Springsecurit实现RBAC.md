# Springsecurit实现RBAC

> 来源：Springsecurit实现RBAC.pdf

> 解析时间：2026-03-14 16:28:23

> 本文档由 OCR 识别生成，可能存在少量识别错误


---


## 文档信息


- **总页数**: 11

- **文件大小**: 13.78 MB


---


## 第 1 页


加如何基于Spring Security实现派聪明 RAG 知识库的RBAC 权限系统?

RBAC，全称为 Role-Based Access Control，翻译过来叫基于角色|

问控制，通过将用户分配到不同的角色，并为角色分配权限，从而实现对资源的访问控制。

用P1  、                                                                              权限1

用P2                                - 角b1  -                                    权限2

用户3                                       -角色2  -                                    权限3                                       吕
吧

用户4                                       -角色3                                          权限4

用户5                                                                                       、 权限5

那如何实现 RBAC 呢? 派联明用的是 Spring Securigy。Spring Security 本质上是一个基于 filter 的安全框架。当请求进入应用时，会经过一系列安全过小器链，每
个过泡器负责不同的安全功能，比如认证、授权、CSRF 防护等-

SecurityFilterChain

FilterChainProxy'

Figure 4. SecurityFilterChain

Spring Security 主要解决了两大核心问题: 认证(Authentication) 和授权 (Authorization)。认证就是验证-你是谁"，比如用户登录时验证用户名密码是否正确;
授权就是验证"你能做什么'，比如检查用户是否有权限访问某个页面或调用某个接口

本篇教程将详细介绍如何基于 Spring Security 实现 RBAC，包括用户注册、登录、JWT 认证、请求拦截与授权等核心流程
一、RBAC 的核心概念

RBAC 的核心思想是给用户赂予某些角色，而每个角色拥有某些权限。等于说，一个权限可以分配给多个角色，一个角色可以拥有多个权限，同样一个用户可以分
配多个角色，一个角色也可以对应多个用户，对应模型如下所示

对干派税明来说，每个公司都有自己的组织架构，比如公司里管理知识座的人员有王老板和毕小三

、王老板不仅桐有毕小三的权限，忆拥有李四眼的权限、像这




## 第 2 页


种管理关系向下兼容的模式就需要用到角色继承的 RBAC 模型。角色继承的 RBAC 模型的思路是上层角色继承下层角色的所有权限，并且可以额外拥有其他权限。

” 。 在派陪明系统中，Spring Security 的 RBAC 实现分为几个层次:

基础角色的定义:

，。 USER (普通用户) : 可以上传文件、进行对话、查看自己的历史记录
，。 ADMIN (管理员) : 除了普通用户的所有权限外，还能管理所有用户、查看系统状态、管理知识库

_URL 级别的权限控制:

java 复制代表
7 任同人才访问的接口《如王好、广册》
requestatchers( -1api/vlyeaersJregisterr，

aptvayusersyloginr)-pereatan0)

// 共通用户和管理只剖能访问的失吕
requestyatchers("1api/vHepload/ne-)-hasanyiolenusERr，-aoR)

7/ 只有管理员能访问的拉口
requestyetchers("/api/vladetn/e) .hasRoletnaoDI)

组织标签权限控制:

。 私人空间 : 以"PRIVATE -开头的资源，只有创建者能访问
，* 组织资源 : 根据用户的组织标签来控制访问权限
。 公开资源 : 所有认证用户都能访问

， 二、派陪明中权限控制的代码结构

派聪明的 Spring Security RBAC 实现采用了非常清晰的分层架构设计，每个层次都有明确的职责分工。

cy
蕊cv
| java/cem/yizhaoqi/smartpai/

伙cr       BE
| 上 SecurityConfig.java
1 F otherttcationfinear ja

上 cenerolen/           ， 控订
| 上 wearcantroller jam
上 servdcey             务必

| 上 werservtce.java
| 上 ceskoslsergetatlsservice -ja

上 repesttory/           * 台所访问导
| 上 wsereposttory ,java

上 moaey               由拓模|
本

上 wansy                二工R

| 上 passueraudljam
| 上 eudasae
上 resowrcesy

| applicarionyml 。。。 * 配因文件
tesey
上 javaycenyyiahaoaiysmartpaay
上servicey             二 测庆

上 wserservicerescjav

配置层 《config) 是整个安全框架的大脑"，负责制定游戏规则。SecurityConfigjava 相当于安全系统的总指挥，定义了哪些 URL 需要什么权限，配置过滤器链的执，
行顺序。JwtAuthenticationFikterjava 则像门卫一样，检查每个请求的身份证 (WT 令牌) 是否有效。




## 第 3 页


控制器层 《controller) 是用户请求的第一站，负责接收和响应。UserControllerjava 处理用户相关的所有操作，如登录、注册、获取用户信息等，是用户与系统交
互的入口。

服务层 (service) 是业务逻辑的核心，负责具体的业务处理。UserServicejava 处理用户相关的业务逻辑，比如用户注册时的数据验证、密码加密等-
CustomUserDetailsServicejava 专门为 Spring Security 服务，负责从数据库加载用户信息并转换成 Spring Security 能理解的格式。

数据访问层 (repository) 是与数据库打交道的地方。UserRepositoryjava 定义了如何从数据库中查询用户信息，使用 Spring Data JPA 简化数据库操作。

数据模型层 model) 是数据的"蓝图"'。Userjava 定义了用户实体的结构，包括用户名、密码、角色、组织标签等字段。

工具类层 (utils) 是系统的"工具箱"。PasswordUtiljava 负责密码的加密和验证，确保密码安全。JwtUtilsjava 负责 JWT 令牌的生成、解析和验证，是无状态认证的
核心o

配置文件 (resources) 中的 applicationyml 是系统的配置中心，包含数据库连接、JWT 密铀、Redis 配置等重要参数
测试层 (test)中的 UserServiceTestjava 确保业务运辑的正确性，通过单元测试验证各个功能模块。

、派聪明中权限控制的核心代码实现

01、用户模型类

User 实体类是派聪明系统实现 RBAC 权限控制的数据基础，通过JPA 注解实现完整的用户信息管理。 @Entity 和 @Table 注解将其映射到数据库的"users"表，并通
过人uniqueconstraint(columnwanes - “usernaee")在数据库层面确保用户名的唯一性，防止重复注册。

oata
Entity
Tablename =- -usersr，untqueConstraints ”BiniqueConstraint(colummllames ”rusername))
Public class User
er
5eneratedvaluefstrategy - GenerationType_IDENTITY

columntmullale - falsey unique - troe)

colemntmullable -false)

EnuneraredtEnumType-STRING)
Columntmwllable = false)

ecrearionTimestamp
Prtvare tecal0ateTise crearedhr

upaarerinestamp
privare tecal0ateTise updaredhr

peplie enum male
se am
了
)

role 字段是 RBAC 的核心，使用 @Enumerated(EnumType STRING) 将枚举值以字符趾形式存储在数据库中。内部定义的 Role 枚举包含 USER 和 ADMIN 两个角
色。Spring Security 可以轻松地将角色转换为 GrantedAuthority ，实现方法级和 URL 级的权限控制。

02、用户数据访问接口
Usernepository 提供了一个方法 findeyusernane，用于根据用户名查找用户。

uslae tnkerface Userepostrery extends paRepositorycuser， tangy {
Optionaldbsery findByUsernametString usernane);
)

03、密码工具类
Passvordutil工具类在用户注册时调用 encodel 方法对密码进行加密，在用户登录时通过 matches( 方法对密码进行验证。

upliec class pasaordudil
Private static 人inal BCryptpassvordEneeder encoder 。 new BCryptpasserdEncoder(i

uslte sratte strtng encedetstring raupassuord) 《
Treeurm ancodervencedetravpassvord)
)

uslie scatde boolesn setches(strang reupasauerd，strtng encodedpassvera) 人
erurn encoder matchestranpassvord，encodedpassvord)
)
)

BCrypt 算法的优势在于它是一种自适应哈希函数，内置了盐值 (sakt) 机制，每次加密同一个密码都会产生不同的哈希值，可以防止彩虹表攻击。同时 BCypt 算法
具有可调节的计算复杂度，能够抵御暴力破解攻击。

04、JWT 工具类

vtutils负责生成、验证和解析JWT 令牌。类中使用 Bvalue("$(jvt .secret-key}") 从配置文件读取 Base64 编码的密钥，通过 getsigningKey0 方法解码并生成
Secretkey 对象。令牌有效期设置为24小时。并使用 HS256 签名算法确保令牌的完整性-

component
public class ukbtils

privae static final String SECRET_KEY = “rest_secret_key;
prtvare startc final long BRIRATIONLTIME - 36089988; 1/ 24 hours




## 第 4 页


Clalms - Jwts'parser()-setSigntngkey(SECRET_XEY|

generateTokentString username) 方法是权限

userld)、组织标签(orgags) 和主

装的核心，它不仅将用户名作为 subject，还将权限信息封装
扣_(primaryQrg) 等。这种设计使得 JWwT 令牌成为一个自包含的权限载体，避免妥繁的数据库查询

laims 中，包括用户角色(role)、用户ID

还提供了多个 extract 方法，分别用于提取用户名、用户ID、角色、组织标签等信息。这些方法可以在 JwtAuthenticationFikter 和

orgTagAuthorizationFilter 中将令牌转换为权
数据基础

Paismart

Explorer

vY Folder

main

javaJcom/Jyizhaoqils

OrgTagCacheser
ParseServicejava
Upload
UserServicejava
VectorizationService

utils
GenerateJwtkeyjava
Jwtutilsjava
Logutilsjava
PasswordUtijava

 SmartPaiApplicationjava

es-mappings

static

application-devyml

applicationyml 。 9+,M

outline
Timeline

Java Projects

实现了 Spring Security 的 UserDetailsService 接口，负责在认证过程中加载用户详细

文。 特别是 extractOrgTagsFromToken0 和 extra

PrimaryOrgFromToken0 方法，为组织级别的权限控

 JwtAuthenticationFiterjava     台 JwtUtilsjava x

btic ct

pubti      extract0rgTagsFromToken(     tokem)
try
cuains =       parserBuitderO
.setSigningKey(getSigningKeyO)
:buitdO)
.parseCLaimsJws(token)

.getBody();

return cLaims.get
catch            ee
.error(

return

pubtic          extractPrimary0rgFromTokent:
try
ctaims =      .parserBuitder()
.setSigningKey(getSigningKe
.buitudO)
.parseCLaimsJws(toli

.getBody()7

return cLaims.get(





## 第 5 页


jw 复浊代可
罗

“实现 Spring Security 的 UnergatailsService 村口，用于加加用户的详细全息(自括用户名、密码和要项)

* 直过用户名从名所库中查找用户，并和其针执为 Spring Securlty 所的 Useroetails 相式

/
service
Public class CustonUsarbetails5ervice implemants UsargetailsService {

areuared
private Usergapositery usergepository; 1/ 用于访问用户革所

现
要所用户名加园用户主细信息，
本
overrtae
Puble Usergeratls loagusereyUsernane(String usernase) rhrovs UsernenelorfoundException ff
7// 从攻据库中查扶用户
ser wser = userReposirory -flndByUsernameusernane)
LerElseThrow(() -》nev UsernameherfoundExceprtont"User or found")i

》

1/ 适问 spring security 所虽的 Usergetails 对旬
Treeurn nen org.sprtngframevark-securttyvcore userdetatls Usert
User .gerUsername()，
User-Berpassword()，
huthertries(user-getfole() // 区取几户的和色相承

]

的
区用户的角色鱼失为 Spring Security 的机由相式。
吕
Private Collectione etends Grantedhuthoriayy Bethutheritiestser-mole rele) {

rerurn Collecrtens.stngleronttsttnew SinpleGranredhurhortry(rROLE_ ”+ rolevname()))
1

当用户烷试登录时，5pring Security 会调用loadUserByUsername 方法根据用户名查找用户信息。并将 User 实体转换为 Spring Security 标准的 UserDetails 对象，
包含三个关键信息: 用户名【usergetUsername0 )、加密密码 (usergetpassword0 ) 和权限集合(getAuthoritiestusergetRolen) )。

getAuthorities(User Role role) 方法则将用户的角色枚举转换为 Spring Security 的 GrantedAuthority 格式。通过在角色名前添加-ROLE “前缀

(押"ROLE ADMIN`、'ROLE USER-) ，使得系统能够使用 Spring Security 的方法级和 URL 级权限注解，如 @PreAuthorizefhasRolefADMIN) 和
securedCROLE UsER 。

06、JWT 认证过滤器

utauthenticationfilter继承了 OnceperRequestfiter，确保每个请求只被处理一次，负责在每个 HTTP 请求中验证JWT 令牌并设置 Spring Security 认证上下文。

ja 复和代表

定义的过天器，用于解析请求关中的 JuT Token，并妈证用户身份”

如果 Token 有让，刚将用户信息和各了设置到 Spring Security 的上下文中，后约请求可以基于用户角色进行反。
/

conponenr

Publie class uthuthenticatienfilter extends ovcepergequestFilter {

srovired
Private Jutukdls jututdlsy /1 于于生二和香析 JUT Taken

surovired
private UsergetallsServlce userOetaflsServicei // 加纺用户洋绍信息

四
* 二次请至用此方法，用于解折 JWT Token 并设置户认证俏息
局
overrian
Prerecred void daFilterTnternaltp5ervlsrRequest reqbest，Hktp5ervlsrResponse responsey FilterChain filrerchan)
hrovs ServletExeeprion， IOExceprion
>             tm
1/ 从训求关中提要 IMT Token
String taken = exeractTokentregueseyi
4 (token I- mall 上 jututtls.validateTokenttoken)) { // 验证 Token 是本有站
String username - JurUtilsvextractUlsernamefroaTokenttoken)1 1/ 从 Token 中提职用户各
erDetatls wsergeralls = wsergetails5ervice ,loadUserByUsernane人usernage); // 加钱用户详细信息

7 创建认证对象设轩到 Securtty 上下文中

sernemepassvordhuthenticationTagen authentication 。 new UsernasepassvordhuthenticationTokenf
iergerails，mull，usergerails.geturhortrles();

urhenrtcarlon.serDeratlstpew Nebhurhenttcarton0eratls5ource().butldDeratlsfrequest));

SecoratyCentextholder .BetCentext(].setauthentication人authentication);

】
) carcn (Beptton ej《

7/ 记杂得日志
aogger.error(-camnat set user authentication: (1-，
)
Derchatn.doFtlrerrequest，respense); /1 多络执行过站入
1
辣
从请束头中提职 JWT Token
吕

private String atractTekantlttpservlstfeqvast request) 人
Sering bearerTeken = request-BetHeadert"huthorizptionr
if (bearerToken tc mull 二 bearerTokenstartsuith("Bearer -) 人
rasarn bearerTeken substring(7)1 1/去掉 “Bearer ” 关
)
eu ma

doFiterInternal0 方法是过滤器的核心，在每个请求到达控制器之前被调用。方江
令牌，支持标准的-Bearer -前组格式。如果

首先通过 extractTokentrequest) 从HTTP请求头的"Authorization"字段中提取 JWT

当成功提取到令牌后，过滤器调用 jwtUtilsvalidateToken(token) 验证令牌的有效性，包括签名验证、过期时间检查等。验证通过后，使用
jwtutilsextractUsernameFromTokenttoken) 从令牌中提取用户名，然后通过 userDetailsServiceloadUserByUsernametusername) 加载完整的用户详细信息，包括用
户权限。




## 第 6 页


》

07、安全配置类
securityconfig定义了哪些 URL 需要什么级别的权限，并配置了认证和授权过滤器的执行顺序，以及会话管理策略。

罗
“本时spring securlty的实
+ 该定义了应再的安全配置,包括请求的航顶风、CS8F保护的配墨以及会话和理和时
configurarion
EnableyebSecurity
Public class SecurityConfig

/日志记录器，用于记录安全配时的相关俏息
Private static final Logger logger -LogBerfactory .BetLogBertSecurttyConfig.class)

站
可几securtoyfilrerchatn bean的方法

请方法主要用于本时应用的窑全旧刚，包括哪些请求党要授权、CsgF保护的启用或共用、会话芝理入竺
eparan hrrp Htpsecurtry对象，用于配因应用的安全规则

1 Brerurn SecurttyFtlterChatn对要，代表本轩好的安全过湖

Bthrows Exception 如果配置过程中必生错误，全出导肖

7

ae

Publie securityFilterchain securityfilterchain(hetpsecurtty hetp) threus Exception {
im

7/ 禁用Csaf保扩
etp-carttcarf -csrf-dtsable()
7/ 配置请求的掺要具风
urherizahfetpRequeststauthorize -》 aukherize
requesthatchers( "1aplvayusersregtster-，-1apt/vlyusers1logtnr).persttaaa0)
-requesthatchers("/apiyvlaaatnrve")-hasRole人-aamTN)
requgstatchers("/api/vHuser/"") -hasRoleUSER)
-anyWequast( .aukhenticated())
17/ 配置人和管理第妨
7/ 设置疾他建生暗为STATELESS，素示不人创建全语，通
sessionagapent(session -》sesston
.sessionCreationpolicy(SessionCreatonpolcy .STATELESS))
/1/ 记好家全配轩加加不功的信息
ogger_info( Security configuration loaded successfally)
// 拓加配置好的安全过法和
rerarn hrp.butld(;
1) cosch (Exception
// 记条配置安全过涝失区的错刘信息
oggerverrortfatled to configure securtty fllrer chainr，ei
7/ 狗册导，以便外部处理
六

其坟的hpI用

)
了

比如说静态资源和 Websocket 连接使用 permitAIl0 允许匿名访问; 登录注册接口对所有用户开放; 文件上传、对话历史、搜索等业务接口要求
hasAmyRolefUSER" "ADMIN-) ，多许普通用户和管理员访问; 管理员专属接口使用 hasRole(ADMIN") 严格限制只有管理员才能访问， 其他所有请求都需要通过
authenticated0 进行身份验证。

并采用 SessionCreationl

/STATELESS 无状态会话策略，完全依赖JWT 令牌进行身份验证，不在服务器册维护会话状态。

   RBAC 的实现流程

整个认证与权限控制流程从用户注册开始。用户首先通过 /api/vl/users/register 接口提交用户名和密码，系统会先检查用户名是否已存在，如果通过校验，则会
为该用户分配一个默认角色(通常是 USER) 。

注册完成后，用户可以通过 /api/vi/users/login 接口进行登录。系统会根据提交的用户名和密码进行验证，验证通过后，会生成一个包含用户信息(如用户名和
角色) 的JWT Token，返回给客户庙-

四- 《                   Hocalhost        品            由 + 吕
司-                           srm
安放芭明      包词         组织标签        启用基态           Q    9 DB @admn
ad
@          用户列表                                             mW 字列R
失 对天记录
有          有        aa       aa
oo           wm                                             [ED]
          ER        机。 aoxsorrnzae ozsoramzd [38
aass
ER                                           _
       2           机 zzsotztmz4e 20250712tt1249 [SEE
意 TAb
v
X口口忻旬时 @ 。 品a                mms 日we 加mm             aq
aa ED                                                       = 四
号             本
日
D
bw                     oaaa an
COREERGIOEEEYRNENGUGNEGRRGRRRREES和oureruovaouuuouewomannowuiv
|              下

Er ycaponrgs2
ra WoagED ecoai oaal vae osX io 7 hepiweenouEoS11E ouL it gealal yesamgt1sateneos1




## 第 7 页


Im
Lammuaoaa
国， De aiam @aam Go                         ?

客户端在后续访问其他接口时，需要将这个 JWT Token 放入请求头中的 Authorization 字段中。
并解析 Token，验证其合法性，并将对应的用户信息加载到 Spring Security 的上下文中

会通过自定义的 JwtAuthenticationFilter 对请求i

拦截，提取

最后，访问控制是基于角色来实现的。Spring Security 会根据配置类 SecurityConfig 中设定的权限规则，判断当前用户是否有权访问请求的接口。例如，只有拥有
ADMIN 角色的用户才能访问后台管理接口

五、面试题: 派聪明的 RBAC 还能继续优化吗?

首先是支持更多角色。如果系统有新的业务需求，比如需要增加一个"版主〔MODERATOR) 角色，只需要在 User Role 枚举中添加对应的枚举值，并在
SecurityConfig 中为这个新角色配置访问规则即可。

其次是引入动态权限管理。相比在代码里写死角色权限，我们可以将角色与权限信息存储到数据库中，通过服务在运
@PreAuthorize 注解，可以实现粒度更细、控制更灵活的方法级权限校验。

态加载。配合 Spring Security 提供的

最后是Token 刷新机制。为提升用户体验，我们可以增加出新 Token 的功能。当用户的访问 Token 快过期时，
有效期，避免频繁重新登录。这一步通常需要配合 Refresh Token 实现。这也是面试中可能考察的一个知识点。

过一个专门的接口获取新的 Token，从而延长登录

How access tokens wor|

Client                                     Resource
Application              全                    Server

User                                    Authorization
(Resource 0

比如说: 项目中的jwt token使用

种类型的token (长token还是短token， access token还是refresh token) ?

第一种回答，用的长 token，配置了 30 天的有效期，这样用户体验更流畅，不用频繁重新登录。 用户登录成功后，后端将生成的jwt 返回给前端，然后前端将其
保存在本地缓存; 之后前端与后册的交互时，都棕 jwt 放在j       比如可以将其放在 Http 身份认证的请求头 Authorization 中，也可以通过自定义的请求头来
传递; 后端接收到用户的请求，从请求头中获取 jwt，然后进行校验，通过之后，才响应相关的接口; 天则表示未登录。

追问: jwt 不支持续期的话 会不会用户还在使用中，结果登录失效了?
是的，确实会这样。但可以这样解决: 每次用户请求时，如果离过期不远了《比如只惠 5 分钟) ，就自动生成一个新的 token; 返回给前端 ~- 前端蔡换|昌 token;

上-        aherization Grant

Ice思         Access Taken
1           efresh Taken

1
1

1

1

1

1    1            ，
1    1 -0- access Taan    1
1    1            1    1
1     |)- Prarected esourcs -| Wesource |
Taaeor |              TS 1
1    上- access Taken -|    1
1    1            1    1
1    1etp- tmwalta Token Erar -|    1
1    1            +
1    1

1   1-     efresh Taken

1    1

1       Ice         ccaaa Taken

用户登录的时候，生成一个 token，将 token 存入 Redis，设置有效期，比如说三十分钟。 用户发起请求时，在拦截器中获取 token，验证其是否在 Redis 中，是否
过期。如果有效内，自动延长 30 分钟。 每次请求都延期一下，让 TTL 滑动前进，用户只要活跃就不会掉线。一旦用户长时间不操作，TTL 自动过期，登录状态失
效-

登录接口

(apt)
Logincontreller {





## 第 8 页


》

autoutrea
private medlsutils redisbeilsi

eposurepptng("/logtnr)
publte ResponaeEntttycstringy logindBRequestparas String usernase，BRequestparan String passvord)
7/ 机抽本好卫
if (Cradninr equals(usernawe) 枉 -123456"-equals(passvord)) {
string taken = UUID-randosuuTD() -tostring()

/设置 TYL 为 38 分入
eatsbtils-settredtskey，username， Duration_opnimutes(a6));

resarn ResponssEneity-okttoken);
)
Treeurn RespanseEnttsy status(Httpstatus_UaurhoRTzED) .body(-用户各或到镇-)

人
Ce
PR Goes Tuenmmeareeor amleeents analerinereepter
era
Te Ramans run
orrise
PC galean pralenalettgsaraleeese request gsar                ee ae sme mapum
et
TI
aeevertSLCGY Iontpe wos0，-记少 Takenn);
Ta
)
ra reatskey = ua ，akem
Er
EC
Tan eayetaeua .amumagrzen viue0，-Tuean 天大
0
1
Am
eatstnnsregtretredtseyy predioneainutestoa));
/可当前用PE
antreehetrtputsCrorrentlerr omrneei
)
)
Redis 工具类:
和
opene
Ce ua
erea
Eee Sonwuamreu masreoaaens
ae wa settstre ke str wa areden ea f
Re
》
aaae srg eeasertog kan
让
)
aaae via aqaretstrue aeyy padion aa
re
)
)
本          17人上            一
记人遇四四@S
国   讨论应以学习和精进为目的。请勿发布不友善或者负能量的内容，与人为善，比聪明更重要!
加                                                                                                                os 天
热门评论 区
篆 azess                                                                                  zasoaposa hzs




## 第 9 页


@派陪明
册上兴国四1

5                                                               026年3朋04日 1125
根据参考资料，Spring Data JPA 在派肌明的 RBAC 实现中用于简化数据库扣作。具体体现在:

1位置:
在 rapoairosy 属〔*oosrrevsrrerrrerr ) 中定义数据访问接口,继承 aaepoaitozycbaar，xcnay ，无需编写SQL *"即可实现数据库交互.

了核心作用
， 提供 inaaycasrnane1) 方法，通过方法名自动生成查询遇辑，实现根据用户名查找用户的功能(如 cusrcsossxnerailsservice 中请用)。

。 支持增放改查 (CRUD)、分页、持序等常见所作，减少手动编写SQL 的成本。

3 与 RBAC 的关联:
在用户认证流程中， szfeposicory 负责从数据库加载用户信息(如角色、密吗) ，为 Spring Security 的权限校验提供数据基础

总结; Spring Data JPA 作为数据访问展框架，通过声明式接口简化了数据库操作，是派生明系统中用户认证与权限控制的核心技术支反之一-
出5 用四

6条评论

篆 azoas                                                                         assoamosa mo

引用原文: 如果请求关中没有令垃或格式不正确，则了

二过程，让请求继续传递到下一个过尖中

为什么不直接请求，而要让请求继续传递@泊聪明
出汪加四呈1

mm                                                                                                                              026年03月04日 1712

在Spring Security 的JWT 认证过江器〈 TvrauzhenricasicnFilrsz ) 中，当请求头没有信和仙或格式不正确时选择吕过认证过程'而非直接，是出于设计灵活性
和责任分离"的考虑，具体原因加下:

， 认证 Authentication) : 验证用户身份 即-你是谁。
。 :raurhenricariongilcer 的职责仅限于解析JWT 令和并验证其有效性 (如签名、过期时间等).

如果请求头没有令牌或格式错误，说明用户未提供身份作证，此时无法完成认证，但也不应直接请求，因为后续的授权 (Authorization) "流程会处理未让
证用户。

。 授权(Authorization) : “用户权限 《即你能做什么")。
在 sacarisyconfia 中， 通过 Lanvvequezc1) .anthenticased1) 配置所有请求需认证，未认证的请求全被后续的授权这辑*”(如返回 101

maaehocizea )。

， 直接在认证过湾器，会绕过授权层的统一规则…，导臻权限控制多辑分用-

.支持公开接口的灵活性

。 系统中存在无矢认证的公开接口(如1: sin 、 -caiscec )

如果 -ucaurhencicaricneilcez 强制"所有无令牌请求，这些公开扩口村无法访问.

， 通过让过认证，让后续的securityconfig 根据规则决定是否放行，例20
Leeqaeseaaschers ln/api/viaaera/logtar) -permasaal0) 1/ 公开

aveaaaase0 .earhaneieasea() 71/ 其接D证
复提人加

3 时锡重复，保持过小器链清晰…
。 Spring Securiy 的过尖吕链 (如 osecaanepasevcrahuthencicasiongilter 、 aucauthenctcariongtlcer )搜须序执行。
， 在 ovtautheattcatienpilter 中无令卫请求"，会导致
。 公开接口无法访问 〈需帮外配置例外) 。
。 与其他认证方式(如表单登录冲突.
， 呈过认证后，由 sscurityconfiq 统一处理未认证请求，带加更清电目可维护.

4 性能优化
。 JWT 解析(如验证签名) 是相对耗时的操作
， 对明确无需认证的请求(如牌坊资源、公开 API) ，跳过JWT 解析可减少不必要的计算-

实际执行流程
1无人障请求 (如 125in

eicer 哑过认证 -继续传递到 secuzicycontig 。

， securicyconfig 通过 pernicall 0) 放行请求。

有令牌但无效 (如过期/伪造)

验证失败 一跳过认证 -继续传递到 <
，。 secaricycenfig 检测到未认证 一"并运回 4ol 。

3 有有效令障:




## 第 10 页


》

rraurhenricariongilcer 设置认证上下文 ~ 后续授权"通过。

总结
“*吝过认证而非直过”"，是为了:

， 过特认证授权-分离原则，六免职责混天

支持公开李品和混合认证场虹。

， 让 sscarisycensia 统一管理权限规则，提升可维护性
这种设计是 Spring Security 的最佳实践，确保安全到辑清晰且灵活。

出训汪 国四

鸭 sanas                                                                                  assoaoka aa

引用原文: 如果请求关中没有令牌或格式不正确，则让过认证过程，让请求继续传递到下一个过泪中

为什么直接请求，而要让请求继续传闻
由上革 用上

罗 aases                                                                                  assoamota has

引用原文: Spring DataJPA

@派陪明
出上半 国四1

二                                                               026年有04B 1125
根据参考资料，Spring Data JPA 在派联明的 RBAC 实现中用于简化数据库扣作。具体体现在:
1位置:
在 raposirory 展〈《 "vv
了核心作用:
， 提供 +inaayceernane1) 方法，通过方法名自动生成查询逻辑，实现根据用户名查找用户的功能 (如cuetc=oseznecailsservice 中调用)
。 支持增放改查 (CRUD)、分页排序等常见操作，减少手动编写 SQL 的成本。

… ) 中证义数据访问接口，继承 Psfepcsirory<basr，icn9> ，无需编写SQL"即可实现数据库交互。

3 与 RBAC 的关联:

在用户认证流程中， nsezFeposicory 负责从数据库加载用户信息 (如角色、密码) ，为 pring Security 的权限校验提供数据基础
总结: Spring Data JPA 作为数据访问层椎架，通过声明式接口简化了数据库排作，是派生明系统中用户认证与权限控制的核心技术支摆之一
出训汪 国四和

网 旧                                                                                                                                        026征01月27日 1956

引用原文: 04、JWT 工具类 JwtUtils负责生成、验证和解析JWT 令精。类中使用 @Valuef gfiwtsecret-keyj") 从配置文件读取 Base64 编码的密钢，通过
getSigningKey0 方法解码并生成 Secretkey 对象。令牌有效期设置为24小时。并使用 H5256 签名算法确保令牌的完整性。 @Component public dass JwtUtis (private
Static final Sting SECRET KEY = "test secret key' Priate static final long EXPIRATION TIME = 86400000: // 24 hours Public Sting generateTokenfSting usernamej{
retum wtsbuilder0 setSubjecttusername) setExpirationtnew DatefsystemcurrentTimeMilis0 + EXPIRATION_TIME) signWithtsignatureNigorithm HS256，
SECRETKEV compad0')

这里和项目代码有点不一样，下面的措术是对的.
generateTokentsting usernama) 方法是权限信息封装的核心，它不仅和用户各作为 subject，还将权限信息封装到 claims 中，包括用户角色 (role)、用户ID (usenld)、标
签 (orgTags) 和主 (primaryOrg) 等。 这种设计使得 JWT 令牌万为一个自包含的权限并体，避兔频旺的数据库查询-

出上 国回旦

网 上                                                                                                                                        oz6年nR27B iao0

引用原文: 不仅将用户各作为subject，还将权限信息封装到 caims 中，和包括用户角色 (role)、用户ID (userid)、组织标签 (orgTags) 和主组织 (primanyOrg) 等-
这种设计使得 JWT 令牌成为一个自包含

这个看一下
出5茧 国四

图 wanan                                                                        osehnmea az

引用原文: 权限集合 【 getAuthoritiestusergetRoleg) )。

为什么用集合?
设计原则: 用户可以有多个权限

扩展性: 未来可以轻松汪加具体权限

灵活性: 支持细粒度的权限控制

虽然你现在只用了角色，但框架为你预贸了扩展空间! 这就是好的设计! 全
2 国昌




