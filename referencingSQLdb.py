import sqlite3
connection = sqlite3.connect("company.db")

cursor = connection.cursor()

cursor.execute("SELECT * FROM employee") 
print("fetchall:")
result = cursor.fetchall()

#Prints the first and last names of the users
dict={'First':1, 'Last': 2}
for r in result:
    print(r[dict['First']], ' ', r[dict['Last']])

cursor.execute("SELECT * FROM employee") 
print("\nfetch one:")
res = cursor.fetchone() 
print(res)
