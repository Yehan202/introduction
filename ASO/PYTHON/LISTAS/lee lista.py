import sys

usuario =[]
group=[]
memoria=[]
for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-u' :
        usuario.append(sys.argv[i + 1])
        group.append(sys.argv[i + 2])
        memoria.append(sys.argv[i + 3])


for i in range(1,len(sys.argv)) :
    if sys.argv[i] == '-user' :
        for j in  range(len(usuario)) :
            print(f"Usuario: {usuario[j]}, Grupo: {group[j]}, Memoria: {memoria[j]}")
