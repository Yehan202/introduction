import random

palabras = ["Pepe come la Manzana", "Carlos tiene una Pera", "Jóse come Coco", "Estás en Madrid", "Vas a irte a Barcelona", "Viaje hacia London"]
palabra = random.choice(palabras)
pista = ["_" 
         if palabra[i] != " " 
         else " " 
         for i in range(len(palabra))]

acentos = {"a":"á" , "e":"é" , "i": "í", "o":"ó" , "u":"ú" }
fallos = 0
max_fallos = 7
letra_usada = []


while fallos < max_fallos:
    print("".join(pista))
    letra = input("Dime una letra: ").lower()


    while len(letra) > 1:
        print("solo puedes introducirte una sola letra")
        letra = input("Dime una letra: ").lower()
       
 
    while letra in letra_usada :
        print(f"ya has introducido esta letra '{letra}' introduce otra letra")
        letra = input("Dime una letra: ").lower()
    letra_usada.append(letra)
    

    letra_comparable = acentos.get(letra, letra)
    
    if letra in palabra.lower():
        print(f'Has acertado la letra {letra}')
        for i in range(len(palabra)):
            if palabra[i].lower() == letra:
                pista[i] = palabra[i]

     
    else:
        fallos += 1
        print(f"Fallaste. La letra '{letra}' no está en la palabra. Te quedan {max_fallos - fallos} fallos.")
    
    if fallos == 1:
        print("""
        +--+
        O  |
           |
           |
           |
           |
    =========
        """)
    elif fallos == 2:
        print("""
        +--+
        O  |
        |  |
           |
           |
           |
    =========
        """)
    elif fallos == 3:
        print("""
        +--+
        O  |
       \\|  |
           |
           |
           |
    =========
        """)
    elif fallos == 4:
        print("""
        +--+
        O  |
       \\|/ |
           |
           |
           |
    =========
        """)
    elif fallos == 5:
        print("""
        +--+
        O  |
       \\|/ |
        |  |
           |
           |
    =========
        """)
    elif fallos == 6:
        print("""
        +--+
        O  |
       \\|/ |
        |  |
       /   |
           |
    =========
        """)
    elif fallos == 7:
        print("""
        +--+
        O  |
       \\|/ |
        |  |
       / \\ |
           |
    =========
        """)
        break

    if "_" not in pista:
        print(f"¡Felicidades! Has adivinado la palabra: {palabra}")
        break

else:
    print(f"Lo siento, has perdido. La palabra era '{palabra}'.")
