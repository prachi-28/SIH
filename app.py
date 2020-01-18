from flask import Flask, render_template, request
import re
import sqlite3 as sql
import time

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('problem.html')

@app.route('/csubmit',methods=['POST'])
def submit():
    body = request.form["complain"]
    cat = request.form["cat"]
    print(cat)
    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO COMPLAIN (body,cat,status_id,time) VALUES (?,?,?,?)",(body,cat,0,time.time()))
        con.commit()
        msg = "Record successfully added"
    return render_template('data.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
