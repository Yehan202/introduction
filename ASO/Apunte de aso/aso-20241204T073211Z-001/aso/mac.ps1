$año= Read-Host "en que año naciste ?"

$añoActual = (Get-Date).Year

$edad = $añoActual -$año

Write-Output "tienes $edad años"
 
