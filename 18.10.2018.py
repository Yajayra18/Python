#Tema Tuplas
# Las tuplas son muy similares a las listas
#recordar que si los elementos tienen corchetes
#es una lista pero si los elementos no están en 
#corchetes entonces es una tupla
t = 1,True,"Hola mi amor"
print (t)

t = (3,"hola",False)
print (type(t))

print (t[1])

#la tupla es de una dimención fija
# a la lista se le puede agregar más elemntos
#pero a la tupla no se le puede agregar más elemntos
#No puedo modificar los elementos de una tupla

#intentaremos modificar asignar un valor nuevo a un elemento
t[0] = "Hola"
#no se puede por que es una tupla

#Tema Diccionaros
#no tienen índice sino una clave

d = {'Clave1':[1,2,3],
	 4: True
}
print (d['Clave1'])
#se les conoce como matricies asociativas
#Ojo en la
d[4] = "Hola"
print (d[4])

#las listas y tublas son secuencias
#por tanto no es psible hacer Slaisi

print (d[0:2])
