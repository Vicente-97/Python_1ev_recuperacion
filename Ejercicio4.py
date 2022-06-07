'''
Created on 3 jun 2022

@author: vicen
'''


numero = int(input("Introduce un numero : "))

media =0
maximo=0
minimo=numero
contador=0;
suma=0

while numero>0:
    if numero>maximo:
        maximo=numero
    if numero<minimo:
        minimo=numero
        
    
    if numero>0:
        suma+=numero
        contador+=1;
        
    media= suma/contador;  
    numero=int(input('Introduce un numero'))


print('La media es ', media, 'El numero maximo es ', maximo, 'El numero minimo es ', minimo)