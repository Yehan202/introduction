n1= int(input("dime un numero "))
n2 = int(input("dime otro numero "))

if n1 > n2 :
    n1,n2 = n2,n1

for numeros in range (n1,n2+1) :
    if numeros % 2 == 0:
        print(numeros)
    