tipo :str = input("Dime el tipo de uva (A o B): ")
tamaño : str = input("Dime el tamaño de la uva (1 o 2): ")
precio :int= int(input("fija el precio inicial"))
ganancia = 0.0  

if tipo == "A":
    if tamaño == "1":
        ganancia = 20
        print(f"El ganancia es {ganancia} céntimos")
        print(f"el precio es {precio+ganancia} centimos ")
    elif tamaño == "2":
        ganancia = 30
        print(f"El ganancia es {ganancia} céntimos")
        print(f"el precio es {precio+ganancia} centimos ")

elif tipo == "B":
    if tamaño == "1":
        ganancia = -30
        print(f"El ganancia es {ganancia} céntimos")
        print(f"el precio es {precio+ganancia} centimos ")

    elif tamaño == "2":
        ganancia = -50
        print(f"El ganancia es {ganancia} céntimos")
        print(f"el precio es {precio+ganancia} centimos ")
else:
    print("Tipo de uva o tamaño inválido")
