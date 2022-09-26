from tkinter import *
from tkinter import ttk


class AdvancementsPage:
    def __init__(self, root, character):
        self.root = root
        self.character = character

    def xp(self):
        xp_frame = LabelFrame(self.root, text="Experience Points")
        xp_label = Label(xp_frame, text=f'{self.character["spent_xp"]} xp / {self.character["total_xp"]} xp')
        avail_xp_label = Label(xp_frame, text=f'Available XP: {self.character["total_xp"]-self.character["spent_xp"]}')
        xp_label.grid(row=0, column=0)
        avail_xp_label.grid(row=0, column=1)

        xp_frame.grid(row=0, column=0)

    def alignment(self):
        alignment_box = LabelFrame(self.root, text='Alignment')

        khorne = Label(alignment_box, text=f'Khorne: {self.character["total_alignments"]["khorne"]}')
        nurgle = Label(alignment_box, text=f'Nurgle: {self.character["total_alignments"]["nurgle"]}')
        slaanesh = Label(alignment_box, text=f'Slaanesh: {self.character["total_alignments"]["slaanesh"]}')
        tzeentch = Label(alignment_box, text=f'Tzeentch: {self.character["total_alignments"]["tzeentch"]}')
        unaligned = Label(alignment_box, text=f'Unaligned: {self.character["total_alignments"]["unaligned"]}')

        khorne.grid(row=1, column=0)
        nurgle.grid(row=1, column=1)
        slaanesh.grid(row=2, column=0)
        tzeentch.grid(row=2, column=1)
        unaligned.grid(row=3, column=0, columnspan=2)

        alignment_box.grid(row=0, column=1)

    def advancements(self):
        advancements_frame = LabelFrame(self.root, text="Advancements")
        for advancement in self.character["purchased_advancements"]:
            advancement_label = Label(advancements_frame, text=advancement["name"])
            advancement_label.grid(sticky=W)
        advancements_frame.grid(row=1, column=0)

    def mutations(self):
        mutations_frame = LabelFrame(self.root, text="Gifts from the Gods")
        for mutation in self.character["mutations"]:
            mutation_label = Label(mutations_frame, text=mutation["name"])
            mutation_label.grid()
        mutations_frame.grid(row=1, column=1, sticky=N)

    def selection(self):
        selection_frame = LabelFrame(self.root, text="Info")

        # TODO: Create functionality for clicking something on this tab and it appearing in the frame
        selection_label = Label(selection_frame,
                                text="TODO: Grab the functionality from other tabs, and put it here")
        selection_label.grid(sticky=N)

        selection_frame.grid(row=1, column=2)

    def create(self):
        self.xp()
        self.alignment()
        self.advancements()
        self.mutations()
        self.selection()
        # TODO: Add new advancements button
