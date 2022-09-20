from tkinter import *
from tkinter import ttk


class Information:
    def __init__(self, root):
        self.root = root

    def create(self):
        infoframe = ttk.Frame(self.root, width=1200, height=400, relief="groove")
        infoframe.grid()
