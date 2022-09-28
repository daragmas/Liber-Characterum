from tkinter import *
from tkinter import ttk
from math import floor
from PIL import Image, ImageTk


class CharacteristicsPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def top_row(self):
        top_row_frame = Frame(self.root, relief="groove")
        name_label = Label(top_row_frame, text=f'Name: {self.character["name"]}\n'
                                               f'Archetype: {self.character["archetype"]}')
        name_label.grid(row=0, column=0, sticky=W)

        wounds_box = LabelFrame(top_row_frame, text="Wounds")
        wounds_tracker = Spinbox(wounds_box,
                                 from_=0,
                                 to=self.character['characteristics']["wounds"],
                                 width=5,
                                 justify=RIGHT)
        wounds_total = Label(wounds_box, text=f"/{self.character['characteristics']['wounds']}")
        wounds_tracker.grid(row=0, column=0, sticky=E)
        wounds_total.grid(row=0, column=1, sticky=E)
        # TODO: Add saving current wounds between switching tabs

        infamy_box = LabelFrame(top_row_frame, text="Infamy:")
        infamy_tracker = Spinbox(infamy_box,
                                 from_=0,
                                 to=floor(self.character["characteristics"]["infamy"] / 10),
                                 width=5,
                                 justify=RIGHT)
        infamy_total = Label(infamy_box, text=floor(self.character["characteristics"]["infamy"] / 10))
        infamy_tracker.grid(row=0, column=0, sticky=E)
        infamy_total.grid(row=0, column=1, sticky=E)
        # TODO: Add saving current IP between switching tabs

        corruption = Label(top_row_frame, text=f'Corruption: {self.character["characteristics"]["corruption"]} ')
        ag_mod = floor(self.character["characteristics"]["agility"] / 10)
        movement = LabelFrame(top_row_frame, text=f'Movement:')
        move_values = Label(movement, text=f'Half {ag_mod} '
                                           f'Full {3 * ag_mod} \n'
                                           f'Charge {6 * ag_mod} '
                                           f'Run {9 * ag_mod}')
        afflictions_box = LabelFrame(top_row_frame, text="Afflictions and Conditions")
        afflictions = Text(afflictions_box, height=4, width=20)
        afflictions.pack()

        # TODO: Add saving what is written in the afflictions box

        wounds_box.grid(row=0, column=1)
        infamy_box.grid(row=0, column=2)
        corruption.grid(row=0, column=3)
        movement.grid(row=0, column=4)
        move_values.grid(row=0, column=5)
        afflictions_box.grid(row=0, column=6, sticky=E)

        top_row_frame.grid(row=0, column=0, padx=5, pady=5, columnspan=3)

    def characteristics_box(self):
        charframe = LabelFrame(self.root, text="Characteristics")
        for characteristic in self.character["characteristics"]:
            charlabel = Label(charframe,
                              text=f'{characteristic.title()}: {self.character["characteristics"][characteristic]}')
            charlabel.grid(sticky=E)
        charframe.grid(row=1, column=0, sticky=N)

    def skills_box(self):
        skills_frame = LabelFrame(self.root, text="Skills")
        x = 0
        y = 0
        nonspecialist = LabelFrame(skills_frame, text="Non-specialist")
        for skill in self.character["skills"]["non-specialist"]:
            skill_label = Label(nonspecialist,
                                text=f'{skill.title()}: {self.character["skills"]["non-specialist"][skill]}')
            skill_label.grid(sticky=W, row=x, column=y)
            x += 1
            if x > 11:
                y += 1
                x = 0
        x = 0
        y = 0
        specialist = LabelFrame(skills_frame, text="Specialist")
        for skill in self.character["skills"]["specialist"]:
            skill_name = LabelFrame(specialist, text=f'{skill.title()}:')
            skill_name.grid(sticky=W, row=x, column=y)
            x += 1
            for sub_category, rating in self.character["skills"]["specialist"][skill].items():
                skill_label = Label(skill_name, text=f'{sub_category}: {rating}')
                skill_label.grid(row=x, column=y, sticky=W)
                x += 1
            if x > 11:
                y += 1
                x = 0

        # TODO: Add functionality to modify skill ratings via clicking on the value
        # TODO: Add functionality to add new specialist skills
        nonspecialist.grid(row=0, column=0, sticky=N)
        specialist.grid(row=0, column=1, sticky=N)
        skills_frame.grid(row=1, column=1)

    def description_box(self):
        description_frame = Frame(self.root)
        picture = ImageTk.PhotoImage(Image.open(self.character["picture"]).resize((80, 80), Image.ANTIALIAS))
        token_image_label = Label(description_frame, image=picture)
        token_image_label.image = picture
        token_image_label.grid(row=0, column=0)

        alignment_image = ImageTk.PhotoImage(
            Image.open(f'assets/{self.character["alignment"]}.png').resize((80, 80), Image.ANTIALIAS))
        alignment = Label(description_frame, image=alignment_image, height=80, width=80)
        alignment.image = alignment_image
        alignment.grid(row=0, column=1)

        details_frame = Frame(description_frame)
        detail_scroll = Scrollbar(details_frame)
        detail_scroll.pack(side=RIGHT, fill=BOTH)
        details = Text(description_frame, height=10, width=20, yscrollcommand=detail_scroll.set)
        details.grid(row=1, column=0, columnspan=2)

        # TODO: Add saving what is written in the description box
        description_frame.grid(row=1, column=2)

    def create(self):
        self.top_row()
        self.characteristics_box()
        self.skills_box()
        self.description_box()
