# check-sync-status.ps1
# Function: Check sync status (run anytime)
# Trigger: When user wants to check current sync status

param(
    [Parameter(Mandatory=$false)]
    [switch]$Detailed,
    
    [Parameter(Mandatory=$false)]
    [switch]$AutoFix
)

$ErrorActionPreference = "Continue"
$workspaceRoot = Split-Path $PSScriptRoot -Parent
$stateFile = Join-Path $workspaceRoot ".random-review-state.json"
$reviewTrackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Sync Status Checker" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$today = Get-Date -Format "yyyy-MM-dd"
$todayDate = Get-Date

# 1. Check if state files exist
Write-Host "`nState Files:" -ForegroundColor Yellow

$files = @{
    ".random-review-state.json" = $stateFile
    ".review-tracker.json" = $reviewTrackerFile
    ".context-snapshot.json" = $contextSnapshotFile
}

$allFilesExist = $true
foreach ($name in $files.Keys) {
    $path = $files[$name]
    if (Test-Path $path) {
        $lastWrite = Get-Item $path | Select-Object -ExpandProperty LastWriteTime
        $status = "OK"
        $color = "Green"
        
        if ($lastWrite.Date -eq $todayDate.Date) {
            $status += " (today $(Get-Date -Date $lastWrite -Format 'HH:mm'))"
        } else {
            $status += " WARNING: Last updated $($lastWrite.ToString('yyyy-MM-dd HH:mm'))"
            $color = "Yellow"
        }
        
        Write-Host "  $name`: $status" -ForegroundColor $color
    } else {
        Write-Host "  $name`: NOT FOUND" -ForegroundColor Red
        $allFilesExist = $false
    }
}

if (-not $allFilesExist) {
    Write-Host "`nWARNING: Some state files are missing" -ForegroundColor Yellow
}

# 2. Check today's review records
Write-Host "`nToday's Review Records:" -ForegroundColor Yellow

$reviewDirs = @("reviews", "weaknesses", "random-review", "sessions")
$todayFiles = @()

foreach ($dir in $reviewDirs) {
    $dirPath = Join-Path $memoryRoot $dir
    if (Test-Path $dirPath) {
        $files = Get-ChildItem $dirPath -Filter "*$today*.md" -ErrorAction SilentlyContinue
        if ($files.Count -gt 0) {
            Write-Host "  $dir`: $($files.Count) files" -ForegroundColor Green
            foreach ($file in $files) {
                Write-Host "    - $($file.Name)" -ForegroundColor Gray
                $todayFiles += $file.FullName
            }
        } else {
            Write-Host "  $dir`: None" -ForegroundColor Gray
        }
    }
}

if ($todayFiles.Count -eq 0) {
    Write-Host "  No review records today" -ForegroundColor Cyan
}

# 3. Check sync logs
Write-Host "`nSync Logs:" -ForegroundColor Yellow

$syncLogDir = Join-Path $memoryRoot "sync-logs"
if (Test-Path $syncLogDir) {
    $syncFiles = Get-ChildItem $syncLogDir -Filter "*$today*.md" -ErrorAction SilentlyContinue
    if ($syncFiles.Count -gt 0) {
        Write-Host "  Synced today: $($syncFiles.Count) times" -ForegroundColor Green
        foreach ($file in $syncFiles) {
            Write-Host "    - $($file.Name)" -ForegroundColor Gray
        }
        
        $lastSync = $syncFiles | Sort-Object LastWriteTime -Descending | Select-Object -First 1
        if ($lastSync) {
            $content = Get-Content $lastSync.FullName -Raw
            if ($content -match "Question Count: (\d+)") {
                Write-Host "  Last sync: $($matches[1]) questions" -ForegroundColor Cyan
            }
        }
    } else {
        Write-Host "  No sync records today WARNING" -ForegroundColor Yellow
    }
} else {
    Write-Host "  Sync log directory not found" -ForegroundColor Gray
}

# 4. Check for unsynced files
Write-Host "`nUnsynced Check:" -ForegroundColor Yellow

$unsyncedFiles = @()
if (Test-Path $syncLogDir) {
    $syncFiles = Get-ChildItem $syncLogDir -Filter "*$today*.md" -ErrorAction SilentlyContinue
    
    foreach ($file in $todayFiles) {
        $hasSync = $false
        foreach ($syncFile in $syncFiles) {
            $syncContent = Get-Content $syncFile.FullName -Raw
            if ($syncContent -match [regex]::Escape([System.IO.Path]::GetFileName($file))) {
                $hasSync = $true
                break
            }
        }
        
        if (-not $hasSync) {
            $unsyncedFiles += $file
        }
    }
} else {
    $unsyncedFiles = $todayFiles
}

if ($unsyncedFiles.Count -gt 0) {
    Write-Host "  Found $($unsyncedFiles.Count) unsynced files:" -ForegroundColor Red
    foreach ($file in $unsyncedFiles) {
        Write-Host "    - $([System.IO.Path]::GetFileName($file))" -ForegroundColor Gray
    }
    
    if ($AutoFix) {
        Write-Host "`nAuto-fix mode: Running sync script..." -ForegroundColor Cyan
        $syncScript = Join-Path $PSScriptRoot "sync-review-state.ps1"
        & $syncScript -AutoMode
    } else {
        Write-Host "`nSuggestion: Run .\scripts\sync-review-state.ps1" -ForegroundColor Yellow
    }
} else {
    Write-Host "  All review records are synced" -ForegroundColor Green
}

# 5. Read state file details (detailed mode)
if ($Detailed -and (Test-Path $stateFile)) {
    Write-Host "`nState File Details:" -ForegroundColor Yellow
    
    $state = Get-Content $stateFile -Raw -Encoding UTF8 | ConvertFrom-Json
    
    Write-Host "  Last Review Date: $($state.lastReviewDate)" -ForegroundColor Cyan
    Write-Host "  Today's Questions: $($state.todayQuestionIds.Count)" -ForegroundColor Cyan
    Write-Host "  Excluded Questions: $($state.excludeIds.Count)" -ForegroundColor Cyan
    Write-Host "  Completed Rounds: $($state.completedRounds)" -ForegroundColor Cyan
    
    if ($state.todaySummary) {
        Write-Host "  Today's Average: $($state.todaySummary.score)" -ForegroundColor Cyan
    }
}

# 6. Summary
Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Summary:" -ForegroundColor Cyan

$syncStatus = "OK"
$syncColor = "Green"

if ($unsyncedFiles.Count -gt 0) {
    $syncStatus = "NOT SYNCED ($($unsyncedFiles.Count) files)"
    $syncColor = "Red"
} elseif ($todayFiles.Count -eq 0) {
    $syncStatus = "No review records today"
    $syncColor = "Cyan"
}

Write-Host "  Sync Status: $syncStatus" -ForegroundColor $syncColor
Write-Host "  Review Records: $($todayFiles.Count)" -ForegroundColor Cyan
Write-Host "  Sync Records: $(if (Test-Path $syncLogDir) { (Get-ChildItem $syncLogDir -Filter "*$today*.md").Count } else { 0 })" -ForegroundColor Cyan

Write-Host "`nQuick Commands:" -ForegroundColor Yellow
Write-Host "  Sync: .\scripts\sync-review-state.ps1" -ForegroundColor Cyan
Write-Host "  Select: .\scripts\random-review-selector.ps1" -ForegroundColor Cyan
Write-Host "  Check: .\scripts\check-sync-status.ps1 -Verbose" -ForegroundColor Cyan
Write-Host "  Auto-fix: .\scripts\check-sync-status.ps1 -AutoFix" -ForegroundColor Cyan

Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
