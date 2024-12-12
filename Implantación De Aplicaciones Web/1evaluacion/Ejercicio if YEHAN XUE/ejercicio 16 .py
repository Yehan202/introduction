tiempo : float = float(input("cuando duro la llamada :"))
dia : int = int(input("que dia llamaste (1-7) :"))
turno : str = str(input("por la mañana o por la tarde :"))
impuesto = 0
coste = 0

if tiempo <= 5 :
    coste = 1*tiempo
elif tiempo <= 8:
    coste = 5+(tiempo-5)*0.8
elif tiempo <= 10:
    coste = 5+3*0.8+(tiempo-8)*0.7
else:
    coste=5+3*0.8+2*0.7+(tiempo-10)*0.5

if dia == 7:
    impuesto= coste*0.03
else:
    if turno == "mañana" :
        impuesto = coste*0.15
    elif turno == "tarde" :
        impuesto = coste*0.1
    else :
        print("error") 
        
print(f"coste base es {coste} euros ")
print(f"impuesto es {impuesto} euros ")
print(f"total es {coste + impuesto}")
