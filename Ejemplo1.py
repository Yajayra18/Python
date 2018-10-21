#Ejemplo práctico
men = 'tengo sueño' #cadena de texto
nom = ['J', 'K', 'C', 2, 4] #Array
#Cantidad de elementos
print(len(men))
print(len(nom))
n = len(men) # 11
m = len(nom) # 5 

# rmen = range(n) # range(0,11) en realidad es =[0,1,2,3,4,5,...,10]
# rnom = range(m) # range(0,5) en realidad es =[0,1,2,3,4]

rmen = range(0,n,3)

print (rmen)

for gatito in rmen:
    print(gatito,men[gatito])




