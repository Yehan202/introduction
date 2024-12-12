empate = 0
ganado = 0

for i in range(3):
    for j in range(3):
        for k in range(3):
            if (i == j and i == k) or (i != j and i != k and j != k):
                empate += 1
            else:
                ganado += 1
                
print(f"Se han realizado las 27 combinaciones de las cuales {empate} han sido empate y {ganado} uno de los jugadores gana")