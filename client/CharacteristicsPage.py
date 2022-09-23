from tkinter import *
from tkinter import ttk
from math import floor


class CharacteristicsPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def top_row(self):
        name_and_archetype = Frame(self.root)
        name_label = Label(name_and_archetype, text=f'Name: {self.character["name"]}')
        name_label.grid(row=0, column=0)
        archetype_label = Label(name_and_archetype, text=f'Archetype: {self.character["archetype"]}')
        archetype_label.grid(row=1, column=0)
        name_and_archetype.grid(row=0, column=0)

        variables = Frame(self.root)
        wounds = Label(variables, text=f'Wounds: CHANGES/{self.character["characteristics"]["wounds"]} ')
        infamy_points = Label(variables, text=f'Infamy: CHANGES/{floor(self.character["characteristics"]["infamy"]/10)}')
        corruption = Label(variables, text=f'Corruption: {self.character["characteristics"]["corruption"]} ')
        ag_mod = floor(self.character["characteristics"]["agility"]/10)
        movement = Label(variables, text=f'Movement:')
        move_values = Label(variables, text=f'Half {ag_mod} '
                                            f'Full {3*ag_mod} \n'
                                            f'Charge {6*ag_mod} '
                                            f'Run {9*ag_mod}')
        wounds.grid(row=0, column=0)
        infamy_points.grid(row=0, column=1)
        corruption.grid(row=0, column=2)
        movement.grid(row=0, column=3)
        move_values.grid(row=0, column=4)
        variables.grid(row=0, column=1)

    def characteristics_box(self):
        charframe = Frame(self.root)
        for characteristic in self.character["characteristics"]:
            charlabel = Label(charframe,
                              text=f'{characteristic.title()}: {self.character["characteristics"][characteristic]}')
            charlabel.grid()
        charframe.grid(row=1, column=0)

    def skills_box(self):
        skills_frame = Frame(self.root)
        x = 0
        y = 0
        for skill in self.character["skills"]:
            if type(self.character["skills"][skill]) == dict:
                skill_name = Label(skills_frame, text=f'{skill.title()}:')
                skill_name.grid(sticky=W, row=x, column=y)
                x += 1
                for sub_category, rating in self.character["skills"][skill].items():
                    # print(sub_category, rating)

                    sub_category_frame = Frame(skills_frame)
                    skill_label = Label(sub_category_frame, text=f'{sub_category}: {rating}')
                    skill_label.grid()
                    sub_category_frame.grid(column=y)
                    x += 1
            else:
                skill_label = Label(skills_frame,
                                    text=f'{skill.title()}: {self.character["skills"][skill]}')
                skill_label.grid(sticky=W, row=x, column=y)
                x += 1

            if x > 18:
                y += 1
                x = 0

        skills_frame.grid(row=1, column=1)

    def description_box(self):
        # TODO: Properly Install PIL and get images to scale
        description_frame = Frame(self.root)
        picture = PhotoImage(file=self.character["picture"])
        token_image = Label(description_frame, image=picture, height=80, width=80)
        token_image.image = picture
        token_image.grid(row=0, column=0)

        alignment_image = PhotoImage(file=f'assets/{self.character["alignment"]}.png')
        alignment = Label(description_frame, image=alignment_image, height=80, width=80)
        alignment.image = alignment_image
        alignment.grid(row=0, column=1)

        details_frame = Frame(description_frame)
        detail_scroll = Scrollbar(details_frame)
        detail_scroll.pack(side=RIGHT, fill=BOTH)
        details = Text(description_frame, height=10, width=20, yscrollcommand=detail_scroll.set)
        details.grid(row=1, column=0, columnspan=2)

        description_frame.grid(row=1, column=2)

    def create(self):
        self.top_row()
        self.characteristics_box()
        self.skills_box()
        self.description_box()