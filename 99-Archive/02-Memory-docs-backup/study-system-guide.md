# 📋 复习系统使用指南

> 本文档说明如何运行和维护丁同学的 Java 复习系统

---

## 🗂️ 文件结构

```
C:\Users\11237\.openclaw-autoclaw\workspace/
├── MEMORY.md                              # 主记忆文件（答题记录 + 掌握看板）
├── memory/
│   ├── question-log/                      # 答题详细日志
│   │   └── 2026-03-05-java-base-pretest.md
│   ├── daily-report-template.md           # 日报模板
│   └── heartbeat-state.json               # 心跳状态（可选）
└── files/
    ├── java-notes/                        # Java 基础 PDF
    ├── jvm-notes/                         # JVM PDF
    ├── concurrent-notes/                  # 并发编程 PDF
    └── collection-notes/                  # 集合框架 PDF
```

---

## 📊 评分标准（5 分制）

| 分数 | 等级 | 标准 | 复习间隔 |
|------|------|------|----------|
| 5 | A | 完整准确，有延伸理解 | 7 天 |
| 4 | B | 核心正确，细节缺失 | 3 天 |
| 3 | C | 部分正确，需要提示 | 1 天 |
| 2 | D | 错误较多，概念模糊 | 当天重测 |
| 1 | E | 完全不会 | 立即讲解后重测 |

---

## 🔄 艾宾浩斯复习点

```
答题日期 → 复习节点：
Day 0 (当天) → Day 1 → Day 3 → Day 7 → Day 14 → Day 30
```

每次复习后根据新得分调整下次间隔：
- 得分 5 分：间隔×2
- 得分 3-4 分：间隔不变
- 得分 1-2 分：间隔÷2

---

## ⏰ 日报推送设置

### 方案 A：使用系统 cron（推荐）

1. 编辑 crontab：
```bash
crontab -e
```

2. 添加任务（每天 09:00）：
```bash
0 9 * * * C:\Users\11237\.openclaw-autoclaw\workspace\scripts/send-daily-report.sh
```

3. 创建脚本 `C:\Users\11237\.openclaw-autoclaw\workspace\scripts/send-daily-report.sh`：
```bash
#!/bin/bash
# 调用 OpenClaw 发送日报
# 具体实现取决于你的消息推送方式
```

### 方案 B：使用 OpenClaw heartbeat

在 `HEARTBEAT.md` 中添加：
```markdown
- 每天 09:00 检查并发送日报
```

然后在每次 heartbeat 时检查时间并推送。

### 方案 C：手动触发

每天上午对 OpenClaw 说："发送今日日报"

---

## 📈 周报生成

每周日 20:00 自动生成，包含：
- 本周答题统计（题目数、平均分、等级分布）
- 薄弱项分析（得分<3 的题目）
- 下周计划

---

## 📝 答题记录流程

### 测试时：
1. 出题（每次 1 题）
2. 接收用户回答（文字或语音）
3. 评分（1-5 分）
4. 记录到 `memory/question-log/日期-主题.md`
5. 更新 `MEMORY.md` 第 7、8 章节

### 复习时：
1. 检查 `MEMORY.md` 第 7 章节的"下次复习"列
2. 筛选到期题目
3. 重新测试
4. 更新得分和下次复习时间

---

## 🎯 1 周 1 个 PDF 节奏

| 周次 | 日期范围 | PDF | 题目数 | 目标 |
|------|----------|-----|--------|------|
| 第 10 周 | 03-03 ~ 03-09 | Java 基础 | 56 题 | 完成 |
| 第 11 周 | 03-10 ~ 03-16 | JVM | ~40 题 | 完成 |
| 第 12 周 | 03-17 ~ 03-23 | 并发编程 | ~50 题 | 完成 |
| 第 13 周 | 03-24 ~ 03-30 | 集合框架 | ~40 题 | 完成 |

---

## 🛠️ 维护命令

### 查看答题日志
```bash
ls -lt C:\Users\11237\.openclaw-autoclaw\workspace/memory/question-log/
```

### 查看待复习题目
```bash
grep "下次复习" C:\Users\11237\.openclaw-autoclaw\workspace/MEMORY.md
```

### 更新进度
编辑 `MEMORY.md` 第 8 章节"知识点掌握看板"

---

## 📞 问题排查

**问题：** 忘记记录答题分数  
**解决：** 回忆大概表现，补录到日志，下次注意

**问题：** 复习时间冲突  
**解决：** 手动调整"下次复习"日期，优先复习得分低的题目

**问题：** 进度落后  
**解决：** 周末加练或调整下周计划，保证质量优先

---

*最后更新：2026-03-05 15:00 GMT+8*
