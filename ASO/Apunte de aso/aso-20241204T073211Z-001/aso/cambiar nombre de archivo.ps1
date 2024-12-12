[int]$puerta = Read-Host "1-rojo,2-azul,3-verde,4-amarillo"
if ($puerta -eq 1) {
    Write-Output "puerta roja"
}elseif ($puerta -eq 2) {
    Write-Output "puerta azul"
}elseif ($puerta -eq 3) {
    Write-Output "puerta verde"
}elseif ($puerta -eq 4) {
    Write-Output "puerta amarillo"
}else {
    Write-Output "error"}