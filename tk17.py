# same as earlier program, w/ an exit btn
from operator import truediv
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# create the root window
root = tk.Tk()
root.geometry('400x300')
root.resizable(True, True)
root.title('Image Label and Widgets')

# display an image label
photo = ImageTk.PhotoImage(Image.open("me.PNG"))
image_label = ttk.Label(
    root,
    image=photo,
    text="HELLO, WORLD FROM MT EKLEEL",
    compound='bottom'  # image will be placed in the bottom
)
image_label.pack()

# button click event
def btn_click():
    new_label = ttk.Label(root, text="Thanks for clicking me!")
    new_label.pack()

# create a button
btn = ttk.Button(
    root,
    text="Click Here!",
    command=btn_click
)

btn.pack(
    ipadx=10,
    ipady=5,
    expand=True
)

root.mainloop()