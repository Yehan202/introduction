import sys

usuario =[]
usuario_usado =[]
contador = 1
for i in range(len(sys.argv)):
    if sys.argv[i] == '-u' :
        usuario.append(sys.argv[i + 1])

for j in range(len(usuario)):
    if usuario[j] not in usuario_usado : 
        usuario_usado.append(usuario[j])
        print(f"Usuario creado : {usuario[j]}")  
    
    elif usuario[j] in usuario_usado :       
        print(f"Usuario creado : {usuario[j]} {contador}")
        contador += 1