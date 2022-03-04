from flask import Flask, render_template, json, redirect
from flask_mysqldb import MySQL
from flask import request
import os

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'classmysql.engr.oregonstate.edu'
app.config['MYSQL_USER'] = 'cs340_cheneak'
app.config['MYSQL_PASSWORD'] = '7051' #last 4 of onid
app.config['MYSQL_DB'] = 'cs340_cheneak'
app.config['MYSQL_CURSORCLASS'] = "DictCursor"


mysql = MySQL(app)


# Routes
@app.route('/')
def root():
    query = "SELECT * FROM diagnostic;"
    cur = mysql.connection.cursor()
    cur.execute(query)
    results = cur.fetchall()

    return results[0]


# Listener
if __name__ == "__main__":

    app.run(port=8766, debug=True)