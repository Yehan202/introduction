descartado : str = ""
sumT : float = 0
Ntot : int = 1
N : int = 0
temperatura : float = 0
respuesta : str = "si"
media : float = 0
while respuesta!="no":
    temperatura = float(input(f"Introduce la temperatura de la persona {Ntot}: "))
    respuesta : str = input("¿Quieres introducir más temperaturas?(sí/no). Por defecto sí. ")
    if temperatura > 40 or temperatura < 35:
      descartado += str(temperatura)+", "
    else:
      sumT += temperatura
      N +=1
    Ntot +=1

print(f"Se han metido un total de {Ntot} personas, de las cuales hemos descartado las siguientes temperaturas:")
print(f"{descartado} (ºC)")
media=sumT/N
print(f"Es decir que la temperatura media es de {media} (ºC) para las {N} personas")