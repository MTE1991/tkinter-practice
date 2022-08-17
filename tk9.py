# 3) Using the config() method with keyword attributes
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

label = ttk.Label(root)
label.config(text='Hi, there')
label.pack()

root.mainloop()