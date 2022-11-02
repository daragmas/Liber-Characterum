import tkinter
from tkinter import *
from tkinter import ttk
import pandas
from pprint import pprint as pp

# pp(data)
# data = pandas.read_csv('./data/powers.csv').to_dict('records')
data = pandas.read_json('./data/powers.json').to_dict('records')


def fill_listbox(listbox, power_filter, character):
    listbox.delete(0, END)
    for index, power in enumerate(data):
        # pp(power['Prerequisites'])
        if power_filter.get() == 1:
            if power['Prerequisites'] == ["None"]:
                print('No PreReq')
                listbox.insert(index, power['Name'])
            else:
                print(power['Prerequisites'])
                for prereq in power['Prerequisites']:
                    pass
        else:
            listbox.insert(index, power['Name'])
    # TODO: Add Filter


def create(root, character):
    # pp(character)
    # print('Add Power Alignment Check:', character['alignment'])

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
        discipline = LabelFrame(details_frame, text='Discipline')
        description = LabelFrame(details_frame, text='Description')

        Label(name, text=selection['Name']).grid()
        Label(alt_names, text=selection['Alternate Names']).grid()
        Label(xp_value, text=selection['Value']).grid()

        if selection['Prerequisites'] != ['None']:
            for prereq, value in selection['Prerequisites'].items():
                if value:
                    prereqCategory = LabelFrame(prereqs, text=prereq)
                    if type(value) != str:
                        for item in value:
                            try:
                                for characteristic, rating in item.items():
                                    Label(prereqCategory, text=f'{characteristic}: {rating}').grid(sticky=NW)
                            except AttributeError:
                                Label(prereqCategory, text=item).grid(sticky=NW)
                    else:
                        Label(prereqCategory, text=value).grid(sticky=NW)
                    prereqCategory.grid(sticky=NW)
        else:
            Label(prereqs, text='None').grid(sticky=NW)

        Label(action, text=selection['Action']).grid()
        Label(focus, text=selection['Focus Power']).grid()
        Label(power_range, text=selection['Range']).grid()
        Label(sustained, text=selection['Sustained']).grid()
        Label(subtype, text=selection['Subtype']).grid()
        Label(discipline, text=selection['Discipline']).grid()
        Label(description, text=selection['Description'], wraplength=600).grid()

        name.grid(row=0, column=0, sticky=NW)
        alt_names.grid(row=0, column=1, sticky=NW)
        xp_value.grid(row=1, column=0, sticky=NW)
        prereqs.grid(row=0, column=2, rowspan=5, sticky=NW)
        action.grid(row=2, column=0, sticky=NW)
        focus.grid(row=2, column=1, sticky=NW)
        power_range.grid(row=4, column=0, sticky=NW)
        sustained.grid(row=4, column=1, sticky=NW)
        subtype.grid(row=5, column=0, sticky=NW)
        discipline.grid(row=1, column=1, sticky=NW)
        description.grid(row=6, column=0, columnspan=3, sticky=NW)
        details_frame.grid(row=1, column=1, sticky=NW)

    powers_window = Toplevel(root)
    powers_window.grab_set()
    powers_window.title('Add Psychic Power')
    powers_window.geometry('800x600')

    powers_list = Listbox(powers_window, height=25)
    power_filter = IntVar(powers_window, 0, "powerFilter")
    fill_listbox(powers_list, power_filter=power_filter, character=character)
    filter_prereqs = Checkbutton(powers_window,
                                 text='Filter by prerequisites',
                                 variable=power_filter,
                                 onvalue=power_filter.set(1),
                                 offvalue=power_filter.set(0),
                                 command=lambda: fill_listbox(powers_list, power_filter, character))

    # TODO: Add Filter
    powers_list.grid(row=1, column=0, rowspan=9, sticky=NW)
    filter_prereqs.grid(row=0, column=0, sticky=NW)
    details_frame = LabelFrame(powers_window, text='Details')
    powers_list.bind('<Button>', lambda e: show_details())
