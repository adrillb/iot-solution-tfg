import tkinter as tk

from style import styles
from components.MenuOptions.RecipeIdeas import RecipeIdeas

class RecipeIdeasScreen(tk.Frame):
    def __init__(self, parent, manager):
        super().__init__(parent)
        self.manager = manager
        self.configure(background = styles.BACKGROUND)
        self.init_widgets()

    def init_widgets(self):   
        tk.Label(
            self,
            text = "RECIPE IDEAS",
            justify = tk.CENTER,
            **styles.STYLE_TITLE_RI
        ).pack(
            **styles.PACK_TITLE
        )

        RecipeIdeas(
            self,
            self.manager,            
        ).pack(
            **styles.PACK_TITLE
        )