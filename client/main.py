from tkinter import *
from tkinter import ttk
from Toolbar import *
from CharacterSelection import *
from Information import *

# TODO: import ttk Styles


def set_character(character):
    try:
        root.winfo_children()[1].destroy()
    except IndexError:
        pass

    info = Info(root, character)
    root.after(0, info.create())


root = Tk()
root.title("Liber Characterum")
root.geometry("1200x600")

# Toolbar
tb = Toolbar(root, set_character)
tb.create()


root.mainloop()
