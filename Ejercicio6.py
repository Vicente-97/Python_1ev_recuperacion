'''
Created on 3 jun 2022

@author: vicen
'''

numero=int(input("Escribe un numero: "))

resultado=0;

primos=[];

for i in range (2, numero+1):
    while numero%i==0:
        primos.append(i)
        numero=numero/i
        
print (primos,'Es el resultado')
    