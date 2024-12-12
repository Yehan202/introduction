x1:float = float(input("indicame el posicione de x1 "))
x2:float = float(input("indicame el posicione de x2 "))
y1:float = float(input("indicame el posicione de y1 "))
y2:float = float(input("indicame el posicione de y2 "))

print(f"la distancia entre ello es {abs(x1-x2)} i y {abs(y1-y2)} j")

distancia = ((x2-x1)**2+(y2-y1)**2)**0.5

print(f"la distancia entre dos puntos es {distancia}")