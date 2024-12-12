resultado:int = int(input("dime el resultado del dado : "))

if resultado == 1 :
    print(f"la cara opuesta es seis")
elif resultado == 6 :
    print(f"la cara opuesta es uno")
elif resultado == 2 :
    print(f"la cara opuesta es cinco")
elif resultado == 5 :
    print(f"la cara opuesta es dos")
elif resultado == 3 :
    print(f"la cara opuesta es cuatro")
elif resultado == 4 :
    print(f"la cara opuesta es seis")
else :
    print("ERROR:número incorrecto")