import sys

usuario =[]
memoria=[]
tamaño = 0
for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-u' :
        usuario.append(sys.argv[i + 1])
        memoria.append(sys.argv[i + 2])
        

for i in range(len(usuario)) :
    tamaño += float(memoria[i])
print(f"tienes {(i+1)} usuarios con memoria {tamaño} TB con la ocupacion maxima de 10 tb cual {tamaño//1} %")
