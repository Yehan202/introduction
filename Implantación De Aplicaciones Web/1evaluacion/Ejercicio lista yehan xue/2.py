import random
import time
import os

# Valores de la ruleta
ruleta_valores = [100, 200, 300, 400, 500, 600, 700, 800, 900, "Pierde turno", "Quiebra"]

# Palabras y selección aleatoria
palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jóse come Coco", "Estás en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras)
pista = ["_" if palabra[i] != " " else " " for i in range(len(palabra))]

# Jugadores y puntos
usuarios = []
for i in range(3):
    usuario = input(f"Dime el nombre del usuario {i + 1}: ")
    usuarios.append({"nombre": usuario, "puntos": 0})
turno = 0  # Índice del jugador actual
letras_usadas = []

# Limpiar pantalla
def limpiar_pantalla():
    if os.name == 'nt':
        os.system('cls')
# Girar ruleta con animación
def girar_ruleta():
    print("¡Girando la ruleta!")
    for _ in range(20):
        resultado = random.choice(ruleta_valores)
        limpiar_pantalla()
        print(f"--> {resultado} <--")
        time.sleep(0.5)
    resultado_final = random.choice(ruleta_valores)
    limpiar_pantalla()
    print(f"Resultado final: --> {resultado_final} <--")
    return resultado_final

# Juego principal
while "_" in pista:
    jugador_actual = usuarios[turno]
    print(f"\n{jugador_actual['nombre']}, es tu turno")
    print(f"Puntos actuales: {jugador_actual['puntos']}")
    print("Progreso de la palabra:", " ".join(pista))
    print("Letras usadas:", ", ".join(letras_usadas))

    # Girar la ruleta
    resultado = girar_ruleta()

    # Condiciones de la ruleta
    if resultado == "Pierde turno":
        print("¡Pierdes el turno!")
        turno = (turno + 1) % 3
        continue
    elif resultado == "Quiebra":
        print("¡Quiebra! Pierdes todos tus puntos.")
        jugador_actual["puntos"] = 0
        turno = (turno + 1) % 3
        continue

    # Entrada de letra
    letra = input("Dime una letra (si aciertas, ganas los puntos de la ruleta): ").lower()
    
    # Verificación de letra usada
    if letra in letras_usadas:
        print("Esa letra ya fue usada, elige otra.")
        continue
    letras_usadas.append(letra)

    # Verificación de compra de vocal
    if letra in "aeiou":
        compra = input("¿Quieres comprar esta vocal por 150 puntos? (si o no): ").lower()
        if compra == "si":
            if jugador_actual["puntos"] >= 150:
                jugador_actual["puntos"] -= 150
                print(f"Has comprado la vocal '{letra}'.")
            else:
                print("No tienes suficientes puntos para comprar la vocal.")
                continue

    # Comprobación de letra en palabra
    if letra in palabra.lower():
        print(f"¡Has acertado la letra '{letra}'!")
        for i in range(len(palabra)):
            if palabra[i].lower() == letra:
                pista[i] = palabra[i]
        jugador_actual["puntos"] += resultado if isinstance(resultado, int) else 0
    else:
        print(f"La letra '{letra}' no está en la palabra.")
    
    # Cambio de turno
    turno = (turno + 1) % 3

# Fin del juego y anuncio del ganador
print("\n¡Felicidades! Se ha completado la palabra:")
ganador = max(usuarios, key=lambda x: x["puntos"])
print(f"El ganador es {ganador['nombre']} con {ganador['puntos']} puntos.")
