import random
import tkinter as tk
from tkinter import *
import glob
import os

checkboxes = {}

def get_excuse():
    excuses = []

    for filename in checkboxes.keys():
        if checkboxes[filename].get():
            with open(filename) as f:
                excuses.extend((s.strip('\n') for s in f.readlines()))

    # If no lists are selected, ask user to select at least one list
    if not excuses:
        return "BRUH. Select at least one list!"

    # Get random excuse from compiled list
    idx = random.randint(0, len(excuses) - 1)
    return excuses[idx]

def regenerate_excuse():
    excuse["text"] = get_excuse()

# Root window
window = tk.Tk()
window.title("Gaming Excuse Generator")
window.minsize(300, 300)
window.rowconfigure([0, 1, 2, 3], minsize=0, weight=1)
window.columnconfigure(0, minsize=300, weight=1)

# Checkboxes
checkbox_frame = tk.Frame(window)
checkbox_inst = tk.Label(
    master=checkbox_frame,
    text="Select your excuse categories:",
    wraplength=280,
    anchor=N,
    font='Arial 10 underline'
)
checkbox_inst.pack()

for filename in glob.glob("**/*.txt", recursive=True):
    checkboxes[filename] = Variable(value=True)
    l = Checkbutton(checkbox_frame, text=os.path.splitext(filename)[0], variable=checkboxes[filename], onvalue=True, offvalue=False)
    l.pack()

checkbox_frame.grid(row=2, column=0)

# Excuse label
excuse = tk.Label(
    master=window,
    text=get_excuse(),
    wraplength=280,
    anchor=CENTER,
    font='Helvetica 14 bold',
    )
excuse.grid(row=0, column=0)

# Button
button = tk.Button(
    master=window,
    text="Get an excuse",
    command=regenerate_excuse,
    anchor=CENTER,
    height=2
    )
button.grid(row=1, column=0)

# Add custom excuses instructions label
custom_excuses_inst = tk.Label(
    master=window,
    text="To add custom excuses, enter new lines in the existing .txt files, or create your own files!",
    wraplength=280,
    anchor=CENTER,
    )
custom_excuses_inst.grid(row=3, column=0)

window.mainloop()