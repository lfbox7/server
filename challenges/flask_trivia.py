#!/usr/bin/python3

from flask import Flask, redirect, request, render_template, url_for
import requests
import random

app = Flask(__name__)

name = ''
correct = 0
incorrect = 0
correct_answer = ''
url = 'https://the-trivia-api.com/questions?categories=music&limit=1&region=US&difficulty=medium'

@app.route("/")
@app.route("/start")
def start():
    return render_template("index.html")

@app.route("/login", methods = ["POST"])
def login():
    name = request.form.get("name")
    return redirect(url_for("question", name= name, correct= correct, incorrect= incorrect))

@app.route("/question")
def question(name, correct, incorrect):
    resp = requests.get(f'{url}')
    answers=[]
    question = resp[0].get('question')
    correct_answer = resp[0].get('correctAnswer')
    answers.append(correct_answer)
    answers.append(resp[0].get('incorrectAnswers[i for i in range(3)]'))
    answers = random.shuffle(answers)
    return render_template("question.html", name= name, correct= correct, incorrect= incorrrect, question= question, answers= answers, correct_answer= correct_answer)

@app.route("/answer", methods = ["POST"])
def answer(name, correct, incorrect, correct_answer):
    ans = request.form.get("answer")
    if ans == correct_answer:
        correct += 1
    else:
        incorrect += 1
    return redirect(url_for("question", name= name, correct= correct, incorrect= incorrrect))


if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

