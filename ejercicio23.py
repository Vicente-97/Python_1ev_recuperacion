'''
Created on 5 jun 2022

@author: vicen
'''
vector_meses=['Enero','Febrero','Marzo','Abril', 'Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']

vector_dias=['31','28','31','30','31','30','31','31','30','31','30','31']

usuario=int(input("Introduce un numero para conocer el mes al que corresponde y su numero de días: "))

mes=""
dias="";
for i in range(0, len(vector_meses)):
    if i+1==usuario:
        mes+=vector_meses[i]
   
        
for j in range(0, len(vector_dias)):
    if j+1==usuario:
        dias+=vector_dias[j] 
    

print(mes, dias)

