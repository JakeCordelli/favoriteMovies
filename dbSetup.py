import sqlite3

conn = sqlite3.connect('movies.db')

conn.execute('CREATE TABLE movies (movieName TEXT, rating INTEGER, seenUnseen INTEGER)')
conn.close()