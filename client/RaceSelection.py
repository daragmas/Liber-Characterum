from tkinter import *
from tkinter import ttk
import pandas


class RaceSelection:
    def __init__(self, root):
        self.root = root
        self.race_select_window = Toplevel(self.root)
        self.info = pandas.read_csv('./data/races.csv').to_dict('records')
        self.race_list = Listbox(self.race_select_window)
        self.decisions = []

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
            self.decisions[index] = {choice: decision}
            # print(self.decisions)

        Label(skill_choices, text=choice).grid(row=index, column=0)
        any_choice = Entry(skill_choices)
        any_choice.grid(row=index, column=1)
        any_choice.bind('<KeyRelease>', lambda e: make_choice(any_choice.get()))

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
            print(split_choices)
            new_spaces = [{}] * len(choices_array)
            self.decisions.extend(new_spaces)
            for index, choice in enumerate(choices_array):
                pass
            # choices_array.grid(row=2, column=3, sticky=NW)

        except AttributeError:
            pass

    def starting_equipment(self, i, details_window):
        equipment_frame = LabelFrame(details_window, text="Equipment")
        # print(self.info[i]["Starting Armor"])
        try:
            armor_frame = LabelFrame(equipment_frame, text="Starting Armor")
            Label(armor_frame, text=self.info[i]["Starting Armor"]).grid()
            armor_frame.grid(sticky=W, row=0, column=0)
        except AttributeError:
            pass
        try:
            weapon_frame = LabelFrame(equipment_frame, text="Starting Weapon")
            Label(weapon_frame, text=self.info[i]["Starting Weapons"]).grid()
            weapon_frame.grid(sticky=W, row=1, column=0)
        except AttributeError:
            pass

        self.starting_equipment_choices(i, equipment_frame)

        equipment_frame.grid(row=3, column=0, sticky=NW)

    def starting_xp(self):
        pass

    def show_info(self, details_window):
        for widget in details_window.winfo_children():
            widget.destroy()

        for i in self.race_list.curselection():
            Label(details_window, text=f"{self.info[i]['Name']}").grid(row=0, column=0)
            Label(details_window, text=f"{self.info[i]['Description']}", wraplength=275, justify=LEFT).grid(row=1,
                                                                                                            column=0,
                                                                                                            columnspan=2)
            # for key in self.info[i]:
            #     if key == 'Name' or key == 'Description' or key == 'System':
            #         pass
            #     else:
            #         print(key)
            self.starting_skills(i, details_window)
            self.starting_skill_choices(i, details_window)
            self.starting_talents(i, details_window)
            self.starting_traits(i, details_window)
            self.starting_equipment(i, details_window)

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
        print(self.info)
