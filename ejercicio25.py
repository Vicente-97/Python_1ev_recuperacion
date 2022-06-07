'''
Created on 6 jun 2022

@author: vicen
'''



nombresAlumno=[]
edades=[]
nuevaLista=[]
edadMayor=0
listaMayorEdad=[]

nombre=input("Introduzca el nombre")



while nombre!='*':
    nombresAlumno.append(nombre)
    edad=int(input("Introduzca la edad"))
    edades.append(edad)
    nombre=input("Introduzca el nombre")
   
for i in range (0, len(edades)):
    if edades[i]>=18:
        nuevaLista.append(nombresAlumno[i])
        
for j in range (0, 5):
    for h in range (0, len(edades)):
        if edades[h]>edadMayor:
            edadMayor=edades[h]

listaMayorEdad.append(edadMayor)
           
        
print('Esta es la lista de alumnos mayores de edad {}, y esta es la lista de los alumnos con más edad {}'.format(nuevaLista, listaMayorEdad ))
        
    
 