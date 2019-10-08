#f = open("archivo.txt", "w")
#f.write("Hola.\n")
#f.write("Quiero aprender\n")
#f.write("Pero aun no entiendo como abrir un archivo")
#f.close()

p = ""
p += "Hola Mi nombre es Yajayra, y estoy aprendiendo a programar\n"
p += "Estoy entusiasmada pero sé que viene un laaaaargo camino"
i = open("Aprendiendo", "w")
i.write(p)
i.close


h = ""
h += "Mi poto es un molestoso poto\n"
h += "Mi michi me maltrata"
Bu = open("El poto 2.txt", "w")
Bu.write(h)
Bu.close()


#file = open("archivo.txt", "r")
#linea = file.readline()
#linea = file.readline()
#print (linea)
#print (help(file))
#file.close()

fb = open("facebook.html", "r")
Nel = fb.readlines()
fb.close()

for y in Nel[:3]:
    print (y)


cadena = "" #Siempre tiene que iniciar con un comillas
cadena += "vamos a unir \n"
cadena = cadena + "otra linea"
archivo = open("potito.txt", "w")
archivo.write(cadena) # Necesario
archivo.close()

