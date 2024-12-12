import sys

usuario =[]
usuario_usado =[]

for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-u' :
        usuario.append(sys.argv[i + 1])

for j in range(len(usuario)):
    if usuario[j] not in usuario_usado : 
        usuario_usado.append(usuario[j])
        print(f"Usuario creado : {usuario[j]}")  
    elif usuario[j] in usuario_usado :
        print(f"usuario {usuario[j]} ya ha sido creado")
           
