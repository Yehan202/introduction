n1= None

while n1 != 0 :
    n1 = int(input("introduzcame otro numero "))
    if (n1 % n1 == 0  and n1%2!= 0) or n1 == 2 :
        print(f"{n1} es un numero primo")
        break
    else:
        print("este numero no es un numero primo ")
