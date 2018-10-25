# Sentencias Condicionales
J = 24
Y = 25


if  Y > J:
	print ("Joseph es muy flojis flojis")
	if True: 
		print ("Joseph ha sido mala influencia")
else:
	print ("Joseph es menor que Yajayra")

#Edad Mínima de Postulante

Emi = 25

#Edad Máxima de postulante
Ema = 45 

#Edad de Postulante
Ep = 48
print ("el rango de edad de nuestras Haditas es de 25 a 45 años")
print ("Respuesta a postulante de 48 años")

if Ep >= Emi and Ep <= Ema :
	print ("El cumplir el primer requisito la invitamos a participar de la entrevista") 
else:
	print ("Lamentablemente no puede participar de la entrevista por no cumplir este primer requisito")

print ("Segunda condición experiencia mínima de 12 meses")
print ("la postulante cuenta con 14 meses de experiencia")
#Experiencia de postulante
# mínimo 12 meses
E = 12
# Postulante cuenta con 14 meses de experiencia
Pos = 14

if Pos >= E:
	print ("Al cumplir con este segundo requisito, puede participar de la entrevista")
else:
	print ("Lamentablemente no puede participar de la entrevista por no cumplir este segundo requisito")

# if not Ep <= Emi and Ep >= Ema:
# if  Ep <= Emi or Ep >= Ema:

if  Ep <= Emi and Ep >= Ema:
	print ("Lamentablemente no puede participar de la entrevista por no cumplir este primer requisito")
elif Pos <= E:
	print ("Lamentablemente no puede participar de la entrevista por no cumplir ambos requisito")
else:
	print ("Al cumplir ambos requisitos, la invitamos a participar de la entrevista")

