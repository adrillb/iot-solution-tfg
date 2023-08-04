import smtplib

class Alerts:
    def __init__(self, sender_email, sender_password):
        self.sender_email = sender_email
        self.sender_password = sender.password

        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def send_email(self, receiver_email, subject, message):
        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender.password)
                email_body = f"Subject: {subject}\n\n{message}"
                server.sendmail(self.sender_email, receiver_email, email_body)
             self.manager.loger.showinfo("Correo de alerta enviado a "+receiver_email)
             print("Correo de alerta  enviado a "+receiver_email)
        except Exception as ex:
            self.manager.logger.showinfo("Error al enviar correo: " + ex)
            print("Error al enviar correo: " + ex)

            

    
    
    
