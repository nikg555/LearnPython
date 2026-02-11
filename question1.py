
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
question 1.

sum=0
i=1
for i in range(1,50):
 if(i%2!=0):
  sum=sum+1
  print(i)

j=1
while j<=50:
 if j%2!=0:
  print(j)
 j=j+1

question 2
num=1
while num<=10:
 print(num*5,end=" ")
 num=num+1

i=1
for i in range(1,10,1):
    print(i*5,end=" ")
question 3
j=7
while j>=1:
    print(j,end=" ")
    j=j-3

print(end="next answer ")

question:-

i=7 
for i in range (7,0,-3):
 print(i)

question:-

 sum=0
i=1
for i in range(1,101,1):
  if i%2==0:
   print(i,end=" ")

question:-

sum=0
i=1
while (i <= 100): 
   if i % 2 == 0:
    sum = sum + i
   i=i+1
  
print(sum)

question:-

for i in range(1,6,1):
    for j in range(5,5-i,-1):
        print(j,end=" ")
    print("\r")
for i in range(0,8,2):
    for j in range(7,i,-2):
        print(j,end=" ")
    print("\r")

question:-

for i in range(7,0,-2):
    for j in range(1,i+1,-2):
        print(j,end=" ")
    print("\r")

question:-

for i in range(0,10,3):
    for j in range(0,11-i,3):
        print(j,end=" ")
    print("\r")

question:-

for i in range(0,10,3):
    for j in range(9,i-1,-3):
        print(j,end=" ")
    print("\r")

question:-

num = 1
for i in range(1,5):
  rowNum = num
  for j in range(1,i+1):
   print(num,end=" ")
   if(num==1):
     num=0
   else:
     num=1
  if(rowNum==1):
     num=0
  else:
     num=1
  print("\r")
 
question:-

for i in range(0,6):
  num="*"

  for j in range(0,i):
   print(num,end=" ")  
  print("\r")
for i in range(0,6):
  num="*"
  for j in range(0,6-i):
    print(num,end=" ")
  
  print("\r")

  
question:-

  for i in range(0,4):
  num=1

  for j in range(0,i):
   print(num,end=" ")  
   num=num+1
  print("\r")
for i in range(0,4):
  num=1
  for j in range(0,4-i):
    print(num,end=" ")
    num=num+1
  print("\r")

 
question:-
for i in range(1,6,1):
    for j in range(1,i+1,1):
        print(j,end="")
    for j in range(i,12-i,1):
        print("-",end="")
    for j in range(5,5-i,-1):
        print(j,end="")
    print("\r")



def show(k,n):
    if(n<=5):
        show3(k,n)
        show2(10-2*(n-1))
        show1(6-n,n)
        print()
        show(k,n+1)

def show3(k,n):
      if( n == 0):
        return
    
      print(k,end="")
      show3(k+1,n-1)  
     
def show2(n):
    if(n<1):
        return
   
    print("-",end="")
    show2(n-1)

def show1(k,n):
    if(n==0):
        return
    print(k,end="")
    show1(k-1,n-1)
show(1,1)

while(n>0):
  r = r+ n%10
  n = n//10


def reverse_num(n):
    if n == 0:
        return          # stop recursion
    print(n % 10)
    reverse_num(n // 10)

reverse_num(1234)


banks = [
    {"bank_id": 101, "bank_name": "State Bank of India", "branch": "Delhi", "ifsc": "SBIN000101", "balance": 85000},
    {"bank_id": 102, "bank_name": "HDFC Bank", "branch": "Mumbai", "ifsc": "HDFC000102", "balance": 120000},
    {"bank_id": 103, "bank_name": "ICICI Bank", "branch": "Bangalore", "ifsc": "ICIC000103", "balance": 95000},
    {"bank_id": 104, "bank_name": "Axis Bank", "branch": "Chennai", "ifsc": "UTIB000104", "balance": 70000},
    {"bank_id": 105, "bank_name": "Punjab National Bank", "branch": "Amritsar", "ifsc": "PNB000105", "balance": 60000}
]



print("\n1. Display all bank details:")
for bank in banks:
    print(bank)

print("\n2. Bank name and branch where bank_id is 103:")
for bank in banks:
    if bank["bank_id"] == 103:
        print(bank["bank_name"], "-", bank["branch"])

print("\n3. Banks located in Mumbai:")
for bank in banks:
    if bank["branch"] == "Mumbai":
        print(bank)

print("\n4. Banks with balance greater than ₹80,000:")
for bank in banks:
    if bank["balance"] > 80000:
        print(bank["bank_name"], bank["balance"])

print("\n5. Total number of banks:")
print(len(banks))

print("\n6. IFSC code of Axis Bank:")
for bank in banks:
    if bank["bank_name"] == "Axis Bank":
        print(bank["ifsc"])

print("\n7. Bank with highest balance:")
highest = max(banks, key=lambda x: x["balance"])
print(highest["bank_name"], highest["balance"])

print("\n8. List of all bank names:")
for bank in banks:
    print(bank["bank_name"])

print("\n9. Banks with balance less than ₹70,000:")
for bank in banks:
    if bank["balance"] < 70000:
        print(bank["bank_name"], bank["balance"])

print("\n10. Check whether HDFC Bank exists:")
exists = any(bank["bank_name"] == "HDFC Bank" for bank in banks)
print(exists)

print("\n11. Update balance of ICICI Bank to ₹1,10,000:")
for bank in banks:
    if bank["bank_name"] == "ICICI Bank":
        bank["balance"] = 110000
        print(bank)

print("\n12. Delete bank record with bank_id 105:")
banks = [bank for bank in banks if bank["bank_id"] != 105]
for bank in banks:
    print(bank)

print("\n13. Sort banks by balance (ascending order):")
banks_sorted = sorted(banks, key=lambda x: x["balance"])
for bank in banks_sorted:
    print(bank["bank_name"], bank["balance"])

import matplotlib.pyplot as plt

 #Employee Department Data (List of Dictionaries)
employees = [
    {"emp_id": 1, "name": "Amit", "department": "HR", "salary": 45000},
    {"emp_id": 2, "name": "Neha", "department": "IT", "salary": 75000},
    {"emp_id": 3, "name": "Rahul", "department": "Finance", "salary": 68000},
    {"emp_id": 4, "name": "Priya", "department": "IT", "salary": 82000},
    {"emp_id": 5, "name": "Karan", "department": "Sales", "salary": 55000},
    {"emp_id": 6, "name": "Anita", "department": "HR", "salary": 60000}
]

# -------------------- QUERIES WITH ANSWERS --------------------

print("\n1. Display all employee details:")
for e in employees:
    print(e)

print("\n2. Total number of employees:")
print(len(employees))

print("\n3. List all employee names:")
for e in employees:
    print(e["name"])

print("\n4. Employees working in IT department:")
for e in employees:
    if e["department"] == "IT":
        print(e)

print("\n5. Employees with salary greater than 60000:")
for e in employees:
    if e["salary"] > 60000:
        print(e["name"], e["salary"])

print("\n6. Find employee with emp_id = 3:")
for e in employees:
    if e["emp_id"] == 3:
        print(e)

print("\n7. Highest salary employee (WITHOUT GRAPH):")
highest = max(employees, key=lambda x: x["salary"])
print(highest["name"], "-", highest["salary"])

print("\n8. Lowest salary employee:")
lowest = min(employees, key=lambda x: x["salary"])
print(lowest["name"], "-", lowest["salary"])

print("\n9. Count employees in HR department:")
count_hr = sum(1 for e in employees if e["department"] == "HR")
print(count_hr)

print("\n10. Update salary of Amit to 50000:")
for e in employees:
    if e["name"] == "Amit":
        e["salary"] = 50000
        print(e)

print("\n11. Delete employee with emp_id = 5:")
employees = [e for e in employees if e["emp_id"] != 5]
for e in employees:
    print(e)

print("\n12. Sort employees by salary (ascending):")
employees_sorted = sorted(employees, key=lambda x: x["salary"])
for e in employees_sorted:
    print(e["name"], e["salary"])

print("\n13. Check if employee Neha exists:")
exists = any(e["name"] == "Neha" for e in employees)
print(exists)

print("\n14. Print employee names with departments:")
for e in employees:
    print(e["name"], "-", e["department"])

print("\n15. Average salary of employees:")
avg_salary = sum(e["salary"] for e in employees) / len(employees)
print(avg_salary)

# -------------------- GRAPHS --------------------

# Graph 1: All Employee Names with Salary
names = [e["name"] for e in employees]
salaries = [e["salary"] for e in employees]

plt.figure()
plt.bar(names, salaries)
plt.title("Employee Salary Graph")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.show()

# Graph 2: Highest Salary Employee
plt.figure()
plt.bar(highest["name"], highest["salary"])
plt.title("Highest Salary Employee")
plt.xlabel("Employee Name")
plt.ylabel("Salary")
plt.show()

# Graph 3: Employee Name vs Department
departments = [e["department"] for e in employees]

plt.figure()
plt.bar(names, range(len(names)))
plt.xticks(names, departments)
plt.title("Employee and Department Graph")
plt.xlabel("Employee Name")
plt.ylabel("Department")
plt.show()

import matplotlib.pyplot as plt
data=[1,2,3,4,6,5]
plt.boxplot(data)
plt.xlabel("Catagories")
plt.ylabel("value")
plt.show()


import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

year = [2000, 2005, 2010, 2015, 2020, 2025, 2030]  
pop_india = [1050, 1140, 1230, 1310, 1380, 1420, 1450]
pop_pakistan = [138, 150, 167, 182, 197, 215, 225]

plt.plot(year,pop_pakistan,color="green")
plt.plot(year,pop_india,color="orange")
plt.xlabel('countreis')
plt.ylabel("population in mill")
plt.title("pakistan india population till 2010")
plt.show()

import numpy as np
print("===== BASIC ARRAY CREATION =====")
a = np.array([1, 2, 3, 4, 5])
b = np.array([[10, 20], [30, 40]])

print("Array a:", a)
print("Array b:\n", b)

# Array Creation Functions
print("\n===== ARRAY CREATION FUNCTIONS =====")
print("zeros():\n", np.zeros((2, 3)))
print("ones():\n", np.ones((3, 2)))
print("full():\n", np.full((2, 2), 9))
print("arange():", np.arange(1, 11, 2))
print("linspace():", np.linspace(1, 10, 5))
print("eye():\n", np.eye(3))


# Array Properties
print("\n===== ARRAY PROPERTIES =====")
print("Shape:", b.shape)
print("Size:", b.size)
print("Dimensions:", b.ndim)
print("Data Type:", b.dtype)

# Mathematical Functions
print("\n===== MATHEMATICAL FUNCTIONS =====")
x = np.array([1, 4, 9, 16])

print("sqrt():", np.sqrt(x))
print("power():", np.power(x, 2))
print("abs():", np.abs([-10, -5, 5]))
print("exp():", np.exp([1, 2]))
print("log():", np.log([1, 10, 100]))

# Statistical Functions
print("\n===== STATISTICAL FUNCTIONS =====")
data = np.array([10, 20, 30, 40, 50])

print("sum():", np.sum(data))
print("mean():", np.mean(data))
print("median():", np.median(data))
print("min():", np.min(data))
print("max():", np.max(data))
print("std():", np.std(data))
print("var():", np.var(data))

print("percentile:", np.percentile(data, 75))

                         
*       * 
*       * 
* * * * * 
*       * 
*       * 
for i in range(1,6):
    for j in range(1,6): 
     if i==3 or j==1 or j==5:
          
          print("*",end=" ")
          
     else:
          print(" ",end=" ")
    print("\r")
         

* * * * * 
  *       
    *     
      *   
* * * * * 


for i in range(1,6):
    for j in range(1,6): 
     if  i==1 or i==5 or j==i:
          print("*",end=" ")      
     else:
          print(" ",end=" ")
    print("\r")

    
     * 
    * * 
  * * * 
* * * * 
for i in range(1,6):
    for j in range (0,5-i):
      print(" ",end=" ")
    for k in range (1,i):
        print("*",end=" ")
    print("\r")

    
    # Indexing & Slicing
# -------------------------------------------------
print("\n===== INDEXING & SLICING =====")
arr = np.array([100, 200, 300, 400, 500])

print("First:", arr[0])
print("Last:", arr[-1])
print("Slice [1:4]:", arr[1:4])

# -------------------------------------------------
# Reshape & Flatten
# -------------------------------------------------
print("\n===== RESHAPE & FLATTEN =====")
arr2 = np.arange(1, 7)

print("Original:", arr2)
print("reshape(2,3):\n", arr2.reshape(2, 3))
print("flatten():", arr2.flatten())

# -------------------------------------------------
# Sorting & Searching
# -------------------------------------------------
print("\n===== SORTING & SEARCHING =====")
arr3 = np.array([30, 10, 50, 20])

print("sort():", np.sort(arr3))
print("argsort():", np.argsort(arr3))
print("where():", np.where(arr3 > 20))
print("argmax():", np.argmax(arr3))
print("argmin():", np.argmin(arr3))

# -------------------------------------------------
# Join & Split
# -------------------------------------------------
print("\n===== JOIN & SPLIT =====")
a1 = np.array([1, 2, 3])
a2 = np.array([4, 5, 6])

print("concatenate():", np.concatenate((a1, a2)))
print("hstack():", np.hstack((a1, a2)))#1 2 3 4 5 6 column side by side
print("vstack():\n", np.vstack((a1, a2)))# row wise

print("split():", np.split(np.arange(1, 7), 3))

# -------------------------------------------------
# Random Functions
# -------------------------------------------------
print("\n===== RANDOM FUNCTIONS =====")
print("rand():\n", np.random.rand(2, 2))
print("randint():", np.random.randint(1, 10, 5))
print("choice():", np.random.choice([10, 20, 30, 40]))

# -------------------------------------------------
# Linear Algebra
# -------------------------------------------------
print("\n===== LINEAR ALGEBRA =====")
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

print("dot():\n", np.dot(m1, m2))
print("transpose():\n", m1.T)
print("determinant():", np.linalg.det(m1))
print("inverse():\n", np.linalg.inv(m1))

# -------------------------------------------------
# Copy vs View
# -------------------------------------------------
print("\n===== COPY vs VIEW =====")
orig = np.array([1, 2, 3])
view = orig.view()
copy = orig.copy()

orig[0] = 100
print("Original:", orig)
print("View:", view)
print("Copy:", copy)

import pandas as pd

data = [10, 20, 30, 40]
s = pd.Series(data)
print(s)
====
data = [100, 200, 300]
index = ['Math', 'Science', 'English']
s = pd.Series(data, index=index)
print(s)

-
data = {'a': 1, 'b': 2, 'c': 3}
s = pd.Series(data)
print(s)

-
s = pd.Series([10, 20, 30], index=['x', 'y', 'z'])
print(s['y'])  # Output: 20

---
s = pd.Series([1, 2, 3])
print(s * 2)  # Multiply each element by 2

---
s = pd.Series([5, 10, 15, 20])
print(s[s > 10])
-
_______________________Data Frame 
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}

df = pd.DataFrame(data)
print(df)

---
data = [['Tom', 28], ['Jerry', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)
---
data = [['Tom', 28], ['Jerry', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

---
data = [['Tom', 28], ['Jerry', 22]]
df = pd.DataFrame(data, columns=['Name', 'Age'])
print(df)

---
print(df[df['Age'] > 25])
"""""""""""""""""

