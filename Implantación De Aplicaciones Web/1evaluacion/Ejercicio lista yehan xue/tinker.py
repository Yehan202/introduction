# tres usuario
# dame una letra si esta resuelve, gana punto , y girar otra vez
# pregunta si compra vocal o resuelve 

import random
import time
import os

# Valores de la ruleta
ruleta_valores = [100, 200, 300, 400, 500, 600, 700, 800, 900, "Pierde turno", "Quiebra"]

palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jóse come Coco", "Estás en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras)
pista = ["_" if palabra[i] != " " else " " for i in range(len(palabra))]

letras_usadas = []
resuelve_usada = []
usuarios = []
for i in range(3):
    usuario = input(f"Dime el nombre del usuario {i + 1}: ")
    usuarios.append({"nombre": usuario, "puntos": 0})
turno = 0

def limpiar_pantalla():
    if os.name == 'nt':  # Si es Windows
        os.system('cls')

def girar_ruleta():
    print("¡Girando la ruleta!")
    for _ in range(20):  # Simular múltiples vueltas
        ruleta = random.choice(ruleta_valores)
        limpiar_pantalla()  # Limpiar pantalla en cada iteración
        print(f"--> {ruleta} <--")  # Mostrar valor temporal
        time.sleep(0.1)  # Pausa breve para animación

    # Resultado final
    resultado_final = random.choice(ruleta_valores)
    limpiar_pantalla()
    print(f"Resultado final: --> {resultado_final} <--")
    return resultado_final


while "_" in pista:
    jugador = usuarios[turno % 3]
    print(f" {jugador["nombre"]}, es tu turno, tienes {jugador["puntos"] } puntos ")

    girar = input("quieres girar la ruleta(s)")
    if girar == "s":
        resultado_ruleta =  girar_ruleta()
        if resultado_ruleta == "Pierde turno":
            print("¡Pierdes el turno!")
            turno = (turno + 1) % 3
            resultado_ruleta = None  
            continue
        elif resultado_ruleta == "Quiebra":
            print("¡Quiebra! Pierdes todos tus puntos.")
            jugador["puntos"] = 0
            turno = (turno + 1) % 3
            resultado_ruleta = None  
            continue

    print("Progreso de la palabra:", " ".join(pista))
    print(f" {jugador["nombre" ]} tienes {jugador["puntos"]} puntos")

    
    letra = input("dime una letra (no vocal), si aciertas puedes hacer resolvere o compra vocal  : ")
    while len(letra) > 1 :
        letra = input("no puedes introducirte mas que un digito, por favor, introduce otro letra : ")
    if letra in "aeiou" :
        input("no puedes usar vocal en aqui ")
        turno = (turno + 1) % 3


    elif letra in palabra:
        opcion = input(f"la letra {letra} ha aparecido en la frase, puedes resolver o comprar vocal(r o c) : ")
        if opcion == "r":
            resuelve = input("dime una letra :")
            if resuelve in palabra:
                print(f"¡Has acertado la letra '{resuelve}'!")
                jugador["puntos"] += (resultado_ruleta * palabra.count(resuelve))
                for i in range(len(palabra)):
                    if palabra[i].lower() == resuelve:
                        pista[i] = palabra[i]
                

        if opcion == "c":
            if jugador["puntos"] > 150 :
                jugador["puntos"] -= 150 
                vocal = input("que vocal quieres compra : ")
                if vocal in palabra :
                    for i in range(len(palabra)):
                        if palabra[i].lower() == vocal:
                            pista[i] = palabra[i]
            else :
                print("no tienes suficiente para compra vocal ")
                continue
    else :
        print ("cambio de turno ")
        turno = (turno + 1) % 3


        