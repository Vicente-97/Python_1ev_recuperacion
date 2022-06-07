'''
Created on 4 jun 2022

@author: vicen
'''
cadena=input("Introduce la cadena")

def valorCadena(cadena):
    suma=0
    for i in range (0, len(cadena)):
        numero=ord(cadena[i])
        suma+=numero
    return 'El valor de {} es {}'.format(cadena, suma)


print(valorCadena(cadena))