x1:int = int(input("dime el x1 "))
y1:int = int(input("dime el y1 "))

x2:int = int(input("dime el x2 "))
y2:int = int(input("dime el y2 "))

r1 :int = int(input("dime el r1 "))
r2:int = int(input("dime el r2 "))

d = ((x2-x1)**2+(y2-y1)**2)**0.5

# exterior
if d > r1+r2 :
    print("son exteriores")

# tangentes exteriores
if d == r1+r2 :
    print("tangente exterior")

# secante
if d < r1+r2 :
    print("son secantes")

# interior
if d < r2-r1 :
    print("son interiores")

# tangentes interiores
if d == r2-r1 :
    print("tangentes interiores")

# concentricas

if d == 0 : 
    print("son cocentricas")



