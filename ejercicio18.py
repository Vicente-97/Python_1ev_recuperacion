'''
Created on 4 jun 2022

@author: vicen
'''
from random import random, randint
vector_enteros=[]

for i in range (0,10):
    vector_enteros.append(randint(1, 10))
for j in range (0, len(vector_enteros)):
    cuadrado=vector_enteros[j]*vector_enteros[j]
    cubo=vector_enteros[j]*vector_enteros[j]*vector_enteros[j]
    print('El vector de numeros es {}, y su cuadrado es {}, su valor al cubo corresponde a {}'.format(vector_enteros[j], cuadrado, cubo))