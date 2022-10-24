from tkinter import *
from tkinter import ttk
import AddPower


class PowersPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.selected_frame = LabelFrame(self.root, text="Info")

    def add_power(self):
        AddPower.create(self.root)

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
        entry = Label(root, text=item["name"])
        entry.bind("<Button>", lambda e: self.render_selected(item))
        entry.grid(sticky=W)

    def powers_list(self):
        powers_frame = LabelFrame(self.root, text="Psychic Powers")
        for power in self.character["psychic"]["powers"]:
            self.create_list_item(root=powers_frame, item=power)
        add_power = Button(powers_frame, text="Add Power", command=self.add_power)
        add_power.grid()
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
