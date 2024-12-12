A :int =  int(input("Dime una variable "))
B :int =  int(input("Dime otra variable "))
C:int=0
D:int=0


C:int=A
D:int=B
A:int=D
B:int=C


print(f"ahora el valor de A es {A} y B es {B}")