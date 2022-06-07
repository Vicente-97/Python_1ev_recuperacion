'''
Created on 3 jun 2022

@author: vicen
'''



def codificar(cadena, clave):
    resultado=""
    
    for i in range(0, len(cadena)):
        numero=int(cadena[i])
        for j in range (0,len(clave)):
            if numero ==j:
                resultado=resultado+clave[j]
                
    return resultado
    
    
def descodificar (cadena, clave):
    resultado=""
    
    for i in range (0, len(cadena)):
        numero=int(cadena[i])
        for j in range (0, len(clave)):
            if numero==int(clave[j]):
                resultado=resultado+str(j)
                
    return resultado



print(codificar("2380", "3651829470"))
print(descodificar("8968", "3651829470"))