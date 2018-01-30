'''The purpose of this program is to create a coordinate for a movie rating'''
'''This program includes code from aaazzz directly rather than by reference'''

'''Takes in the 3-letter code from turnTo3'''
'''Pairs it with the dictionary in aaazzz'''

from turnTo3 import turnTo3


'''Modify the code to reference csv rather than hash table'''
'''Generate a list of strings from AAA-ZZZ'''
import string

ltrs = list(string.ascii_lowercase)
'''x holds the list we need'''
x = [''.join([a, b, c]) for a in ltrs for b in ltrs for c in ltrs]
# print(x)

'''Map these strings to values in a dictionary'''
letterMap = {}
for i in range(17576):
    letterMap[x[i]] = i+1

'''Matches the generated 3 digit code to the dictionary and return the x,y coordinates for the point'''

'''Include code to export dictionary as a csv file'''
import csv
w = csv.writer(open("output.csv", "w"))
for key, val in letterMap.items():
    w.writerow([key, val])


import matplotlib.pyplot as plt

def assignValues(movieTitle, rating, seen):
    code = turnTo3(movieTitle)
    value = letterMap[code]

    '''This will be turned into a database entry'''
    movieList=[]
    movieList.append(movieTitle)

    '''This will make the code and values negative '''
    '''Items to the left of 0 are unseen'''
    if (seen==0):
        value=value*-1
        code=code*-1
    else:
        value=value
        code=code
    '''Plot the data points'''
    plt.plot(value, rating, marker='o', markersize=5, color="magenta")

    '''Add a division line at x=0'''
    plt.plot([0,0], [0,10], color='cyan')

    '''Add labels to the points'''
    plt.annotate(movieTitle, (value+10, rating), size='7')
    plt.suptitle('Representing Interest in Movies Seen & Unseen')
    plt.ylabel('Rating')
    plt.xlabel('Movies (Alphabetically)')

    return (value, rating)


'''Pull this information from the database'''
import sqlite3
connection = sqlite3.connect("movies.db")

cursor = connection.cursor()
cursor.execute("SELECT * FROM movies")
print("fetchall:")
result = cursor.fetchall()
x,y,z=0,0,0
movieList=[]
for r in result:
    print(r[1])

    #Add the movies from the database into a list (no reason)
    movieList.append(r[1])

    #Get information from each row
    x,y,z=r[1],r[2],r[3]
    assignValues(x, y, z)


plt.show()

