# UserService - 用户与组织管理

## 📌 基本信息

- **文件路径**：`src/main/java/com/yizhaoqi/smartpai/service/UserService.java`
- **代码行数**：约500行
- **核心职责**：用户注册/认证、组织标签CRUD、权限分配

---

## 🎯 一句话理解

> UserService = 用户和组织标签的「管家」
> 注册时自动创建私人空间，通过组织标签实现多租户权限隔离

---

## 🏗️ 用户-组织标签体系

```
组织标签（OrganizationTag）
├── DEFAULT              ← 系统默认标签
├── TECH                 ← 管理员创建的部门标签
│   └── TECH_BACKEND     ← 子标签（支持层级）
├── FINANCE              ← 另一个部门
└── PRIVATE_zhangsan     ← 用户zhangsan的私人空间（自动创建）

用户（User）
├── orgTags: "PRIVATE_zhangsan,TECH"  ← 逗号分隔，可有多个
└── primaryOrg: "PRIVATE_zhangsan"    ← 主组织（上传文件时的默认标签）
```

---

## 🔥 registerUser() - 注册流程

```java
@Transactional
public void registerUser(String username, String password) {
    // 1. 检查用户名是否重复
    if (userRepository.findByUsername(username).isPresent()) {
        throw new CustomException("Username already exists", BAD_REQUEST);
    }

    // 2. 确保DEFAULT标签存在（系统内部使用）
    ensureDefaultOrgTagExists();

    // 3. 创建用户
    User user = new User();
    user.setUsername(username);
    user.setPassword(PasswordUtil.encode(password));  // BCrypt加密
    user.setRole(User.Role.USER);
    userRepository.save(user);  // 先保存，获得自增ID

    // 4. 创建用户专属私人标签：PRIVATE_{username}
    String privateTagId = "PRIVATE_" + username;
    createPrivateOrgTag(privateTagId, username, user);

    // 5. 绑定私人标签 + 设为主组织
    user.setOrgTags(privateTagId);      // orgTags = "PRIVATE_zhangsan"
    user.setPrimaryOrg(privateTagId);   // primaryOrg = "PRIVATE_zhangsan"
    userRepository.save(user);

    // 6. 更新Redis缓存
    orgTagCacheService.cacheUserOrgTags(username, List.of(privateTagId));
    orgTagCacheService.cacheUserPrimaryOrg(username, privateTagId);
}
```

**注册后的初始状态：**

```
用户 zhangsan：
  orgTags = "PRIVATE_zhangsan"
  primaryOrg = "PRIVATE_zhangsan"

OrganizationTag PRIVATE_zhangsan：
  name = "zhangsan的私人空间"
  description = "用户的私人组织标签，仅用户本人可访问"
  createdBy = zhangsan
```

---

## 🔥 authenticateUser() - 登录认证

```java
public String authenticateUser(String username, String password) {
    User user = userRepository.findByUsername(username)
        .orElseThrow(() -> new CustomException(
            "Invalid username or password", UNAUTHORIZED));

    // BCrypt密码比较
    if (!PasswordUtil.matches(password, user.getPassword())) {
        throw new CustomException("Invalid username or password", UNAUTHORIZED);
    }

    return user.getUsername();  // 返回用户名，由Controller调用JwtUtils生成Token
}
```

**密码安全：**
```java
// 存储时：BCrypt单向哈希
PasswordUtil.encode("mypassword")
// → "$2a$10$N9qo8uLOickgx2ZMRZoMyeIjZAgcfl7p92ldGxad68LJZdL17lhWy"

// 验证时：不解密，重新哈希比较
PasswordUtil.matches("mypassword", storedHash)
// BCrypt自动处理salt，每次哈希结果不同但比较正确
```

---

## 🔥 组织标签层级体系

### createOrganizationTag() - 创建标签

```java
// 只有管理员可以创建
@Transactional
public OrganizationTag createOrganizationTag(
    String tagId, String name, String description,
    String parentTag,         // 父标签ID（可为null）
    String creatorUsername    // 必须是ADMIN
) {
    // 防循环检测：设置parentTag时检查是否形成环
    if (wouldFormCycle(tagId, parentTag)) {
        throw new CustomException("Would create cycle", BAD_REQUEST);
    }
    // 创建标签后清除所有有效标签缓存（层级关系变了）
    orgTagCacheService.invalidateAllEffectiveTagsCache();
}
```

### 层级标签的权限继承

```
标签树：
COMPANY
├── TECH
│   ├── TECH_BACKEND
│   └── TECH_FRONTEND
└── FINANCE

用户A 拥有标签 TECH：
  有效标签 = [TECH, TECH_BACKEND, TECH_FRONTEND]  ← 自动继承子标签

用户B 拥有标签 COMPANY：
  有效标签 = [COMPANY, TECH, TECH_BACKEND, TECH_FRONTEND, FINANCE]

检索时用有效标签列表过滤ES，实现层级权限继承
```

### getOrganizationTagTree() - 获取标签树

```java
// 递归构建树形结构
public List<Map> getOrganizationTagTree() {
    // 获取所有根节点（parentTag == null）
    List<OrganizationTag> roots = organizationTagRepository.findByParentTag(null);
    return buildTagTreeRecursive(roots);
}

private List<Map> buildTagTreeRecursive(List<OrganizationTag> tags) {
    return tags.stream().map(tag -> {
        Map node = new HashMap();
        node.put("tagId", tag.getTagId());
        node.put("name", tag.getName());
        // 递归获取子节点
        List<OrganizationTag> children =
            organizationTagRepository.findByParentTag(tag.getTagId());
        if (!children.isEmpty()) {
            node.put("children", buildTagTreeRecursive(children));
        }
        return node;
    }).toList();
}
```

**返回给前端的树形结构：**

```json
[
  {
    "tagId": "COMPANY",
    "name": "全公司",
    "children": [
      {
        "tagId": "TECH",
        "name": "技术部",
        "children": [
          {"tagId": "TECH_BACKEND", "name": "后端组"}
        ]
      },
      {"tagId": "FINANCE", "name": "财务部"}
    ]
  }
]
```

---

## 🔥 assignOrgTagsToUser() - 分配标签

```java
@Transactional
public void assignOrgTagsToUser(Long userId, List<String> orgTags, String adminUsername) {
    // 验证操作者是ADMIN
    // 验证所有标签存在

    // 关键：保留用户的私人标签！
    String privateTagId = "PRIVATE_" + user.getUsername();
    Set<String> finalTags = new HashSet<>(orgTags);
    if (hasPrivateTag) {
        finalTags.add(privateTagId);  // 私人标签不能被覆盖
    }

    user.setOrgTags(String.join(",", finalTags));
    userRepository.save(user);

    // 清除并更新缓存
    orgTagCacheService.deleteUserOrgTagsCache(user.getUsername());
    orgTagCacheService.cacheUserOrgTags(user.getUsername(), new ArrayList<>(finalTags));
    orgTagCacheService.deleteUserEffectiveTagsCache(user.getUsername());
}
```

**私人标签保护机制：**
```
场景：管理员给用户zhangsan分配标签 [TECH]

如果直接覆盖：
  orgTags = "TECH"  ← 私人空间 PRIVATE_zhangsan 丢失！
  用户失去私人文档访问权限

有保护的逻辑：
  finalTags = {TECH} + {PRIVATE_zhangsan} = {TECH, PRIVATE_zhangsan}
  orgTags = "TECH,PRIVATE_zhangsan"  ← 私人空间保留
```

---

## 🔥 deleteOrganizationTag() - 删除标签（多重保护）

```java
@Transactional
public void deleteOrganizationTag(String tagId, String adminUsername) {
    // 保护1：DEFAULT标签不能删除
    if ("DEFAULT".equals(tagId)) throw new CustomException("Cannot delete default tag");

    // 保护2：有子标签的不能删除
    List<OrganizationTag> children = organizationTagRepository.findByParentTag(tagId);
    if (!children.isEmpty()) throw new CustomException("Has child tags");

    // 保护3：已分配给用户的不能删除
    List<User> users = userRepository.findAll();
    for (User user : users) {
        Set<String> userTags = Set.of(user.getOrgTags().split(","));
        if (userTags.contains(tagId)) throw new CustomException("Assigned to users");
    }

    organizationTagRepository.delete(tag);
    orgTagCacheService.invalidateAllEffectiveTagsCache();
}
```

---

## ⚠️ 代码的不足

### 1. orgTags 用逗号分隔字符串存储，扩展性差

```java
// 当前：字符串存储
user.setOrgTags("TECH,FINANCE,DEFAULT");

// 问题：
//   查询"拥有TECH标签的所有用户"需要 LIKE '%TECH%'，全表扫描
//   标签数量多时字符串很长
//   增删标签需要字符串解析

// 更好：独立的关联表
// user_org_tag(user_id, tag_id)，支持精确查询和索引
```

### 2. deleteOrganizationTag 遍历所有用户

```java
List<User> users = userRepository.findAll();  // 全表扫描！
for (User user : users) { ... }
// 1万用户时性能差
// 应改为：SELECT COUNT(*) FROM user WHERE org_tags LIKE '%{tagId}%'
// 或者通过关联表查询
```

### 3. 没有角色细化

```
当前只有两个角色：USER 和 ADMIN
企业场景常见的需求：
  - 部门管理员（只能管理本部门的标签和用户）
  - 只读用户（只能检索，不能上传）
  - 审计员（可以查看所有操作日志）
目前这些都无法实现，需要引入RBAC（基于角色的访问控制）
```

---

## ❓ 我的疑问记录

| 疑问 | 答案 |
|------|------|
| 为什么每个用户都有私人标签？ | 实现文档的个人隔离。私人标签只有本人有，上传的私有文档只有自己能检索到 |
| 层级标签的权限继承在哪里计算？ | OrgTagCacheService.getUserEffectiveOrgTags()，递归向下展开所有子标签 |
| DEFAULT标签有什么用？ | 系统内部使用，确保组织标签机制初始化时有根节点，不对用户直接暴露 |
| 注册时为什么先save再创建私人标签？ | 创建私人标签需要 createdBy=user，而user.id在save之前是null |

---

## 🔗 相关文件

- [JWT认证体系](../07-安全与认证/01-JWT认证体系.md) - Token中携带orgTags
- [HybridSearchService](../04-混合检索/01-HybridSearchService.md) - 检索时用有效标签过滤
- [DocumentService](../09-文档管理/01-DocumentService.md) - 文件列表权限控制

