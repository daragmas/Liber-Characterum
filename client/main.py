from tkinter import *
from tkinter import ttk
from Toolbar import *
from CharacterSelection import *
from Information import *

# TODO: import ttk Styles


def set_character(character):
    info = Info(root, character)
    root.after(0, info.create())


root = Tk()
root.title("Liber Characterum")
root.geometry("1200x600")

# Toolbar
tb = Toolbar(root, set_character)
tb.create()

# TODO: Replace CharacterSelection functionality with ttk.Notebook tabs
# Character Selection
# charsel = CharacterSelection(root, characters=character_list)
# charsel.create()

root.mainloop()
