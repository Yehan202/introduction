#Haz un script llamado rnd.ps1 que escoja un numero aleatorio entre 1 y 20, pregunte al usuario, 
#le diga si es más pequeño o más grande y que continué hasta que acierte. Cuando el usuario acierte haz que muestre el número de intentos.

$numero = $(Get-Random -Minimum 0 -Maximum 20)

$contador = 0
$x = -1
# -ne no es igual
while ($x -ne $numero) {
    [int]$x = Read-Host "dime un numero"
    $contador ++
    if ($x -ge $numero){
        Write-Output "menor que ese"
    }
    else{
        Write-Output "Mayor que es"
    }
}
Write-Output "has adiminado, ha hecho $contador intentos"