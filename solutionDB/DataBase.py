from firebase import firebase
import firebase_admin 
from firebase_admin import credentials, db

class DataBase:
    def __init__(self):
        self.dataBase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

        cred = credentials.Certificate("/home/adrillb/Desktop/TFG/Python/iot-solution/FirebaseCredentials/iot-solution-8d63c-firebase-adminsdk-w137e-7cbc402569.json")
        firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app'})
        self.ref = db.reference('/Database/Products')


    def insert_product(self, product):            
        self.dataBase.post('/Database/Products', product)

    def read_products(self):
        return self.ref.get()

    def delete_product(self, id):
        self.dataBase.delete('/Database/Products', id)
