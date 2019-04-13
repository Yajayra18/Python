#Realizar una funcion llamada relacion (a,b)
#que a partir de dos numeros intermedio cumpla los siguiente
#* Si el primer numero es mayor que el segundo, devolver 1
#*Si el primer numero es menor que el segundo, devolver -1
#* si ambos numeros son iguales, debe devolver un 0
#Compruebe la relacion de los numeros:
#5 y20; 10y5; 5y5.

def relacion(a,b):
    if a > b:
        print (1)
    elif a < b:
        print (-1)
    elif a == b:
        print (0)
    else:
        print ("nothing")

relacion(5,20)
relacion(10,5)
relacion(5,5)