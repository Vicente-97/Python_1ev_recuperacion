'''
Created on 4 jun 2022

@author: vicen
'''
'''17.- Los preprocesadores de los lenguajes de programación como Java o C eliminan del código
fuente los comentarios (/* ....*/) antes de compilarlo. Diseña un método que reciba una sentencia
en Java y devuelva una cadena eliminando los comentarios'''


cadena=input("Introduce una sentencia en Java")

def eliminarComentarios(cadena):
    resultado=""
    encontrado=False
    for i in range(0, len(cadena)):
        if i!=len(cadena)-1:
            if cadena[i]=="/" and cadena[i+1]=="*":
                encontrado=True
            
            if encontrado==False and cadena[i]!="/" and cadena[i]!="*":
                resultado+=cadena[i]
    
            if cadena[i]=="*" and cadena[i+1]=="/":
                encontrado=False
        elif cadena[i]!="*" and cadena[i]!="/":
            resultado+=cadena[i]
    
    return resultado

print(eliminarComentarios(cadena))

