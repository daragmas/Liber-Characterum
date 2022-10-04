import random
from pprint import pp
from tkinter import *
from tkinter import ttk

characteristics_bc = [
    "weapon skill",
    "ballistic skill",
    "strength",
    "toughness",
    "agility",
    "intelligence",
    "perception",
    "willpower",
    "fellowship",
    "infamy",
    "corruption",
    "wounds"
]

# TODO: Figure out how to pass modifiers from archetype to show_modifiers

class CharacteristicsGeneration:
    def __init__(self, characteristics_frame, new_character, set_characteristics):
        self.characteristics_frame = characteristics_frame
        self.characteristics = {characteristic: {"base": 0, "modifiers": {}, 'final': 0} for characteristic in characteristics_bc}
        self.new_character = new_character
        self.set_characteristics = set_characteristics

    def change_rating(self, characteristic, value, index):
        print('characteristic', characteristic, 'value', value)
        self.characteristics[characteristic]["base"] = int(value)
        # pp(self.characteristics[characteristic])
        self.calculate_final(characteristic, index)

    def roll_stats(self):
        # TODO: Move racial mods to show_modifiers?
        if self.new_character['race'] == 'Mortal':
            characteristics_mod = 25
        elif self.new_character['race'] == 'Chaos Space Marine':
            characteristics_mod = 30
        else:
            characteristics_mod = 0
        for characteristic in characteristics_bc:
            self.characteristics[characteristic]['base'] = random.randint(2, 20) + characteristics_mod
        self.characteristics["infamy"]['base'] = random.randint(1, 5) + 19
        self.characteristics["corruption"]['base'], self.characteristics["wounds"]['base'] = 0, 0
        # pp(self.characteristics)
        self.characteristics_table()

    def characteristic_row(self, characteristic, index):
        characteristic_label = Label(self.characteristics_frame, text=characteristic.title())
        characteristic_label.grid(row=index, column=0, sticky=W)
        characteristic_rating = IntVar()
        characteristic_rating.set(self.characteristics[characteristic]["base"])
        characteristic_value = Entry(self.characteristics_frame, textvariable=characteristic_rating, width=5)
        characteristic_value.grid(row=index, column=1)
        characteristic_value.bind("<KeyRelease>",
                                  lambda e: self.change_rating(characteristic, characteristic_value.get(), index))

    def show_modifiers(self, characteristic, index):
        # if self.new_character['race'] == 'Mortal':
        #     characteristics_mod = 25
        # elif self.new_character['race'] == 'Chaos Space Marine':
        #     characteristics_mod = 30
        # else:
        #     characteristics_mod = 0
        # self.characteristics[characteristic]['modifiers'] = {**self.characteristics[characteristic]['modifiers'], "race": {
        #     "value": characteristics_mod}}
        modifier_label = Label(self.characteristics_frame, text=0, width=5)
        modifier_label.grid(row=index, column=2)

    def calculate_final(self, characteristic, index):
        total_modifier = sum([value for key, value in self.characteristics[characteristic]['modifiers'].items() if key == 'value'])
        self.characteristics[characteristic]['final'] = self.characteristics[characteristic]['base'] + total_modifier
        final_label = Label(self.characteristics_frame, text=self.characteristics[characteristic]['final'], width=5)
        final_label.grid(row=index, column=3)

        self.set_characteristics(characteristic, self.characteristics[characteristic]['final'])

    def characteristics_table(self):
        for widget in self.characteristics_frame.winfo_children():
            widget.destroy()

        Label(self.characteristics_frame, text="Characteristic").grid(row=0, column=0)
        Label(self.characteristics_frame, text="Base").grid(row=0, column=1)
        Label(self.characteristics_frame, text="Modifiers").grid(row=0, column=2)
        Label(self.characteristics_frame, text="Total").grid(row=0, column=3)

        for index, characteristic in enumerate(characteristics_bc):
            self.characteristic_row(characteristic, index+1)
            self.show_modifiers(characteristic, index+1)
            self.calculate_final(characteristic, index+1)
        roll_button = Button(self.characteristics_frame, text="Roll Characteristics", command=self.roll_stats)
        roll_button.grid(row=13, column=0, columnspan=2)

    def create(self):
        self.roll_stats()
