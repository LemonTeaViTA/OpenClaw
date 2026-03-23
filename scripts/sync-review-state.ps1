# sync-review-state.ps1
# Function: Sync review records to state files (run after each review session)
# Trigger: Immediately after review session ends

param(
    [Parameter(Mandatory=$false)]
    [string]$SessionType = "auto",
    
    [Parameter(Mandatory=$false)]
    [string]$Topics = "",
    
    [Parameter(Mandatory=$false)]
    [switch]$AutoMode
)

$ErrorActionPreference = "Stop"
$workspaceRoot = Split-Path $PSScriptRoot -Parent
$stateFile = Join-Path $workspaceRoot ".random-review-state.json"
$reviewTrackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Syncing review state..." -ForegroundColor Cyan

$today = Get-Date -Format "yyyy-MM-dd"
$todayDate = Get-Date

# 1. Scan today's review record files
Write-Host "`nScanning review records..." -ForegroundColor Yellow

$reviewFiles = @()
$weaknessFiles = @()
$randomReviewFiles = @()
$sessionFiles = @()
$dialogFiles = @()

if (Test-Path (Join-Path $memoryRoot "reviews")) {
    $reviewFiles = Get-ChildItem (Join-Path $memoryRoot "reviews") -Filter "*$today*.md" -ErrorAction SilentlyContinue
}

if (Test-Path (Join-Path $memoryRoot "weaknesses")) {
    $weaknessFiles = Get-ChildItem (Join-Path $memoryRoot "weaknesses") -Filter "*$today*.md" -ErrorAction SilentlyContinue
}

if (Test-Path (Join-Path $memoryRoot "random-review")) {
    $randomReviewFiles = Get-ChildItem (Join-Path $memoryRoot "random-review") -Filter "*$today*.md" -ErrorAction SilentlyContinue
}

if (Test-Path (Join-Path $memoryRoot "sessions")) {
    $sessionFiles = Get-ChildItem (Join-Path $memoryRoot "sessions") -Filter "*$today*.md" -ErrorAction SilentlyContinue
}

if (Test-Path (Join-Path $memoryRoot "dialogs")) {
    $dialogFiles = Get-ChildItem (Join-Path $memoryRoot "dialogs") -Filter "*$today*.md" -ErrorAction SilentlyContinue
}

$totalFiles = $reviewFiles.Count + $weaknessFiles.Count + $randomReviewFiles.Count + $sessionFiles.Count + $dialogFiles.Count

Write-Host "  Found $totalFiles review record files" -ForegroundColor Green

# 2. Read current state file
Write-Host "`nReading state file..." -ForegroundColor Yellow

if (-not (Test-Path $stateFile)) {
    Write-Host "Error: State file not found: $stateFile" -ForegroundColor Red
    exit 1
}

$state = Get-Content $stateFile -Raw -Encoding UTF8 | ConvertFrom-Json

# 3. Extract question info from review records
Write-Host "`nExtracting question info..." -ForegroundColor Yellow

$allQuestionIds = @()
$todayScores = @()

foreach ($file in ($reviewFiles + $weaknessFiles + $randomReviewFiles + $sessionFiles + $dialogFiles)) {
    $content = Get-Content $file.FullName -Raw
    
    $matches = [regex]::Matches($content, '\b(java|coll|jvm)-(\d+)\b')
    foreach ($match in $matches) {
        $questionId = $match.Value
        if ($questionId -notin $allQuestionIds) {
            $allQuestionIds += $questionId
        }
    }
    
    $scoreMatches = [regex]::Matches($content, '(\d+\.?\d*)/5')
    if ($scoreMatches.Count -gt 0) {
        $lastScore = $scoreMatches[-1].Groups[1].Value
        $todayScores += @{
            File = $file.Name
            Score = $lastScore
        }
    }
}

Write-Host "  Found $($allQuestionIds.Count) questions" -ForegroundColor Green

# 4. Update state file
Write-Host "`nUpdating state file..." -ForegroundColor Yellow

foreach ($questionId in $allQuestionIds) {
    if ($questionId -notin $state.excludeIds) {
        $state.excludeIds += $questionId
        Write-Host "  Added to exclude: $questionId" -ForegroundColor Gray
    }
}

$state.todayQuestionIds = $allQuestionIds
$state.lastReviewDate = $today
$state.todayDate = $today

if ($allQuestionIds.Count -gt 0) {
    if ($null -eq $state.completedRounds) {
        $state.completedRounds = 0
    }
    $state.completedRounds = $state.completedRounds + 1
}

$avgScore = 0
if ($todayScores.Count -gt 0) {
    $totalScore = 0
    foreach ($score in $todayScores) {
        $totalScore += [float]$score.Score
    }
    $avgScore = [math]::Round($totalScore / $todayScores.Count, 1)
}

$state.todaySummary = @{
    date = $today
    questionCount = $allQuestionIds.Count
    score = "$avgScore/5"
    scoringStandard = "Strict"
}

$state | ConvertTo-Json -Depth 10 | Set-Content $stateFile -Encoding UTF8
Write-Host "  Updated: $stateFile" -ForegroundColor Green

# 5. Update .review-tracker.json
Write-Host "`nUpdating review tracker..." -ForegroundColor Yellow

if (Test-Path $reviewTrackerFile) {
    $tracker = Get-Content $reviewTrackerFile -Raw -Encoding UTF8 | ConvertFrom-Json
    $tracker.lastSession = "sync-$today-$(Get-Date -Format 'HHmm')"
    $tracker.lastUpdate = (Get-Date -o).ToString()
    
    if ($null -ne $tracker.randomReview) {
        $tracker.randomReview.lastReview = $today
        $nextReview = $todayDate.AddDays(1).ToString("yyyy-MM-dd")
        $tracker.randomReview.nextReview = $nextReview
    }
    
    $tracker | ConvertTo-Json -Depth 10 | Set-Content $reviewTrackerFile -Encoding UTF8
    Write-Host "  Updated: $reviewTrackerFile" -ForegroundColor Green
}

# 6. Update .context-snapshot.json
Write-Host "`nUpdating context snapshot..." -ForegroundColor Yellow

if (Test-Path $contextSnapshotFile) {
    $context = Get-Content $contextSnapshotFile -Raw -Encoding UTF8 | ConvertFrom-Json
    $context.lastUpdate = (Get-Date -o).ToString()
    $context.sessionId = "sync-$today-$(Get-Date -Format 'HHmm')"
    
    if ($null -eq $context.todaySession) {
        $context.todaySession = @{
            date = $today
            completed = @()
            pending = @()
        }
    }
    
    $sessionSummary = "Sync completed ($($allQuestionIds.Count) questions)"
    if ($Topics -ne "") {
        $sessionSummary = "$Topics ($($allQuestionIds.Count) questions)"
    }
    
    if ($sessionSummary -notin $context.todaySession.completed) {
        $context.todaySession.completed += $sessionSummary
    }
    
    $context | ConvertTo-Json -Depth 10 | Set-Content $contextSnapshotFile -Encoding UTF8
    Write-Host "  Updated: $contextSnapshotFile" -ForegroundColor Green
}

# 7. Create sync record
Write-Host "`nCreating sync record..." -ForegroundColor Yellow

$syncLogDir = Join-Path $memoryRoot "sync-logs"
if (-not (Test-Path $syncLogDir)) {
    New-Item -ItemType Directory -Path $syncLogDir -Force | Out-Null
}

$syncLogFile = Join-Path $syncLogDir "$today-sync-$(Get-Date -Format 'HHmmss').md"
$syncContent = @"
# Sync Record - $today $(Get-Date -Format 'HH:mm:ss')

## Sync Details
- **Session Type**: $SessionType
- **Topics**: $(if ($Topics -ne "") { $Topics } else { "Auto-detected" })
- **Question Count**: $($allQuestionIds.Count)
- **Average Score**: $avgScore/5

## Synced Questions
$(($allQuestionIds | ForEach-Object { "- $_" }) -join "`n")

## Updated Files
- .random-review-state.json OK
- .review-tracker.json OK
- .context-snapshot.json OK

## Status
Sync completed successfully
"@

$syncContent | Set-Content $syncLogFile -Encoding UTF8
Write-Host "  Created: $syncLogFile" -ForegroundColor Green

# 8. Complete
Write-Host "`nSync completed!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Summary:" -ForegroundColor Cyan
Write-Host "  - Questions: $($allQuestionIds.Count)" -ForegroundColor White
Write-Host "  - Average Score: $avgScore/5" -ForegroundColor White
Write-Host "  - Next Random Review: $today after 20:00" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
