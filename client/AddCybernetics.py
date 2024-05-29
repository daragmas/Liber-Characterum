from tkinter import *
import pandas

data = pandas.read_csv('./data/cybernetics.csv').to_dict('records')
selection = {}


def set_selected(cybernetics_list):
    for cybernetic in data:
        if cybernetics_list.get(ANCHOR) == cybernetic.get('Name'):
            global selection
            selection = cybernetic


def fill_listbox(listbox, character):
    listbox.delete(0, END)
    for index, cybernetic in enumerate(data):
        print(cybernetic)
        listbox.insert(index, cybernetic['Name'])
    listbox.grid(row=0, column=0, sticky=NW)


def create(root, character, new_cybernetic):
    def done():
        cybernetic_window.grab_release()
        cybernetic_window.destroy()
        new_cybernetic(selection)

    cybernetic_window = Toplevel(root)
    cybernetic_window.grab_set()
    cybernetic_window.title('Add Cybernetics')
    cybernetic_window.geometry('800x600')

    cybernetic_list = Listbox(cybernetic_window, height=25)
    fill_listbox(cybernetic_list, character=character)

    details_frame = LabelFrame(cybernetic_window, text='Details')

    def show_details():
        for widget in details_frame.winfo_children():
            widget.destroy()

        set_selected(cybernetic_list)

        name = LabelFrame(details_frame, text='Name')
        description = LabelFrame(details_frame, text='Description')

        try:
            Label(name, text=selection['Name']).grid()
            Label(description, text=selection['Description'], wraplength=600).grid()
        except UnboundLocalError:
            pass

        name.grid(row=0, column=0, sticky=NW)
        description.grid(row=6, column=0, columnspan=3, sticky=NW)
        details_frame.grid(row=0, column=1, sticky=NW)

    cybernetic_list.bind('<Button>', lambda e: show_details())

    add_cybernetic_button = Button(cybernetic_window, text='Add Cybernetic', command=done)
    add_cybernetic_button.grid(row=11, column=0, sticky=NW)
