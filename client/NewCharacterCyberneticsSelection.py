from tkinter import *
import pandas
import pprint as pp


def create(root):
    data = pandas.read_csv('/data/cybernetics.csv').to_dict('records')

    cybernetics_window = Toplevel(root)
    cybernetics_window.grab_set()
    cybernetics_window.title('Select Cybernetic Enhancement')
    cybernetics_window.geometry('800x600')

    list_frame = LabelFrame(cybernetics_window,text='Cybernetics')

    cybernetics_list = Listbox(list_frame, height=25)

    def fill_cybernetics_list():
        cybernetics_list.delete(0,END)

    fill_cybernetics_list()