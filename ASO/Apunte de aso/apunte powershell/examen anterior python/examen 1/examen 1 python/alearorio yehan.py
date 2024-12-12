# ejercicio 1: 
import random
numero_alearotio = random.randint(1,100)
punto = 0

numero :int = int(input("dime un numero entre 1-100 : "))

if abs(numero_alearotio-numero) >= 30 :
    print("has perdido")
    punto += 0
    print(f"tienes {punto} en total")

elif abs(numero_alearotio-numero) < 30 : 
    print("Estás cerca")
    punto += 10

    numero1 :int = int(input("dime otro numero entre 1-100 : "))
    if abs(numero_alearotio-numero1) >= 20 :
        print("has perdido")
        punto +=0
        print(f"tienes {punto} en total")

    elif abs(numero_alearotio-numero1) < 20 :
        print ("estas cerca")
        punto += 30

        numero2 :int = int(input("dime ultimo numero entre 1-100 : "))
        if abs(numero_alearotio-numero2) >= 5 :
            print("has perdido")
            print(f"tienes {punto} en total")
        elif abs(numero_alearotio-numero2) < 5 :
            punto += 40
            print(f"tienes {punto} en total")
