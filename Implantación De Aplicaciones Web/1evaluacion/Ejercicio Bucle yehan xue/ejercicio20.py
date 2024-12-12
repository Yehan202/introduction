# Pedir al usuario cuántos números primos quiere mostrar
n = int(input("¿Cuántos números primos quieres mostrar?: "))

contador = 0  # Para contar cuántos primos hemos encontrado
numero = 2  # El primer número a verificar si es primo

# Bucle para encontrar y mostrar los primeros N números primos
while contador < n:
    es_primo = True  # Suponemos que el número es primo

    # Verificamos si el número tiene divisores aparte de 1 y él mismo
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break

    # Si es primo, lo mostramos y aumentamos el contador de primos encontrados
    if es_primo:
        print(numero, end=" ")
        contador += 1

    # Pasamos al siguiente número
    numero += 1

print()  # Para dejar un salto de línea al final
