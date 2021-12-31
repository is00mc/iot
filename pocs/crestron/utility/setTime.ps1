import-module PSCrestron

# TIMEDATE [hh:mm:ss mm-dd-yyyy]
#         hh:mm:ss - time in hours (use 24hr), mins and secs
#         mm/dd/yyyy or mm-dd-yyyy - date in months(1-12), day(1-31) and year
#         No parameter - displays current setting
#


$time = $args[0]
$dev = ''
$username = ''
$password = ''


function send-cmd {
    param($cmd)
    Invoke-CrestronCommand $dev $cmd -Secure -Username $username -Password $password
}

if ($time -eq '-wd') {
    send-cmd -cmd @('sntp stop', 'time 12:00:00 09-15-2021', 'time')
}
elseif ($time -eq '-ah') {
    send-cmd -cmd @('sntp stop', 'time 21:49:20 09-15-2021', 'time')
}
elseif ($time -eq '-we') {
    send-cmd -cmd @('sntp stop', 'time 12:00:00 09-18-2021', 'time')
}
elseif ($time -eq '-n') {
    send-cmd -cmd @('sntp start', 'time')
}
elseif ($time -eq '-g') {
    send-cmd -cmd 'time'
}
else {
    Write-Host Usage:
    Write-Host '    -wd = weekday (12:00:00 09-15-2021)'
    Write-Host '    -ah = after hours (21:49:20 09-15-2021)'
    Write-Host '    -we = weekend (12:00:00 09-18-2021)'
    Write-Host '    -n  = sync with ntp'
    Write-Host '    -g = get current time'
}
