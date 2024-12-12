n1 :int= int(input("dime un numero "))
n2 :int= int(input("dime otro numero "))
n3 :int= int(input("dime el ultimo numero "))


if n1>n2>n3 :
    print([n1,n2,n3])
elif n2>n1>n3 :
    print([n2,n1,n3])
elif n3>n1>n2 :
    print([n3,n1,n2])
elif n2>n3>n1 :
    print([n2,n3,n1])
elif n3>n2>n1 :
    print([n3,n2,n1])