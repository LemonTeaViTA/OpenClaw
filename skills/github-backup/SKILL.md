---
name: github-backup
description: GitHub 自动备份技能。用于将本地学习记录、题库、笔记等文件自动提交到 GitHub 仓库。使用场景：(1) 每日学习结束后备份 (2) 检测文件变更并 commit (3) 生成变更摘要 (4) 推送到远程仓库。支持增量备份和完整备份模式。
---

# GitHub 备份技能

## 快速开始

```bash
# 备份所有变更
./scripts/github-backup.py --backup

# 检查变更状态
./scripts/github-backup.py --status

# 手动提交
./scripts/github-backup.py --commit -m "每日复习记录 2026-04-03"

# 查看历史
./scripts/github-backup.py --log --count 10
```

## 备份范围

### 默认备份目录

| 目录 | 内容 | 优先级 |
|------|------|--------|
| `memory/` | 每日学习记录 | ⭐⭐⭐ 高 |
| `01-Obsidian/40-Questions/` | Java 八股文题库 | ⭐⭐⭐ 高 |
| `01-Obsidian/40-Questions/复习进度记录.md` | 复习进度 | ⭐⭐⭐ 高 |
| `AGENTS.md`, `SOUL.md` | 配置文件 | ⭐⭐ 中 |
| `skills/` | 自定义技能 | ⭐⭐ 中 |

### 排除文件

```
*.pyc
__pycache__/
*.log
.tmp/
```

## 脚本使用

### github-backup.py

```bash
# 完整备份流程（检查 + 提交 + 推送）
./scripts/github-backup.py --backup

# 仅检查变更
./scripts/github-backup.py --status

# 手动提交
./scripts/github-backup.py --commit -m "自定义提交信息"

# 推送远程
./scripts/github-backup.py --push

# 查看提交历史
./scripts/github-backup.py --log --count 20

# 生成变更摘要
./scripts/github-backup.py --summary --date today
```

### 参数说明

| 参数 | 说明 | 示例 |
|------|------|------|
| `--backup` | 完整备份流程 | |
| `--status` | 检查变更状态 | |
| `--commit` | 手动提交 | -m "提交信息" |
| `--push` | 推送到远程 | |
| `--log` | 查看提交历史 | --count 10 |
| `--summary` | 生成变更摘要 | --date today |
| `--dry-run` | 模拟运行（不实际提交） | |

## 提交信息规范

### 自动提交信息格式

```
<类型>: <描述>

- 变更 1
- 变更 2

📊 统计：+120 -30 | 文件：3
```

### 提交类型

| 类型 | 说明 | 示例 |
|------|------|------|
| `📚 学习` | 学习记录更新 | 📚 学习：2026-04-03 复习记录 |
| `📝 笔记` | 笔记文件更新 | 📝 笔记：Java 基础篇补充 |
| `🔧 配置` | 配置文件更新 | 🔧 配置：更新复习计划 |
| `✨ 技能` | 新增/更新技能 | ✨ 技能：新增 java-review |
| `🐛 修复` | 错误修复 | 🐛 修复：题库格式问题 |

## 变更摘要生成

### 摘要内容

```markdown
## 📊 2026-04-03 变更摘要

### 新增文件
- memory/2026-04-03.md (1107 行)

### 修改文件
- 01-Obsidian/40-Questions/复习进度记录.md (+50, -10)
- memory/2026-04-02.md (+20, -5)

### 统计
- 新增：1177 行
- 删除：15 行
- 文件：3 个
```

## Git 配置

### 仓库配置

```bash
# 仓库路径
REPO_PATH="/root/.openclaw/workspace"

# 远程仓库
REMOTE_URL="https://github.com/username/java-review-notes.git"

# 分支
BRANCH="main"
```

### 自动配置

脚本会自动检测并配置：
- 用户邮箱和姓名
- 远程仓库 URL
- 默认分支

## 定时备份

### Cron 配置

```bash
# 每日 23:00 自动备份
0 23 * * * /path/to/github-backup.py --backup >> /tmp/backup.log 2>&1

# 每小时检查变更
0 * * * * /path/to/github-backup.py --status --notify-if-changed
```

### 触发条件

- 每日学习结束后自动触发
- 检测到重要文件变更时
- 手动触发

## 安全注意事项

1. **不要提交敏感信息**
   - API 密钥
   - 密码
   - 个人隐私数据

2. **检查 .gitignore**
   - 确保敏感文件已排除
   - 定期审查排除规则

3. **私有仓库**
   - 学习记录建议设为私有
   - 公开前审查内容

## 相关文件

- **Git 配置**: `/root/.openclaw/workspace/.git/config`
- **忽略文件**: `/root/.openclaw/workspace/.gitignore`
- **提交历史**: `git log --oneline`

## 相关技能

- **java-review** - Java 八股文复习
- **review-logger** - 复习记录与进度追踪

---

*创建时间：2026-04-03*
*版本：v1.0*
