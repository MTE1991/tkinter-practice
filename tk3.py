# make a cross platform app
import tkinter as tk
from ctypes import windll

try:
    windll.shcore.SetProcessDpiAwareness(1)

    root = tk.Tk()
    msg = tk.Label(root, text="Hello, world!")
finally:
    root.mainloop()