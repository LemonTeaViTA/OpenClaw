#!/bin/bash
# OpenClaw 自动备份脚本（Linux 版本）
# 使用 SSH Key 认证，无需 Token

set -e

# 进入工作区
cd /root/.openclaw/workspace

# 配置 Git 用户信息
git config user.name "LemonTeaViTA"
git config user.email "LemonTeaViTA@users.noreply.github.com"

# 添加所有变更
git add -A

# 检查是否有变更
if git diff --staged --quiet; then
    echo "✅ 没有变更，跳过备份"
    exit 0
fi

# 提交
timestamp=$(date "+%Y-%m-%d %H:%M:%S")
git commit -m "🔄 AutoBackup $timestamp"

# 推送到 GitHub
echo "📤 推送到 GitHub..."
git push origin main

echo "✅ 备份完成：$timestamp"
