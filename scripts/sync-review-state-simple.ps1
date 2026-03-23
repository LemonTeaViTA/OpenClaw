# sync-review-state-simple.ps1
# 简化版同步脚本（用于测试）

$ErrorActionPreference = "Stop"
$workspaceRoot = "C:\Users\11237\.openclaw-autoclaw\workspace"
$stateFile = Join-Path $workspaceRoot ".random-review-state.json"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Syncing review state (simple version)..." -ForegroundColor Cyan

$today = Get-Date -Format "yyyy-MM-dd"

# Scan dialogs directory
Write-Host "`nScanning memory/dialogs/..." -ForegroundColor Yellow
$dialogPath = Join-Path $memoryRoot "dialogs"
$dialogFiles = Get-ChildItem $dialogPath -Filter "*$today*.md" -ErrorAction SilentlyContinue

Write-Host "  Found $($dialogFiles.Count) files" -ForegroundColor Green

if ($dialogFiles.Count -eq 0) {
    Write-Host "No review records found for today" -ForegroundColor Yellow
    exit 0
}

# Extract question IDs and scores
Write-Host "`nExtracting data..." -ForegroundColor Yellow

$allQuestionIds = @()
$totalScore = 0
$scoreCount = 0

foreach ($file in $dialogFiles) {
    Write-Host "  Processing: $($file.Name)" -ForegroundColor Gray
    $content = Get-Content $file.FullName -Raw
    
    # Extract question IDs (java-XXX, coll-XXX, jvm-XXX)
    $matches = [regex]::Matches($content, '(java|coll|jvm)-(\d+)')
    foreach ($match in $matches) {
        $questionId = $match.Value
        if ($questionId -notin $allQuestionIds) {
            $allQuestionIds += $questionId
            Write-Host "    Found: $questionId" -ForegroundColor Gray
        }
    }
    
    # Extract scores (X/5 or X.X/5)
    $scoreMatches = [regex]::Matches($content, '(\d+\.?\d*)/5')
    if ($scoreMatches.Count -gt 0) {
        $lastScore = $scoreMatches[$scoreMatches.Count - 1].Groups[1].Value
        Write-Host "    Score: $lastScore/5" -ForegroundColor Gray
        $totalScore += [float]$lastScore
        $scoreCount++
    }
}

Write-Host "`n  Total questions: $($allQuestionIds.Count)" -ForegroundColor Green
Write-Host "  Total scores found: $scoreCount" -ForegroundColor Green

# Calculate average
$avgScore = 0
if ($scoreCount -gt 0) {
    $avgScore = [math]::Round($totalScore / $scoreCount, 1)
}
Write-Host "  Average score: $avgScore/5" -ForegroundColor Green

# Update state file
Write-Host "`nUpdating .random-review-state.json..." -ForegroundColor Yellow

$state = Get-Content $stateFile -Raw -Encoding UTF8 | ConvertFrom-Json

# Add to exclude list
foreach ($questionId in $allQuestionIds) {
    if ($questionId -notin $state.excludeIds) {
        $state.excludeIds += $questionId
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

$state.todaySummary = @{
    date = $today
    questionCount = $allQuestionIds.Count
    score = "$avgScore/5"
    scoringStandard = "Strict"
}

$state | ConvertTo-Json -Depth 10 | Set-Content $stateFile -Encoding UTF8
Write-Host "  Updated state file" -ForegroundColor Green

# Update context snapshot
Write-Host "`nUpdating .context-snapshot.json..." -ForegroundColor Yellow

$context = Get-Content $contextSnapshotFile -Raw -Encoding UTF8 | ConvertFrom-Json
$context.lastUpdate = (Get-Date -Format "yyyy-MM-ddTHH:mm:ss.fffZ").ToString()
$context.sessionId = "sync-$today-$(Get-Date -Format 'HHmm')"

if ($null -eq $context.todaySession) {
    $context.todaySession = @{
        date = $today
        completed = @()
        pending = @()
    }
}

$sessionSummary = "System Test ($($allQuestionIds.Count) questions, $avgScore/5)"
if ($sessionSummary -notin $context.todaySession.completed) {
    $context.todaySession.completed += $sessionSummary
}

$context | ConvertTo-Json -Depth 10 | Set-Content $contextSnapshotFile -Encoding UTF8
Write-Host "  Updated context snapshot" -ForegroundColor Green

# Create sync log
Write-Host "`nCreating sync log..." -ForegroundColor Yellow

$syncLogDir = Join-Path $memoryRoot "sync-logs"
if (-not (Test-Path $syncLogDir)) {
    New-Item -ItemType Directory -Path $syncLogDir -Force | Out-Null
}

$syncLogFile = Join-Path $syncLogDir "$today-sync-$(Get-Date -Format 'HHmmss').md"
$syncContent = @"
# Sync Record - $today $(Get-Date -Format 'HH:mm:ss')

## Sync Details
- **Session Type**: System Test
- **Topics**: ConcurrentHashMap, sleep vs wait, HashMap vs HashTable, GC Roots, CMS
- **Question Count**: $($allQuestionIds.Count)
- **Average Score**: $avgScore/5

## Synced Questions
$(($allQuestionIds | ForEach-Object { "- $_" }) -join "`n")

## Updated Files
- .random-review-state.json OK
- .context-snapshot.json OK

## Status
Sync completed successfully
"@

$syncContent | Set-Content $syncLogFile -Encoding UTF8
Write-Host "  Created: $syncLogFile" -ForegroundColor Green

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Sync completed!" -ForegroundColor Green
Write-Host "  Questions: $($allQuestionIds.Count)" -ForegroundColor White
Write-Host "  Average: $avgScore/5" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
