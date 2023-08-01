from firebase import firebase
import firebase_admin 
from firebase_admin import credentials, db

#firebase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        
cred = credentials.Certificate("/home/adrillb/Desktop/TFG/Python/iot-solution/FirebaseCredentials/iot-solution-8d63c-firebase-adminsdk-w137e-7cbc402569.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app'})

ref = db.reference('/Database/Products')
products = ref.get()
print("Holu")

product = {
    "product_name" : "Miel de flores",
    "expiry_date" : "(23-14-49)"
}
# firebase.post('/Database/Products', product)

#products = firebase.get('/Database/Products', None)
print("hola")

#firebase.delete('/Database/Products', '-NTdtv0JU3RSDZXqVrJF')
