'''
Created on 3 jun 2022

@author: vicen
'''
acumulador=0


numero=int(input('Introduce un numero'))
while numero>0:
    for i in range (0,numero+1):
        if numero>0:
            acumulador+=i;
    numero=int(input('Introduce un numero'))
    
print(acumulador, 'es la suma de los numeros introducidos')


