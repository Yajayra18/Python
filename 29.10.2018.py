#Condicionales
#Considerando que los  siguiente son calificaciones

A = 20
B = 15
C = 10

pp = 16

if pp <= C:
	print ("Pepito ha jalado el curso")
elif pp <= B and pp >= C:
	print ("Pepito, aprobó")
elif pp <= A and pp >= B:
	print ("Pepito aprobó con excelencia")

#Edades y grado de instrucción

#Inicial
I = 3
#Primaria
P = 6
#Segundaria 
S = 12
# Fin de Cole
F = 16

Ada = 17

if Ada < P and Ada >= I:
	print ("Ada se encuentra cursando la educación Inicial")
elif Ada < S and Ada >= P:
	print ("Ada se encuentra cursando la Primaria")
elif Ada <= F and Ada >= S:
	print ("Ada se encuentra cursando la Segundaria")
else:
	print ("Ada ya no está en el colegio, y no sé que será de su vida :P")

print ("Yo siempre amo a mi amor El Joseph")