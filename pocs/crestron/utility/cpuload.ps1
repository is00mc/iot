$h = ''
$u = ''
$p = ''

$x = 1
$l = @()
$high = 0
clear
While ($x -ne 101) {
    Write-Host [*] Running CPULOAD $x/100
    $c = Invoke-CrestronCommand $h 'cpuload' -Secure -Username $u -Password $p 
    clear
    $c -match 'CPU:LOAD (?<percent>.+)%' >> $null
    $l += $Matches.percent
    if ($Matches.percent -ge $high) {
        $high = $Matches.percent
    }
    Write-host '[*] Current Load:' $matches.percent % -Separator '' 
    $sum = 0 
    foreach ($i in $l) {
        $sum += $i
    }
    $avg = $sum / $l.length
    Write-Host '[*] Current High:' $high % -Separator '' -NoNewLine
    Write-Host ' Current AVG:' $avg % -Separator ''
    $x += 1
    Write-Host ''
}
