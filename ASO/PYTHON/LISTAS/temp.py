import sys
temperatura_insertado=[]
temperatura_minimo="null"
temperatura_maximo="null"

for j in range(1,len(sys.argv)):
  if(sys.argv[j] == "-T") :
    temperatura_insertado.append(float(sys.argv[j+1]))
  if(sys.argv[j] == "-Tmin") :
    temperatura_minimo=float(sys.argv[j+1])
  if(sys.argv[j] == "-Tmax") :
    temperatura_maximo=float(sys.argv[j+1])

media=0.0
n=0
no_usado=[]

if temperatura_minimo=="null":
  temperatura_minimo=temperatura_insertado[0]
  for t in temperatura_insertado:
    if temperatura_minimo > t:
      temperatura_minimo=t

if temperatura_maximo=="null":
    temperatura_maximo=temperatura_insertado[0]
    for t in temperatura_insertado:
        if temperatura_maximo < t:
            temperatura_maximo=t

for t in temperatura_insertado:
  if t < temperatura_minimo or t > temperatura_maximo:
    no_usado.append(t)
  else:
    media+=t
    n+=1

print(media/n)
print(no_usado)