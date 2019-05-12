# # Pregunta 1: 
print("\n===========Pregunta1==============\n")
def funcion1(inicio,final):
    for x in range(inicio,final):
        print(x)
funcion1(2,5)

# # Pregunta 2
print("\n===========Pregunta2==============\n")
def funcion2(b,h):
    print (b*h)
funcion2(5,6)

# # Pregunta 3
print("\n===========Pregunta3==============\n")

def funcion3(texto,letra):
    print(texto.count(letra))   
    contador = 0
    for y in texto:
        if y == letra:
            contador += 1 
    ## Escribe tu codigo
    print(contador)
funcion3("Hola amorcito cuchurrumi alias la flojis flojis","o")

# # Pregunta 4
print("\n===========Pregunta4==============\n")
def funcion4(cadena):
    print(cadena[::-1])

def funcion5(cadena):
    cadena_invertida = "" #<- Porqué usar comillas? cadena de texto vacia
    for i in cadena: # i toma cada elemento de la variable cadena comenzando por C,a,r
#y por que la impresión no es cada letra inicando con C --- desde que momento sabe que tiene que imprimir invertida? mmm :O.. ya veo 
        cadena_invertida = i + cadena_invertida#+ i #<- se parece al que le sumabamos 1 pero en ese le sumas i.
        #print(cadena_invertida)#print en cada iteracion
    print(cadena_invertida)#print fuera del bucle, solo se ejecuta 1 vez
#como haces para que imprima el último resultado y no todooo lo que se vez
#entiendo. 
#practicamente el i define en donde  se pondrá la siguien letra. si la pongo antes da el resultado que se ve y si se pone después sale en el mismo orden.

# "hola " + "como estas" == "hola como estas"
# "como estas" + "hola " == "como estashola "

#sí importa el orden en una cadena

# 2 + 3 == 5
# 3 + 2 == 5

#ejemplo
nombres = "Carmen Yajayra"
apellidos = "Arauco Flores"

#print() #escribe el orden, escribe dentro del parentesis

print(nombres + " " + apellidos)#no va con mayuscula!!!

print(nombres[0]) #posicion 0
print(nombres[0:6]) # posicion 0,1,2,3,4,5
print(nombres[0:6:2]) # posicion 0,2,4
print(nombres[6:0:-2]) # posicion 6,4,2 #[inicio:final+1;salto]
print(range(0,10,3)) # 0,3,6,9
print(range(0,10,2)) # 0,2,4,6,8     inicio = 0, final = 9, salto = 2
#nomenclatura
print(nombres[:6:2]) # si no hay numero se sobre entiendo que desde la position cero
print(nombres[6::2]) # si no hay numero se sobre entiende que es hasta el final
print(nombres[::2]) # desde el inicio hasta el final saltando de 2 en 2
print(nombres[::-2]) # desde el final hasta el inicio saltando de 2 en 2
print(nombres[::-1]) #Genial! ahora sí te puedo llamar?

#funcion4("Carmen Yajayra Arauco Flores")
#funcion5("Carmen Yajayra Arauco Flores")

# # Preguntas para Yajayra
# 
# ## Pregunta 1
# #Crea una función que dados dos números mostrará todos los números que hay entre ellos.
# #```python
# #funcion1(inicio, final)
# #funcion1(2,5)
# #```
# 
# ## Pregunta 2
# #Crear una función que calcule el área de un rectángulo dando como valores la base y la #altura.
# #```python
# #funcion2(altura, base)
# #funcion2(5,6)
# #```
# 
# ## Pregunta 3
# #Crea una función que dado una cadena de texto cadena_texto y una letra variable_letra  #retorne cuantas veces aparece la letra variabla_letra  en la cadena de texto cadena_texto.
# #```python
# #funcion3(cadena_texto,variable_letra)
# #funcion3("Hola amorcito cuchurrumi alias la flojis flojis", "o")
# #```
# 
# ## Pregunta 4
# #Crear una función que  permita mostrar los caracteres de una cadena del final al principio.
# #```python
# #funcion4(cadena)
# #funcion4("Carmen Yajayra Arauco Flores")
# #```
