from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Liber Characterum")
root.geometry("1200x600")

# Toolbar
toolbar = ttk.Frame(root)

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
toolsoptions = ["New", "Open", "Save", "Export"]
clickedtools = StringVar()
clickedtools.set("")
toolsdropdown = OptionMenu(toolbar, clickedtools, *toolsoptions)
toolslabel.grid(column=1, row=0)
toolsdropdown.grid(column=1, row=1)

# Special
speciallabel = Label(toolbar, text="Special")
specialoptions = ["New", "Open", "Save", "Export"]
clickedspecial = StringVar()
clickedspecial.set("")
specialdropdown = OptionMenu(toolbar, clicked, *specialoptions)
speciallabel.grid(column=2, row=0)
specialdropdown.grid(column=2, row=1)

# Help
helplabel = Label(toolbar, text="Help")
helpoptions = ["New", "Open", "Save", "Export"]
clickedhelp = StringVar()
clickedhelp.set("")
helpdropdown = OptionMenu(toolbar, clickedhelp, *helpoptions)
toolbar.grid()
helplabel.grid(column=3, row=0)
helpdropdown.grid(column=3, row=1)

# Character Selection
characterselection = ttk.Frame(root)
samplechars = ["Char1", "Char2", "Char3"]
for i in range(len(samplechars)):
    charlabel = Label(characterselection, text=samplechars[i])
    charlabel.grid(column=i, row=0)

characterselection.grid()

# Characteristics Page




root.mainloop()