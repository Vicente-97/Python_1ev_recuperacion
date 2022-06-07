'''
Created on 3 jun 2022

@author: vicen
'''

segundos=int(input("Indica el numero de segundos"))
horas=0
minutos=segundos//60
segundos-=minutos*60

while minutos>=60:
    horas+=1
    minutos=minutos-60

    

print(horas,'Horas', minutos, 'Minutos', segundos,'Segundos')