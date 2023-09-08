from firebase import firebase
import firebase_admin 
from firebase_admin import credentials, db
import datetime


cred = credentials.Certificate("/home/adrillb/Desktop/TFG/Python/iot-solution/FirebaseCredentials/iot-solution-8d63c-firebase-adminsdk-w137e-7cbc402569.json")
firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app'})

ref = db.reference('/Database/AlertDate')
current_date = datetime.datetime.now().strftime("%d-%m-%Y") 
ref.child("last_alerted_date").set(current_date)

# products = ref.get()
# for i, (id, registro) in enumerate(products.items(), start=1):
#     print(id)
#     print(registro.get("product_name"))
#     print(registro.get("expiry_date"))

# firebase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

# for i in range(1):
#     name = "ProductTest"+str(i+3)
#     product = {
#     "product_name" : name,
#     "expiry_date" : "07-08-2023"
#     }
#     firebase.post('/Database/Products', produc



#products = firebase.get('/Database/Products', None)

#firebase.delete('/Database/Products', '-NTdtv0JU3RSDZXqVrJF')
