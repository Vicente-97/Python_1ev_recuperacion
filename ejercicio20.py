'''
Created on 4 jun 2022

@author: vicen
'''
notas=[]
notaMedia=0
notaMaxima=0
notaMinima=9999
contador=0

suma=0

for i in range (0,5):
    calificacion=int(input("Introduce tu calificacion final : "))
    notas.append(calificacion)
    
    
for i in range (0, len(notas)):
    contador+=1
    
    suma=suma+notas[i]
    
    if notas[i]>notaMaxima:
        notaMaxima=notas[i]
    if notas[i]<notaMinima:
        notaMinima=notas[i]
    notaMedia=suma/contador
    
print('Las notas son {}, La nota Maxima ha sido de {}, La nota Minima ha sido de {}, Y la media de sus notas ha sido de {}'.format(notas, notaMaxima, notaMinima, notaMedia))