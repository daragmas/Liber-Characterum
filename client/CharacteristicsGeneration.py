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


class CharacteristicsGeneration:
    def __init__(self, characteristics_frame, new_character, set_characteristics, modifiers, update_mods):
        self.characteristics_frame = characteristics_frame
        self.new_character = new_character
        self.modifiers = modifiers
        self.characteristics = {characteristic: {"base": 0, "modifiers": {}, 'final': 0} for characteristic in characteristics_bc}
        self.set_characteristics = set_characteristics
        self.update_modifiers = update_mods

    def change_rating(self, characteristic, value, index):
        self.characteristics[characteristic]["base"] = int(value)
        self.modifiers = self.update_modifiers()
        pp(self.modifiers)
        self.calculate_final(characteristic, index)
        # TODO: Update characteristic values when modifiers are updated

    def roll_stats(self):
        for characteristic in characteristics_bc:
            if characteristic == 'infamy':
                self.characteristics[characteristic]['base'] = random.randint(1, 5)
                self.characteristics[characteristic]['modifiers'] = {'race': 0}
            elif characteristic == 'corruption' or characteristic == 'wounds':
                self.characteristics[characteristic]['base'] = 0
                self.characteristics[characteristic]['modifiers'] = {'race': 0}
            else:
                self.characteristics[characteristic]['base'] = random.randint(2, 20)
                self.characteristics[characteristic]['modifiers'] = {'race': self.modifiers['race']}
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
        if characteristic == 'infamy':
            total_modifier = 19
        elif characteristic == 'corruption' or characteristic == 'wounds':
            total_modifier = 0
        else:
            total_modifier = self.modifiers['race']

        for key, value in self.modifiers['archetype'].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Pride"].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Disgrace"].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Motivation"].items():
            if key == characteristic:
                total_modifier += int(value)

        # print(characteristic, total_modifier)

        modifier_label = Label(self.characteristics_frame,
                               text=total_modifier,
                               width=5)
        modifier_label.grid(row=index, column=2)

    def calculate_final(self, characteristic, index):
        # TODO: pass modifiers from show_modifiers to calculate_final

        if characteristic == 'infamy':
            total_modifier = 19
        elif characteristic == 'corruption' or characteristic == 'wounds':
            total_modifier = 0
        else:
            total_modifier = self.modifiers['race']

        for key, value in self.modifiers['archetype'].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Pride"].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Disgrace"].items():
            if key == characteristic:
                total_modifier += int(value)

        for key, value in self.modifiers["Motivation"].items():
            if key == characteristic:
                total_modifier += int(value)

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
