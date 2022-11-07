from tkinter import *
from tkinter import ttk


class GearPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character
        self.selected_item_frame = LabelFrame(self.root, text="Info")

    def selected_item(self, item):
        # print(item["name"])

        for widget in self.selected_item_frame.winfo_children():
            widget.destroy()

        selected_name = Label(self.selected_item_frame, text=item["Name"])
        selected_book = Label(self.selected_item_frame, text=item["Book"])
        selected_description = Label(self.selected_item_frame, text=item["Description"], wraplength=300)
        selected_name.grid(row=0, column=0, sticky=NW)
        selected_book.grid(row=1, column=0, sticky=NW)
        selected_description.grid(row=2, column=0, columnspan=2)
        self.selected_item_frame.grid(row=0, column=1, sticky=NW)

    def create_list_item(self, root, item):
        gear_subframe = Frame(root)
        gear_name = Label(gear_subframe, text=item['Name'], justify=LEFT)
        gear_quality = Label(gear_subframe, text=f'Quality: {item["Quality"]}')
        gear_quantity = Label(gear_subframe, text=f'Quantity: {item["Quantity"]}')
        gear_name.grid(row=0, column=0, sticky=NW)
        gear_name.bind(sequence='<Button>', func=lambda e: self.selected_item(item))
        gear_quality.grid(row=0, column=1)
        gear_quantity.grid(row=0, column=2, stick=E)
        gear_subframe.grid()

    def gear_list(self):
        gear_frame = LabelFrame(self.root, text="Gear")

        for item in self.character['equipment']['gear']:
            self.create_list_item(gear_frame, item)

        gear_frame.grid(row=0, column=0, sticky=NW)

    def add_gear(self):
        print("This will add some gear to the table!")

    def add_gear_button(self):
        add_gear_button = Button(self.root, text="Add Gear", command=self.add_gear)
        add_gear_button.grid(row=1, column=0, sticky=NW)

    def create(self):
        self.gear_list()
        self.selected_item(item={"Name": "", "Book": "", "Description": ""})
        self.add_gear_button()
