import sys
print(sys.argv)
resultado = int(sys.argv[1])

for j in range (2,len(sys.argv),2): 
    operacion = sys.argv[j]
    numeros = int(sys.argv[j+1])

    if operacion == "+" :
        resultado += numeros

    elif operacion == "-" :
        resultado -= numeros
    elif operacion == "*" :
        resultado *= numeros
    elif operacion == "/":
        resultado /= numeros

    else : 
        print('introduce algo valido ')
print(resultado)

