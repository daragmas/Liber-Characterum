from tkinter import *
from tkinter import ttk


class CharacterSelection:
    def __init__(self, root, characters):
        self.root = root
        self.characters = characters

    def create(self):
        character_selection = ttk.Frame(self.root, relief="groove")
        # samplechars = ["Char1", "Char2", "Char3"]
        for character in self.characters:
            char_button = Button(character_selection, text=character["name"])
            char_button.grid(row=0)

        character_selection.grid(row=1, column=0, padx=5, pady=5)
