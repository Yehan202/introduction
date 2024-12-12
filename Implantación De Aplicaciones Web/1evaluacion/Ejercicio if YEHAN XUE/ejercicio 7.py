base :int = int(input("dame una base "))
exponente :int= int(input("dime su exponente "))
potencia = base**exponente

if exponente > 0 :
    print(f"la potencia es {base}**{exponente} cual {potencia}")
elif exponente == 0 :
    print(f"el resultado es 1")
elif exponente < 0 :
     print(f"el resultado es 1/{base}**{exponente} cual {1/potencia}")