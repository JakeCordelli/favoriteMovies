#The purpose of this python script is to read from the DB,
#format the information, and output a json file for plotting

from flask import Flask, render_template, request
import sqlite3 as sql
from nameToPlots import *
import json


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
    #print(x, y, z)
    return (j)


def returnJson():
    #will print all needed information for grpahing
    data=addFromDB()
    print(data)

    #Feed this data into a dictionary for json conversion
    somedict = { "xCos"     : [ x[0] for x in data ],
                 "yCos"     : [ x[1] for x in data ],
                 "title"     : [ x[2] for x in data ],
               }
    #print json.dumps(somedict)
    # Export this information as a json
    with open('data.txt', 'w') as outfile:
        x=json.dump(data, outfile)

    return(x)
returnJson()
