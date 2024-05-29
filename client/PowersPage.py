import pprint
from tkinter import *
from tkinter import ttk
import AddPower

# TODO: Fix formatting for Top Bar
# TODO: Fix formatting for power information


class PowersPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.bottom_box = Frame(self.root)
        self.selected_frame = LabelFrame(self.bottom_box, text="Info")

    def add_power(self):
        def new_power(power):
            self.character['psychic']['powers'].append(power)
            pprint.pp(self.character['psychic']['powers'])
            self.powers_list()

        AddPower.create(self.root, self.character, new_power)
        self.powers_list()

    def top_bar(self):
        psy_rating_frame = Frame(self.root)
        psy_rating_label = Label(psy_rating_frame, text=f"Psy Rating: {self.character['psychic']['rating']}")
        psy_rating_label.grid(row=0, column=0)
        psy_rating_frame.grid(row=0, column=0)

        psyker_type = LabelFrame(self.root, text="Type")
        try:
            type_label = Label(psyker_type, text=self.character['psychic']["class"].title())
            type_label.pack()
        except AttributeError:
            type_label = Label(psyker_type, text="None")
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

        window_width = self.selected_frame.winfo_width()

        try:
            # Name
            power_name_frame = LabelFrame(self.selected_frame, text='Name', width=int(window_width*0.2))
            power_name = Label(power_name_frame, text=item['Name'])
            power_name.grid(sticky=NW)
            power_name_frame.grid(row=0, column=0, sticky=NW)

            # Discipline
            power_disc_frame = LabelFrame(self.selected_frame, text='Discipline', width=int(window_width*0.2))
            power_disc = Label(power_disc_frame, text=item['Discipline'])
            power_disc.grid(sticky=NW)
            power_disc_frame.grid(row=1, column=0, sticky=NW)

            # Action
            power_action_frame = LabelFrame(self.selected_frame, text='Action', width=int(window_width*0.2))
            power_action = Label(power_action_frame, text=item['Action'])
            power_action.grid(sticky=NW)
            power_action_frame.grid(row=2, column=0, sticky=NW)

            # Focus Power
            power_focus_frame = LabelFrame(self.selected_frame, text='Focus Power', width=int(window_width*0.2))
            power_focus = Label(power_focus_frame, text=item['Focus Power'])
            power_focus.grid(sticky=NW)
            power_focus_frame.grid(row=3, column=0, sticky=NW)

            # Range
            power_range_frame = LabelFrame(self.selected_frame, text='Range', width=int(window_width*0.2))
            power_range = Label(power_range_frame, text=item['Range'])
            power_range.grid(sticky=NW)
            power_range_frame.grid(row=1, column=1, sticky=NW)

            # Sustained
            power_sustained_frame = LabelFrame(self.selected_frame, text='Sustained', width=int(window_width*0.2))
            power_sustained = Label(power_sustained_frame, text=item['Sustained'])
            power_sustained.grid(sticky=NW)
            power_sustained_frame.grid(row=2, column=1, sticky=NW)

            # Subtypes
            power_subtype_frame = LabelFrame(self.selected_frame, text='Subtypes', width=int(window_width*0.2))
            power_subtype = Label(power_subtype_frame, text=item['Subtype'])
            power_subtype.grid(sticky=NW)
            power_subtype_frame.grid(row=4, column=0, sticky=NW)

            # Description
            power_desc_frame = LabelFrame(self.selected_frame, text='Description', width=int(window_width*0.2))
            power_desc = Label(power_desc_frame, text=item['Description'], wraplength=600, justify=LEFT)
            power_desc.grid(sticky=NW)
            power_desc_frame.grid(row=0, column=2, sticky=NW, rowspan=5)

        except KeyError:
            pass
        # for key in item:
        #     label = Label(self.selected_frame, text=f'{key.title()}: {item[key]}')
        #     label.grid(sticky=W)

        self.selected_frame.grid(row=1, column=1, columnspan=3)

    def create_list_item(self, root, item):
        # print(item)
        entry = Label(root, text=item["Name"])
        entry.bind("<Button>", lambda e: self.render_selected(item))
        entry.grid(sticky=W)

    def powers_list(self):
        # TODO: refactor powers list into a listbox.
        #   Why didn't you make it a listbox in the first place, you dingus?
        # for widget in self.bottom_box.winfo_children():
        #     widget.destroy()

        powers_frame = LabelFrame(self.bottom_box, text="Psychic Powers")
        for power in self.character["psychic"]["powers"]:
            self.create_list_item(root=powers_frame, item=power)

        add_power = Button(powers_frame, text="Add Power", command=self.add_power)

        if self.character["psychic"]["rating"] == 0:
            print("Not a psyker")
            add_power.config(state=DISABLED)

        add_power.grid()

        self.bottom_box.grid(row=1, column=0, columnspan=3)
        powers_frame.grid(row=1, column=0, sticky=N)

    def create(self):
        self.top_bar()
        self.powers_list()
        try:
            self.render_selected(item=self.character['psychic']['powers'][0])
        except KeyError:
            pass
        except IndexError:
            pass
