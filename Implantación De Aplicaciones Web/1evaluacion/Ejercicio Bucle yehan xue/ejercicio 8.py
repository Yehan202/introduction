inferior :int = int(input("dime el limite inferior "))
superior : int = int (input("dime el limite superior "))

while inferior > superior :
    print("el limite inferior debe ser menor que limite superior ")
    inferior :int = int(input("dime el limite inferior "))
    superior : int = int (input("dime el limite superior "))
   
y=0
suma = 0
x=None

while x != 0 :
    x = int(input("Dime un número (0 para terminar): "))

    if x < inferior or x > superior:
       y += 1 

    elif x == inferior or x == superior :
        print("este numero es igual que el limite")
    
    else:
        suma += x

print(f"la suma de los numeros es {suma} ")
print(f"habia {y} veces el numero en fuera de intervalo")
