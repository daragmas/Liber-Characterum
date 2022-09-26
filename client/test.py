from tkinter import *
from tkinter import ttk
from Toolbar import *
from CharacterSelection import *
from Information import *
# from PageButtons import *

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
            ],
        "gear":
            [
                {
                    "name": "Thing",
                    "book": "Book",
                    "quantity": 1,
                    "quality": "average",
                    "description": "A thing of average quality."
                },
{
                    "name": "Another Thing",
                    "book": "Book 2",
                    "quantity": 2,
                    "quality": "best",
                    "description": "A thing of great quality."
                },
{
                    "name": "Thing number 3",
                    "book": "Book 3",
                    "quantity": 3,
                    "quality": "poor",
                    "description": "A thing of bad quality."
                }
            ]
    },
    "spent_xp": 7000,
    "total_xp": 10000,
    "total_alignments": {
        "khorne": 1,
        "nurgle": 2,
        "slaanesh": 3,
        "tzeentch": 8,
        "unaligned": 4
    },
    "purchased_advancements": [
        {
            "name": "Test Advancement",
            "book": "Test book",
            "description": "Does this work?"
        },
        {
            "name": "Another Test Advancement",
            "book": "Test book 2: Textual Boogaloo",
            "description": "It work!?!?!"
        }
    ],
    "mutations":
    [
        {
            "name": "Test Mutation",
            "description": "This is a test value"
        }
    ]
}

character_list = [testcharacter]

selector = "characteristics"

root = Tk()
root.title("Liber Characterum")
root.geometry("1200x600")

# Toolbar
tb = Toolbar(root)
tb.create()

# Character Selection
charsel = CharacterSelection(root, characters=character_list)
charsel.create()

# Information Page
info = Info(root, testcharacter)
root.after(0, info.create())

root.mainloop()
