from flask import Flask, render_template, request
import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('movie.html')


@app.route('/enternew')
def movie():
    return render_template('movie.html')


@app.route('/addrec', methods=['POST', 'GET'])
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
        except:
            con.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("movies.db")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select * from movies")

    rows = cur.fetchall();
    return render_template("list.html", rows=rows)


if __name__ == '__main__':
    app.run(debug=True)