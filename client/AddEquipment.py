from tkinter import *
from tkinter import ttk
import pandas


class AddEquipment:
    def __init__(self, category, root):
        self.category = category
        self.root = root
        self.item_window = Toplevel(self.root)
        self.item_list = Listbox(self.item_window)
        self.dict = pandas.read_csv(f'./data/{category}.csv').to_dict('records')

    def quality(self):
        quality = StringVar()
        quality_frame = Frame(self.item_window)
        quality.set("Average")
        quality_ranks = ["Poor", "Average", "Good", "Best"]
        quality_selector = OptionMenu(quality_frame, quality, *quality_ranks)
        Label(quality_frame, text="Quality").grid(row=0, column=0, sticky=W)
        quality_selector.grid(row=0, column=1, sticky=W)
        quality_frame.grid(row=1, column=1)

    def add_button_click(self):
        self.item_window.grab_release()
        self.item_window.destroy()

    def weapons_details(self, details_window):
        for widget in details_window.winfo_children():
            widget.destroy()

        for i in self.item_list.curselection():
            Label(details_window, text=self.dict[i]["Name"]).grid(row=0, column=0)
            Label(details_window, text=f'Class: {self.dict[i]["Class"].title()}').grid(row=1, column=0)
            Label(details_window, text=f'DAM: {self.dict[i]["Damage"]} {self.dict[i]["Damage Type"]}').grid(row=1,
                                                                                                            column=1)
            Label(details_window, text=f'PEN: {self.dict[i]["Penetration"]}').grid(row=1, column=2)
            Label(details_window, text=f'Range: {self.dict[i]["Range"]}m').grid(row=2, column=0)
            Label(details_window, text=f'RoF: {self.dict[i]["RoF"]}').grid(row=2, column=1)
            Label(details_window, text=f'Clip: {self.dict[i]["Clip"]}').grid(row=2, column=2)
            Label(details_window, text=f'Rld: {self.dict[i]["Reload"]}').grid(row=2, column=3)

            special_frame = Frame(details_window)
            Label(details_window, text="Special Rules: ").grid(row=3, column=0)
            specials = self.dict[i]["Special"].split(',')
            for special in specials:
                special_name = Label(special_frame, text=special.title())
                special_name.pack(side=LEFT)
            special_frame.grid(row=3, column=1, columnspan=3)

            Label(details_window, text=f'Availability: {self.dict[i]["Availability"]}').grid(row=4, column=0, columnspan=2)
            description_frame = LabelFrame(details_window, text="Description")
            Label(description_frame, text=self.dict[i]["Description"], wraplength=250).pack(side=LEFT)
            description_frame.grid(row=5, column=0, columnspan=4)

    def create(self):
        self.item_window.grab_set()
        self.item_window.geometry("500x500")
        self.item_window.title(f"Add {self.category.title()}")
        details_window = LabelFrame(self.item_window, text='Details', width=300, height=300)

        for index, item in enumerate(self.dict):
            self.item_list.insert(index, item["Name"])
        if self.category == "weapons":
            self.item_list.bind("<Button>", lambda e: self.weapons_details(details_window))
        elif self.category == "armors":
            pass
        self.item_list.grid(row=0, column=0, sticky=N)
        details_window.grid(row=0, column=1, sticky=N)
        add_button = Button(self.item_window, text="Add Weapon", command=self.add_button_click)
        add_button.grid(row=1, column=0)
        self.quality()

