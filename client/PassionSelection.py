from pprint import pp
from tkinter import *
from tkinter import ttk
import pandas


class PassionSelection:
    def __init__(self, root, set_passions):
        self.root = root
        self.passions_window = Toplevel(self.root, padx=5, pady=5)
        self.info = pandas.read_csv('./data/passions.csv').to_dict('records')
        self.choices = {'Pride': {}, 'Disgrace': {}, 'Motivation': {}}
        self.pride_info = LabelFrame(self.passions_window, text="Pride", width=20)
        self.disgrace_info = LabelFrame(self.passions_window, text="Disgrace", width=20)
        self.motivation_info = LabelFrame(self.passions_window, text="Motivation", width=20)
        self.set_passions = set_passions

    def details(self, listbox):
        characteristics = ["weapon skill", "ballistic skill", 'strength', "toughness", "agility",
                           "intelligence", "perception", "willpower", "fellowship"]

        def display_info(selection, details_box):
            for widget in details_box.winfo_children():
                widget.destroy()

            Label(details_box, text=selection['Name']).grid(row=0, column=0)

            bonus_frame = LabelFrame(details_box, text='Characteristics Bonus')
            try:
                if ', ' in selection['Characteristic Bonus']:
                    split_bonuses = selection['Characteristic Bonus'].split(', ')
                    for bonus in split_bonuses:
                        Label(bonus_frame, text=bonus.title()).grid(sticky=NW)
                elif 'ANY' in selection['Characteristic Bonus']:
                    bonus_selection = StringVar(bonus_frame)
                    bonus_selection.set("Weapon Skill")
                    characteristic_menu = OptionMenu(bonus_frame, bonus_selection, *characteristics)
                    characteristic_menu.bind('<Configure>',
                                             lambda e: self.choices['Motivation'].update(
                                                 {'Characteristic Bonus': f'{bonus_selection.get()}: 5'}))
                    characteristic_menu.grid(sticky=NW)
                    Label(bonus_frame, text='+5').grid(row=0, column=1, sticky=NW)
                else:
                    Label(bonus_frame, text=selection['Characteristic Bonus'].title()).grid(sticky=NW)
            except TypeError:
                Label(bonus_frame, text="Special").grid(sticky=NW)
            bonus_frame.grid(row=1, sticky='nsew', rowspan=3)

            penalty_frame = LabelFrame(details_box, text='Characteristics Penalty')
            try:
                if 'ANY' in selection['Characteristic Penalty']:
                    penalty_one_selection = StringVar(penalty_frame)
                    penalty_one_selection.set("Weapon Skill")
                    char_pen_one_menu = OptionMenu(penalty_frame, penalty_one_selection, *characteristics)
                    char_pen_one_menu.grid(sticky=NW)
                    Label(penalty_frame, text='-3').grid(row=0, column=1, sticky=NW)

                    penalty_two_selection = StringVar(penalty_frame)
                    penalty_two_selection.set("Weapon Skill")
                    char_pen_two_menu = OptionMenu(penalty_frame, penalty_two_selection, *characteristics)
                    char_pen_two_menu.grid(sticky=NW)
                    Label(penalty_frame, text='-3').grid(row=0, column=1, sticky=NW)

                    char_pen_one_menu.bind('<Configure>',
                                           lambda e: self.choices['Motivation'].update(
                                               {'Characteristic Penalty': f'{penalty_one_selection.get()}: 3, {penalty_two_selection.get()}: 3'}))
                    char_pen_two_menu.bind('<Configure>',
                                           lambda e: self.choices['Motivation'].update(
                                               {'Characteristic Penalty': f'{penalty_one_selection.get()}: 3, {penalty_two_selection.get()}: 3'}))

                elif ', ' in selection['Characteristic Penalty']:
                    split_penalty = selection['Characteristic Penalty'].split(', ')
                    for penalty in split_penalty:
                        Label(penalty_frame, text=penalty.title()).grid(sticky=NW)
                else:
                    Label(penalty_frame, text=selection['Characteristic Penalty'].title()).grid(sticky=NW)
            except TypeError:
                Label(penalty_frame, text="Special").grid(sticky=NW)
            penalty_frame.grid(row=4, rowspan=2, sticky='nsew')

            if type(selection['Special Modifier']) != float:
                special_frame = LabelFrame(details_box, text="Special Modifier")
                Label(special_frame, text=selection['Special Modifier'], wraplength=200, justify=LEFT).grid(
                    sticky='nsew')
                special_frame.grid(row=6, sticky='nsew')
            Label(details_box, text=selection['Description'], wraplength=200, justify=LEFT).grid(row=7)

        choice = {}

        for passion in self.info:
            if passion.get('Name') == listbox.get(ANCHOR):
                choice = passion
                self.choices = {**self.choices, passion['Type']: passion}

        try:
            if choice['Type'] == 'Pride':
                display_info(choice, self.pride_info)
            elif choice['Type'] == 'Disgrace':
                display_info(choice, self.disgrace_info)
            elif choice['Type'] == 'Motivation':
                display_info(choice, self.motivation_info)
        except KeyError:
            pass

    def populate_listbox(self, listbox, items):
        for index, item in enumerate(items):
            listbox.insert(index, item['Name'])
        listbox.bind('<Button>', lambda e: self.details(listbox))

    def show_info(self):
        prides = [x for x in self.info if x['Type'] == 'Pride']
        disgraces = [x for x in self.info if x['Type'] == 'Disgrace']
        motivations = [x for x in self.info if x['Type'] == 'Motivation']

        pride_listbox = Listbox(self.passions_window, width=20)
        disgrace_listbox = Listbox(self.passions_window, width=20)
        motivation_listbox = Listbox(self.passions_window, width=20)

        self.populate_listbox(pride_listbox, prides)
        self.populate_listbox(disgrace_listbox, disgraces)
        self.populate_listbox(motivation_listbox, motivations)

        pride_listbox.grid(row=0, column=0, sticky='new')
        disgrace_listbox.grid(row=0, column=1, sticky='new')
        motivation_listbox.grid(row=0, column=2, sticky='new')

    def choose_passions(self):
        self.set_passions(self.choices)
        self.passions_window.grab_release()
        self.passions_window.destroy()

    def create(self):
        self.passions_window.title('Select Passions')
        self.passions_window.grab_set()
        self.passions_window.geometry('650x550')

        Label(self.pride_info, text='Pick One', width=25).grid()
        Label(self.disgrace_info, text='Pick One', width=25).grid()
        Label(self.motivation_info, text='Pick One', width=25).grid()

        self.pride_info.grid(row=1, column=0, sticky='nsew')
        self.disgrace_info.grid(row=1, column=1, sticky='nsew')
        self.motivation_info.grid(row=1, column=2, sticky='nsew')

        select_button = Button(self.passions_window, text='Choose Passions', command=self.choose_passions)
        select_button.grid(row=2, columnspan=3, sticky=S)

        print_button = Button(self.passions_window, text='Show Selections', command=lambda: pp(self.choices))
        print_button.grid()

        self.show_info()
