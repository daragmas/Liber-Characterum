from tkinter import *
from tkinter import ttk
from CharacteristicsPage import *
from TraitsAndTalentsPage import *
from EquipmentPage import *
from GearPage import *
from PowersPage import *
from AdvancementsPage import *


class Info:
    def __init__(self, root, character):
        self.root = ttk.Notebook(root)
        self.root.grid()
        self.character = character
        self.characteristics_tab = Frame(self.root, width=1200, height=400)
        self.traits_and_talents_tab = Frame(self.root, width=1200, height=400)
        self.equipment_tab = Frame(self.root, width=1200, height=400)
        self.gear_tab = Frame(self.root, width=1200, height=400)
        self.powers_tab = Frame(self.root, width=1200, height=400)
        self.advancements_tab = Frame(self.root, width=1200, height=400)

    def create(self):
        characteristics_page = CharacteristicsPage(root=self.characteristics_tab, character=self.character)
        characteristics_page.create()

        traits_and_talents_page = TraitsAndTalentsPage(root=self.traits_and_talents_tab, character=self.character)
        traits_and_talents_page.create()

        equipment_page = EquipmentPage(root=self.equipment_tab, character=self.character)
        equipment_page.create()

        gear_page = GearPage(root=self.gear_tab, character=self.character)
        gear_page.create()

        powers_page = PowersPage(root=self.powers_tab, character=self.character)
        powers_page.create()

        advancements_page = AdvancementsPage(root=self.advancements_tab, character=self.character)
        advancements_page.create()

        self.root.add(self.characteristics_tab, text='Characteristics')
        self.root.add(self.traits_and_talents_tab, text='Traits and Talents')
        self.root.add(self.equipment_tab, text='Equipment')
        self.root.add(self.gear_tab, text='Gear')
        self.root.add(self.powers_tab, text='Powers')
        self.root.add(self.advancements_tab, text='Advancements')
