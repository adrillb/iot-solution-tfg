from firebase import firebase
import firebase_admin 
from firebase_admin import credentials, db


# cred = credentials.Certificate("/home/adrillb/Desktop/TFG/Python/iot-solution/FirebaseCredentials/iot-solution-8d63c-firebase-adminsdk-w137e-7cbc402569.json")
# firebase_admin.initialize_app(cred, {'databaseURL': 'https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app'})

# ref = db.reference('/Database/Products')
# products = ref.get()
# print("Holu")
# for i, (id, registro) in enumerate(products.items(), start=1):
#     print(id)
#     print(registro.get("product_name"))
#     print(registro.get("expiry_date"))

firebase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

for i in range(20):
    name = "test"+str(i)
    product = {
    "product_name" : name,
    "expiry_date" : "(23-14-49)"
    }
    firebase.post('/Database/Products', product)


#products = firebase.get('/Database/Products', None)
print("hola")

#firebase.delete('/Database/Products', '-NTdtv0JU3RSDZXqVrJF')
3