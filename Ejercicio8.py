'''
Created on 3 jun 2022

@author: vicen
'''
letras='ABCDEFGHIJKLMNÑOPQRSTUVWXYZ'
numero='123456789'

parteA=[]
parteB=[]

letrasCorrecta=False
numerosCorrecto=False

limiteCarac=int(input("Cuantos caracteres quieres incluir, (Minimo 2)"))
limiteNumero=int(input("Cuantos numeros quieres incluir, (Minimo 2)"))

while limiteCarac<=1:
    limiteCarac=int(input("Error, Cuantos caracteres quieres incluir, (Minimo 2)"))
    
    
for i in range (0,limiteCarac):
    caracteres=input("Introduce los caracteres correspondientes al numero de SS: ")
    parteA.append(caracteres.upper())
    for j in letras:
        if parteA==j:
            letrasCorrecta=True
        else:
            letrasCorrecta=False
                   
while limiteNumero<=1:        
    limiteNumero=int(input("Error, Cuantos numeros quieres incluir, (Minimo 2)"))
    
for i in range (0,limiteNumero):
    numeros=input("Introduce los numeros correspondientes al numero de SS: ")
    parteB.append(numeros)
    for j in  numero:
        if parteB==j:
            numerosCorrecto=True  
        else:
            numerosCorrecto=False
            
            
if numerosCorrecto==True and letrasCorrecta==True:
    print('Es Correcto')
