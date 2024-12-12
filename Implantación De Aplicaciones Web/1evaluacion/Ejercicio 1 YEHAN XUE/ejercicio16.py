distancia:float = float(input("dime la distancia entre ello (km)"))

v1:float = float (input("dime la velocidad de coche1(km/h) "))
v2:float = float (input("dime la velocidad de coche2(km/h) "))

if v1>v2:
    tiempo:float = float(distancia/(v1-v2))
    minuto:float = tiempo*60
    print(f"El coche 1 alcanzara al coche 2 en {minuto} minutos.")

elif v1<v2:
    tiempo: float = float(distancia / (v2 - v1))
    minuto: float = tiempo * 60
    print(f"El coche 2 alcanzará al coche 1 en {minuto} minutos.")
    
else:
    print("Tienen la misma velocidad, no se alcanzarán.")






