'''
Created on 3 jun 2022

@author: vicen
'''

entradasGeneral=8

entradasMiercoles=5

entradaPareja=11

tarjetaCine=0.1

precioTotal=0

diaSemana=input("Introduce el dia de la semana: L=Lunes, M= martes, X= Miercoles, J= Jueves V= Viernes = S=sabado D=Domingo");
numeroPersonas=int(input("Introduce el numero de personas: "));
tieneTarjeta=input("Dispone de tarjeta Cine Jacaranda?: S=SI, N=No");

if diaSemana=='L' or diaSemana=='M' or diaSemana=='V' or diaSemana=='S' or diaSemana=='D':
    if tieneTarjeta=='S':
        precioTotal=(entradasGeneral*numeroPersonas)-((entradasGeneral*numeroPersonas)*tarjetaCine)
    elif tieneTarjeta=='N':
        precioTotal=(entradasGeneral*numeroPersonas)

if diaSemana=='X':
    if tieneTarjeta=='S':
        precioTotal=(entradasMiercoles*numeroPersonas)-((entradasMiercoles*numeroPersonas)*tarjetaCine)
    elif tieneTarjeta=='N':
        precioTotal=(entradasMiercoles*numeroPersonas)

if diaSemana=='J':
    if numeroPersonas%2==0 and tieneTarjeta=='N':
        precioTotal=(entradaPareja*(numeroPersonas/2))
        
    elif numeroPersonas%2==0 and tieneTarjeta=='S':
        precioTotal=(entradaPareja*(numeroPersonas/2))-(entradaPareja*(numeroPersonas/2))*tarjetaCine
    
    if numeroPersonas%2!=0 and tieneTarjeta=='N':
        precioTotal=(entradaPareja*((numeroPersonas-1)/2))+entradasGeneral
        
    elif numeroPersonas%2!=0 and tieneTarjeta=='S':
        precioTotal=((entradaPareja*((numeroPersonas-1)/2))+entradasGeneral)-((entradaPareja*((numeroPersonas-1)/2))+entradasGeneral)*tarjetaCine
        
print(precioTotal,'Es el precio Total de sus Entradas. Disfrute del Cine Jacaranda.');