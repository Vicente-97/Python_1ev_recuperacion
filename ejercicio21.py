'''
Created on 4 jun 2022

@author: vicen
'''
vector=[]

numero=int(input("Introduce un numero"))
for i in range (0,10):
    if numero>0:
        vector.append(numero)
        numero=int(input("Introduce un numero"))

print(vector)
    