import tkinter as tk
from tkinter import Tk, Text

root = Tk()
root.resizable(True, True)
root.title("Text Widget Example")

text = Text(root, height=8)
text.pack(expand=True, fill=tk.BOTH)


root.mainloop()
