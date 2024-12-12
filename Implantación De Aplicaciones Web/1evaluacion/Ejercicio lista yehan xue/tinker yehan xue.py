import random
import time
import os

# posibilidad de ruleta
ruleta_valores = [100, 200, 300, 400, 500, 600, 700, 800, 900, "Pierde turno", "Quiebra"]

# palabra y pistas de ruleta.
palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jose come Coco", "Estas en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras).lower()
pista = ["_" if palabra[i] != " " else " " for i in range(len(palabra))]

letras_usadas = []

# usuarios
usuarios = []
for i in range(3):
    usuario = input(f"Dime el nombre del usuario {i + 1}: ")
    usuarios.append({"nombre": usuario, "puntos": 0})#añade nombres y puntos
turno = 0

def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')

# Girar ruleta con animación
def girar_ruleta():
    print("¡Girando la ruleta!")
    for _ in range(20):
        ruleta = random.choice(ruleta_valores)
        limpiar_pantalla()
        print(f"--> {ruleta} <--")
        time.sleep(0.1)
    resultado_final = random.choice(ruleta_valores)
    limpiar_pantalla()
    print(f"Resultado final: --> {resultado_final} <--")
    return resultado_final

# juego principal
while "_" in pista:
    jugador = usuarios[turno % 3]
    print(f"{jugador['nombre']}, es tu turno, tienes {jugador['puntos']} puntos")


    #ruleta ,opcion y posibilidades
    girar = input("¿Quieres girar la ruleta? (s/n): ")
    if girar.lower() != "s":
        turno = (turno + 1) % 3
        continue
    ruleta = girar_ruleta()
    if ruleta == "Pierde turno":
        print("¡Pierdes el turno!")
        turno = (turno + 1) % 3
        continue
    elif ruleta == "Quiebra":
        print("¡Quiebra! Pierdes todos tus puntos.")
        jugador["puntos"] = 0
        turno = (turno + 1) % 3
        continue
    print("Progreso de la palabra:", " ".join(pista))
    print(f'letras usadas : {letras_usadas}')

    #letra 
    letra = input("Dime una letra (sin vocales): ").lower()
    while len(letra) > 1:
        letra = input("Por favor, ingresa solo una letra.")
        continue
    if letra == "":
        print("no has introducido nada : ")
        turno = (turno + 1 )%3
        continue

    if letra in "aeiou":
        print("No puedes usar vocales en esta fase.")
        turno = (turno + 1 )%3
        continue       
    if letra in letras_usadas:
        print("Esta letra ya fue usada.")
        turno = (turno + 1 )%3
        continue
    letras_usadas.append(letra)
    
    # Verificar si la letra está en la palabra
    if letra in palabra:
        print(f"¡La letra '{letra}' está en la palabra!")
        # si acierta puede rusolver la frase, 
        opcion = input("¿Deseas resolver la palabra entera (r) o comprar vocal (c) o resolver pistas (p)?: ").lower()
        if opcion == "r":
            resolucion = input("Escribe la palabra completa: ").lower()
            if resolucion == palabra:
                jugador['puntos'] += 5000
                print(f"¡Felicidades {jugador['nombre']}! Has resuelto la palabra y ganado {jugador['puntos']} puntos.")
                break
            else:
                print("La resolución no es correcta.")
                turno = (turno + 1) % 3
                continue
        #opcion de comprar vocal                
        elif opcion == "c":                
            if jugador["puntos"] >= 150:
                jugador["puntos"] -= 150
                vocal = input("¿Qué vocal quieres comprar?: ").lower()
                while len(vocal) > 1:
                    vocal = input("no puedes introducirte mas que una letra : ")

                if vocal in "aeiou" and vocal in palabra:
                    veces_vocal = palabra.count(vocal)
                    for i in range(len(palabra)):
                        if palabra[i] == vocal:
                            pista[i] = vocal
                    jugador["puntos"] += ruleta * veces_vocal
                    print(f"has conseguido {(ruleta * veces_vocal)-150} puntos ")

                else:
                    print("La vocal no está en la palabra o ya ha sido descubierta.")
            else:
                print("No tienes suficientes puntos para comprar una vocal.")
                turno = (turno + 1) % 3
                continue
        
        elif opcion == 'p':
            
            resuelve_pista = input("Dime una letra que no sea vocal : ").lower()
            while len(resuelve_pista) > 1:
                resuelve_pista = input("no puedes introducirte mas que una letra : ")

            if resuelve_pista in 'aeiou':
                print('has introducido vocal, paso de turno')
                turno = (turno+1)%3
                continue
            elif resuelve_pista in palabra:
                veces_letra = palabra.count(resuelve_pista)
                for i in range(len(palabra)):
                    if palabra[i] == resuelve_pista:
                        pista[i] = resuelve_pista
                print(f"has conseguido {(ruleta * veces_letra)} puntos ")
                jugador["puntos"] += ruleta * veces_letra
 
    else:
        print("La letra no está en la palabra. Cambio de turno.")
        turno = (turno + 1) % 3
        continue


print("Juego terminado.")
