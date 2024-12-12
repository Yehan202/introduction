## -usuario -grupo -password
$user = "usuario"
$grupo = "grupo"
$password = "password"

for($i=0;$i -lt $args.Length;$i++){

    if ( $args[$i] -eq '-usuario'){
        $user = $args[$($i+1)]
        }
    if ( $args[$i] -eq '-grupo'){
        $grupo = $args[$($i+1)]
        }
    if ( $args[$i] -eq '-password'){
        $password = $args[$($i+1)]
        }

    }

    Write-Output "Se ha creado el usuario : $user, de grupo : $grupo, con password : $password"