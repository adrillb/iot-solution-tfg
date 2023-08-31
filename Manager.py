import tkinter as tk
import logging

from screens.HomeScreen import HomeScreen
from screens.NewPurchaseScreen import NewPurchaseScreen
from screens.ViewStorageScreen import ViewStorageScreen
from screens.VoiceInputScreen import VoiceInputScreen
from screens.ScanInputScreen import ScanInputScreen
from screens.TypeInputScreen import TypeInputScreen
from screens.RecipeIdeasScreen import RecipeIdeasScreen
from datetime import datetime
from solutionAlerts.Alerts import Alerts
from solutionDB.DataBase import DataBase
from style import styles


class Manager(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("IOT-SOLUTION")        
        self.attributes('-fullscreen', True)
        self.dataBase = DataBase()
        self.alerts = Alerts(self)
        self.logger = self.setUpLogger()
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
        
        screens =(HomeScreen, NewPurchaseScreen, ViewStorageScreen, VoiceInputScreen, ScanInputScreen, TypeInputScreen, RecipeIdeasScreen,)
        for F in screens:
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky = tk.NSEW)

        self.show_frame(HomeScreen)

    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()
        self.logger.info("Raise "+str(container))

###########################################################################################################################################################################################################################

     #MAIN MENU METHODS#

    def new_purchase(self):     #Register products from new purchase
         self.show_frame(NewPurchaseScreen)                  

    def show_stored_products(self):         
         self.show_frame(ViewStorageScreen)
     
    def show_recipe_ideas(self):         
         self.show_frame(RecipeIdeasScreen)

         
     #NEW_PURCHASE METHODS#
    def voice_input(self):
         self.show_frame(VoiceInputScreen)                  

    def type_input(self):
         self.show_frame(TypeInputScreen)

    def scan_product(self):
         self.show_frame(ScanInputScreen)                                       


    def register_productList(self, productList):         
         for product in productList:
              data = self.toJson(product)
              self.dataBase.insert_product(data)
              self.logger.info(product[0]+" - "+ product[1] +" insertado.")


    def toJson(self, product):
         return {
              "product_name" : product[0],
              "expiry_date" : product[1]
         }              
            
    def isValid_date(self, date):        
        try:
            datetime.strptime(date, "%d-%m-%Y")
            return True
        except ValueError:
            return False
        
    def setUpLogger(self):    
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(message)s')
        file_handler = logging.FileHandler('app.log')
        file_handler.setLevel(logging.INFO)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
        return logger
    

                     
