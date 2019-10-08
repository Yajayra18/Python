#Operadores Aritmeticos
#Un tip (de las buenas practicas)
#Es colocar espacios entre los operadores aritmeticos
# otro tip es no usar tildes :)

#SUMA
t = 26 + 4 
print (t)
#no olvides que para usar print,
#es importante coloca parentesis

#RESTA
i = 55 - 10

#MODULO
e = 5 % 2 
# el modulo"%" hace como si fuera una division, y saldra de respuesta el residuo 
print (e)
# en este caso el residuo es 1.

#DIVISION
u = 8 / 2
print (u)
#De esta realmente no me acuerdo si el resultado es int o float. (Queda como duda xD)

#MULTIPLICACION
p = 200 * 5

#EXPONENTE
d = 5 ** 2

#DIVISION ENTERA
r = 80 // 7

#Aprendizaje del dia.- Funcion imput() -
#esta funcion nos permitira obtener un texto (string)
#escrito por el teclado.
#Cuando se llegue a la funcion el programa se detendra
#para recibir la informacion y se tomara esta  ponerlo con un 
#"enter"

print ("Hola soy Yajayra, ¿Cómo te llamas tú?")
nombre = input()
print ("me alegra mucho conocerte, {nombre}")

# supongamos que en el nombre pusieron "Pepito Palotes"
# Aqui se imprimira  me alegra mucho de conocerte, Pepito Palotes

#Recuerda que input solo ingresa texto, entonces si quieres cambiarlo a un numero
#Puedes hacer lo siguiente

cantidad = int(input("Coméntame¿Cuántos vasos de agua tomas al día?"))
print ("cantidad",", Interesante")

#Aprendizaje2: Igual == , Diferente != , Mayor que > , menor que <. mayor igual que >=, menor igual que <=.

#Ejercicios
#Vamos inténtalo

#1- Realiza un programa que lea 2 numeros 
#por teclado y determine los siguientes aspectos
#Es suficiente mostrar True o False
#- Si los dos numeros son iguales
#- Si los dos numeros son diferentes
#- Si el primero es mayor que el segundo
#- Si el segundo es mayor o igual que el primero

print ("Hola, por favor ingresa un número ")
num_1 = input()
print ("Ahora ingresa otro número ")
num_2 = input()

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 >= num_2)


#Intentando hacer algo mas elaborado (Falta Corregir :3)
print ("Hola, por favor ingresa un número ")
n_1 = input()
print ("Ahora ingresa otro número ")
n_2 = input()

if n_1 == n_2:
    print ("Ambos números son iguales")
elif n_1 != n_2:
    print ("Ambos números son irerentes")
elif n_1 > n_2:
    print ("El primer número es mayor que el segundo número")
elif n_1 >= n_2:
                print ("El primer número es mayor igual que el segundo número")
pass: print("Que Bonitos números xD")
     
