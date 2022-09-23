from tkinter import *
from tkinter import ttk


class PowersPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def create(self):
        test = Label(self.root, text="Powers")
        test.pack()