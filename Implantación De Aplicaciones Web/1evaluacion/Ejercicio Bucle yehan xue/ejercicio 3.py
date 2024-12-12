suma = 0

numero : int = int ( input("introduzca un numero "))
i = 0
while numero != 0:

    numero : int = int ( input("introduzca otro numero "))
    suma += numero 
    # guarda los numeros que han introducido cada vez suma la cantidad de numero
    i += 1
    # contador, cada vez en bucle el i suma 1
    if numero == 0 :
        break

print (f"suma de numero {suma} y la media es {suma/i}")
 
