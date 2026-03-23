# JWT认证体系 - 安全与认证

## 📌 涉及文件

| 文件 | 职责 |
|------|------|
| `config/SecurityConfig.java` | Spring Security规则配置 |
| `config/JwtAuthenticationFilter.java` | 每次请求解析JWT，设置用户上下文 |
| `config/OrgTagAuthorizationFilter.java` | 解析orgTag放入请求属性 |
| `utils/JwtUtils.java` | JWT生成/验证/刷新工具类 |
| `service/TokenCacheService.java` | Redis缓存Token状态 |

---

## 🎯 一句话理解

> 每次HTTP请求 → Filter解析JWT → 验证Redis缓存 → 放入SecurityContext
> 无状态认证：服务器不保存Session，Token本身携带用户信息

---

## 🔐 安全过滤器链

```
HTTP请求
    ↓
【JwtAuthenticationFilter】  ← 第1道
    解析 Authorization: Bearer {token}
    验证Token有效性（Redis + JWT签名）
    自动刷新快过期的Token
    设置 SecurityContextHolder
    ↓
【OrgTagAuthorizationFilter】 ← 第2道
    从Token提取 userId, role, orgTag
    设置到 request.setAttribute()
    （Controller用 @RequestAttribute 取值）
    ↓
【Spring Security授权检查】
    .hasRole("ADMIN") / .hasAnyRole("USER","ADMIN")
    ↓
【Controller处理业务】
```

---

## 🔥 JwtUtils - Token生命周期

### Token的内容（JWT Payload）

```json
{
  "sub": "username",        // 用户名
  "tokenId": "abc123",      // 唯一ID，用于Redis查询
  "userId": "42",           // 数据库用户ID
  "role": "USER",           // 角色
  "orgTags": "TECH,DEFAULT", // 组织标签
  "primaryOrg": "TECH",     // 主组织
  "exp": 1234567890         // 过期时间
}
```

### 时间参数

```java
EXPIRATION_TIME = 3600000;         // Token有效期：1小时
REFRESH_TOKEN_EXPIRATION_TIME = 604800000; // RefreshToken有效期：7天
REFRESH_THRESHOLD = 300000;        // 提前刷新阈值：剩余5分钟时开始刷新
REFRESH_WINDOW = 600000;           // 宽限期：过期后10分钟内仍可刷新
```

### Token状态机

```
生成Token
    ↓ Redis缓存 tokenId → {userId, username, expireTime}
有效期内（1小时）
    ↓ 剩余<5分钟时
自动刷新（生成新Token，通过响应头 New-Token 返回给前端）
    ↓ 过期后
宽限期（10分钟内）
    ↓ 仍可刷新
宽限期结束
    ↓
Token完全失效，需重新登录
```

### generateToken() - 生成Token

```java
public String generateToken(String username) {
    // 1. 查询用户信息（角色、组织标签）
    User user = userRepository.findByUsername(username);

    // 2. 生成唯一tokenId
    String tokenId = UUID.randomUUID().toString().replace("-", "");

    // 3. 构建JWT（包含所有用户信息）
    Map<String, Object> claims = Map.of(
        "tokenId", tokenId,
        "role", user.getRole().name(),
        "userId", user.getId().toString(),
        "orgTags", user.getOrgTags(),
        "primaryOrg", user.getPrimaryOrg()
    );

    String token = Jwts.builder()
        .setClaims(claims)
        .setSubject(username)
        .setExpiration(new Date(now + EXPIRATION_TIME))
        .signWith(getSigningKey(), HS256)
        .compact();

    // 4. 缓存到Redis（可以做集中式失效）
    tokenCacheService.cacheToken(tokenId, userId, username, expireTime);

    return token;
}
```

### validateToken() - 双重验证

```java
public boolean validateToken(String token) {
    // 第1步：从JWT提取tokenId（快速操作）
    String tokenId = extractTokenIdFromToken(token);

    // 第2步：查Redis（主要验证）
    // Redis中有记录 + 未被加入黑名单 = 有效
    if (!tokenCacheService.isTokenValid(tokenId)) return false;

    // 第3步：验证JWT签名（防篡改）
    Jwts.parserBuilder().setSigningKey(getSigningKey())
        .build().parseClaimsJws(token);

    return true;
}
```

**为什么要双重验证？**
```
只验证JWT签名：
  无法主动失效Token（如用户登出、密码修改）
  Token在有效期内永远有效

只验证Redis：
  无法防止Token被篡改

双重验证：
  Redis记录失效 → Token立即失效（登出生效）
  JWT签名验证 → 防止伪造Token
```

### 自动刷新机制

```java
// JwtAuthenticationFilter.doFilterInternal() 中
if (jwtUtils.validateToken(token)) {
    // Token有效，但快过期了（剩余<5分钟）
    if (jwtUtils.shouldRefreshToken(token)) {
        String newToken = jwtUtils.refreshToken(token);
        response.setHeader("New-Token", newToken);  // 通过响应头返回新Token
    }
} else {
    // Token已过期，但在10分钟宽限期内
    if (jwtUtils.canRefreshExpiredToken(token)) {
        String newToken = jwtUtils.refreshToken(token);
        response.setHeader("New-Token", newToken);
        // 使用新Token继续处理请求（无感刷新）
    }
}
```

**无感刷新流程：**
```
前端：发请求（携带快过期的Token）
服务端：发现Token剩余<5分钟 → 生成新Token
服务端：在响应头里放 New-Token: {新Token}
前端：收到响应，检查是否有 New-Token Header
前端：有则更新本地存储的Token
前端：下次请求用新Token
```

---

## 🔥 SecurityConfig - 路由权限规则

```java
.authorizeHttpRequests(authorize -> authorize
    // 完全公开
    .requestMatchers("/api/v1/users/register", "/api/v1/users/login").permitAll()
    .requestMatchers("/chat/**", "/ws/**").permitAll()  // WebSocket
    .requestMatchers("/api/v1/test/**").permitAll()

    // 普通用户和管理员都可访问
    .requestMatchers("/api/v1/upload/**").hasAnyRole("USER", "ADMIN")
    .requestMatchers("/api/search/**").hasAnyRole("USER", "ADMIN")
    .requestMatchers("/api/v1/users/conversation/**").hasAnyRole("USER", "ADMIN")

    // 仅管理员
    .requestMatchers("/api/v1/admin/**").hasRole("ADMIN")

    // 其他所有请求需要认证
    .anyRequest().authenticated()
)
// 无状态Session（不创建HttpSession）
.sessionManagement(session -> session
    .sessionCreationPolicy(SessionCreationPolicy.STATELESS))
```

**路由权限总览：**

| 路径 | 权限 | 说明 |
|------|------|------|
| `/api/v1/users/login` | 公开 | 登录 |
| `/api/v1/users/register` | 公开 | 注册 |
| `/chat/**` | 公开 | WebSocket（自己验JWT）|
| `/api/v1/upload/**` | USER/ADMIN | 文件上传 |
| `/api/search/**` | USER/ADMIN | 检索 |
| `/api/v1/admin/**` | ADMIN only | 管理员功能 |

---

## 🔥 Token在请求中的传递

```
前端登录 → 获得JWT Token
    ↓
前端每次请求携带：
GET /api/v1/documents
Authorization: Bearer eyJhbGciOiJIUzI1NiJ9.eyJ...
    ↓
JwtAuthenticationFilter 解析：
    username = "zhangsan"
    userId = "42"
    role = "USER"
    orgTags = "TECH,DEFAULT"
    ↓
OrgTagAuthorizationFilter 设置到请求属性：
    request.setAttribute("userId", "42")
    request.setAttribute("role", "USER")
    request.setAttribute("orgTag", "TECH")
    ↓
Controller 取用：
    @RequestAttribute("userId") String userId
    @RequestAttribute("role") String role
```

---

## 🔥 Token黑名单（登出实现）

```java
// 登出时调用
public void invalidateToken(String token) {
    String tokenId = extractTokenIdFromToken(token);
    // 加入Redis黑名单
    tokenCacheService.blacklistToken(tokenId, expireTime);
    // 从缓存中移除
    tokenCacheService.removeToken(tokenId, userId);
}

// isTokenValid() 中检查
public boolean isTokenValid(String tokenId) {
    // 检查是否在黑名单中
    if (isBlacklisted(tokenId)) return false;
    // 检查是否在有效Token缓存中
    return tokenExists(tokenId);
}
```

---

## ⚠️ 代码的不足

### 1. orgTags 存在JWT里，修改权限不生效

```
场景：管理员给用户A新增了组织标签FINANCE
用户A的Token还有30分钟才过期
→ Token里的orgTags还是旧值，没有FINANCE
→ 用户A在这30分钟内无法访问FINANCE的文档
→ 必须等Token过期重新登录才能生效

解决方案：
① 权限变更时强制让用户所有Token失效（tokenCacheService.removeAllUserTokens）
② 不把orgTags存在JWT里，每次从Redis/数据库动态获取
```

### 2. WebSocket的JWT放在URL路径里，有安全风险

```
当前：ws://host/chat/{jwt_token}
Token出现在URL中 → 会被记录在：
  - 浏览器历史
  - 服务器访问日志
  - 代理日志

更安全的方式：
  WebSocket握手时通过 Sec-WebSocket-Protocol 头传递Token
  或建立连接后立即发送认证消息
```

### 3. 宽限期内的Token刷新没有频率限制

```
恶意用户可以在宽限期内无限刷新Token
→ 实际上延长了Token有效期

建议：每个tokenId只允许刷新一次
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| JWT的密钥存在哪里？ | application.yml的 `jwt.secret-key`，Base64编码的HMAC-SHA256密钥 |
| 为什么要把tokenId存在JWT里再存Redis，不直接用用户名查Redis？ | 同一用户可以在多个设备登录，每个设备有不同tokenId，可以精确失效某一个设备的Token |
| STATELESS Session意味着什么？ | 服务器不创建HttpSession，每次请求都通过JWT重新验证身份，天然支持水平扩展 |
| RefreshToken和Token有什么区别？ | Token短期有效（1小时）用于API调用；RefreshToken长期有效（7天）只用于换取新Token |

---

## 🔗 相关文件

- [UserService](../08-用户与组织管理/01-UserService.md) - 用户注册登录
- [OrgTagCacheService](#) - 组织标签缓存
- [FileProcessingConsumer](../05-Kafka与异步处理/01-FileProcessingConsumer.md) - 权限信息在异步任务中的传递

