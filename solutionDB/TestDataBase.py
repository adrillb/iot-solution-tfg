from firebase import firebase

firebase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

product = {
    "product_name" : "Miel de flores",
    "expiry_date" : "(23-14-49)"
}
# firebase.post('/Database/Products', product)

# firebase.get('/Database/Products')

firebase.delete('/Database/Products', '-NTdtv0JU3RSDZXqVrJF')
