import tkinter.filedialog
from tkinter.ttk import *
from tkinter import ttk
from RaceSelection import *
from CharacteristicsGeneration import *
from ArchetypeSelection import *
from PassionSelection import *
from CharacterTemplate import character_template
from mergedeep import merge, Strategy
from tkinter.filedialog import asksaveasfile
import json
import pandas

# TODO: Refactor widget placement.
#   Need to be able to destroy and repopulate race, archetype, and passions if choices change

traits = pandas.read_csv('./data/traits.csv').to_dict('records')
talents = pandas.read_csv('./data/talents.csv').to_dict('records')
armors = pandas.read_csv('./data/armor.csv').to_dict('records')
weapons = pandas.read_csv('./data/weapon.csv').to_dict('records')
gear = pandas.read_csv('./data/gear.csv').to_dict('records')


class NewCharacter:
    def __init__(self, root):
        self.root = root
        self.new_character_window = Toplevel(self.root, padx=5, pady=5, name='new_character_window')
        self.new_character = {'characteristics': {},
                              'passions': {
                                  'Pride': '',
                                  'Disgrace': '',
                                  'Motivation': ''
                              }}
        self.characteristics_window = LabelFrame(self.new_character_window,
                                                 text="Characteristics",
                                                 name='characteristics_window')
        self.characteristics_modifiers = {
            "race": 0,
            "archetype": {},
            "Pride": {},
            "Disgrace": {},
            "Motivation": {}
        }
        self.display_stats_window = LabelFrame(self.new_character_window, text='Stats', name='stats_window')
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

        # Check if the racelabel widget exists and delete it if it does
        try:
            self.new_character_window.nametowidget('.!toplevel.raceLabel').destroy()
            print('Race label deleted')
        except KeyError:
            print('Race label does not exist yet')

        # Create a new racelabel widget
        racelabel = Label(self.new_character_window,
                          text=f'{self.new_character["race"]}',
                          name='raceLabel')
        racelabel.grid(row=1, column=1, sticky=NW)

        # Check if the archetype key exists and if it's not empty
        try:
            if self.new_character["archetype"] != "":
                self.new_character['archetype'] = ""
                self.archetype_selection()
        except KeyError:
            pass

        # Set the race characteristic modifier
        if self.new_character['race'] == 'Mortal':
            self.characteristics_modifiers['race'] = 25
        elif self.new_character['race'] == 'Chaos Space Marine':
            self.characteristics_modifiers['race'] = 30

        # Generate characteristics
        self.characteristics_generation.create()

        # Display stats
        self.display_stats()

    def display_stats(self):
        for widget in self.display_stats_window.winfo_children():
            widget.destroy()

        # DISPLAY TALENTS
        talent_frame = LabelFrame(self.display_stats_window, text='Talents', name='talents_frame')
        for talent in self.new_character['talents']:
            Label(talent_frame, text=talent).grid(sticky=NW)
        talent_frame.grid(sticky='nsew', row=0, column=0)

        # DISPLAY TRAITS
        traits_frame = LabelFrame(self.display_stats_window, text='Traits', name='traits_frame')
        for trait in self.new_character['traits']:
            Label(traits_frame, text=trait).grid(sticky=NW)
        traits_frame.grid(sticky='nsew', row=0, column=1)

        # DISPLAY EQUIPMENT
        equipment_frame = LabelFrame(self.display_stats_window, text='Equipment', name='equipment_frame')
        for equipment, item_array in self.new_character['equipment'].items():
            equipment_type = LabelFrame(equipment_frame, text=equipment.title(), name=f'{equipment}')
            if type(item_array) == str:
                Label(equipment_type, text=item_array, name=f'{item_array[0]}').grid(sticky=NW)
            else:
                for item in item_array:
                    try:
                        Label(equipment_type, text=f"{item['name']} ({item['quality']})").grid(sticky=NW)
                    except AttributeError:
                        Label(equipment_type, text=item).grid(sticky=NW)
                    except TypeError:
                        Label(equipment_type, text=item).grid(sticky=NW)
            equipment_type.grid(sticky=NW)
        equipment_frame.grid(sticky='nsew', columnspan=2)

        # DISPLAY SKILLS
        skill_frame = LabelFrame(self.display_stats_window, text='Skills', name='skills_frame')

        # NON-SPECIALIST SKILLS
        non_spec_skills = LabelFrame(skill_frame, text='Non-Specialist Skills', name='non-spec_skills_frame')
        for skill, rating in self.new_character['skills']['non-specialist'].items():
            Label(non_spec_skills, text=f'{skill.title()}: {rating}').grid(sticky=NW)
        non_spec_skills.grid(row=0, column=0, sticky='nw')

        # SPECIALIST SKILLS
        spec_skills = LabelFrame(skill_frame, text='Specialist Skills', name='spec_skills_frame')
        try:
            for skill, rating in self.new_character['skills']['specialist'].items():
                Label(spec_skills, text=f'{skill.title()}: {rating}').grid(sticky=NW)
            spec_skills.grid(row=0, column=1, sticky='nw')
        except AttributeError:
            print(self.new_character['skills']['specialist'].items())

        skill_frame.grid(row=0, column=2, sticky='n')

        # DISPLAY PSYCHIC
        psychic_frame = LabelFrame(self.display_stats_window, text='Psychic', name='psychic_frame')

        try:
            psy_rating = Label(psychic_frame, text=f'Psy Rating: {self.new_character["psychic"]["rating"]}')
            psy_class = Label(psychic_frame, text=f'Psychic Class: {self.new_character["psychic"]["class"].title()}')
            powers_frame = LabelFrame(psychic_frame, text="Powers", name="psychic_powers_frame")

            for power in self.new_character["psychic"]["powers"]:
                Label(powers_frame, text=power['Name']).grid(sticky=NW)

            psy_rating.grid(row=0, column=0, sticky=NW)
            psy_class.grid(row=1, column=0, sticky=NW)
            powers_frame.grid(row=0, column=1, rowspan=5, sticky=NW)

        except KeyError:
            print('Not a psyker')

        except AttributeError:
            print('Not a psyker')

        psychic_frame.grid(row=1, column=2, sticky=NW)

        self.display_stats_window.grid(row=0, column=3, rowspan=20)

    def set_character_characteristics(self, characteristic, rating):
        try:
            self.new_character['characteristics'] = {**self.new_character['characteristics'], characteristic: rating}
        except KeyError:
            print("characteristic", characteristic, "rating", rating)

    def set_character_archetype(self, archetype, characteristic_mods):
        # TODO: Previously selected powers are not being removed when reselecting archetype

        self.new_character = merge(self.new_character, archetype, strategy=Strategy.ADDITIVE)

        try:
            archetypelabel = Label(self.new_character_window,
                                   text=f'{self.new_character["archetype"]}',
                                   name='archetype_label')
            archetypelabel.grid(row=2, column=1, sticky=NW)
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

            try:
                bonuses = passions_choices[passion]['Characteristic Bonus'].split(', ')
                split_bonuses = {}
                for bonus in bonuses:
                    split_bonus = bonus.split(': ')
                    split_bonuses = {**split_bonuses, split_bonus[0]: int(split_bonus[1])}

            except AttributeError:
                split_bonuses = {}

            try:
                penalties = passions_choices[passion]['Characteristic Penalty'].split(', ')
                split_penalties = {}
                for penalty in penalties:
                    split_penalty = penalty.split(': ')
                    split_penalties = {**split_penalties, split_penalty[0]: int(split_penalty[1]) * -1}
            except AttributeError:
                split_penalties = {}

            try:
                special_trait = passions_choices[passion]["Special Modifier"].split(': ')[0]
                for trait in traits:
                    if trait['Name'] == special_trait:
                        self.new_character['traits'].append(special_trait)
            except AttributeError:
                print(passions_choices[passion]["Special Modifier"])

            characteristic_mods = {**split_bonuses, **split_penalties}
            self.characteristics_generation.modifiers[passion] = characteristic_mods

            for characteristic in characteristic_mods:
                index = characteristics_bc.index(characteristic) + 1
                self.characteristics_generation.show_modifiers(characteristic, index)
                self.characteristics_generation.calculate_final(characteristic, index)

            self.display_stats()

        try:
            passions_frame = Frame(self.new_character_window, name='passions_frame')
            Label(passions_frame,
                  text=f'Pride: {self.new_character["passions"]["Pride"]}',
                  name='pride_choice').grid(sticky=NW)
            Label(passions_frame,
                  text=f'Disgrace: {self.new_character["passions"]["Disgrace"]}',
                  name='disgrace_choice').grid(sticky=NW)
            Label(passions_frame,
                  text=f'Motivation: {self.new_character["passions"]["Motivation"]}',
                  name='motivation_choice').grid(sticky=NW)
            passions_frame.grid(row=3, column=1, sticky=NW)
        except KeyError:
            pp(self.new_character['passions'])

    def name_character(self):
        Label(self.new_character_window, text="Name ", name='nameLabel').grid(row=0, column=0, sticky=NW)
        character_name = Entry(self.new_character_window, name='charNameEntry')
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
        # TODO: Add checks for missing choices. Maybe disable button if missing choices?

        formattedspecialists = {
            "Common Lore": {},
            "Forbidden Lore": {},
            "Linguistics": {},
            "Scholastic Lore": {},
            "Navigate": {},
            "Trade": {}
        }

        # Add specialist skills to character
        for skill, rating in self.new_character['skills']['specialist'].items():
            splitskill = skill.strip(')').split(' (')
            merge(formattedspecialists, {splitskill[0]: {splitskill[1]: rating}}, strategy=Strategy.ADDITIVE)
        self.new_character['skills']['specialist'] = formattedspecialists

        # Add armor to character
        for index, armor in enumerate(self.new_character['equipment']['armors']):
            for a in armors:
                if armor == a['Name']:
                    self.new_character['equipment']['armors'][index] = a

        # Add weapons to Character
        for index, weapon in enumerate(self.new_character['equipment']['weapons']):
            for w in weapons:
                if 'x' in weapon['name']:
                    if weapon['name'].split(' x')[0] == w['Name']:
                        self.new_character['equipment']['weapons'][index] = {
                            **w,
                            'Quality': weapon['quality'],
                            'Special': f'{w["Special"]}, Quantity: {weapon["name"].split(" x")[1]}'
                        }
                elif weapon['name'] == w['Name']:
                    self.new_character['equipment']['weapons'][index] = {
                        **w, 'Quality': weapon['quality']}

        # Add gear to character
        for index, starting_gear in enumerate(self.new_character['equipment']['gear']):
            for g in gear:
                if ' - ' in starting_gear:
                    split_gear = starting_gear.split(' - ')
                    if split_gear[0] == g['Name']:
                        self.new_character['equipment']['gear'][index] = {
                            **g,
                            "Description": f'{g["Description"]}. {split_gear[1]}',
                            "Quality": "Common",
                            "Quantity": 1
                        }
                elif ' x' in starting_gear:
                    split_gear = starting_gear.split(' (')
                    split_gear[1] = split_gear[1].split(') x')
                    if split_gear[0] == g['Name']:
                        self.new_character['equipment']['gear'][index] = {
                            **g,
                            "Name": f'{split_gear[0]} ({split_gear[1][0]})',
                            "Quantity": split_gear[1][1],
                            "Quality": "Common"
                        }
                elif starting_gear == g['Name']:
                    self.new_character['equipment']['gear'][index] = {
                        **g,
                        "Quality": "Common",
                        "Quantity": 1
                    }

                # TODO: Factor in Qualities after refactoring starting Cybernetics for Heretek
                qualities = ['Poor', "Good", "Best"]
                # if any(quality in starting_gear for quality in qualities):
                #     self.new_character['equipment']['gear'][index] = {
                #         **self.new_character['equipment']['gear'][index],
                #         "Quality":
                #     }

        # Add missing pieces of character sheet to new character
        self.new_character = merge(character_template, self.new_character, strategy=Strategy.ADDITIVE)

        # Save new character to disk
        path = asksaveasfile(initialdir='./characters',
                             title='Save New Character',
                             initialfile='Untitled.json',
                             defaultextension=".json",
                             filetypes=[("JSON Documents", "*.json")])
        json.dump(fp=path, obj=self.new_character, indent=2)

        # Close character creation window
        self.new_character_window.grab_release()
        self.new_character_window.destroy()

    def new_character_form(self):
        Label(self.new_character_window, text="Name: ", name='name_label').grid(row=0, column=0, sticky=NE)
        character_name = Entry(self.new_character_window, name='charName')
        character_name.grid(row=0, column=1, sticky=NW)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

        race_select = Button(self.new_character_window,
                             text="Race ",
                             command=self.race_selection,
                             name='raceSelect')
        race_select.grid(row=1, column=0, sticky=NE)

        self.characteristics_window.grid(row=0, column=2, sticky=NW, rowspan=15)

        archetype_select = Button(self.new_character_window,
                                  text="Archetype ",
                                  command=self.archetype_selection,
                                  name='archetypeSelect')
        archetype_select.grid(row=2, column=0, sticky=NE)

        passions_select = Button(self.new_character_window,
                                 text='Passions',
                                 command=self.passion_selection,
                                 name='passionSelect')
        passions_select.grid(row=3, column=0, sticky=NE)

        for widget in self.new_character_window.winfo_children():
            widget.grid_configure(padx=5, pady=5)

    def create(self):
        self.new_character_window.grab_set()
        self.new_character_window.geometry("1200x600")
        self.new_character_window.title("New Character")
        self.new_character_form()

        Button(self.new_character_window, text="Create",
               command=self.finish_creation,
               name='createChar').grid(row=20, sticky=N, columnspan=5)

        # Debugging Buttons
        Button(self.new_character_window,
               text="Console Log",
               command=lambda: pp(self.new_character)).grid()
        Button(self.new_character_window,
               text="Window Info",
               command=lambda: pp(self.new_character_window.winfo_children())).grid()
        Button(self.new_character_window,
               text="RaceLabel Info",
               command=lambda: pp(self.new_character_window.nametowidget('.!toplevel.raceLabel'))).grid()
