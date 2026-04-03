---
name: review-logger
description: 复习记录与进度追踪技能。用于自动记录复习结果、更新进度统计、生成复习报告。使用场景：(1) 复习结束后记录结果 (2) 更新复习进度 (3) 生成日报/周报 (4) 追踪艾宾浩斯复习曲线。
---

# 复习记录技能

## 快速开始

```bash
# 记录复习结果
./scripts/review-logger.py --record --questions JAVA-001,JAVA-002 --scores 4,5

# 生成今日报告
./scripts/review-logger.py --report --date today

# 更新进度统计
./scripts/review-logger.py --update-progress
```

## 记录格式

### 单日记录文件

位置：`/root/.openclaw/workspace/memory/YYYY-MM-DD.md`

```markdown
# 2026-04-03 学习记录

## 📚 今日复习

### 复习题目

| 题目 ID | 得分 | 掌握情况 | 复习次数 |
|---------|------|----------|----------|
| JAVA-001 | 4/5 | ✅ 已掌握 | 1 |
| JAVA-002 | 5/5 | ✅✅ 熟练 | 2 |
| MYSQL-013 | 3/5 | 🔄 需强化 | 3 |

### 正确率统计

| 篇章 | 复习数 | 正确率 |
|------|--------|--------|
| Java 基础 | 5 | 85% |
| MySQL | 3 | 70% |

### 薄弱题目

- MYSQL-013: count(*) vs count(1) - 需再次复习
- CONCURRENCY-011: 线程状态 - 概念混淆

## 📊 累计进度

总复习：120 题 | 掌握：95 题 | 待复习：25 题
```

## 脚本使用

### review-logger.py

```bash
# 记录复习结果
./scripts/review-logger.py --record \
  --questions "JAVA-001,JAVA-002,MYSQL-013" \
  --scores "4,5,3" \
  --time "2026-04-03 16:00"

# 生成报告
./scripts/review-logger.py --report \
  --date "2026-04-03" \
  --output "feishu"

# 更新进度
./scripts/review-logger.py --update-progress

# 获取待复习题目（艾宾浩斯）
./scripts/review-logger.py --get-due-questions
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `--record` | 记录复习结果 | |
| `--questions` | 题目 ID 列表（逗号分隔） | JAVA-001,JAVA-002 |
| `--scores` | 得分数组（逗号分隔） | 4,5,3 |
| `--report` | 生成报告 | |
| `--date` | 指定日期 | today, 2026-04-03 |
| `--update-progress` | 更新进度统计 | |
| `--output` | 输出格式 | console, feishu, markdown |

## 艾宾浩斯复习曲线

自动计算每道题目的下次复习时间：

```python
# 复习间隔（天）
REVIEW_INTERVALS = [0, 1, 2, 4, 7, 15, 30]

# 根据掌握程度调整
# 5/5 → 延长间隔
# 3/5 以下 → 缩短间隔，加入薄弱题列表
```

## 进度统计

### 总体进度

```json
{
  "total": 454,
  "reviewed": 120,
  "mastered": 95,
  "weak": 25,
  "accuracy": 85.5
}
```

### 篇章进度

| 篇章 | 总题数 | 已复习 | 掌握 | 正确率 |
|------|--------|--------|------|--------|
| Java 基础 | 66 | 30 | 25 | 83% |
| 集合框架 | 37 | 20 | 18 | 90% |
| ... | ... | ... | ... | ... |

## 报告生成

### 日报

- 今日复习题目数
- 正确率统计
- 薄弱题目列表
- 明日复习建议

### 周报

- 本周复习趋势
- 各篇章进度
- 掌握率变化
- 下周复习计划

## 相关文件

- **日记录**: `/root/.openclaw/workspace/memory/YYYY-MM-DD.md`
- **进度文件**: `/root/.openclaw/workspace/01-Obsidian/40-Questions/复习进度记录.md`
- **索引文件**: `/root/.openclaw/workspace/01-Obsidian/40-Questions/题库-ID 完整索引.md`

## 相关技能

- **java-review** - Java 八股文复习
- **github-backup** - 自动备份学习记录

---

*创建时间：2026-04-03*
*版本：v1.0*
