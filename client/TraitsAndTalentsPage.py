from tkinter import *
from tkinter import ttk

import pandas

data = {'talents': pandas.read_csv('./data/talents.csv').to_dict('records'),
        'traits': pandas.read_csv('./data/traits.csv').to_dict('records')}


class TraitsAndTalentsPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.description_frame = LabelFrame(self.root, text="Info")

    def set_selected(self, item, type):
        for widget in self.description_frame.winfo_children():
            widget.destroy()

        info = {'Name': '',
                'Description': ''}

        # TODO: Fix starting displayed info from showing The Quick and the Dead

        if '(' in item:
            item = item.split(' (')[0]

        for entry in data[type]:
            if item in entry.get('Name'):
                info = entry

        description_name = Label(self.description_frame, text=info["Name"])
        description_description = Label(self.description_frame, text=info["Description"], wraplength=300)

        description_name.grid(row=0, column=0, sticky=NW)
        description_description.grid(row=2, column=0, sticky=NW)
        self.description_frame.grid(row=0, column=2, sticky=NE)

    def create_list_item(self, root, item, type):
        entry = Label(root, text=item)
        entry.bind("<Button>", lambda e: self.set_selected(item, type))
        entry.grid(sticky=NW)

    def talents_list(self):
        talents_frame = LabelFrame(self.root, text="Talents")

        for talent in self.character["talents"]:
            self.create_list_item(root=talents_frame, item=talent, type='talents')

        talents_frame.grid(row=0, column=0, sticky=NW)

    def traits_list(self):
        traits_frame = LabelFrame(self.root, text="Traits")

        for trait in self.character["traits"]:
            self.create_list_item(root=traits_frame, item=trait, type='traits')

        traits_frame.grid(row=0, column=1, sticky=NW)

    def add_talent(self):
        print("coming soon!")

    def add_talent_button(self):
        add_talent = Button(self.root, text="Add Talent", command=self.add_talent)
        add_talent.grid(row=1, column=0)

    def create(self):
        self.talents_list()
        self.traits_list()
        self.set_selected(item='', type="traits")
        self.add_talent_button()
