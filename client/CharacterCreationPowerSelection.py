# TODO: Variables needed:
#   Powers Budget
#   Powers Discipline Options
#   New Character Stats for prereqs
#   Archetype Selection Window
# TODO: Create:
#   new window,
#   listbox of powers and info window,
#   listbox of selected powers,
#   label with remaining powers budget
# Functionality: See powers options available, choose powers from list,
# keep list of powers chosen, return chosen powers to archetype selection variables
from tkinter import *
import pandas


def create(root, disciplines, budget, character):
    data = pandas.read_json('./data/powers.json').to_dict('records')
    disciplines = disciplines.split(', ')
    all_powers = [power for power in data if power['Discipline'] in disciplines]
    print(all_powers)

    # powers_window = Toplevel(root)
    # powers_window.grab_set()
    # powers_window.title('Add Psychic Power')
    # powers_window.geometry('800x600')
    #
    # powers_list = Listbox(powers_window, height=25)
    # fill_listbox(powers_list, power_filter=power_filter, character=character)
    #
    print(disciplines)
    print(budget)
    print(character)
