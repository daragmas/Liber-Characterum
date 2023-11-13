import pprint
from tkinter import *
from tkinter import ttk
from AddEquipment import *
from PIL import ImageTk, Image


class EquipmentPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def weapons(self):
        weapons_frame = LabelFrame(self.root, text="Weapons")

        for weapon in self.character["equipment"]["weapons"]:
            # pprint.pp(weapon)
            # TODO: Why do Force Weapons indent?

            weapon_subframe = Frame(weapons_frame)
            name = Label(weapon_subframe, text=f'Name: {weapon["Name"].title()}')
            weapon_class = Label(weapon_subframe, text=f'Class: {weapon["Class"].title()}')
            damage = Label(weapon_subframe, text=f'DAM: {weapon["Damage"]} {weapon["Damage Type"]}')
            penetration = Label(weapon_subframe, text=f'PEN: {weapon["Penetration"]}')
            weapon_range = Label(weapon_subframe, text=f'Range: {weapon["Range"]}m')
            rof = Label(weapon_subframe, text=f'RoF: {weapon["RoF"]}')
            clip = Label(weapon_subframe, text=f'Clip: {weapon["Clip"]}')
            reload = Label(weapon_subframe, text=f'Rld: {weapon["Reload"]}')
            special_frame = Frame(weapon_subframe)
            special_label = Label(weapon_subframe, text="Special Rules: ")

            if type(weapon['Special']) != float:
                for index, special in enumerate(weapon["Special"].split(', ')):
                    special_name = Label(special_frame, text=special.title())
                    special_name.grid(row=0, column=index, sticky=NW)

            name.grid(row=0, sticky=NW)
            weapon_class.grid(row=1, column=0, sticky=NW)
            damage.grid(row=1, column=1, sticky=NW)
            penetration.grid(row=1, column=2, sticky=NW)
            weapon_range.grid(row=2, column=0, sticky=NW)
            rof.grid(row=2, column=1, sticky=NW)
            clip.grid(row=2, column=2, sticky=NW)
            reload.grid(row=2, column=3, sticky=NW)
            special_label.grid(row=3, column=0, sticky=NW)
            special_frame.grid(row=3, column=1, columnspan=3, sticky=NW)

            weapon_subframe.grid()

        weapons_frame.grid(row=0, column=0, sticky=N)

    def armors(self):
        # TODO: Set up "equipped" parameter that handles ap values on diagram
        armors_frame = LabelFrame(self.root, text="Armors")

        for armor in self.character["equipment"]["armors"]:
            armor_subframe = Frame(armors_frame)
            name = Label(armor_subframe, text=f'Name: {armor["Name"]}')
            # TODO: Change "ALL Coverage to list of "Head, Body, Arms, Legs"?
            coverage = Label(armor_subframe, text=f'Coverage: {armor["Covering"]}')
            armor_points = Label(armor_subframe, text=f'AP: {armor["AP"]}')
            weight = Label(armor_subframe, text=f'Wgt: {armor["Wt"]}kg')

            name.grid(row=0, column=0, columnspan=2)
            armor_points.grid(row=0, column=3)
            coverage.grid(row=1, column=0)
            weight.grid(row=1, column=1)
            armor_subframe.grid()

        armors_frame.grid(row=0, column=1, sticky=N)

    def armor_diagram(self):
        # TODO: Set up fields for AP values on body parts
        # TODO: Fix scaling of armor diagram

        canvas_frame = Frame(self.root, height=200, width=200)
        canvas_frame.grid(row=0, column=3, sticky=NE)

        diagram_image = ImageTk.PhotoImage(Image.open('assets/armor_diagram.PNG').resize((100, 200), Image.ANTIALIAS))
        diagram_canvas = Canvas(canvas_frame, width=200, height=200)
        diagram_canvas.background = diagram_image
        diagram_canvas.pack(fill="both", expand=True)
        diagram_canvas.create_image(0, 0, image=diagram_image, anchor="nw")

    def force_field(self):
        force_field_frame = LabelFrame(self.root, text="Force Field")
        x = 0
        for key in self.character["equipment"]["force_field"]:
            force_field_attribute = Label(force_field_frame, text=key)
            force_field_value = Label(force_field_frame, text=self.character["equipment"]["force_field"][key])
            force_field_attribute.grid(row=0, column=x)
            force_field_value.grid(row=1, column=x)
            x += 1

        force_field_frame.grid(row=0, column=2, sticky=N)

    def add_weapon(self):
        add_wep = AddEquipment(root=self.root, category='weapon')
        add_wep.create()

    def add_armor(self):
        add_arm = AddEquipment(root=self.root, category='armor')
        add_arm.create()

    def force_field_select(self):
        print("Coming soon!")

    def add_equipment_buttons(self):
        add_weapon_button = Button(self.root, text="Add Weapon", command=self.add_weapon)
        add_armor_button = Button(self.root, text="Add Armor", command=self.add_armor)
        select_force_field = Button(self.root, text="Select Force Field", command=self.force_field_select)
        add_weapon_button.grid(row=1, column=0)
        add_armor_button.grid(row=1, column=1)
        select_force_field.grid(row=1, column=2)

    def create(self):
        self.weapons()
        self.armors()
        self.armor_diagram()
        self.force_field()
        self.add_equipment_buttons()
