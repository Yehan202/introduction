hsalida = int(input("dime la hora de salida "))
msalida = int(input("dime el minuto de salida "))
ssalida = int(input("dime el segundo de salida "))

segsalida = hsalida*3600+msalida*60+ssalida



tiempo:int = int(input("dime cuandos segundos requiere para llegar a ciudad B : "))

tiempoTotal = tiempo+segsalida

hora:int = int(tiempoTotal/3600)%24
min:int = int(tiempoTotal/60)%60 
seg:int = int(tiempoTotal)%60

print(f"tienes {hora} hora {min} minutos {seg} segundos para llegar a ciuadad B")