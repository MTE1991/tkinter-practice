import tkinter as tk

root = tk.Tk()
root.title("Resizing windows")
root.geometry("640x480+50+50")
msg = tk.Label(root, text="This window is only resizable until 800x600! It's 70% transparent. It will remain always on "
                          "top. It has a custom icon.")  # places a label on the root window
msg.pack()  # positions the Label on the main window
root.resizable(True, True)  # window.resizable(width, height)
root.maxsize(800, 600)
root.attributes("-alpha", 0.7)  # set alpha channel to be 70% transparent
root.attributes("-topmost", 1)  # sets window always on top of the stacking order
root.iconbitmap("demo_icon.ico")  # sets a custom icon for the window

root.mainloop()
