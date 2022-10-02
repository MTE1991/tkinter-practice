import tkinter as tk

root = tk.Tk()
root.title('Pack Demo')
root.geometry("350x200")

# box 1
box1 = tk.Label(root, text="Green color", bg="green", fg="white")
box1.pack(ipadx=55, ipady=10)

# box 2
box2 = tk.Label(root, text="Red colour", bg="red", fg="white")
box2.pack(ipadx=55, ipady=10)

root.mainloop()
