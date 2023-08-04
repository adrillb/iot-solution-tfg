import tkinter as tk
import speech_recognition as sr
import time

from Controller import Controller
from style import styles
from tkinter import simpledialog
from screens.HomeScreen import HomeScreen


class VoiceInput(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background=styles.BACKGROUND)
        self.recognizer = sr.Recognizer()

        self.productList = []

        self.start_listeting_button = tk.Button(self, text="SAY PRODUCT", command=lambda: self.start_voiceInput(
        ), **styles.STYLE, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.finish_voiceInput_button = tk.Button(self, text="FINISH", command=lambda: self.finish_voiceInput(
        ), **styles.STYLE, activebackground=styles.BACKGROUND, activeforeground=styles.TEXT)
        self.label_listening = tk.Label(
            self, text="Listening...", **styles.STYLE)
        self.insert_date = tk.Label(self, text="Insert Date:", **styles.STYLE)
        self.timeout = 5

        self.init_widgets()

    def init_widgets(self):
        self.start_listeting_button.pack(
            **styles.PACK_BUTTON
        )
        self.finish_voiceInput_button.pack(
            **styles.PACK_BUTTON
        )

    def start_voiceInput(self):
     self.hide_frame_widgets()
     self.label_listening.pack(**styles.PACK_TITLE)
     self.update()
     #time.sleep(0.5)
     product = self.listen_product()
     self.show_result(product)

    def listen_product(self):
        self.manager.logger.info("Start Listening product")
        audio = "x"
        while True:
            with sr.Microphone() as source:
                print("Listening")
                self.recognizer.adjust_for_ambient_noise(source)
                try:
                    audio = self.recognizer.listen(source, timeout=self.timeout)
                    print("processing...")
                except sr.WaitTimeoutError:
                    print("TIMEOUT, be faster next time!")  
                    self.manager.logger.info("Timeout reached")  
                    tk.messagebox.showinfo("TryAgain", "Didn't get that, repeat please.")                
            if audio != "x":
                try:
                    print("GoogleRecognition...")
                    #Good Internet Connection
                    text = self.recognizer.recognize_google(audio, language='es-ES')          
                    #Poor Internet Connection
                    #text = self.recognizer.recognize_sphinx(audio, language='es-ES')
                    if text is not None:              
                        break
                except sr.UnknownValueError:
                    print("Didn't get that")
                    self.manager.logger.info("Did not recognize audio")
                    self.listen_product()
                except sr.RequestError as e:
                    print("Error calling Google Search Speech Recognition; {0}".format(e))
                    self.manager.logger.info("Error calling Google Search Speech Recognition; {0}".format(e))
        return text  

    def show_result(self, product):
        self.manager.logger.info("Audio recognized: " + product)
        if product != "":
              self.label_listening.pack_forget()
              self.label_product = tk.Label(self, text="Product: " + product).pack(**styles.PACK_TITLE)
              self.confirm_button = tk.Button(self, text="Confirm", command=lambda:self.confirm_product(product, False), **styles.STYLE).pack(**styles.PACK_BUTTON)
              self.say_again_button = tk.Button(self, text="Say again", command=self.start_voiceInput, **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_LEFT)
              self.with_date_button = tk.Button(self, text="Add Expiry Date", command=lambda:self.confirm_product(product, True), **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_RIGTH)


    def confirm_product(self, product_name, hasDate):
        #Registrar producto.
        productList = []
        expiry_date = "00-00-0000"
        
        if hasDate:
            #ask for date
            print("preguntamos fecha")
            expiry_date = self.ask_date()

        product = (product_name, expiry_date)
        productList.append(product)
        self.productList.append(product)
        
        self.hide_frame_widgets()
        self.init_widgets()

    def ask_date(self):
        self.hide_frame_widgets()
        self.insert_date.pack(**styles.PACK_TITLE)
        while True:
            date = simpledialog.askstring("Insert date", "Insert date(DD-MM-YYYY):")
            if date is None:
                return None
            if self.manager.isValid_date(date):
                return date
            else:
                tk.messagebox.showerror("Invalid date", "Invalid date")
        
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
        