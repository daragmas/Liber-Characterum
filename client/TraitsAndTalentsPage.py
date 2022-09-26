from tkinter import *
from tkinter import ttk


class TraitsAndTalentsPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.selected = {"name": "Select", "desc": "Talent or Trait", "book": "a"}

    def set_selected(self, name, desc, book):
        self.selected = {"name": name, "desc": desc, "book": book}
        print(name, desc, book)

    def talents_list(self):
        talents_frame = LabelFrame(self.root, text="Talents")

        talents_subframe = Frame(talents_frame)
        for talent in self.character["talents"]:
            print(talent["name"], "|", talent["description"], "|", talent["book"])
            entry = Label(talents_subframe, text=talent["name"])
            entry.bind("<Button-1>", lambda e: self.set_selected(talent["name"], talent["description"], talent["book"]))
            entry.grid(sticky=W)

        talents_subframe.grid(row=1, column=0)
        talents_frame.grid(row=0, column=0)

    def traits_list(self):
        traits_frame = LabelFrame(self.root, text="Traits")

        traits_subframe = Frame(traits_frame)
        for trait in self.character["traits"]:
            print(trait["name"], "|", trait["description"], "|", trait["book"])
            entry = Label(traits_subframe, text=trait["name"])
            entry.bind("<Button-1>", lambda e: self.set_selected(trait["name"], trait["description"], trait["book"]))
            entry.grid(sticky=W)

        traits_subframe.grid(row=1, column=0)
        traits_frame.grid(row=0, column=1)

    def description_box(self):
        description_frame = LabelFrame(self.root, text="Info")
        description_name = Label(description_frame, text=self.selected["name"])
        description_book = Label(description_frame, text=self.selected["book"])
        description_description = Label(description_frame, text=self.selected["desc"])

        description_name.grid(row=0, column=0, sticky=W)
        description_book.grid(row=1, column=0, sticky=W)
        description_description.grid(row=2, column=0, sticky=W)
        description_frame.grid(row=0, column=2)

    def create(self):
        self.talents_list()
        self.traits_list()
        self.description_box()
