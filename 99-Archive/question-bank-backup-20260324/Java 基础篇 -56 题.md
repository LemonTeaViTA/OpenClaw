# Java 基础篇 - 面试题库

> 来源：面渣逆袭 Java 基础篇 V2.1  
> 整理时间：2026-03-14  
> 题数：56 题

---

## 1. Java 概述（6 题）

### 【ID: java-001】题 1：Java 语言有哪些主要特点？

**答案：**

1. **面向对象**：封装、继承、多态
2. **跨平台性**：一次编译，处处运行（JVM）
3. **自动内存管理**：GC 自动回收垃圾对象
4. **多线程支持**：内置多线程机制
5. **安全性**：字节码验证、沙箱机制
6. **健壮性**：强类型、异常处理、边界检查
7. **即时编译**：JIT 编译器
8. **丰富的类库**：Java API

**记忆口诀：** 面跨自多安健即类

---

### 【ID: java-002】题 2：JVM、JRE、JDK 三者有什么区别？

**答案：**

**包含关系：** JDK > JRE > JVM

| 名称 | 全称 | 作用 | 包含内容 |
|------|------|------|---------|
| JVM | Java Virtual Machine | 运行字节码 | 类加载器、运行时数据区、执行引擎 |
| JRE | Java Runtime Environment | 运行 Java 程序 | JVM + 核心类库 |
| JDK | Java Development Kit | 开发 Java 程序 | JRE + 开发工具（javac、java 等） |

---

### 【ID: java-003】题 3：Java 跨平台原理是什么？

**答案：**

.java 源文件 → javac 编译 → .class 字节码（平台无关）→ JVM 解释/编译 → 机器码（平台相关）

**关键：** 字节码平台无关，JVM 平台相关。每个平台有自己的 JVM 实现，将相同的字节码转换为对应的机器码。

---

### 【ID: java-004】题 4：Java 的发展历史？主要版本有哪些？

**答案：**

**重要版本：**
- Java 5（2004）：泛型、注解
- Java 7（2011）：try-with-resources
- **Java 8（2014）**：Lambda、Stream API（最经典）
- Java 11（2018）：LTS
- **Java 17（2021）**：LTS（当前主流）
- **Java 21（2023）**：LTS（虚拟线程）

**LTS 版本：** 8、11、17、21

---

### 【ID: java-005】题 5：Java 的主要应用领域有哪些？

**答案：**

1. **企业级后端开发**：Spring Boot、微服务
2. **大数据处理**：Hadoop、Spark、Flink
3. **移动开发**：Android
4. **金融系统**：银行、证券、支付
5. **云计算**：Kubernetes、Dubbo
6. **嵌入式系统**：IoT 设备
7. **游戏开发**：服务器端、Minecraft

---

### 【ID: java-006】题 6：如何配置 Java 开发环境？

**答案：**

1. 下载并安装 JDK（推荐 Java 17 或 21）
2. 配置环境变量：
   - JAVA_HOME = JDK 安装路径
   - PATH = %JAVA_HOME%\bin
3. 验证安装：`java -version`、`javac -version`
4. 安装 IDE（推荐 IntelliJ IDEA）
5. 配置 Maven（可选）

---

## 2. 基础语法（10 题）

### 题 7：Java 有哪些基本数据类型？各占用多少字节？

**答案：**

| 类型 | 关键字 | 字节 | 取值范围 |
|------|--------|------|---------|
| 字节型 | byte | 1 | -128 ~ 127 |
| 短整型 | short | 2 | -32768 ~ 32767 |
| 整型 | int | 4 | -2³¹ ~ 2³¹-1 |
| 长整型 | long | 8 | -2⁶³ ~ 2⁶³-1 |
| 单精度 | float | 4 | ±3.4×10³⁸ |
| 双精度 | double | 8 | ±1.7×10³⁰⁸ |
| 字符型 | char | 2 | \u0000 ~ \uffff |
| 布尔型 | boolean | 1/4* | true/false |

*boolean：数组中 1 字节，单独使用时未定义

---

### 题 8：& 和 && 的区别？

**答案：**

| 运算符 | 名称 | 特点 | 使用场景 |
|--------|------|------|---------|
| & | 逻辑与/按位与 | 两边都执行 | 位运算 |
| && | 短路与 | 左边 false 时右边不执行 | 常规判断（推荐） |

**示例：**
```java
// 短路保护
if (str != null && str.length() > 0) {
    // 安全：如果 str 为 null，不会执行 length()
}
```

---

### 题 9：final、finally、finalize 的区别？

**答案：**

| 关键字 | 作用 | 使用场景 |
|--------|------|---------|
| final | 修饰符，表示不可变 | 修饰类（不可继承）、方法（不可重写）、变量（不可修改） |
| finally | 异常处理的一部分 | try-catch-finally，最终会执行的代码块 |
| finalize() | Object 类的方法 | GC 回收前调用（已废弃） |

---

### 题 10：== 和 equals 的区别？

**答案：**

| 对比项 | == | equals() |
|--------|----|---------|
| 本质 | 运算符 | Object 类的方法 |
| 基本数据类型 | 比较值 | 不能使用 |
| 引用数据类型 | 比较地址 | 默认比较地址，可重写比较值 |

**示例：**
```java
String s1 = new String("abc");
String s2 = new String("abc");
s1 == s2;      // false（地址不同）
s1.equals(s2); // true（值相同）
```

---

### 题 11：类型转换与复合赋值

**答案：**

**自动类型转换（小→大）：** byte → short → int → long → float → double

**强制类型转换（大→小）：** `(int) doubleValue`

**复合赋值：** `+=`、`-=`、`*=`、`/=` 等，包含自动类型转换

```java
int a = 10;
a += 3.5;  // 相当于 a = (int)(a + 3.5)
```

---

### 题 12：& vs && 短路与（实际应用）

**答案：**

**短路优化：**
```java
// 推荐：短路保护
if (obj != null && obj.isValid()) {
    // 安全
}

// 危险：不短路
if (obj != null & obj.isValid()) {
    // obj 为 null 时仍会调用 isValid() → NPE
}
```

---

### 题 13：final/finally/finalize 区别（详细）

**答案：**

**final 修饰变量的细节：**
- 基本数据类型：值不可变
- 引用数据类型：地址不可变，但内容可变

```java
final List<String> list = new ArrayList<>();
list.add("item");  // ✅ 允许（内容可变）
list = new ArrayList<>();  // ❌ 错误（地址不可变）
```

---

### 题 14：== vs equals（hashCode）

**答案：**

**为什么重写 equals 必须重写 hashCode？**

因为 HashMap、HashSet 等集合同时使用 hashCode 和 equals 判断对象是否相等。如果只重写 equals，会导致哈希冲突时无法正确判断。

---

### 题 15：Java 是值传递还是引用传递？

**答案：**

**Java 只有值传递！**

- 基本数据类型：传递值的副本
- 引用数据类型：传递引用的副本（地址的副本）

```java
public void change(StringBuilder sb) {
    sb.append("world");  // ✅ 影响原对象（地址相同）
    sb = new StringBuilder();  // ❌ 不影响原引用（地址副本）
}
```

---

### 题 16：深拷贝 vs 浅拷贝

**答案：**

| 类型 | 说明 | 实现方式 |
|------|------|---------|
| 浅拷贝 | 只复制对象本身，不复制引用的对象 | clone() |
| 深拷贝 | 复制对象本身 + 引用的所有对象 | 序列化、手动拷贝 |

---

## 3. 面向对象（16 题）

（此处省略 16 题，格式同上）

---

## 4. String 类（8 题）

### 题 33：String 为什么是不可变类？

**答案：**

**底层实现：**
```java
public final class String {
    private final char[] value;  // final 修饰
}
```

**好处：**
1. 安全性（传递过程不被修改）
2. 线程安全（多线程共享无需同步）
3. 缓存 hashCode（HashMap 的 key 高效）
4. 字符串常量池（节省内存）
5. 可用作 Map 的 key

---

### 题 34：String vs StringBuilder vs StringBuffer

**答案：**

| 特性 | String | StringBuilder | StringBuffer |
|------|--------|--------------|--------------|
| 可变性 | 不可变 | 可变 | 可变 |
| 线程安全 | ✅ | ❌ | ✅（synchronized） |
| 性能 | 低 | 高（最快） | 中 |
| 使用场景 | 少量操作 | 单线程大量操作 | 多线程操作 |

---

### 题 35：字符串拼接原理？

**答案：**

**编译器优化：**
```java
// 源码
String s = "a" + "b" + "c";

// 编译后
String s = new StringBuilder()
    .append("a")
    .append("b")
    .append("c")
    .toString();
```

**使用建议：**
- 常量/少量变量拼接：用 `+`（简洁）
- 循环/大量拼接：用 `append()`（高效）

---

（其余题目继续...）

---

## 5. 异常处理（4 题）

## 6. IO 流（6 题）

## 7. 反射泛型注解（6 题）

---

## 8. 补充题目（7 题 - 2026-03-20 新增）

### 题 57：成员变量和局部变量的区别

**答案：**

| 对比维度 | 成员变量 | 局部变量 |
|---------|---------|---------|
| 定义位置 | 类中、方法外 | 方法内、代码块内 |
| 作用域 | 整个类 | 代码块内 |
| 默认值 | 有默认值 | 无默认值，必须显式初始化 |
| 内存位置 | 堆内存 | 栈内存 |
| 生命周期 | 随对象 | 随方法调用 |

**记忆口诀**："成局五别"：位、域、值、存、命

---

### 题 58：Java 创建对象的几种方式

**答案：**

**4 种方式：**
1. **new 关键字**：`new MyClass()`（最常用）
2. **反射**：`Class.forName().newInstance()`（框架用）
3. **clone()**：`obj.clone()`（对象复制）
4. **反序列化**：`ObjectInputStream.readObject()`（持久化）

**记忆口诀**："牛（new）反（反射）拷（clone）序（序列化）"

---

### 题 59：Object 类的常见方法

**答案：**

**11 个方法：**
| 方法 | 作用 | 使用频率 |
|------|------|---------|
| toString() | 对象字符串表示 | ⭐⭐⭐⭐⭐ |
| equals(Object obj) | 判断对象相等 | ⭐⭐⭐⭐⭐ |
| hashCode() | 返回哈希码 | ⭐⭐⭐⭐⭐ |
| clone() | 对象克隆 | ⭐⭐⭐ |
| getClass() | 获取运行时类 | ⭐⭐⭐⭐ |
| notify()/notifyAll() | 唤醒等待线程 | ⭐⭐⭐ |
| wait() | 使线程等待 | ⭐⭐⭐ |
| finalize() | GC 前调用（已废弃） | ❌ |

**重点**：toString()、equals()、hashCode() 必须掌握

---

### 题 60：Java 有几种序列化方式

**答案：**

**4 种方式：**
| 方式 | 实现接口 | 使用场景 | 性能 |
|------|---------|---------|------|
| Java 原生序列化 | Serializable | 简单持久化 | ⭐⭐ |
| Externalizable | Externalizable | 自定义序列化 | ⭐⭐⭐ |
| JSON 序列化 | Jackson/Gson | Web API | ⭐⭐⭐⭐ |
| 协议序列化 | Protobuf/Thrift | 高性能 RPC | ⭐⭐⭐⭐⭐ |

**transient 作用**：修饰的字段不序列化（敏感信息、资源句柄）

---

### 题 61：Socket 网络编程了解吗

**答案：**

**Socket** = 网络通信端点

**TCP Socket 流程：**
```
服务端：ServerSocket → accept() → getInputStream()/getOutputStream()
客户端：Socket → getOutputStream()/getInputStream()
```

**BIO/NIO/AIO：**
- **BIO**：同步阻塞，一个连接一个线程
- **NIO**：同步非阻塞，多路复用（Selector）
- **AIO**：异步非阻塞，事件驱动

**三次握手**：建立连接（SYN→SYN+ACK→ACK）  
**四次挥手**：断开连接（FIN→ACK→FIN→ACK）

---

### 题 62：RPC 框架了解吗

**答案：**

**RPC** = 远程过程调用（像调用本地方法一样调用远程服务）

**核心组件：**
- Client Stub（客户端代理）
- Server Stub（服务端代理）
- 序列化器（Protobuf/JSON）
- 传输层（Netty/TCP）
- 注册中心（ZooKeeper/Nacos）

**主流框架：**
- **Dubbo**（阿里，国内最流行）
- **gRPC**（Google，跨语言）
- **Thrift**（Facebook）
- **Spring Cloud**（微服务全家桶）

**RPC vs REST：** RPC 性能高（二进制 + 长连接），REST 可读性好（JSON+HTTP）

---

### 题 63：JDK 1.8 有哪些新特性

**答案：**

**8 大核心特性：**
1. **Lambda 表达式**：`(params) -> { body }`
2. **Stream API**：流式处理集合（filter/map/collect）
3. **函数式接口**：Predicate、Function、Consumer、Supplier
4. **方法引用**：`类名::方法名`
5. **Optional 类**：避免空指针
6. **新日期 API**：LocalDate/LocalDateTime（线程安全）
7. **默认方法**：interface 的 default 方法
8. **重复注解**：@Repeatable

**记忆口诀**："Lam 流函选日默重"

---

*完整 63 题，持续整理中（2026-03-20 更新）*
