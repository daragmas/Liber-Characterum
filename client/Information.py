from tkinter import *
from tkinter import ttk
# from PageButtons import *
from CharacteristicsPage import *
from TraitsAndTalentsPage import *
from EquipmentPage import *
from GearPage import *
from PowersPage import *
from AdvancementsPage import *


class Info:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.info_frame = ttk.Frame(self.root, width=1200, height=400, relief="groove")
        self.info_frame.grid(sticky=E, row=2, column=0, padx=5, pady=5)

    def clear_frame(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()

    def render_characteristics(self):
        self.clear_frame()
        characteristics_page = CharacteristicsPage(root=self.info_frame, character=self.character)
        characteristics_page.create()

    def render_traits_talents(self):
        self.clear_frame()
        traits_and_talents_page = TraitsAndTalentsPage(root=self.info_frame, character=self.character)
        traits_and_talents_page.create()

    def render_equipment(self):
        self.clear_frame()
        equipment_page = EquipmentPage(root=self.info_frame, character=self.character)
        equipment_page.create()

    def render_gear(self):
        self.clear_frame()
        gear_page = GearPage(root=self.info_frame, character=self.character)
        gear_page.create()

    def render_powers(self):
        self.clear_frame()
        powers_page = PowersPage(root=self.info_frame, character=self.character)
        powers_page.create()

    def render_advancements(self):
        self.clear_frame()
        advancements_page = AdvancementsPage(root=self.info_frame, character=self.character)
        advancements_page.create()

    def page_buttons(self):
        page_buttons = ttk.Frame(self.root, relief="groove")

        characteristics_button = ttk.Button(page_buttons,
                                            text="Characteristics",
                                            command=self.render_characteristics)
        traits_and_talents_button = ttk.Button(page_buttons,
                                               text="Traits and Talents",
                                               command=self.render_traits_talents)
        equipment_button = ttk.Button(page_buttons,
                                      text="Equipment",
                                      command=self.render_equipment)
        gear_button = ttk.Button(page_buttons,
                                 text="Gear",
                                 command=self.render_gear)
        powers_button = ttk.Button(page_buttons,
                                   text="Powers",
                                   command=self.render_powers)
        advancement_button = ttk.Button(page_buttons,
                                        text="Advancements",
                                        command=self.render_advancements)

        characteristics_button.grid(column=0, row=0)
        traits_and_talents_button.grid(column=1, row=0)
        equipment_button.grid(column=2, row=0)
        gear_button.grid(column=3, row=0)
        powers_button.grid(column=4, row=0)
        advancement_button.grid(column=5, row=0)

        page_buttons.grid(row=3, column=0, padx=5, pady=5)

    def create(self):
        self.page_buttons()
        self.render_characteristics()
