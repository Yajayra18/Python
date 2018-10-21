
#Listas
# Pueden contener  enteros/boleanos/ listas
x = [2, "tres", True, ["uno",10]]
#"tres" es un elemento 2 pero con ìndice 1

x2 = x [1]

print (x2)


#acceder a un elemento de una lista que 
#está dentro de otra lista 

x3 = x [3][0]
print (x3)

#
x[1] = 4
x2 = x[1]

print (x2)

# se va aconsiderar los indices que quiero contadar
# desde el 0, considerar 3 elementos

x4 = x[0:3]
print (x4)

#Salto
x5 = x[0:3:2]

print (x5)

#lo siguiente se usará para presentar elementos
#intercalados
x6 = x[1::2]
print (x6)
# reemplazar elementos

x[0:2] = [4,3]
print (x) 
# tambièn puede reemplazar a 2 elementos

x[0:2] = [5]
print (x)

# tambièn se puede ver el elemento del final
y = x[-1]
print (y)