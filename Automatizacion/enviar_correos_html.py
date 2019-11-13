import smtplib
#from bullet import Password
#cli = Password("Contraseña: ")
#p= cli.launch()
#print(p)

# Clase mensaje
class Mensaje:
    # Constructor
    def __init__(self,From):
        self.From = From
        self.To = []
        self.Subject = ""
        self.Message = ""
        print("New Message was created.")
    
    def add_email(self,email):
        self.To.append(email)
    
    def add_list_email(self,email):
        self.To.append(email)

    def add_subject(self,subject):
        self.Subject = subject

    def add_message(self, message, html_flag):
        if html_flag:
            with open("./correo_html.html","r",encoding='utf-8') as html:
                self.Message = html.read()
        else:
            self.Message = message
    

    def get_message(self):
        temp = "Subject: %s\n"%self.Subject
        temp += "From: %s\n"%self.From
        temp += "To: "
        for i in range(len(self.To)):
            temp += "%s"%self.To[i]
        temp += "\n"
        temp += "Content-Type: text/html; charset=UTF-8\n\n"
        temp += "%s"%self.Message

        return temp

# Configuracion de conexion
host = "smtp.live.com"
port = 587

# Configuracion de correo(s)
html = "./correo_html.html"

mail_personal = "titanico19@hotmail.com"
pass_personal = input("Cerrar terminal despues de ejecutar\nPassword: ")


new_message = Mensaje(mail_personal)
#Mensaje.add_email(["carauco@cosapi.com.pe"])
new_message.add_email("jkahn@imca.edu.pe")
new_message.add_subject("Feliz cumpleaños")
new_message.add_message("",True)


with smtplib.SMTP(host, port) as server:
    server.starttls()
    server.login(new_message.From, pass_personal)
    server.sendmail(new_message.From, new_message.To, new_message.get_message().encode("utf8"))
    #server.quit()
print("Mensaje enviado satisfactoriamente")

