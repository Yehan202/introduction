import sys

suma=0.0
unidad_salida="GB"

for i in range(1,len(sys.argv)):
    unidades=sys.argv[i][-2:]
    medida=float(sys.argv[i][:-2])
    if unidades=="KB":
        medida=medida/10**6
    if unidades=="MB":
        medida=medida/10**3
    if unidades=="GB":
        medida=medida
    if unidades=="TB":
        medida=medida*10**3        
    suma=suma+medida    

    
print(f'{suma} ({unidad_salida})')