import sys
print(sys.argv) #lista lee lo que introduce antes 

for i in sys.argv: #imprime por primera 
    print(i)

for j in range (1,len(sys.argv)): # imprime otra vez
    print(sys.argv[j])