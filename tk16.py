import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# create the root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Label Widget Image')

# display an image label
photo = ImageTk.PhotoImage(Image.open("me.PNG"))
image_label = ttk.Label(
    root,
    image=photo,
    text="HELLO, WORLD FROM MT EKLEEL",
    compound='top'
)
image_label.pack()

root.mainloop()
