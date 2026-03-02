# 🔐 定时备份任务配置指南

## ⚠️ 紧急安全警告

**你之前在消息中暴露了 GitHub PAT**：
```
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
```

**请立即执行以下操作：**

1. **前往 GitHub 撤销该 PAT**：
   - https://github.com/settings/tokens
   - 找到对应 token，点击 "Revoke"

2. **重新生成 PAT**，权限要求：
   - ✅ `repo` (完整仓库控制)
   - ✅ `workflow` (可选，如需 CI/CD)

3. **不要在任何聊天中发送 PAT**，只通过安全渠道配置

---

## 🛠️ 配置步骤

### 步骤 1：编辑环境变量文件

```bash
nano /root/.openclaw/workspace/.env.backup
```

将 `YOUR_PAT_HERE` 替换为你的新 PAT：
```bash
export GITHUB_PAT="ghp_xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

保存后设置权限：
```bash
chmod 600 /root/.openclaw/workspace/.env.backup
```

### 步骤 2：运行配置脚本

```bash
/root/.openclaw/workspace/scripts/setup-cron.sh
```

### 步骤 3：验证配置

```bash
# 查看 crontab
crontab -l

# 手动测试运行一次
source /root/.openclaw/workspace/.env.backup
/root/.openclaw/workspace/scripts/daily-backup.sh

# 查看日志
cat /root/.openclaw/workspace/logs/backup-$(date +%Y%m%d).log
```

---

## 📋 任务说明

| 时间 | 任务 |
|------|------|
| 每天 12:00 | 1. 备份 OpenClaw workspace 到 GitHub<br>2. 同步 Obsidian vault<br>3. 拉取 PaiSmart 最新代码 |
| 每天 24:00 | 同上 |

---

## 📁 文件结构

```
/root/.openclaw/workspace/
├── .env.backup              # PAT 环境变量 (权限 600)
├── scripts/
│   ├── daily-backup.sh      # 主备份脚本
│   ├── setup-cron.sh        # Cron 配置脚本
│   └── README-BACKUP.md     # 本文件
└── logs/
    └── backup-YYYYMMDD.log  # 每日备份日志
```

---

## 🔍 故障排查

### 问题 1：PAT 无效
```
ERROR: GitHub PAT not configured
```
**解决**：检查 `.env.backup` 文件中 PAT 是否正确配置

### 问题 2：Git 推送失败
```
remote: Permission denied
```
**解决**：确认 PAT 有 `repo` 权限，且仓库 URL 正确

### 问题 3：Cron 未执行
```bash
# 检查 cron 服务状态
systemctl status cron

# 查看 cron 日志
grep CRON /var/log/syslog
```

---

## 🔐 安全最佳实践

1. **永远不要**在聊天、邮件、代码中明文发送 PAT
2. **定期轮换** PAT（建议每 90 天）
3. **最小权限**：只授予必要的权限
4. **文件权限**：`.env.backup` 必须是 600
5. **日志审计**：定期检查备份日志

---

## 📞 需要帮助？

如果遇到问题，请提供：
1. 备份日志内容
2. `crontab -l` 输出
3. 错误信息截图
