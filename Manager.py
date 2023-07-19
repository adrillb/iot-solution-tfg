import tkinter as tk
import subprocess
import requests
# import datetime

from Controller import Controller
from screens.HomeScreen import HomeScreen
from screens.NewPurchaseScreen import NewPurchaseScreen
from screens.ViewStorageScreen import ViewStorageScreen
from screens.Screen1 import Screen1
from tkinter import messagebox
from solutionDB.DataBase import DataBase
from style import styles
from PIL import Image

from pyzbar.pyzbar import decode

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("IOT-SOLUTION")        
        # self.attributes('-fullscreen', True)
        self.controller = Controller()
        self.dataBase = DataBase()
     #    self.new_purchase = NewPurchase()
        self.container = tk.Frame(self)
        self.container.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True
        )
        
        self.container.configure(
            background = styles.BACKGROUND
        )
        self.container.grid_columnconfigure(0, weight = 1)
        self.container.grid_rowconfigure(0, weight = 1)

        self.frames = {}
        
        screens =(HomeScreen, NewPurchaseScreen, ViewStorageScreen,)
        for F in screens:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.show_frame(HomeScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

###########################################################################################################################################################################################################################

     #MAIN MENU METHODS#

    def new_purchase(self):     #Register products from new purchase
         self.show_frame(NewPurchaseScreen)                  

    def show_stored_products(self):
         print("def show_stored_products")
         self.show_frame(ViewStorageScreen)

         
     #NEW_PURCHASE METHODS#
    def voice_input(self):
         print("Start voice_input method.") 
    def scan_product(self):
         productList = []

         #while 'Next product' until 'Finish'
         # {
         barcode = self.read_barcode()
         print('Barcode: ', barcode)

         product_name = self.get_product_name(barcode)
         print('Product_Name: ', product_name)

         #  bool registerEXP? 
         #  {
         expiry_date = self.get_expiry_date()
         print('Expiry_Date: ', expiry_date)
         # article.name = product_name
         # article.expiry_date = expiry_date
         #  }
         # }
         product = (product_name, expiry_date)

         productList.append(product)
         #_____________________________________________
         #Insert Product on DDBB         
         self.register_productList(productList)
         self.show_product_succ_registered(product_name)

    def read_barcode(self):
            print("He llegado a la funcion")
            # ##############################################################################################################################
            ###TOMAR FOTO Y LEER CODIGO DE BARRAS

            # process = subprocess.Popen(['libcamera-still', '-f', '-t', '2000', '-o', 'barcode.png'])
            # process.wait()
            # with open('barcode.png', 'rb') as img:
            #     barcodeImage = img.read()
            # barcode = decode(barcodeImage)
            # barcodeImg = Image.open("REAL")
            # print(barcodeImg)
                                 
            # barcode = decode(Image.open("/home/adrillb/Downloads/barcode.png"))            
             
            # if len(barcode) != 0:
            #     print("Tipo: ", barcode[0].type)
            #     print("Data: ", barcode[0].data.decode())                       
            #CON FOTO
            
            # keepScanning = True
            # cont = 0
            # while keepScanning:        
                
            #       process = subprocess.Popen(['libcamera-still', '-f', '-t', '2000', '-o', 'barcode.png'])
            #       process.wait()
            #       with open('barcode.png', 'b') as img:
            #            barcodeImage = img.read()
            #       barcode = decode(Image.open(barcodeImage))                    

            #       if len(barcode) != 0:
            #            print("Tipo: ", barcode[0].type)
            #            print("Data: ", barcode[0].data.decode('utf-8'))                       
            #            keepScanning = False
            #       if cont > 10:
            #            keepScanning = False
            #       cont += 1                                                                         
            # print("SALÍ")  
            barcodeNumber = "8480000154309"
            print('Voy a salir def1 b:', barcodeNumber)
            return barcodeNumber                 

            # ##############################################################################################################################          

    
    def get_product_name(self, productId):  # Get product name by barcodeNumber [Using OpenFoodFacts API]
         
         url = 'https://world.openfoodfacts.org/api/v0/product/' + productId + '.json'
         params = {'fields': 'product_name'}

         response = requests.get(url, params=params)

         if response.status_code == 200:
              data = response.json()
              product_name = data['product']['product_name']
              print('Product_name: ', product_name)
              ## Posible lógica de cambio de nombre que decida el usuario              
              return product_name
         else:
              print('OpenFoodFacts_API_request failed: ' + response.status_code)
              return "fail"


    def get_expiry_date(self):  # Register expiry date if user chooses to [Manual entry]                  
         day = "01"
         month = "09"
         year = "9999"
         return day + "/" + month + "/" + year


    def register_productList(self, productList):         
         for product in productList:
              data = self.toJson(product)
              self.dataBase.insert_product(data)


    def toJson(self, product):
         return {
              "product_name" : product[0],
              "expiry_date" : product[1]
         }         

     # POP-UP MESSAGES

    def show_product_succ_registered(self, product_name):
         messagebox.showinfo("Product registered", ("\""+product_name+"\" succesfully registered"))
            
            
            

            #CAMARA ACTIVA
            # cap = cv2.VideoCapture(1)

            # if not cap.isOpened():                
            #     print("Error al abrir la cámara")
            #     exit()

            # cap.set(3, 640)
            # cap.set(4, 480)

            # while True:           
            #     success, frame = cap.read()

            #     if not success:
            #         print("Error al leer el fotograma")
            #         break
                
            #     # barcodes = decode(frame)

            #     # for barcode in barcodes:
            #     #     print("Valor: ", barcode.data.decode("utf-8"))

            #     cv2.imshow('frame', frame)

            #     if cv2.waitKey(1) & 0xFF == ord('q'):
            #         break
            
            # cap.release()
            