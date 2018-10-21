# comentario, esta linea no se imprime
# es una buena practica hacer comentarios!
# para el entendimiento en un futuro.

# Imprime hola mundo en ingles
print('Hello world, gasmorcito muah!\n') # Comentario al final de la linea

# ***** TIPOS DE DATOS *****
# Enteros
x1 = 4 # igual hace la asignacion(guarda la informacion)
x2 = -5
print('x1 y x2 son enteros')
print('x1 = ',x1)
print('x2 = ',x2)
print('el tipo de dato es :',type(x1))
print('\n')
# Reales
x3 = 4.5
x4 = 2.0

print('x3 y xy son reales')
print('x3 = ',x3)
print('x4 = ',x4)
print('el tipo de dato es :',type(x3))

print('\n')
# Cadenas de texto/String
nombre = 'Gasmorcito muah'
print('la variable nombre tiene la siguiente informacion')
print(nombre)
print('el tipo de dato es :',type(nombre))

print('\n')

# Boleano
bolean_T = True
bolean_F = False
print('bolean_T =',bolean_T)
print('bolean_F =',bolean_F)
print('el tipo de dato es :',type(bolean_F))

print('\n')
# Array / Cadenas
edades = [1,2,3,4,5,6] 
letras = ['A','b','C','d']
print(edades)
print(letras)
print('el tipo de dato es :',type(edades))
    # Observaciones
        ## La primera posicion es 0.
        ## si tiene n elementos, se cuenta de 0 a n-1.
        ## n es el numero de elementos del array.
        ## len() cuenta numero de elementos
        ## len() para un string cuenta numero de caracteres.
        ## subarray se realiza con [a:b] va desde la posicion a hasta la posicion b-1
        ## con saltaos [a:b:c] va desde a hasta b-1 saltando c posiciones cada vez
print('\nOperaciones Basicas con array')
print(edades[0],letras[2])
print(len(edades),len(letras))
#print(edades[6]) no es posible por que se sale del rango
# 6 elementos pero se cuenta de 0 a 5.
print('cuantos caracteres tiene la variable nombre')
print(len(nombre))
print(nombre[-1],edades[-1],letras[-2])
print(nombre[0:5])
print(edades[1:3])
print(letras[1:3])
print(nombre[2:15:3])

print('\n')
# Comando range()
print(range(10))
print(range(4,10))
print(range(4,10,2))

# Ejemplo usando for, para ver su aplicacion
# Queremos que salga de la siguiente manera
    ## G
    ## Ga
    ## Gas
    ## Gasm
    ## ....

for i in range(len(nombre)):
    print(nombre[0:i+1])

print('\n')
for j in range(10):
    print((j+1)*'*')
