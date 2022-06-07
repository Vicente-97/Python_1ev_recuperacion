'''
Created on 4 jun 2022

@author: vicen
'''

cadena=input("Introduce la cadena a cifrar")
numeroASumar=int(input("Introduce el numero"))




def cifrasoAsci(cadena, numeroASumar):
    cadenaNueva=""
    
    for i in range (0, len(cadena)):
        ascii=numeroASumar+ord(cadena[i])
        while ascii>90:
            ascii=ascii-25
        cadenaNueva=cadenaNueva+chr(ascii)

    print(cadenaNueva)
    return cadenaNueva

print(cifrasoAsci(cadena, numeroASumar))




