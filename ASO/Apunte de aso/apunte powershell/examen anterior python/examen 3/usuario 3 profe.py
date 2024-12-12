import sys 

count = 0 
suma=0.0 

for i in range(1,len(sys.argv)): 
   if sys.argv[i] == '-u': 
       suma += float(sys.argv[i+2]) 
       count +=1 

porcentaje = suma/10 *100 
print(f"Tenemos {count} usuarios, con {suma} (TB) utilizados de 10.00 (TB), una ocupación total de {porcentaje}%")  
