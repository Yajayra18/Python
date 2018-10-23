#Operadores Relacionales
a = 25
b = 24
# == significa igual
# hay mayor que menor que o mayor igual que o menos igual que
x = a == b
y = b <= a
 
print (x)
print (y)

z = a < b
w = b > a

print (z)
print (w)

# != significa diferente

t = a != b
print (t)

#La cadena de texto tambié puede ser 
#operadores relacionales
q = "Hola soy Yajayra"
s = "Hola hoy es 22.10.2018"

print (q==s)
d = ["one", "two", 3]
f = ["one"]

print (d >= f)

# Sentencias Condicionales
if (q != s):
	print (" se imprimirá")
else: ("no imprimirá")