'''
Created on 3 jun 2022

@author: vicen
'''

frase=input('Dime una frase')

VALOR=4
cuatroUltimas=len(frase)-VALOR;
resultadoFinal=""

def fraseChachi (frase):
    
    cuatroPrimeras=""
    resultado=""
    contador=0;
    
    for  i in frase:
        contador+=1
        if contador <=VALOR:
            cuatroPrimeras+=i
            
        if contador>cuatroUltimas:
            resultado+=i
    
    if  cuatroPrimeras==resultado:
        resultadoFinal='Es chachi'
    else:
        resultadoFinal='No es chachi'

    return resultadoFinal


print(fraseChachi(frase))
        