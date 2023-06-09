import tkinter as tk

from Controller import Controller
from style import styles

class MainMenu(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = styles.BACKGROUND
        )
        self.init_widgets()

    def init_widgets(self):                

        #Botón Nueva compra
        tk.Button(
            self,
            text = "NUEVA COMPRA",
            command = lambda : self.manager.new_purchase(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Ideas Recetas
        tk.Button(
            self,
            text = "STORED PRODUCTS",
            command = lambda : self.manager.show_stored_products(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Consultar estado
        tk.Button(
            self,
            text = "RECIPE IDEAS",
            command = lambda : print("RECIPE IDEAS"), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

