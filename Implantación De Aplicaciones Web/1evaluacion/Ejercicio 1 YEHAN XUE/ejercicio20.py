euro = int (input("cuantos euros tienes "))
cent = int (input("cuantos centimos tienes "))
dinero =int(euro*100+cent)


euro2 = int(dinero/200)
euro1 = int(dinero/100)

cent50 = int(dinero/50)
cent20 = int(dinero/20)
cent10 = int(dinero/10)

print(f"tengo {euro2} de 2 euro o tengo {euro1} de 1 euro o {cent50} de 50 centimo o{cent20} de 20 centimo o {cent10} de 10 centimo")