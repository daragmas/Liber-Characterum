from tkinter import *
from tkinter import ttk


class GearPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def create(self):
        test = Label(self.root, text="Gear")
        test.pack()
