# 复习系统测试流程 (System Test Procedures)

**目的**：确保复习记录→状态同步→MEMORY.md 更新流程正常工作，避免数据丢失。

---

## 🧪 测试场景

### 场景 1：复习后会话同步（核心流程）

**触发时机**：每次复习会话结束后

**测试步骤**：
1. 创建模拟复习记录文件
2. 运行同步脚本
3. 验证状态文件更新
4. 验证 MEMORY.md 更新

**预期结果**：
- ✅ `.random-review-state.json` 更新（questionCount、score）
- ✅ `.context-snapshot.json` 更新（todaySession.completed）
- ✅ `memory/sync-logs/` 创建同步日志
- ✅ `MEMORY.md` 更新（薄弱项表格、复习总结）

---

### 场景 2：随机复习选题

**触发时机**：每日随机复习前（20:00 后）

**测试步骤**：
1. 运行检查脚本（确认无未同步记录）
2. 运行选题脚本
3. 验证 `.today-random-review.json` 生成

**预期结果**：
- ✅ 检查无未同步文件
- ✅ 生成 10-15 道随机题目
- ✅ 题目均匀分布（Java/集合/JVM）
- ✅ 排除已复习题目

---

### 场景 3：Heartbeat 自动检查

**触发时机**：每次 Heartbeat 轮询

**测试步骤**：
1. Heartbeat 检查 `.random-review-state.json`
2. 如果 `lastReviewDate < today` 且 `时间 > 20:00` → 提醒用户
3. 如果 `memory/dialogs/` 有未同步文件 → 提醒同步

**预期结果**：
- ✅ 自动检测未同步记录
- ✅ 自动提醒随机复习
- ✅ 不阻塞正常流程

---

## 📋 测试清单

### 每次系统更新后必测

- [ ] **检查脚本**：`check-sync-status.ps1` 正常运行
- [ ] **同步脚本**：`sync-review-state.ps1` 能正确扫描 dialogs 目录
- [ ] **选题脚本**：`random-review-selector.ps1` 排除已复习题目
- [ ] **状态文件**：JSON 格式正确，无编码问题
- [ ] **MEMORY.md**：模板正确，表格更新正常

### 每周测试（周日 22:00）

- [ ] 完整复习流程测试（创建记录→同步→更新 MEMORY.md）
- [ ] Git 备份测试（推送成功）
- [ ] Heartbeat 提醒测试

---

## 🐛 已知问题与解决方案

### 问题 1：同步脚本未执行导致数据丢失

**症状**：
- `memory/dialogs/` 有复习记录
- `.random-review-state.json` 未更新
- `MEMORY.md` 缺少最新数据

**根因**：
- 复习结束后忘记运行同步脚本
- AI 没有自动触发同步

**解决方案**：
1. ✅ 修复同步脚本（扫描 dialogs 目录）
2. ⏳ 添加自动同步（会话结束时自动运行）
3. ⏳ Heartbeat 检查未同步文件

---

### 问题 2：Git 备份认证失败

**症状**：
- 本地提交成功
- 推送失败（credential 错误）

**根因**：
- Token 过期
- Git credential 缓存失效

**解决方案**：
1. 手动刷新 Token：运行 `C:\Users\11237\.secure_tokens.sh`
2. 检查 Git 配置：`git config --global credential.helper`
3. 备用方案：手动推送

---

### 问题 3：MEMORY.md 模板不匹配

**症状**：
- 同步脚本运行成功
- MEMORY.md 未更新

**根因**：
- MEMORY.md 模板变更
- 同步脚本中的字符串匹配失败

**解决方案**：
1. 检查 MEMORY.md 最新模板
2. 更新同步脚本中的匹配字符串
3. 添加模板版本检测

---

## 🔧 快速诊断命令

```powershell
# 1. 检查同步状态
cd C:\Users\11237\.openclaw-autoclaw\workspace\scripts
.\check-sync-status.ps1 -Detailed

# 2. 手动同步（如果有未同步文件）
.\sync-review-state.ps1 -AutoMode

# 3. 生成今日随机复习题目
.\random-review-selector.ps1 -QuestionCount 12

# 4. 检查状态文件
Get-Content ..\.random-review-state.json | ConvertFrom-Json | ConvertTo-Json -Depth 10

# 5. 检查同步日志
Get-ChildItem ..\memory\sync-logs -Filter "*.md" | Sort-Object LastWriteTime -Descending | Select-Object -First 5
```

---

## 📊 系统健康指标

| 指标 | 正常值 | 告警值 | 检查频率 |
|------|--------|--------|----------|
| 同步延迟 | <1 小时 | >24 小时 | Heartbeat |
| 状态文件更新 | 每日 | >2 天未更新 | Heartbeat |
| Git 备份成功率 | 100% | <90% | 每日检查 |
| MEMORY.md 更新 | 同步后即时 | >1 小时未更新 | 每次会话 |
| 随机复习完成率 | 100% | <80% | 每日检查 |

---

## 🚨 紧急修复流程

### 当发现数据不同步时

**步骤 1：诊断**
```powershell
.\check-sync-status.ps1 -Detailed
```

**步骤 2：手动同步**
```powershell
.\sync-review-state.ps1 -AutoMode
```

**步骤 3：验证**
```powershell
# 检查状态文件
Get-Content ..\.random-review-state.json | ConvertFrom-Json

# 检查 MEMORY.md（最新 50 行）
Get-Content ..\MEMORY.md -Tail 50
```

**步骤 4：手动更新 MEMORY.md（如需要）**
- 读取 `memory/dialogs/` 最新记录
- 手动编辑 MEMORY.md 添加数据
- 记录到 `memory/sync-logs/`

---

## 📝 更新日志

| 日期 | 变更 | 负责人 |
|------|------|--------|
| 2026-03-23 | 添加 dialogs 目录扫描 | AI |
| 2026-03-23 | 创建系统测试文档 | AI |
| 2026-03-23 | 修复 check-sync-status.ps1 | AI |
| 2026-03-23 | 修复 random-review-selector.ps1 | AI |

---

**最后更新**：2026-03-23 08:30  
**下次测试**：2026-03-24（周日 22:00 完整流程测试）
