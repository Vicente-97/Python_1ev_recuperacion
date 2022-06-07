'''
Created on 4 jun 2022

@author: vicen
'''

vector_cadena=[]
vector_inverso=[]
cadena=""

for i in range (0,5):
    cadena=input("Introduzca la cadena")
    vector_cadena.append(cadena)

for j in range (len(vector_cadena)-1,-1,-1):
    vector_inverso.append(vector_cadena[j])

print('Este es el vector inicial {}, y este es el vector con los elementos en orden inverso {}'.format(vector_cadena, vector_inverso))