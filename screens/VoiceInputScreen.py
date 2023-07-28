import tkinter as tk

from style import styles
from components.VoiceInput import VoiceInput

class VoiceInputScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text = "IOT-SOLUTION",
            justify = tk.CENTER,
            **styles.STYLE
        ).pack(
            **styles.PACK_TITLE
        )

        VoiceInput(
            self,
            self.manager,            
        ).pack(
            **styles.PACK_TITLE
        )