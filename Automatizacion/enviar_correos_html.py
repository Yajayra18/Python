import smtplib
import getpass
import bullet
import sys
import json
import re

from claseMensaje import Mensaje

# Regular Expression
email_patron = re.compile(r'\b[\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,6}\b')
url_patron = re.compile(r"^(https?:\/\/)?([\da-z\.-]+)\.([a-z\.]{2,6})([\/\w \.-]*)*\/?$")
html_patron = re.compile(r"\b[\w.%+-]+\.html")

# Import Configuration from json
with open("config.json", "r") as config_file:
    config = json.load(config_file)

# SMTP Connection
with smtplib.SMTP(config["host"][config["host_opc"]], config["port"]) as server:
    server.starttls()

    print("***** Login *****")
    # Username
    while True:
        temp_email = input("Login ( [%s] ): "%config["email"])
        if temp_email != "":
            if email_patron.match(temp_email):
                config["email"] = temp_email
                break
            else:
                print("WARNING: write an able email.")
        else:
            break

    # Password
    pass_personal = getpass.getpass()
    if pass_personal == "":
        print("WARNING: please write your password.")
        sys.exit(1)

    # Login 
    try:
        server.login(config["email"], pass_personal)
    except smtplib.SMTPAuthenticationError:
        print("WARNING: Could not login to the smtp server please check your username and password.")
        sys.exit(1)
    
    # Message class
    new_message = Mensaje(config["email"])

    print("\n***** Email *****")
    # Subject
    new_message.add_subject("Feliz cumpleaños")
    # To
    new_message.add_email("jkahn@imca.edu.pe")
    # HTML

    while True:
        temp_html = input("HTML ( [%s] ): "%config["html"])
        if temp_html != "":
            if html_patron.match(temp_html):
                config["html"] = temp_html
                break
            else:
                print("WARNING: write an able html file.")
        else:
            break
    new_message.add_message_html(config["html"])

    #server.sendmail(new_message.From, new_message.To, new_message.get_message().encode("utf8"))

# Save Configuration into json
with open('config.json', 'w') as outfile:
    print("Save configuration ... in process")
    json.dump(config, outfile, sort_keys=True, indent=4)
    print("Save configuration ... OK")

print("Mensaje enviado satisfactoriamente")