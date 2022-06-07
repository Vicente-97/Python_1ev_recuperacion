'''
Created on 4 jun 2022

@author: vicen
'''

cadena=input("Introduce la cadena para ver si es palindroma")

def esPalindroma (cadena):
    cadena2=""
    cadena1=""
    resultado=""
    cadenaMayus=cadena.upper()
    for i in range (0,len(cadenaMayus)):
        cadena1 +=cadenaMayus[i]
    for j in range (len(cadenaMayus)-1,-1,-1):
        cadena2+=cadenaMayus[j]
    if cadena1==cadena2:
        resultado+="Es palindroma"
    else:
        resultado+="No es palidroma"
        
    return resultado


print(esPalindroma(cadena))