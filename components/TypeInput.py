import tkinter as tk

from style import styles
from tkinter import simpledialog
from screens.HomeScreen import HomeScreen


class TypeInput(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)        

        self.productList = []

        self.start_typing_button = tk.Button(self, text="TYPE PRODUCT", command=lambda: self.start_typeInput()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.finish_typeInput_button = tk.Button(self, text="FINISH", command=lambda: self.finish_voiceInput()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT) 

        self.label_insert_product = tk.Label(self, text="Insert Product:", **styles.STYLE_NP) 
        self.label_insert_date = tk.Label(self, text="Insert Date:", **styles.STYLE_NP)

        self.accept_productName_button = tk.Button(self, text="ACCEPT", command=lambda: self.accept_type()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)                
        self.cancel_button = tk.Button(self, text="CANCEL", command=lambda: self.cancel_type()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)                
        self.confirm_button = tk.Button(self, text="CONFIRM", command=lambda: self.cancel_type()
        ,**styles.STYLE_NP, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)        

        self.product_entry = tk.Entry(self)
        self.date_entry = tk.Entry(self)

        self.init_widgets()

    def init_widgets(self):
        self.hide_frame_widgets()
        self.start_typing_button.pack(
            **styles.PACK_BUTTON
        )
        self.finish_typeInput_button.pack(
            **styles.PACK_BUTTON
        )

    def start_typeInput(self):
        self.manager.logger.info("Start Typing product")   
        self.hide_frame_widgets()  
        self.label_insert_product.pack()  
        self.product_entry.pack()
        self.accept_productName_button.pack(**styles.PACK_BUTTON_MINI_RIGTH)
        self.cancel_button.pack(**styles.PACK_BUTTON_MINI_LEFT)             
          
    def accept_type(self):
        productName = self.product_entry.get()
        if not productName:
            tk.messagebox.showinfo("Warning", "Please, insert product name.")
        else:
            self.product_entry.delete(0, tk.END)
            self.hide_frame_widgets()
            self.show_result(productName)        

    def cancel_type(self):
        self.init_widgets()

    def show_result(self, product):
        self.manager.logger.info("User typed: " + str(product))
        if product != "":              
              self.label_product = tk.Label(self, text="Product: " + product).pack(**styles.PACK_TITLE)
              self.confirm_button = tk.Button(self, text="Confirm", command=lambda:self.confirm_product(product, False), **styles.STYLE_NP).pack(**styles.PACK_BUTTON)
              self.say_again_button = tk.Button(self, text="Type again", command=self.start_typeInput, **styles.STYLE_NP).pack(**styles.PACK_BUTTON_MINI_LEFT)
              self.with_date_button = tk.Button(self, text="Add Expiry Date", command=lambda:self.confirm_product(product, True), **styles.STYLE_NP).pack(**styles.PACK_BUTTON_MINI_RIGTH)


    def confirm_product(self, product_name, hasDate):
        #Registrar producto.
        productList = []
        expiry_date = "00-00-0000"
        
        if hasDate:            
            print("preguntamos fecha")
            expiry_date = self.ask_date()
        if expiry_date is not None:                                
            product = (product_name, expiry_date)
            productList.append(product)
            self.productList.append(product)
            
        self.hide_frame_widgets()
        self.init_widgets()

    def ask_date(self):
        self.hide_frame_widgets()
        self.label_insert_date.pack(**styles.PACK_TITLE)
        while True:
            date = simpledialog.askstring("Insert date", "Insert date(DD-MM-YYYY):", parent=self)
            if date is None:
                return None
            if self.manager.isValid_date(date):
                return date
            else:
                tk.messagebox.showerror("Invalid date", "Invalid date, remember format must be (DD-MM-YYYY)")
        
    def finish_voiceInput(self):
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
        