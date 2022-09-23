from tkinter import *
from tkinter import ttk
from Information import *


class PageButtons(Info):
    def __init__(self, root):
        super().__init__(root)
        # root = root
        # self.selector = selector

    def set_selector(self, choice):
        super.selector = choice

    def create(self):
        pagebuttons = ttk.Frame(self.root, relief="groove")

        characteristicsbutton = ttk.Button(pagebuttons,
                                           text="Characteristics",
                                           command=self.set_selector("characteristics"))
        traitsandtalentsbutton = ttk.Button(pagebuttons,
                                            text="Traits and Talents",
                                            command=self.set_selector("traits_talents"))
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

        pagebuttons.grid(row=3, column=0, padx=5, pady=5)
