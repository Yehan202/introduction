# Realizar un ejemplo de menú, donde podemos escoger las distintas opciones hasta que
# seleccionamos la opción de “Salir”.

import datetime

# Inicializar la opción
opcion = ""

# Bucle principal del menú
while opcion != "4":
    print("\n----- Menú -----")
    print("1. Opción 1: Saludar")
    print("2. Opción 2: Mostrar la hora")
    print("3. Opción 3: Calcular suma de dos números")
    print("4. Opción 4: Salir")
    print("----------------")
    
    # Solicitar la opción del usuario
    opcion = input("Elige una opción: ")

    if opcion == "1":
        print("¡Hola! Espero que estés teniendo un buen día.")
    elif opcion == "2":
        hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"La hora actual es: {hora_actual}")
    elif opcion == "3":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        suma = num1 + num2
        print(f"La suma de {num1} y {num2} es: {suma}")
    elif opcion == "4":
        print("Saliendo del programa. ¡Hasta luego!")
    else:
        print("Opción no válida, por favor intenta de nuevo.")
