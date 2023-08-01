import tkinter as tk

from screens.HomeScreen import HomeScreen
from style import styles

class NewPurchase(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = styles.BACKGROUND
        )
        self.init_widgets()

    def init_widgets(self):
        
        #BOTONES
        #Botón Entrada de voz
        tk.Button(
            self,
            text = "VOICE INPUT PRODUCTS",
            command = lambda : self.manager.voice_input(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Escribir
        tk.Button(
            self,
            text = "TYPE PRODUCTS",
            command = lambda : self.manager.voice_input(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Escanear
        tk.Button(
            self,
            text = "SCAN PRODUCT BARCODES",
            command = lambda : self.manager.scan_product(), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )

        #Botón Finalizar
        tk.Button(
            self,
            text = "FINISH",
            command = lambda : self.manager.show_frame(HomeScreen), #Funionalidad
            **styles.STYLE,
            activebackground = styles.BACKGROUND,
            activeforeground = styles.TEXT            
        ).pack(
            **styles.PACK_BUTTON
        )
