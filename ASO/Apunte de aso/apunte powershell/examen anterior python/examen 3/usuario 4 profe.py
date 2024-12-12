import sys 

count = 0 
suma=0.0 
usuario=[] 
capacidad=[] 

for i in range(1,len(sys.argv)): 
   if sys.argv[i] == '-u': 
       suma += float(sys.argv[i+2]) 
       usuario.append(sys.argv[i+1]) 
       capacidad.append(float(sys.argv[i+2])) 
       count +=1 

porcentaje = suma/10 *100 
print(f"Tenemos {count} usuarios, con {suma} (TB) utilizados de 10.00 (TB), una ocupación total de {porcentaje}%") 

media= 10/count 

salida="Tenemos los usuarios " 
for j in range(1,len(sys.argv)): 
   if sys.argv[j]  == '-encima_media': 
       for i in range(len(usuario)): 
           if capacidad[i] > media: 
               salida=salida+f'{usuario[i]} con {(capacidad[i]-media):.2f}(TB), ' 