# event handling (multiple handlers for same event)
import tkinter as tk
from tkinter import ttk

def return_pressed(event):
    print("Return key pressed.")

def log(event):
    print(event)

root = tk.Tk()

btn = ttk.Button(root, text="Save")  # create a button

# bind return_pressed function to the Return (Enter) key
btn.bind("<Return>", return_pressed)
# also bind log to the retun key
btn.bind("<Return>", log, add="+")
btn.focus() # refers to the widget or window which is currently accepting input
btn.pack(expand=True)

root.mainloop()