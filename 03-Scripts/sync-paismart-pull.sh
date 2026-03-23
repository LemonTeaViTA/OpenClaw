#!/bin/bash
set -e

source "$(dirname "$0")/../.secure_tokens.sh"

echo "ðŸ”„ Pulling PaiSmart latest code..."
cd "$(dirname "$0")/../PaiSmart"

git config user.name "$GITHUB_USER"
git config user.email "$GITHUB_USER@users.noreply.github.com"

TOKEN_URL="https://${PAISMART_GITHUB_TOKEN}@github.com/LemonTeaViTA/PaiSmart.git"
git remote set-url origin "$TOKEN_URL"

git fetch origin
git reset --hard origin/main

git remote set-url origin "$GITHUB_REPO_PAISMART"
echo "âœ?PaiSmart updated!"
