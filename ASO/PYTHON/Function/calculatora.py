import sys

def  mul_div(lista):
    a=[]
    for j in range(2,len(lista)-1):
        if lista[j] == '*' or lista[j] == '/' :
            if lista[j] == '*':
                a.append(float(lista[j-1])*float(lista[j+1]))
            if lista[j] == '/':
                a.append(float(lista[j-1])/float(lista[j+1]))            
            j=j+1
        else:
            a.append(lista[j-1])                
    if lista[len(lista)-2] != '*' or lista[len(lista)-2] != '/':
        a.append(lista[len(lista)-2])
        a.append(lista[len(lista)-1]) 
    return a

def suma_resta(lista):
    out=float(lista[0])
    for j in range(1,len(lista),2):
        if lista[j] == '+':
            out = out + float(lista[j+1])
        if lista[j] == '-':
            out = out - float(lista[j+1])
    return out

aux=mul_div(sys.argv)
print(str(suma_resta(aux)))