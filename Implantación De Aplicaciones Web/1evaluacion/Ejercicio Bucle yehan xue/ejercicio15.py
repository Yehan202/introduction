pago =10
total_pago =0
for mes in range(1,21) :
    total_pago += pago
    pago *= 2
    
print(pago)