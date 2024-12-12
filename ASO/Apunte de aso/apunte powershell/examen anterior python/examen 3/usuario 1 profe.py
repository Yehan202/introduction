import sys 

usuarios_creados=[] 

for i in range(1,len(sys.argv)): 
   if sys.argv[i] == '-u': 
       creado=False 
       for j in usuarios_creados: 
           if j == sys.argv[i+1]: 
               creado=True 
       if not creado: 
           usuarios_creados.append(sys.argv[i+1]) 
           print(f"Creando usuario {sys.argv[i+1]}") 
       else: 
           print(f"Usuario {sys.argv[i+1]} ya ha sido creado") 