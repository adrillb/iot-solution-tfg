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
        
        articlesList = []

        #Botón Nueva compra
        tk.Button(
            self,
            text = "NUEVA COMPRA",
            command = lambda : self.manager.new_purchase(articlesList), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Ideas Recetas
        tk.Button(
            self,
            text = "IDEAS RECETAS",
            command = lambda : print("IDEAS RECETAS"), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Consultar estado
        tk.Button(
            self,
            text = "CONSULTAR ESTADO",
            command = lambda : print("CONSULTAR ESTADO"), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

