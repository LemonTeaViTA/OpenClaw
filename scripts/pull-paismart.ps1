# PaiSmart 每日拉取脚本（PowerShell 版本）
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

# 进入项目目录
Set-Location "C:\Users\11237\.openclaw-autoclaw\workspace\PaiSmart"

# 配置 Git
git config user.name "LemonTeaViTA"
git config user.email "LemonTeaViTA@users.noreply.github.com"

# 拉取最新代码（使用 Token）
$tokenUrl = "https://$env:PAISMART_GITHUB_TOKEN@github.com/LemonTeaViTA/PaiSmart.git"
git remote set-url origin $tokenUrl
git fetch origin
git reset --hard origin/main
git remote set-url origin "https://github.com/LemonTeaViTA/PaiSmart.git"

Write-Host "PaiSmart updated at $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')"
