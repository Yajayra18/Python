Contador = 0
for x in "hola Mundo":
    if x == "o":
        Contador += 1
    else:
        Contador += 0 
#print (Contador)


 
def evaluar_letra(x):
    Contador = 0
    for x in "hola Mundo":
        if x == "o":
            Contador += 1
            return 1
        else:
            Contador += 0
            return 0

print (Contador)
a = evaluar_letra(x) 
print (a)