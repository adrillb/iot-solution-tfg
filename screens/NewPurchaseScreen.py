import tkinter as tk

from style import styles
from components.MenuOptions.NewPurchase import NewPurchase

class NewPurchaseScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):
        tk.Label(
            self,
            text = "NEW PURCHASE",
            justify = tk.CENTER,
            **styles.STYLE_TITLE_NP
        ).pack(
            **styles.PACK_TITLE
        )

        NewPurchase(
            self,
            self.manager,            
        ).pack(
            **styles.PACK_TITLE
        )