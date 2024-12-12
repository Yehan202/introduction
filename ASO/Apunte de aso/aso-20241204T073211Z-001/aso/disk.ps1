#Crea un script llamado disk.ps1 que imprima por pantalla el porcentaje que esta ocupada la partición C:
$disco = Get-PSDrive -Name E

$Porcent = ($disco.Used / ($disco.Used + $disco.Free))*100

Write-Output ("E: ocapada al {0:N2}%" -f $Porcent)

