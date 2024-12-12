base:int = int(input("dime el base "))
exponente:int = int(input("dime el exponente "))


resultado=1
while exponente != 0 :
    exponente -= 1
    resultado *= base
print(f"el resultado de la potencia es {resultado}")