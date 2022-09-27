import tkinter as tk
from tkinter import ttk 
from tkinter.messagebox import showinfo

# root window
root = tk.Tk()
root.geometry("300x150")
root.resizable(False, False)
root.title("Log in")

# store email address and password
email = tk.StringVar()
password = tk.StringVar()


def loginClicked():
	"""callback when login btn is clicked"""
	msg = f"Your email: {email.get()} and password: {password.get()}"
	showinfo(
		title="Information",
		message=msg 
	)

# sign in frame
signIn = ttk.Frame(root)
signIn.pack(padx=10, pady=10, fill="x", expand=True)

# email
emailLabel = ttk.Label(signIn, text="Email Address: ")
emailLabel.pack(fill="x", expand=True)

emailEntry = ttk.Entry(signIn, textvariable=email)
emailEntry.pack(fill="x", expand=True)
emailEntry.focus()  # focus on this entry after opening the app

# password
passwordLabel = ttk.Label(signIn, text="Password:")
passwordLabel.pack(fill='x', expand=True)

passwordEntry = ttk.Entry(signIn, textvariable=password, show="*")
passwordEntry.pack(fill='x', expand=True)

# Login btn
loginBtn = ttk.Button(signIn, text="Log in", command=loginClicked)
loginBtn.pack(fill="x", expand=True, pady=10)

root.mainloop()