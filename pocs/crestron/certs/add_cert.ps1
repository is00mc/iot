Import-Module PSCrestron

$hostlist = Get-Content $PSScriptroot/devicelist.txt
$u = ''
$p = ''
$uid = ''
$certName = ''
$cn = ''
$uid1 = ''
$uid2 = ''

$lpath = ''
$rpath = '/CERT/root_cert.cer'
$remcmd1 = "certif rem root $($cn) $($uid1) $($p)"
$remcmd2 = "certif rem root $($cn) $($uid2) $($p)"
$addcmd = "certif add root $($certName) $($uid) $($p)"
$dev = ""
#try {
#Foreach ($dev in $hostlist) {
Write-Host $dev '- Sending cert'

Send-FTPFile $dev $lpath $rpath -Secure -Username $u -Password $p
Write-Host $dev '- Adding cert to list'

Invoke-CrestronCommand $dev $addcmd -Secure -Username $u -Password $p
#}
#}
#Catch {Write-Host $dev "error"}
