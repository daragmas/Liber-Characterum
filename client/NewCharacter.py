import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from RaceSelection import *
from CharacteristicsGeneration import *


class NewCharacter:
    def __init__(self, root):
        self.root = root
        self.new_character_window = Toplevel(self.root)
        self.new_character = {'characteristics': {}}
        self.characteristics_window = LabelFrame(self.new_character_window, text="Characteristics")

    def set_character_name(self, character_name):
        self.new_character = {**self.new_character, "name": character_name.get()}

    def set_character_race_attributes(self, attributes):
        for key in attributes:
            self.new_character = {**self.new_character, key: attributes[key]}

        # print("new Character", self.new_character)
        try:
            Label(self.new_character_window, text=f'{self.new_character["race"]}').grid(row=1, column=1)
        except KeyError:
            pass
        self.characteristics_generation()

    def set_character_characteristics(self, characteristic, rating):
        try:
            self.new_character['characteristics'] = {**self.new_character['characteristics'], characteristic:rating}
        except KeyError:
            print("characteristic", characteristic, "rating", rating)
        pp(self.new_character)

    def name_character(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

    def race_selection(self):
        race_selection = RaceSelection(root=self.new_character_window, new_character=self.set_character_race_attributes)
        race_selection.create()

    def characteristics_generation(self):
        characteristics_generation = CharacteristicsGeneration(self.characteristics_window, self.new_character, self.set_character_characteristics)
        characteristics_generation.create()

    def archetype_selection(self):
        pass

    def passions_selection(self):
        pass

    def finish_creation(self):
        # TODO: make comparator to fill in skills that are untrained
        pp(self.new_character)

    def new_character_form(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))
        race_select = Button(self.new_character_window, text="Race ", command=self.race_selection)
        race_select.grid(row=1, column=0)
        self.characteristics_window.grid(row=1, column=2, sticky=W)
        # self.characteristics_generation()

    def create(self):
        self.new_character_window.grab_set()
        self.new_character_window.geometry("600x600")
        self.new_character_window.title("New Character")
        self.new_character_form()

        Button(self.new_character_window, text="Create", command=self.finish_creation).grid()
