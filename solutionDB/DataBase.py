from firebase import firebase
import firebase_admin 
from firebase_admin import credentials, db

class DataBase:
    def __init__(self):
        self.dataBase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

        cred = credentials.Certificate("/home/adrillb/Desktop/TFG/Python/iot-solution/FirebaseCredentials/iot-solution-8d63c-firebase-adminsdk-w137e-7cbc402569.json")
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app'})
        self.refProducts = db.reference('/Database/Products')
        self.refAlertDate = db.reference('/Database/AlertDate') 


    def insert_product(self, product):            
        self.dataBase.post('/Database/Products', product)

    def read_products(self):
        return self.refProducts.get()

    def delete_product(self, id):
        self.dataBase.delete('/Database/Products', id)

    def modify_alertDate(self, date):
        self.refAlertDate.child("last_alerted_date").set(date)

    def read_alertDate(self):
        return self.refAlertDate.child("last_alerted_date").get()
