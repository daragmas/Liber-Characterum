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

aboutFrame = LabelFrame(root, text='About', width=1200, pady=10, padx=10)
headerText = "Welcome to Liber Characterum!"
subHeaderText = "A character creation application for Warhammer 40k RPGs"
aboutText = "This a Python project built by Nathaniel Wolf. " \
            "Currently, the only system supported by this application is Black Crusade."
instructions = "To make a new character, click New. To open an existing character, click Open."
disclaimer = "Materials referenced for this application are copyrighted property of Games Workshop and " \
             "Fantasy Flight Games."

Label(aboutFrame, text=headerText).pack(side=TOP)
Label(aboutFrame, text=subHeaderText).pack(side=TOP)
Label(aboutFrame, text=aboutText).pack(side=TOP)
Label(aboutFrame, text=instructions).pack(side=TOP)
Label(aboutFrame, text=disclaimer).pack(side=BOTTOM)
aboutFrame.grid(sticky='nsew')

root.mainloop()
