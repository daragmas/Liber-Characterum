from pprint import pp
from tkinter import *
from tkinter import ttk
import pandas


class RaceSelection:
    def __init__(self, root, new_character):
        self.root = root
        self.race_select_window = Toplevel(self.root)
        self.info = pandas.read_csv('./data/races.csv').to_dict('records')
        self.race_list = Listbox(self.race_select_window)
        self.decisions = []
        self.pass_choice = new_character

    def choose_race(self):
        print(self.race_list.curselection())
        for i in self.race_list.curselection():
            selected = self.info[i]
            if type(selected["Starting Skills"]) != float:
                non_specialist_skills = {x: 0 for x in selected["Starting Skills"].split(', ')}
            else:
                non_specialist_skills = {}

            print('talents')
            if type(selected["Starting Talents"]) != float:
                talents = [x for x in selected["Starting Talents"].split(', ')]
            else:
                talents = []

            selection = {
                "race": selected["Name"],
                "skills":
                    {
                        "non-specialist": non_specialist_skills,
                        "specialist": {x: 0 for x in selected["Starting Specialist Skills"].split(', ')}
                    },
                "talents": talents,
                "traits": [x for x in selected["Starting Traits"].split(', ')],
                "equipment": {
                    "armors": [selected["Starting Armor"]],
                    "weapons": [selected["Starting Weapons"]],
                    "gear": [selected["Starting Gear"]]
                },
                "spent_xp": 0,
                "total_xp": selected["Starting XP"]
            }

            for choice in self.decisions:
                print("choice", choice)
                for key in choice:
                    # if key == 'equipment':
                    for subtype in choice[key]:
                        # print('subtype', subtype)
                        for item in choice[key][subtype]:
                            # print('item', item)
                            selection[key][subtype] = [*selection[key][subtype], item]

            self.pass_choice(selection)
        self.race_select_window.grab_release()
        self.race_select_window.destroy()

    def starting_skills(self, i, root):
        skills = LabelFrame(root, text=f"Starting Skills")
        try:
            skills_array = self.info[i]["Starting Skills"].split(', ')
            for index, skill in enumerate(skills_array):
                Label(skills, text=skill).grid(row=index, column=0, sticky=W)
        except AttributeError:
            pass

        specialist_skills = self.info[i]["Starting Specialist Skills"].split(', ')

        for index, skill in enumerate(specialist_skills):
            Label(skills, text=skill).grid(row=index, column=1, sticky=W)

        skills.grid(row=2, column=0, columnspan=2, sticky=NW)

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

    def starting_skill_choices(self, i, root):
        skill_choices = LabelFrame(root, text="Skill Choices")
        try:
            choices_array = self.info[i]["Starting Skill Choices"].split(', ')
            self.decisions = [{}] * len(choices_array)
            for index, choice in enumerate(choices_array):
                if "(Any)" in choice:
                    choice = choice.strip(" (Any)")
                    self.any_choice(choice, index, skill_choices)

            skill_choices.grid(row=2, column=3, sticky=NW)

        except AttributeError:
            pass

    def starting_talents(self, i, details_window):
        talents = LabelFrame(details_window, text="Talents")
        try:
            talents_array = self.info[i]["Starting Talents"].split(', ')
            for index, talent in enumerate(talents_array):
                Label(talents, text=talent).grid(row=index, column=0, sticky=W)
            talents.grid(row=2, column=4, sticky=NW, rowspan=2)
        except AttributeError:
            pass

    def starting_traits(self, i, details_window):
        traits = LabelFrame(details_window, text="Traits")
        try:
            traits_array = self.info[i]["Starting Traits"].split(', ')
            for index, trait in enumerate(traits_array):
                Label(traits, text=trait).grid(row=index, column=0, sticky=W)
            traits.grid(row=3, column=1, sticky=NW)
        except AttributeError:
            pass

    def starting_equipment_choices(self, i, root):
        equipment_choices = LabelFrame(root, text="Equipment Choices")
        try:
            choices_array = self.info[i]["Starting Equipment Choices"].split(', ')
            split_choices = []
            for choices in choices_array:
                split_choices += [choices.split(' or ')]
            new_spaces = [{}] * len(choices_array)
            self.decisions.extend(new_spaces)
            for index, choice in enumerate(split_choices):
                choice_var = StringVar()
                for ind, option in enumerate(choice):
                    self.option_choice(choices_frame=equipment_choices, option=option, index=ind, choice_var=choice_var)

            choices_array.grid(row=4, column=3, sticky=NW)
        except AttributeError:
            pass
        equipment_choices.grid()

    def starting_equipment(self, i, details_window):
        # TODO: Fix nan rendering for Mortal
        equipment_frame = LabelFrame(details_window, text="Equipment")
        armor_frame = LabelFrame(equipment_frame, text="Starting Armor")
        try:
            Label(armor_frame, text=self.info[i]["Starting Armor"]).grid()
        except AttributeError:
            Label(armor_frame, text="").grid()
        armor_frame.grid(sticky=W, row=0, column=0)

        weapon_frame = LabelFrame(equipment_frame, text="Starting Weapon")
        try:
            Label(weapon_frame, text=self.info[i]["Starting Weapons"]).grid()
        except AttributeError:
            Label(weapon_frame, text="").grid()
        weapon_frame.grid(sticky=W, row=1, column=0)

        gear_frame = LabelFrame(equipment_frame, text="Starting Gear")
        try:
            Label(gear_frame, text=self.info[i]["Starting Gear"]).grid()
        except AttributeError:
            Label(gear_frame, text="").grid()
        gear_frame.grid(sticky=W, row=2, column=0)

        self.starting_equipment_choices(i, equipment_frame)

        equipment_frame.grid(row=3, column=0, sticky=NW)

    def starting_xp(self, i, details_window):
        xp_frame = LabelFrame(details_window, text="Starting XP")
        Label(xp_frame, text=self.info[i]["Starting XP"]).grid()
        xp_frame.grid(row=5, column=0, sticky=W)

    def show_info(self, details_window):
        for widget in details_window.winfo_children():
            widget.destroy()

        for i in self.race_list.curselection():
            self.decisions = []
            Label(details_window, text=f"{self.info[i]['Name']}").grid(row=0, column=0)
            Label(details_window,
                  text=f"{self.info[i]['Description']}",
                  wraplength=275, justify=LEFT).grid(row=1, column=0, columnspan=2)
            self.starting_skills(i, details_window)
            self.starting_skill_choices(i, details_window)
            self.starting_talents(i, details_window)
            self.starting_traits(i, details_window)
            self.starting_equipment(i, details_window)
            self.starting_xp(i, details_window)

    def create(self):
        self.race_select_window.grab_set()
        self.race_select_window.title("Race Selection")
        self.race_select_window.geometry("800x600")

        details_window = LabelFrame(self.race_select_window, text="Details", width=300, height=300)

        for index, item in enumerate(self.info):
            self.race_list.insert(index, item["Name"])
        self.race_list.bind("<Button>", lambda e: self.show_info(details_window=details_window))

        self.race_list.grid(row=0, column=0, sticky=N)
        details_window.grid(row=0, column=1, sticky=N)
        select_button = Button(self.race_select_window, text="Choose Race", command=self.choose_race)
        select_button.grid(row=2, column=0)
        # print(self.info)
