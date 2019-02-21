"""ESTRUCTURAS DE CONTROL INTERACTIVAS
Blucles, nos permite ejecutar el mismo código de manera
repetitiva, mientras cumpla la condición.
"""

#BUCLE while
""" ejecuta la misma acción, mientras se cumpla
la condición puesta.
Condición:
pndré el año que nacimos 1993 e imprimirá hasta este año
"""
anio = 1993
while anio <= 2019:
	print ("Año de Vida", str(anio))
	anio += 1

#notita anio +=1 es equivalente a anio + 1 = anio


#Ejemplo
gatos = 1
while gatos <= 7:
	print ("comprenos un gato más,total tenemos ", str(gatos))
	gatos += 1