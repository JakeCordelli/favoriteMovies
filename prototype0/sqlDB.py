import sqlite3
connection = sqlite3.connect("movies.db")

cursor = connection.cursor()

# delete
#cursor.execute("""DROP TABLE movies;""")

'''
sql_command = """
CREATE TABLE movies ( 
movie_number INTEGER PRIMARY KEY, 
mtitle VARCHAR(20), 
rating DOUBLE(2), 
seen INTEGER(2));"""

cursor.execute(sql_command)

'''


#This is the command for adding a movie to the database
sql_command = """INSERT INTO movies (movie_number, mtitle, rating, seen)
    VALUES (NULL, "Jumanji", 3, 1);"""
cursor.execute(sql_command)

# never forget this, if you want the changes to be saved:
connection.commit()


#Prints the information from the database
cursor = connection.cursor()

cursor.execute("SELECT * FROM movies")
print("fetchall:")
result = cursor.fetchall()
for r in result:
    print(r)
cursor.execute("SELECT * FROM movies")
print("\nfetch one:")
res = cursor.fetchone()
print(res)

connection.close()
