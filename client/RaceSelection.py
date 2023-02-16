from pprint import pp
from tkinter import *
from tkinter import ttk
import pandas


class RaceSelection:
    def __init__(self, root, new_character):
        self.root = root
        self.race_select_window = Toplevel(self.root)
        self.info = pandas.read_csv('./data/races.csv').to_dict('records')
        self.race_list = Listbox(self.race_select_window, height=2)
        self.decisions = []
        self.pass_choice = new_character
        self.selection = {}

    def choose_race(self):
        if type(self.selection["Starting Skills"]) != float:
            non_specialist_skills = {x.casefold(): 0 for x in self.selection["Starting Skills"].split(', ')}
        else:
            non_specialist_skills = {}

        if type(self.selection["Starting Talents"]) != float:
            talents = [x for x in self.selection["Starting Talents"].split(', ')]
        else:
            talents = []

        if str(self.selection["Starting Weapons"]) != 'nan':
            split_and_strip = self.selection["Starting Weapons"].strip(')').split(' (')
            self.selection['Starting Weapons'] = {'name': split_and_strip[0], 'quality': split_and_strip[1]}

        selection = {
            "race": self.selection["Name"],
            "skills":
                {
                    "non-specialist": non_specialist_skills,
                    "specialist": {x: 0 for x in self.selection["Starting Specialist Skills"].split(', ')}
                },
            "talents": talents,
            "traits": [x for x in self.selection["Starting Traits"].split(', ')],
            "equipment": {
                "armors": [self.selection["Starting Armor"]] if str(self.selection["Starting Armor"]) != 'nan' else [],
                "weapons": [self.selection["Starting Weapons"]] if str(self.selection["Starting Weapons"]) != 'nan' else [],
                "gear": [self.selection["Starting Gear"]] if str(self.selection["Starting Gear"]) != 'nan' else []
            },
            "spent_xp": 0,
            "total_xp": self.selection["Starting XP"]
        }

        for choice in self.decisions:
            for key in choice:
                for subtype in choice[key]:
                    for item in choice[key][subtype]:
                        if subtype == 'weapons':
                            split_strip = item.strip(')').split(' (')
                            item = {'name': split_strip[0], 'quality': split_strip[1]}
                        selection[key][subtype] = [*selection[key][subtype], item]

        self.pass_choice(selection)

        self.race_select_window.grab_release()
        self.race_select_window.destroy()

    def starting_skills(self, root):
        skills = LabelFrame(root, text=f"Starting Skills", width=250)
        try:
            skills_array = self.selection["Starting Skills"].split(', ')
            for index, skill in enumerate(skills_array):
                Label(skills, text=skill, justify=LEFT).grid(row=index, column=0, sticky='nsw')
        except AttributeError:
            pass

        specialist_skills = self.selection["Starting Specialist Skills"].split(', ')

        for index, skill in enumerate(specialist_skills):
            Label(skills, text=skill, justify=LEFT).grid(row=index, column=1, sticky='nsw')

        skills.grid(row=2, column=0, columnspan=2, sticky='snew')

    def any_choice(self, choice, index, skill_choices):
        def make_choice(decision):
            self.decisions[index] = {"skills": {"specialist": {f'{choice} ({decision})': 0}}}

        Label(skill_choices, text=choice).grid(row=index, column=0)
        any_choice = Entry(skill_choices)
        any_choice.grid(row=index, column=1)
        any_choice.bind('<KeyRelease>', lambda e: make_choice(any_choice.get()))

    def option_choice(self, choices_frame, option, index, choice_var):
        def make_choice():
            self.decisions[0] = {'equipment': {"weapons": [choice_var.get()]}}

        choice_radio = Radiobutton(choices_frame,
                                   text=option,
                                   value=option,
                                   variable=choice_var,
                                   command=make_choice)
        choice_radio.pack(side=LEFT)

    def starting_skill_choices(self, root):
        skill_choices = LabelFrame(root, text="Skill Choices", width=250)
        try:
            choices_array = self.selection["Starting Skill Choices"].split(', ')
            self.decisions = [{}] * len(choices_array)
            for index, choice in enumerate(choices_array):
                if "(Any)" in choice:
                    choice = choice.strip(" (Any)")
                    self.any_choice(choice, index, skill_choices)
        except AttributeError:
            Label(skill_choices, text="None").grid(sticky='nsew')
        skill_choices.grid(row=2, column=2, sticky='snew')

    def starting_talents(self, details_window):
        talents = LabelFrame(details_window, text="Talents", width=250)
        try:
            talents_array = self.selection["Starting Talents"].split(', ')
            for index, talent in enumerate(talents_array):
                Label(talents, text=talent).grid(row=index, column=0, sticky='nsw')
        except AttributeError:
            Label(talents, text="None").grid(row=0, column=0, sticky='nsw')
        talents.grid(row=2, column=3, sticky='snew', rowspan=2)

    def starting_traits(self, details_window):
        traits = LabelFrame(details_window, text="Traits", width=250)
        try:
            traits_array = self.selection["Starting Traits"].split(', ')
            for index, trait in enumerate(traits_array):
                Label(traits, text=trait, justify=LEFT).grid(row=index, column=0, sticky='nsw')
            traits.grid(row=3, column=2, sticky='snew')
        except AttributeError:
            pass

    def starting_equipment_choices(self, root):
        equipment_choices = LabelFrame(root, text="Equipment Choices")
        try:
            if str(self.selection["Starting Equipment Choices"]) != 'nan':
                choices_array = self.selection["Starting Equipment Choices"].split(', ')
                split_choices = []
                for choices in choices_array:
                    split_choices += [choices.split(' or ')]
                new_spaces = [{}] * len(choices_array)
                self.decisions.extend(new_spaces)
                for index, choice in enumerate(split_choices):
                    choice_var = StringVar()
                    for ind, option in enumerate(choice):
                        self.option_choice(choices_frame=equipment_choices, option=option, index=ind, choice_var=choice_var)
            else:
                self.selection["Starting Equipment Choices"] = []
                Label(equipment_choices, text='None').grid(sticky='nsew')
            equipment_choices.grid(sticky='nsew')
        except AttributeError:
            print(self.selection["Starting Equipment Choices"], "Start equipment Attribute Error")

    def starting_equipment(self, details_window):
        equipment_frame = LabelFrame(details_window, text="Equipment", width=250)

        # Armor
        armor_frame = LabelFrame(equipment_frame, text="Starting Armor")
        if str(self.selection["Starting Armor"]) != 'nan':
            Label(armor_frame, text=self.selection["Starting Armor"]).grid(sticky='nsew')
        else:
            Label(armor_frame, text="None").grid(sticky='nsew')
        armor_frame.grid(sticky='nsew', row=0, column=0)

        # Weapons
        weapon_frame = LabelFrame(equipment_frame, text="Starting Weapon")
        if str(self.selection["Starting Weapons"]) != 'nan':
            Label(weapon_frame, text=self.selection["Starting Weapons"]).grid(sticky='nsew')
        else:
            Label(weapon_frame, text='None').grid(sticky='nsew')
        weapon_frame.grid(sticky='nsew', row=1, column=0)

        # Gear
        gear_frame = LabelFrame(equipment_frame, text="Starting Gear")
        if str(self.selection["Starting Gear"]) != 'nan':
            Label(gear_frame, text=self.selection["Starting Gear"]).grid(sticky='nsew')
        else:
            Label(gear_frame, text="None").grid(sticky='nsew')
        gear_frame.grid(sticky='nsew', row=2, column=0)

        self.starting_equipment_choices(equipment_frame)

        equipment_frame.grid(row=3, column=0, columnspan=2, sticky='snew')

    def starting_xp(self, details_window):
        xp_frame = LabelFrame(details_window, text="Starting XP")
        Label(xp_frame, text=self.selection["Starting XP"], justify=CENTER).grid(sticky='ns')
        xp_frame.grid(row=5, column=2, sticky='ew')

    def show_info(self, details_window):
        for widget in details_window.winfo_children():
            widget.destroy()

        for race in self.info:
            if race.get('Name') == self.race_list.get(ANCHOR):
                self.selection = race

        self.decisions = []
        Label(details_window, text=f"{self.selection['Name']}").grid(row=0, column=0, columnspan=4)
        Label(details_window,
              text=f"{self.selection['Description']}",
              wraplength=800, justify=CENTER).grid(row=1, column=0, columnspan=4)
        self.starting_skills(details_window)
        self.starting_skill_choices(details_window)
        self.starting_talents(details_window)
        self.starting_traits(details_window)
        self.starting_equipment(details_window)
        self.starting_xp(details_window)

    def create(self):
        self.race_select_window.grab_set()
        self.race_select_window.title("Race Selection")
        self.race_select_window.geometry("950x500")

        details_window = LabelFrame(self.race_select_window, text="Details", width=250, height=300)

        for index, item in enumerate(self.info):
            self.race_list.insert(index, item["Name"])
        self.race_list.bind("<Button>", lambda e: self.show_info(details_window=details_window))

        self.race_list.grid(row=0, column=0, sticky=N)
        details_window.grid(row=0, column=1, sticky=N)
        select_button = Button(self.race_select_window, text="Choose Race", command=self.choose_race)
        select_button.grid(row=2, column=0, columnspan=3)
