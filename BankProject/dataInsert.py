import pymysql

conn=pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="bank_database"
)
name=input("enter email")
password=input("enter password")

cursor=conn.cursor()
cursor.execute("INSERT INTO login ('"+name+"','"+password+"')")
conn.commit()
print("data insert")