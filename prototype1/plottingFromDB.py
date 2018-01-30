from flask import Flask, render_template, request
import sqlite3 as sql
from nameToPlots import *
import mpld3
from mpld3 import plugins
import numpy as np

#Collect the information from the database
def addFromDB():
    con = sql.connect("movies.db")
    con.row_factory = sql.Row

    '''Pull this information from the database'''
    cursor = con.cursor()
    cursor.execute("SELECT * FROM movies")
    print("fetchall:")
    result = cursor.fetchall()
    x, y, z = 0, 0, 0
    j=[]
    for r in result:
        # Get information from each row
        x, y, z = r[0], r[1], r[2]
        j.append(assignValues(x, y, z))
    con.close()

    #j is a list of ordered pairs
    return (j)

import matplotlib.pyplot as plt

#plot the information from the database and return a graph
def plotFromDB():
    #Generating points
    j=addFromDB()
    codes=[]
    ratings=[]
    movieNames=[]
    for i in range(len(j)):
        codes.append(j[i][0])
        ratings.append(j[i][1])
        movieNames.append(j[i][2])

        '''Plot the data points'''
        plt.plot(codes[i], ratings[i], marker='o', markersize=5, color="magenta")

        '''Add labels to the points'''
        plt.annotate(movieNames[i], (codes[i] + 10, ratings[i]), size='7')


    '''Add a division line at x=0'''
    plt.plot([0,0], [0,10], color='cyan')
    plt.suptitle('Representing Interest in Movies seen& Unseen')
    plt.ylabel('Rating')
    plt.xlabel('Movies (Alphabetically)')
    plt.savefig('static/images/graph.png')

plotFromDB()




