from tkinter import *
from tkinter import ttk
from Toolbar import *
from CharacterSelection import *
from Information import *
from PageButtons import *


root = Tk()
root.title("Liber Characterum")
root.geometry("1200x600")

# Toolbar
tb = Toolbar(root)
tb.create()

# Character Selection
charsel = CharacterSelection(root)
charsel.create()

# Information Page
info = Information(root)
info.create()


# Page Buttons
pgb = PageButtons(root)
pgb.create()

root.mainloop()
