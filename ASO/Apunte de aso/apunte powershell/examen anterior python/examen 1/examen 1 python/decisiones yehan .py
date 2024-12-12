# ejercicio 2

puerta :str = str(input("elige entre puerta roja o puerta verde(roja o verde) : "))
punto = 0

if puerta == "roja" :
    punto += 10 
    print(f"entras a museo ahora tienes {punto} puntos ")
    

    museo:str = str (input("ir a sala o salir de museo(sala o salir) "))

    if museo == "sala" :
        punto -= 10
        print(f"la momia se levanta el juego acabado, tienes {punto} puntos ")
    elif museo == "salir" :
        print(f"has encontrado un taxi rojo , ahora tienes {punto} puntos  ")
        taxi:str =  str(input("coges este taxi o no (si o no) "))

        if taxi == "si" :
            punto += 20 
            print(f"el juego acabado, tienes {punto} puntos ") 
        elif taxi == "no" :
            punto -= 10
            print(f"ha caido un rayo en ti, el juego se ha acabado tienes {punto} puntos ")




elif puerta == "verde" :
    punto += 20
    print(f"entras bosque con un rio, has ganado 20 puntos, ahora tienes {punto} puntos ")
    

    bosque : str = str(input("estas en un bosque quieres entrar a bosque o coger una lancha(entrar o coger) "))

    if bosque == "entrar" :
        punto -= 10
        print(f"has perdido en el bosque, el juego acabado tienes {punto} puntos ")
    elif bosque == "coger" :
        punto += 20
        print(f"has cogido una lancha en el rio y va a bajar el rio, ganas 20 puntos ahora tienes {punto} puntos ")

        direccion : str = str (input("has llegado a una difucación, decide tu direccion (izquierda o derecha)"))

        if direccion == "derecha" :
            punto -= 10
            print(f"has caido por una cascada, pierdes 10 puntos y el juego se ha acabado y tienes {punto} puntos")
        elif direccion == "izquierda" : 
            punto += 30
            print(f" has llegado un museo ganas 30 puntos, ahora tienes {punto} puntos ")

            m_verde : str = str (input("has venido el museo desde la lancha, puedes irte la sala o salirte (sala o salir) "))

            if m_verde == "sala" :
                punto -= 10
                print(f"la momia se levanta pierdes 10 puntos, y el juego se ha acabado ahora tienes {punto} puntos")
            elif m_verde == "salir" :
                print (f"has encontrado un taxi, el punto no suma")
                taxi_verde = str(input("has encontrado un taxi verde, quieres coger este taxi? (si o no)"))
                if taxi_verde == "si" :
                    punto += 20
                    print(f"has vuelto a casa, ganas 20 puntos. El juego ha terminado tienes {punto} puntos ")
                else :
                    punto -= 10
                    print(f"ha caido un rayo en ti, el juego ha terminado y tienes {punto} puntos")
            else :
                print("introduzca algo valido ")
                chance2 = input("vuelve a contestar")
                if chance2 == "si" :
                    punto += 20
                    print(f"has vuelto a casa, ganas 20 puntos. El juego ha terminado tienes {punto} puntos ")
                else :
                    punto -= 10
                    print(f"ha caido un rayo en ti, el juego ha terminado y tienes {punto} puntos")          

