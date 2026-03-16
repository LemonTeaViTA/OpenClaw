#!/bin/bash
set -e

# Load tokens
source "$(dirname "$0")/../.secure_tokens.sh"

echo "Starting OpenClaw backup..."
cd "$(dirname "$0")/.."

git config user.name "$GITHUB_USER"
git config user.email "$GITHUB_USER@users.noreply.github.com"

# Add token to URL
TOKEN_URL=$(echo "$GITHUB_REPO_OPENCLAW" | sed 's|https://|https://${BACKUP_GITHUB_TOKEN}@|')
git remote set-url origin "$TOKEN_URL"

git add -A

if git diff --staged --quiet; then
    echo "No changes to backup"
else
    git commit -m "AutoBackup $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin HEAD:master --force
    echo "Backup completed!"
fi

git remote set-url origin "$GITHUB_REPO_OPENCLAW"
