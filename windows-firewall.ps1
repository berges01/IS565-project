# Get the Windows Firewall profile information
$firewallProfiles = Get-NetFirewallProfile

foreach ($profile in $firewallProfiles) {
    Write-Host "Profile Name: $($profile.Name)"
    Write-Host "Firewall Enabled: $($profile.Enabled)"
    Write-Host "Default Inbound Action: $($profile.DefaultInboundAction)"
    Write-Host "Default Outbound Action: $($profile.DefaultOutboundAction)"
    Write-Host "LogBlocked: $($profile.LogBlocked)"
    Write-Host "LogAllowed: $($profile.LogAllowed)"
    Write-Host "Notifications: $($profile.NotifyOnListen)"
    Write-Host "UnicastResponseToMulticast: $($profile.UnicastResponseToMulticast)"
    Write-Host ""
}

# Check Windows Firewall service status
$windowsFirewallService = Get-Service -Name "MpsSvc" | Select-Object -ExpandProperty Status

# Check Windows Defender Firewall service status
$defenderFirewallService = Get-Service -Name "mpssvc" | Select-Object -ExpandProperty Status

Write-Host "Windows Firewall Service Status: $windowsFirewallService"
Write-Host "Windows Defender Firewall Service Status: $defenderFirewallService"
