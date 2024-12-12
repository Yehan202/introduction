a                                                                                                                                                                                           :int= int(input("dime el lado A "))
b :int= int(input("dime el lado B "))
c :int= int(input("dime el lado C "))

if c**2 == a**2+b**2 or  b**2 == a**2+c**2 or a**2 == c**2+b**2 :
    print("cumple la teorema de pitagoras. Es un triangulo rectangulo")
elif a==b or a==c or c==b :
    print("tiene dos lados iguales, es un triangulo isosceles")
elif a==b==c :
    print("los tres lados son iguales, es un triangulo equilatero")
else :
    print("es un escaleno")
    