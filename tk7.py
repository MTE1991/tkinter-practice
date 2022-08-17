# 3 Ways to Set Options for a Tk Themed Widget
# 1) Using keyword arguments when creating the widget
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
ttk.Label(root, text="Hi, there!").pack()

root.mainloop()

# continued in tk8 onwards
