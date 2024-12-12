letra:str = str(input("introduce una letra "))

if letra.isupper():
    print(f" es mayuscula ")
elif letra.isnumeric() :
    print(f" es un numero ")
else :
    print(f" es minuscula ")