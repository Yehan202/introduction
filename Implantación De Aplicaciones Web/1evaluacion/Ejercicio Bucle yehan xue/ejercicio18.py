import time

segundos = 0
while True:
    horas = segundos // 3600 
    minutos = (segundos % 3600) // 60  
    segundos_restantes = segundos % 60    #los segundos esta sobre 60
    print(f"{horas:02}:{minutos:02}:{segundos_restantes:02}") 
    time.sleep(1)
    segundos += 1
    