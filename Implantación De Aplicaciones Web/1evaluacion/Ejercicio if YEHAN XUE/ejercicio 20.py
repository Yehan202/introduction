peso:float = float(input("Cuanto pesa el paquete "))
destino:str = str(input("Cual es su destino "))
precio = 0.0

peso_gramo = peso*1000

if peso > 5:
        print(input("no son tranportados"))

else :
    if destino == "america del norte" :
        precio = 24
        print(f"el precio total es {peso_gramo*precio}")

    elif destino == "america central" :
        precio = 20
        print(f"el precio total es {peso_gramo*precio}")

    elif destino == "america del sur" :
        precio = 21
        print(f"el precio total es {peso_gramo*precio}")

    elif destino == "asia" :
        precio = 18
        print(f"el precio total es {peso_gramo*precio}")


    elif destino == "europa" :
        precio = 10
        print(f"el precio total es {peso_gramo*precio}")

