import tkinter.filedialog
from tkinter import *
from tkinter import ttk
from RaceSelection import *


class NewCharacter:
    def __init__(self, root):
        self.root = root
        self.new_character_window = Toplevel(self.root)
        self.new_character = {}

    def set_character_name(self, character_name):
        self.new_character = {**self.new_character, "name": character_name.get()}

    def name_character(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))

    def race_selection(self):
        # race_choice = StringVar()
        race_selection = RaceSelection(root=self.new_character_window)
        race_selection.create()
        # race_select = Button(self.new_character_window, text="Race ", command=race_selection.create)
        # race_select.grid(row=1, column=0)
        # Label(self.new_character_window, text=f'{race_choice}').grid(row=1, column=1)

    def characteristics_generation(self):
        pass

    def archetype_selection(self):
        pass

    def passions_selection(self):
        pass

    def finish_creation(self):
        # TODO: make comparator to fill in skills that are untrained
        print(self.new_character)

    def new_character_form(self):
        Label(self.new_character_window, text="Name ").grid(row=0, column=0)
        character_name = Entry(self.new_character_window)
        character_name.grid(row=0, column=1)
        character_name.bind('<KeyRelease>', lambda e: self.set_character_name(character_name=character_name))
        race_choice = StringVar()
        race_select = Button(self.new_character_window, text="Race ", command=self.race_selection)
        race_select.grid(row=1, column=0)
        Label(self.new_character_window, text=f'{race_choice}').grid(row=1, column=1)


    def create(self):
        self.new_character_window.grab_set()
        self.new_character_window.geometry("600x600")
        self.new_character_window.title("New Character")
        self.new_character_form()
        # self.name_character()
        # self.race_selection()
        # self.characteristics_generation()
        # self.archetype_selection()
        # self.passions_selection()

        Button(self.new_character_window, text="Create", command=self.finish_creation).grid()

