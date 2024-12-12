# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Para esto, se registran los días que trabajó y las horas de cada día. Realice un algoritmo
# para determinar el sueldo semanal de N trabajadores y además calcule cuánto pagó la
# empresa por los N empleados.

sueldo_total = 0
trabajador : int = int ( input("trabajadores hay : "))

for i in range (1, trabajador+1) :
    dia = int(input("cuandos dias trabajas cada semana : "))
    for x in range (1,dia+1) :
        hora = float(input(f"cuandos horas has trabajado en dia {x} :")) 
        hora += hora
    salario = float(input("cuantos paga cada hora: "))
    sueldo = hora*salario*dia
    sueldo_total += sueldo 
    print(f"el sueldo semanal de trabajado {i} es {sueldo}")
print(f"el sueldo total que hay que pagar la empresa es {sueldo_total} euros")    