# 集合框架综合测试 - 2026-03-13

**日期**：2026-03-13 下午  
**题量**：10 题（原计划 20 题，用户要求到此为止）  
**总分**：约 46/50  
**平均分**：4.6/5  
**等级**：A

---

## 答题详情

| 题号 | 题目 | 得分 | 掌握度 | 问题 |
|------|------|------|--------|------|
| 1 | ArrayList 数据结构 | 5/5 | ✅ | 完全正确 |
| 2 | HashMap 1.7 vs 1.8 | 4.5/5 | ✅ | 知道红黑树，但不知道转换阈值 8 的原因 |
| 3 | HashMap 扩容机制 | 4.5/5 | ✅ | rehash 优化细节不完整 |
| 4 | ConcurrentHashMap 原理 | 5/5 | ✅ | 完全正确 |
| 5 | ConcurrentHashMap null 限制 | 5/5 | ✅ | 完全正确（上次 0/5，进步 +5） |
| 6 | HashSet vs ArrayList | 4/5 | ⚠️ | 说反了"允许重复" |
| 7 | LinkedHashMap vs TreeMap | 5/5 | ✅ | 完全正确 |
| 8 | 队列 vs 栈 | 4/5 | ⚠️ | 不知道队列的 Java 实现 |
| 9 | 阻塞队列实现方式 | 3.5/5 | ⚠️ | 不知道底层结构、锁机制 |
| 10 | hashCode + equals | 5/5 | ✅ | 完全正确 |

---

## 薄弱点分析

### 1. HashSet vs ArrayList（说反了）
- **错误**：说 HashSet 可以重复，ArrayList 不可以
- **正确**：HashSet 不允许重复，ArrayList 允许重复
- **原因**：紧张口误
- **复习点**：HashSet 底层是 HashMap（key 唯一性保证不重复）

### 2. 队列的 Java 实现
- **问题**：不知道 Queue 接口
- **补充**：
  - 普通队列：`Queue<Integer> queue = new LinkedList<>()`
  - 双端队列：`Deque<Integer> deque = new ArrayDeque<>()`
  - 栈（推荐）：`Deque<Integer> stack = new ArrayDeque<>()`

### 3. 阻塞队列实现方式
- **问题**：只知道名称，不知道底层实现
- **补充**：
  - ArrayBlockingQueue：数组 + 一把锁（ReentrantLock）
  - LinkedBlockingQueue：链表 + 两把锁（takeLock + putLock）
  - SynchronousQueue：无存储，直接传递（CAS + 等待队列）

---

## 高光时刻

- ✅ **ConcurrentHashMap null 限制**：从 0/5 提升到 5/5，完全掌握！
- ✅ **hashCode + equals**：完全理解只重写一个的后果
- ✅ **LinkedHashMap vs TreeMap**：清晰区分双向链表 vs 红黑树

---

## 集合框架总结

**掌握情况**：
- ArrayList：✅ 完全掌握
- HashMap：✅ 完全掌握（数据结构、扩容、rehash 优化）
- ConcurrentHashMap：✅ 完全掌握（1.7 vs 1.8、null 限制）
- HashSet：✅ 基本掌握（底层 HashMap）
- LinkedHashMap/TreeMap：✅ 完全掌握
- 队列/栈：✅ 基本掌握
- 阻塞队列：✅ 基本掌握

**集合框架 正式收官！** 🎉

---

## 下一步计划

- JVM Day 2：垃圾回收基础（全新知识）
- JVM Day 1 第 2 次复习：2026-03-15（3 天后）

---

*记录时间：2026-03-13 15:05 GMT+8*
