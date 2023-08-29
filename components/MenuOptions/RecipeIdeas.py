import tkinter as tk

from style import styles
from screens.HomeScreen import HomeScreen
from IARequest.IARequest import IARequest
from tkinter import PhotoImage

class RecipeIdeas(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager        
        self.configure(
            background = styles.BACKGROUND
        )
        #icon = PhotoImage(file="/home/adrillb/Desktop/TFG/Python/iot-solution/delete-icon")

        
        self.selected_productList = []             
        self.selected_productList_ListBox = tk.Listbox(self, **styles.STYLE_RI)
        self.productList_ListBox = tk.Listbox(self, **styles.STYLE_RI, width=25)        

        self.selectProducts_button = tk.Button(self, text = "SELECT PRODUCTS", command = lambda : self.show_products()
                                        ,**styles.STYLE_RI, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.back_button = tk.Button(self, text = "BACK", command = lambda : self.manager.show_frame(HomeScreen)
                                        ,**styles.STYLE_RI, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        
        self.inside_back_button = tk.Button(self, text = "<", command = lambda : self.init_widgets()
                                        ,**styles.STYLE_RI, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.add_button = tk.Button(self, text="ADD", command=lambda : self.add_product(self.getName())
                                        ,**styles.STYLE_RI, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.look_for_recipes_button = tk.Button(self, text="LOOK FOR RECIPES", command=lambda : self.look_for_recipes()
                                        ,**styles.STYLE_RI, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)        
        
        self.init_widgets()

    def init_widgets(self):
        self.hide_frame_widgets()
        self.selectProducts_button.pack(**styles.PACK_BUTTON)        
        self.back_button.pack(**styles.PACK_BUTTON)

    def getData(self):
        self.productList_ListBox.delete(0, tk.END)
        data = self.manager.dataBase.read_products()
        if data:
            for i, (id, record) in enumerate(data.items(), start=1):                
                date = record.get("expiry_date")
                if date == "00-00-0000":
                    date = "No Expiry Date"
                element = record.get("product_name") + " - " + date
                self.productList_ListBox.insert(tk.END, element)  

    
    def show_products(self):          
        self.getData()                      
        self.hide_frame_widgets()
        self.productList_ListBox.pack(**styles.PACK_LISTBOX_LEFT)     
        self.add_button.pack(**styles.PACK_BUTTON)      
        self.inside_back_button.pack(**styles.PACK_BUTTON)  
        self.inside_back_button.config(text="<")               

    def getName(self):          
        name = "Error"
        index = 0
        indexes = self.productList_ListBox.curselection()
        if indexes:
            index = indexes[0]               
            name = self.productList_ListBox.get(index).split(" -")[0]            
        else:
            tk.messagebox.showinfo("Warning", ("No product selected"))
        return name

    def add_product(self, name):    
        if name != "Error":
            if self.selected_productList == []:
                self.hide_frame_widgets()
                self.productList_ListBox.grid(row=0, column=0, padx=10, pady=10, rowspan=2)
                self.add_button.grid(row=0, column=1, padx=10, pady=10)
                self.inside_back_button.grid(row=1, column=1, padx=10, pady=10)
                self.look_for_recipes_button.grid(row=1, column=2, padx=10, pady=10)
                self.selected_productList_ListBox.grid(row=0, column=2, padx=10, pady=10)
                # self.productList_ListBox.pack(side=tk.LEFT)
                # self.add_button.pack(side=tk.BOTTOM)
                # self.inside_back_button.pack(side=tk.BOTTOM)
                # self.selected_productList_ListBox.pack(side=tk.RIGHT)
                # self.look_for_recipes_button.pack(side=tk.RIGHT)
            self.selected_productList_ListBox.insert(tk.END, name)                  
            self.selected_productList.append(name)            

    def look_for_recipes(self):
        if self.selected_productList != []:
            message = "Dame 5 posibles recetas con los siguientes productos: "
            for product in self.selected_productList:
                message += product + ","
            chatGpt = IARequest()
            recipes = chatGpt.chatGPT_request(message)                
            self.show_recipes(recipes)

    def show_recipes(self, recipes):
        self.hide_frame_widgets()
        message = "5 possible recipes with your products:\n" + recipes
        self.back_button.pack(**styles.PACK_BUTTON)
        text_recipes = tk.Text(self, background="#363636", foreground="#FF8A33", font=("Trip Sans", 16))
        text_recipes.pack()
        text_recipes.insert(tk.END, message)
        

    def hide_frame_widgets(self):
        for widget in self.winfo_children():
            widget.pack_forget()
            widget.grid_forget()