#Crea un script en PowerShell llamado csv.ps1 que cumpla con las siguientes características:

#csv.ps1 -usuario [nombre usuario] -grupo [grupo]
#El script debe agregar una entrada al archivo usuarios.csv (si no existe, debe crearlo). El archivo usuarios.csv tendrá el siguiente formato:
#La contraseña debe generarse de forma aleatoria, haz que sea una cadena alfanumérica de 8 caracteres.

#Al ejecutar el script, debe mostrar un mensaje en la terminal indicando que el usuario ha sido creado. El mensaje debe seguir el formato:

#El usuario [usuario] ha sido creado con la password [password] en el grupo [grupo].
#En el caso de que el usuario exista, la salida será :
#El usuario [usuario] ya existe, no se puede crear.


param (
    #[Parameter(Mandatory = $true)] en el caso de que ingreses usuario, te lo pregunta
    [string]$usuario,
       
    [string]$grupo="A"
)

$archivoCSV = "E:\aso\usuario1\usuarios.csv"


if(! $usuario){ #caso de no recibir nombre de usuario se para
echo "no me han dado usuario"
exit
}


function GenerarPassword {
    $chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#~$%&"
    $salida=""
    for ($i=0;$i -lt 8;$i++){ 
     $r = Get-Random -Minimum 0 -Maximum $chars.Length
     $salida+=$chars[$r]
    }
    Write-Output $salida
}

# Si no existe crear el encabezado
if (!(Test-Path $archivoCSV)) {
    Write-Output "usuario,grupo,password" >  $archivoCSV 
}

# Si el usuario ya existe
$usuariosExistentes = Import-Csv -Path $archivoCSV

if ($usuariosExistentes | Where-Object { $_.usuario -eq $usuario }) 
{
    Write-Output "El usuario $usuario ya existe, no se puede crear."
}else{
    $password = GenerarPassword
    Write-Output "$usuario,$grupo,$password" >> $archivoCSV
    Write-Output "El usuario $usuario ha sido creado con la password $password en el grupo $grupo."
}
