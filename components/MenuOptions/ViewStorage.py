import tkinter as tk

from style import styles
from screens.HomeScreen import HomeScreen
from tkinter import PhotoImage

class ViewStorage(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(
            background = styles.BACKGROUND
        )
        #icon = PhotoImage(file="/home/adrillb/Desktop/TFG/Python/iot-solution/delete-icon")

        self.product_ids = {}
        
        self.productList = tk.Listbox(self, **styles.STYLE)        

        self.viewProducts_button = tk.Button(self, text = "VIEW PRODUCTS", command = lambda : self.show_products()
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.clearData_button = tk.Button(self, text = "CLEAR DATA", command = lambda : self.security_question()
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.back_button = tk.Button(self, text = "BACK", command = lambda : self.manager.show_frame(HomeScreen)
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        
        self.inside_back_button = tk.Button(self, text = "<", command = lambda : self.init_widgets()
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.delete_button = tk.Button(self, text="X", command=lambda : self.delete_product(self.getId())
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)

        self.confirmClearData_button = tk.Button(self, text="Confirm and delete ALL data", command=lambda : self.delete_all_products()
                                        ,**styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)        
        
        self.init_widgets()

    def init_widgets(self):
        self.hide_frame_widgets()
        self.viewProducts_button.pack(**styles.PACK_BUTTON)
        self.clearData_button.pack(**styles.PACK_BUTTON)
        self.back_button.pack(**styles.PACK_BUTTON)

    def getData(self):
        data = self.manager.dataBase.read_products()
        if data:
            for i, (id, record) in enumerate(data.items(), start=1):
                self.product_ids[i] = id
                date = record.get("expiry_date")
                if date == "00-00-0000":
                    date = "No Expiry Date"
                element = record.get("product_name") + " - " + date
                self.productList.insert(tk.END, element)  

    
    def show_products(self):  
        self.getData()                      
        self.hide_frame_widgets()
        self.productList.pack(**styles.PACK_LISTBOX_LEFT)     
        self.delete_button.pack(**styles.PACK_BUTTON)      
        self.inside_back_button.pack(**styles.PACK_BUTTON)  
        self.inside_back_button.config(text="<")               

    def getId(self):          
        id = "Error"
        index = 0
        indexes = self.productList.curselection()
        if indexes:
            index = indexes[0]               
            id = self.product_ids[index+1]                
        return [id, index]

    def delete_product(self, info):
        id = info[0]
        index = info[1]
        if id != "Error":
            self.manager.dataBase.delete_product(id)
            message = "Product '" + self.productList.get(index) + "' deleted"
            print(message)
            self.manager.logger.info(message)
            self.init_widgets()            
            
            self.productList.delete(0, tk.END)
            tk.messagebox.showinfo("Product deleted", message)  
        else:
            tk.messagebox.showinfo("Error deleting", "Select Product to delete")      

    def delete_all_products(self):
        self.getData()
        if self.product_ids:
            self.manager.logger.info("Deleting all products.")
            for i in self.product_ids:
                self.manager.dataBase.delete_product(self.product_ids.get(i-1))
                print(self.productList.get(i-1) + " deleted")
                self.manager.logger.info(self.productList.get(i-1) + " deleted")
            self.productList.delete(0, tk.END)
            tk.messagebox.showinfo("Info", "All products have been deleted.")
            self.init_widgets()

    def security_question(self):
        self.hide_frame_widgets()
        tk.messagebox.showinfo("WARNING!", "All stored products will be deleted. This action will be final.")
        self.confirmClearData_button.pack(**styles.PACK_BUTTON)
        self.inside_back_button.pack(**styles.PACK_BUTTON)
        self.inside_back_button.config(text="BACK")


    def hide_frame_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()