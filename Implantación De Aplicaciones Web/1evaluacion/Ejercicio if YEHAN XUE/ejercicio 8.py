nota:int = int(input("dime la nota que tiene "))
edad:int = int(input("dime el edad que tiene "))
sexo:str = str(input("dime el sexo "))

if nota >= 5 and edad >= 18 and sexo == "F":
  print ("aceptada")
elif  nota >= 5 and edad >= 18 and sexo == "M":
  print("Posible")
else :
  print("no aceptada")