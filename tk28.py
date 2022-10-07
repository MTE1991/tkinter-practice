# swapping colors
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side="top")

# box 2
box2 = tk.Label(root, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side="bottom")

# callback function to swap colors
def swapColors():
	box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side="top")
	box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side="bottom")

# Button
btn = ttk.Button(
    root,
    text="Click Here!",
    command=swapColors
)

btn.pack(
    ipadx=10,
    ipady=10,
    expand=True,
    fill=tk.BOTH
)

root.mainloop()