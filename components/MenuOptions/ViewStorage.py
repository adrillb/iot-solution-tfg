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
        self.init_widgets()

    def init_widgets(self):
        
        #Botón Nueva compra
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

        

