import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from NewCharacter import *
import json


class Toolbar:
    def __init__(self, root, character_setter):
        self.root = root
        self.character_setter = character_setter

    def make_new_character(self):
        new_character = NewCharacter(root=self.root)
        new_character.create()
        # Save choices and info to dictionary
        # Save dictionary as JSON file in characters folder
        # self.character_setter(new_character_json)
        pass

    def open_character(self):
        character_file = tkinter.filedialog.askopenfilename(initialdir='./characters',
                                                            title='Select Character')
        with open(file=character_file, mode='r') as char_file:
            character_json = json.load(char_file)
            self.character_setter(character_json)

    def save_character(self):
        pass

    def create(self):
        toolbar = ttk.Frame(self.root, relief="groove")

        new_character = Button(toolbar, text="New", command=self.make_new_character)
        open_character = Button(toolbar, text="Open", command=self.open_character)
        save_character = Button(toolbar, text="Save", command=self.save_character)

        new_character.grid(row=0, column=0)
        open_character.grid(row=0, column=1)
        save_character.grid(row=0, column=2)

        toolbar.grid(row=0, column=0, padx=5, pady=5, sticky=N, columnspan=5)
