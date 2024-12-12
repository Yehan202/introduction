# vocal a,e,i,o,u

letra :str =str(input("dime una letra : "))

while letra != " " :
    if letra in "aeiou" :
        print ("vocal") 

    else :
        print ("no vocal")
        
    letra :str =str(input("dime una letra : "))
print("salir ")
        
