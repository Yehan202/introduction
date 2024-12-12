correcta = int(input("dime los numeros de respuestas correctas "))
incorrecta = int(input("dime los numeros de respuestas incorrectas"))
blanco = int (input("dime los ejercicios que has dejado en blanco"))

numeroejercicio = correcta+incorrecta+blanco
notaMax=numeroejercicio *5

print(f"Tienes {correcta} ejercicios correctas , {incorrecta} ejercicios incorrectas y {blanco} ejercicios en blanco")

print(f"Tu nota final es {correcta*5+incorrecta*-1} / {notaMax}")

