#!/usr/bin/python3

from flask import Flask, redirect, request, render_template, url_for
import requests
import random

app = Flask(__name__)

name = ''
correct = 0
incorrect = 0
correct_answer = ''

@app.route("/")
@app.route("/start")
def start():
    return render_template("index.html")

@app.route("/login", methods = ["POST"])
def login():
    name = request.form.get("name")
    return redirect(url_for("question", name= name))

@app.route("/question/<name>")
def question(name):
    resp = requests.get('http://Localhost:2224').json()
    print(resp)
    answers=[]
    question = resp[0]['question']
    correct_answer = resp[0]['correctAnswer']
    answers.append(correct_answer)
    [answers.append(resp[0]['incorrectAnswers'][i]) for i in range(3)]
    random.shuffle(answers)
    print(str(answers))
    return render_template("question.html", name= name, correct= correct, incorrect= incorrect, question= question, answers= answers, correct_answer= correct_answer)

@app.route("/answer/<name>", methods = ["POST"])
def answer(name, correct):
    ans = request.form.get("answer")
    if ans == correct_answer:
        correct += 1
    else:
        incorrect += 1
    return redirect(url_for("question", name= name, correct= correct, incorrect= incorrrect))


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)
