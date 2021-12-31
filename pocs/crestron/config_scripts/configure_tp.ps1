Import-Module PSCrestron

$dev = ""
$username = ""
$password = ""
$lpath = ''
$rpath = ''
$uid = ''
$certName = ''
$addcmd = "certif add root $($certName) $($uid) $($password)"
$cid = ""
$master = ""
$ipt_cmd = "addm" + $cid + $master

# disable autodiscovery
Write-Host "Disabling Autodiscovery"
Invoke-CrestronCommand $dev "autodiscovery off" -Secure -Username $username -Password $password

#set hostname
Write-Host "Setting Hostname"
Invoke-CrestronCommand $dev "host NYCHS-AV-WRTSW" -Secure -Username $username -Password $password

#add cert
#Write-Host $dev '- Sending cert'

#Send-FTPFile $dev $lpath $rpath -Secure -Username $username -Password $password
#Write-Host $dev '- Adding cert to list'

#Invoke-CrestronCommand $dev $addcert -Secure -Username $username -Password $password

#set time
Write-Host "Setting Timezone"
Invoke-CrestronCommand $dev "timezone 014" -Secure -Username $username -Password $password
Write-Host "Setting SNTP Server"
Invoke-CrestronCommand $dev "sntp server:10.165.83.11" -Secure -Username $username -Password $password
Write-Host "Syncing with SNTP Server"
Invoke-CrestronCommand $dev "sntp start" -Secure -Username $username -Password $password
Write-Host "Checking Time..."
Invoke-CrestronCommand $dev "time" -Secure -Username $username -Password $password

# set ip table
Write-Host "Setting IP Table"
Invoke-CrestronCommand $dev $ipt_cmd -Secure -Username $username -Password $password

Write-Host "Rebooting"
Invoke-CrestronCommand $dev "reboot" -Secure -Username $username -Password $password

