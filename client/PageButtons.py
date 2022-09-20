from tkinter import *
from tkinter import ttk


class PageButtons:
    def __init__(self, root):
        self.root = root

    def create(self):
        pagebuttons = ttk.Frame(self.root)
        characteristicsbutton = ttk.Button(pagebuttons, text="Characteristics")
        traitsandtalentsbutton = ttk.Button(pagebuttons, text="Traits and Talents")
        equipmentbutton = ttk.Button(pagebuttons, text="Equipment")
        gearbutton = ttk.Button(pagebuttons, text="Gear")
        powersbutton = ttk.Button(pagebuttons, text="Powers")
        advancementbutton = ttk.Button(pagebuttons, text="Advancement")

        characteristicsbutton.grid(column=0, row=0)
        traitsandtalentsbutton.grid(column=1, row=0)
        equipmentbutton.grid(column=2, row=0)
        gearbutton.grid(column=3, row=0)
        powersbutton.grid(column=4, row=0)
        advancementbutton.grid(column=5, row=0)

        pagebuttons.grid()
