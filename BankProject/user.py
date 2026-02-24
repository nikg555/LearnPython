import tkinter as tk
from tkinter import ttk,messagebox


def show():
    root=tk.Tk()
    root.title("USER")
    root.geometry("500x500")

    tk.Label(root, text="Welcome to User").pack(pady=30)

    tk.Button(root, text="Manage Users").pack(pady=5)
    tk.Button(root, text="View System Reports").pack(pady=5)
    tk.Button(root, text="Manage Branches").pack(pady=5)

    root.mainloop()