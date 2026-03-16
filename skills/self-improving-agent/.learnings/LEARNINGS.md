# Learnings Log

Captured learnings, corrections, and discoveries. Review before major tasks.

---

## 2026-03-05

### ✅ 语音转文字方案确定
**类型：** correction  
**场景：** 用户发送语音，但 AI 无法直接听取  
**解决方案：** 使用飞书自带语音转文字 → 复制文字稿 → AI 过滤口语 → 记录答案  
**改进：** 后续对话采用此方案，避免安装复杂 STT skill

### ✅ 日报双时段方案
**类型：** best_practice  
**场景：** 用户需要学习计划提醒  
**方案：** 
- 早 9 点：学习计划 + 鼓励语（用户说"日报"触发）
- 晚 23 点：今日总结 + 完成情况（用户说"总结"触发）

### ✅ 答题记录系统建立
**类型：** best_practice  
**场景：** 需要追踪学习进度和薄弱项  
**方案：**
- MEMORY.md 记录摘要和看板
- memory/question-log/ 记录详细答题日志
- 5 分制评分 + 艾宾浩斯复习点
- 得分<3 的题目 3 天后复习，得分 5 的题目 7 天后复习

### ⚠️ self-improving hook 不兼容
**类型：** error  
**场景：** 尝试启用 self-improvement hook 失败  
**原因：** 该 skill 是为 Clawdbot 设计的，hook 元数据使用 `clawdbot` 标识，OpenClaw 不识别  
**解决：** 改用手动记录方式，功能相同无需 hook

---
