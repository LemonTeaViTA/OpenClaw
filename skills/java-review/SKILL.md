---
name: java-review
description: Java 八股文复习技能。用于从题库中随机抽选题目进行复习，支持按篇章复习或混合复习。使用场景：(1) 开始每日复习 (2) 随机抽选题目 (3) 按指定篇章复习 (4) 复习薄弱题目。题库位置：/root/.openclaw/workspace/01-Obsidian/40-Questions/Java 八股文题库/
---

# Java 八股文复习技能

## 快速开始

```bash
# 开始每日复习（随机 10 题）
./scripts/java-review.py --mode daily --count 10

# 按篇章复习
./scripts/java-review.py --section java-basic --count 5

# 复习薄弱题目
./scripts/java-review.py --mode weak --count 5
```

## 题库结构

题库位于 `/root/.openclaw/workspace/01-Obsidian/40-Questions/Java 八股文题库/`，包含以下文件：

| 文件 | 内容 | ID 范围 |
|------|------|--------|
| `01-Java 基础篇.md` | Java 语言基础 | JAVA-001 ~ JAVA-066 |
| `02-集合框架篇.md` | 集合框架 | COLLECTION-001 ~ COLLECTION-037 |
| `03-并发编程篇.md` | 并发编程 | CONCURRENCY-001 ~ CONCURRENCY-104 |
| `04-JVM 篇.md` | JVM 相关 | JVM-001 ~ JVM-060 |
| `05-Redis 篇.md` | Redis 缓存 | REDIS-001 ~ REDIS-065 |
| `06-MySQL 篇.md` | MySQL 数据库 | MYSQL-001 ~ MYSQL-074 |
| `07-Spring 篇.md` | Spring 框架 | SPRING-001 ~ SPRING-048 |

## 复习流程

### 标准复习流程

1. **读取复习进度** - 从 `复习进度记录.md` 获取已复习/未复习题目
2. **抽选题目** - 根据模式随机选择题目
3. **出题** - 展示题目，等待用户回答
4. **评分** - 用户回答后显示解析和评分
5. **记录** - 更新复习进度和掌握情况

### 复习模式

| 模式 | 说明 | 使用场景 |
|------|------|----------|
| `daily` | 每日复习，混合各篇章 | 日常复习 |
| `section` | 指定篇章复习 | 专项突破 |
| `weak` | 薄弱题目复习 | 强化训练 |
| `random` | 完全随机 | 模拟面试 |

## 脚本使用

### java-review.py

主复习脚本，支持多种参数：

```bash
# 基本用法
./scripts/java-review.py --mode <模式> --count <题数>

# 参数说明
--mode      复习模式：daily, section, weak, random
--count     复习题目数量（默认 10）
--section   指定篇章：java-basic, collection, concurrency, jvm, redis, mysql, spring
--output    输出模式：console, feishu, wecom
```

### 题目格式

每道题目包含：
- **ID** - 唯一标识（如 JAVA-001）
- **题目** - 问题描述
- **答案要点** - 评分标准
- **解析** - 详细说明
- **难度** - 🟢简单/🟡中等/🔴困难

## 进度追踪

复习进度记录在 `复习进度记录.md` 中，格式：

```markdown
## 复习进度

| 篇章 | 总题数 | 已复习 | 掌握 | 待复习 | 进度 |
|------|--------|--------|------|--------|------|
| Java 基础 | 66 | 10 | 8 | 56 | 15% |
```

## 艾宾浩斯遗忘曲线

根据遗忘曲线自动安排复习：

| 间隔 | 复习时间点 |
|------|-----------|
| 第 1 次 | 学习后 20 分钟 |
| 第 2 次 | 1 小时后 |
| 第 3 次 | 9 小时后 |
| 第 4 次 | 1 天后 |
| 第 5 次 | 2 天后 |
| 第 6 次 | 6 天后 |
| 第 7 次 | 31 天后 |

## 相关技能

- **review-logger** - 复习记录与进度追踪
- **github-backup** - 自动备份学习记录到 GitHub

---

*创建时间：2026-04-03*
*版本：v1.0*
