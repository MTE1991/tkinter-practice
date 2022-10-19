# bmi calculator ver 1.0

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x200")
root.resizable(True, True)
root.title("BMI Calculator 1.0")


def btn_clicked(event):
    """callback when calculate bmi btn is pressed"""
    try:
        h = float(height_entry.get())
        w = float(weight_entry.get())
        bmi = round(w / (h**2), 3)
        if bmi < 18.5:
            msg = f"Your BMI is {bmi}\nYou are underweight."
            showinfo(
                title="BMI Info",
                message=msg
            )
        elif bmi >= 18.5 and bmi <= 24.9:
            msg = f"Your BMI is {bmi}\nYou have normal weight."
            showinfo(
                title="BMI Info",
                message=msg
            )
        elif bmi >= 25 and bmi <= 29.1:
            msg = f"Your BMI is {bmi}\nYou are overweight."
            showinfo(
                title="BMI Info",
                message=msg
            )
        else:
            msg = f"Your BMI is {bmi}\nYou are very obese, lose weight immediately!"
            showinfo(
                title="BMI Info",
                message=msg
            )
    except:
        msg = f"Sorry, an error occured. Please try again with proper inputs."
        showinfo(
            title="BMI Info",
            message=msg
        )

# main frame
main = ttk.Frame(root)
main.pack(padx=10, pady=10, fill='x', expand=True)

# height
height_lbl = ttk.Label(main, text="Height (in m): ")
height_lbl.pack(fill='x', expand=True)

height_entry = ttk.Entry(main)
height_entry.pack(fill='x', expand=True)
height_entry.focus()

# weight
weight_lbl = ttk.Label(main, text="Weight (in kg): ")
weight_lbl.pack(fill='x', expand=True)

weight_entry = ttk.Entry(main)
weight_entry.pack(fill='x', expand=True)

# button
btn = ttk.Button(main, text="Calculate BMI", command=btn_clicked)
btn.bind("<Button-1>", btn_clicked)
btn.bind("<Return>", btn_clicked)
btn.pack(fill='x', expand=True, ipadx=10, ipady=10)

root.mainloop()