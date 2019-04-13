# Funciones suma
print("====== Funcion sumar =====")
def SumarNumeros(a,b):
    print(a+b)
    x = a+b
    print("variable local x: ",x) 
x = 4+4
print("variable global x: ", x)
SumarNumeros(1,1)
#suma 2 + 3 utilizando la funcion SumarNumeros
SumarNumeros(2,3)
SumarNumeros(2,4)   
print(x)

print("====== Funcion restar =====")
# Define una funcion que reste dos numeros
def RestarNumeros(a,b):
    print(a-b)
RestarNumeros(4,2)

print("====== Funcion imprimir un texto =====")
def ImprimirTexto():
    x = 2 + 3
    'hola, puto!'
    print("Puto el que lo lea! PUTO!")

ImprimirTexto()
ImprimirTexto()
ImprimirTexto()

print("====== Comando Return =====")
def Sumar(a,b):
    print('dentro de la funcion',a+b)
    return a+b

valor = Sumar(1,4)
print('fuera de la funcion',valor)


print('fuera de la funcion',Sumar(1,4))

print("====== Resumen =====")
# 1. Como definir una funcion
# 2. Argumentos de una funcion(variables)
# 3. Retorno del resultado de la funcion


def unirCadenas(cadena1,cadena2):
    #union = cadena1 +" "+ cadena2
    #print(union)
    #guardar union en un archivo
    
    return "Super Mega Puto el que lo lea"

print(unirCadenas("Puto", "el que lo lea"))
#abrir archivo y asignar el valor de union

#print(unirCadenas("Super Puto", "el que lo lea"))
 
#Notita, obj reducir el codigo... al llamar a la función realiza toda la funcion.

def Sumasa(a,b):
    print('dentro de la funcion',a+b)
    return a+b

valor1 = Sumar(1,4)
valor2 = Sumar(5,4)




def f(numero):
    return 2

print(f(3))