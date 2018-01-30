from flask import Flask, render_template, request
import sqlite3 as sql
from plottingFromDB import *
app=Flask(__name__)


@app.route('/')
def home():
    plotFromDB()
    return render_template("mainView.html")


@app.route('/', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            movieName = request.form['movieName']
            rating = request.form['rating']
            seenUnseen = request.form['seenUnseen']

            with sql.connect("movies.db") as con:
                cur = con.cursor()

                cur.execute("INSERT INTO movies (movieName, rating, seenUnseen)\
                VALUES(?, ?, ?)",(movieName,rating,seenUnseen) )

                con.commit()
                msg = "Record successfully added"
                plotFromDB()

        except:
            con.rollback()
            msg = "error in insert operation"

        finally:

            return render_template("mainView.html", msg=msg)
            con.close()


if __name__ == '__main__':
    app.run(debug=True)