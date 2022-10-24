from tkinter import *
from tkinter import ttk
import pandas
from pprint import pprint as pp


# pp(data)
data = pandas.read_csv('./data/powers.csv').to_dict('records')


def create(root):
    def show_details():
        for widget in details_frame.winfo_children():
            widget.destroy()

        selection = {}

        for power in data:
            if powers_list.get(ANCHOR) == power.get('Name'):
                selection = power

        name = LabelFrame(details_frame, text='Name')
        alt_names = LabelFrame(details_frame, text='Alternate Names')
        xp_value = LabelFrame(details_frame, text='Value')
        prereqs = LabelFrame(details_frame, text='Prerequisites')
        action = LabelFrame(details_frame, text='Action')
        focus = LabelFrame(details_frame, text='Focus Power')
        power_range = LabelFrame(details_frame, text='Range')
        sustained = LabelFrame(details_frame, text='Sustained')
        subtype = LabelFrame(details_frame, text='Subtype')
        description = LabelFrame(details_frame, text='Description')

        Label(name, text=selection['Name']).grid()
        Label(alt_names, text=selection['Alternate Names']).grid()
        Label(xp_value, text=selection['Value']).grid()
        Label(prereqs, text=selection['Prerequisites']).grid()
        Label(action, text=selection['Action']).grid()
        Label(focus, text=selection['Focus Power']).grid()
        Label(power_range, text=selection['Range']).grid()
        Label(sustained, text=selection['Sustained']).grid()
        Label(subtype, text=selection['Subtype']).grid()
        Label(description, text=selection['Description'], wraplength=600).grid()

        name.grid(row=0, column=0, sticky=NW)
        alt_names.grid(row=0, column=1, sticky=NW)
        xp_value.grid(row=2, column=0, sticky=NW)
        prereqs.grid(row=2, column=1, sticky=NW)
        action.grid(row=3, column=0, sticky=NW)
        focus.grid(row=3, column=1, sticky=NW)
        power_range.grid(row=4, column=0, sticky=NW)
        sustained.grid(row=4, column=1, sticky=NW)
        subtype.grid(row=8, column=0, sticky=NW)
        description.grid(row=9, column=0, columnspan=2, sticky=NW)
        details_frame.grid(row=1, column=1)

    powers_window = Toplevel(root)
    powers_window.grab_set()
    powers_window.title('Add Psychic Power')
    powers_window.geometry('800x600')

    powers_list = Listbox(powers_window, height=25)
    for index, power in enumerate(data):
        powers_list.insert(index, power['Name'])
    # TODO: Add Filter
    powers_list.grid(row=1, column=0, rowspan=9, sticky=NW)

    details_frame = LabelFrame(powers_window, text='Details')
    powers_list.bind('<Button>', lambda e: show_details())





