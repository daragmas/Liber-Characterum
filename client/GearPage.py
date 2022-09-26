from tkinter import *
from tkinter import ttk


class GearPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.selected = {}

    def gear_list(self):
        gear_frame = LabelFrame(self.root, text="Gear")

        for item in self.character['equipment']['gear']:
            gear_subframe = Frame(gear_frame)
            gear_name = Label(gear_subframe, text=item['name'], justify=LEFT)
            gear_quality = Label(gear_subframe, text=f'Quality: {item["quality"]}')
            gear_quantity = Label(gear_subframe, text=f'Quantity: {item["quantity"]}')
            gear_name.grid(row=0, column=0, sticky=W)
            gear_name.bind(sequence='<Button>', func=lambda e: self.selected_item(item))
            gear_quality.grid(row=0, column=1)
            gear_quantity.grid(row=0, column=2, stick=E)
            gear_subframe.grid()

        gear_frame.grid(row=0, column=0, sticky=W)

    def selected_item(self, item):
        print(item["name"])
        selected_item_frame = LabelFrame(self.root, text="Info")

        selected_item_frame.grid(row=0, column=1)

    def create(self):
        self.gear_list()
