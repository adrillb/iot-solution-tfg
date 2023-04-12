import tkinter as tk
import subprocess
import requests

from Controller import Controller
from screens.HomeScreen import HomeScreen
from screens.Screen1 import Screen1
from style import styles
from PIL import Image

from pyzbar.pyzbar import decode

class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("IOT-SOLUTION")
        self.controller = Controller()
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
        
        screens =(HomeScreen, )
        for F in screens:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.show_frame(HomeScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()


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
            self.request_openFoodFacts_API(barcodeNumber)

            # ##############################################################################################################################          

    def request_openFoodFacts_API(self, productId):
         url = 'https://world.openfoodfacts.org/api/v0/product/' + productId + '.json'
         params = {'fields': 'product_name'}

         response = requests.get(url, params=params)

         if response.status_code == 200:
              data = response.json()
              print('Product_name: ', data['product']['product_name'])
         else:
              print('OpenFoodFacts_API_request failed: ', response.status_code)

            
            

            
            
            

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
            