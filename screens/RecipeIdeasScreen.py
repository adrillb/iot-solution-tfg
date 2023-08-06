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
        RecipeIdeas(
            self,
            self.manager,            
        ).pack(
            **styles.PACK_TITLE
        )