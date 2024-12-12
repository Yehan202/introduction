suma = 0.0
signo = 1 
for i in range(100):
   denominador = 2 * i + 1  # 1, 3, 5, 7, 9, ...
   suma += signo * (4 / denominador)
   signo *= -1  # Alterna + y -
print (suma)