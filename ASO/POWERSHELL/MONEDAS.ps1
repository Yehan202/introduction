$tiradas=1000
$tresCara =0
for ($i=0;$i -lt $tiradas; $i++){
    $moneda1 =$(Get-Random -Minimum 0 -Maximum 2)
    $moneda2 =$(Get-Random -Minimum 0 -Maximum 2)
    $moneda3 =$(Get-Random -Minimum 0 -Maximum 2)

    
    if (($moneda1 -eq 0) -and ($moneda2 -eq 0) -and ($moneda3 -eq 0)){
         $tresCara++
         }
    }
echo "La probabilidad es $([math]::Round(($tresCara / $tiradas) * 100, 2))%"#para que devuelve una probabilidad


    