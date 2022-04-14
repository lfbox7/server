#!/usr/bin/python3
 
from flask import Flask, jsonify
import json
import alta3research_music03 as music

app= Flask(__name__)


@app.route("/")
def index():
    # jsonify returns legal JSON
    return jsonify(requests.get(music))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)

