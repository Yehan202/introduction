import random

palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jóse come Coco", "Estás en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras)
pista = ["_" if palabra[i] != " " else " " for i in range(len(palabra))]
letras_usadas = []


usuario1 = input("Dime el nombre del usuario1: ")
usuario2 = input("Dime el nombre del usuario2: ")
turno = usuario1 

while "_" in pista:
    print(f"Es el turno de {turno}")
    print(" ".join(pista))
    
    opcion = input(f"{turno}, ¿quieres adivinar una 'letra' o la 'palabra' completa?: ").lower()
    
    if opcion == "letra":
        letra = input("Dime una letra: ").lower()
        
        while len(letra) != 1 or letra in letras_usadas:
            if len(letra) != 1:
                print("Por favor, introduce solo una letra.")
            elif letra in letras_usadas:
                print(f"Ya has introducido la letra '{letra}', intenta con otra.")
            letra = input("Dime una letra: ").lower()
        
        letras_usadas.append(letra)
        
        if letra in palabra.lower():
            print(f"¡{turno} ha acertado la letra '{letra}'!")
            for i in range(len(palabra)):
                if palabra[i].lower() == letra:
                    pista[i] = palabra[i]
        else:
            print(f"La letra '{letra}' no está en la palabra. Cambio de turno.")
            turno = usuario2 if turno == usuario1 else usuario1

    elif opcion == "palabra":
        palabra_adivinada = input("Dime la palabra completa: ").lower()
        
        if palabra_adivinada in palabra.lower():
            for i in range(len(palabra)):
                if palabra[i].lower() == palabra_adivinada:
                    pista[i] = palabra[i]
        else:
            print(f"La palabra '{palabra_adivinada}' no es correcta. Cambio de turno.")
            turno = usuario2 if turno == usuario1 else usuario1

print(f"La palabra era '{palabra}'. ¡Fin del juego!")
