# JVM 篇 - 完整面试题库（含答案）

> 来源：面渣逆袭 JVM 篇 V2.1
> 整理时间：2026-03-16 22:37:33
> 题数：60 题
> 状态：✅ 答案已补充 + 清理

---

## 1. ⼀、引⾔

### 题1：什么是 JVM?

**答案：**

JVM，也就是 Java 虚拟机，它是 Java 实现跨平台的基⽯。
程序运⾏之前，需要先通过编译器将 Java 源代码⽂件编译成 Java 字节码⽂件；
程序运⾏时，JVM 会对字节码⽂件进⾏逐⾏解释，翻译成机器码指令，并交给对应的操作系统去执⾏。
这样就实现了 Java ⼀次编译，处处运⾏的特性。
说说 JVM 的其他特性？
①、JVM 可以⾃动管理内存，通过垃圾回收器回收不再使⽤的对象并释放内存空间。
②、JVM 包含⼀个即时编译器 JIT，它可以在运⾏时将热点代码缓存到 codeCache 中，下次执⾏的时候不⽤再⼀⾏
⼀⾏的解释，⽽是直接执⾏缓存后的机器码，执⾏效率会⼤幅提⾼。
③、任何可以通过 Java 编译的语⾔，⽐如说 Groovy、Kotlin、Scala 等，都可以在 JVM 上运⾏。
为什么要学习 JVM？
学习 JVM 可以帮助我们开发者更好地优化程序性能、避免内存问题。
⽐如说了解 JVM 的内存模型和垃圾回收机制，可以帮助我们更合理地配置内存、减少 GC 停顿。
⽐如说掌握 JVM 的类加载机制可以帮助我们排查类加载冲突或异常。
再⽐如说，JVM 还提供了很多调试和监控⼯具，可以帮助我们分析内存和线程的使⽤情况，从⽽解决内存溢出内存

---

## 2. ⼆、内存管理

### 题1：Java ⾯试指南（付费）收录的字节跳动同学 20 测开⼀⾯的原题：了解过 JVM 么？讲⼀下 JVM 的特性

**答案：**

2.说说 JVM 的组织架构（补充）
增补于 2024 年 03 ⽉ 08 ⽇。
JVM ⼤致可以划分为三个部分：类加载器、运⾏时数据区和执⾏引擎。
① 类加载器，负责从⽂件系统、⽹络或其他来源加载 Class ⽂件，将 Class ⽂件中的⼆进制数据读⼊到内存当中。
② 运⾏时数据区，JVM 在执⾏ Java 程序时，需要在内存中分配空间来处理各种数据，这些内存区域按照 Java 虚拟
机规范可以划分为⽅法区、堆、虚拟机栈、程序计数器和本地⽅法栈。
③ 执⾏引擎，也是 JVM 的⼼脏，负责执⾏字节码。它包括⼀个虚拟处理器、即时编译器 JIT 和垃圾回收器。
能说⼀下 JVM 的内存区域吗？
按照 Java 虚拟机规范，JVM 的内存区域可以细分为程序计数器、虚拟机栈、本地⽅法栈、堆和⽅法区。
其中⽅法区和堆是线程共享的，虚拟机栈、本地⽅法栈和程序计数器是线程私有的。
程序计数器也被称为 PC 寄存器，是⼀块较⼩的内存空间。它可以看作是当前线程所执⾏的字节码⾏号指示器。
介绍⼀下 Java 虚拟机栈？
Java 虚拟机栈的⽣命周期与线程相同。
当线程执⾏⼀个⽅法时，会创建⼀个对应的栈帧，⽤于存储局部变量表、操作数栈、动态链接、⽅法出⼝等信息，
然后栈帧会被压⼊虚拟机栈中。当⽅法执⾏完毕后，栈帧会从虚拟机栈中移除。
⼀个什么都没有的空⽅法，空的参数都没有，那局部变量表⾥有没有变量？
对于静态⽅法，由于不需要访问实例对象 this，因此在局部变量表中不会有任何变量。
对于⾮静态⽅法，即使是⼀个完全空的⽅法，局部变量表中也会有⼀个⽤于存储 this 引⽤的变量。this 引⽤指向当
前实例对象，在⽅法调⽤时被隐式传⼊。
⽐如说有这样⼀段代码：
⽤ javap -v VarDemo1  命令查看编译后的字节码，就可以在 emptyMethod 中看到这样的内容：
这⾥的 locals=1  表示局部变量表有⼀个变量，即 this，Slot 0 位置存储了 this 引⽤。
⽽在静态⽅法 staticEmptyMethod 中，你会看到这样的内容：
public class VarDemo1 {
public void emptyMethod() {
public static void staticEmptyMethod() {
这⾥的 locals=0 表示局部变量表为空，因为静态⽅法属于类级别⽅法，不需要 this 引⽤，也就没有局部变量。
本地⽅法栈与虚拟机栈相似，区别在于虚拟机栈是为 JVM 执⾏ Java 编写的⽅法服务的，⽽本地⽅法栈是为 Java 调
⽤本地 native ⽅法服务的，通常由 C/C++ 编写。
在本地⽅法栈中，主要存放了 native ⽅法的局部变量、动态链接和⽅法出⼝等信息。当⼀个 Java 程序调⽤⼀个
native ⽅法时，JVM 会切换到本地⽅法栈来执⾏这个⽅法。
介绍⼀下本地⽅法栈的运⾏场景？
当 Java 应⽤需要与操作系统底层或硬件交互时，通常会⽤到本地⽅法栈。
⽐如调⽤操作系统的特定功能，如内存管理、⽂件操作、系统时间、系统调⽤等。
⽐如说获取系统时间的 System.currentTimeMillis()  ⽅法就是调⽤本地⽅法，来获取操作系统当前时间的。
再⽐如 JVM ⾃身的⼀些底层功能也需要通过本地⽅法来实现。像 Object 类中的 hashCode()  ⽅法、clone()  ⽅
native ⽅法解释⼀下？
native ⽅法是在 Java 中通过 native 关键字声明的，⽤于调⽤⾮ Java 语⾔，如 C/C++ 编写的代码。Java 可以通过
JNI，也就是 Java Native Interface 与底层系统、硬件设备、或者本地库进⾏交互。
介绍⼀下 Java 堆？
堆是 JVM 中最⼤的⼀块内存区域，被所有线程共享，在 JVM 启动时创建，主要⽤来存储 new 出来的对象。
Java 中“⼏乎”所有的对象都会在堆中分配，堆也是垃圾收集器管理的⽬标区域。
从内存回收的⻆度来看，由于垃圾收集器⼤部分都是基于分代收集理论设计的，所以堆⼜被细分为新⽣代、⽼年
代、Eden空间、From Survivor空间、To Survivor空间等。
随着 JIT 编译器的发展和逃逸技术的逐渐成熟，“所有的对象都会分配到堆上”就不再那么绝对了。
从 JDK 7 开始，JVM 默认开启了逃逸分析，意味着如果某些⽅法中的对象引⽤没有被返回或者没有在⽅法体外使
⽤，也就是未逃逸出去，那么对象可以直接在栈上分配内存。
堆属于线程共享的内存区域，⼏乎所有 new 出来的对象都会堆上分配，⽣命周期不由单个⽅法调⽤所决定，可以
在⽅法调⽤结束后继续存在，直到不再被任何变量引⽤，最后被垃圾收集器回收。
栈属于线程私有的内存区域，主要存储局部变量、⽅法参数、对象引⽤等，通常随着⽅法调⽤的结束⽽⾃动释放，
不需要垃圾收集器处理。
⽅法区并不真实存在，属于 Java 虚拟机规范中的⼀个逻辑概念，⽤于存储已被 JVM 加载的类信息、常量、静态变
量、即时编译器编译后的代码缓存等。
在 HotSpot 虚拟机中，⽅法区的实现称为永久代 PermGen，但在 Java 8 及之后的版本中，已经被元空间
Metaspace 所替代。
变量存在堆栈的什么位置？
对于局部变量，它存储在当前⽅法栈帧中的局部变量表中。当⽅法执⾏完毕，栈帧被回收，局部变量也会被释放。
public void method() {
int localVar = 100;  // 局部变量，存储在栈帧中的局部变量表⾥
对于静态变量来说，它存储在 Java 虚拟机规范中的⽅法区中，在 Java 7 中是永久带，在 Java8 及以后 是元空间。

---

### 题2：Java ⾯试指南（付费）收录的美团⾯经同学 2 Java 后端技术⼀⾯⾯试原题：JVM 内存结构了解吗？

**答案：**

表除了栈帧还有什么？⼀个什么都没有的空⽅法，完全空的参数什么都没有，那局部变量表⾥有没有变
景，Native⽅法解释⼀下

---

### 题3：Java ⾯试指南（付费）收录的腾讯⾯经同学 29 Java 后端⼀⾯原题：new⼀个对象存放在哪⾥？（运⾏

**答案：**

时数据区），局部变量存在JVM哪⾥

---

### 题4：说⼀下 JDK 1.6、1.7、1.8 内存区域的变化？

**答案：**

JDK 1.6 使⽤永久代来实现⽅法区：
public class StaticVarDemo {
public static int staticVar = 100;  // 静态变量，存储在⽅法区中
JDK 1.7 时仍然是永久带，但发⽣了⼀些细微变化，⽐如将字符串常量池、静态变量存放到了堆上。
在 JDK 1.8 时，直接在内存中划出了⼀块区域，叫元空间，来取代之前放在 JVM 内存中的永久代，并将运⾏时常量
池、类常量池都移动到了元空间。

---

### 题5：为什么使⽤元空间替代永久代？

**答案：**

客观上，永久代会导致 Java 应⽤程序更容易出现内存溢出的问题，因为它要受到 JVM 内存⼤⼩的限制。
HotSpot 虚拟机的永久代⼤⼩可以通过 -XX：MaxPermSize  参数来设置，32 位机器默认的⼤⼩为 64M，64 位的
⽽ J9 和 JRockit 虚拟机就不存在这种限制，只要没有触碰到进程可⽤的内存上限，例如 32 位系统中的 4GB 限制，
主观上，当 Oracle 收购 BEA 获得了 JRockit 的所有权后，就准备把 JRockit 中的优秀功能移植到 HotSpot 中。
如 Java Mission Control 管理⼯具。
但因为两个虚拟机对⽅法区实现有差异，导致这项⼯作遇到了很多阻⼒。
考虑到 HotSpot 虚拟机未来的发展，JDK 6 的时候，开发团队就打算放弃永久代了。
JDK 7 的时候，前进了⼀⼩步，把原本放在永久代的字符串常量池、静态变量等移动到了堆中。
JDK 8 就终于完成了这项移出⼯作，这样的好处就是，元空间的⼤⼩不再受到 JVM 内存的限制，⽽是可以像 J9 和
JRockit 那样，只要系统内存⾜够，就可以⼀直⽤。
对象创建的过程了解吗？
当我们使⽤ new 关键字创建⼀个对象时，JVM ⾸先会检查 new 指令的参数是否能在常量池中定位到类的符号引
⽤，然后检查这个符号引⽤代表的类是否已被加载、解析和初始化。如果没有，就先执⾏类加载。
如果已经加载，JVM 会为对象分配内存完成初始化，⽐如数值类型的成员变量初始值是 0，布尔类型是 false，对
接下来会设置对象头，⾥⾯包含了对象是哪个类的实例、对象的哈希码、对象的 GC 分代年龄等信息。
最后，JVM 会执⾏构造⽅法 <init>  完成赋值操作，将成员变量赋值为预期的值，⽐如 int age = 18 ，这样⼀
对象的销毁过程了解吗？
当对象不再被任何引⽤指向时，就会变成垃圾。垃圾收集器会通过可达性分析算法判断对象是否存活，如果对象不
垃圾收集器通过标记清除、标记复制、标记整理等算法来回收内存，将对象占⽤的内存空间释放出来。
可以通过 java -XX:+PrintCommandLineFlags -version  和 java -XX:+PrintGCDetails -version  命令查
看 JVM 的 GC 收集器。
-XX:+UseSerialGC
Parallel Scavenge
-XX:+UseParallelGC -XX:-UseParallelOldGC
Parallel Scavenge
Parallel Old
-XX:+UseParallelGC -XX:+UseParallelOldGC
Parallel New
-XX:+UseParNewGC -XX:+UseConcMarkSweepGC
-XX:+UseG1GC
可以看到，我本机安装的 JDK 8 默认使⽤的是 Parallel Scavenge + Parallel Old 。
不同参数代表对应的垃圾收集器表单：

---

### 题6：Java ⾯试指南（付费）收录的美团⾯经同学 2 Java 后端技术⼀⾯⾯试原题：说说创建对象的流程？

**答案：**

何分配的，（类加载和对象创建过程，CMS，G1 内存清理和分配）

---

### 题7：堆内存是如何分配的？

**答案：**

在堆中为对象分配内存时，主要使⽤两种策略：指针碰撞和空闲列表。
指针碰撞适⽤于管理简单、碎⽚化较少的内存区域，如年轻代；⽽空闲列表适⽤于内存碎⽚化较严重或对象⼤⼩差
异较⼤的场景如⽼年代。
假设堆内存是⼀个连续的空间，分为两个部分，⼀部分是已经被使⽤的内存，另⼀部分是未被使⽤的内存。
在分配内存时，Java 虚拟机会维护⼀个指针，指向下⼀个可⽤的内存地址，每次分配内存时，只需要将指针向后移
动⼀段距离，如果没有发⽣碰撞，就将这段内存分配给对象实例。
JVM 维护⼀个列表，记录堆中所有未占⽤的内存块，每个内存块都记录有⼤⼩和地址信息。
当有新的对象请求内存时，JVM 会遍历空闲列表，寻找⾜够⼤的空间来存放新对象。
分配后，如果选中的内存块未被完全利⽤，剩余的部分会作为⼀个新的内存块加⼊到空闲列表中。
何分配的，（类加载和对象创建过程，CMS，G1 内存清理和分配）
memo：2025 年 1 ⽉ 10 ⽇修改到此

---

### 题8：new 对象时，堆会发⽣抢占吗？

**答案：**

new 对象时，指针会向右移动⼀个对象⼤⼩的距离，假如⼀个线程 A 正在给字符串对象 s 分配内存，另外⼀个线
程 B 同时为 ArrayList 对象 l 分配内存，两个线程就发⽣了抢占。
JVM 怎么解决堆内存分配的竞争问题？
为了解决堆内存分配的竞争问题，JVM 为每个线程保留了⼀⼩块内存空间，被称为 TLAB，也就是线程本地分配缓
冲区，⽤于存放该线程分配的对象。
当线程需要分配对象时，直接从 TLAB 中分配。只有当 TLAB ⽤尽或对象太⼤需要直接在堆中分配时，才会使⽤全
这⾥简单测试⼀下 TLAB。
可以通过 java -XX:+PrintFlagsFinal -version | grep TLAB  命令查看当前 JVM 是否开启了 TLAB。
如果开启了 TLAB，会看到类似以下的输出，其中 bool UseTLAB 的值为 true。
我们编写⼀个简单的测试类，创建⼤量对象并强制触发垃圾回收，查看 TLAB 的使⽤情况。
在 VM 参数中添加 -XX:+UseTLAB -XX:+PrintTLAB -XX:+PrintGCDetails -XX:+PrintGCDateStamps ，运⾏
后可以看到这样的内容：
class TLABDemo {
public static void main(String[] args) {
for (int i = 0; i < 10_000_000; i++) {
allocate(); // 创建⼤量对象
System.gc(); // 强制触发垃圾回收
private static void allocate() {
// ⼩对象分配，通常会使⽤ TLAB
byte[] bytes = new byte[64];
waste：未使⽤的 TLAB 空间。
alloc：分配到 TLAB 的空间。
refills：TLAB 被重新填充的次数。
可以看到，当前线程的 TLAB ⽬标⼤⼩为 10,496 KB（desired_size: 10496KB ）；未发⽣慢分配（slow
allocs: 0 ）；分配效率直接拉满（alloc: 1.00000 52494KB ）。
当使⽤ -XX:-UseTLAB -XX:+PrintGCDetails  关闭 TLAB 时，会看到类似以下的输出：
直接出现了两次 GC，因为没有 TLAB，Eden 区更快被填满，导致年轻代 GC。年轻代 GC 频繁触发，⼀部分⻓⽣
命周期对象被晋升到⽼年代，间接导致⽼年代 GC 触发。

---

### 题9：能说⼀下对象的内存布局吗？

**答案：**

对象的内存布局是由 Java 虚拟机规范定义的，但具体的实现细节各有不同，如 HotSpot 和 OpenJ9 就不⼀样。
就拿我们常⽤的 HotSpot 来说吧。
对象在内存中包括三部分：对象头、实例数据和对⻬填充。
对象头是对象存储在内存中的元信息，包含了Mark Word、类型指针等信息。
Mark Word 存储了对象的运⾏时状态信息，包括锁、哈希值、GC 标记等。在 64 位操作系统下占 8 个字节，32
位操作系统下占 4 个字节。
类型指针指向对象所属类的元数据，也就是 Class 对象，⽤来⽀持多态、⽅法调⽤等功能。
除此之外，如果对象是数组类型，还会有⼀个额外的数组⻓度字段。占 4 个字节。
类型指针可能会被压缩，以节省内存空间。⽐如说在开启压缩指针的情况下占 4 个字节，否则占 8 个字节。在 JDK
8 中，压缩指针默认是开启的。
可以通过 java -XX:+PrintFlagsFinal -version | grep UseCompressedOops  命令来查看 JVM 是否开启了压
如果压缩指针开启，输出结果中的 bool UseCompressedOops 值为 true。
实例数据是对象实际的字段值，也就是成员变量的值，按照字段在类中声明的顺序存储。
JVM 会对这些数据进⾏对⻬/重排，以提⾼内存访问速度。
由于 JVM 的内存模型要求对象的起始地址是 8 字节对⻬（64 位 JVM 中），因此对象的总⼤⼩必须是 8 字节的倍
如果对象头和实例数据的总⻓度不是 8 的倍数，JVM 会通过填充额外的字节来对⻬。
⽐如说，如果对象头 + 实例数据 = 14 字节，则需要填充 2 个字节，使总⻓度变为 16 字节。
为什么⾮要进⾏ 8 字节对⻬呢？
因为 CPU 进⾏内存访问时，⼀次寻址的指针⼤⼩是 8 字节，正好是 L1 缓存⾏的⼤⼩。如果不进⾏内存对⻬，则可
能出现跨缓存⾏访问，导致额外的缓存⾏加载，CPU 的访问效率就会降低。
⽐如说上图中 obj1 占 6 个字节，由于没有对⻬，导致这⼀⾏缓存中多了 2 个字节 obj2 的数据，当 CPU 访问 obj2
的时候，就会导致缓存⾏刷新。
也就说，8 字节对⻬，是为了效率的提⾼，以空间换时间的⼀种⽅案。
class ObjectDemo {
String name;
new Object() 对象的内存⼤⼩是多少？
⼀般来说，⽬前的操作系统都是 64 位的，并且 JDK 8 中的压缩指针是默认开启的，因此在 64 位的 JVM 上，new
Object() 的⼤⼩是 16 字节（12 字节的对象头 + 4 字节的对⻬填充）。
对象头的⼤⼩是固定的，在 32 位 JVM 上是 8 字节，在 64 位 JVM 上是 16 字节；如果开启了压缩指针，就是 12
实例数据的⼤⼩取决于对象的成员变量和它们的类型。对于new Object() 来说，由于默认没有成员变量，因此我
们可以认为此时的实例数据⼤⼩是 0。
假如 MyObject 对象有三个成员变量，分别是 int、long 和 byte 类型，那么它们占⽤的内存⼤⼩分别是 4 字节、8
考虑到对⻬填充，MyObject 对象的总⼤⼩为 12（对象头） + 4（a） + 8（b） + 1（c） + 7（填充） = 32 字节。
⽤过 JOL 查看对象的内存布局吗？
JOL 是⼀款分析 JVM 对象布局的⼯具。
第⼀步，在 pom.xml 中引⼊ JOL 依赖：
第⼆步，使⽤ JOL 编写代码示例：
第三步，运⾏代码，查看输出结果：
class MyObject {
int a;        // 4 字节
long b;       // 8 字节
byte c;       // 1 字节
<dependency>
<groupId>org.openjdk.jol</groupId>
<artifactId>jol-core</artifactId>
<version>0.9</version>
</dependency>
public class JOLSample {
public static void main(String[] args) {
// 打印JVM详细信息（可选）
System.out.println(VM.current().details());
// 创建Object实例
Object obj = new Object();
// 打印Object实例的内存布局
String layout = ClassLayout.parseInstance(obj).toPrintable();
System.out.println(layout);
可以看到有 OFFSET、SIZE、TYPE DESCRIPTION、VALUE 这⼏个信息。
OFFSET：偏移地址，单位字节；
SIZE：占⽤的内存⼤⼩，单位字节；
TYPE DESCRIPTION：类型描述，其中 object header 为对象头；
VALUE：对应内存中当前存储的值，⼆进制 32 位；
从上⾯的结果能看到，对象头是 12 个字节，还有 4 个字节的 padding，new Object()  ⼀共 16 个字节。
对象的引⽤⼤⼩了解吗？
在 64 位 JVM 上，未开启压缩指针时，对象引⽤占⽤ 8 字节；开启压缩指针时，对象引⽤会被压缩到 4 字节。
HotSpot 虚拟机默认是开启压缩指针的。
运⾏代码，查看输出结果：
class ReferenceSizeExample {
private static class ReferenceHolder {
Object reference;
public static void main(String[] args) {
System.out.println(VM.current().details());
System.out.println(ClassLayout.parseClass(ReferenceHolder.class).toPrintable());
ReferenceHolder.reference 的⼤⼩为 4 字节。
memo：2025 年 1 ⽉ 11 ⽇修改到此

---

### 题10：JVM 怎么访问对象的？

**答案：**

主流的⽅式有两种：句柄和直接指针。
两种⽅式的区别在于，句柄是通过⼀个中间的句柄表来定位对象的，⽽直接指针则是通过引⽤直接指向对象的内存
优点是，对象被移动时只需要修改句柄表中的指针，⽽不需要修改对象引⽤本身。
在直接指针访问中，引⽤直接存储对象的内存地址；对象的实例数据和类型信息都存储在堆中固定的内存区域。
优点是访问速度更快，因为少了⼀次句柄的寻址操作。缺点是如果对象在内存中移动，引⽤需要更新为新的地址。
HotSpot 虚拟机主要使⽤直接指针来进⾏对象访问。

---

### 题11：说⼀下对象有哪⼏种引⽤？

**答案：**

四种，分别是强引⽤、软引⽤、弱引⽤和虚引⽤。
强引⽤是 Java 中最常⻅的引⽤类型。使⽤ new 关键字赋值的引⽤就是强引⽤，只要强引⽤关联着对象，垃圾收集
器就不会回收这部分对象，即使内存不⾜。
软引⽤于描述⼀些⾮必须对象，通过 SoftReference 类实现。软引⽤的对象在内存不⾜时会被回收。
弱引⽤⽤于描述⼀些短⽣命周期的⾮必须对象，如 ThreadLocal 中的 Entry，就是通过 WeakReference 类实现
的。弱引⽤的对象会在下⼀次垃圾回收时会被回收，不论内存是否充⾜。
// str 就是⼀个强引⽤
String str = new String("沉默王⼆");
// softRef 就是⼀个软引⽤
SoftReference<String> softRef = new SoftReference<>(new String("沉默王⼆"));
虚引⽤主要⽤来跟踪对象被垃圾回收的过程，通过 PhantomReference 类实现。虚引⽤的对象在任何时候都可能

---

### 题12：Java 堆的内存分区了解吗？

**答案：**

了解。Java 堆被划分为新⽣代和⽼年代两个区域。
新⽣代⼜被划分为 Eden 空间和两个 Survivor 空间（From 和 To）。
新创建的对象会被分配到 Eden 空间。当 Eden 区填满时，会触发⼀次 Minor GC，清除不再使⽤的对象。存活下
来的对象会从 Eden 区移动到 Survivor 区。
对象在新⽣代中经历多次 GC 后，如果仍然存活，会被移动到⽼年代。当⽼年代内存不⾜时，会触发 Major GC，
对整个堆进⾏垃圾回收。
static class Entry extends WeakReference<ThreadLocal<?>> {
/** The value associated with this ThreadLocal. */
Object value;
Entry(ThreadLocal<?> k, Object v) {
// phantomRef 就是⼀个虚引⽤
PhantomReference<String> phantomRef = new PhantomReference<>(new String("沉默王⼆"), new
ReferenceQueue<>());

---

### 题13：说⼀下新⽣代的区域划分？

**答案：**

新⽣代的垃圾收集主要采⽤标记-复制算法，因为新⽣代的存活对象⽐较少，每次复制少量的存活对象效率⽐较
基于这种算法，虚拟机将内存分为⼀块较⼤的 Eden 空间和两块较⼩的 Survivor 空间，每次分配内存只使⽤ Eden
和其中⼀块 Survivor。发⽣垃圾收集时，将 Eden 和 Survivor 中仍然存活的对象⼀次性复制到另外⼀块 Survivor
空间上，然后直接清理掉 Eden 和已⽤过的那块 Survivor 空间。默认 Eden 和 Survivor 的⼤⼩⽐例是 8∶1。
对象什么时候会进⼊⽼年代？
对象通常会在年轻代中分配，随着时间的推移和垃圾收集的进程，某些满⾜条件的对象会进⼊到⽼年代中，如⻓期
⻓期存活的对象如何判断？
JVM 会为对象维护⼀个“年龄”计数器，记录对象在新⽣代中经历 Minor GC 的次数。每次 GC 未被回收的对象，其
当超过⼀个特定阈值，默认值是 15，就会被认为⽼对象了，需要重点关照。这个年龄阈值可以通过 JVM 参数-
XX:MaxTenuringThreshold 来设置。
可以通过 jinfo -flag MaxTenuringThreshold $(jps | grep -i nacos | awk '{print $1}')  来查看当前
1. 如果应⽤中的对象存活时间较短，可以适当调⼤这个值，让对象在新⽣代多待⼀会⼉
2. 如果对象存活时间较⻓，可以适当调⼩这个值，让对象更快进⼊⽼年代，减少在新⽣代的复制次数
⼤对象是指占⽤内存较⼤的对象，如⼤数组、⻓字符串等。
其⼤⼩由 JVM 参数 -XX:PretenureSizeThreshold  控制，但在 JDK 8 中，默认值为 0，也就是说默认情况下，对
象仅根据 GC 存活的次数来判断是否进⼊⽼年代。
G1 垃圾收集器中，⼤对象会直接分配到 HUMONGOUS 区域。当对象⼤⼩超过⼀个 Region 容量的 50% 时，会被
Region 的⼤⼩可以通过 JVM 参数 -XX:G1HeapRegionSize  来设置，默认情况下从 1MB 到 32MB 不等，会根据
可以通过 java -XX:+UseG1GC -XX:+PrintGCDetails -version  查看 G1 垃圾收集器的相关信息。
int[] array = new int[1000000];
String str = new String(new char[1000000]);
从结果上来看，我本机上 G1 的堆⼤⼩为 2GB，Region 的⼤⼩为 4MB。
如果 Survivor 区中所有对象的总⼤⼩超过了⼀定⽐例，通常是 Survivor 区的⼀半，那么年龄较⼩的对象也可能会
这是因为如果年龄较⼩的对象在 Survivor 区中占⽤了较⼤的空间，会导致 Survivor 区中的对象复制次数增多，影
memo：2025 年 1 ⽉ 13 ⽇修改到此

---

### 题14：STW 了解吗？

**答案：**

JVM 进⾏垃圾回收的过程中，会涉及到对象的移动，为了保证对象引⽤在移动过程中不被修改，必须暂停所有的⽤
户线程，像这样的停顿，我们称之为Stop The World 。简称 STW。
JVM 会使⽤⼀个名为安全点（Safe Point）的机制来确保线程能够被安全地暂停，其过程包括四个步骤：
JVM 发出暂停信号；
线程执⾏到安全点后，挂起⾃身并等待垃圾收集完成；
垃圾回收器完成 GC 操作；
安全点是 JVM 的⼀种机制，常⽤于垃圾回收的 STW 操作，⽤于让线程在执⾏到某些特定位置时，可以被安全地暂
通常位于⽅法调⽤、循环跳转、异常处理等位置，以保证线程暂停时数据的⼀致性。
⽤个通俗的⽐喻，⽼王去拉⻋，⻋上的东⻄很重，⽼王累的汗流浃背，但是⽼王不能在上坡或者下坡时休息，只能
在平地上停下来擦擦汗，喝⼝⽔。
推荐⼤家看看这个HotSpot JVM Deep Dive - Safepoint，对 safe point 有⼀个⽐较深⼊地解释。

---

### 题15：对象⼀定分配在堆中吗？

**答案：**

默认情况下，Java 对象是在堆中分配的，但 JVM 会进⾏逃逸分析，来判断对象的⽣命周期是否只在⽅法内部，如
果是的话，这个对象可以在栈上分配。
举例来说，下⾯的代码中，对象 new Person()  的⽣命周期只在 testStackAllocation  ⽅法内部，因此 JVM 会
将这个对象分配在栈上。
逃逸分析是⼀种 JVM 优化技术，⽤来分析对象的作⽤域和⽣命周期，判断对象是否逃逸出⽅法或线程。
可以通过分析对象的引⽤流向，判断对象是否被⽅法返回、赋值到全局变量、传递到其他线程等，来确定对象是否
如果对象没有逃逸，就可以进⾏栈上分配、同步消除、标量替换等优化，以提⾼程序的性能。
可以通过 java -XX:+PrintFlagsFinal -version | grep DoEscapeAnalysis  来确认 JVM 是否开启了逃逸分
根据对象逃逸的范围，可以分为⽅法逃逸和线程逃逸。
当对象被⽅法外部的代码引⽤，⽣命周期超出了⽅法的范围，那么对象就必须分配在堆中，由垃圾收集器管理。
⽐如说 new Person()  创建的对象被返回，那么这个对象就逃逸出当前⽅法了。
public void testStackAllocation() {
Person p = new Person();  // 对象可能分配在栈上
p.name = "沉默王⼆是只狗";
p.age = 18;
System.out.println(p.name);
public Person createPerson() {
return new Person(); // 对象逃逸出⽅法
再⽐如说，对象被另外⼀个线程引⽤，⽣命周期超出了当前线程，那么对象就必须分配在堆中，并且线程之间需要
对象 new Person()  被另外⼀个线程引⽤了，发⽣了线程逃逸。
逃逸分析会带来什么好处？
第⼀，如果确定⼀个对象不会逃逸，那么就可以考虑栈上分配，对象占⽤的内存随着栈帧出栈后销毁，这样⼀来，
垃圾收集的压⼒就降低很多。
第⼆，线程同步需要加锁，加锁就要占⽤系统资源，如果逃逸分析能够确定⼀个对象不会逃逸出线程，那么这个对
象就不⽤加锁，从⽽减少线程同步的开销。
public void threadEscapeExample() {
Person p = new Person(); // 对象逃逸到另⼀个线程
new Thread(() -> {
System.out.println(p);
}).start();
第三，如果对象的字段在⽅法中独⽴使⽤，JVM 可以将对象分解为标量变量，避免对象分配。
如果 Point 对象未逃逸，JVM 可以优化为：

---

### 题16：内存溢出和内存泄漏了解吗？

**答案：**

内存溢出，俗称 OOM，是指当程序请求分配内存时，由于没有⾜够的内存空间，从⽽抛出 OutOfMemoryError。
可能是因为堆、元空间、栈或直接内存不⾜导致的。可以通过优化内存配置、减少对象分配来解决。
内存泄漏是指程序在使⽤完内存后，未能及时释放，导致占⽤的内存⽆法再被使⽤。随着时间的推移，内存泄漏会
导致可⽤内存逐渐减少，最终导致内存溢出。
内存泄漏通常是因为⻓期存活的对象持有短期存活对象的引⽤，⼜没有及时释放，从⽽导致短期存活对象⽆法被回
⽤⼀个⽐较有味道的⽐喻来形容就是，内存溢出是排队去蹲坑，发现没坑了；内存泄漏，就是有⼈占着茅坑不拉
public void scalarReplacementExample() {
Point p = new Point(1, 2);
System.out.println(p.getX() + p.getY());
System.out.println(x + y);
List<String> list = new ArrayList<>();
while (true) {
list.add("OutOfMemory".repeat(1000)); // ⽆限增加内存
class MemoryLeakExample {
private static List<Object> staticList = new ArrayList<>();
public void addObject() {
staticList.add(new Object()); // 对象不会被回收

---

### 题17：能⼿写内存溢出的例⼦吗？

**答案：**

我就拿最常⻅的堆内存溢出来完成吧，堆内存溢出通常是因为创建了⼤量的对象，且⻓时间⽆法被垃圾收集器回
很快就会发⽣内存溢出。
这就相当于⼀个房⼦⾥，不断堆积不能被回收的杂物，那么房⼦很快就会被堆满了。
也可以通过 VM 参数设置堆内存⼤⼩为 -Xmx128M ，然后运⾏程序，出现的内存溢出的时间会更快。
class HeapSpaceErrorGenerator {
public static void main(String[] args) {
// 第⼀步，创建⼀个⼤的容器
List<byte[]> bigObjects = new ArrayList<>();
// 第⼆步，循环写⼊数据
while (true) {
// 第三步，创建⼀个⼤对象，⼀个⼤约 10M 的数组
byte[] bigObject = new byte[10 * 1024 * 1024];
// 第四步，将⼤对象添加到容器中
bigObjects.add(bigObject);
} catch (OutOfMemoryError e) {
System.out.println("OutOfMemoryError 发⽣在 " + bigObjects.size() + " 对象后");
可以看到，堆内存溢出发⽣在 11 个对象后。
memo：2025 年 1 ⽉ 14 ⽇修改到此

---

### 题18：内存泄漏可能由哪些原因导致呢？

**答案：**

①、静态的集合中添加的对象越来越多，但却没有及时清理；静态变量的⽣命周期与应⽤程序相同，如果静态变量
持有对象的引⽤，这些对象将⽆法被 GC 回收。
②、单例模式下对象持有的外部引⽤⽆法及时释放；单例对象在整个应⽤程序的⽣命周期中存活，如果单例对象持
有其他对象的引⽤，这些对象将⽆法被回收。
③、数据库、IO、Socket 等连接资源没有及时关闭；
ThreadLocal 的引⽤未被清理，线程退出后仍然持有对象引⽤；在线程执⾏完后，要调⽤ ThreadLocal
的 remove ⽅法进⾏清理。

---

### 题19：有没有处理过内存泄漏问题？

**答案：**

1. ⼀次内存溢出的排查优化实战
2. JVM 性能监控⼯具之命令⾏篇
class OOM {
static List list = new ArrayList();
public void oomTests(){
Object obj = new Object();
list.add(obj);
class Singleton {
private static final Singleton INSTANCE = new Singleton();
private List<Object> objects = new ArrayList<>();
public static Singleton getInstance() {
return INSTANCE;
Connection conn = null;
Class.forName("com.mysql.jdbc.Driver");
conn = DriverManager.getConnection("url", "", "");
Statement stmt = conn.createStatement();
ResultSet rs = stmt.executeQuery("....");
} catch (Exception e) {
ThreadLocal<Object> threadLocal = new ThreadLocal<>();
threadLocal.set(new Object()); // 未清理
3. JVM 性能监控⼯具之可视化篇
当时在做技术派项⽬的时候，由于 ThreadLocal 没有及时清理导致出现了内存泄漏问题。
我⽤可视化的监控⼯具 VisualVM，配合 JDK ⾃带的 jstack 等命令⾏⼯具进⾏了排查。
⼤致的过程我回想了⼀下，主要有 7 个步骤：
第⼀步，使⽤ jps -l  查看运⾏的 Java 进程 ID。
第⼆步，使⽤top -p [pid]  查看进程使⽤ CPU 和内存占⽤情况。
第三步，使⽤ top -Hp [pid]  查看进程下的所有线程占⽤ CPU 和内存情况。
第四步，抓取线程栈：jstack -F 29452 > 29452.txt ，可以多抓⼏次做个对⽐。
29452 为 pid，顺带作为⽂件名。
看看有没有线程死锁、死循环或⻓时间等待这些问题。
第五步，可以使⽤jstat -gcutil [pid] 5000 10  每隔 5 秒输出 GC 信息，输出 10 次，查看 YGC 和 Full GC
通常会出现 YGC 不增加或增加缓慢，⽽ Full GC 增加很快。
或使⽤ jstat -gccause [pid] 5000  输出 GC 摘要信息。
或使⽤ jmap -heap [pid]  查看堆的摘要信息，关注⽼年代内存使⽤是否达到阀值，若达到阀值就会执⾏ Full
如果发现 Full GC  次数太多，就很⼤概率存在内存泄漏了。
第六步，⽣成 dump  ⽂件，然后借助可视化⼯具分析哪个对象⾮常多，基本就能定位到问题根源了。
执⾏命令 jmap -dump:format=b,file=heap.hprof 10025  会输出进程 10025 的堆快照信息，保存到⽂件
heap.hprof 中。
第七步，使⽤图形化⼯具分析，如 JDK ⾃带的 VisualVM，从菜单 > ⽂件 > 装⼊ dump ⽂件。
然后在结果观察内存占⽤最多的对象，找到内存泄漏的源头。

---

### 题20：有没有处理过内存溢出问题？

**答案：**

当时在做技术派的时候，由于上传的⽂件过⼤，没有正确处理，导致⼀下⼦撑爆了内存，程序直接崩溃了。
我记得是通过导出堆转储⽂件进⾏分析发现的。
第⼀步，使⽤ jmap 命令⼿动⽣成 Heap Dump ⽂件：
然后使⽤ MAT、JProfiler 等⼯具进⾏分析，查看内存中的对象占⽤情况。
如果⽣产环境的内存还有很多空余，可以适当增⼤堆内存⼤⼩来解决，例如 -Xmx4g  参数。
或者检查代码中是否存在内存泄漏，如未关闭的资源、⻓⽣命周期的对象等。
之后，在本地进⾏压⼒测试，模拟⾼负载情况下的内存表现，确保修改有效，且没有引⼊新的问题。

---

### 题21：Java ⾯试指南（付费）收录的华为⾯经同学 9 Java 通⽤软件开发⼀⾯⾯试原题：如何排查 OOM？

**答案：**



---

### 题22：什么情况下会发⽣栈溢出？（补充）

**答案：**

2024 年 10 ⽉ 16 ⽇增补
栈溢出发⽣在程序调⽤栈的深度超过 JVM 允许的最⼤深度时。
栈溢出的本质是因为线程的栈空间不⾜，导致⽆法再为新的栈帧分配内存。
当⼀个⽅法被调⽤时，JVM 会在栈中分配⼀个栈帧，⽤于存储该⽅法的执⾏信息。如果⽅法调⽤嵌套太深，栈帧不
断压⼊栈中，最终会导致栈空间耗尽，抛出 StackOverflowError。
最常⻅的栈溢出场景就是递归调⽤，尤其是没有正确的终⽌条件下，会导致递归⽆限进⾏。
jmap -dump:format=b,file=heap.hprof <pid>
另外，如果⽅法中定义了特别⼤的局部变量，栈帧会变得很⼤，导致栈空间更容易耗尽。

---

## 3. 三、垃圾收集

### 题1：Java ⾯试指南（付费）收录的 OPPO ⾯经同学 1 ⾯试原题：什么情况下会发⽣栈溢出？

**答案：**

讲讲 JVM 的垃圾回收机制（补充）
本题是增补的内容，by 2024 年 03 ⽉ 09 ⽇；参照：深⼊理解 JVM 的垃圾回收机制
垃圾回收就是对内存堆中已经死亡的或者⻓时间没有使⽤的对象进⾏清除或回收。
JVM 在做 GC 之前，会先搞清楚什么是垃圾，什么不是垃圾，通常会通过可达性分析算法来判断对象是否存活。
class StackOverflowExample {
public static void recursiveMethod() {
// 没有终⽌条件的递归调⽤
recursiveMethod();
public static void main(String[] args) {
recursiveMethod();  // 导致栈溢出
public class LargeLocalVariables {
public static void method() {
int[] largeArray = new int[1000000];  // ⼤量局部变量
method();  // 递归调⽤
public static void main(String[] args) {
method();  // 导致栈溢出
在确定了哪些垃圾可以被回收后，垃圾收集器（如 CMS、G1、ZGC）要做的事情就是进⾏垃圾回收，可以采⽤标
记清除算法、复制算法、标记整理算法、分代收集算法等。
技术派项⽬使⽤的 JDK 8，采⽤的是 CMS 垃圾收集器。
垃圾回收的过程是什么？
Java 的垃圾回收过程主要分为标记存活对象、清除⽆⽤对象、以及内存压缩/整理三个阶段。不同的垃圾回收器在
执⾏这些步骤时会采⽤不同的策略和算法。

---

### 题2：Java ⾯试指南（付费）收录的美团⾯经同学 2 Java 后端技术⼀⾯⾯试原题：了解 GC 吗？不可达判断知

**答案：**



---

### 题3：Java ⾯试指南（付费）收录的 OPPO ⾯经同学 1 ⾯试原题：垃圾回收的过程是什么？

**答案：**

java -XX:+UseConcMarkSweepGC \
-XX:+UseParNewGC \
-XX:CMSInitiatingOccupancyFraction=75 \
-XX:+UseCMSInitiatingOccupancyOnly \
-jar your-application.jar

---

### 题4：Java ⾯试指南（付费）收录的荣耀⾯经同学 4 ⾯试原题：对垃圾回收的理解？

**答案：**



---

### 题5：Java ⾯试指南（付费）收录的腾讯⾯经同学 29 Java 后端⼀⾯原题：JVM垃圾回收机制？

**答案：**

如何判断对象仍然存活？
Java 通过可达性分析算法来判断⼀个对象是否还存活。
通过⼀组名为 “GC Roots” 的根对象，进⾏递归扫描，⽆法从根对象到达的对象就是“垃圾”，可以被回收。
这也是 G1、CMS 等主流垃圾收集器使⽤的主要算法。
每个对象有⼀个引⽤计数器，记录引⽤它的次数。当计数器为零时，对象可以被回收。
引⽤计数法⽆法解决循环引⽤的问题。例如，两个对象互相引⽤，但不再被其他对象引⽤，它们的引⽤计数都不为
做可达性分析的时候，应该有哪些前置性的操作？
在进⾏垃圾回收之前，JVM 会暂停所有正在执⾏的应⽤线程。
这是因为可达性分析过程必须确保在执⾏分析时，内存中的对象关系不会被应⽤线程修改。如果不暂停应⽤线程，
可能会出现对象引⽤的改变，导致垃圾回收过程中判断对象是否可达的结果不⼀致，从⽽引发严重的内存错误或数

---

### 题6：Java 中可作为 GC Roots 的引⽤有哪⼏种？

**答案：**

所谓的 GC Roots，就是⼀组必须活跃的引⽤，它们是程序运⾏时的起点，是⼀切引⽤链的源头。在 Java 中，GC
Roots 包括以下⼏种：
虚拟机栈中的引⽤（⽅法的参数、局部变量等）
本地⽅法栈中 JNI 的引⽤
运⾏时常量池中的常量（String 或 Class 类型）
说说虚拟机栈中的引⽤？
在 greet ⽅法中，localVar 是⼀个局部变量，存在于虚拟机栈中，可以被认为是 GC Roots。
在 greet ⽅法执⾏期间，localVar 引⽤的对象是活跃的，因为它是从 GC Roots 可达的。
当 greet ⽅法执⾏完毕后，localVar 的作⽤域结束，localVar 引⽤的 Object 对象不再由任何 GC Roots 引⽤（假设
没有其他引⽤指向这个对象），因此它将有资格作为垃圾被回收掉
说说本地⽅法栈中 JNI 的引⽤？
Java 通过 JNI 提供了⼀种机制，允许 Java 代码调⽤本地代码（通常是 C 或 C++ 编写的代码）。
当调⽤ Java ⽅法时，虚拟机会创建⼀个栈帧并压⼊虚拟机栈，⽽当它调⽤本地⽅法时，虚拟机会通过动态链接直
接调⽤指定的本地⽅法。
public class StackReference {
public void greet() {
Object localVar = new Object(); // 这⾥的 localVar 是⼀个局部变量，存在于虚拟机栈中
System.out.println(localVar.toString());
public static void main(String[] args) {
new StackReference().greet();
JNI 引⽤是在 Java 本地接⼝代码中创建的引⽤，这些引⽤可以指向 Java 堆中的对象。
在本地代码中，localRef 是对 Java 对象的⼀个 JNI 引⽤，它在本地⽅法执⾏期间保持 Java 对象活跃，可以被认为
是 GC Roots。
⼀旦 JNI ⽅法执⾏完毕，除⾮这个引⽤是全局的，否则它指向的对象将会被作为垃圾回收掉（假设没有其他地⽅再
// 假设的JNI⽅法
public native void nativeMethod();
// 假设在C/C++中实现的本地⽅法
* Class:     NativeExample
* Method:    nativeMethod
* Signature: ()V
JNIEXPORT void JNICALL Java_NativeExample_nativeMethod(JNIEnv *env, jobject thisObj) {
jobject localRef = (*env)->NewObject(env, ...); // 在本地⽅法栈中创建JNI引⽤
// localRef 引⽤的Java对象在本地⽅法执⾏期间是活跃的
StaticFieldReference 类中的 staticVar 引⽤了⼀个 Object 对象，这个引⽤存储在元空间，可以被认为是 GC
只要 StaticFieldReference 类未被卸载，staticVar 引⽤的对象都不会被垃圾回收。如果 StaticFieldReference 类被
卸载（这通常发⽣在其类加载器被垃圾回收时），那么 staticVar 引⽤的对象也将有资格被垃圾回收（如果没有其
他引⽤指向这个对象）。
说说运⾏时常量池中的常量？
在 ConstantPoolReference 中，CONSTANT_STRING 和 CONSTANT_CLASS 作为常量存储在运⾏时常量池。它们
可以⽤来作为 GC Roots。
这些常量引⽤的对象（字符串"Hello, World"和 Object.class 类对象）在常量池中，只要包含这些常量的
ConstantPoolReference 类未被卸载，这些对象就不会被垃圾回收。

---

### 题7：Java ⾯试指南（付费）收录的腾讯⾯经同学 27 云后台技术⼀⾯⾯试原题：GC Root？

**答案：**



---

### 题8：finalize()⽅法了解吗？

**答案：**

垃圾回收就是古代的秋后问斩，finalize()  就是⼑下留⼈，在⼈犯被处决之前，还要做最后⼀次审计，⻘天⼤⽼
爷会看看有没有什么冤情，需不需要⼑下留⼈。
public class StaticFieldReference {
private static Object staticVar = new Object(); // 类静态变量
public static void main(String[] args) {
System.out.println(staticVar.toString());
class ConstantPoolReference {
public static final String CONSTANT_STRING = "Hello, World"; // 常量，存在于运⾏时常量池中
public static final Class<?> CONSTANT_CLASS = Object.class; // 类类型常量
public static void main(String[] args) {
System.out.println(CONSTANT_STRING);
System.out.println(CONSTANT_CLASS.getName());
如果对象在进⾏可达性分析后发现没有与 GC Roots 相连接的引⽤链，那它将会被第⼀次标记，随后进⾏⼀次筛
筛选的条件是对象是否有必要执⾏ finalize() ⽅法。
如果对象在 finalize()  中成功拯救⾃⼰——只要重新与引⽤链上的任何⼀个对象建⽴关联即可。
譬如把⾃⼰ （this 关键字）赋值给某个类变量或者对象的成员变量，那在第⼆次标记时它就”逃过⼀劫“；但是如果
没有抓住这个机会，那么对象就真的要被回收了。
垃圾收集算法主要有三种，分别是标记-清除算法、标记-复制算法和标记-整理算法。
标记-清除算法分为两个阶段：
标记：标记所有需要回收的对象
清除：回收所有被标记的对象
优点是实现简单，缺点是回收过程中会产⽣内存碎⽚。
标记-复制算法可以解决标记-清除算法的内存碎⽚问题，因为它将内存空间划分为两块，每次只使⽤其中⼀块。当
这⼀块的内存⽤完了，就将还存活着的对象复制到另外⼀块上⾯，然后清理掉这⼀块。
缺点是浪费了⼀半的内存空间。
标记-整理算法是标记-清除复制算法的升级版，它不再划分内存空间，⽽是将存活的对象向内存的⼀端移动，然后
缺点是移动对象的成本⽐较⾼。
分代收集算法是⽬前主流的垃圾收集算法，它根据对象存活周期的不同将内存划分为⼏块，⼀般分为新⽣代和⽼年
新⽣代⽤复制算法，因为⼤部分对象⽣命周期短。⽼年代⽤标记-整理算法，因为对象存活率较⾼。
为什么要⽤分代收集呢？
分代收集算法的核⼼思想是根据对象的⽣命周期优化垃圾回收。
新⽣代的对象⽣命周期短，使⽤复制算法可以快速回收。⽼年代的对象⽣命周期⻓，使⽤标记-整理算法可以减少
标记复制的标记过程和复制过程会不会停顿？
在标记-复制算法 中，标记阶段和复制阶段都会触发STW。
标记阶段停顿是为了保证对象的引⽤关系不被修改。
复制阶段停顿是防⽌对象在复制过程中被修改。

---

### 题9：Java ⾯试指南（付费）收录的腾讯⾯经同学 27 云后台技术⼀⾯⾯试原题：回收的⽅法？分代收集算法

**答案：**

⾥⾯具体是怎么回收的？为什么要⽤分代收集呢？

---

### 题10：Java ⾯试指南（付费）收录的百度同学 4 ⾯试原题：Gc 算法有哪些?

**答案：**



---

### 题11：Minor GC、Major GC、Mixed GC、Full GC 都是什么意思？

**答案：**

Minor GC 也称为 Young GC，是指发⽣在年轻代的垃圾收集。年轻代包含 Eden 区以及两个 Survivor 区。
Major GC 也称为 Old GC，主要指的是发⽣在⽼年代的垃圾收集。是 CMS 的特有⾏为。
Mixed GC 是 G1 垃圾收集器特有的⼀种 GC 类型，它在⼀次 GC 中同时清理年轻代和部分⽼年代。
Full GC 是最彻底的垃圾收集，涉及整个 Java 堆和⽅法区。它是最耗时的 GC，通常在 JVM 压⼒很⼤时发⽣。
FULL gc怎么去清理的？
Full GC 会从 GC Root 出发，标记所有可达对象。新⽣代使⽤复制算法，清空 Eden 区。⽼年代使⽤标记-整理算
法，回收对象并消除碎⽚。
停顿时间较⻓，会影响系统响应性能。

---

### 题12：Young GC 什么时候触发？

**答案：**

如果 Eden 区没有⾜够的空间时，就会触发 Young GC 来清理新⽣代。

---

### 题13：什么时候会触发 Full GC？

**答案：**

在进⾏ Young GC 的时候，如果发现⽼年代可⽤的连续内存空间 < 新⽣代历次 Young GC 后升⼊⽼年代的对象总和的
平均⼤⼩，说明本次 Young GC 后升⼊⽼年代的对象⼤⼩，可能超过了⽼年代当前可⽤的内存空间，就会触发 Full
执⾏ Young GC 后⽼年代没有⾜够的内存空间存放转⼊的对象，会⽴即触发⼀次 Full GC。
System.gc() 、jmap -dump  等命令会触发 full gc。
空间分配担保是指在进⾏ Minor GC 前，JVM 会确保⽼年代有⾜够的空间存放从新⽣代晋升的对象。如果⽼年代空
间不⾜，可能会触发 Full GC。

---

### 题14：Java ⾯试指南（付费）收录的快⼿同学 4 ⼀⾯原题：如何判断死亡对象？GC Roots有哪些？空间分配

**答案：**

JVM 的垃圾收集器主要分为两⼤类：分代收集器和分区收集器，分代收集器的代表是 CMS，分区收集器的代表是
CMS 是第⼀个关注 GC 停顿时间的垃圾收集器，JDK 1.5 时引⼊，JDK9 被标记弃⽤，JDK14 被移除。
G1 在 JDK 1.7 时引⼊，在 JDK 9 时取代 CMS 成为了默认的垃圾收集器。
ZGC 是 JDK11 推出的⼀款低延迟垃圾收集器，适⽤于⼤内存低延迟服务的内存管理和回收，在 128G 的⼤堆下，
最⼤停顿时间才 1.68 ms，性能远胜于 G1 和 CMS。
说说 Serial 收集器？
Serial 收集器是最基础、历史最悠久的收集器。
如同它的名字（串⾏），它是⼀个单线程⼯作的收集器，使⽤⼀个处理器或⼀条收集线程去完成垃圾收集⼯作。并
且进⾏垃圾收集时，必须暂停其他所有⼯作线程，直到垃圾收集结束——这就是所谓的“Stop The World”。
Serial/Serial Old 收集器的运⾏过程如图：
说说 ParNew 收集器？
ParNew 收集器实质上是 Serial 收集器的多线程并⾏版本，使⽤多条线程进⾏垃圾收集。
ParNew/Serial Old 收集器运⾏示意图如下：
说说 Parallel Scavenge 收集器？
Parallel Scavenge 收集器是⼀款新⽣代收集器，基于标记-复制算法实现，也能够并⾏收集。和 ParNew 有些类
似，但 Parallel Scavenge 主要关注的是垃圾收集的吞吐量——所谓吞吐量，就是 CPU ⽤于运⾏⽤户代码的时间和
总消耗时间的⽐值，⽐值越⼤，说明垃圾收集的占⽐越⼩。
根据对象存活周期的不同会将内存划分为⼏块，⼀般是把 Java 堆分为新⽣代和⽼年代，这样就可以根据各个年代
的特点采⽤最适当的收集算法。
说说 Serial Old 收集器？
Serial Old 是 Serial 收集器的⽼年代版本，它同样是⼀个单线程收集器，使⽤标记-整理算法。
说说 Parallel Old 收集器？
Parallel Old 是 Parallel Scavenge 收集器的⽼年代版本，基于标记-整理算法实现，使⽤多条 GC 线程在 STW 期间
说说 CMS 收集器？
CMS 在 JDK 1.5 时引⼊，JDK 9 时被标记弃⽤，JDK 14 时被移除。
CMS 是⼀种低延迟的垃圾收集器，采⽤标记-清除算法，分为初始标记、并发标记、重新标记和并发清除四个阶
段，优点是垃圾回收线程和应⽤线程同时运⾏，停顿时间短，适合延迟敏感的应⽤，但容易产⽣内存碎⽚，可能触
G1 在 JDK 1.7 时引⼊，在 JDK 9 时取代 CMS 成为默认的垃圾收集器。
G1 是⼀种⾯向⼤内存、⾼吞吐场景的垃圾收集器，它将堆划分为多个⼩的 Region，通过标记-整理算法，避免了
内存碎⽚问题。优点是停顿时间可控，适合⼤堆场景，但调优较复杂。
说说 ZGC 收集器？
ZGC 是 JDK 11 时引⼊的⼀款低延迟的垃圾收集器，最⼤特点是将垃圾收集的停顿时间控制在 10ms 以内，即使在
TB 级别的堆内存下也能保持较低的停顿时间。
它通过并发标记和重定位来避免⼤部分 Stop-The-World 停顿，主要依赖指针染⾊来管理对象状态。
标记对象的可达性：通过在指针上增加标记位，不需要额外的标记位即可判断对象的存活状态。
重定位状态：在对象被移动时，可以通过指针染⾊来更新对象的引⽤，⽽不需要等待全局同步。
适⽤于需要超低延迟的场景，⽐如⾦融交易系统、电商平台。
垃圾回收器的作⽤是什么？
垃圾回收器的核⼼作⽤是⾃动管理 Java 应⽤程序的运⾏时内存。它负责识别哪些内存是不再被应⽤程序使⽤的，
并释放这些内存以便重新使⽤。
这⼀过程减少了程序员⼿动管理内存的负担，降低了内存泄漏和溢出错误的⻛险。
⽣代、⽼年代）吗，使⽤的 jdk 版本
个讲⼀下垃圾回收的流程
知不知道ZGC回收器（不知道）
能详细说⼀下 CMS 的垃圾收集过程吗？
CMS 使⽤标记-清除算法进⾏垃圾收集，分 4 ⼤步：
初始标记：标记所有从 GC Roots 直接可达的对象，这个阶段需要 STW，但速度很快。
并发标记：从初始标记的对象出发，遍历所有对象，标记所有可达的对象。这个阶段是并发进⾏的。
重新标记：完成剩余的标记⼯作，包括处理并发阶段遗留下来的少量变动，这个阶段通常需要短暂的 STW 停
并发清除：清除未被标记的对象，回收它们占⽤的内存空间。
你提到了remark，那它remark具体是怎么执⾏的？三⾊标记法？
是的，remark 阶段通常会结合三⾊标记法来执⾏，确保在并发标记期间所有存活对象都被正确标记。⽬的是修正
并发标记阶段中可能遗漏的对象引⽤变化。
在 remark 阶段，垃圾收集器会停⽌应⽤线程，以确保在这个阶段不会有引⽤关系的进⼀步变化。这种暂停通常很
短暂。remark 阶段主要包括以下操作：
1. 处理写屏障记录的引⽤变化：在并发标记阶段，应⽤程序可能会更新对象的引⽤（⽐如⼀个⿊⾊对象新增了
对⼀个⽩⾊对象的引⽤），这些变化通过写屏障记录下来。在 remark 阶段，GC 会处理这些记录，确保所有
可达对象都正确地标记为灰⾊或⿊⾊。
2. 扫描灰⾊对象：再次遍历灰⾊对象，处理它们的所有引⽤，确保引⽤的对象正确标记为灰⾊或⿊⾊。
3. 清理：确保所有引⽤关系正确处理后，灰⾊对象标记为⿊⾊，⽩⾊对象保持不变。这⼀步完成后，所有存活
三⾊标记法⽤于标记对象的存活状态，它将对象分为三类：
1. ⽩⾊（White）：尚未访问的对象。垃圾回收结束后，仍然为⽩⾊的对象会被认为是不可达的对象，可以回
2. 灰⾊（Gray）：已经访问到但未标记完其引⽤的对象。灰⾊对象是需要进⼀步处理的。
3. ⿊⾊（Black）：已经访问到并且其所有引⽤对象都已经标记过。⿊⾊对象是完全处理过的，不需要再处理。
三⾊标记法的⼯作流程：
①、初始标记（Initial Marking）：从 GC Roots 开始，标记所有直接可达的对象为灰⾊。
②、并发标记（Concurrent Marking）：在此阶段，标记所有灰⾊对象引⽤的对象为灰⾊，然后将灰⾊对象⾃身
标记为⿊⾊。这个过程是并发的，和应⽤线程同时进⾏。
此阶段的⼀个问题是，应⽤线程可能在并发标记期间修改对象的引⽤关系，导致⼀些对象的标记状态不准确。
③、重新标记（Remarking）：重新标记阶段的⽬标是处理并发标记阶段遗漏的引⽤变化。为了确保所有存活对象
都被正确标记，remark 需要在 STW 暂停期间执⾏。
④、使⽤写屏障（Write Barrier）来捕捉并发标记阶段应⽤线程对对象引⽤的更新。通过遍历这些更新的引⽤来修
正标记状态，确保遗漏的对象不会被错误地回收。
个讲⼀下垃圾回收的流程
何分配的，（类加载和对象创建过程，CMS，G1 内存清理和分配）
法？你提到了remark，那它remark具体是怎么执⾏的？三⾊标记法？
G1 垃圾收集器了解吗？
G1 在 JDK 1.7 时引⼊，在 JDK 9 时取代 CMS 成为默认的垃圾收集器。
G1 把 Java 堆划分为多个⼤⼩相等的独⽴区域Region，每个区域都可以扮演新⽣代或⽼年代的⻆⾊。
同时，G1 还有⼀个专⻔为⼤对象设计的 Region，叫 Humongous 区。
⼤对象的判定规则是，如果⼀个⼤对象超过了⼀个 Region ⼤⼩的 50%，⽐如每个 Region 是 2M，只要⼀个
对象超过了 1M，就会被放⼊ Humongous 中。
这种区域化管理使得 G1 可以更灵活地进⾏垃圾收集，只回收部分区域⽽不是整个新⽣代或⽼年代。
G1 收集器的运⾏过程⼤致可划分为这⼏个步骤：
①、并发标记，G1 通过并发标记的⽅式找出堆中的垃圾对象。并发标记阶段与应⽤线程同时执⾏，不会导致应⽤
②、混合收集，在并发标记完成后，G1 会计算出哪些区域的回收价值最⾼（也就是包含最多垃圾的区域），然后
优先回收这些区域。这种回收⽅式包括了部分新⽣代区域和⽼年代区域。
选择回收成本低⽽收益⾼的区域进⾏回收，可以提⾼回收效率和减少停顿时间。
③、可预测的停顿，G1 在垃圾回收期间仍然需要「Stop the World」。不过，G1 在停顿时间上添加了预测机制，
⽤户可以 JVM 启动时指定期望停顿时间，G1 会尽可能地在这个时间内完成垃圾回收。
否，通过区域划分和压缩减少碎⽚
整个堆，但区分年轻代和⽼年代
并发标记、并发清理、并发回收
内存碎⽚、Concurrent Mode Failure
何分配的，（类加载和对象创建过程，CMS，G1 内存清理和分配）

---

### 题15：有了 CMS，为什么还要引⼊ G1？

**答案：**

CMS 适⽤于对延迟敏感的应⽤场景，主要⽬标是减少停顿时间，但容易产⽣内存碎⽚。
G1 则提供了更好的停顿时间预测和内存压缩能⼒，适⽤于⼤内存和多核处理器环境。

---

### 题16：你们线上⽤的什么垃圾收集器？

**答案：**

我们⽣产环境中采⽤了设计⽐较优秀的 G1 垃圾收集器，因为它不仅能满⾜低停顿的要求，⽽且解决了 CMS 的浮
动垃圾问题、内存碎⽚问题。
G1 ⾮常适合⼤内存、多核处理器的环境。
以上是⽐较符合⾯试官预期的回答，但实际上，⼤多数情况下我们可能还是使⽤的 JDK 8 默认垃圾收集器。
可以通过以下命令查看当前 JVM 的垃圾收集器：
java -XX:+PrintCommandLineFlags -version
UseParallelGC  = Parallel Scavenge + Parallel Old ，表示新⽣代⽤Parallel Scavenge 收集器，⽼年代
使⽤Parallel Old  收集器。
因此你也可以这样回答：
我们系统的业务相对复杂，但并发量并不是特别⾼，所以我们选择了适⽤于多核处理器、能够并⾏处理垃圾回收任
务，且能提供⾼吞吐量的Parallel GC 。
但这个说法不讨喜，你也可以回答：
我们系统采⽤的是 CMS 收集器，能够最⼤限度减少应⽤暂停时间。
⼯作中项⽬使⽤的什么垃圾回收算法？
我们⽣产环境中采⽤了设计⽐较优秀的 G1 垃圾收集器，G1 采⽤的是分区式标记-整理算法，将堆划分为多个区
域，按需回收，适⽤于⼤内存和多核环境，能够同时考虑吞吐量和暂停时间。
我们系统采⽤的是 CMS 收集器，CMS 采⽤的是标记-清除算法，能够并发标记和清除垃圾，减少暂停时间，适⽤
我们系统采⽤的是 Parallel 收集器，Parallel 采⽤的是年轻代使⽤复制算法，⽼年代使⽤标记-整理算法，适⽤于⾼

---

## 4. 四、JVM 调优

### 题1：垃圾收集器应该如何选择？

**答案：**

如果应⽤程序只需要⼀个很⼩的内存空间（⼤约 100 MB），或者对停顿时间没有特殊的要求，可以选择 Serial 收
如果优先考虑应⽤程序的峰值性能，并且没有时间要求，或者可以接受 1 秒或更⻓的停顿时间，可以选择 Parallel
如果响应时间⽐吞吐量优先级⾼，或者垃圾收集暂停必须保持在⼤约 1 秒以内，可以选择 CMS/ G1 收集器。
如果响应时间是⾼优先级的，或者堆空间⽐较⼤，可以选择 ZGC 收集器。
memo：2025 年 1 ⽉ 16 ⽇修改⾄此。

---

### 题2：⽤过哪些性能监控的命令⾏⼯具？

**答案：**

操作系统层⾯，我⽤过 top、vmstat、iostat、netstat 等命令，可以监控系统整体的资源使⽤情况，⽐如说内存、
CPU、IO 使⽤情况、⽹络使⽤情况。
JDK ⾃带的命令⾏⼯具层⾯，我⽤过 jps、jstat、jinfo、jmap、jhat、jstack、jcmd 等，可以查看 JVM 运⾏时信
息、内存使⽤情况、堆栈信息等。
你⼀般都怎么⽤jmap？
①、我⼀般会使⽤ jmap -heap <pid>  查看堆内存摘要，包括新⽣代、⽼年代、元空间等。
②、或者使⽤ jmap -histo <pid>  查看对象分布。
③、还有⽣成堆转储⽂件：jmap -dump:format=b,file=<path> <pid> 。

---

### 题3：了解哪些可视化的性能监控⼯具？

**答案：**

我⾃⼰⽤过的可视化⼯具主要有：
①、JConsole：JDK ⾃带的监控⼯具，可以⽤来监视 Java 应⽤程序的运⾏状态，包括内存使⽤、线程状态、类加
②、VisualVM：⼀个基于 NetBeans 的可视化⼯具，在很⻓⼀段时间内，VisualVM 都是 Oracle 官⽅主推的故障
处理⼯具。集成了多个 JDK 命令⾏⼯具的功能，⾮常友好。
③、Java Mission Control：JMC 最初是 JRockit VM 中的诊断⼯具，但在 Oracle JDK7 Update 40 以后，就绑定到
了 HotSpot VM 中。不过后来⼜被 Oracle 开源出来作为了⼀个单独的产品。
⽤过哪些第三⽅的⼯具？
①、MAT：⼀个 Java 堆内存分析⼯具，主要⽤于分析和查找 Java 堆中的内存泄漏和内存消耗问题；可以从 Java
堆转储⽂件中分析内存使⽤情况，并提供丰富的报告，如内存泄漏疑点、最⼤对象和 GC 根信息；⽀持通过图形界
⾯查询对象，以及检查对象间的引⽤关系。
②、GChisto：GC ⽇志分析⼯具，可以帮助我们优化垃圾收集⾏为和调整 GC 性能。
③、JProfiler：⼀个全功能的商业化 Java 性能分析⼯具，提供 CPU、 内存和线程的实时分析。
④、arthas：阿⾥巴巴开源的 Java 诊断⼯具，主要⽤于线上的应⽤诊断；⽀持在不停机的情况下进⾏诊断；可以
提供包括 JVM 信息查看、监控、Trace 命令、反编译等功能。
⑤、async-profiler：⼀个低开销的性能分析⼯具，⽀持⽣成⽕焰图，适⽤于复杂性能问题的分析。
序⾥哪些对象正在使⽤，哪些对象已经被释放

---

### 题4：JVM 的常⻅参数配置知道哪些？

**答案：**

配置堆内存⼤⼩的参数有哪些？
-Xms ：初始堆⼤⼩
-Xmx ：最⼤堆⼤⼩
-XX:NewSize=n ：设置年轻代⼤⼩
-XX:NewRatio=n ：设置年轻代和年⽼代的⽐值。如：n 为 3 表示年轻代和年⽼代⽐值为 1：3，年轻代占总
-XX:SurvivorRatio=n ：年轻代中 Eden 区与两个 Survivor 区的⽐值。如 n=3 表示 Eden 占 3 Survivor 占
2，⼀个 Survivor 区占整个年轻代的 1/5
配置 GC 收集器的参数有哪些？
-XX:+UseSerialGC ：设置串⾏收集器
-XX:+UseParallelGC ：设置并⾏收集器
-XX:+UseParalledlOldGC ：设置并⾏⽼年代收集器
-XX:+UseConcMarkSweepGC ：设置并发收集器
配置并⾏收集的参数有哪些？
-XX:MaxGCPauseMillis=n ：设置最⼤垃圾回收停顿时间
-XX:GCTimeRatio=n ：设置垃圾回收时间占程序运⾏时间的⽐例
-XX:+CMSIncrementalMode ：设置增量模式，适合单 CPU 环境
-XX:ParallelGCThreads=n ：设置并⾏收集器的线程数
打印 GC 回收的过程⽇志信息的参数有哪些？
-XX:+PrintGC ：输出 GC ⽇志
-XX:+PrintGCDetails ：输出 GC 详细⽇志
-XX:+PrintGCTimeStamps ：输出 GC 的时间戳（以基准时间的形式）
-Xloggc:filename ：⽇志⽂件的输出路径

---

### 题5：做过 JVM 调优吗？

**答案：**

JVM 调优是⼀个复杂的过程，调优的对象包括堆内存、垃圾收集器和 JVM 运⾏时参数等。
如果堆内存设置过⼩，可能会导致频繁的垃圾回收。所以在技术派实战项⽬中，启动 JVM 的时候配置了 -Xms  和
-Xmx  参数，让堆内存最⼤可⽤内存为 2G（我⽤的丐版服务器）。
在项⽬运⾏期间，我会使⽤ JVisualVM 定期观察和分析 GC ⽇志，如果发现频繁的 Full GC，我会特意关注⼀下⽼
接着，通过分析 Heap dump 寻找内存泄漏的源头，看看是否有未关闭的资源，⻓⽣命周期的⼤对象等。
之后进⾏代码优化，⽐如说减少⼤对象的创建、优化数据结构的使⽤⽅式、减少不必要的对象持有等。

---

### 题6：CPU 占⽤过⾼怎么排查？

**答案：**

⾸先，使⽤ top 命令查看 CPU 占⽤情况，找到占⽤ CPU 较⾼的进程 ID。
接着，使⽤ jstack 命令查看对应进程的线程堆栈信息。
这个命令会将所有线程的堆栈信息输出到 thread-dump.txt ⽂件中。
然后再使⽤ top 命令查看进程中线程的占⽤情况，找到占⽤ CPU 较⾼的线程 ID。
注意，top 命令显示的线程 ID 是⼗进制的，⽽ jstack 输出的是⼗六进制的，所以需要将线程 ID 转换为⼗六
接着在 jstack 的输出中搜索这个⼗六进制的线程 ID，找到对应的堆栈信息。
jstack -l <pid> > thread-dump.txt
top -H -p <pid>
printf "%x\n" PID
"Thread-5" #21 prio=5 os_prio=0 tid=0x00007f812c018800 nid=0x1a85 runnable
[0x00007f811c000000]
java.lang.Thread.State: RUNNABLE
at com.example.MyClass.myMethod(MyClass.java:123)
最后，根据堆栈信息定位到具体的业务⽅法，查看是否有死循环、频繁的垃圾回收、资源竞争导致的上下⽂频繁切
如某个线程 cpu 占⽤率⾼，怎么看堆栈信息
段？排查后发现是项⽬产⽣了内存泄露，如何确定问题出在哪⾥？

---

### 题7：内存飙⾼问题怎么排查？

**答案：**

内存飚⾼⼀般是因为创建了⼤量的 Java 对象导致的，如果持续飙⾼则说明垃圾回收跟不上对象创建的速度，或者
内存泄漏导致对象⽆法回收。
排查的⽅法主要分为以下⼏步：
第⼀，先观察垃圾回收的情况，可以通过 jstat -gc PID 1000  查看 GC 次数和时间。
或者使⽤ jmap -histo PID | head -20  查看堆内存占⽤空间最⼤的前 20 个对象类型。
第⼆步，通过 jmap 命令 dump 出堆内存信息。
第三步，使⽤可视化⼯具分析 dump ⽂件，⽐如说 VisualVM，找到占⽤内存⾼的对象，再找到创建该对象的业务
代码位置，从代码和业务场景中定位具体问题。

---

### 题8：频繁 minor gc 怎么办？

**答案：**

频繁的 Minor GC 通常意味着新⽣代中的对象频繁地被垃圾回收，可能是因为新⽣代空间设置的过⼩，或者是因为
程序中存在⼤量的短⽣命周期对象（如临时变量）。
可以使⽤ GC ⽇志进⾏分析，查看 GC 的频率和耗时，找到频繁 GC 的原因。
或者使⽤监控⼯具查看堆内存的使⽤情况，特别是新⽣代（Eden 和 Survivor 区）的使⽤情况。
如果是因为新⽣代空间不⾜，可以通过 -Xmn  增加新⽣代的⼤⼩，减缓新⽣代的填满速度。
如果对象需要⻓期存活，但频繁从 Survivor 区晋升到⽼年代，可以通过 -XX:SurvivorRatio  参数调整 Eden 和
Survivor 的⽐例。默认⽐例是 8:1，表示 8 个空间⽤于 Eden，1 个空间⽤于 Survivor 区。
调整为 6 的话，会减少 Eden 区的⼤⼩，增加 Survivor 区的⼤⼩，以确保对象在 Survivor 区中存活的时间⾜够
⻓，避免过早晋升到⽼年代。

---

## 5. 五、类加载机制

### 题1：频繁 Full GC 怎么办？

**答案：**

-XX:+PrintGCDetails -Xloggc:gc.log
java -Xmn256m your-app.jar
-XX:SurvivorRatio=6
频繁的 Full GC 通常意味着⽼年代中的对象频繁地被垃圾回收，可能是因为⽼年代空间设置的过⼩，或者是因为程
序中存在⼤量的⻓⽣命周期对象。
该怎么排查 Full GC 频繁问题？
我⼚会通过专⻔的性能监控系统，查看 GC 的频率和堆内存的使⽤情况，然后根据监控数据分析 GC 的原因。
如果是⼩⼚，可以这么回复。
我⼀般会使⽤ JDK 的⾃带⼯具，包括 jmap、jstat 等。
或者使⽤⼀些可视化的⼯具，⽐如 VisualVM、JConsole 等，查看堆内存的使⽤情况。
假如是因为⼤对象直接分配到⽼年代导致的 Full GC 频繁，可以通过 -XX:PretenureSizeThreshold  参数设置⼤
对象直接进⼊⽼年代的阈值。
或者将⼤对象拆分成⼩对象，减少⼤对象的创建。⽐如说分⻚。
假如是因为内存泄漏导致的频繁 Full GC，可以通过分析堆内存 dump ⽂件找到内存泄漏的对象，再找到内存泄漏
假如是因为⻓⽣命周期的对象进⼊到了⽼年代，要及时释放资源，⽐如说 ThreadLocal、数据库连接、IO 资源
假如是因为 GC 参数配置不合理导致的频繁 Full GC，可以通过调整 GC 参数来优化 GC ⾏为。或者直接更换更适合
的 GC 收集器，如 G1、ZGC 等。
了解类的加载机制吗？（补充）
2024 年 03 ⽉ 29 ⽇增补
JVM 的操作对象是 Class ⽂件，JVM 把 Class ⽂件中描述类的数据结构加载到内存中，并对数据进⾏校验、解析和
初始化，最终转化成可以被 JVM 直接使⽤的类型，这个过程被称为类加载机制。
其中最重要的三个概念就是：类加载器、类加载过程和双亲委派模型。
类加载器：负责加载类⽂件，将类⽂件加载到内存中，⽣成 Class 对象。
类加载过程：包括加载、验证、准备、解析和初始化等步骤。
双亲委派模型：当⼀个类加载器接收到类加载请求时，它会把请求委派给⽗——类加载器去完成，依次递
归，直到最顶层的类加载器，如果⽗——类加载器⽆法完成加载请求，⼦类加载器才会尝试⾃⼰去加载。
# 查看堆内存各区域的使⽤率以及GC情况
jstat -gcutil -h20 pid 1000
# 查看堆内存中的存活对象，并按空间排序
jmap -histo pid | head -n20
# dump堆内存⽂件
jmap -dump:format=b,file=heap pid

---

### 题2：Java ⾯试指南（付费）收录的⼩⽶暑期实习同学 E ⼀⾯⾯试原题：你了解类的加载机制吗？

**答案：**

派机制 这样设计的原因是什么

---

### 题3：类加载器有哪些？

**答案：**

①、启动类加载器，负责加载 JVM 的核⼼类库，如 rt.jar 和其他核⼼库位于JAVA_HOME/jre/lib ⽬录下的类。
②、扩展类加载器，负责加载JAVA_HOME/jre/lib/ext ⽬录下，或者由系统属性java.ext.dirs 指定位置的类
库，由sun.misc.Launcher$ExtClassLoader  实现。
③、应⽤程序类加载器，负责加载 classpath 的类库，由sun.misc.Launcher$AppClassLoader 实现。
我们编写的任何类都是由应⽤程序类加载器加载的，除⾮显式使⽤⾃定义类加载器。
④、⽤户⾃定义类加载器，通常⽤于加载⽹络上的类、执⾏热部署（动态加载和替换应⽤程序的组件），或者为了
安全考虑，从不同的源加载类。
通过继承java.lang.ClassLoader 类来实现。

---

### 题4：能说⼀下类的⽣命周期吗？

**答案：**

⼀个类从被加载到虚拟机内存中开始，到从内存中卸载，整个⽣命周期需要经过七个阶段：加载 、验证、准备、
解析、初始化、使⽤和卸载。
类装载过程包括三个阶段：载⼊、链接和初始化。
①、载⼊：将类的⼆进制字节码加载到内存中。
②、链接可以细分为三个⼩的阶段：
验证：检查类⽂件格式是否符合 JVM 规范
准备：为类的静态变量分配内存并设置默认值。
解析：将符号引⽤替换为直接引⽤。
③、初始化：执⾏静态代码块和静态变量初始化。
在准备阶段，静态变量已经被赋过默认初始值了，在初始化阶段，静态变量将被赋值为代码期望赋的值。⽐如说
static int a = 1; ，在准备阶段，a  的值为 0，在初始化阶段，a  的值为 1。
换句话说，初始化阶段是在执⾏类的构造⽅法，也就是 javap 中看到的 <clinit>() 。
载⼊过程 JVM 会做什么？
1）通过⼀个类的全限定名来获取定义此类的⼆进制字节流。
2）将这个字节流所代表的静态存储结构转化为⽅法区的运⾏时数据结构。
3）在内存中⽣成⼀个代表这个类的 java.lang.Class  对象，作为这个类的访问⼊⼝。

---

### 题5：Java ⾯试指南（付费）收录的⼩⽶暑期实习同学 E ⼀⾯⾯试原题：你了解类的加载机制吗？

**答案：**



---

### 题6：Java ⾯试指南（付费）收录的快⼿同学 4 ⼀⾯原题：类装载的执⾏过程？双亲委派模式是什么？为什么

**答案：**

memo：2025 年 1 ⽉ 17 ⽇修改⾄此。
双亲委派模型要求类加载器在加载类时，先委托⽗加载器尝试加载，只有⽗加载器⽆法加载时，⼦加载器才会加
这个过程会⼀直向上递归，也就是说，从⼦加载器到⽗加载器，再到更上层的加载器，⼀直到最顶层的启动类加载
启动类加载器会尝试加载这个类。如果它能够加载这个类，就直接返回；如果它不能加载这个类，就会将加载任务
返回给委托它的⼦加载器。
⼦加载器尝试加载这个类。如果⼦加载器也⽆法加载这个类，它就会继续向下传递这个加载任务，依此类推。
直到某个加载器能够加载这个类，或者所有加载器都⽆法加载这个类，最终抛出 ClassNotFoundException。

---

### 题7：Java ⾯试指南（付费）收录的⼩⽶暑期实习同学 E ⼀⾯⾯试原题：你了解类的加载机制吗？

**答案：**



---

### 题8：为什么要⽤双亲委派模型？

**答案：**

①、避免类的重复加载：⽗加载器加载的类，⼦加载器⽆需重复加载。
②、保证核⼼类库的安全性：如 java.lang.*  只能由 Bootstrap ClassLoader 加载，防⽌被篡改。

---

### 题9：如何破坏双亲委派机制？

**答案：**

重写 ClassLoader 的 loadClass()  ⽅法。
如果不想打破双亲委派模型，就重写 ClassLoader 类中的 findClass()  ⽅法，那些⽆法被⽗类加载器加载的类最
终会通过这个⽅法被加载。
memo：2025 年 1 ⽉ 18 ⽇修改⾄此。

---

### 题10：有哪些破坏双亲委派模型的典型例⼦？

**答案：**

第⼀种：SPI 机制加载 JDBC 驱动。
SPI 是 Java 的⼀种扩展机制，⽤于加载和注册第三⽅类库，常⻅于 JDBC、JNDI 等框架。
双亲委派模型会优先让⽗类加载器加载类，⽽ SPI 需要动态加载⼦类加载器中的实现。
根据双亲委派模型，java.sql.Driver  类应该由⽗加载器加载，但⽗类加载器⽆法加载由⼦类加载器定义的驱动
类，如 MySQL 的 com.mysql.cj.jdbc.Driver 。
那么只能使⽤ SPI 机制通过 META-INF/services  ⽂件指定服务提供者的实现类。
DriverManager 使⽤了线程上下⽂类加载器来加载 SPI 的实现类，从⽽允许⼦类加载器加载具体的 JDBC 驱动。
ClassLoader cl = Thread.currentThread().getContextClassLoader();
Enumeration<Driver> drivers = ServiceLoader.load(Driver.class, cl).iterator();
热部署是指在不重启服务器的情况下更新应⽤程序代码，需要替换旧版本的类，但旧版本的类可能由⽗加载器加
如 Spring Boot 的 DevTools 通常会⾃定义类加载器，优先加载新的类版本。
memo：2025 年 1 ⽉ 19 ⽇修改⾄此。

---

### 题11：Tomcat 的类加载机制了解吗？

**答案：**

Tomcat 基于双亲委派模型进⾏了⼀些扩展，主要的类加载器有：
Bootstrap ClassLoader：加载 Java 的核⼼类库；
Catalina ClassLoader：加载 Tomcat 的核⼼类库；
Shared ClassLoader：加载共享类库，允许多个 Web 应⽤共享某些类库；
WebApp ClassLoader：加载 Web 应⽤程序的类库，⽀持多应⽤隔离和优先加载应⽤⾃定义的类库（破坏了

---

### 题12：你觉得应该怎么实现⼀个热部署功能？

**答案：**

热部署是指在不重启服务器的情况下，动态加载、更新或卸载应⽤程序的组件，⽐如类、配置⽂件等。
需要在类加载器的基础上，实现类的重新加载。
第⼀步，使⽤⽂件监控机制，如 Java NIO 的 WatchService 来监控类⽂件或配置⽂件的变化。当监控到⽂件变更
class FileWatcher {
public static void watchDirectoryPath(Path path) {
// 检查路径是否是有效⽬录
if (!isDirectory(path)) {
System.err.println("Provided path is not a directory: " + path);
System.out.println("Starting to watch path: " + path);
// 获取⽂件系统的 WatchService
try (WatchService watchService = path.getFileSystem().newWatchService()) {
// 注册⽬录监听服务，监听创建、修改和删除事件
path.register(watchService, ENTRY_CREATE, ENTRY_MODIFY, ENTRY_DELETE);
while (true) {
WatchKey key;
// 阻塞直到有事件发⽣
key = watchService.take();
} catch (InterruptedException e) {
System.out.println("WatchService interrupted, stopping directory
Thread.currentThread().interrupt();
for (WatchEvent<?> event : key.pollEvents()) {
processEvent(event);
// 重置 key，如果失败则退出
if (!key.reset()) {
System.out.println("WatchKey no longer valid. Exiting watch loop.");
} catch (IOException e) {
System.err.println("An error occurred while setting up the WatchService: " +
e.getMessage());
e.printStackTrace();
第⼆步，创建⼀个⾃定义类加载器，继承java.lang.ClassLoader ，并重写findClass() ⽅法，⽤来加载新的类
private static boolean isDirectory(Path path) {
return Files.isDirectory(path, LinkOption.NOFOLLOW_LINKS);
private static void processEvent(WatchEvent<?> event) {
WatchEvent.Kind<?> kind = event.kind();
if (kind == OVERFLOW) {
System.out.println("Event overflow occurred. Some events might have been
@SuppressWarnings("unchecked")
Path fileName = ((WatchEvent<Path>) event).context();
System.out.println("Event: " + kind.name() + ", File affected: " + fileName);
public static void main(String[] args) {
// 设置监控路径为当前⽬录
Path pathToWatch = Paths.get(".");
watchDirectoryPath(pathToWatch);
class HotSwapClassLoader extends ClassLoader {
public HotSwapClassLoader() {
super(ClassLoader.getSystemClassLoader());
protected Class<?> findClass(String name) throws ClassNotFoundException {
// 加载指定路径下的类⽂件字节码
byte[] classBytes = loadClassData(name);
if (classBytes == null) {
throw new ClassNotFoundException(name);
// 调⽤defineClass将字节码转换为Class对象
return defineClass(name, classBytes, 0, classBytes.length);
private byte[] loadClassData(String name) {
// 实现从⽂件系统或其他来源加载类⽂件的字节码
友情提示：Intellij IDEA 提供了热部署功能，当我们修改了代码后，IDEA 会⾃动保存并编译，如果是 Web 项⽬，
还可以在 Chrome 浏览器中装⼀个 LiveReload 插件，⼀旦编译完成，⻚⾯就会⾃动刷新看到最新的效果。对于测
试或者调试来说，⾮常⽅便。

---

### 题13：Java ⾯试指南（付费）收录的⼩⽶暑期实习同学 E ⼀⾯⾯试原题：那你知道类的热更新的？

**答案：**

54.说说解释执⾏和编译执⾏的区别（补充）
2024 年 03 ⽉ 08 ⽇增补
先说解释和编译的区别：
解释：将源代码逐⾏转换为机器码。
编译：将源代码⼀次性转换为机器码。
⼀个是逐⾏，⼀个是⼀次性，再来说说解释执⾏和编译执⾏的区别：
解释执⾏：程序运⾏时，将源代码逐⾏转换为机器码，然后执⾏。
编译执⾏：程序运⾏前，将源代码⼀次性转换为机器码，然后执⾏。
Java ⼀般被称为“解释型语⾔”，因为 Java 代码在执⾏前，需要先将源代码编译成字节码，然后在运⾏时，再由
JVM 的解释器“逐⾏”将字节码转换为机器码，然后执⾏。
这也是 Java 被诟病“慢”的主要原因。
但 JIT 的出现打破了这种刻板印象，JVM 会将热点代码（即运⾏频率⾼的代码）编译后放⼊ CodeCache，当下次执
⾏再遇到这段代码时，会从 CodeCache 中直接读取机器码，然后执⾏。
因此，Java 的执⾏效率得到了⼤幅提升。
return null;
memo：2025 年 1 ⽉ 21 ⽇修改⾄此。
果，并且从从 24 届到 25 届，帮助了很多⼩伙伴。未来的 26、27 届，也将因此受益，从⽽拿到⼼仪的 offer。
很多时候，我觉得⾃⼰是⼀个佛系的⼈，不愿意和别⼈争个⾼低，也不愿意去刻意宣传⾃⼰的作品。
我还会继续优化，也不确定第三版什么时候会来，但我会尽⼒。
愿⼤家都有⼀个光明的未来。
这次仍然是三个版本，亮⽩、暗⿊和 epub 版本。给⼤家展示其中⼀个 epub 版本吧，有些⼩伙伴很急需这个版
本，所以也满⾜⼤家了。
由于 PDF 没办法⾃我更新，所以需要最新版的⼩伙伴，可以微信搜【沉默王⼆】，或者扫描/⻓按识别下⾯的⼆维
码，关注⼆哥的公众号，回复【222】即可拉取最新版本。
当然了，请允许我的⼀点点私⼼，那就是星球的 PDF 版本会⽐公众号早⼀个⽉时间，毕竟星球⽤户都付费过了，
我有必要让他们先享受到⼀点点福利。相信⼤家也都能理解，毕竟在线版是免费的，CDN、服务器、域名、OSS
更别说我付出的时间和精⼒了，⼤家觉得有帮助还请给个⼝碑，让你身边的同事、同学都能受益到。
基础、Java集合、Java并发、JVM、Spring、MyBatis、计算机⽹络、操作系统、MySQL、Redis、RocketMQ、分
布式、微服务、设计模式、Linux 等 16 个⼤的主题，共有 40 多万字，2000+张⼿绘图，可以说是诚意满满。
图⽂详解 54 道 Java 虚拟机⾼频⾯试题，这次⾯试，⼀定吊打⾯试官，整理：沉默王⼆，戳转载链接，作者：三分
没有什么使我停留——除了⽬的，纵然岸旁有玫瑰、有绿荫、有宁静的港湾，我是不系之⾈。

---
# JVM 篇 - 类加载机制（Day 5 完整答案）

> 来源：面渣逆袭 JVM 篇 V2.1  
> 创建时间：2026-03-18  
> 题数：7 题  
> 状态：✅ 已学习 + 网络补充

---

## 题 1：JVM 的类加载器有哪些？分别负责加载什么？

**考点：** 类加载器类型及职责

**标准答案：**

JVM 有 4 种类加载器：

| 类加载器 | 负责加载 | 实现类 |
|---------|---------|--------|
| **启动类加载器** (Bootstrap) | JVM 核心类库（rt.jar、JAVA_HOME/jre/lib） | C++ 实现，JVM 内置 |
| **扩展类加载器** (Extension) | JAVA_HOME/jre/lib/ext 或 java.ext.dirs 指定位置 | `sun.misc.Launcher$ExtClassLoader` |
| **应用程序类加载器** (Application) | classpath 的类库（我们编写的类） | `sun.misc.Launcher$AppClassLoader` |
| **用户自定义类加载器** | 网络类、热部署、安全隔离 | 继承 `java.lang.ClassLoader` |

**记忆口诀：** 启扩应自（启动、扩展、应用、自定义）

**常见错误：**
- ❌ 说"静态属性"而不是"静态变量"
- ❌ 不知道扩展类加载器的实现类名称

---

## 题 2：什么是双亲委派模型？它有什么好处？

**考点：** 双亲委派模型原理

**标准答案：**

**双亲委派模型工作流程：**

当一个类加载器收到类加载请求时：
1. 先委托给父加载器尝试加载
2. 父加载器再委托给它的父加载器
3. 递归到最顶层的启动类加载器
4. 如果父加载器无法加载，才返回给子加载器
5. 子加载器尝试自己加载

**好处（2 个）：**

| 好处 | 说明 |
|------|------|
| **避免类的重复加载** | 父加载器加载的类，子加载器无需重复加载 |
| **保证核心类库安全** | `java.lang.*` 只能由 Bootstrap ClassLoader 加载，防止被篡改 |

**举例：**
```java
// 我们编写的类中引用 java.lang.String
// 请求先委托给启动类加载器，它能加载 java.lang.String
// 所以不会加载我们自己定义的 java.lang.String（防止篡改）
```

**常见错误：**
- ❌ 说"找父类"而不是"委托父加载器"
- ❌ 漏了"递归到顶层启动类加载器"
- ❌ 漏了"加载失败后返回给子加载器"

---

## 题 3：有哪些破坏双亲委派模型的典型场景？

**考点：** 破坏双亲委派的场景

**标准答案：**

主要有 3 种场景：

### 场景 1：SPI 机制（JDBC 驱动）

**问题：** `java.sql.Driver` 由启动类加载器加载，但 MySQL 驱动 `com.mysql.cj.jdbc.Driver` 由应用程序类加载器加载，父加载器无法加载子类加载器的类。

**解决方案：** 使用**线程上下文类加载器**
```java
// DriverManager 使用线程上下文类加载器加载 SPI 实现
ClassLoader cl = Thread.currentThread().getContextClassLoader();
ServiceLoader.load(Driver.class, cl);
```

### 场景 2：热部署框架

**场景：** Spring Boot DevTools、OSGi 等

**实现：** 自定义类加载器，**优先加载新版本**的类（而不是先委托给父加载器）

### 场景 3：Tomcat 类加载机制

Tomcat 的类加载器层次：
```
Bootstrap ClassLoader（Java 核心类）
    ↓
Catalina ClassLoader（Tomcat 核心类）
    ↓
Shared ClassLoader（共享类库）
    ↓
WebApp ClassLoader（Web 应用类库）← **优先加载应用自定义类**
```

**为什么破坏？**
- 支持多应用隔离（不同 Web 应用可以用不同版本的类库）
- 优先加载应用自定义的类（而不是先委托给父加载器）

**记忆口诀：** SPI 热部署 Tomcat

---

## 题 4：类的生命周期有几个阶段？类加载过程有几个阶段？两者的区别是什么？

**考点：** 生命周期 vs 类加载过程

**标准答案：**

### 类的生命周期（7 个阶段）

**完整流程：** 加载 → 验证 → 准备 → 解析 → 初始化 → **使用** → **卸载**

### 类加载过程（5 个阶段）

**只是生命周期的一部分！**

加载 → 验证 → 准备 → 解析 → 初始化

### 两者的区别

| 对比 | 生命周期 | 类加载过程 |
|------|---------|-----------|
| **阶段数** | 7 个 | 5 个 |
| **包含关系** | 包含类加载过程 | 是生命周期的子集 |
| **差异** | 多了**使用**和**卸载** | 不包含使用和卸载 |

**⑥ 使用阶段：** 类被应用程序使用（创建对象、调用方法、访问字段等）

**⑦ 卸载阶段：** 类从内存中卸载（很少发生，只有当该类的所有实例都被回收，且类加载器被回收时）

**记忆口诀：** 生 7 加 5（生命周期 7 个，类加载过程 5 个）

---

## 题 5：准备阶段和初始化阶段有什么区别？举例说明。

**考点：** 准备 vs 初始化的区别

**标准答案：**

| 阶段 | 作用 | 示例 |
|------|------|------|
| **准备** | 静态变量分配内存 + **设置默认值** | `static int a = 1` → a=0 |
| **初始化** | 执行**静态代码块** + 静态变量赋值 | `static int a = 1` → a=1 |

**关键考点：**

```java
static int a = 1;
static {
    System.out.println("初始化");
}

// 准备阶段：a = 0（默认值）
// 初始化阶段：a = 1（期望值，执行<clinit>()）
```

**常见错误：**
- ❌ 说"准备阶段不分配内存"（实际会分配）
- ❌ 不知道初始化阶段会执行静态代码块
- ❌ 混淆默认值和期望值

---

## 题 6：如何破坏双亲委派模型？

**考点：** 破坏双亲委派的实现方式

**标准答案：**

### 方法：重写 `ClassLoader` 的 `loadClass()` 方法

**默认行为（不破坏）：** 重写 `findClass()` 方法
```java
@Override
protected Class<?> findClass(String name) throws ClassNotFoundException {
    // 父加载器无法加载时，才调用这个方法
    byte[] classData = loadClassData(name);
    return defineClass(name, classData, 0, classData.length);
}
```

**破坏双亲委派：** 重写 `loadClass()` 方法
```java
@Override
protected Class<?> loadClass(String name, boolean resolve) throws ClassNotFoundException {
    // 不委托给父加载器，直接自己加载
    byte[] classData = loadClassData(name);
    return defineClass(name, classData, 0, classData.length);
}
```

**常见错误：**
- ❌ 说重写 `defineClass()` 方法
- ❌ 不知道默认应该重写 `findClass()`

---

## 题 7：Tomcat 的类加载机制是怎样的？它为什么要破坏双亲委派？

**考点：** Tomcat 类加载机制

**标准答案：**

### Tomcat 类加载器层次（从上到下）

```
Bootstrap ClassLoader（Java 核心类库）
    ↓
Catalina ClassLoader（Tomcat 核心类库）
    ↓
Shared ClassLoader（共享类库，所有 Web 应用共享）
    ↓
WebApp ClassLoader（Web 应用类库）← **每个应用有自己的实例**
```

### Tomcat 破坏双亲委派的表现

**正常双亲委派：** 先委托父加载器，父加载器无法加载才自己加载

**Tomcat 的做法：**
1. **优先加载应用自定义的类**（而不是先委托给父加载器）
2. **每个 Web 应用有自己的 WebApp ClassLoader**（应用隔离）

### 为什么要破坏？

| 原因 | 说明 |
|------|------|
| **多应用隔离** | 不同 Web 应用可以用不同版本的类库（如 Spring 5.x vs Spring 6.x） |
| **应用优先级** | 应用自定义的类优先于共享类库（允许覆盖 Tomcat 提供的类） |
| **安全性** | 防止应用修改 Tomcat 核心类 |

**面试回答模板：**
> Tomcat 自定义了类加载器层次：Bootstrap → Catalina → Shared → WebApp
> 
> 其中 WebApp ClassLoader 破坏了双亲委派模型，它优先加载应用自定义的类，而不是先委托给父加载器。
> 
> 这样做的好处是：
> 1. 支持多应用隔离（不同应用可以用不同版本的类库）
> 2. 允许应用覆盖 Tomcat 提供的类

---

## 📊 Day 5 学习总结

| 题号 | 考点 | 掌握度 | 状态 |
|------|------|--------|------|
| 1 | 类加载器 + 类加载过程 | 3/5 | 🟡 |
| 2 | 双亲委派模型 | 3.5/5 | 🟡 |
| 3 | 破坏双亲委派场景 | 4/5 | ✅ |
| 4 | 生命周期 vs 类加载过程 | 5/5 | ✅ 🎉 |
| 5 | 准备 vs 初始化 | 5/5 | ✅ 🎉 |
| 6 | 如何破坏双亲委派 | 4/5 | ✅ |
| 7 | Tomcat 类加载机制 | 3.5/5 | 🟡 |

**总评：4.0/5** ✅

**薄弱项：**
- 🟡 类加载器职责（每个加载器负责加载什么）
- 🟡 Tomcat 类加载器层次结构

---

## 🔗 关联知识点

- **JVM 内存区域**：方法区（元空间）存储类信息
- **垃圾回收**：类的卸载条件
- **并发编程**：线程上下文类加载器

---

*最后更新：2026-03-18 20:35*

---

# JVM Day 4 - JMM + volatile + synchronized（完整答案）

> 来源：面渣逆袭 JVM 篇 V2.1  
> 创建时间：2026-03-18  
> 题数：10 题  
> 状态：✅ 已学习 + 网络补充

---

## 题 1：JMM（Java 内存模型）是什么？它解决了什么问题？有哪些核心特性？

**考点：** JMM 三特性

**标准答案：**

**JMM = Java Memory Model**

JMM 定义了**主内存**（所有线程共享）和**工作内存**（每个线程私有）的交互规则，用于解决多线程访问共享变量产生的**原子性、可见性、有序性**问题。

**三特性：**

| 特性 | 说明 | 示例 |
|------|------|------|
| **原子性** | 操作要么全部完成，要么完全不执行 | i++ 不是原子操作 |
| **可见性** | 一个线程修改变量，其他线程能立即看到 | volatile 保证可见性 |
| **有序性** | 程序执行顺序按照代码顺序 | 禁止指令重排序 |

**JMM 的抽象结构：**
- **主内存**：所有线程共享，变量存储在主内存
- **工作内存**：每个线程私有，线程不能直接访问主内存，必须通过工作内存

**记忆口诀：** 原可有（原子性、可见性、有序性）

**常见错误：**
- ❌ 漏了主内存 vs 工作内存的交互规则
- ❌ 不知道 JMM 是抽象概念，不是物理结构

---

## 题 2：volatile 关键字的作用是什么？它能保证原子性吗？为什么？

**考点：** volatile 作用

**标准答案：**

**volatile 的作用：**
1. **保证可见性**：通过内存屏障，强制每次读取都从主内存加载
2. **保证有序性**：禁止指令重排序
3. **不能保证原子性**

**为什么不能保证原子性？**

原子性 = 操作要么全部完成，要么完全不执行，中间不可打断

volatile 的原理：
- 通过内存屏障禁止指令重排序（保证有序性）
- 强制每次读取都从主内存加载（保证可见性）
- **但是！它不锁住操作**

**经典反例：** i++ 操作
`java
volatile int i = 0;

// 线程 A 和线程 B 同时执行 i++
i++;  // 实际是 3 步：读取 i → i+1 → 写回 i
`

**问题：**
1. 线程 A 读取 i=0
2. 线程 B 读取 i=0（A 还没写回）
3. 线程 A 计算 0+1=1，写回 i=1
4. 线程 B 计算 0+1=1，写回 i=1
5. **结果 i=1**（应该是 2！）

**原因：** i++ 不是原子操作，是**读取→修改→写入**三步，volatile 无法保证这三步不被其他线程打断。

**解决方案：**
- 用 AtomicInteger（CAS 保证原子性）
- 用 synchronized（锁保证原子性）

**记忆口诀：** 可有原不行（可见性、有序性可以，原子性不行）

---

## 题 3：synchronized 关键字有哪些用法？锁升级过程是怎样的？

**考点：** synchronized 用法 + 锁升级

**标准答案：**

**synchronized 的 3 种用法：**

| 用法 | 锁对象 | 说明 |
|------|--------|------|
| **实例方法** | this | 锁住当前实例 |
| **静态方法** | Class 对象 | 锁住类 |
| **代码块** | 指定对象 | 锁住括号内的对象 |

**锁升级过程（4 种状态）：**

`
无锁 → 偏向锁 → 轻量级锁 → 重量级锁（不可降级）
`

| 锁状态 | 说明 |
|--------|------|
| **无锁** | 没有线程竞争 |
| **偏向锁** | 第一个获取锁的线程"偏向"于它，后续直接获取（无竞争） |
| **轻量级锁** | 有竞争时，线程自旋等待（不阻塞） |
| **重量级锁** | 自旋失败后，线程阻塞（操作系统互斥量） |

**优化策略：** 自旋锁、锁消除、锁粗化、偏向锁

**记忆口诀：** 偏轻重量（偏向、轻量、重量）

**常见错误：**
- ❌ "锁粗化"说成"锁粗话"（口误）
- ❌ 不知道锁升级方向不可逆

---

## 题 4：CAS 原理是什么？什么是 ABA 问题？如何解决？

**考点：** CAS 原理 + ABA 问题

**标准答案：**

**CAS = Compare And Swap（比较并交换）**

**三要素：**
- **内存值 V**：内存中的实际值
- **预期值 A**：线程认为的当前值
- **新值 B**：线程想更新的新值

**操作流程：**
`
只有当 V == A 时，才将 V 更新为 B
否则，不更新，返回失败
`

**代码示例：**
`java
AtomicInteger atomicInt = new AtomicInteger(0);

// CAS 操作：如果当前值是 0，就更新为 1
atomicInt.compareAndSet(0, 1);  // true，更新成功

atomicInt.compareAndSet(0, 1);  // false，当前值已是 1，失败
`

**底层实现：** CPU 指令 cmpxchg（硬件级原子操作）

---

**ABA 问题：**

**场景：**
`
线程 1 读取内存值为 A
线程 2 将 A → B → A（改回原值）
线程 1 执行 CAS，发现还是 A，认为没变过 → **错误地成功**
`

**问题：** 值虽然回到 A，但**中间被修改过**！

**解决方案：版本号机制**
`java
AtomicStampedReference<Integer> ref = 
    new AtomicStampedReference<>(0, 0);  // 值 + 版本号

// CAS 时同时检查值和版本号
ref.compareAndSet(0, 1, 0, 1);  // 值 0→1，版本 0→1
`

**记忆口诀：** CAS 比换，ABA 版本号

**常见错误：**
- ❌ 不知道 CAS 三要素
- ❌ 忘记 ABA 解决方案

---

## 题 5：如何保证线程安全？有哪些实现方式？

**考点：** 线程安全实现方式

**标准答案：**

**线程安全：** 多线程访问共享变量时，不添加额外同步措施也能保证正确性

**三大实现方式：**

| 方式 | 说明 | 示例 |
|------|------|------|
| **不可变** | 对象创建后状态不能修改 | String、final 基本类型 |
| **同步** | 通过锁或 CAS 保证原子性 | synchronized、Lock、AtomicXXX |
| **线程封闭** | 数据只在线程内部访问，不共享 | 栈封闭、ThreadLocal |

**volatile 的定位：**
- ❌ **不能单独保证线程安全**（因为不能保证原子性）
- ✅ 可以配合其他机制使用（如双重检查锁 DCL）

**记忆口诀：** 不变封同（不可变、封闭、同步）

**常见错误：**
- ❌ 把 volatile 和锁、CAS 并列（volatile 不能保证原子性）
- ❌ 分类混乱

---

## 题 6：ReentrantLock 和 synchronized 有什么区别？

**考点：** ReentrantLock vs synchronized

**标准答案：**

| 对比 | ReentrantLock | synchronized |
|------|---------------|--------------|
| **实现层面** | API 层（Java 类） | JVM 层（字节码） |
| **锁释放** | 手动 lock/unlock | 自动释放 |
| **锁尝试** | tryLock 可尝试 | 不可尝试 |
| **可中断** | 可中断 | 不可中断 |
| **多条件** | 多个 Condition | 单一条件 |
| **公平锁** | 支持公平/非公平 | 只能非公平 |
| **性能** | JDK 1.6 后两者接近 | 优化后接近 ReentrantLock |

**使用建议：**
- 优先用 synchronized（简洁）
- 需要高级功能时用 ReentrantLock

**记忆口诀：** API 手尝中多公（API 层、手动、尝试、中断、多条件、公平）

---

## 题 7：死锁产生的 4 个必要条件是什么？如何避免死锁？

**考点：** 死锁 4 条件 + 避免方法

**标准答案：**

**死锁 4 个必要条件（必须同时满足）：**

| 条件 | 说明 |
|------|------|
| **互斥条件** | 资源一次只能被一个线程占用 |
| **请求与保持条件** | 线程已持有资源，又申请新资源，但不释放已持有的 |
| **不可剥夺条件** | 线程已获得的资源，不能被强行剥夺，只能自己主动释放 |
| **循环等待条件** | 线程之间形成环形等待链：A 等 B，B 等 C，C 等 A |

**避免死锁的方法（破坏任一条件）：**

| 破坏条件 | 方法 | 示例 |
|---------|------|------|
| **破坏互斥** | 用 CAS/原子类替代锁 | AtomicInteger |
| **破坏请求与保持** | 一次性申请所有资源 | 同时获取 lockA 和 lockB |
| **破坏不可剥夺** | 设置超时，获取失败就释放 | tryLock(100ms) |
| **破坏循环等待**（最常用） | **按顺序申请资源** | 线程 A 和 B 都先 lockA 后 lockB |

**记忆口诀：** 互请不可循（互斥、请求、不可剥夺、循环）

**常见错误：**
- ❌ "不可剥夺"说成"可剥夺"（记反了）
- ❌ 避免方法说不全

---

## 题 8：happens-before 原则是什么？列举 3 个最常见的 happens-before 规则。

**考点：** happens-before 原则

**标准答案：**

**happens-before 是什么？**

happens-before 是 JMM 定义内存可见性的规则，它规定了哪些操作的结果对后续操作可见。即使没有同步措施，只要满足 happens-before 规则，操作就是可见的。

**8 大 happens-before 规则：**

| 序号 | 规则 | 说明 |
|------|------|------|
| 1 | **程序次序规则** | 单线程内，代码书写顺序保证前面的操作 happens-before 后面的操作 |
| 2 | **锁规则** | 解锁 (unlock) 一定 happens-before 后续对同一个锁的加锁 (lock) |
| 3 | **volatile 规则** | volatile 写 happens-before 后续对同一个 volatile 变量的读 |
| 4 | **传递性规则** | A happens-before B，B happens-before C → A happens-before C |
| 5 | **线程启动规则** | Thread.start() happens-before 该线程的任何操作 |
| 6 | **线程终止规则** | 线程的所有操作 happens-before Thread.join() 返回 |
| 7 | **线程中断规则** | 中断操作 happens-before 被中断线程检测到中断事件 |
| 8 | **对象终结规则** | 对象构造完成 happens-before finalize() 方法开始 |

**最常见的 3 个考点：**
1. **volatile 写→读**（可见性保证）
2. **锁释放→锁获取**（解锁前的修改对加锁后可见）
3. **线程启动→线程内操作**（start() 后的操作能看到启动前的修改）

**记忆口诀：** 程锁 vol 传启终断（程序次序、锁、volatile、传递、启动、终止、中断）

---

## 题 9：wait() 和 notify() 的作用是什么？它们有什么特点？使用时需要注意什么？

**考点：** wait/notify 机制

**标准答案：**

**wait() 和 notify() 是 Object 类的方法，用于线程间通信。**

| 方法 | 作用 | 是否释放锁 |
|------|------|-----------|
| **wait()** | 当前线程等待，释放锁 | ✅ 释放 |
| **notify()** | 唤醒一个等待线程 | ❌ 不释放（要等当前线程执行完） |
| **notifyAll()** | 唤醒所有等待线程 | ❌ 不释放 |

**使用场景：** 经典生产者 - 消费者模式
`java
synchronized (queue) {
    while (queue.isEmpty()) {
        queue.wait();  // 队列空，等待
    }
    // 消费数据
    queue.notify();  // 唤醒生产者
}
`

**注意事项：**
1. **必须在 synchronized 块中调用**（否则抛 IllegalMonitorStateException）
2. **wait() 要用 while 循环检查条件**（防止虚假唤醒）
3. **notify() 不释放锁**，要等当前 synchronized 块执行完才释放

**虚假唤醒：** 线程可能在没有 notify() 的情况下被唤醒，所以要用 while 循环检查条件

**记忆口诀：** wait 放锁，notify 不放

---

## 题 10：LockSupport 和 Condition 是什么？它们和 wait/notify 有什么区别？

**考点：** LockSupport/Condition

**标准答案：**

### LockSupport

**LockSupport 是 JDK 提供的底层线程阻塞/唤醒工具。**

`java
// 阻塞当前线程
LockSupport.park();

// 唤醒指定线程
LockSupport.unpark(thread);
`

**特点：**
- 比 wait/notify 更灵活（不需要 synchronized）
- 可以唤醒指定线程（notify 只能随机唤醒一个）
- **ReentrantLock、AQS 底层就是用 LockSupport 实现的**

---

### Condition

**Condition 是 Lock 接口的方法，实现类似 wait/notify 的功能。**

`java
ReentrantLock lock = new ReentrantLock();
Condition condition = lock.newCondition();

lock.lock();
try {
    condition.await();    // 类似 wait()
    condition.signal();   // 类似 notify()
} finally {
    lock.unlock();
}
`

**Condition vs wait/notify：**

| 特性 | wait/notify | Condition |
|------|-------------|-----------|
| **锁类型** | synchronized | ReentrantLock |
| **多条件** | ❌ 单一条件 | ✅ 多个 Condition |
| **灵活性** | 低 | 高 |

**多条件场景：**
`java
Condition notFull = lock.newCondition();   // 不满条件
Condition notEmpty = lock.newCondition();  // 不空条件

// 生产者
notFull.await();    // 等待不满
notEmpty.signal();  // 唤醒消费者

// 消费者
notEmpty.await();   // 等待不空
notFull.signal();   // 唤醒生产者
`

**记忆口诀：** LockSupport 灵，Condition 多条件

---

## 📊 Day 4 学习总结

| 题号 | 考点 | 掌握度 | 状态 |
|------|------|--------|------|
| 1 | JMM 三特性 | 4/5 | ✅ |
| 2 | volatile 作用 | 4/5 | ✅ |
| 3 | synchronized 用法 | 4.5/5 | ✅ |
| 4 | CAS 原理+ABA | 5/5 | ✅ 🎉 |
| 5 | 线程安全实现 | 5/5 | ✅ 🎉 |
| 6 | ReentrantLock vs synchronized | 4.5/5 | ✅ |
| 7 | 死锁 4 条件 | 4/5 | ✅ |
| 8 | happens-before 原则 | 4/5 | ✅ |
| 9 | wait/notify 机制 | 4.5/5 | ✅ |
| 10 | LockSupport/Condition | 4/5 | ✅ |

**总评：4.4/5** ✅

**薄弱项（已修复）：**
- ✅ CAS 原理+ABA：2.5/5 → 5/5
- ✅ 线程安全实现：3.5/5 → 5/5
- ✅ 死锁 4 条件：3/5 → 4/5

---

## 🔗 关联知识点

- **JMM**：volatile、synchronized 的理论基础
- **CAS**：AtomicXXX 原子类的底层实现
- **锁升级**：JDK 1.6 后 synchronized 的优化

---

*更新时间：2026-03-18 20:50*

