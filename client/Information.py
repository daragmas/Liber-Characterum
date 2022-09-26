from tkinter import *
from tkinter import ttk
# from PageButtons import *
from CharacteristicsPage import *
from TraitsAndTalentsPage import *
from EquipmentPage import *
from GearPage import *
from PowersPage import *
from AdvancementsPage import *

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
    },
    "talents": [
        {
            "name": "Touch Typer",
            "description": "Able to type without looking at the keyboard",
            "book": "Internet"
         },
        {
            "name": "Google-fu",
            "description": "+10 to Inquiry tests when using a search engine",
            "book": "Internet"
        }
    ],
    "traits": [
        {
            "name": "Flatiron Alumni",
            "description": "+10 to social tests during interviews with other Flatiron Alumni",
            "book": "Canvas"
        },
        {
            "name": "Just one more test...",
            "description": "+10 to Toughness tests for staying up late to work on code.",
            "book": "Michael Law's Guide to Coding"
        }
    ],
    "equipment": {
        "weapons": [
            {
                "name": "Laspistol",
                "class": "basic",
                "damage": "1d10+2",
                "damage_type": "E",
                "penetration": 0,
                "range": 30,
                "rate_of_fire": "S/2/-",
                "clip": 30,
                "reload": "half",
                "special": ["reliable", "variable fire"]
            },
{
                "name": "Another Laspistol",
                "class": "basic",
                "damage": "1d10+2",
                "damage_type": "E",
                "penetration": 0,
                "range": 30,
                "rate_of_fire": "S/2/-",
                "clip": 30,
                "reload": "half",
                "special": ["reliable", "variable fire"]
            }
            ],
        "armors":
            [
                {
                    "name": "Guard Flak Armor",
                    "coverage": "all",
                    "armor_points": 4,
                    "weight": "11",
                }
            ]

    }
}


class Info:
    def __init__(self, root):  # , selector):
        self.root = root
        self.selector = "advancements"

    def create(self):
        print(self.selector)
        infoframe = ttk.Frame(self.root, width=1200, height=400, relief="groove")
        # Put comparator statement for checking which panel to access
        characteristicspage = CharacteristicsPage(root=infoframe, character=testcharacter)
        traits_and_talents_page = TraitsAndTalentsPage(root=infoframe, character=testcharacter)
        equipment_page = EquipmentPage(root=infoframe, character=testcharacter)
        gear_page = GearPage(root=infoframe, character=testcharacter)
        powers_page = PowersPage(root=infoframe, character=testcharacter)
        advancements_page = AdvancementsPage(root=infoframe, character=testcharacter)
        if self.selector == "characteristics":
            characteristicspage.create()
        elif self.selector == "traits_talents":
            traits_and_talents_page.create()
        elif self.selector == "equipment":
            equipment_page.create()
        elif self.selector == "gear":
            gear_page.create()
        elif self.selector == "powers":
            powers_page.create()
        elif self.selector == "advancements":
            advancements_page.create()
        else:
            pass

        # pgb = PageButtons(self.root)
        # pgb.create()

        infoframe.grid(sticky=E, row=2, column=0, padx=5, pady=5)
