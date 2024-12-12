examen1:float = float(input("dime la nota que tienes en la primera parcial"))
examen2:float = float(input("dime la nota que tienes en la segunda parcial"))
examen3:float = float(input("dime la nota que tienes en la tercera parcial"))

examenfinal:float = float(input("dime la nota que tienes en el examen final"))
trabajofinal:float = float(input("dime la nota que tienes en el trabajo final"))

promedio = (examen1+examen2+examen3)/3
notafinal =promedio*0.55+examenfinal*0.3+trabajofinal*0.15

print(f"la nota final de usted es {notafinal}")

if notafinal < 5:
    print("Estás suspenso")
elif notafinal >= 5:
    print("Felicidades, estás aprobado")