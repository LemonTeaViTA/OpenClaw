# random-review-selector.ps1
# Function: Random question selection with sync check
# Trigger: Before random review session

param(
    [Parameter(Mandatory=$false)]
    [int]$QuestionCount = 12,
    
    [Parameter(Mandatory=$false)]
    [switch]$Force,
    
    [Parameter(Mandatory=$false)]
    [switch]$AutoMode
)

$ErrorActionPreference = "Stop"
$workspaceRoot = Split-Path $PSScriptRoot -Parent
$stateFile = Join-Path $workspaceRoot ".random-review-state.json"
$reviewTrackerFile = Join-Path $workspaceRoot ".review-tracker.json"
$contextSnapshotFile = Join-Path $workspaceRoot ".context-snapshot.json"
$memoryRoot = Join-Path $workspaceRoot "memory"

Write-Host "Random Review Selector" -ForegroundColor Cyan
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$today = Get-Date -Format "yyyy-MM-dd"
$todayDate = Get-Date

# First insurance: Check for unsynced review records
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
            $syncScript = Join-Path $PSScriptRoot "sync-review-state.ps1"
            & $syncScript -AutoMode
            Write-Host "`nSync completed, continuing with selection..." -ForegroundColor Green
        } else {
            Write-Host "`nSkipping sync, continuing with selection (may cause duplicates)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "`nAuto mode: Running sync script..." -ForegroundColor Cyan
        $syncScript = Join-Path $PSScriptRoot "sync-review-state.ps1"
        & $syncScript -AutoMode
    }
} else {
    Write-Host "  All review records are synced" -ForegroundColor Green
}

# Second: Read question bank and state
Write-Host "`nReading question bank..." -ForegroundColor Yellow

if (-not (Test-Path $stateFile)) {
    Write-Host "Error: State file not found: $stateFile" -ForegroundColor Red
    exit 1
}

$state = Get-Content $stateFile -Raw -Encoding UTF8 | ConvertFrom-Json

$questionBank = @{
    "java" = @{
        total = 56
        prefix = "java"
        name = "Java Basics"
    }
    "coll" = @{
        total = 37
        prefix = "coll"
        name = "Collections"
    }
    "jvm" = @{
        total = 66
        prefix = "jvm"
        name = "JVM"
    }
}

$totalQuestions = 0
foreach ($module in $questionBank.Values) {
    $totalQuestions += $module.total
}

Write-Host "  Java Basics: $($questionBank.java.total) questions" -ForegroundColor Gray
Write-Host "  Collections: $($questionBank.coll.total) questions" -ForegroundColor Gray
Write-Host "  JVM: $($questionBank.jvm.total) questions" -ForegroundColor Gray
Write-Host "  Total: $totalQuestions questions" -ForegroundColor Green

# Third: Get exclude list and weaknesses
Write-Host "`nLoading exclude list..." -ForegroundColor Yellow

$excludeIds = @()
if ($null -ne $state.excludeIds) {
    $excludeIds = @($state.excludeIds)
}
Write-Host "  Excluded: $($excludeIds.Count) questions" -ForegroundColor Gray

# Fourth: Smart selection strategy
Write-Host "`nSelecting questions..." -ForegroundColor Yellow

$allIds = @()
foreach ($module in $questionBank.Values) {
    for ($i = 1; $i -le $module.total; $i++) {
        $id = "$($module.prefix)-$(('{0:D3}' -f $i))"
        $allIds += $id
    }
}

$availableIds = @()
foreach ($id in $allIds) {
    if ($id -notin $excludeIds) {
        $availableIds += $id
    }
}

Write-Host "  Available: $($availableIds.Count) questions" -ForegroundColor Green

if ($availableIds.Count -lt $QuestionCount) {
    Write-Host "WARNING: Not enough available questions ($($availableIds.Count) < $QuestionCount)" -ForegroundColor Yellow
}

# Selection strategy: Balance across modules
$selectedIds = @()

$moduleCount = $questionBank.Count
$perModule = [math]::Floor($QuestionCount / $moduleCount)
$remainder = $QuestionCount % $moduleCount

Write-Host "`nModule allocation:" -ForegroundColor Cyan
Write-Host "  Base per module: $perModule questions" -ForegroundColor Gray

$moduleIndex = 0
foreach ($module in $questionBank.Values) {
    $moduleQuestionCount = $perModule
    if ($moduleIndex -lt $remainder) {
        $moduleQuestionCount++
    }
    
    $moduleAvailable = @()
    foreach ($id in $availableIds) {
        if ($id -like "$($module.prefix)-*") {
            $moduleAvailable += $id
        }
    }
    
    if ($moduleAvailable.Count -gt 0) {
        $selected = @()
        $count = [math]::Min($moduleQuestionCount, $moduleAvailable.Count)
        
        $random = New-Object System.Random
        $indices = @(0..($moduleAvailable.Count - 1))
        
        for ($i = $indices.Count - 1; $i -gt 0; $i--) {
            $j = $random.Next(0, $i + 1)
            $temp = $indices[$i]
            $indices[$i] = $indices[$j]
            $indices[$j] = $temp
        }
        
        for ($i = 0; $i -lt $count; $i++) {
            $selected += $moduleAvailable[$indices[$i]]
        }
        
        $selectedIds += $selected
        Write-Host "  $($module.name): $($selected.Count) questions" -ForegroundColor Green
    }
    
    $moduleIndex++
}

# Fifth: Output results
Write-Host "`nSelection completed!" -ForegroundColor Green
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

$questionList = @()
$index = 1
foreach ($id in $selectedIds) {
    $module = "Unknown"
    if ($id -like "java-*") { $module = "Java Basics" }
    elseif ($id -like "coll-*") { $module = "Collections" }
    elseif ($id -like "jvm-*") { $module = "JVM" }
    
    $questionList += [PSCustomObject]@{
        Index = $index
        ID = $id
        Module = $module
        Priority = "Normal"
    }
    $index++
}

$questionList | Format-Table -AutoSize

$jsonOutput = @{
    date = $today
    questionCount = $selectedIds.Count
    questionIds = $selectedIds
    modules = @{
        java = ($selectedIds | Where-Object { $_ -like "java-*" }).Count
        coll = ($selectedIds | Where-Object { $_ -like "coll-*" }).Count
        jvm = ($selectedIds | Where-Object { $_ -like "jvm-*" }).Count
    }
}

Write-Host "`nJSON Output:" -ForegroundColor Cyan
$jsonOutput | ConvertTo-Json -Depth 5

$outputFile = Join-Path $workspaceRoot ".today-random-review.json"
$jsonOutput | ConvertTo-Json -Depth 5 | Set-Content $outputFile -Encoding UTF8
Write-Host "`nSaved to: $outputFile" -ForegroundColor Green

Write-Host "`n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray
Write-Host "Ready for random review!" -ForegroundColor Green
Write-Host "Tip: Run sync-review-state.ps1 after review to sync state" -ForegroundColor Yellow
Write-Host "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━" -ForegroundColor Gray

exit 0
