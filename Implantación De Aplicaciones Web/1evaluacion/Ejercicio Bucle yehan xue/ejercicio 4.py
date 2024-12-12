mayor = 0
menor = 0 
cero = 0
time = int (input("cuantos veces quieres introducir : "))

while time != 0 :
    numero = int(input("dime un numero : "))

    if numero == 0 :
        cero += 1
        time -=1

    elif numero > 0 :
        mayor += 1
        time -=1

    elif numero < 0 :
        menor += 1
        time -=1


print (f"tienes {cero} veces igual a cero")
print (f"tienes {mayor} veces mayor a cero")
print (f"tienes {menor} veces menor a cero")