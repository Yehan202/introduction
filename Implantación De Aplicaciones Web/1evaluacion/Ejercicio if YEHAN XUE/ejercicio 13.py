dia:int = int(input("Dime qué día es: "))
mes:int = int(input("Dime qué mes es: "))
año:int = int(input("Dime qué año es: "))

if año > 2024:
    print("incorrecto")

elif mes == 2:
    if (dia <= 28):
        print("correcto")
    elif dia == 29 and ((año % 4 == 0 and año % 100 != 0) or año % 400 == 0):
        print("correcto")
    else:
        print("incorrecto")
elif mes in [1, 3, 5, 7, 8, 10, 12] and dia <= 31:
    print("correcto")
elif mes in [4, 6, 9, 11] and dia <= 30:
    print("correcto")

else:
    print("incorrecto")
