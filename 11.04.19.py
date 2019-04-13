#Crea una funcion que calcule factoria de un numero.
def holi():
    numero = 4
    factorial = 1
    while numero > 0:
        factorial = factorial * numero
        numero -=1
    print (factorial)

holi ()

#Crea una funcion que dados dos numeros mostrara
#todos los numeros que hay entre ellos
def imprime():
    for x in range(1,5):
        print (x)
imprime()


#Realiza una funcion llamada area_rectangulo(base,altura)
#que devuelva el area del rectangulo a partir
#de una base y altura. Cda area de n rectangulo
#de 15 de base y 10 de altura.

def area_rectangulo(base, altura):
    print (base * altura)

area_rectangulo(15, 10)

#Realiza una funcion llamada area_circulo(radio)
#que devuelva el area de un circulo a partir
#de un calculo a partir de un radio.
#Calcula el area del circulo de 5 de radio

def area_circulo(radio):
    print(radio**2*3.1415926)

area_circulo(5)