from tkinter import *
from tkinter import ttk


class EquipmentPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def create(self):
        test = Label(self.root, text="Equipment")
        test.pack()
