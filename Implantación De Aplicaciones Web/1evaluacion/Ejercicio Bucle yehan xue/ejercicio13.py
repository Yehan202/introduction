dia_trabaja = 0
hora = 0
for dia in range(7) :
    trabaja = str(input("hoy trabajas ? "))
    if trabaja == 'si' :
        dia_trabaja += 1
        hora_trabajado = float(input('cuantas horas has trabajodo hoy '))
        hora += hora_trabajado
    else :
        print('descanse bien')

if dia_trabaja < 6 :
    print("no has trabajado suficiente")
else :
    salario = float(input('cuantos te cobra la hora? '))
    print(f'tu salario total es {salario*hora} ')
    print(f'la hora total ha trabajado es {hora} ')

