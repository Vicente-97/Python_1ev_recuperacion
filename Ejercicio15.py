'''
Created on 4 jun 2022

@author: vicen
'''

cadena=input("Introduce la cadena")
caracter=(input("INTRODUCER EL CARACTER"))

def numeroCaracteres(cadena, caracter):
    contador=0
    for i in range (0, len(cadena)):
        if caracter==cadena[i]:
            contador+=1
    return contador


print(numeroCaracteres(cadena, caracter))