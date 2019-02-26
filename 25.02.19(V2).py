"""Escriba un programa que pida dos 
números enteros y escriba qué números 
son pares y cuáles impares desde el 
primero hasta el segundo.
"""

print ("PARES E IMPARES")
n = int(input("Escriba un número entero:"))
x = int(input ("Escriba un número mayor o igual que %i:"%n))
if x >= n:
    for y in range (n,x + 1):
        if y%2 == 0:
                print ("El número %i es par" %y) 
        else:
               print ("El número %i es impar" %y)

  
else:
    print ("¡Le he pedido un número entero mayor o igual que %i!" %n)


#Gracias!!!!  hoy aprendí mucho <3 <3 , Eres grandioso :*





