
import tkinter as tk

BACKGROUND = "#121212"
COMPONENT ="#363636"
TEXT = "#84C9FB"
FONT = ("Arial", 16)

STYLE = {
    "bg" : COMPONENT,
    "fg" : TEXT,
    "font" : FONT
}

PACK_TITLE = {
    "side" : tk.TOP,
    "fill" : tk.BOTH,
    "expand" : True,
    "padx" : 1,
    "pady" : 1
}

PACK_BUTTON = {
    "side" : tk.TOP,
    "fill" : tk.BOTH,
    "expand" : True,
    "padx" : 22,
    "pady" : 11
}

PACK_BUTTON_MINI_RIGTH = {
    "side" : tk.RIGHT,
    "fill" : tk.BOTH,
    "expand" : True,
    "padx" : 22,
    "pady" : 11
}

PACK_BUTTON_MINI_LEFT = {
    "side" : tk.LEFT,
    "fill" : tk.BOTH,
    "expand" : True,
    "padx" : 22,
    "pady" : 11
}

PACK_BUTTON_MINI_BOTTOM = {
    "side" : tk.BOTTOM,
    "fill" : tk.BOTH,
    "expand" : True,
    "padx" : 22,
    "pady" : 11
}

PACK_LISTBOX_RIGHT = {
    "side" : tk.RIGHT,
    "expand" : True
}
PACK_LISTBOX_LEFT = {
    "side" : tk.LEFT,
    "expand" : True
}