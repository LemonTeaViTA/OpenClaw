# Spring 学习资料索引

## 📚 已归档文档

### 面渣逆袭 Spring 篇 V2.0 亮白版.pdf
- **归档日期**: 2026-03-04
- **来源**: 飞书消息附件
- **文件 Key**: `file_v3_00vf_cd881008-79a3-4d68-a2f8-e301f339b46g`
- **状态**: ⏳ 待下载到本地

## 📋 核心知识点目录

根据文档内容，Spring 面试核心涵盖：

1. **Spring 核心**
   - IOC 容器与 Bean 生命周期
   - DI 依赖注入（构造器/Setter/字段）
   - AOP 面向切面编程（动态代理、AspectJ）

2. **Bean 管理**
   - Bean 作用域（Singleton/Prototype/Request/Session）
   - Bean 初始化与销毁
   - 循环依赖解决（三级缓存）

3. **事务管理**
   - @Transactional 注解
   - 传播行为（REQUIRED/REQUIRES_NEW/NESTED）
   - 隔离级别与失效场景

4. **Spring MVC**
   - 请求处理流程
   - 常用注解（@Controller/@RestController/@RequestBody）
   - 拦截器与过滤器

5. **Spring Boot**
   - 自动装配原理
   - Starter 机制
   - 常用配置与 Actuator

## 🎯 学习建议

1. 结合派聪明项目中的 Spring 使用场景理解（如 Controller 层、Service 层、事务管理）
2. 重点关注：AOP 在日志/权限中的应用、事务失效场景、自动装配原理
3. 模拟面试时优先考察：Bean 生命周期、循环依赖、事务传播、AOP 实现

## 🔗 与派聪明项目关联

| 模块 | 派聪明应用场景 |
|------|---------------|
| IOC | 文档解析器、向量存储、LLM 服务注入 |
| AOP | 接口日志、性能监控、权限校验 |
| 事务 | ES 写入与 MySQL 记录的事务一致性 |
| Spring Boot | 项目启动、自动配置、健康检查 |

---
*最后更新：2026-03-04*
