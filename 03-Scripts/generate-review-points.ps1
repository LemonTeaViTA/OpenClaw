# generate-review-points.ps1
# Function: Generate Ebbinghaus review points based on learning date
# Trigger: After learning new content or weekly review

param(
    [Parameter(Mandatory=$false)]
    [string]$LearningDate,  # Format: yyyy-MM-dd
    
    [Parameter(Mandatory=$false)]
    [string]$Topic,         # e.g., "JVM Day 1"
    
    [Parameter(Mandatory=$false)]
    [int]$QuestionCount = 10
)

$ErrorActionPreference = "Stop"
$workspaceRoot = "C:\Users\11237\.openclaw-autoclaw\workspace"
$trackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Ebbinghaus Review Point Generator" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

# If no learning date provided, use today
if (-not $LearningDate) {
    $LearningDate = Get-Date -Format "yyyy-MM-dd"
    Write-Host "  Using today's date: $LearningDate" -ForegroundColor Gray
}

# Calculate review points
Write-Host "`nCalculating review points..." -ForegroundColor Yellow

$reviewPoints = @(
    @{ date = (Get-Date $LearningDate).AddDays(1); type = "Review-1"; daysAfter = 1 },
    @{ date = (Get-Date $LearningDate).AddDays(3); type = "Review-2"; daysAfter = 3 },
    @{ date = (Get-Date $LearningDate).AddDays(7); type = "Review-3"; daysAfter = 7 },
    @{ date = (Get-Date $LearningDate).AddDays(15); type = "Review-4"; daysAfter = 15 }
)

# Only keep review points within next 7 days (for Heartbeat check)
$today = Get-Date
$futurePoints = @()
foreach ($point in $reviewPoints) {
    if ($point.date -ge $today) {
        $futurePoints += $point
        $status = if ($point.date -le $today.AddDays(7)) { "✓ (within 7 days)" } else { " (future)" }
        Write-Host "  $($point.type): $($point.date.ToString('yyyy-MM-dd'))$status" -ForegroundColor Green
    }
}

Write-Host "`n  Total future points: $($futurePoints.Count)" -ForegroundColor Green

# Update .review-tracker.json
Write-Host "`nUpdating .review-tracker.json..." -ForegroundColor Yellow

if (Test-Path $trackerFile) {
    $tracker = Get-Content $trackerFile -Raw -Encoding UTF8 | ConvertFrom-Json
    
    # Add to scheduledReviews
    $newReview = @{
        topic = $Topic
        nextReview = if ($futurePoints.Count -gt 0) { $futurePoints[0].date.ToString('yyyy-MM-dd') } else { $LearningDate }
        reviewCount = 0
        lastReview = $LearningDate
        file = "memory/dialogs/$LearningDate-session-1.md"
    }
    
    # Check if topic already exists
    $existingIndex = -1
    for ($i = 0; $i -lt $tracker.scheduledReviews.Count; $i++) {
        if ($tracker.scheduledReviews[$i].topic -eq $Topic) {
            $existingIndex = $i
            break
        }
    }
    
    if ($existingIndex -ge 0) {
        # Update existing
        $tracker.scheduledReviews[$existingIndex] = $newReview
        Write-Host "  Updated existing review: $Topic" -ForegroundColor Green
    } else {
        # Add new
        $tracker.scheduledReviews += $newReview
        Write-Host "  Added new review: $Topic" -ForegroundColor Green
    }
    
    # Save
    $tracker | ConvertTo-Json -Depth 10 | Set-Content $trackerFile -Encoding UTF8
    Write-Host "  Saved: $trackerFile" -ForegroundColor Green
} else {
    Write-Host "Error: Tracker file not found: $trackerFile" -ForegroundColor Red
    exit 1
}

# Create review schedule file
Write-Host "`nCreating review schedule..." -ForegroundColor Yellow

$scheduleDir = Join-Path $memoryRoot "review-schedules"
if (-not (Test-Path $scheduleDir)) {
    New-Item -ItemType Directory -Path $scheduleDir -Force | Out-Null
}

$scheduleFile = Join-Path $scheduleDir "$Topic-review-schedule.md"
$scheduleContent = @"
# Review Schedule - $Topic

**Learning Date**: $LearningDate  
**Question Count**: $QuestionCount  
**Generated**: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')

## Ebbinghaus Review Points

| Review | Date | Days After | Status |
|--------|------|------------|--------|
| Review-1 | $($reviewPoints[0].date.ToString('yyyy-MM-dd')) | +1 | ⏳ |
| Review-2 | $($reviewPoints[1].date.ToString('yyyy-MM-dd')) | +3 | ⏳ |
| Review-3 | $($reviewPoints[2].date.ToString('yyyy-MM-dd')) | +7 | ⏳ |
| Review-4 | $($reviewPoints[3].date.ToString('yyyy-MM-dd')) | +15 | ⏳ |

## Review Records

- [ ] Review-1 → memory/dialogs/$((Get-Date $LearningDate).AddDays(1).ToString('yyyy-MM-dd'))-review.md
- [ ] Review-2 → memory/dialogs/$((Get-Date $LearningDate).AddDays(3).ToString('yyyy-MM-dd'))-review.md
- [ ] Review-3 → memory/dialogs/$((Get-Date $LearningDate).AddDays(7).ToString('yyyy-MM-dd'))-review.md
- [ ] Review-4 → memory/dialogs/$((Get-Date $LearningDate).AddDays(15).ToString('yyyy-MM-dd'))-review.md

## Notes

- Review points automatically generated based on Ebbinghaus forgetting curve
- Only reviews within next 7 days tracked in .review-tracker.json
- After each review, update score and next review date
"@

$scheduleContent | Set-Content $scheduleFile -Encoding UTF8
Write-Host "  Created: $scheduleFile" -ForegroundColor Green

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Review points generated!" -ForegroundColor Green
Write-Host "  Topic: $Topic" -ForegroundColor White
Write-Host "  Learning Date: $LearningDate" -ForegroundColor White
Write-Host "  Future Points (7 days): $($futurePoints.Count)" -ForegroundColor White
Write-Host "  Next Review: $(if ($futurePoints.Count -gt 0) { $futurePoints[0].date.ToString('yyyy-MM-dd') } else { 'None in next 7 days' })" -ForegroundColor White
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
