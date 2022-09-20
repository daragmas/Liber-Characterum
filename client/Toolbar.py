from tkinter import *
from tkinter import ttk


class Toolbar:
    def __init__(self, root):
        self.root = root

    def create(self):
        toolbar = ttk.Frame(self.root)

        # File
        filelabel = Label(toolbar, text="File")
        fileoptions = ["New", "Open", "Save", "Export"]
        clicked = StringVar()
        clicked.set("")
        filedropdown = OptionMenu(toolbar, clicked, *fileoptions)
        filelabel.grid(column=0, row=0)
        filedropdown.grid(column=0, row=1)

        # Tools
        toolslabel = Label(toolbar, text="Tools")
        toolsoptions = ["Tool1", "Tool2", "Tool3", "Tool4"]
        clickedtools = StringVar()
        clickedtools.set("")
        toolsdropdown = OptionMenu(toolbar, clickedtools, *toolsoptions)
        toolslabel.grid(column=1, row=0)
        toolsdropdown.grid(column=1, row=1)

        # Special
        speciallabel = Label(toolbar, text="Special")
        specialoptions = ["Spec1", "Spec2", "Spec3", "Spec4"]
        clickedspecial = StringVar()
        clickedspecial.set("")
        specialdropdown = OptionMenu(toolbar, clicked, *specialoptions)
        speciallabel.grid(column=2, row=0)
        specialdropdown.grid(column=2, row=1)

        # Help
        helplabel = Label(toolbar, text="Help")
        helpoptions = ["Help1", "Help2", "Help3", "Help4"]
        clickedhelp = StringVar()
        clickedhelp.set("")
        helpdropdown = OptionMenu(toolbar, clickedhelp, *helpoptions)
        helplabel.grid(column=3, row=0)
        helpdropdown.grid(column=3, row=1)

        toolbar.grid()
