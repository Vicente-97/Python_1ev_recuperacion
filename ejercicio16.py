'''
Created on 4 jun 2022

@author: vicen
'''

cadena=input("Introduce una cadena")

def sumarDigitosCadena (cadena):
    suma=0
    for i in range (0, len(cadena)):
        if ord(cadena[i])>=48 and ord(cadena[i])<=57:
            suma+=int(cadena[i])
    return suma

print(sumarDigitosCadena(cadena))