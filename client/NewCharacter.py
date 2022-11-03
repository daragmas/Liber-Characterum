import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from RaceSelection import *
from CharacteristicsGeneration import *
from ArchetypeSelection import *
from PassionSelection import *
from CharacterTemplate import character_template
from mergedeep import merge, Strategy
from tkinter.filedialog import asksaveasfile
import json


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
        self.display_stats_window = Frame(self.new_character_window)
        self.update_modifiers = lambda: self.characteristics_modifiers
        self.characteristics_generation = CharacteristicsGeneration(characteristics_frame=self.characteristics_window,
                                                                    new_character=self.new_character,
                                                                    set_characteristics=self.set_character_characteristics,
                                                                    modifiers=self.characteristics_modifiers,
                                                                    update_mods=self.update_modifiers)

    def set_character_name(self, character_name):
        self.new_character = {**self.new_character, "name": character_name.get()}

    def set_character_race_attributes(self, attributes):
        for key in attributes:
            self.new_character = {**self.new_character, key: attributes[key]}

        try:
            Label(self.new_character_window, text=f'{self.new_character["race"]}').grid(row=1, column=1, sticky=NW)
        except KeyError:
            print("Race: ", self.new_character['race'])

        if self.new_character['race'] == 'Mortal':
            self.characteristics_modifiers['race'] = 25
        elif self.new_character['race'] == 'Chaos Space Marine':
            self.characteristics_modifiers['race'] = 30

        self.characteristics_generation.create()
        self.display_stats()

    def display_stats(self):
        for widget in self.display_stats_window.winfo_children():
            widget.destroy()

        talent_frame = LabelFrame(self.display_stats_window, text='Talents')
        for talent in self.new_character['talents']:
            Label(talent_frame, text=talent).grid(sticky=NW)
        talent_frame.grid(sticky=NW, row=0, column=0)

        traits_frame = LabelFrame(self.display_stats_window, text='Traits')
        for traits in self.new_character['traits']:
            Label(traits_frame, text=traits).grid(sticky=NW)
        traits_frame.grid(sticky=NW, row=0, column=1)

        equipment_frame = LabelFrame(self.display_stats_window, text='Equipment')
        for equipment, item_array in self.new_character['equipment'].items():
            equipment_type = LabelFrame(equipment_frame, text=equipment.title())
            if type(item_array) == str:
                Label(equipment_type, text=item_array).grid(sticky=NW)
            else:
                for item in item_array:
                    try:
                        Label(equipment_type, text=f"{item['Name']} ({item['quality']})").grid(sticky=NW)
                    except AttributeError or TypeError:
                        Label(equipment_type, text=item).grid(sticky=NW)
            equipment_type.grid(sticky=NW)
        equipment_frame.grid(sticky=NW, columnspan=2)

        self.display_stats_window.grid(row=0, column=3, rowspan=20)

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

        self.characteristics_generation.modifiers['archetype'] = characteristic_mods
        for characteristic in characteristic_mods:
            index = characteristics_bc.index(characteristic) + 1
            self.characteristics_generation.show_modifiers(characteristic, index)
            self.characteristics_generation.calculate_final(characteristic, index)

        self.display_stats()

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
                split_penalties = {**split_penalties, split_penalty[0]: int(split_penalty[1]) * -1}
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

    def name_character(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0, sticky=NW)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1, sticky=NW)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

    def race_selection(self):
        race_selection = RaceSelection(root=self.new_character_window,
                                       new_character=self.set_character_race_attributes)
        race_selection.create()

    def archetype_selection(self):
        archetype_selection = ArchetypeSelection(root=self.new_character_window,
                                                 set_archetype=self.set_character_archetype,
                                                 new_character=self.new_character)
        archetype_selection.create()

    def passion_selection(self):
        passions_selection = PassionSelection(root=self.new_character_window, set_passions=self.set_passions)
        passions_selection.create()

    def finish_creation(self):
        formattedspecialists = {
            "Common Lore": {},
            "Forbidden Lore": {},
            "Linguistics": {},
            "Scholastic Lore": {},
            "Navigate": {},
            "Trade": {}
        }
        for skill, rating in self.new_character['skills']['specialist'].items():
            splitskill = skill.strip(')').split(' (')
            merge(formattedspecialists, {splitskill[0]: {splitskill[1]: rating}}, strategy=Strategy.ADDITIVE)

        self.new_character['skills']['specialist'] = formattedspecialists

        self.new_character = merge(character_template, self.new_character, strategy=Strategy.ADDITIVE)

        path = asksaveasfile(initialdir='./characters',
                             title='Save New Character',
                             initialfile='Untitled.json',
                             defaultextension=".json",
                             filetypes=[("JSON Documents", "*.json")])
        json.dump(fp=path, obj=self.new_character, indent=2)

        self.new_character_window.grab_release()
        self.new_character_window.destroy()

    def new_character_form(self):
        Label(self.new_character_window, text="Name: ").grid(row=0, column=0, sticky=NW)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1, sticky=NW)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

        race_select = Button(self.new_character_window, text="Race ", command=self.race_selection)
        race_select.grid(row=1, column=0, sticky=NW)

        self.characteristics_window.grid(row=0, column=2, sticky=NW, rowspan=15)

        archetype_select = Button(self.new_character_window, text="Archetype ", command=self.archetype_selection)
        archetype_select.grid(row=2, column=0, sticky=NW)

        passions_select = Button(self.new_character_window, text='Passions', command=self.passion_selection)
        passions_select.grid(row=3, column=0, sticky=NW)

    def create(self):
        self.new_character_window.grab_set()
        self.new_character_window.geometry("600x600")
        self.new_character_window.title("New Character")
        self.new_character_form()

        Button(self.new_character_window, text="Create", command=self.finish_creation).grid()
        Button(self.new_character_window, text="Console Log", command=lambda: pp(self.new_character)).grid()
