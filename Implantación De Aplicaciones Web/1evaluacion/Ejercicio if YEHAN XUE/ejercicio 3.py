n1:int = int(input("Dime un número: "))

ultimo_digito:str = str(n1)[-1]

if n1 == 0:
    print("es cero")

elif ultimo_digito in ('1', '3', '5', '7', '9'):
    print("El número es impar")

elif ultimo_digito in ('0', '2', '4', '6', '8'):
    print("El número es par")


