import csv
import sys
import matplotlib as plt

def findValue(movieName):
    code = turnTo3(movieName)
    value= 0
    listOfRows=[]
    with open('letterList.csv') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            listOfRows.append(row)


    for i in range (len(listOfRows)):
        if (listOfRows[i][0]==code):
            value=i

    return (value)

'''This program is designed to parse movie titles into 3-letter codes'''
'''The 3 letter codes will then be compared to the hash table created in aaazzz in order to determine
x-coordinates for plotting'''

def turnTo3(movieTitle):
    '''Include code to remove the'''
    theRemoved=movieTitle.replace("the ","")
    theRemoved=theRemoved.replace("The ","")

    '''Code to lowercase'''
    lowerCased=theRemoved.lower()
    #print(movieTitle)
    #print(theRemoved)

    code=lowerCased[:3]
    #print(code)
    return(code)

def assignValues(movieName, rating, seenUnseen):
    code = turnTo3(movieName)
    value = findValue(movieName)


    '''This will make the code and values negative '''
    '''Items to the left of 0 are unseen'''
    if(seenUnseen=='on'):
        seenUnseen=1
    if(seenUnseen=='off'):
        seenUnseen=0

    if (seenUnseen==0):
        value=value*-1
        code=code*-1
    else:
        value=value
        code=code

    return(value, rating, movieName)

#Can be attached to plotting method