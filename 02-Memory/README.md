# 复习记录体系说明

## 📁 文件夹结构

```
memory/
├── sessions/          # 每日学习会话记录（完整流程）
├── reviews/           # 章节复习记录（艾宾浩斯）
├── random-review/     # 随机复习记录（每日 Java 基础 + 集合）
└── weaknesses/        # 薄弱项专项复习记录
```

## 🔄 每日执行流程

```
1️⃣ 学习新知识 → memory/sessions/YYYY-MM-DD-session-N.md
   ↓
2️⃣ 当前章节复习 → memory/reviews/章节-review-YYYY-MM-DD.md
   ↓
3️⃣ 随机复习 → memory/random-review/YYYY-MM-DD.md
   ↓
4️⃣ 薄弱项复习 → memory/weaknesses/YYYY-MM-DD.md
   ↓
更新 MEMORY.md（汇总 + 引用）
```

## 📊 各文件职责

### 1. memory/sessions/（会话记录）
- **内容**：当日 4 个环节的完整记录
- **命名**：`YYYY-MM-DD-session-N.md`
- **用途**：快速回顾"今天学了什么"

### 2. memory/reviews/（章节复习）
- **内容**：某个章节的艾宾浩斯复习记录
- **命名**：`章节-review-YYYY-MM-DD.md`
- **用途**：追踪某个章节的复习历史

### 3. memory/random-review/（随机复习）
- **内容**：每日随机抽取的 5-8 题
- **命名**：`YYYY-MM-DD.md`
- **用途**：防止已学章节遗忘

### 4. memory/weaknesses/（薄弱项）
- **内容**：得分<3.5 的知识点专项复习
- **命名**：`YYYY-MM-DD.md`
- **用途**：集中攻克薄弱点

## 🔗 与 MEMORY.md 的关系

**MEMORY.md 保持精简**，只包含：
- 薄弱项统计表（带引用链接）
- 学习进度汇总
- 文档索引

**详细记录在子文件夹**，通过 Markdown 链接引用：
```markdown
[详情](memory/reviews/jvm-day2-review-2026-03-19.md)
```

## 📅 追踪文件

### .review-tracker.json
```json
{
  "scheduledReviews": [
    {
      "topic": "JVM Day 2",
      "nextReview": "2026-03-22",
      "reviewCount": 2
    }
  ],
  "randomReview": {
    "lastReview": "2026-03-15",
    "nextReview": "2026-03-16"
  },
  "weaknesses": {
    "四种引用类型": {
      "score": 4,
      "nextReview": "2026-03-22"
    }
  }
}
```

**用途**：heartbeat 自动检查"今天该复习什么"

### .random-review-state.json
```json
{
  "lastReviewDate": "2026-03-15",
  "nextReviewDate": "2026-03-16"
}
```

**用途**：追踪随机复习执行状态

## 🎯 复习时间规则

### 艾宾浩斯曲线（当前章节复习）
- 第 1 次：学习后 1 天
- 第 2 次：学习后 3 天
- 第 3 次：学习后 7 天
- 第 4 次：学习后 15 天

### 薄弱项复习（根据得分）
- 5/5 → 7 天后
- 4/5 → 3 天后
- 3/5 → 1 天后
- <3/5 → 立即安排专项复习

### 随机复习
- **频率**：每日 1 次（20:00 后）
- **来源**：已学完章节（Java 基础 + 集合框架）
- **题数**：5-8 题

## 📝 文件模板

详见各文件夹中的示例文件。

---

*最后更新：2026-03-19*
