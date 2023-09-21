import tkinter as tk
import requests
import libcamera
import subprocess

from style import styles
from tkinter import simpledialog
from screens.HomeScreen import HomeScreen
from pyzbar.pyzbar import decode
from PIL import Image
class ScanInput(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)        

        self.productList = []
        self.start_scanning_button = tk.Button(self, text="SCAN PRODUCT", command=lambda: self.start_scanInput()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.finish_scanInput_button = tk.Button(self, text="FINISH", command=lambda: self.finish_scanInput()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.label_scanning = tk.Label(
            self, text="Scanning...", **styles.STYLE_NP)
        self.insert_date = tk.Label(self, text="Insert Date:", **styles.STYLE_NP)
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

    def scan_product(self):
        self.manager.logger.info("Start Scanning product")
        barcode  = 0
        
        barcode = self.read_barcode(0)

        product_name = self.get_product_name(barcode)

        self.show_result(product_name)

    def read_barcode(self, cont):
            if(cont > 3):
                return 0
            barcode = 0
            process = subprocess.Popen(['libcamera-still', '-f', '-t', '2000', '-o', 'barcode.png'])
            process.wait()
            image = Image.open('barcode.png')
            result = decode(image)
            if result:
                barcode = result.data.decode("utf-8")
            else:
                cont += 1
                barcode = self.read_barcode(cont)                     
            
            self.manager.logger.info("Barcode scanned: ", barcode)
            return barcode             
    
    def get_product_name(self, productId):  # Get product name by barcodeNumber [Using OpenFoodFacts API]
         self.manager.logger.info("OpenFoodApi request productId:"+productId)
         url = 'https://world.openfoodfacts.org/api/v0/product/' + productId + '.json'
         params = {'fields': 'product_name'}
         
         try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
              data = response.json()
              product_name = data['product']['product_name']
              self.manager.logger.info('Product_name: ', product_name)
              ## Posible lógica de cambio de nombre que decida el usuario              
              return product_name
            else:
                self.manager.logger.info('OpenFoodFacts_API_request failed: ' + response.status_code)
                return "fail"
         except Exception as ex: 
            self.manager.logger.info(ex)


    def show_result(self, product):
        if product != "":
              self.label_scanning.pack_forget()
              self.label_product = tk.Label(self, text="Product: " + product).pack(**styles.PACK_TITLE)
              self.confirm_button = tk.Button(self, text="Confirm", command=lambda:self.confirm_product(product, False), **styles.STYLE_NP).pack(**styles.PACK_BUTTON)
              self.say_again_button = tk.Button(self, text="Scan again", command=self.start_scanInput, **styles.STYLE_NP).pack(**styles.PACK_BUTTON_MINI_LEFT)
              self.with_date_button = tk.Button(self, text="Add Expiry Date", command=lambda:self.confirm_product(product, True), **styles.STYLE_NP).pack(**styles.PACK_BUTTON_MINI_RIGTH)


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
            date = simpledialog.askstring("Insert date", "Insert date(DD-MM-YYYY):", parent=self)
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
        


        
