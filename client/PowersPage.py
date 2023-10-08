from tkinter import *
from tkinter import ttk
import AddPower

# TODO: Fix formatting for Top Bar
# TODO: Fix formatting for power information
# TODO: Repopulate list when new power is added
# TODO: Refactor powers on character sheet to be just names? Involves adding powers data lookup. Maybe move
#   lookup from AddPower into its own file?


class PowersPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.bottom_box = Frame(self.root)
        self.selected_frame = LabelFrame(self.bottom_box, text="Info")

    def add_power(self):
        def new_power(power):
            self.character['psychic']['powers'].append(power)
            print(self.character['psychic']['powers'])

        AddPower.create(self.root, self.character, new_power)
        self.powers_list()

    def top_bar(self):
        psy_rating_frame = Frame(self.root)
        psy_rating_label = Label(psy_rating_frame, text=f"Psy Rating: {self.character['psychic']['rating']}")
        psy_rating_label.grid(row=0, column=0)
        psy_rating_frame.grid(row=0, column=0)

        psyker_type = LabelFrame(self.root, text="Type")
        type_label = Label(psyker_type, text=self.character['psychic']["class"].title())
        type_label.pack()
        psyker_type.grid(row=0, column=1)

        psychic_strength_table = LabelFrame(self.root, text='Psychic Strength')
        x = 0
        for key in self.character["psychic"]['type']:
            psy_strength_header = LabelFrame(psychic_strength_table, text=key.title())
            psy_strength_info = Label(psy_strength_header, text=self.character['psychic']['type'][key])
            psy_strength_info.pack(side=LEFT)
            psy_strength_header.grid(row=0, column=x)
            x += 1

        psychic_strength_table.grid(row=0, column=3)

    def render_selected(self, item):
        for widget in self.selected_frame.winfo_children():
            widget.destroy()

        for key in item:
            label = Label(self.selected_frame, text=f'{key.title()}: {item[key]}')
            label.grid(sticky=W)

        self.selected_frame.grid(row=1, column=1, columnspan=3)

    def create_list_item(self, root, item):
        entry = Label(root, text=item["Name"])
        entry.bind("<Button>", lambda e: self.render_selected(item))
        entry.grid(sticky=W)

    def powers_list(self):
        # for widget in self.bottom_box.winfo_children():
        #     widget.destroy()

        powers_frame = LabelFrame(self.bottom_box, text="Psychic Powers")
        for power in self.character["psychic"]["powers"]:
            self.create_list_item(root=powers_frame, item=power)
        add_power = Button(powers_frame, text="Add Power", command=self.add_power)
        add_power.grid()
        self.bottom_box.grid(row=1, column=0, columnspan=3)
        powers_frame.grid(row=1, column=0, sticky=N)
    # TODO: Move some power information from description window to powers list?

    def create(self):
        self.top_bar()
        self.powers_list()
        self.render_selected(item={
                "name": "",
                "action": "",
                "focus": "",
                "focus_difficulty": '',
                "range": '',
                "description": "",
                "sustained": "",
                "grouping": "",
                "subtypes": []
            }
        )
