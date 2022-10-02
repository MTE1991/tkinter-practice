import tkinter as tk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Box 1", bg="blue", fg="white")
box1.pack()

# box 2
box2 = tk.Label(root, text="Box 2", bg="green", fg="white")
box2.pack()

root.mainloop()