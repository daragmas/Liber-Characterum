from pprint import pp
from tkinter import *
from tkinter import ttk
import pandas


class ArchetypeSelection:
    def __init__(self, root, set_archetype, new_character):
        self.root = root
        self.new_character = new_character
        self.set_archetype = set_archetype
        self.archetype_select_window = Toplevel(self.root)
        self.info = pandas.read_csv('./data/archetypes.csv').to_dict('records')
        self.archetypes_list = Listbox(self.archetype_select_window)
        self.details_frame = LabelFrame(self.archetype_select_window, text="Details")
        self.decisions = []

    def starting_characteristics_mods(self, mods):
        mods_frame = LabelFrame(self.details_frame, text="Characteristics Bonuses")
        try:
            all_mods = mods.split(', ')
            for mod in all_mods:
                split_mod = mod.split(': ')
                if '_' in split_mod[0]:
                    split_mod[0] = split_mod[0].replace('_', " ")
                Label(mods_frame, text=f'{split_mod[0].title()} : {split_mod[1]}').grid(sticky=W)
        except AttributeError:
            pass
        mods_frame.grid(row=2, column=0, sticky=W)

    def starting_skills(self, archetype_selection):
        skills_frame = LabelFrame(self.details_frame, text='Skills')

        def fill_skill_frame(skill_list, col):
            try:
                skills = archetype_selection[skill_list].split(', ')
                for index, skill in enumerate(skills):
                    Label(skills_frame, text=skill).grid(row=index, column=col, sticky=W)
            except AttributeError:
                pass

        fill_skill_frame("Starting Skills", 0)
        fill_skill_frame("Starting Specialist Skills", 1)

        skills_frame.grid(row=3, column=0, columnspan=1, sticky=NW)

    def starting_talents(self, archetype_selection):
        talents_frame = LabelFrame(self.details_frame, text="Talents")
        try:
            talents = archetype_selection['Starting Talents'].split(', ')
            for index, talent in enumerate(talents):
                Label(talents_frame, text=talent).grid(row=index, column=0, sticky=W)
        except AttributeError:
            pass
        talents_frame.grid(row=4, column=0, sticky=NW)

    def starting_traits(self, traits):
        traits_frame = LabelFrame(self.details_frame, text="Traits")
        try:
            traits = traits.split(', ')
        except AttributeError:
            pass

        for index, trait in enumerate(traits):
            Label(traits_frame, text=trait).grid(sticky=W, row=index, column=0)

        traits_frame.grid(row=5, column=0, sticky=NW)


    def starting_equipment(self, archetype_selection):
        equipment_frame = LabelFrame(self.details_frame, text='Equipment')
        armor_frame = LabelFrame(equipment_frame, text='Armor')
        weapons_frame = LabelFrame(equipment_frame, text='Weapons')


    def any_choice(self, choice, frame, index, category):
        choice = choice.strip(" (Any)")

        def make_choice(decision):
            if category == 'skill':
                self.decisions[index] = {'skills': {'specialist': {f'{choice} ({decision})': 0}}}
            elif category == 'talent':
                self.decisions[index] = {'talents': f'{choice} ({decision})'}

        Label(frame, text=choice).grid(row=index, column=0)
        choice_entry = Entry(frame)
        choice_entry.grid(row=index, column=1)
        choice_entry.bind('<KeyRelease>', lambda e: make_choice(choice_entry.get()))

    def option_choice(self, choice, frame, index, category, choice_var):
        choice = choice.split(' or ')

        # TODO: Save decisions to self.decisions
        def make_choice():
            if category == 'skill':
                print(choice_var.get())
            elif category == 'talent':
                print(choice_var.get())

        for ind, option in enumerate(choice):
            # TODO: Parse Specialist skill option for radio button
            option_radio = Radiobutton(frame, text=option, value=option, variable=choice_var, command=make_choice)
            option_radio.grid(row=index, column=ind)

    def starting_skill_choices(self, choices):
        skill_choice_frame = LabelFrame(self.details_frame, text='Skill Choices')
        try:
            choices = choices.split(', ')
            for index, choice in enumerate(choices):
                if ' or ' in choice:
                    choice_var = StringVar()
                    self.option_choice(choice, skill_choice_frame, index, 'skill', choice_var)
                else:
                    print('any choice')
                    self.any_choice(choice, skill_choice_frame, index, 'skill')
        except AttributeError:
            pass
        skill_choice_frame.grid(row=3, column=1, columnspan=2, sticky=N)

    def starting_talent_choices(self, choices):
        talent_choice_frame = LabelFrame(self.details_frame, text="Talent Choices")
        try:
            choices = choices.split(', ')
            for index, choice in enumerate(choices):
                if ' or ' in choice:
                    choice_var = StringVar()
                    self.option_choice(choice, talent_choice_frame, index, 'talent', choice_var)
                else:
                    print('any choice')
                    self.any_choice(choice, talent_choice_frame, index, 'talent')
        except AttributeError:
            pass
        talent_choice_frame.grid(row=4, column=1, columnspan=2, sticky=N)

    def show_info(self):
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        archetype_selection = {}
        for archetype in self.info:
            if archetype.get('Name') == self.archetypes_list.get(ANCHOR):
                archetype_selection = archetype

        self.decisions = []
        try:
            # pp(archetype_selection)
            Label(self.details_frame, text=archetype_selection['Name']).grid(row=0, column=0)
            Label(self.details_frame,
                  text=archetype_selection["Summary"],
                  wraplength=275, justify=LEFT).grid(row=1, column=0, columnspan=2)
            self.starting_characteristics_mods(archetype_selection["Starting Characteristics Bonuses"])
            self.starting_skills(archetype_selection)
            self.starting_talents(archetype_selection)
            self.starting_traits(archetype_selection['Starting Traits'])
            self.starting_skill_choices(archetype_selection['Starting Skill Choices'])
            self.starting_talent_choices(archetype_selection['Starting Talent Choices'])
            self.starting_equipment(archetype_selection)
        except KeyError:
            pass
        self.details_frame.grid(row=0, column=1, sticky=N)

    def create(self):
        self.archetype_select_window.grab_set()
        self.archetype_select_window.title("Archetype Selection")
        self.archetype_select_window.geometry("800x600")

        list_row = 0
        for index, item in enumerate(self.info):
            if item['Prerequisite'] == self.new_character['race']:
                self.archetypes_list.insert(list_row, item['Name'])
                list_row += 1
        self.archetypes_list.bind('<Button>', lambda e: self.show_info())

        self.archetypes_list.grid(row=0, column=0, sticky=NW)
        # pp(self.info)
