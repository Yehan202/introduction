import sys

# Listas para almacenar los datos
usuario = []
group = []
memoria = []

# Parsear los argumentos de la línea de comandos
for i in range(1, len(sys.argv)):
    if sys.argv[i] == '-u' and i + 3 < len(sys.argv):
        usuario.append(sys.argv[i + 1])
        group.append(sys.argv[i + 2])
        memoria.append(sys.argv[i + 3])  # Convertir memoria a entero para cálculos

# Mostrar detalles de los usuarios si se especifica '-user'
if '-user' in sys.argv:
    for j in range(len(usuario)):
        print(f"Usuario: {usuario[j]} en Grupo: {group[j]} tiene Memoria: {memoria[j]} MB")

# Mostrar todos los usuarios agrupados por cada grupo si se especifica '-group'
if '-group' in sys.argv:
    # Obtener grupos únicos
    group_sin_repetir = []
    for g in group:
        if g not in group_sin_repetir:
            group_sin_repetir.append(g)
    
    # Imprimir los usuarios por grupo
    for grupo in group_sin_repetir:
        print(f"\nEn el grupo {grupo} están:")
        for k in range(len(usuario)):
            if group[k] == grupo:
                print(f" - Usuario: {usuario[k]}, Memoria: {memoria[k]} MB")
