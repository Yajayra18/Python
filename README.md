# LearnPython
Pasos para aprender python y git.

Pasos de instalacion del repositorio:
PASO 1 ! ----- Crear cuenta 
(Imagen adjunta)
Crear cuenta en el siguiente link:
	https://github.com/
Conectarse a la cuenta (sing in).
Conectar a Setting (click sobre la imagen parte superior derecha).
Entrar a SSH and GPG keys (letras azules).
	https://github.com/settings/keys
Esperar al paso 3


PASO 2 ! ----- Instalar Git
Instalar git descargandolo del siguiente link
	https://gitforwindows.org/


PASO 3 ! ----- Configuracion clave SSH 
Abrir CMD.
	Buscar en los programas con el nombre "CMD"(pantalla negra)
Crear la carpeta(escribir el texto despues del simbolo ">"):
	C:\Users\Joseph> mkdir .ssh
Entrar en la carpeta:
	C:\Users\Joseph> cd .ssh
Generar clave SSH:
	C:\Users\Joseph\.ssh> ssh-keygen -t rsa -b 4096 -C "email@gmail.com"

Genera dos archivos (id_rsa y id_rsa.pub) en la carpeta .ssh
Abrir id_rsa.pub con sublime o blog de notas
Copiar el contenido del archivo id_rsa.pub en setting/SSH key
	https://github.com/settings/keys


PASO 4 ! ----- Configuracion Git
Configurar git
	C:\Users\Joseph> git config --global user.name "Joseph Kahn"
	C:\Users\Joseph> git config --global user.email "email@gmail.com"

	


