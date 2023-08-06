import tkinter as tk
import requests
import time

from style import styles
from tkinter import simpledialog
from screens.HomeScreen import HomeScreen


class ScanInput(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)        

        self.productList = []

        self.start_scanning_button = tk.Button(self, text="SCAN PRODUCT", command=lambda: self.start_scanInput()
        ,**styles.STYLE, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.finish_scanInput_button = tk.Button(self, text="FINISH", command=lambda: self.finish_scanInput()
        ,**styles.STYLE, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.label_scanning = tk.Label(
            self, text="Scanning...", **styles.STYLE)
        self.insert_date = tk.Label(self, text="Insert Date:", **styles.STYLE)
        self.timeout = 5

        self.init_widgets()

    def init_widgets(self):
        self.hide_frame_widgets()
        self.start_scanning_button.pack(
            **styles.PACK_BUTTON
        )
        self.finish_scanInput_button.pack(
            **styles.PACK_BUTTON
        )

    def start_scanInput(self):
     self.hide_frame_widgets()
     self.label_scanning.pack(**styles.PACK_TITLE)     
     self.update()
     product = self.scan_product()
     #self.show_result(product)

    def scan_product(self):
        self.manager.logger.info("Start Scanning product")
        barcode  = 0
        # while True:


        
        #productList = []

        # while 'Next product' until 'Finish'
        # {
        

        #  product_name = self.get_product_name(barcode)
        #  print('Product_Name: ', product_name)

        #  #  bool registerEXP? 
        #  #  {
        #  expiry_date = self.get_expiry_date()
        #  print('Expiry_Date: ', expiry_date)
        #  # article.name = product_name
        #  # article.expiry_date = expiry_date
        #  #  }
        #  # }
        #  product = (product_name, expiry_date)

        #  productList.append(product)
        #  #_____________________________________________
        #  #Insert Product on DDBB         
        #  self.register_productList(productList)
        #  self.show_product_succ_registered(product_name)

        #___________________________________________________________________________________________________________
        # audio = "x"
        # while True:
        #     with sr.Microphone() as source:
        #         print("Listening")
        #         self.recognizer.adjust_for_ambient_noise(source)
        #         try:
        #             audio = self.recognizer.listen(source, timeout=self.timeout)
        #             print("processing...")
        #         except sr.WaitTimeoutError:
        #             print("TIMEOUT, be faster next time!")  
        #             self.manager.logger.info("Timeout reached")  
        #             tk.messagebox.showinfo("TryAgain", "Didn't get that, repeat please.")                
        #     if audio != "x":
        #         try:
        #             print("GoogleRecognition...")
        #             #Good Internet Connection
        #             text = self.recognizer.recognize_google(audio, language='es-ES')          
        #             #Poor Internet Connection
        #             #text = self.recognizer.recognize_sphinx(audio, language='es-ES')
        #             if text is not None:              
        #                 break
        #         except sr.UnknownValueError:
        #             print("Didn't get that")
        #             self.manager.logger.info("Did not recognize audio")
        #             self.scan_product()
        #         except sr.RequestError as e:
        #             print("Error calling Google Search Speech Recognition; {0}".format(e))
        #             self.manager.logger.info("Error calling Google Search Speech Recognition; {0}".format(e))
        # return text  

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
    
    def get_product_name(self, productId):  # Get product name by barcodeNumber [Using OpenFoodFacts API]
         self.logger.info("OpenFoodApi request productId:"+productId)
         url = 'https://world.openfoodfacts.org/api/v0/product/' + productId + '.json'
         params = {'fields': 'product_name'}
         
         try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
              data = response.json()
              product_name = data['product']['product_name']
              self.logger.info('Product_name: ', product_name)
              ## Posible lógica de cambio de nombre que decida el usuario              
              return product_name
            else:
                self.logger.info('OpenFoodFacts_API_request failed: ' + response.status_code)
                return "fail"
         except Exception as ex: 
            self.manager.logger.showinfo("")
            self.manager.logger.showinfo(ex)


    #____________________________________________________________________________________________________________

    def show_result(self, product):
        self.manager.logger.info("Audio recognized: " + product)
        if product != "":
              self.label_listening.pack_forget()
              self.label_product = tk.Label(self, text="Product: " + product).pack(**styles.PACK_TITLE)
              self.confirm_button = tk.Button(self, text="Confirm", command=lambda:self.confirm_product(product, False), **styles.STYLE).pack(**styles.PACK_BUTTON)
              self.say_again_button = tk.Button(self, text="Say again", command=self.start_voiceInput, **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_LEFT)
              self.with_date_button = tk.Button(self, text="Add Expiry Date", command=lambda:self.confirm_product(product, True), **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_RIGTH)


    def confirm_product(self, product_name, hasDate):
        #Registrar producto.
        productList = []
        expiry_date = "00-00-0000"
        
        if hasDate:
            #ask for date
            print("preguntamos fecha")
            expiry_date = self.ask_date()

        product = (product_name, expiry_date)
        productList.append(product)
        self.productList.append(product)
        
        self.hide_frame_widgets()
        self.init_widgets()

    def ask_date(self):
        self.hide_frame_widgets()
        self.insert_date.pack(**styles.PACK_TITLE)
        while True:
            date = simpledialog.askstring("Insert date", "Insert date(DD-MM-YYYY):")
            if date is None:
                return None
            if self.manager.isValid_date(date):
                return date
            else:
                tk.messagebox.showerror("Invalid date", "Invalid date")
        
    def finish_scanInput(self):
        if self.productList != []:
            print(self.productList)
            self.manager.logger.info("Done registering products:")
            self.manager.logger.info(self.productList)
            self.manager.register_productList(self.productList)
            listToShow = "Products registered: "
            for l in self.productList:
                listToShow += l[0] + ", "
            self.productList.clear()
            tk.messagebox.showinfo("Registered", listToShow)
        self.manager.show_frame(HomeScreen)

    def hide_frame_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        


        
