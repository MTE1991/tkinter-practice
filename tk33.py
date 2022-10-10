import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Tkinter place Geometry Manager')
root.geometry("320x200")

# label 1
label1 = tk.Label(
    root,
    text="Absolute placement",
    bg='red',
    fg='white'
)

label1.place(x=20, y=10)

# label 2
label2 = tk.Label(
    root,
    text="Relative placement",
    bg='blue',
    fg='white'
)

# color changer callback function
def colorChange():
    label2.config(bg="red")
    label1.config(bg="blue")

# button
btn = ttk.Button(
    root,
    text="Swap colors",
    command=colorChange
)

btn.pack(padx=10, pady=10, expand=True, anchor=tk.S)

label2.place(relx=0.8, rely=0.2, relwidth=0.5, anchor='ne')

root.mainloop()
