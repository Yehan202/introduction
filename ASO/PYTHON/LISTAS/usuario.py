import sys

usuarios=[]
grupos=[]
tamaño=[]

for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-u':
        usuarios.append(sys.argv[i+1])
        grupos.append(sys.argv[i+2])
        tamaño.append(sys.argv[i+3])

for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-user':
        for j in range(len(usuarios)):
            print(f'El usuario: {usuarios[j]} tiene {tamaño[j]}')

          
grupos_sin_repetir=[]
tamaño_del_grupo=[]

for i in range(1,len(sys.argv)):
    if sys.argv[i] == '-group':
        for j in grupos:
            if grupos_sin_repetir.count(j) == 0:
                grupos_sin_repetir.append(j)
                tamaño_del_grupo.append(float(0.0))
        #print(grupos_sin_repetir)
        for g in range(len(grupos_sin_repetir)):
            #print("Es el grupo",g)
            for k in range(len(usuarios)):
                if(grupos_sin_repetir[g] == grupos[k]):
                    #print(f'El usuario: {usuarios[k]} tiene {tamaño[k]}')
                    tamaño_del_grupo[g]+=float(tamaño[k][:2])
                    #print(tamaño_del_grupo[g])

        for g in range(len(grupos_sin_repetir)):
            print(f'El grupo {grupos_sin_repetir[g]} tiene {tamaño_del_grupo[g]}GB')    