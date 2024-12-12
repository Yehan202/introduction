minutos = float(input("dame una cantidad de minutos que quieres convertirse en horas y minutos"))
hora = minutos//60
min= minutos%60
print(f"tienes {int(minutos/60)} horas y {int(min)} minutos")