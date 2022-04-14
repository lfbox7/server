#!/usr/bin/python3

from flask import Flask, redirect, request, render_template, url_for

app = Flask(__name__)

@app.route("/success")
def success():
    return f"Correct!\nSaturn has 82 moons.\n"

@app.route("/failure")
def failure():
    return f"Wrong!\nSaturn has 82 moons.\n"

@app.route("/")
@app.route("/start")
def start():
    return render_template("index.html")

@app.route("/answer", methods = ["POST"])
def answer():
    ans = ''
    if request.method == "POST":
        if request.form.get("answer"):
            print(request.form.get("answer"))
            ans = request.form.getlist("answer")
            print(ans)
            if ans[0] == "d":
                return redirect(url_for("success"))
            else:
                return redirect(url_for("failure"))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224)

