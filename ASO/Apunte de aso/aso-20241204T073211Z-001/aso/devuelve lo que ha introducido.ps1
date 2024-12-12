
[int]$puerta = Read-Host "1-rojo,2-azul,3-verde,4-amarillo"
if ($puerta -eq 1) {
    Write-Output "puerta roja,perdido"
}elseif ($puerta -eq 2) {
    Write-Output "puerta azul,perdido"
}elseif ($puerta -eq 3) {
    $moneda = Read-Host "puerta verde,lanza una moneda (cara o cruz)"

    if ($moneda -eq "cara"){
        Write-Output "has ganado"}
    else{
        Write-Output "has perdido"}
    
}elseif ($puerta -eq 4) {
    Write-Output "puerta amarillo,perdido"
}else {
    Write-Output "error"}