"""Escriba un programa que pida dos 
números enteros y escriba qué números 
son pares y cuáles impares desde el 
primero hasta el segundo.
"""

print ("PARES E IMPARES")
n = int(input("Escriba un número entero:"))
x = int(input ("Escriba un número mayor o igual que %i:"%n))
if x >= n:
    a = n
    while a <= x:
        if a%2 == 0:
            print ("El número %i es par" %a) 
        else:
            print ("El número %i es impar" %a)
        a += 1
#elif n == x:
    #while n == x:
         #if x%2 == 0:
             #print ("El número %i es par" %n)
        #else:print ("El número %i es impar" %n)
else:
    print ("¡Le he pedido un número entero mayor que %i" %n)


#n += 1 <= x



