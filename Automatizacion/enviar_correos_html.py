import smtplib
import getpass
import bullet
import sys
import json
import re

from claseMensaje import Mensaje

email_patron = re.compile(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b')
url_patron = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
#configparser
# Import previously config
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# Configuracion de correo(s)
html = "html/correo_html.html"

print("***** Send email *****")
# Email
while True:
    temp_email = input("Login ([%s]): "%config["email"])
    if temp_email != "":
        if email_patron.match(temp_email):
            config["email"] = temp_email
            break
        else:
            print("WARNING: write an able email.")
    else:
        break

# Password
try:
    if sys.platform == "linux":
        cli = bullet.Password("Password: ")
        pass_personal = cli.launch()
    elif sys.platform == "win32":
        pass_personal = getpass.getpass()
except Exception as error: 
    print('ERROR: ', error) 
#else: 
#    print('Password entered:', p) 


new_message = Mensaje(config["email"])
#Mensaje.add_email(["carauco@cosapi.com.pe"])
new_message.add_email("jkahn@imca.edu.pe")
new_message.add_subject("Feliz cumpleaños")
new_message.add_message_html(config["html"])

"""
with smtplib.SMTP(host, port) as server:
    server.starttls()
    server.login(new_message.From, pass_personal)
    server.sendmail(new_message.From, new_message.To, new_message.get_message().encode("utf8"))
    #server.quit()
"""
print("Mensaje enviado satisfactoriamente")

