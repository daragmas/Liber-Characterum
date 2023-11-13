from tkinter import *
import pandas
from pprint import pprint as pp

selection = {}
spent_xp = 0


def create(root, disciplines, budget, character, talents, refresh):
    # TODO: Fix spent_xp not being 0 when closing screen and reopening
    spent_xp = 0

    data = pandas.read_json('./data/powers.json').to_dict('records')
    disciplines = disciplines.split(', ')
    all_powers = [power for power in data if power['Discipline'] in disciplines]
    selected_powers = []

    powers_window = Toplevel(root)
    powers_window.grab_set()
    powers_window.title('Add Psychic Power')
    powers_window.geometry('1200x600')

    all_powers_frame = LabelFrame(powers_window, text='Powers')

    powers_list = Listbox(all_powers_frame, height=25)

    def fill_listbox():
        powers_list.delete(0, END)
        for index, power in enumerate(all_powers):
            addpowerbool = True

            # Characteristics Filtering
            try:
                for char, value in power['Prerequisites']['Characteristics'][0].items():
                    if character['characteristics'][char.lower()] < value:
                        addpowerbool = False
            except IndexError:
                pass

            # Powers Filtering
            try:
                # Prerequisite Powers Filtering
                for pow in power['Prerequisites']['Powers']:
                    selected_powers_names = [sel_pow['Name'] for sel_pow in selected_powers]
                    # print(selected_powers_names)
                    if pow not in selected_powers_names:
                        addpowerbool = False

                # Already Selected Filtering
                for sel_pow in selected_powers:
                    if power['Name'] == sel_pow['Name']:
                        addpowerbool = False
                # if power['Name'] in selected_powers:
                #     addpowerbool = False
            except IndexError:
                pass

            # Talents Filtering
            try:
                for talent in power['Prerequisites']['Talents']:
                    if 'Psy Rating' in talent:
                        if int(talent.split('g ')[1]) > int(talents[0].split(' ')[2]):
                            addpowerbool = False
                    elif '(Any)' in talent:
                        if talent.split(' (')[0] not in character['talents']:
                            addpowerbool = False
                    elif talent not in character['talents']:
                        addpowerbool = False
            except IndexError:
                pass

            if addpowerbool:
                powers_list.insert(index, power['Name'])

    fill_listbox()
    all_powers_frame.grid(row=0, column=0, sticky='NW')
    powers_list.grid(row=0, column=0, sticky='NW')

    info_frame = LabelFrame(powers_window, text='Powers Info')

    def show_details(clicked_list):
        for widget in info_frame.winfo_children():
            widget.destroy()

        for power in data:
            if clicked_list.get(ANCHOR) == power.get('Name'):
                global selection
                selection = power

        name = LabelFrame(info_frame, text='Name')
        alt_names = LabelFrame(info_frame, text='Alternate Names')
        xp_value = LabelFrame(info_frame, text='Value')
        prereqs = LabelFrame(info_frame, text='Prerequisites')
        action = LabelFrame(info_frame, text='Action')
        focus = LabelFrame(info_frame, text='Focus Power')
        power_range = LabelFrame(info_frame, text='Range')
        sustained = LabelFrame(info_frame, text='Sustained')
        subtype = LabelFrame(info_frame, text='Subtype')
        discipline = LabelFrame(info_frame, text='Discipline')
        description = LabelFrame(info_frame, text='Description')

        try:
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
        except UnboundLocalError:
            pass

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

    info_frame.grid(row=0, column=1, rowspan=25, sticky='NW')
    powers_list.bind('<Button>', lambda e: show_details(powers_list))

    # SELECTED POWER LIST
    selected_powers_frame = LabelFrame(powers_window, text="Selected Powers")
    selected_powers_list = Listbox(selected_powers_frame, height=25)

    selected_powers_list.bind('<Button>', lambda e: show_details(selected_powers_list))

    # Fill listbox with selected powers

    selected_powers_list.grid(sticky='NW')
    selected_powers_frame.grid(row=0, column=2, sticky='NW')

    # BUDGET LEFT LABEL
    budget_frame = LabelFrame(powers_window, text='Budget')
    budget_label = Label(budget_frame, text=f'{int(budget - spent_xp)} / {int(budget)} xp')
    budget_label.grid(sticky="N")
    budget_frame.grid(row=2, column=0, sticky='NW')

    # ADD/Remove POWER TO SELECTED BUTTON

    def fill_selected_listbox():
        selected_powers_list.delete(0, END)

        for index, power in enumerate(selected_powers):
            selected_powers_list.insert(index, power['Name'])

        fill_listbox()

    def add_selection():
        selected_powers.append(selection)
        # pp(selected_powers)
        global spent_xp
        spent_xp += int(selection['Value'].split('x')[0])
        budget_label.configure(text=f'{int(budget - spent_xp)} / {int(budget)} xp')

        fill_selected_listbox()

    def remove_selection():
        # print(selected_powers)
        # TODO: Add check to prevent prerequisite powers being removed before subsequent power
        selected_powers.remove(selection['Name'])
        global spent_xp
        spent_xp -= int(selection['Value'].split('x')[0])
        budget_label.configure(text=f'{int(budget - spent_xp)} / {int(budget)} xp')

        fill_selected_listbox()

    # TODO: Add check to disable add button when there isn't enough xp in the budget for the selected power
    add_power_to_selected = Button(powers_window, text='Add to Selected', command=add_selection)
    add_power_to_selected.grid(row=1, column=0, sticky='NW')

    # TODO: Disable remove button when selected list is empty?
    remove_power_from_selected = Button(powers_window, text='Remove from Selected', command=remove_selection)
    remove_power_from_selected.grid(row=1, column=1, sticky='NW')

    # FINISH SELECTION BUTTON
    def finish():
        powers_window.grab_release()
        powers_window.destroy()
        refresh(selected_powers)

    finish_selection_button = Button(powers_window, text='Finish Selection', command=finish)
    finish_selection_button.grid(row=2, column=2, sticky='NW')

    # fill_listbox(powers_list, power_filter=power_filter, character=character)
    #
    # pp(disciplines)
    # pp(budget)
    # pp(character)
