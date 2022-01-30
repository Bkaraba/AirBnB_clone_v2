#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def HelloHBNB():
    """method triggered by "/" route"""
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """method triggered by "/hbtn" route """
    return "<p>HBNB</p>"

@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """method triggered by /c/<text> route"""
    return "C {}".format(text.replace("_","")))
    
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
