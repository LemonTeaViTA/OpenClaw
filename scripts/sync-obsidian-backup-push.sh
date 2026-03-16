#!/bin/bash
set -e

source "$(dirname "$0")/../.secure_tokens.sh"

echo "ðŸ”„ Backing up Obsidian notes..."
cd "$(dirname "$0")/../Obsidian"

git config user.name "$GITHUB_USER"
git config user.email "$GITHUB_USER@users.noreply.github.com"

TOKEN_URL="https://${BACKUP_GITHUB_TOKEN}@github.com/LemonTeaViTA/Obsidian.git"
git remote set-url origin "$TOKEN_URL"

git add -A

if git diff --staged --quiet; then
    echo "âœ?No changes to backup"
else
    git commit -m "AutoBackup Obsidian $(date '+%Y-%m-%d %H:%M:%S')"
    git push origin HEAD:master --force
    echo "âœ?Obsidian backup pushed!"
fi

git remote set-url origin "$GITHUB_REPO_OBSIDIAN"
echo "ðŸŽ‰ Done!"
