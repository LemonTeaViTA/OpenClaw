# OpenClaw 定时备份脚本（PowerShell 版本）
# 用于 Windows Task Scheduler

$ErrorActionPreference = "Stop"

# 加载 Token 配置
$TokenFile = "C:\Users\11237\.secure_tokens.sh"
if (Test-Path $TokenFile) {
    Get-Content $TokenFile | ForEach-Object {
        if ($_ -match "^export\s+([A-Z_]+)=(.+)$") {
            $name = $matches[1]
            $value = $matches[2] -replace '^"', '' -replace '"$', ''
            [Environment]::SetEnvironmentVariable($name, $value, "Process")
        }
    }
}

# 进入工作区
Set-Location "C:\Users\11237\.openclaw-autoclaw\workspace"

# 配置 Git
git config user.name "LemonTeaViTA"
git config user.email "LemonTeaViTA@users.noreply.github.com"

# 添加文件
git add -A

# 检查是否有变更
$hasChanges = git diff --staged --quiet
if ($hasChanges) {
    Write-Host "No changes to backup"
    exit 0
}

# 提交
$timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
git commit -m "AutoBackup $timestamp"

# 推送（使用 Token）
$tokenUrl = "https://$env:BACKUP_GITHUB_TOKEN@github.com/LemonTeaViTA/OpenClaw.git"
git remote set-url origin $tokenUrl
git push origin HEAD:master --force
git remote set-url origin "https://github.com/LemonTeaViTA/OpenClaw.git"

Write-Host "Backup completed at $timestamp"
