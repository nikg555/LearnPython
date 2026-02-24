import tkinter as tk
from tkinter import ttk,messagebox
import pymysql
import admin
import customer

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_database"
)

cursor = conn.cursor()

def Register():
   name=user_name.get()
   password=entry_pass.get()
   address=entry_address.get()
   cursor.execute("insert into login values('"+name+"' , '"+password+"', '"+address+"')")
   conn.commit()
   data=cursor.fetchall()
   messagebox.showinfo("Success", "User REgistered")
   

root=tk.Tk()
root.title("Bank login")
root.geometry("500x400")

tk.Label(root,text="BANK LOGIN").pack(pady=10)

tk.Label(root,text="Username").pack(pady=5)
user_name=tk.Entry(root)
user_name.pack (pady=5)

tk.Label(root,text="password").pack(pady=5)
entry_pass=tk.Entry(root)
entry_pass.pack(pady=5)

tk.Label(root,text="address").pack(pady=5)
entry_address=tk.Entry(root)
entry_address.pack(pady=5)

tk.Button(root,text="Login",command=Register).pack(pady=5)
root.mainloop()