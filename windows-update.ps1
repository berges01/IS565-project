# Get the last Windows Update installation date
$lastUpdate = (Get-WmiObject -Query "SELECT * FROM Win32_QuickFixEngineering" | Sort-Object -Property InstalledOn | Select-Object -Last 1).InstalledOn

# Calculate the time since the last update
$timeSinceLastUpdate = (Get-Date) - $lastUpdate

# Define a threshold for what you consider "up to date" (e.g., 7 days)
$threshold = New-TimeSpan -Days 7

# Check if the time since the last update is within the threshold
if ($timeSinceLastUpdate -le $threshold) {
    Write-Host "Windows is up to date."
} else {
    Write-Host "Windows is not up to date."
}

# Display the last update installation date
Write-Host "Last Cumulative Update Installed On: $lastUpdate"