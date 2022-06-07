'''
Created on 5 jun 2022

@author: vicen
'''
from random import randint
vector=[]
for i in range (0,10):
    numero=randint(0, 100)
    vector.append(numero)
    
print(vector)

esVerda=True
while esVerda:
    esVerda=False
    for i in range (0, len(vector)-1):
        if vector[i]>vector[i+1]:
            
            vector[i],vector[i+1]=vector[i+1],vector[i]
            
            esVerda=True
    
        

print(vector)

        

