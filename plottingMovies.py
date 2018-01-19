'''The purpose of this program is to create a coordinate for a movie rating'''
'''This program includes code from aaazzz directly rather than by reference'''

'''Takes in the 3-letter code from turnTo3'''
'''Pairs it with the dictionary in aaazzz'''

from turnTo3 import turnTo3

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



'''Modify the code to reference csv rather than hash table'''







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
    plt.plot([0,0], [0,10])

    '''Add labels to the points'''
    plt.annotate(movieTitle, (value+10, rating), size='7')
    plt.suptitle('Representing Interest in Movies Seen & Unseen')
    plt.ylabel('Rating')
    plt.xlabel('Movies (Alphabetically)')

    return (value, rating)


assignValues("The godfather", 8, 1)
assignValues("Bee Movie", 6, 0)
assignValues("Brave Heart", 5, 0)
assignValues("Zoolander", 5, 0)
assignValues("Zongo", 10, 1)
assignValues("Jumanji: Welcome to the Jungle", 9, 0)
assignValues("Gayest movie ever made", 10, 0)
assignValues("Robocop", 2, 1)

'''When adding a datapoint next to another one very closely, there is stacking'''
assignValues("Jumanji", 7, 1)
assignValues("Jumbalaya", 7, 1)

import numpy as np



plt.show()




# def createCoordinate(movieTitle, rating):





