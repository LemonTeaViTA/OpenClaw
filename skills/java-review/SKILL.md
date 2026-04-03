---
name: java-review
description: Java 八股文复习技能。从所有题库篇章中随机抽选题目进行复习，支持每日混合复习、按篇章复习、薄弱题强化。题库覆盖：Java 基础、集合框架、并发编程、JVM、Redis、MySQL、Spring 共 7 大板块 454 题。使用场景：(1) 开始每日复习 (2) 随机抽选题目 (3) 专项突破 (4) 薄弱题强化。
---

# Java 八股文复习技能

## 快速开始

```bash
# 每日复习（从所有未复习题目中随机抽选 10 题）
./scripts/java-review.py --mode daily --count 10

# 按篇章复习
./scripts/java-review.py --section java-basic --count 5

# 复习薄弱题目
./scripts/java-review.py --mode weak --count 5
```

## 题库结构

题库位于 `/root/.openclaw/workspace/01-Obsidian/40-Questions/`：

| 篇章 | 文件 | ID 范围 | 题数 |
|------|------|---------|------|
| **Java 基础** | `Java 基础篇 - 完整题库.md` | JAVA-001 ~ JAVA-066 | 66 |
| **集合框架** | `集合框架篇 - 完整题库.md` | COLLECTION-001 ~ COLLECTION-037 | 37 |
| **并发编程** | `并发编程篇 - 完整题库.md` | CONCURRENCY-001 ~ CONCURRENCY-104 | 104 |
| **JVM** | `JVM 篇 - 完整题库.md` | JVM-001 ~ JVM-060 | 60 |
| **Redis** | `Redis 篇 - 完整题库.md` | REDIS-001 ~ REDIS-065 | 65 |
| **MySQL** | `MySQL 篇 - 完整题库.md` | MYSQL-001 ~ MYSQL-074 | 74 |
| **Spring** | `Spring 篇 - 完整题库.md` | SPRING-001 ~ SPRING-048 | 48 |
| **总计** | **7 个主题库** | - | **454** |

## 复习流程

### 标准复习流程

1. **读取进度** - 从 `复习进度记录.md` 获取已复习题目 ID
2. **加载题库** - 从 7 个篇章文件中解析所有题目
3. **过滤题目** - 排除已复习的，从未复习的中抽选
4. **出题** - 展示题目，等待用户回答
5. **评分** - 用户回答后显示解析和评分
6. **记录** - 更新复习进度和掌握情况

### 复习模式

| 模式 | 说明 | 抽选范围 | 使用场景 |
|------|------|----------|----------|
| `daily` | 每日复习 | 所有未复习题目 | 日常复习 |
| `section` | 指定篇章 | 指定篇章未复习题目 | 专项突破 |
| `weak` | 薄弱题目 | 掌握度<3/5 的题目 | 强化训练 |
| `random` | 完全随机 | 所有题目（含已复习） | 模拟面试 |

## 脚本使用

### java-review.py

```bash
# 基本用法
./scripts/java-review.py --mode <模式> --count <题数>

# 参数说明
--mode      复习模式：daily, section, weak, random
--count     复习题目数量（默认 10）
--section   指定篇章：java-basic, collection, concurrency, jvm, redis, mysql, spring
--output    输出模式：console, feishu, wecom
```

### 示例

```bash
# 每日复习 10 题
./scripts/java-review.py --mode daily --count 10

# Java 基础专项复习 5 题
./scripts/java-review.py --section java-basic --count 5

# Redis 和 MySQL 混合复习
./scripts/java-review.py --section redis,mysql --count 10

# 薄弱题强化
./scripts/java-review.py --mode weak --count 5
```

## 题目格式

每道题目包含：
- **ID** - 唯一标识（如 JAVA-001）
- **题目** - 问题描述
- **答案要点** - 评分标准
- **解析** - 详细说明
- **难度** - 🟢简单/🟡中等/🔴困难

## 进度追踪

复习进度记录在 `复习进度记录.md` 中：

```markdown
## 📊 总体进度

| 板块 | 总题数 | 已复习 | 掌握 | 待复习 | 进度 |
|------|--------|--------|------|--------|------|
| Java 基础 | 66 | 10 | 8 | 56 | 15% |
| 集合框架 | 37 | 5 | 4 | 32 | 14% |
| ... | ... | ... | ... | ... | ... |
```

## 艾宾浩斯遗忘曲线

根据遗忘曲线自动安排复习：

| 间隔 | 复习时间点 | 说明 |
|------|-----------|------|
| 第 1 次 | 学习后 20 分钟 | 短期记忆 |
| 第 2 次 | 1 小时后 | 巩固记忆 |
| 第 3 次 | 9 小时后 | 加深印象 |
| 第 4 次 | 1 天后 | 长期记忆 |
| 第 5 次 | 2 天后 | 强化 |
| 第 6 次 | 6 天后 | 巩固 |
| 第 7 次 | 31 天后 | 永久记忆 |

## 相关技能

- **review-logger** - 复习记录与进度追踪
- **github-backup** - 自动备份学习记录到 GitHub

---

*创建时间：2026-04-03*  
*版本：v1.1*  
*题库版本：454 题（7 大篇章）*
