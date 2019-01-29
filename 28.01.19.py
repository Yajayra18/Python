#28.01.19

# VARIABLE
''' one variable have data modifiable. 

'''

you = "you are so special for me"

print (you)

#exist  constant data
# es decir que estos no son modificables, y estos son escritos en
# mayúscula


"""Tipos de Datos
this can be  string, int, float and boleano.
"""

v1 = "Hola mi amor \n ten un lindo día, eres grandioso"

v2 = 7

v3 = 0.02

v4 = True

print  (v1)

"""OPERACIONES ARITMETICAS
suma(+), resta (-), negación(-), multiplicación(*), exponente(**), 
división(/),división entera (//), módulo(%).
"""

j = 2
i = 5
h = 3
k = 9

print (j + i)
print (i - h)
print (j + i + h + k)
print (-j)
print (j * i)
print (h ** j)
print (k / h)
print (i // j)
print (i % h)

#Ejemplo con legislación laboral
""" Yajayra gana 1000 nuevos soles y realiza 5 horas extras
el lunes y 4 horas extras el jueves. Teniendo en cuenta
que las horas extras son remuneradas siendo las primeras
2 en un 25% más y a partir de la 3era hora un 35% más del 
pago por hora.
Cuanto recibiría yajayra a fin de mes? """

#Sueldo de Yajayra
sy = 1000
#días del mes
d = 30
#horas trabajadas al día
h = 6
#pago  regular por dia trabajado
p_d = sy / d

#pago regular por hora trabajada
p_h = p_d / h

print ("yajayra es remunerada por hora lo siguiente")
print (p_h)


# el pago por cada hora extra hasta la 2da es la siguiente
hx2 = p_h * 25 / 100 + p_h
print ("el pago por cada hora extra hasta la 2da es la siguiente")
print (hx2)

# el pago por cada hora extra de la 3era en adelante es la siguiente
hx3 = p_h * 35 / 100 + p_h
print ("l pago por cada hora extra de la 3era en adelante es la siguiente")
print (hx3)

#entonces Yajayra es remunerada a fin de mes de la siguiene 
#forma, considerando que tiene 5 y 4 hras extras
"""si lo deglosamos se tiene 4 hrs reconocidas +25% y 5 hras 
reconocidas con el 35% + """

sf = sy + 4 * hx2 + 5 * hx3

print ("entonces Yajayra recibe a fin de mes el siguiente sueldo")
print (sf)


# TIPO DE DATOS COMPLEJOS
""" son tipo de datos complejo por que en ellas se encuentran
una colección de datos.
Estas son Tuplas, Listas y Diccionarios."""

#tuplas
""" almacena datos que no pueden ser modificados una vez 
creados se caracteríza por usar parentesis"""

mi_tupla = ("te quiero", 7, 0.2, "dos mil dieciocho")
print (mi_tupla)

#se acceder a los datos mediante su índice
print (mi_tupla[0] + " Joseph")

