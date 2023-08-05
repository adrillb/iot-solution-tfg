import smtplib
import datetime
import json
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class Alerts:
    def __init__(self, manager):        
        self.manager = manager
        settings = self.getUserSettings()
        self.sender_email = settings.get("sender_email")
        self.sender_password = settings.get("sender_password")
        self.receiver_email = settings.get("receiver_email")

        self.smtp_server = "smtp-mail.outlook.com"
        self.smtp_port = 587

    def send_email(self, subject, message):
        msg = MIMEMultipart()
        msg['From'] = self.sender_email        
        msg['Subject'] = subject        

        try:
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)   
                for email in self.receiver_email:  
                    msg['To'] = email                  
                    username = email.split('@')[0]
                    body = "Hey " + username + ",\n\n" + message
                    msg.attach(MIMEText(body, 'plain'))
                    #server.sendmail(self.sender_email, email, msg.as_string())
                    body = ""
                    print("Correo de alerta  enviado a "+email)       
                    #self.manager.loger.showinfo("Correo de alerta enviado a "+email)                                    
                        
        except Exception as ex:
            #self.manager.logger.showinfo("Error al enviar correo: " + ex)
            print("Error al enviar correo: ")
            print(ex)

    def check_alerts(self):
        print("check_alerts")
        current_date = datetime.datetime.now().date()        
        data = self.manager.dataBase.read_products()
        alert = False
        if data:
            message = ""
            for i, (id, record) in enumerate(data.items(), start=1):
                product_date = record.get("expiry_date")
                if product_date != "00-00-0000":
                    product_name = record.get('product_name')
                    expiry_date = datetime.datetime.strptime(record.get("expiry_date"), "%d-%m-%Y").date()
                    dif = (expiry_date - current_date).days
                    if dif <= 2:
                        alert = True                                                 
                        if dif < 0:                            
                            message += "\n\n\t- " + product_name + " expired on " + product_date + ". Consider getting it out of the fridge/pantry or throwing it away."                            
                        elif dif == 0:
                            message += "\n\n\t- " + product_name + " expires today " + product_date + "! Hurry, go use it!."  
                        elif dif == 1:
                            message += "\n\n\t- " + product_name + " expires tomorrow " + product_date + ". Don't let it go to waste!"                          
                        else:
                            message += "\n\n\t- " + product_name + " expires the day after tomorrow " + product_date + ". Don't let it go to waste!"                                                     
            if alert:                                           
                subject = "ALERT IN YOUR FRIDGE/PANTRY"
                intro = "Important information about your stored products has been detected:\n"  
                message += "\n\n\nThanks for using our services!\nHave a pleasant day,\nPapito dulse." 
                body = intro + message
                self.send_email(subject, body)
                # self.manager.logger.showinfo("Email body: " + message)
                print("Email body: " + body)






































                        
    
    def getUserSettings(self): 
        with open('/home/adrillb/Desktop/TFG/Python/iot-solution/solutionAlerts/userSettings.json', 'r') as json_file:
            return json.load(json_file)

    
    
    
