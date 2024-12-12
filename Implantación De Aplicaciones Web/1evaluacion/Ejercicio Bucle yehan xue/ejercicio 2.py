import random
from random import randint
time = 1
numero_adivina = randint(1, 100)
numero = int(input("Dime un número entre 1 y 100: "))

for  time in range (1,10):
    if numero != numero_adivina:
        time +=1
        if numero < numero_adivina:
            print("Es mayor")
        else:
            print("Es menor")
    else: 
        print("has ganado")
        break
    
    numero = int(input("Intenta de nuevo: "))
if time == 10 :
    print("¡Has perdido!")
