'''
Created on 3 jun 2022

@author: vicen
'''

numero=int(input("Escribe un numero para pasarlo a binario: "))

binario=[]

while numero>=1:
    binario.insert(0,numero%2)
    numero=numero//2

print(' El numero en binario es: ', binario)
    
    
    



    
    
