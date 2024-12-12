ahorro_total : float = 0
ahorro_mensual : float = 0
mes = 0
while mes != 12 :
    deposito = float(input("cuantos dineros vas a depositar en este mes ? "))
    mes += 1
    ahorro_total += deposito
    ahorro_mensual = deposito
    print (f"el ahorro de mes {mes} es {ahorro_mensual}")
print(f"ahorro total {ahorro_total} ahorromesual")    
    
