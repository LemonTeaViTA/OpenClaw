#!/bin/bash
# Setup cron jobs for daily backup
# Run this script once to configure the定时任务

CRON_FILE="/tmp/openclaw-cron"
BACKUP_SCRIPT="C:\Users\11237\.openclaw-autoclaw\workspace/scripts/daily-backup.sh"
ENV_FILE="C:\Users\11237\.openclaw-autoclaw\workspace/.env.backup"

# Create cron entries (12:00 and 24:00 daily)
cat > "$CRON_FILE" << EOF
# OpenClaw Daily Backup Tasks
# Runs at 12:00 (noon) and 24:00 (midnight)

0 12 * * * source $ENV_FILE && $BACKUP_SCRIPT
0 0 * * * source $ENV_FILE && $BACKUP_SCRIPT
EOF

# Install crontab
crontab "$CRON_FILE"

# Verify
echo "Cron jobs installed successfully:"
crontab -l

# Cleanup
rm -f "$CRON_FILE"
