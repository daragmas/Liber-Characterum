from tkinter import *
from tkinter import ttk
from CharacteristicsPage import *

testcharacter = {
    'name': "Testy McTestface",
    "archetype": "Codetester",
    "picture": "assets/testy_mctestface.png",
    "alignment": "tzeentch",
    "characteristics": {
        "weapon_skill": 10,
        "ballistic_skill": 11,
        "strength": 13,
        "toughness": 14,
        "agility": 15,
        "intelligence": 16,
        "perception": 17,
        "willpower": 18,
        "fellowship": 19,
        "infamy": 20,
        "corruption": 21,
        "wounds": 22
    },
    "skills": {
        "acrobatics": 0,
        "athletics": 0,
        "awareness": 0,
        "charm": 10,
        "command": -20,
        "commerce": 0,
        "common_lore": {"Take Out": 10},
        "deceive": 10,
        "dodge": -20,
        "forbidden_lore": {"Sinatra": 10},
        "inquiry": 30,
        "intimidate": 0,
        "linguistics": {"English": 0, "Python": 10, "Ruby": 10, "JavaScript": 30},
        "logic": 20,
        "medicae": 0,
        "navigation_surface": 0,
        "navigation_stellar": -20,
        "navigation_warp": -20,
        "operate_aeronautica": -20,
        "operate_surface": -20,
        "operate_voidship": -20,
        "parry": 0,
        "psyniscience": -20,
        "scholastic_lore": {},
        "scrutiny": 10,
        "security": 0,
        "sleight_of_hand": -20,
        "stealth": 0,
        "survival": 10,
        "tech_use": 30,
        "tracking": -20,
        "trade": {"Software Development": 20}
    }
}


class Information:
    def __init__(self, root):
        self.root = root

    def create(self):
        infoframe = ttk.Frame(self.root, width=1200, height=400, relief="groove")
        # Put comparator statement for checking which panel to access
        characteristicspage = CharacteristicsPage(root=infoframe, character=testcharacter)
        characteristicspage.create()

        infoframe.grid()
