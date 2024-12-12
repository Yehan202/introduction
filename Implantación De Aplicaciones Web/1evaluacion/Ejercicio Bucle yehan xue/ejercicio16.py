# Una empresa les paga a sus empleados con base en las horas trabajadas en la semana.
# Realice un algoritmo para determinar el sueldo semanal de N trabajadores y, además, 
# calcule cuánto pagó la empresa por los N empleados.


# numero de trabajador
# hora cada uno
# cantidada total
sueldo_total = 0
trabajador : int = int ( input("trabajadores hay : "))

for i in range (1, trabajador+1) :
    hora : float = float(input(f"dime las hora que trabaja el trabajador {i} en la semana "))
    salario = float(input("cuantos paga cada hora: "))
    dia = int(input("cuandos dias trabajas cada semana : "))
    sueldo = hora*salario*dia
    sueldo_total += sueldo 
    print(f"el sueldo semanal de trabajado {i} es {sueldo}")
print(f"el sueldo total que hay que pagar la empresa es {sueldo_total} euros")    