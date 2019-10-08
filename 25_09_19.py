#Hoy aprenderemos algunos términos importantes
#1. hola_mundo.py es un scrib
#cd me permite desplazarme entre carpetas
#ls es el comando que me muestra los archivos que estan dentro de la carpeta donde me encuentrocd
#si luego de un cd colocamos y el tab, este nos ayuda completar la plabra

#Iniciemos
#TUPLAS

lanche = ("Hamburguesa", "Refresco", "Pizza", "Budin")
#en lanche efisten 4 elementos y cada uno de ellos es un indice donde:
# Indice 1 : Hamburguesa/ Indice 2 : Refresco / Indice 3 : Pizza / Indice 4 : Budin

print (lanche [1:3])

print (lanche [-2])
print (lanche [0:2])
#en lo siguient c va a ser todos los elementos uno a uno
for c in lanche:
    print (c)

nouns = ("teacher", "student", "phone number", "friend","classmate")

print (nouns [3:5])
print (nouns [:3])

#Hay un hermoso truquito, este trata de lo siguiente:
#el entre los corchetes el primer numero es el índice y despues de los dos puntos el otro numero es
#el elemento. 


##PRACTICANDO##

#() [] {}
#() --- Tupla -- Estas son Inmutables - NO CAMBIAN
#[] --- Lista
#{} --- Diccionario

desayuno = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
print (desayuno [1])
#Rpta. Suco
print (desayuno [3])
#Rpta. Pudim
print (desayuno [1:3])
#Rpta. Suco, Pizza
#print (desayuno [2:])
#Rpta. Pizza, Pudim
#print (desayuno [:2])
#Rpta. Hamburguer, Suco
#print (desayuno[-3:])
#Rpta. Suco, Pizza, pudim
#print (desayuno [-3])
#Rpta. Suco

#Las Tuplas son inmutables
#desayuno [1] = 'Refrigerante'
#print(desayuno[1])

#TypeError: 'tuple' object does not support item assignment
print(len(desayuno))
#len cuenta la cantidad de elementos que hay en la tupla
breakfast = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

for comida in breakfast:
    print ('Yo voy a comer %s' %comida)
print ('Que delicia')

for cont in range (0, len(breakfast)):
    print(breakfast[cont])
