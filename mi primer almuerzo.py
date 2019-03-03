print ("MAYORES QUE EL ANTERIOR")
a = int(input ("¿Cuántos valores va a introducir?"))
print ("escriba los valores")

b = int(input("Escriba un número:"))

for x in range(a-1):
    c = int(input("Escriba un número más grande que %i :" %(b)))
    if c < b:
        print ("%i no es mayor que %i:" %(c,b))
print ("Gracias por su colaboración")
