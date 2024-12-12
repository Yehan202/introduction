venta1:float = float(input("cantidad de dinero de la primera venta"))
venta2:float = float(input("cantidad de dinero de la segunda venta"))
venta3:float = float(input("cantidad de dinero de la tercera venta"))

Sueldobase = float(input("dime la cantidad base de usted"))

comision = (venta1+venta2+venta3)*0.1

print(f"el sueldo base de usted es {Sueldobase} y comision que puedes obtener es {comision}. Finalmente, usted puedes recibirte {Sueldobase+comision}")