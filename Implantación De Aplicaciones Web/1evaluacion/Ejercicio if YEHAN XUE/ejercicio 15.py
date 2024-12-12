alumno :int= int(input("cuantos alumnos hay "))
cobro_alumno :float = 0.0
pago_compania :float = 0.0 
autobus = 4000

if alumno >= 100 :
    cobro_alumno = 65
    
    print(f"el coste cada alumno es {cobro_alumno} euros")
    
elif alumno >= 50 and alumno <= 99 :
    cobro_alumno = 70
    print(f"el coste cada alumno es {cobro_alumno} euros")
elif alumno >= 30 and alumno <= 49 :
    cobro_alumno = 95
    print(f"el coste cada alumno es {cobro_alumno} euros")

elif alumno < 30 :
    cobro_alumno = autobus/alumno
    print(f"el coste cada alumno es {cobro_alumno} euros")


     
        