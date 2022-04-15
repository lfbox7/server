#!/usr/bin/python3
 
from flask import Flask, jsonify
from alta3research_music03 import music


app= Flask(__name__)

# route to access JSON from music dictionary
@app.route("/")
def index():
    # return music dictionary as JSON
    return jsonify(music)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2225)
