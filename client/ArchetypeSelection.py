import random
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
        self.archetypes_list = Listbox(self.archetype_select_window, height=4)
        self.details_frame = LabelFrame(self.archetype_select_window, text="Details")
        self.skill_decisions = []
        self.talent_decisions = []
        self.equipment_decisions = []
        self.archetype_selection = {}
        self.psychic_powers_choices = []

    # -------------------------- Starting Features --------------------------------------- #
    def starting_characteristics_mods(self, mods, wounds):
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
        Label(mods_frame, text=f'Wounds : {wounds} + 1d5').grid(sticky=W)
        mods_frame.grid(row=2, column=0, sticky='nswe')

    def starting_skills(self):
        skills_frame = LabelFrame(self.details_frame, text='Skills')

        def fill_skill_frame(skill_list, col):
            try:
                skills = self.archetype_selection[skill_list].split(', ')
                for index, skill in enumerate(skills):
                    Label(skills_frame, text=skill).grid(row=index, column=col, sticky=W)
            except AttributeError:
                pass

        fill_skill_frame("Starting Skills", 0)
        fill_skill_frame("Starting Specialist Skills", 1)

        skills_frame.grid(row=2, column=1, columnspan=1, sticky='nswe')

    def starting_talents(self):
        talents_frame = LabelFrame(self.details_frame, text="Talents")
        try:
            talents = self.archetype_selection['Starting Talents'].split(', ')
            for index, talent in enumerate(talents):
                Label(talents_frame, text=talent).grid(row=index, column=0, sticky=W)
        except AttributeError:
            pass
        talents_frame.grid(row=3, column=1, sticky='nswe')

    def starting_traits(self, traits):
        traits_frame = LabelFrame(self.details_frame, text="Traits")
        try:
            traits = traits.split(', ')
        except AttributeError:
            pass

        for index, trait in enumerate(traits):
            Label(traits_frame, text=trait).grid(sticky=W, row=index, column=0)

        traits_frame.grid(row=3, column=0, sticky='nswe')

    def starting_equipment(self):
        equipment_frame = LabelFrame(self.details_frame, text='Equipment')
        armor_frame = LabelFrame(equipment_frame, text='Armor')
        weapons_frame = LabelFrame(equipment_frame, text='Weapons')
        gear_frame = LabelFrame(equipment_frame, text='Gear')

        def display_starting_equipment(frame, equipment_list):
            try:
                for item in equipment_list.split(', '):
                    Label(frame, text=item).grid(sticky=W)
            except AttributeError:
                pass
            frame.grid(sticky=W)

        display_starting_equipment(armor_frame, self.archetype_selection['Starting Armor'])
        display_starting_equipment(weapons_frame, self.archetype_selection['Starting Weapons'])
        display_starting_equipment(gear_frame, self.archetype_selection['Starting Gear'])

        equipment_frame.grid(row=4, column=0, columnspan=2, sticky='nswe')

    def starting_psychic_info(self):
        psychic_frame = LabelFrame(self.details_frame, text='Psychic Details')

        psyker_class = LabelFrame(psychic_frame, text='Starting Psyker Class')
        Label(psyker_class, text=self.archetype_selection["Starting Psyker Class"].title()).grid(sticky=W)
        psyker_class.grid(sticky=W)

        starting_budget = LabelFrame(psychic_frame, text='Starting Powers Budget')
        Label(starting_budget, text=int(self.archetype_selection["Starting Powers Budget"])).grid(sticky=W)
        starting_budget.grid(row=0, column=1, sticky=W)

        discipline_choices = LabelFrame(psychic_frame, text="Starting Discipline Options")
        for index, discipline in enumerate(self.archetype_selection["Starting Powers Disciplines"].split(', ')):
            Label(discipline_choices, text=discipline).grid(row=0, column=index, sticky=W)
        discipline_choices.grid(row=1, column=0, columnspan=2, sticky='nswe')

        starting_powers_frame = LabelFrame(psychic_frame, text="Powers")
        Label(starting_powers_frame, text="Functionality Coming Soon!").grid()
        starting_powers_frame.grid(row=3, column=0, sticky='nswe')

        choose_powers = Button(psychic_frame, text="Choose Powers", command=lambda: print("Coming Soon!"))
        choose_powers.grid(row=4, column=0, sticky='nswe')
        # TODO: Choose Starting Psychic Powers here

        psychic_frame.grid(row=5, columnspan=2, sticky='nswe')

    # ----------------------------Choices-------------------------------------------------#

    def any_choice(self, choice, frame, index, category):
        choice = choice.strip(" (Any)")

        def make_choice(decision):
            if category == 'skill':
                self.skill_decisions[index] = {'specialist': {f'{choice} ({decision})': 0}}
            elif category == 'talent':
                self.talent_decisions[index] = f'{choice} ({decision})'
            else:
                # TODO: Factor in for craftsmanship quality of gear options
                # TODO: Factor in cybernetics any choice
                self.equipment_decisions[index] = {'weapons': {'name': f'{choice} {decision}', 'quality': 'Common'}}

        Label(frame, text=choice).grid(row=index, column=0, sticky=W)
        choice_entry = Entry(frame)
        choice_entry.grid(row=index, column=1, sticky=W)
        choice_entry.bind('<KeyRelease>', lambda e: make_choice(choice_entry.get()))

    def option_choice(self, choice, frame, index, category, choice_var):
        choice = choice.split(' or ')

        def make_choice():
            decision = choice_var.get()
            if category == 'skill':
                if '+' in decision:
                    rating = decision.split(' +')[1]
                    decision = decision.split(' +')[0]
                else:
                    rating = 0

                if '(' in decision and 'Operate' not in decision:
                    self.skill_decisions[index] = {'specialist': {decision: rating}}
                else:
                    self.skill_decisions[index] = {'non-specialist': {decision: rating}}
            elif category == 'talent':
                self.talent_decisions[index] = decision
            else:
                if '(' in decision:
                    decision = decision.split(' (')
                    self.equipment_decisions[index] = {'weapons': {'name': decision[0], 'quality': decision[1].strip(')')}}
                elif 'Armour' in decision:
                    self.equipment_decisions[index] = {'armors': decision}
                else:
                    self.equipment_decisions[index] = {'gear': decision}

        for ind, option in enumerate(choice):
            # TODO: Parse Specialist (Any) skill option for radio button
            option_radio = Radiobutton(frame, text=option, value=option, variable=choice_var, command=make_choice)
            option_radio.grid(row=index, column=ind, sticky=W)

    def starting_skill_choices(self, choices):
        skill_choice_frame = LabelFrame(self.details_frame, text='Skill Choices')
        try:
            choices = choices.split(', ')
            self.skill_decisions = [{}] * len(choices)
            for index, choice in enumerate(choices):
                if ' or ' in choice:
                    choice_var = StringVar()
                    self.option_choice(choice, skill_choice_frame, index, 'skill', choice_var)
                else:
                    self.any_choice(choice, skill_choice_frame, index, 'skill')
        except AttributeError:
            pass
        skill_choice_frame.grid(row=2, column=2, columnspan=2, sticky='nswe')

    def starting_talent_choices(self, choices):
        talent_choice_frame = LabelFrame(self.details_frame, text="Talent Choices")
        try:
            choices = choices.split(', ')
            self.talent_decisions = [""] * len(choices)
            for index, choice in enumerate(choices):
                if ' or ' in choice:
                    choice_var = StringVar()
                    self.option_choice(choice, talent_choice_frame, index, 'talent', choice_var)
                else:
                    self.any_choice(choice, talent_choice_frame, index, 'talent')
        except AttributeError:
            pass
        talent_choice_frame.grid(row=3, column=2, columnspan=2, sticky='nswe')

    def starting_equipment_choices(self, choices):
        equipment_choice_frame = LabelFrame(self.details_frame, text='Equipment Choices')

        try:
            choices = choices.split(', ')
            self.equipment_decisions = [""] * len(choices)
            for index, choice in enumerate(choices):
                if ' or ' in choice:
                    choice_var = StringVar()
                    self.option_choice(choice, equipment_choice_frame, index, 'equipment', choice_var)
                else:
                    self.any_choice(choice, equipment_choice_frame, index, 'equipment')
        except AttributeError:
            pass

        equipment_choice_frame.grid(row=4, column=2, columnspan=2, sticky='nswe')

    # ------------------------------Show Info----------------------------------------- #

    def show_info(self):
        for widget in self.details_frame.winfo_children():
            widget.destroy()

        for archetype in self.info:
            if archetype.get('Name') == self.archetypes_list.get(ANCHOR):
                self.archetype_selection = archetype

        try:
            Label(self.details_frame, text=self.archetype_selection['Name']).grid(row=0, column=0, columnspan=4)
            Label(self.details_frame,
                  text=self.archetype_selection["Summary"],
                  wraplength=600, justify=LEFT).grid(row=1, column=0, columnspan=4)
            self.starting_characteristics_mods(mods=self.archetype_selection["Starting Characteristics Bonuses"],
                                               wounds=self.archetype_selection['Wounds'])
            self.starting_skills()
            self.starting_talents()
            self.starting_traits(self.archetype_selection['Starting Traits'])
            self.starting_skill_choices(self.archetype_selection['Starting Skill Choices'])
            self.starting_talent_choices(self.archetype_selection['Starting Talent Choices'])
            self.starting_equipment()
            self.starting_equipment_choices(self.archetype_selection['Starting Equipment Choices'])
            if 'Psyker' in self.archetype_selection['Starting Traits']:
                self.starting_psychic_info()
        except KeyError:
            pass
        self.details_frame.grid(row=0, column=1, rowspan=2, sticky='nswe')

    def choose_archetype(self):
        # TODO: Talents, Traits, and Equipment if reselecting archetype

        try:
            starting_specialist_skills = {x: 0 for x in
                                          self.archetype_selection["Starting Specialist Skills"].split(', ')}
        except AttributeError:
            starting_specialist_skills = {}

        weapons = []
        try:
            split_weapons = self.archetype_selection['Starting Weapons'].split(', ')
            for weapon in split_weapons:
                if " (" not in weapon:
                    weapons.append({'name': weapon, 'quality': "Common"})
                else:
                    x = weapon.strip(')').split(' (')
                    weapons.append({'name': x[0], "quality": x[1]})
        except AttributeError:
            pass

        archetype = {
            'archetype': self.archetype_selection['Name'],
            'alignment': self.archetype_selection['Alignment'],
            'characteristics': {'wounds': self.archetype_selection["Wounds"] + random.randint(1, 5)},
            'skills': {
                'non-specialist': {x: 0 for x in self.archetype_selection["Starting Skills"].split(', ')},
                'specialist': starting_specialist_skills
            },
            'talents': self.archetype_selection['Starting Talents'].split(', '),
            'traits': self.archetype_selection['Starting Traits'].split(', '),
            'equipment': {
                'armors': [self.archetype_selection['Starting Armor']] if type(
                    self.archetype_selection['Starting Armor']) != float else [],
                'weapons': weapons,
                'gear': self.archetype_selection['Starting Gear'].split(', ') if type(
                    self.archetype_selection['Starting Gear']) != float else []
            },
            'psychic': {
                # TODO: Find way to get psy rating from starting talents list
                'rating': 0, # self.archetype_selection['Starting Talents'][
                # self.archetype_selection['Starting Talents'].find('Psy Rating') + 11],
                'class': "None", # self.archetype_selection['Starting Psyker Class'],
                'powers': self.psychic_powers_choices
            }
        }

        for decision in self.skill_decisions:
            for key in decision:
                for subtype in decision[key]:
                    archetype['skills'][key] = {**archetype['skills'][key], subtype: decision[key][subtype]}

        for decision in self.talent_decisions:
            archetype['talents'].append(decision)

        for decision in self.equipment_decisions:
            for key in decision:
                archetype['equipment'][key].append(decision[key])

        characteristics_mods = {}
        try:
            all_mods = self.archetype_selection['Starting Characteristics Bonuses'].split(', ')
            for mod in all_mods:
                split_mod = mod.split(': ')
                if '_' in split_mod[0]:
                    split_mod[0] = split_mod[0].replace('_', " ")
                characteristics_mods = {**characteristics_mods, split_mod[0]: split_mod[1]}
        except AttributeError:
            pass

        characteristics_mods = {**characteristics_mods, 'wounds': archetype['characteristics']['wounds']}

        self.set_archetype(archetype, characteristics_mods)
        self.archetype_select_window.grab_release()
        self.archetype_select_window.destroy()

    def create(self):
        self.archetype_select_window.grab_set()
        self.archetype_select_window.title("Archetype Selection")
        self.archetype_select_window.geometry("1200x750")

        list_row = 0
        for index, item in enumerate(self.info):
            if item['Prerequisite'] == self.new_character['race']:
                self.archetypes_list.insert(list_row, item['Name'])
                list_row += 1
        self.archetypes_list.bind('<Button>', lambda e: self.show_info())
        self.archetypes_list.grid(row=0, column=0, sticky='nw')
        select_button = Button(self.archetype_select_window, text="Choose Archetype", command=self.choose_archetype)
        select_button.grid(row=2, column=0, sticky='n', columnspan=2)
