print ("SUMA ENTRE VALORES")
a = int(input("Escriba un número entero:"))
b = int(input("Escriba un número entero mayor que %i:" %a))
if a >= b:
    print ("Le he pedido un número entero mayor que %i"%a)
else:
    suma = 0
    for i in range(a,b+1):
        suma += i
    print ("La suma desde %i hasta %i es %i" %(a,b,suma))
    print (str(range))
