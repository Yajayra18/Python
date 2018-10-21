# OPERADORES

# ----- Datos -----
a = 3
b = 4
c1 = 'Hola'
c2 = 'Comida'
bT = True
bF = False

# == : Igualdad
    # = es de asignación (Guardar información)
    # La igualdad me brinda boleanos (es decir True o False)
        
print(a==b)
print(c1 == c2)
print(c1 == 'Hola')
print(bT == bF)
# Notita: estos pueden ser usados con if, else o elif.


# +,-,*,/ : Operaciones básicas
print(a+b,a-b,a*b,a/b)
print(a/b)  # división real
print(a//b) # división entera
print(4/2)
print(4/2== 2)
print(4//2)

arr = range(10)
print (arr[10//2])
print (c1 + c2)
#print (c1 - c2) #no se puede restar cadena con cadena
#print (c1*c2) # no se puede multiplicar cadena con cadena
#print (c1/c2) #no  se puede divider cadena con cadena

print (a*c1)

# **, % : Exponenciación y módulo
print(a**b) # a: base, b: exponente

x = 3
y = 10
for i in range(y):
    print('%i = %i (mod %i)'%(i,i%x,x))
