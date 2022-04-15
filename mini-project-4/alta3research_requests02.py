#!/usr/bin/python3
 
from flask import Flask, jsonify
from alta3research_music03 import music


app= Flask(__name__)


@app.route("/")
def index():
    # jsonify returns legal JSON

    return jsonify(music)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)
