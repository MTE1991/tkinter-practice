# Text editor pre-alpha xD
import tkinter as tk
from tkinter import ttk, Tk, Text
from tkinter.messagebox import showinfo

root = Tk()
root.title("Text Editor WIP")
root.geometry("600x575")
root.resizable(False, False)

root.columnconfigure(1, weight=1) # Using grid geometry manager

nameLabel = ttk.Label(root, text="File name:")
nameLabel.grid(column=0, row=0, sticky=tk.W, columnspan=5)

nameEntry = ttk.Entry(root)
nameEntry.grid(column=0, row=1, sticky=tk.W, columnspan=5)
nameEntry.focus()

text = Text(root, height=30)
text.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5, columnspan=5)

text.insert('1.0', 'Type something here...\n')

# event handling
def disableText():
    text['state'] = 'disabled'

def enableText():
    text['state'] = 'normal'

def textOut():
    txt = text.get('1.0','end')
    if nameEntry.get() != "":
        with open(f"{nameEntry.get()}.txt",'w',encoding = 'utf-8') as f:
            f.write(txt)
    else:
        showinfo(
            title="Empty filename",
            message="File name is empty! Please enter a file name."
        )

# buttons
btn1 = ttk.Button(
    root,
    text="Enable Edit",
    command=enableText
)
btn1.grid(column=3, row=3, sticky=tk.SE)

btn2 = ttk.Button(
    root,
    text="Disable Edit",
    command=disableText
)
btn2.grid(column=4, row=3, sticky=tk.SE)

btn3 = ttk.Button(
    root,
    text="Output as .txt file",
    command=textOut
)
btn3.grid(column=5, row=3, sticky=tk.SE)

root.mainloop()
