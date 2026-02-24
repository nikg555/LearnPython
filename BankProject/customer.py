import tkinter as tk

def show():
    root = tk.Tk()
    root.title("Customer Panel")
    root.geometry("500x400")

    tk.Label(root, text="Welcome to Customer" ).pack(pady=30)

    tk.Button(root, text="View Balance").pack(pady=5)
    tk.Button(root, text="Apply Loan").pack(pady=5)
    tk.Button(root, text="Download Statement").pack(pady=5)

    root.mainloop()