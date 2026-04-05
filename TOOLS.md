# TOOLS.md - Local Notes

Skills define _how_ tools work. This file is for _your_ specifics — the stuff that's unique to your setup.

## What Goes Here

Things like:

- Camera names and locations
- SSH hosts and aliases
- Preferred voices for TTS
- Speaker/room names
- Device nicknames
- Anything environment-specific
- Backup preferences

## Examples

```markdown
### Cameras

- living-room → Main area, 180° wide angle
- front-door → Entrance, motion-triggered

### SSH

- home-server → 192.168.1.100, user: admin

### TTS

- Preferred voice: "Nova" (warm, slightly British)
- Default speaker: Kitchen HomePod
```

---

## 📦 备份配置（重要！）

### 双仓库备份策略

**每次备份必须同时备份两个仓库！**

| 仓库 | 路径 | 远程地址 | 备份内容 |
|------|------|---------|---------|
| **OpenClaw** | `/root/.openclaw/workspace/` | github.com:LemonTeaViTA/OpenClaw.git | 学习记录、memory、技能配置 |
| **Obsidian** | `/root/.openclaw/workspace/01-Obsidian/` | github.com:LemonTeaViTA/Obsidian.git | 题库、笔记、Obsidian 配置 |

### 备份流程

```bash
# 1. OpenClaw 仓库
cd /root/.openclaw/workspace
git add -A
git commit -m "📚 学习记录"
git push origin main

# 2. Obsidian 仓库
cd /root/.openclaw/workspace/01-Obsidian
git add -A
git commit -m "📝 题库更新"
git push origin main
```

### 备份时机

- ✅ 每日学习结束后
- ✅ 创建重要文件后
- ✅ 用户明确要求备份时

## Why Separate?

Skills are shared. Your setup is yours. Keeping them apart means you can update skills without losing your notes, and share skills without leaking your infrastructure.

---

Add whatever helps you do your job. This is your cheat sheet.
