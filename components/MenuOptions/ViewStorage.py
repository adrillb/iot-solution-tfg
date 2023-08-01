import tkinter as tk

from Controller import Controller
from style import styles

class ViewStorage(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = styles.BACKGROUND
        )
        self.productList = tk.Listbox(self, width=20)
        self.init_widgets()

    def init_widgets(self):
        
        #Botón Nueva compra
        tk.Button(
            self,
            text = "VIEW PRODUCTS",
            command = lambda : self.show_products(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        tk.Button(
            self,
            text = "CLEAR DATA",
            command = lambda : print("PLEASE"), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        tk.Button(
            self,
            text = "BACK",
            command = lambda : print("PLEASE"), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

    def show_products(self):
        listbox = tk.Listbox(self, width=30)
        
        for i in range(10):
            listbox.insert(tk.END, "Holi")
            listbox.insert(tk.END, "Holu")
        listbox.pack()
        #products = self.manager.dataBase.read_dataBase()