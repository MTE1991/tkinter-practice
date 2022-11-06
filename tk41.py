import tkinter as tk
from tkinter import ttk, Tk
from tkinter.messagebox import showinfo
from tkinter.scrolledtext import ScrolledText

root = Tk()
root.title("Text Editor (pre-alpha)")
root.geometry("600x450")
root.resizable(True, True)
root.rowconfigure(3, weight=1)
root.columnconfigure(2, weight=1)

# name entry
nameLabel = ttk.Label(root, text="File name:")
nameLabel.grid(column=0, row=0)

nameEntry = ttk.Entry(root)
nameEntry.grid(column=1, row=0)
nameEntry.focus()

# extension entry
extLabel = ttk.Label(root, text="Extension:")
extLabel.grid(column=0, row=1)

extEntry = ttk.Entry(root)
extEntry.grid(column=1, row=1)

# fonts
fonts = {
    "Calibri",
    "Times New Roman",
    "Arial",
    "Lucida Console"
}

# drop down menu for font selection
clicked = tk.StringVar()
clicked.set("Calibri")

dropLbl = ttk.Label(root, text="Font:")
dropLbl.grid(column=0, row=2, sticky=tk.W)

dropDown = tk.OptionMenu(root, clicked, *fonts)
dropDown.grid(column=1, row=2, sticky=tk.W)

# Scroll text box
text = ScrolledText(root, width=65, height=20)
text.grid(column=0, row=3, sticky=tk.EW, padx=5, pady=5, columnspan=6)
text.insert('1.0', 'Type something here...\n')

# event handling
def disableText():
    text['state'] = 'disabled'

def enableText():
    text['state'] = 'normal'

def textOut():
    txt = text.get('1.0','end')
    if nameEntry.get() != "":
        with open(f"{nameEntry.get()}.{extEntry.get()}",'w',encoding = 'utf-8') as f:
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
btn1.grid(column=2, row=4, sticky=tk.SE)

btn2 = ttk.Button(
    root,
    text="Disable Edit",
    command=disableText
)
btn2.grid(column=3, row=4, sticky=tk.SE)

btn3 = ttk.Button(
    root,
    text="Output file",
    command=textOut
)
btn3.grid(column=4, row=4, sticky=tk.SE)

root.mainloop()
