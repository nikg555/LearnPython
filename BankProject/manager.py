import tkinter as tk
from tkinter import ttk,messagebox


def show():
    root=tk.Tk()
    root.title("MANAGER")
    root.geometry("500x500")

    tk.Label(root, text="Welcome to Manager").pack(pady=30)

    tk.Button(root, text="Manage Customers").pack(pady=5)
    tk.Button(root, text="Approve Loans").pack(pady=5)
    tk.Button(root, text="Branch Report").pack(pady=5)

    root.mainloop()