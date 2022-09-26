from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image


class EquipmentPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def weapons(self):
        weapons_frame = Frame(self.root)
        weapons_label = Label(weapons_frame, text="Weapons")
        weapons_label.grid(row=0, column=0)

        for weapon in self.character["equipment"]["weapons"]:
            print(weapon)
            weapon_subframe = Frame(weapons_frame)
            name = Label(weapon_subframe, text=f'Name: {weapon["name"].title()}')
            weapon_class = Label(weapon_subframe, text=f'Class: {weapon["class"].title()}')
            damage = Label(weapon_subframe, text=f'DAM: {weapon["damage"]} {weapon["damage_type"]}')
            penetration = Label(weapon_subframe, text=f'PEN: {weapon["penetration"]}')
            weapon_range = Label(weapon_subframe, text=f'Range: {weapon["range"]}m')
            rof = Label(weapon_subframe, text=f'RoF: {weapon["rate_of_fire"]}')
            clip = Label(weapon_subframe, text=f'Clip: {weapon["clip"]}')
            reload = Label(weapon_subframe, text=f'Rld: {weapon["reload"]}')
            special_frame = Frame(weapon_subframe)
            special_label = Label(weapon_subframe, text="Special Rules: ")

            for special in weapon["special"]:
                special_name = Label(special_frame, text=special.title())
                special_name.grid(row=0)

            name.grid(row=0)
            weapon_class.grid(row=1, column=0)
            damage.grid(row=1, column=1)
            penetration.grid(row=1, column=2)
            weapon_range.grid(row=2, column=0)
            rof.grid(row=2, column=1)
            clip.grid(row=2, column=2)
            reload.grid(row=2, column=3)
            special_label.grid(row=3, column=0)
            special_frame.grid(row=3, column=1, columnspan=3)

            weapon_subframe.grid()

        weapons_frame.grid(row=1, column=0, sticky=N)

    def armors(self):
        # TODO: Set up "equipped" parameter that handles ap values on diagram
        armors_frame = Frame(self.root)
        armors_label = Label(armors_frame, text="Armors")
        armors_label.grid(row=0, column=0)

        for armor in self.character["equipment"]["armors"]:
            armor_subframe = Frame(armors_frame)
            name = Label(armor_subframe, text=f'Name: {armor["name"]}')
            # TODO: Change "ALL Coverage to list of "Head, Body, Arms, Legs"?
            coverage = Label(armor_subframe, text=f'Coverage: {armor["coverage"]}')
            armor_points = Label(armor_subframe, text=f'AP: {armor["armor_points"]}')
            weight = Label(armor_subframe, text=f'Wgt: {armor["weight"]}kg')

            name.grid(row=0, column=0, columnspan=2)
            armor_points.grid(row=0, column=3)
            coverage.grid(row=1, column=0)
            weight.grid(row=1, column=1)
            armor_subframe.grid()

        armors_frame.grid(row=1, column=1, sticky=N)

    def armor_diagram(self):
        # TODO: Set up fields for AP values on body parts

        canvas_frame = Frame(self.root, height=200, width=200)
        canvas_frame.grid(row=0, column=2, sticky=NE, rowspan=2, columnspan=2)

        diagram_image = ImageTk.PhotoImage(Image.open('assets/armor_diagram.PNG').resize((100, 200), Image.ANTIALIAS))
        diagram_canvas = Canvas(canvas_frame, width=200, height=200)
        diagram_canvas.background = diagram_image
        diagram_canvas.pack(fill="both", expand=True)
        diagram_canvas.create_image(0, 0, image=diagram_image, anchor="nw")

    def create(self):
        self.weapons()
        self.armors()
        self.armor_diagram()
