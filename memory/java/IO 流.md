# Java IO 流 - 知识点笔记

> 来源：01-Java 基础 - 面渣逆袭 V2.1.pdf (No.68-78/95)  
> 创建时间：2026-03-09  
> 第 1 次 PDF 提取：2026-03-09  
> 最后复习：待测试  
> 掌握度：⏳ 待测试

---

## 1. IO 流的分类 (题 44)

### 四个划分维度

#### 维度 1：按数据流方向

| 类型 | 说明 | 举例 |
|------|------|------|
| **输入流 (Input Stream)** | 从源读取数据到程序 | FileInputStream、BufferedReader |
| **输出流 (Output Stream)** | 从程序写出到目的地 | FileOutputStream、PrintWriter |

#### 维度 2：按处理数据单位

| 类型 | 说明 | 适用场景 | 举例 |
|------|------|----------|------|
| **字节流** | 以字节为单位读写 | 二进制数据（音频、图像、视频） | FileInputStream、FileOutputStream |
| **字符流** | 以字符为单位读写 | 文本数据 | FileReader、BufferedReader |

#### 维度 3：按功能

| 类型 | 说明 | 举例 |
|------|------|------|
| **节点流** | 直接与数据源/目的地相连 | FileInputStream、FileOutputStream |
| **处理流** | 对已存在的流进行包装 | BufferedInputStream、BufferedOutputStream |
| **管道流** | 用于线程间数据传输 | PipedInputStream、PipedOutputStream |

#### 维度 4：按阻塞方式（IO 模型）

| 类型 | 阻塞方式 | 适用场景 |
|------|---------|----------|
| **BIO** | 阻塞式 IO | 连接数较少 |
| **NIO** | 非阻塞 IO | 连接数多、时间短 |
| **AIO** | 异步 IO | 连接数多、时间长 |

### IO 流用到的设计模式

**装饰器模式**：处理流（如 BufferedInputStream）对节点流进行包装，增强功能。

---

## 2. 字节流 vs 字符流 (题 45)

### 为什么有了字节流还要有字符流？

**原因：**
1. 字符流由 JVM 将字节转换得到，过程耗时
2. 不知道编码类型容易乱码
3. 字符流提供直接操作字符的接口，方便文本处理

### 使用场景

| 文件类型 | 推荐流类型 | 原因 |
|----------|-----------|------|
| **音频、图片、视频** | 字节流 | 二进制数据 |
| **文本文件** | 字符流 | 方便字符处理 |

### 文本和视频的存储形式

**物理存储：** 文本和视频都是以**字节流**形式存储

**区别：** Java 代码解释和处理方式不同
- 文本：作为编码后的字符（字符流）
- 视频：作为二进制数据（字节流）

**实际应用（技术派项目）：**
- 文本（文章、教程）：存储在数据库
- 视频、图片：存储在 OSS

---

## 3. BIO、NIO、AIO 区别 (题 46)

### 三种 IO 模型对比

| 特性 | BIO | NIO | AIO |
|------|-----|-----|-----|
| **全称** | Blocking IO | Non-blocking IO | Asynchronous IO |
| **阻塞方式** | 阻塞 | 非阻塞 | 异步 |
| **引入版本** | JDK 1.0 | JDK 1.4 | JDK 7 |
| **包路径** | java.io | java.nio | java.nio.channels |
| **线程模型** | 一个连接一个线程 | 一个线程处理多个连接 | 异步回调 |
| **核心组件** | Stream、Reader/Writer | Channel、Buffer、Selector | AsynchronousChannel |
| **适用场景** | 连接数较少 | 连接数多、时间短 | 连接数多、时间长 |

### BIO（传统 IO）

**特点：**
- 阻塞式 IO 模型
- 线程执行 IO 操作时被阻塞，无法处理其他任务
- 基于字节流/字符流（FileInputStream、BufferedReader）
- 基于 Socket 和 ServerSocket 进行网络通信
- 每个连接需要独立线程处理

### NIO（非阻塞 IO）

**特点：**
- 非阻塞 IO 模型
- 线程等待 IO 时可执行其他任务
- 通过 Selector 监控多个 Channel 实现多路复用
- 基于 Channel、Buffer、Selector
- 文件读写：RandomAccessFile、FileChannel、ByteBuffer
- 网络通信：SocketChannel、ServerSocketChannel

**优势：**
- 一个线程处理多个客户端连接
- 极大提高网络编程性能
- 缓冲区 Buffer 提升 IO 操作效率

**注意：** "旧"的 IO 包已用 NIO 重新实现，文件读写时 NIO 无法体现比 BIO 更可靠的性能，优势主要在网络编程。

### AIO（异步 IO）

**特点：**
- 异步 IO 模型
- 线程发起 IO 请求后立即返回
- IO 操作完成时通过回调函数通知线程
- 引入异步通道概念（AsynchronousFileChannel、AsynchronousSocketChannel）

**示例：**
```java
AsynchronousFileChannel fileChannel = AsynchronousFileChannel.open(
    Paths.get("test.txt"), StandardOpenOption.READ);
ByteBuffer buffer = ByteBuffer.allocate(1024);
Future<Integer> result = fileChannel.read(buffer, 0);
while (!result.isDone()) {
    // do something
}
```

---

## 4. 序列化与反序列化 (题 47)

### 基本概念

| 概念 | 说明 |
|------|------|
| **序列化** | 将对象转换为字节流（保存到文件、数据库或网络传输） |
| **反序列化** | 将字节流转换回对象 |

### Serializable 接口

**作用：** 标记一个类可以被序列化

```java
public class Person implements Serializable {
    private String name;
    private int age;
    // 省略 getter 和 setter
}
```

### serialVersionUID

**作用：** 标识类版本的唯一标识符，确保序列化和反序列化版本兼容

```java
public class MyClass implements Serializable {
    private static final long serialVersionUID = 1L;
    private String name;
    private int age;
}
```

**规则：**
- 设置为 1L 是省事做法（IDEA 可自动生成）
- 不显式声明：JVM 根据类详细信息自动生成
- 类结构变化时，自动生成的 serialVersionUID 会变化，导致反序列化失败
- **建议：** 显式声明 serialVersionUID

### transient 关键字

**作用：** 标记不想序列化的变量

```java
public class Person implements Serializable {
    private String name;
    private transient int age;  // 不会被序列化
}
```

### 序列化特点

**静态变量不序列化：**
- 序列化只保存对象状态
- 静态变量属于类，不属于对象

### 序列化过程

```java
// 1. 实现 Serializable 接口
public class Person implements Serializable {
    private String name;
    private int age;
}

// 2. 创建 ObjectOutputStream
ObjectOutputStream out = new ObjectOutputStream(
    new FileOutputStream("person.ser"));

// 3. 写入对象
Person person = new Person("沉默王二", 18);
out.writeObject(person);
```

---

## 5. 序列化方式 (题 48)

### 三种常见序列化方式

| 方式 | 说明 | 特点 | 常用工具 |
|------|------|------|----------|
| **Java 原生序列化** | 通过 Java 原生流转化 | 简单但效率低 | ObjectOutputStream/ObjectInputStream |
| **JSON 序列化** | 转化为 JSON 格式 | 最常用，可读性好 | Jackson（ObjectMapper） |
| **ProtoBuff 序列化** | 结构化数据存储格式 | 轻便高效，压缩率高 | Google ProtoBuff |

---

## 6. Socket 网络套接字 (题 49)

### 基本概念

**Socket：** 网络通信的基础，表示两台设备通信的一个端点

**用途：** 建立 TCP 或 UDP 连接，实现进程间网络通信

### TCP 客户端示例

```java
class TcpClient {
    public static void main(String[] args) throws IOException {
        Socket socket = new Socket("127.0.0.1", 8080);  // 连接服务器
        BufferedReader in = new BufferedReader(
            new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        
        out.println("Hello, Server!");  // 发送消息
        System.out.println("Server response: " + in.readLine());  // 接收响应
        
        socket.close();
    }
}
```

### TCP 服务端示例

```java
class TcpServer {
    public static void main(String[] args) throws IOException {
        ServerSocket serverSocket = new ServerSocket(8080);  // 创建服务端 Socket
        System.out.println("Server started, waiting for connection...");
        Socket socket = serverSocket.accept();  // 等待客户端连接
        System.out.println("Client connected: " + socket.getInetAddress());
        
        BufferedReader in = new BufferedReader(
            new InputStreamReader(socket.getInputStream()));
        PrintWriter out = new PrintWriter(socket.getOutputStream(), true);
        
        String message;
        while ((message = in.readLine()) != null) {
            System.out.println("Received: " + message);
            out.println("Echo: " + message);  // 回送消息
        }
        
        socket.close();
        serverSocket.close();
    }
}
```

---

## 7. 面试原题收录

| 公司 | 面试题目 | 来源 |
|------|----------|------|
| 美团一面 | Java IO 流如何划分？ | 题 44 |
| 华为一面 | Java 缓冲区溢出，如何预防 | 题 44 |
| 国企面试 | 文本存储是字节流还是字符流，视频文件呢？ | 题 45 |
| 比亚迪一面 | BIO NIO 的区别 | 题 46 |
| 美团一面 | BIO、NIO、AIO 的区别？ | 题 46 |
| 360 一面 | 说一下阻塞非阻塞 IO | 题 46 |
| 阿里云 | 介绍 NIO BIO AIO | 题 46 |
| 京东 | 用过序列化和反序列化吗？ | 题 47 |
| 美团 AI | 了解 java 的序列化和反序列化吗？ | 题 47 |
| vivo 一面 | 什么是序列化，什么是反序列化 | 题 47 |

---

## 8. 复习记录

| 日期 | 复习方式 | 掌握度 | 备注 |
|------|---------|--------|------|
| 2026-03-09 | PDF 讲解 + 笔记创建 | ⏳ 待测试 | 第 1 次复习 |

---

*本笔记由 OpenClaw 自动维护，每次复习后更新*
