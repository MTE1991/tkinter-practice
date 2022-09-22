# tkinter buttons
# a program with an exit button

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry("640x480")
root.resizable(True, True)
root.title("Exit Buttons")
lbl = tk.Label(root, text="Click the button below to exit.")
lbl.pack(ipadx=10, ipady=80)

# exit button
btn = ttk.Button(
    root,
    text="Exit",
    command=lambda: root.quit()
)

btn.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()