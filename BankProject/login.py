import tkinter as tk
from tkinter import ttk,messagebox
import pymysql
import admin
import user
import manager

conn = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_database"
)

cursor = conn.cursor()

def Login():
   name=user_name.get()
   password=entry_pass.get()
   cursor.execute("SELECT * FROM login WHERE username='"+name+"' and password='"+password+"'")
   data=cursor.fetchone()
   
   print(data[1])
   print(name, password)
       
   if (data):
      if(data[0]=="admin" and data[1]=="admin"):
          messagebox.showinfo("Success", "Welcome Admin")
          admin.show()
      elif(data[0]=="manager" and data[1]=="manager"):
          messagebox.showinfo("Success", "Welcome Manager")
          manager.show()
      else:
            messagebox.showinfo("Success", "Welcome Customer")
            user.show()
   else:
      messagebox.showwarning("Error", "Invalid Username or Password")
      

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


tk.Button(root,text="Login",command=Login).pack(pady=5)
root.mainloop()