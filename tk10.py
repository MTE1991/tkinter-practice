# Tkinter command binding
import tkinter as tk
from tkinter import ttk

root = tk.Tk()


# this callback function will be called on button click
def button_clicked():
    print("Button is pressed!")


button = ttk.Button(root, text="Click Here", command=button_clicked)
button.pack()

root.mainloop()
