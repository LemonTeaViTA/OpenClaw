# session-start-check.ps1
# Function: Check and fix state at session start
# Trigger: At the beginning of each AI session

$ErrorActionPreference = "Stop"
$workspaceRoot = "C:\Users\11237\.openclaw-autoclaw\workspace"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$randomReviewStateFile = Join-Path $workspaceRoot ".random-review-state.json"
$reviewTrackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Session Start Check" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$today = Get-Date -Format "yyyy-MM-dd"
$todayDate = Get-Date
$issuesFound = $false

# 1. Check .context-snapshot.json date
Write-Host "`n1. Checking context snapshot..." -ForegroundColor Yellow

if (Test-Path $contextSnapshotFile) {
    $context = Get-Content $contextSnapshotFile -Raw -Encoding UTF8 | ConvertFrom-Json
    
    if ($context.todaySession.date -ne $today) {
        Write-Host "  ⚠️ Context snapshot date mismatch: $($context.todaySession.date) != $today" -ForegroundColor Red
        Write-Host "  Fixing: Resetting todaySession..." -ForegroundColor Yellow
        
        $context.todaySession.date = $today
        $context.todaySession.completed = @()
        $context.todaySession.pending = @()
        $context.lastUpdate = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ")
        $context.sessionId = "real-$(Get-Date -Format 'yyyyMMdd-HHmm')"
        
        $context | ConvertTo-Json -Depth 10 | Set-Content $contextSnapshotFile -Encoding UTF8
        Write-Host "  ✓ Fixed: Context snapshot updated" -ForegroundColor Green
        $issuesFound = $true
    } else {
        Write-Host "  ✓ OK: Context snapshot date is today" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️ Context snapshot file not found!" -ForegroundColor Red
    $issuesFound = $true
}

# 2. Check .random-review-state.json date logic
Write-Host "`n2. Checking random review state..." -ForegroundColor Yellow

if (Test-Path $randomReviewStateFile) {
    $state = Get-Content $randomReviewStateFile -Raw -Encoding UTF8 | ConvertFrom-Json
    
    # Check date logic
    if ($state.lastReviewDate -lt $state.nextReviewDate) {
        Write-Host "  ⚠️ Date logic error: lastReviewDate < nextReviewDate" -ForegroundColor Red
        Write-Host "  Fixing: Setting nextReviewDate to tomorrow..." -ForegroundColor Yellow
        
        $state.nextReviewDate = $todayDate.AddDays(1).ToString("yyyy-MM-dd")
        
        $state | ConvertTo-Json -Depth 10 | Set-Content $randomReviewStateFile -Encoding UTF8
        Write-Host "  ✓ Fixed: Date logic corrected" -ForegroundColor Green
        $issuesFound = $true
    } else {
        Write-Host "  ✓ OK: Date logic is correct" -ForegroundColor Green
    }
    
    # Check if nextReviewDate is overdue
    if ([DateTime]$state.nextReviewDate -lt $todayDate) {
        Write-Host "  ⚠️ nextReviewDate is overdue: $($state.nextReviewDate)" -ForegroundColor Red
        Write-Host "  Fixing: Setting to tomorrow..." -ForegroundColor Yellow
        
        $state.nextReviewDate = $todayDate.AddDays(1).ToString("yyyy-MM-dd")
        
        $state | ConvertTo-Json -Depth 10 | Set-Content $randomReviewStateFile -Encoding UTF8
        Write-Host "  ✓ Fixed: nextReviewDate updated" -ForegroundColor Green
        $issuesFound = $true
    } else {
        Write-Host "  ✓ OK: nextReviewDate is not overdue" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️ Random review state file not found!" -ForegroundColor Red
    $issuesFound = $true
}

# 3. Check .review-tracker.json for overdue reviews
Write-Host "`n3. Checking review tracker..." -ForegroundColor Yellow

if (Test-Path $reviewTrackerFile) {
    $tracker = Get-Content $reviewTrackerFile -Raw -Encoding UTF8 | ConvertFrom-Json
    
    $overdueReviews = @()
    foreach ($review in $tracker.scheduledReviews) {
        if ([DateTime]$review.nextReview -lt $todayDate) {
            $daysOverdue = ($todayDate - [DateTime]$review.nextReview).Days
            $overdueReviews += @{
                Topic = $review.topic
                NextReview = $review.nextReview
                DaysOverdue = $daysOverdue
            }
        }
    }
    
    if ($overdueReviews.Count -gt 0) {
        Write-Host "  ⚠️ Found $($overdueReviews.Count) overdue reviews:" -ForegroundColor Red
        foreach ($review in $overdueReviews) {
            Write-Host "    - $($review.Topic) (overdue by $($review.DaysOverdue) days)" -ForegroundColor Gray
        }
        Write-Host "  Suggestion: Schedule these reviews ASAP" -ForegroundColor Yellow
        $issuesFound = $true
    } else {
        Write-Host "  ✓ OK: No overdue reviews" -ForegroundColor Green
    }
} else {
    Write-Host "  ⚠️ Review tracker file not found!" -ForegroundColor Red
    $issuesFound = $true
}

# 4. Check for unsynced dialogs
Write-Host "`n4. Checking for unsynced dialogs..." -ForegroundColor Yellow

$syncLogDir = Join-Path $memoryRoot "sync-logs"
$dialogFiles = Get-ChildItem (Join-Path $memoryRoot "dialogs") -Filter "*$today*.md" -ErrorAction SilentlyContinue

if ($dialogFiles.Count -gt 0) {
    Write-Host "  Found $($dialogFiles.Count) dialog files today" -ForegroundColor Gray
    
    if (Test-Path $syncLogDir) {
        $syncFiles = Get-ChildItem $syncLogDir -Filter "*$today*.md" -ErrorAction SilentlyContinue
        
        if ($syncFiles.Count -lt $dialogFiles.Count) {
            Write-Host "  ⚠️ Some dialogs are not synced!" -ForegroundColor Red
            Write-Host "  Suggestion: Run sync-review-state-simple.ps1" -ForegroundColor Yellow
            $issuesFound = $true
        } else {
            Write-Host "  ✓ OK: All dialogs are synced" -ForegroundColor Green
        }
    } else {
        Write-Host "  ⚠️ Sync log directory not found!" -ForegroundColor Red
        $issuesFound = $true
    }
} else {
    Write-Host "  ✓ OK: No dialogs today (yet)" -ForegroundColor Green
}

# Summary
Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

if ($issuesFound) {
    Write-Host "Summary: Issues found and fixed!" -ForegroundColor Yellow
    Write-Host "  - Review the fixes above" -ForegroundColor Gray
    Write-Host "  - Continue with your session" -ForegroundColor Gray
} else {
    Write-Host "Summary: All checks passed!" -ForegroundColor Green
    Write-Host "  - System is healthy" -ForegroundColor Gray
    Write-Host "  - Ready for session" -ForegroundColor Gray
}

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
