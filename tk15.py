import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.geometry('300x200')
root.resizable(False, False)
root.title('Label Widget Demo')

# label with a specific font
label = ttk.Label(
    root,
    text='A Label with the Calibri font',
    font=("Calibri", 18))

label.pack(ipadx=10, ipady=10)

root.mainloop()
