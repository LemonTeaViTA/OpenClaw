#!/bin/bash
# Daily Backup Script for OpenClaw Workspace
# Runs at 12:00 and 24:00 daily
# Tasks:
# 1. Backup OpenClaw workspace to GitHub
# 2. Sync Obsidian vault
# 3. Pull latest PaiSmart code

set -e

# Configuration
WORKSPACE="C:\Users\11237\.openclaw-autoclaw\workspace"
PAISMART_DIR="C:\Users\11237\projects/PaiSmart"
VAULT_DIR="C:\Users\11237\vault"
LOG_FILE="C:\Users\11237\.openclaw-autoclaw\workspace/logs/backup-$(date +%Y%m%d).log"
PAT_ENV_VAR="GITHUB_PAT"

# Create log directory
mkdir -p "$(dirname "$LOG_FILE")"

log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" | tee -a "$LOG_FILE"
}

log "========== Backup Started =========="

# Check if PAT is configured
if [ -z "${!PAT_ENV_VAR}" ]; then
    log "ERROR: GitHub PAT not configured in environment variable $PAT_ENV_VAR"
    log "Please set: export GITHUB_PAT='your_pat_here'"
    exit 1
fi

# Task 1: Backup OpenClaw Workspace
log "Task 1: Backing up OpenClaw workspace..."
cd "$WORKSPACE"

# Configure git credential using PAT
git config --global credential.helper store
echo "https://${PAT_ENV_VAR}:x-oauth-basic@github.com" > ~/.git-credentials 2>/dev/null || true
chmod 600 ~/.git-credentials

# Check if remote is configured
REMOTE_URL="https://github.com/LemonTeaViTA/OpenClaw.git"
if ! git remote get-url origin >/dev/null 2>&1; then
    log "Configuring remote origin..."
    git remote add origin "$REMOTE_URL" || git remote set-url origin "$REMOTE_URL"
fi

# Commit and push changes
git add -A
if ! git diff --cached --quiet; then
    git commit -m "Auto-backup: $(date '+%Y-%m-%d %H:%M:%S')"
    log "Pushing workspace changes..."
    git push origin master 2>&1 | tee -a "$LOG_FILE"
else
    log "No changes to commit in workspace"
fi

# Task 2: Pull Latest PaiSmart Code
log "Task 2: Pulling latest PaiSmart code..."
if [ -d "$PAISMART_DIR" ]; then
    cd "$PAISMART_DIR"
    git fetch origin
    git checkout master
    git pull origin master 2>&1 | tee -a "$LOG_FILE"
    log "PaiSmart code updated successfully"
else
    log "WARNING: PaiSmart directory not found at $PAISMART_DIR"
fi

# Task 3: Sync Obsidian Vault
log "Task 3: Syncing Obsidian vault..."
if [ -d "$VAULT_DIR" ]; then
    cd "$VAULT_DIR"
    git fetch origin
    git pull origin master 2>&1 | tee -a "$LOG_FILE"
    
    # Commit any local changes
    git add -A
    if ! git diff --cached --quiet; then
        git commit -m "Auto-sync: $(date '+%Y-%m-%d %H:%M:%S')"
        git push origin master 2>&1 | tee -a "$LOG_FILE"
        log "Obsidian vault synced with changes"
    else
        log "No changes in Obsidian vault"
    fi
else
    log "WARNING: Vault directory not found at $VAULT_DIR"
    log "Skipping Obsidian sync"
fi

log "========== Backup Completed =========="
