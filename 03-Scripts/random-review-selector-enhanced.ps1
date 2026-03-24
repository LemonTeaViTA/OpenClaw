# random-review-selector-enhanced.ps1
# 增强版随机选题脚本
# 功能：从题库映射文件读取实际 ID + 支持难度筛选 + 薄弱项优先
# 更新：2026-03-23

param(
    [Parameter(Mandatory=$false)]
    [int]$QuestionCount = 12,
    
    [Parameter(Mandatory=$false)]
    [ValidateSet("all", "easy", "medium", "hard")]
    [string]$Difficulty = "all",
    
    [Parameter(Mandatory=$false)]
    [switch]$PrioritizeWeaknesses,
    
    [Parameter(Mandatory=$false)]
    [switch]$Force,
    
    [Parameter(Mandatory=$false)]
    [switch]$AutoMode
)

$ErrorActionPreference = "Stop"
$workspaceRoot = Split-Path $PSScriptRoot -Parent | Split-Path -Parent  # Go up from 03-Scripts to workspace
$stateFile = Join-Path $workspaceRoot ".random-review-state.json"
$questionMapFile = Join-Path $workspaceRoot ".question-id-map.json"
$reviewTrackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Random Review Selector (Enhanced)" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$today = Get-Date -Format "yyyy-MM-dd"
$todayDate = Get-Date

# Check for unsynced review records
Write-Host "`nChecking sync status..." -ForegroundColor Yellow

$unsyncedFiles = @()
$syncLogDir = Join-Path $memoryRoot "sync-logs"

$reviewDirs = @("dialogs")
foreach ($dir in $reviewDirs) {
    $dirPath = Join-Path $memoryRoot $dir
    if (Test-Path $dirPath) {
        $files = Get-ChildItem $dirPath -Filter "*$today*.md" -ErrorAction SilentlyContinue
        foreach ($file in $files) {
            $hasSync = $false
            if (Test-Path $syncLogDir) {
                $syncFiles = Get-ChildItem $syncLogDir -Filter "*$today*.md" -ErrorAction SilentlyContinue
                if ($syncFiles.Count -gt 0) {
                    foreach ($syncFile in $syncFiles) {
                        $syncContent = Get-Content $syncFile.FullName -Raw
                        if ($syncContent -match [regex]::Escape($file.Name)) {
                            $hasSync = $true
                            break
                        }
                    }
                }
            }
            
            if (-not $hasSync) {
                $unsyncedFiles += $file.FullName
            }
        }
    }
}

if ($unsyncedFiles.Count -gt 0 -and -not $Force) {
    Write-Host "WARNING: Found $($unsyncedFiles.Count) unsynced review records:" -ForegroundColor Red
    foreach ($file in $unsyncedFiles) {
        Write-Host "    - $([System.IO.Path]::GetFileName($file))" -ForegroundColor Gray
    }
    
    if (-not $AutoMode) {
        Write-Host "`nSuggestion: Run sync script first to ensure state files are up to date." -ForegroundColor Yellow
        $sync = Read-Host "Run sync script now? (y/n)"
        
        if ($sync -eq 'y') {
            Write-Host "`nRunning sync script..." -ForegroundColor Cyan
            $syncScript = Join-Path $PSScriptRoot "sync-review-state-simple.ps1"
            & $syncScript -AutoMode
            Write-Host "`nSync completed, continuing with selection..." -ForegroundColor Green
        } else {
            Write-Host "`nSkipping sync, continuing with selection (may cause duplicates)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "`nAuto mode: Running sync script..." -ForegroundColor Cyan
        $syncScript = Join-Path $PSScriptRoot "sync-review-state-simple.ps1"
        & $syncScript -AutoMode
    }
} else {
    Write-Host "  All review records are synced" -ForegroundColor Green
}

# Read question map
Write-Host "`nReading question map..." -ForegroundColor Yellow

if (-not (Test-Path $questionMapFile)) {
    Write-Host "Error: Question map file not found: $questionMapFile" -ForegroundColor Red
    Write-Host "Please run create_question_map.py first to generate the mapping file." -ForegroundColor Yellow
    exit 1
}

$questionMap = Get-Content $questionMapFile -Raw -Encoding UTF8 | ConvertFrom-Json

Write-Host "  Total questions: $($questionMap.totalQuestions)" -ForegroundColor Green
Write-Host "  Java Basics: $($questionMap.modules.java.total) questions" -ForegroundColor Gray
Write-Host "  Collections: $($questionMap.modules.coll.total) questions" -ForegroundColor Gray
Write-Host "  JVM: $($questionMap.modules.jvm.total) questions" -ForegroundColor Gray

# Get exclude list and weaknesses
Write-Host "`nLoading exclude list and weaknesses..." -ForegroundColor Yellow

$state = Get-Content $stateFile -Raw -Encoding UTF8 | ConvertFrom-Json

$excludeIds = @()
if ($null -ne $state.excludeIds) {
    $excludeIds = @($state.excludeIds)
}
Write-Host "  Excluded: $($excludeIds.Count) questions" -ForegroundColor Gray

$weaknesses = @()
if ($null -ne $state.weaknesses) {
    $weaknesses = @($state.weaknesses)
    Write-Host "  Weaknesses: $($weaknesses.Count) questions" -ForegroundColor Yellow
}

# Filter questions by difficulty
Write-Host "`nFiltering questions..." -ForegroundColor Yellow

$availableQuestions = @()
foreach ($qId in $questionMap.questions.PSObject.Properties.Name) {
    $q = $questionMap.questions.$qId
    
    # Skip excluded questions
    if ($qId -in $excludeIds) {
        continue
    }
    
    # Filter by difficulty
    if ($Difficulty -ne "all") {
        $diff = $q.difficulty
        if ($Difficulty -eq "easy" -and $diff -notlike "⭐ 基础") {
            continue
        }
        if ($Difficulty -eq "medium" -and $diff -notlike "⭐⭐ 进阶") {
            continue
        }
        if ($Difficulty -eq "hard" -and $diff -notlike "⭐⭐⭐ 提高") {
            continue
        }
    }
    
    $availableQuestions += [PSCustomObject]@{
        ID = $qId
        Title = $q.title
        Module = $q.module
        Difficulty = $q.difficulty
        Tags = $q.tags -join ", "
        IsWeakness = ($weaknesses | Where-Object { $_.id -eq $qId }) -ne $null
    }
}

Write-Host "  Available questions: $($availableQuestions.Count)" -ForegroundColor Green

if ($availableQuestions.Count -lt $QuestionCount) {
    Write-Host "WARNING: Not enough available questions ($($availableQuestions.Count) < $QuestionCount)" -ForegroundColor Yellow
    Write-Host "Consider resetting exclude list or reviewing more questions." -ForegroundColor Yellow
}

# Selection strategy
Write-Host "`nSelecting questions..." -ForegroundColor Yellow

$selectedQuestions = @()

# Strategy 1: Prioritize weaknesses
if ($PrioritizeWeaknesses -and $weaknesses.Count -gt 0) {
    Write-Host "  Prioritizing weaknesses..." -ForegroundColor Cyan
    
    $weaknessQuestions = $availableQuestions | Where-Object { $_.IsWeakness }
    Write-Host "  Found $($weaknessQuestions.Count) weakness questions" -ForegroundColor Gray
    
    $weaknessCount = [Math]::Min([Math]::Floor($QuestionCount / 2), $weaknessQuestions.Count)
    
    $random = New-Object System.Random
    $shuffledWeaknesses = $weaknessQuestions | Sort-Object { $random.Next() }
    
    for ($i = 0; $i -lt $weaknessCount; $i++) {
        $selectedQuestions += $shuffledWeaknesses[$i]
    }
    
    Write-Host "  Selected $weaknessCount weakness questions" -ForegroundColor Green
}

# Strategy 2: Balance across modules
$remainingCount = $QuestionCount - $selectedQuestions.Count
if ($remainingCount -gt 0) {
    $remainingQuestions = $availableQuestions | Where-Object { $_.ID -notin $selectedQuestions.ID }
    
    $moduleCount = 3  # java, coll, jvm
    $perModule = [math]::Floor($remainingCount / $moduleCount)
    $remainder = $remainingCount % $moduleCount
    
    Write-Host "`nModule allocation:" -ForegroundColor Cyan
    Write-Host "  Base per module: $perModule questions" -ForegroundColor Gray
    
    $random = New-Object System.Random
    
    foreach ($module in @("java", "coll", "jvm")) {
        $moduleQuestionCount = $perModule
        if ($remainder -gt 0) {
            $moduleQuestionCount++
            $remainder--
        }
        
        $moduleAvailable = $remainingQuestions | Where-Object { $_.Module -eq $module }
        
        if ($moduleAvailable.Count -gt 0) {
            $selected = $moduleAvailable | Sort-Object { $random.Next() } | Select-Object -First $moduleQuestionCount
            $selectedQuestions += $selected
            Write-Host "  $($module): $($selected.Count) questions" -ForegroundColor Green
        }
    }
}

# Output results
Write-Host "`nSelection completed!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$index = 1
foreach ($q in $selectedQuestions) {
    $weaknessMark = ""
    if ($q.IsWeakness) {
        $weaknessMark = " ⚠️ 薄弱项"
    }
    
    Write-Host "  $index. [$($q.ID)] $($q.Title.Substring(0, [Math]::Min(40, $q.Title.Length)))... [$($q.Difficulty)]$weaknessMark" -ForegroundColor White
    $index++
}

# Save to output file
$jsonOutput = @{
    date = $today
    questionCount = $selectedQuestions.Count
    questionIds = $selectedQuestions.ID
    difficulty = $Difficulty
    prioritizeWeaknesses = $PrioritizeWeaknesses
    modules = @{
        java = ($selectedQuestions | Where-Object { $_.Module -eq "java" }).Count
        coll = ($selectedQuestions | Where-Object { $_.Module -eq "coll" }).Count
        jvm = ($selectedQuestions | Where-Object { $_.Module -eq "jvm" }).Count
    }
}

$outputFile = Join-Path $workspaceRoot ".today-random-review.json"
$jsonOutput | ConvertTo-Json -Depth 5 | Set-Content $outputFile -Encoding UTF8
Write-Host "`nSaved to: $outputFile" -ForegroundColor Green

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Ready for random review!" -ForegroundColor Green
Write-Host "Tip: Run sync-review-state-simple.ps1 after review to sync state" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
