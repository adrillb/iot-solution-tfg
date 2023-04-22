from firebase import firebase

class DataBase:
    def __init__(self):
        self.dataBase = firebase.FirebaseApplication("https://iot-solution-8d63c-default-rtdb.europe-west1.firebasedatabase.app", None)        

    def insert_product(self, product):            
        self.dataBase.post('/Database/Products', product)

    def read_dataBase(self):
        return self.dataBase.get('/Database/Products')

    def delete_product(self, id):
        self.dataBase.delete('/Database/Products', id)
