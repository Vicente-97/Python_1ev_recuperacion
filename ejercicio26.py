'''
Created on 6 jun 2022

@author: vicen
'''
temperaturaMedia=[]
temperaturaMax=[]
temperaturaMin=[]
listaMinimasTemp=[]
contador=0
temperaturaMenor=9999
contadorDiasIgual=0

for i in range (0,5):
    temperaturaMaxima=int(input("Introduce la temperatura maxima"))
    temperaturaMax.append(temperaturaMaxima)
    temperaturaMinima=int(input("Introduce la temperatura minima"))
    temperaturaMin.append(temperaturaMinima)
    temperaturaMedia.append((temperaturaMax[contador]+temperaturaMin[contador])/2)
    contador+=1

tempTeclado=int(input("Introduce un numero de temperatura, se indicara los días que tienen dicha temperatura"))
for i in range (0, len(temperaturaMax)):
    if temperaturaMax[i]==tempTeclado:
        contadorDiasIgual+=1
if contadorDiasIgual>0:
    print('Hay un total de {} días que coinciden con su temperatura'.format(contadorDiasIgual))
else:
    print("Error no hay días que coincidan con esa temperatura")


for i in range (0,len(temperaturaMin)):
        if temperaturaMin[i]<temperaturaMenor:
            temperaturaMenor=temperaturaMin[i]


print('Es la lista de temperaturas máxima que usted ha indicado {}'.format(temperaturaMax))
print('Es la lista de temperaturas mínima que usted ha indicado {}'.format(temperaturaMin))
print('Es la lista de temperaturas mínima que usted ha indicado {}'.format(temperaturaMedia))
print('Es la temperatura menor de los 5 días es:  {}, grados'.format(temperaturaMenor))

