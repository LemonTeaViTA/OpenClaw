# 随机复习自动化脚本使用指南

## 📚 脚本功能

### 1. sync-review-state.ps1 - 同步复习状态
**功能**：将复习记录同步到状态文件  
**运行时机**：每次复习环节结束后

```powershell
# 手动运行
.\scripts\sync-review-state.ps1

# 自动模式（无提示）
.\scripts\sync-review-state.ps1 -AutoMode
```

### 2. random-review-selector.ps1 - 随机选题
**功能**：智能随机选题（12 题，包含 Java+ 集合+JVM）  
**运行时机**：随机复习开始前

```powershell
# 选择 12 题（默认）
.\scripts\random-review-selector.ps1

# 自动模式（发现未同步自动修复）
.\scripts\random-review-selector.ps1 -AutoMode
```

### 3. check-sync-status.ps1 - 检查同步状态
**功能**：检查所有状态文件和同步状态  
**运行时机**：随时检查

```powershell
# 基本检查
.\scripts\check-sync-status.ps1

# 详细信息
.\scripts\check-sync-status.ps1 -Detailed

# 自动修复（发现未同步自动运行同步脚本）
.\scripts\check-sync-status.ps1 -AutoFix
```

---

## 🔄 三重保险机制

### 第一重：复习后手动同步
```
复习结束 → 运行 sync-review-state.ps1 → 状态已同步
```

### 第二重：选题前自动检查
```
运行 random-review-selector.ps1
  ↓
检查是否有未同步的复习记录
  ↓
如果有 → 提示并自动运行同步脚本
  ↓
继续选题
```

### 第三重：Heartbeat 自动检查
```
Heartbeat 每小时检查
  ↓
发现新复习记录但未同步
  ↓
自动运行同步脚本 + 通知用户
```

---

## 📋 推荐工作流程

### 日常复习流程

```
1. 早上/下午：薄弱项复习
   ↓
2. 复习结束后立即运行
   .\scripts\sync-review-state.ps1
   ↓
3. 状态已同步 ✓

4. 晚上 20:00 后：随机复习
   ↓
5. 运行选题脚本
   .\scripts\random-review-selector.ps1 -AutoMode
   ↓
6. 开始随机复习（12 题）
   ↓
7. 复习结束后再次同步
   .\scripts\sync-review-state.ps1
```

### 检查状态

```powershell
# 随时检查同步状态
.\scripts\check-sync-status.ps1 -Detailed
```

---

## 📁 生成的文件

| 文件 | 功能 | 说明 |
|------|------|------|
| `.random-review-state.json` | 随机复习状态 | 记录已复习题目、排除列表 |
| `.review-tracker.json` | 复习追踪器 | 艾宾浩斯复习计划 |
| `.context-snapshot.json` | 上下文快照 | 当前学习进度 |
| `.today-random-review.json` | 今日选题 | 当天随机复习题目 |
| `memory/sync-logs/*.md` | 同步日志 | 每次同步的记录 |

---

## ⚠️ 注意事项

1. **复习后必须同步**  
   每次复习结束后立即运行 `sync-review-state.ps1`，确保状态文件是最新的

2. **选题脚本会自动检查**  
   如果忘记同步，`random-review-selector.ps1` 会自动检测并提示

3. **Heartbeat 兜底**  
   如果前两步都忘了，Heartbeat 会自动检查并同步

4. **题库范围**  
   - Java 基础篇：56 题
   - 集合框架篇：37 题
   - JVM 篇：66 题
   - **总计：159 题**

5. **选题策略**  
   - 模块均衡：Java/集合/JVM 各 4 题（共 12 题）
   - 薄弱项优先（未来版本）
   - 避免重复：自动排除已复习题目

---

## 🎯 快速命令

```powershell
# 同步状态（复习后）
.\scripts\sync-review-state.ps1

# 随机选题（复习前）
.\scripts\random-review-selector.ps1 -AutoMode

# 检查状态（随时）
.\scripts\check-sync-status.ps1 -Detailed

# 一键完成（检查 + 同步 + 选题）
.\scripts\check-sync-status.ps1 -AutoFix
.\scripts\random-review-selector.ps1 -AutoMode
```

---

## 📊 测试状态

✅ 所有脚本测试通过  
✅ JSON 编码问题已修复  
✅ 三重保险机制已实现  
✅ Heartbeat 集成已完成

**最后更新**：2026-03-22 17:40
