from tkinter import *
from tkinter import ttk


class CharacterSelection:
    def __init__(self, root):
        self.root = root

    def create(self):
        characterselection = ttk.Frame(self.root, relief="groove")
        samplechars = ["Char1", "Char2", "Char3"]
        for i in range(len(samplechars)):
            charbutton = Button(characterselection, text=samplechars[i])
            charbutton.grid(column=i, row=0)

        characterselection.grid(row=1, column=0, padx=5, pady=5)
