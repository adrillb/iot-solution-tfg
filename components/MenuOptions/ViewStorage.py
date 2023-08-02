import tkinter as tk

from style import styles
from screens.HomeScreen import HomeScreen

class ViewStorage(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = styles.BACKGROUND
        )
        self.productList = tk.Listbox(self, **styles.STYLE)
        self.expiryDateList = tk.Listbox(self, **styles.STYLE)

        self.viewProducts_button = tk.Button(self, text = "VIEW PRODUCTS", command = lambda : self.show_products()
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.clearData_button = tk.Button(self, text = "CLEAR DATA", command = lambda : print("PLEASE")
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.back_button = tk.Button(self, text = "BACK", command = lambda : self.manager.show_frame(HomeScreen)
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)

        self.init_widgets()

    def init_widgets(self):
        self.hide_frame_widgets()
        self.viewProducts_button.pack(**styles.PACK_BUTTON)
        self.clearData_button.pack(**styles.PACK_BUTTON)
        self.back_button.pack(**styles.PACK_BUTTON)
    
    def show_products(self):
        data = self.manager.dataBase.read_products()
        self.hide_frame_widgets()
        self.productList.pack(**styles.PACK_LISTBOX_LEFT)
        self.expiryDateList.pack(**styles.PACK_LISTBOX_RIGHT)
        back_button = tk.Button(self, text = "BACK", command = lambda : self.init_widgets()
                            ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT).pack(**styles.PACK_BUTTON_MINI_BOTTOM)
        
        if data:
            for i, record in enumerate(data.values(), start=1):
                self.productList.insert(tk.END, record.get("product_name"))
                self.expiryDateList.insert(tk.END, record.get("expiry_date"))
        
        #products = self.manager.dataBase.read_dataBase()

    
    def hide_frame_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()