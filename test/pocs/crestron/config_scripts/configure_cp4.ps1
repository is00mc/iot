Import-Module PSCrestron

# current device settings
$dev = ''
$username = ''
$password = ''


# target settings
$ip = ''
$subnet = ''
$gateway = ''
$hostname = ''
$dns1 = ''
#$dns2 = ''
#$ntp = ''
#$domain = ''
$timezone = '014'

# text console commands
$timezone_cmd = "timezone $($timezone)"
$ip_cmd = "ipaddress 0  $($ip)"
$subnet_cmd = "ipmask 0 $($subnet)"
$gateway_cmd = "defrouter 0 $($gateway)"
$hostname_cmd = "hostname $($hostname)"
$dns1_cmd = "adddns $($dns1)"
$dns2_cmd = "adddns $($dns2)"
$ntp_server_cmd = "sntp server:$($ntp)"
$ntp_start_cmd = "sntp start"
$dhcp_cmd = "dhcp 0 off"
$domain_cmd = "domainname $($domain)"



# set timezone
Write-Host "setting $($dev) timezone..."
Invoke-CrestronCommand $dev $timezone_cmd -Secure -Username $username -Password $password

# set ntp server
#Write-Host "setting ntp server"
#Invoke-CrestronCommand $dev $ntp_server_cmd -Secure -Username $username -Password $password

#start ntp server
#Write-Host "starting ntp server"
#Invoke-CrestronCommand $dev $ntp_start_cmd -Secure -Username $username -Password $password

# disable dhcp
Write-Host "disabling dhcp"
Invoke-CrestronCommand $dev $dhcp_cmd -Secure -Username $username -Password $password

# set ip address
Write-Host "setting $($dev) ip address"
Invoke-CrestronCommand $dev $ip_cmd -Secure -Username $username -Password $password

# set subnet
Write-Host "setting $($dev) subnet"
Invoke-CrestronCommand $dev $subnet_cmd -Secure -Username $username -Password $password

# set gateway
Write-Host "setting $($dev) gateway"
Invoke-CrestronCommand $dev $gateway_cmd -Secure -Username $username -Password $password

#set hostname
Write-Host "setting $($dev) hostname"
Invoke-CrestronCommand $dev $hostname_cmd -Secure -Username $username -Password $password

# set dns
Write-Host "setting dns1"
Invoke-CrestronCommand $dev $dns1_cmd -Secure -Username $username -Password $password
#Write-Host "setting dns2"
#Invoke-CrestronCommand $dev $dns2_cmd -Secure -Username $username -Password $password

#set domain
#Write-Host "setting domain"
#Invoke-CrestronCommand $dev $domain_cmd -Secure -Username $username -Password $password

# getting device info
Write-Host "getting version info"
Get-VersionInfo $dev -Secure -Username $username -Password $password


# reboot
Write-Host "rebooting $($dev)"
Invoke-CrestronCommand $dev "reboot" -Secure -Username $username -Password $password

# debug
#Write-Host $timezone_cmd
#Write-Host $ip_cmd
#Write-Host $subnet_cmd
#Write-Host $gateway_cmd
#Write-Host $hostname_cmd
#Write-Host $dns1_cmd
#Write-Host $dns2_cmd
#Write-Host $ntp_server_cmd
#Write-Host $ntp_start_cmd
