'''
Created on 6 jun 2022

@author: vicen
'''
from random import randint


vector1=[]
vector2=[]
vector3=[]
contador=0


for i in range (0, 5):
    numero=int(input("Introduce el numero para el vector 1"))
    vector1.append(numero)
    
for i in range (0, 5):
    numero=int(input("Introduce el numero vector 2"))
    vector2.append(numero)
    

    
for i in range(0, len(vector1)): 
    vector3.append(vector1[contador]+vector2[contador])
    contador+=1

   

print('Este es el vector 1 {}, Este es el vector 2 {}, y este es el vector3, {}'.format(vector1, vector2, vector3 ))


   
