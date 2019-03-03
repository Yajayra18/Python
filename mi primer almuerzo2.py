print ("CONTADOR DE PARES E IMPARES")
a = int(input("¿Cuántos valores va introducir?"))
par = 0
impar = 0
if a < 0:
    print ("¡Imposible!")
for x in range(a):
    b = int(input("Escriba el valor %i:" %(x+1)))
    if x%2 == 0:
        par = par + 1 #par += 1
    if x%2 == 1:
        impar = impar + 1 

print ("Ha escrito %i números pares y %i números impares" %(par,impar))
print ("Gracias por su colaboración")


