# 🔐 Git 备份配置指南（安全版）

## ⚠️ 重要安全提示

**绝对不要在聊天、代码或日志中明文存储 GitHub PAT！**

---

## 🛠️ 推荐配置：Git Credential Manager（Windows）

### 方案 1：使用 Git Credential Manager（推荐）

**优点**：
- ✅ Windows 内置，无需手动管理 PAT
- ✅ 凭据加密存储在 Windows 凭据管理器
- ✅ 自动刷新 Token
- ✅ 最安全

**配置步骤**：

1. **启用 Credential Manager**：
```powershell
git config --global credential.helper wincred
```

2. **首次推送时输入凭据**：
```powershell
cd C:\Users\11237\.openclaw-autoclaw\workspace
git add .
git commit -m "Initial commit"
git push
# 会弹出窗口要求输入 GitHub 账号密码
# 密码输入 PAT，勾选"记住凭据"
```

3. **验证配置**：
```powershell
git config --global credential.helper
# 输出：wincred
```

---

### 方案 2：使用 SSH Key（备选）

**优点**：
- ✅ 最安全，无需 PAT
- ✅ 配置一次，永久使用

**配置步骤**：

1. **生成 SSH Key**：
```powershell
ssh-keygen -t ed25519 -C "your_email@example.com"
# 按回车使用默认路径
```

2. **添加 SSH Key 到 GitHub**：
```powershell
# 复制公钥
cat ~/.ssh/id_ed25519.pub | clip
# 粘贴到 GitHub: Settings → SSH and GPG keys → New SSH key
```

3. **切换远程仓库为 SSH**：
```powershell
git remote set-url origin git@github.com:LemonTeaViTA/OpenClaw.git
```

4. **测试连接**：
```powershell
ssh -T git@github.com
# 输出：Hi LemonTeaViTA! You've successfully authenticated
```

---

## 📋 备份任务说明

| 时间 | 任务 |
|------|------|
| 每天 12:00 | 1. 备份 OpenClaw workspace 到 GitHub<br>2. 同步 Obsidian vault |
| 每天 22:30 | 1. 备份 OpenClaw workspace 到 GitHub<br>2. 同步 Obsidian vault |

---

## 📁 文件结构

```
C:\Users\11237\.openclaw-autoclaw\workspace/
├── scripts/
│   ├── sync-oc-backup-push.sh    # OpenClaw 备份脚本
│   ├── sync-obsidian-backup-push.sh  # Obsidian 备份脚本
│   └── README-BACKUP.md          # 本文件
└── logs/
    └── oc-backup.log             # 备份日志
```

---

## 🔍 故障排查

### 问题 1：认证失败
```
remote: Invalid username or password
```

**解决**：
1. 清除旧凭据：
```powershell
cmdkey /list | findstr github
cmdkey /delete:LegacyGeneric:target=https://github.com
```

2. 重新推送：
```powershell
git push
# 重新输入凭据
```

### 问题 2：Git 推送失败
```
remote: Permission denied
```

**解决**：
- 确认有仓库写入权限
- 检查远程仓库 URL：`git remote -v`

### 问题 3：备份脚本失败

**解决**：
- 查看日志：`Get-Content C:\Users\11237\logs\oc-backup.log -Tail 50`
- 检查网络连接
- 手动运行脚本测试

---

## 🔐 安全最佳实践

1. ✅ **使用 Credential Manager**，不要明文存储 PAT
2. ✅ **定期轮换** 凭据（建议每 90 天）
3. ✅ **最小权限**：只授予必要的权限
4. ✅ **日志审计**：定期检查备份日志
5. ❌ **永远不要**在聊天、邮件、代码中发送 PAT

---

## 📞 需要帮助？

如果遇到问题，请提供：
1. 备份日志内容
2. `git remote -v` 输出
3. 错误信息

---

## 📝 更新日志

| 日期 | 变更 |
|------|------|
| 2026-03-23 | 移除 PAT 明文存储，改用 Credential Manager |
| 2026-03-23 | 清理历史 PAT 泄露记录 |
