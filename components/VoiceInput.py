import tkinter as tk
import speech_recognition as sr
import threading

from Controller import Controller
from style import styles

class VoiceInput(tk.Frame):   
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)

        self.recognizer = sr.Recognizer()
        
        self.start_listeting_button = tk.Button(self, text = "START LISTENING", command = lambda : self.start_voiceInput(), **styles.STYLE, activebackground = styles.BACKGROUND, activeforeground = styles.TEXT)
        self.label_listening = tk.Label(self, text="Listening...", **styles.STYLE)
        
        self.timeout = 4

        self.init_widgets()

    def init_widgets(self):
        self.start_listeting_button.pack(
            **styles.PACK_BUTTON
        )     
        
    
    def start_voiceInput(self):
     self.start_listeting_button.pack_forget()
     self.label_listening.pack(**styles.PACK_TITLE)
     # [Threading] - Ensure button is hidden and label is visible
     threading.Thread(target= self.listen_product).start() 

    def listen_product(self):
     try:
          with sr.Microphone() as source:
              print("Listening")
              self.recognizer.adjust_for_ambient_noise(source)
              audio = self.recognizer.listen(source, timeout = self.timeout)

          text = self.recognizer.recognize_google(audio, language='es-ES')
          self.show_result(text)
          return text
     
     except sr.WaitTimeoutError:
          print("TIMEOUT, be faster next time!")
          self.listen_product()
     except sr.UnknownValueError:
          print("Didn't get that")
          self.listen_product()
     except sr.RequestError as e:
          print("Error calling Google Search Speech Recognition; {0}".format(e))
    def show_result(self, product):
        print("AQUI TOY")
        if product != "":
              self.label_listening.pack_forget()
              self.label_product = tk.Label(self, text="Product: " + product).pack(**styles.PACK_TITLE)
              self.confirm_button = tk.Button(self, text="Confirm", command=lambda:self.confirm_product(product), **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_RIGTH)
              self.say_again = tk.Button(self, text="Say again", command=self.start_voiceInput, **styles.STYLE).pack(**styles.PACK_BUTTON_MINI_LEFT)


    def confirm_product(self, product):
        print(product, "hola")
        #Registrar producto.