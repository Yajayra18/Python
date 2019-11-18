# Clase mensaje
class Mensaje:
    # Constructor
    def __init__(self, From):
        self.From = From
        self.To = []
        self.Subject = ""
        self.MessageHTML = ""
        print("New Message was created.")
    
    def add_email(self, email):
        self.To.append(email)

    def add_subject(self, subject):
        self.Subject = subject
    
    def add_message_html(self,html_file):
        with open("html/" + html_file, "r", encoding='utf-8') as html:
            self.MessageHTML = html.read()
    

    def get_message(self):
        temp = "Subject: %s\n"%self.Subject
        temp += "From: %s\n"%self.From
        temp += "To: " + ", ".join(self.To) + "\n"
        #temp += "To: CaraMoco@hotmail.com\n"
        temp += "Content-Type: text/html; charset=UTF-8\n\n"
        temp += "%s"%self.MessageHTML
        return temp