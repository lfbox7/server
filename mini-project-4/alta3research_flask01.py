#!/usr/bin/python3

from flask import Flask, escape, jsonify, redirect, request, render_template, session, url_for
import sqlite3 as sql
import requests
import random


app = Flask(__name__)
app.secret_key = "We have 3 Dog$ @ h0me!"

global correct
global incorrect
global correct_answer
global question_index
correct = 0
incorrect = 0
correct_answer = ''
question_index = list(range(0, 50))


@app.route("/")
@app.route("/start")
def start():
    session.clear()
    return render_template("index.html")


@app.route("/login", methods = ["POST"])
def login():
    global name
    name = request.form.get("name")
    session["username"] = name
    return redirect(url_for("question", name= name))


@app.route("/question/<name>")
def question(name):
    global correct_answer
    global question_index
    random.shuffle(question_index)
    resp = requests.get('http://127.0.0.1:2225').json()
    answers=[]
    if len(question_index) > 40:
        i = question_index.pop()
        question = resp[i]['question']
        correct_answer = resp[i]['correctAnswer'].replace(" ", "_")
        answers.append(correct_answer)
        [answers.append(resp[i]['incorrectAnswers'][j].replace(" ", "_")) for j in range(3)]
        random.shuffle(answers)
    else:
        question = ''
    return render_template("question.html", name= name, correct= correct, incorrect= incorrect, question= question, answers= answers, correct_answer= correct_answer)


@app.route("/answer/<name>", methods = ["POST"])
def answer(name):
    global correct
    global incorrect
    global correct_answer
    ans = request.form.get("answer")
    if ans == correct_answer:
        correct += 1
    else:
        incorrect += 1
    return redirect(url_for("question", name= name))


@app.route("/high_scores")
def high_scores():
    data = []
    try:
        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            rows = cur.execute("SELECT * from users").fetchall()
            for row in rows:
                data.append(list(row))
    except Exception as e:
        print(e)
    finally:
        data.sort(key=lambda row: row[1], reverse=True)
        data = data[0:10]
        return render_template("high_scores.html", rows= data)


@app.route("/high_scores/api")
def high_scores_api():
    data = []
    try:
        with sql.connect("database.db") as con:
            con.row_factory = sql.Row
            cur = con.cursor()
            rows = cur.execute("SELECT * from users").fetchall()
            for row in rows:
                data.append(list(row))
    except Exception as e:
        print(e)
    finally:
        return jsonify(data)


@app.route("/logout")
def logout():
    global correct
    global incorrect
    name = session.pop("username", None)
    try:
        with sql.connect("database.db") as con:
            con.execute('''CREATE TABLE IF NOT EXISTS USERS(NAME TEXT PRIMARY KEY NOT NULL, CORRECT INT NOT NULL, INCORRECT INT NOT NULL);''')
            cur = con.cursor()
            cur.execute("INSERT INTO USERS (NAME, CORRECT, INCORRECT) VALUES (?,?,?)",(name, correct, incorrect))
            con.commit()
    except Exception as e:
        print(e)
        con.rollback()
    finally:
        con.close()
        session.clear()
        return redirect(url_for("start"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
