
import tkinter as tk


BACKGROUND = "#121212"
COMPONENT ="#363636"


TEXT = "#84C9FB"
TEXT_NP = "#3DD697"
TEXT_ST = "#7D3C98"
TEXT_RI = "#FF8A33"

FONT = ("Trip Sans", 16)
CURSOR = "cross"
RELIEF = "groove"

STYLE = {
    "bg" : COMPONENT,
    "fg" : TEXT,
    "font" : FONT,
    "cursor" : CURSOR
}

STYLE_TITLE = {
    "bg" : TEXT,
    "fg" : BACKGROUND,
    "font" : FONT,
    "cursor" : CURSOR

}

STYLE_NP = {
    "bg" : COMPONENT,
    "fg" : TEXT_NP,
    "font" : FONT,
    "cursor" : CURSOR
}

STYLE_TITLE_NP = {
    "bg" : TEXT_NP,
    "fg" : BACKGROUND,
    "font" : FONT,
    "cursor" : CURSOR

}

STYLE_ST = {
    "bg" : COMPONENT,
    "fg" : TEXT_ST,
    "font" : FONT,
    "cursor" : CURSOR
}

STYLE_TITLE_ST = {
    "bg" : TEXT_ST,
    "fg" : BACKGROUND,
    "font" : FONT,
    "cursor" : CURSOR

}

STYLE_RI = {
    "bg" : COMPONENT,
    "fg" : TEXT_RI,
    "font" : FONT,
    "cursor" : CURSOR
}

STYLE_TITLE_RI = {
    "bg" : TEXT_RI,
    "fg" : BACKGROUND,
    "font" : FONT,
    "cursor" : CURSOR

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