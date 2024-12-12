import sys 

usuarios_creados=[] 
count=[] 

for i in range(1,len(sys.argv)): 
   if sys.argv[i] == '-u': 
       creado=False 
       for j in range(len(usuarios_creados)): 
           if usuarios_creados[j] == sys.argv[i+1]: 
               creado=True                 
       if not creado: 
           usuarios_creados.append(sys.argv[i+1]) 
           print(f"Creando usuario {sys.argv[i+1]}") 
           count.append(0) 
       else: 
           count[ usuarios_creados.index(sys.argv[i+1])]+=1 
           print(f"Creando usuario {sys.argv[i+1]}{count[ usuarios_creados.index(sys.argv[i+1])]}") 