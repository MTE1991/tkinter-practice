import tkinter as tk
from tkinter import ttk

root = tk.Tk()

cars = ["Ferrari 488 GTB", "Lamborghini Huracan STO", "Maserati MC20"]


def select(option):
    if option == cars[0]:
        print("$262,800")
    elif option == cars[1]:
        print("$327,838")
    elif option == cars[2]:
        print("$250,000")


root.title("Supercar Prices")
root.geometry("300x200+40+40")
ttk.Label(root, text="Supercar prices")

ttk.Button(root, text=cars[0], command=lambda: select(cars[0])).pack()
ttk.Button(root, text=cars[1], command=lambda: select(cars[1])).pack()
ttk.Button(root, text=cars[2], command=lambda: select(cars[2])).pack()

root.mainloop()