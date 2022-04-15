#!/usr/bin/python3

from flask import Flask, escape, jsonify, redirect, request, render_template, session, url_for
import sqlite3 as sql
import requests
import random


app = Flask(__name__)
app.secret_key = "We have 3 Dog$ @ h0me!"

# global variable declarations
global correct
global incorrect
global correct_answer
global question_index
# global variable initialization
correct = 0
incorrect = 0
correct_answer = ''
question_index = list(range(0, 50))

# homepage / sign in route
@app.route("/")
@app.route("/start")
def start():
    session.clear()
    return render_template("index.html")

# post route for login
@app.route("/login", methods = ["POST"])
def login():
    # gets name from html form
    name = request.form.get("name")
    # set session username to name
    session["username"] = name
    return redirect(url_for("question", name= name))

# game play route with user name
@app.route("/question/<name>")
def question(name):
    # call global variables for use in function
    global correct_answer
    global question_index
    # shuffle indices in question_index list
    random.shuffle(question_index)
    # call api for questions and answers
    resp = requests.get('http://127.0.0.1:2225').json()
    # create answers list
    answers=[]
    # limit game to 10 questions from bank of 50
    if len(question_index) > 40:
        # set an index from question_index and remove from list
        i = question_index.pop()
        # get question from api
        question = resp[i]['question']
        # get correct answer from api
        correct_answer = resp[i]['correctAnswer'].replace(" ", "_")
        # put correct answer in answers list
        answers.append(correct_answer)
        # loop through incorrect answers and put in answers list
        [answers.append(resp[i]['incorrectAnswers'][j].replace(" ", "_")) for j in range(3)]
        # shuffle answers list to ensure order of answers is always randomized
        random.shuffle(answers)
    else:
        # set question as flag for html template
        question = ''
    return render_template("question.html", name= name, correct= correct, incorrect= incorrect, question= question, answers= answers, correct_answer= correct_answer)

# route for posting answers
@app.route("/answer/<name>", methods = ["POST"])
def answer(name):
    # call global variables for use in function
    global correct
    global incorrect
    global correct_answer
    # get user answer from html form
    ans = request.form.get("answer")
    # check if correct and add to correct or incorrect totals
    if ans == correct_answer:
        correct += 1
    else:
        incorrect += 1
    return redirect(url_for("question", name= name))

# route to view high scores from database
@app.route("/high_scores")
def high_scores():
    # create data list
    data = []
    # try to connect to database
    try:
        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            # get all of the users from db table
            rows = cur.execute("SELECT * from users").fetchall()
            # loop through Row objects and place in data list
            for row in rows:
                data.append(list(row))
    except Exception as e:
        print(e)
    finally:
        # sort data list based on total correct answers
        data.sort(key=lambda row: row[1], reverse=True)
        # drop all but top 10 scores from data
        data = data[0:10]
        return render_template("high_scores.html", rows= data)

# route to access database table users as an api
@app.route("/high_scores/api")
def high_scores_api():
    # try to connect to database
    data = []
    try:
        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            # get all of the users from db table
            rows = cur.execute("SELECT * from users").fetchall()
            # loop through Row objects and place in data list
            for row in rows:
                data.append(list(row))
    except Exception as e:
        print(e)
    finally:
        # return data list as JSON
        return jsonify(data)

# route to logout user
@app.route("/logout")
def logout():
    # call global variables for use in function
    global correct
    global incorrect
    # get name from session
    name = session.pop("username", None)
    # try to access database
    try:
        with sql.connect("database.db") as con:
            # create table if necessary
            con.execute('''CREATE TABLE IF NOT EXISTS USERS(NAME TEXT PRIMARY KEY NOT NULL, CORRECT INT NOT NULL, INCORRECT INT NOT NULL);''')
            cur = con.cursor()
            # insert user, correct score, and incorrect score into table
            cur.execute("INSERT INTO USERS (NAME, CORRECT, INCORRECT) VALUES (?,?,?)",(name, correct, incorrect))
            con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        # close database conncection
        con.close()
        # clear session
        session.clear()
        session.pop("username", None)
        return redirect(url_for("start"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
