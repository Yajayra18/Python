#Realiza un funcion que imprima "Hola mundo"
def texto ():
    print ('Hola mundo')
texto()
#Realiza una funcion que indique si 
def suma (num1,num2):
    print (num1 + num2)
#Realiza una funcion que indique si un
#numero pasado por parametro es para o impar
def parimpar(a):
    if a%2 == 0:
        print ("El numero es par")
    if a%2 == 1:
        print ('El numero es impar')
    
#parimpar(0)
def numero(a):
    if a%2 == 0:
        print ("El numero es par")
        return 1
    if a%2 == 1:
        print ('El numero es impar')
        return 0
    
#numero (5)

contador = 0
for x in range(15,17):
    contador += numero(x) #contador + numero(x) = contador
print (contador)