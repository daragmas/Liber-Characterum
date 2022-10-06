import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from RaceSelection import *
from CharacteristicsGeneration import *
from ArchetypeSelection import *
from PassionSelection import *
from mergedeep import merge, Strategy


class NewCharacter:
    def __init__(self, root):
        self.root = root
        self.new_character_window = Toplevel(self.root)
        self.new_character = {'characteristics': {},
                              'passions': {
                                  'Pride': '',
                                  'Disgrace': '',
                                  'Motivation': ''
                              }}
        self.characteristics_window = LabelFrame(self.new_character_window, text="Characteristics")
        self.characteristics_modifiers = {
            "race": 0,
            "archetype": {},
            "Pride": {},
            "Disgrace": {},
            "Motivation": {}
        }
        self.update_modifiers = lambda: self.characteristics_modifiers
        self.race_selection = RaceSelection(root=self.new_character_window,
                                            new_character=self.set_character_race_attributes)
        self.characteristics_generation = CharacteristicsGeneration(characteristics_frame=self.characteristics_window,
                                                                    new_character=self.new_character,
                                                                    set_characteristics=self.set_character_characteristics,
                                                                    modifiers=self.characteristics_modifiers,
                                                                    update_mods=self.update_modifiers)
        self.passions_selection = PassionSelection(root=self.new_character_window, set_passions=self.set_passions)

    def set_character_name(self, character_name):
        self.new_character = {**self.new_character, "name": character_name.get()}

    def set_character_race_attributes(self, attributes):
        for key in attributes:
            self.new_character = {**self.new_character, key: attributes[key]}

        try:
            Label(self.new_character_window, text=f'{self.new_character["race"]}').grid(row=1, column=1,sticky=NW)
        except KeyError:
            pass

        if self.new_character['race'] == 'Mortal':
            self.characteristics_modifiers['race'] = 25
        elif self.new_character['race'] == 'Chaos Space Marine':
            self.characteristics_modifiers['race'] = 30

        self.characteristics_generation.create()

    def set_character_characteristics(self, characteristic, rating):
        try:
            self.new_character['characteristics'] = {**self.new_character['characteristics'], characteristic: rating}
        except KeyError:
            print("characteristic", characteristic, "rating", rating)

    def set_character_archetype(self, archetype, characteristic_mods):
        self.new_character = merge(self.new_character, archetype, strategy=Strategy.ADDITIVE)
        try:
            Label(self.new_character_window, text=f'{self.new_character["archetype"]}').grid(row=2, column=1, sticky=NW)
        except KeyError:
            pass

        # pp(characteristic_mods)
        self.characteristics_generation.modifiers['archetype'] = characteristic_mods
        for characteristic in characteristic_mods:
            index = characteristics_bc.index(characteristic) + 1
            self.characteristics_generation.show_modifiers(characteristic, index)
            self.characteristics_generation.calculate_final(characteristic, index)

    def set_passions(self, passions_choices):
        for passion in passions_choices:
            self.new_character['passions'][passion] = passions_choices[passion]['Name']

            bonuses = passions_choices[passion]['Characteristic Bonus'].split(', ')
            split_bonuses = {}
            for bonus in bonuses:
                split_bonus = bonus.split(': ')
                split_bonuses = {**split_bonuses, split_bonus[0]: int(split_bonus[1])}
            split_penalties = {}
            penalties = passions_choices[passion]['Characteristic Penalty'].split(', ')
            for penalty in penalties:
                split_penalty = penalty.split(': ')
                split_penalties = {**split_penalties, split_penalty[0]: int(split_penalty[1])*-1}
            characteristic_mods = {**split_bonuses, **split_penalties}
            self.characteristics_generation.modifiers[passion] = characteristic_mods

            for characteristic in characteristic_mods:
                index = characteristics_bc.index(characteristic) + 1
                self.characteristics_generation.show_modifiers(characteristic, index)
                self.characteristics_generation.calculate_final(characteristic, index)

        try:
            pride_label = Label(self.new_character_window, text=f'Pride: {self.new_character["passions"]["Pride"]}')
            pride_label.grid(row=3, column=1, sticky=NW)
            disgrace_label = Label(self.new_character_window,
                                   text=f'Disgrace: {self.new_character["passions"]["Disgrace"]}')
            disgrace_label.grid(row=4, column=1, sticky=NW)
            motivation_label = Label(self.new_character_window,
                                     text=f'Motivation: {self.new_character["passions"]["Motivation"]}')
            motivation_label.grid(row=5, column=1, sticky=NW)
        except KeyError:
            pp(self.new_character['passions'])
        # pp(characteristic_mods)
        # pp(self.characteristics_generation.modifiers)

    def name_character(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0, sticky=NW)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1, sticky=NW)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

    def archetype_selection(self):
        archetype_selection = ArchetypeSelection(root=self.new_character_window,
                                                 set_archetype=self.set_character_archetype,
                                                 new_character=self.new_character)
        archetype_selection.create()

    def finish_creation(self):
        # TODO: make comparator to fill in skills that are untrained
        pp(self.new_character)

    def new_character_form(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

        race_select = Button(self.new_character_window, text="Race ", command=self.race_selection.create)
        race_select.grid(row=1, column=0, sticky=NW)

        self.characteristics_window.grid(row=1, column=2, sticky=W, rowspan=15)

        archetype_select = Button(self.new_character_window, text="Archetype ", command=self.archetype_selection)
        archetype_select.grid(row=2, column=0, sticky=NW)

        passions_select = Button(self.new_character_window, text='Passions', command=self.passions_selection.create)
        passions_select.grid(row=3, column=0, sticky=NW)
        # self.characteristics_generation()

    def create(self):
        self.new_character_window.grab_set()
        self.new_character_window.geometry("600x600")
        self.new_character_window.title("New Character")
        self.new_character_form()

        Button(self.new_character_window, text="Create", command=self.finish_creation).grid()
