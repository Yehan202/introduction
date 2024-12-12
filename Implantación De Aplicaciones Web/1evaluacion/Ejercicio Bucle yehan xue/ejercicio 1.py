numero = int(input("dime un numero"))
 
if numero < 0 :
    # si numero es menor que 0, no hay solocion
    print ("Introduzca un numero valido")
elif numero == 0 or numero == 1 :
    print("1")
    # si el numero es 0 o 1 el resultado es 1
else:
    factorial = 1
    i = 1
    for i in range (2,numero + 1 ):
        factorial *= i
        i += 1
    print (f"la factorial de {numero} es {factorial}")

    # cuando el rango esta entre 2 a numero+1
    # factorial es igual a i * fanctorial cual i suma cada vez que multiplica entre i y el variable factorial



