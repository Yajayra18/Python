

x1 = ("te quiero", 7, 0.2, "dos mil dieciocho")
x2 = {0:"te quiero", 1:7, 3:"dos mil dieciocho", 2:0.2} 
print (x2.keys())
print (x2.values())
print (x2[0],x1[0])
print (x2[3],x1[3])


x3 = {True : "te quiero", "dia":7, "año":"dos mil dieciocho", "mes":0.2} 

print (x3[True])

"""entonces aprendí que se accede a la tupla, 
diccionario o lista usando corchetes y teniendo 
en cuenta que el primer número es el indice que deseo
que inicie y el después de los dos putos sigue el
indice final que deseo más uno"""

#Por ejemplo quiero acceder desde el ínice uno al 4.
#entonces se pone lo siguiente

print (x1[1:5])

#soy feliz lo comprendí :D
