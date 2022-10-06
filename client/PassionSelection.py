from pprint import pp
from tkinter import *
from tkinter import ttk
import pandas


class PassionSelection:
    def __init__(self, root, set_passions):
        self.root = root
        self.passions_window = Toplevel(self.root)
        self.info = pandas.read_csv('./data/passions.csv').to_dict('records')
        self.choices = {'Pride': {}, 'Disgrace': {}, 'Motivation': {}}
        self.pride_info = LabelFrame(self.passions_window, text="Pride")
        self.disgrace_info = LabelFrame(self.passions_window, text="Disgrace")
        self.motivation_info = LabelFrame(self.passions_window, text="Motivation")
        self.set_passions = set_passions

    def details(self, listbox):
        def display_info(selection, details_box):
            for widget in details_box.winfo_children():
                widget.destroy()

            Label(details_box, text=selection['Name']).grid(row=0, column=0)
            Label(details_box, text=f"Characteristics Bonus : {selection['Characteristic Bonus'].title()}").grid(row=1, column=0)
            Label(details_box, text=f"Characteristics Penalty : {selection['Characteristic Penalty'].title()}").grid(row=2, column=0)
            if type(selection['Special Modifier']) != float:
                Label(details_box, text=f"Special Modifier").grid(row=1, column=1)
                Label(details_box, text=selection['Special Modifier']).grid(row=2, column=1)
            Label(details_box, text=selection['Description'], wraplength=200).grid(row=3, column=0)

        choice = {}

        for passion in self.info:
            if passion.get('Name') == listbox.get(ANCHOR):
                choice = passion
                self.choices = {**self.choices, passion['Type']: passion}

        try:
            if choice['Type'] == 'Pride':
                display_info(choice, self.pride_info)
            elif choice['Type'] == 'Disgrace':
                display_info(choice, self.disgrace_info)
            elif choice['Type'] == 'Motivation':
                display_info(choice, self.motivation_info)
        except KeyError:
            pass

        self.pride_info.grid(row=1, column=0, sticky=N)
        self.disgrace_info.grid(row=1, column=1, sticky=N)
        self.motivation_info.grid(row=1, column=2, sticky=N)

    def populate_listbox(self, listbox, items):
        for index, item in enumerate(items):
            listbox.insert(index, item['Name'])
        listbox.bind('<Button>', lambda e: self.details(listbox))

    def show_info(self):
        prides = [x for x in self.info if x['Type'] == 'Pride']
        disgraces = [x for x in self.info if x['Type'] == 'Disgrace']
        motivations = [x for x in self.info if x['Type'] == 'Motivation']

        pride_listbox = Listbox(self.passions_window)
        disgrace_listbox = Listbox(self.passions_window)
        motivation_listbox = Listbox(self.passions_window)

        self.populate_listbox(pride_listbox, prides)
        self.populate_listbox(disgrace_listbox, disgraces)
        self.populate_listbox(motivation_listbox, motivations)

        pride_listbox.grid(row=0, column=0)
        disgrace_listbox.grid(row=0, column=1)
        motivation_listbox.grid(row=0, column=2)

    def choose_passions(self):
        # pp(self.choices)
        self.set_passions(self.choices)
        self.passions_window.grab_release()
        self.passions_window.destroy()

    def create(self):
        self.passions_window.title('Select Passions')
        self.passions_window.grab_set()
        self.passions_window.geometry('800x600')

        select_button = Button(self.passions_window, text='Choose Passions', command=self.choose_passions)
        select_button.grid(row=2, columnspan=3, sticky=S)

        self.show_info()
