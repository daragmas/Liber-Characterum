from tkinter import *
from tkinter import ttk


class CharacterSelection:
    def __init__(self, root):
        self.root = root

    def create(self):
        characterselection = ttk.Frame(self.root)
        samplechars = ["Char1", "Char2", "Char3"]
        for i in range(len(samplechars)):
            charbutton = Button(characterselection, text=samplechars[i])
            charbutton.grid(column=i, row=0)

        characterselection.grid()
