import random

palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jóse come Coco", "Estás en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras)
pista = ["_" if palabra[i] != " " else " " for i in range(len(palabra))]

letras_usadas = []

usuario1 = str(input("Dime el nombre del usuario 1: "))
usuario2 = str(input("Dime el nombre del usuario 2: "))
turno = usuario1

while "_" in pista:
    print(f" {turno}, es tu turno")
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
            print(f"¡Has acertado la letra '{letra}'!")
            for i in range(len(palabra)):
                if palabra[i].lower() == letra:
                    pista[i] = palabra[i]
        else:
            print("No has acertado la letra. Cambio de turno.")
            turno = usuario2 if turno == usuario1 else usuario1

    elif opcion == "palabra":
        palabra_adivinada = input("Dime la palabra completa: ").lower()

        if palabra_adivinada == palabra.lower():
            print(f"¡Felicidades, {turno} ha adivinado la palabra completa!")
            pista = list(palabra)  
            break 
        else:
            print("No has acertado la palabra. Cambio de turno.")
            turno = usuario2 if turno == usuario1 else usuario1

print(f"\n¡Juego terminado! La palabra era: '{palabra}'.")
