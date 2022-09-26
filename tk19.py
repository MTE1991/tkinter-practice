# image button
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from PIL import Image, ImageTk

# root window
root = tk.Tk()
root.geometry('300x200')
root.resizable(True, True)
root.title('Image Button Demo')


# download button callback function
def download_clicked():
    tk.messagebox.showinfo(
        title="Info",
        message="File downloaded succesfully!"
    )


download_icon = ImageTk.PhotoImage(Image.open("download.png"))
download_btn = ttk.Button(
    root,
    image=download_icon,
    command=download_clicked
)

download_btn.pack(
    ipadx=5,
    ipady=5,
    expand=True
)

root.mainloop()