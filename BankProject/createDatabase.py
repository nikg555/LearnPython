import tkinter as tk
from tkinter import ttk,messagebox
import pandas as pd
import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_database"
)
cursor = conn.cursor()

cursor.execute("""
INSERT INTO loans (loan_id, customer_id, loan_type, amount, status, issue_date) VALUES
(1, 1, 'home', 120000.00, 'approved', '2022-05-20'),
(2, 2, 'car', 25000.00, 'pending', '2023-03-10'),
(3, 3, 'education', 18000.00, 'approved', '2021-07-22'),
(4, 4, 'personal', 10000.00, 'defaulted', '2020-10-15'),
(5, 5, 'home', 95000.00, 'rejected', '2023-01-08');
 """)
conn.commit()
print("Data Inserted Successfully!")
root = tk.Tk()
root.title("Bank Management System")
root.geometry("900x600")


columns = ("account_id", "customer_name","account_number", "account_type", "balance","branch_name","city","phone","email","status","created_date")
tree = ttk.Treeview(root, columns=columns, show="headings")

for col in columns:
    tree.heading(col, text=col)
    tree.column(col, width=120)

tree.pack(fill=tk.BOTH, expand=True)

def load_data(query):
    for row in tree.get_children():
     tree.delete(row)
    df=pd.read_sql(query,conn)   
    for _, row in df.iterrows():
      tree.insert("",tk.END, values=list(row))


def show_all():
  load_data("SELECT * FROM bank_account")

def show_name_accno_balance():
  load_data("SELECT account_id, customer_name, account_number, balance FROM bank_account")

def show_active():
    load_data("SELECT * FROM bank_account WHERE status = 'Active'")

def show_savings():
    load_data("SELECT * FROM bank_account WHERE account_type = 'Savings'")

def show_after_2023():
    load_data("SELECT * FROM bank_account WHERE created_date > '2023-01-01'")

def show_balance_50k():
    load_data("SELECT * FROM bank_account WHERE balance > 50000")

def  show_city_moh():
    load_data("SELECT * FROM bank_account WHERE city = 'MOH'")

def show_count():
    cursor.execute("SELECT COUNT(*) AS total_accounts FROM bank_account")
    result = cursor.fetchone()
    messagebox.showinfo("Total Accounts", f"Total Accounts: {result[0]}")

def show_avg_balance():
    cursor.execute("SELECT AVG(balance) AS average_balance FROM bank_account")
    result = cursor.fetchone()
    messagebox.showinfo("Average Balance", f"Average Balance: ₹{round(result[0], 2)}")


def show_order_balance():
    load_data("SELECT * FROM bank_account ORDER BY balance DESC")

def show_highest():
    load_data("SELECT * FROM bank_account WHERE balance = (SELECT MAX(balance) FROM bank_account)")

def show_branch_balance():
    cursor.execute("SELECT branch_name, SUM(balance) AS total_balance FROM bank_account GROUP BY branch_name")
    rows = cursor.fetchall()
    result = "\n".join([f"{row[0]} : ₹{row[1]}" for row in rows])
    messagebox.showinfo("Branch-wise Balance", result)

def show_duplicate_phone():
    cursor.execute("SELECT phone, COUNT(*) AS count FROM bank_account GROUP BY phone HAVING COUNT(*) > 1")
    rows = cursor.fetchall()
    if rows:
        result = "\n".join([f"Phone: {row[0]} Count: {row[1]}" for row in rows])
        messagebox.showinfo("Duplicate Phones", result)
    else:
        messagebox.showinfo("Duplicate Phones", "No Duplicate Phone Numbers Found!")

def show_inactive_zero():
    load_data("SELECT * FROM bank_account WHERE status = 'Inactive' AND balance = 0")


    frame=tk.Frame(root)
    frame.pack(pady=10)
    
btn_frame = tk.Frame(root)
btn_frame.pack(pady=8)
tk.Button(btn_frame,text="show_all", width=15,command=show_all).grid(row=0,column=0,padx=5)
tk.Button(btn_frame,text="show_name_accno_balance", width=15,command=show_name_accno_balance).grid(row=0,column=1,padx=5)
tk.Button(btn_frame,text="show_active", width=15,command=show_active).grid(row=0,column=2,padx=5)
tk.Button(btn_frame,text="show_savings", width=15,command=show_savings).grid(row=0,column=3,padx=5)
tk.Button(btn_frame,text="show_after_23", width=15,command=show_after_2023).grid(row=0,column=4,padx=5)
tk.Button(btn_frame,text="show_balance_50k", width=15,command=show_balance_50k).grid(row=0,column=5,padx=5)
tk.Button(btn_frame,text="show_city_moh", width=15,command=show_city_moh).grid(row=0,column=6,padx=5)
tk.Button(btn_frame,text="show_count", width=15,command=show_count).grid(row=0,column=7,padx=5)
tk.Button(btn_frame,text="show_avg_balance", width=15,command=show_avg_balance).grid(row=0,column=8,padx=5)
tk.Button(btn_frame,text="show_order_balance", width=15,command=show_order_balance).grid(row=0,column=9,padx=5)
tk.Button(btn_frame,text="show_highest", width=15,command=show_highest).grid(row=0,column=10,padx=5)
tk.Button(btn_frame,text="show_branch_balance", width=15,command=show_branch_balance).grid(row=0,column=11,padx=5)
tk.Button(btn_frame,text="show_duplicate_phone", width=15,command=show_duplicate_phone).grid(row=0,column=12,padx=5)
tk.Button(btn_frame,text="show_inactive_zero", width=15,command=show_inactive_zero).grid(row=0,column=13,padx=5)

show_all()
root.mainloop()