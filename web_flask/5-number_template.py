#!/usr/bin/python3
"""script that starts a Flask web application:"""
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def HelloHBNB():
    """method triggered by "/" route"""
    return "<p>Hello HBNB!</p>"

@app.route("/hbnb" strict_slashes=False)
def HBNB():
    """method triggered by "/hbtn" route """
    return "<p>HBNB</p>"

@app.route("/c/<text>", strict_slashes=False)
def cisfun(text):
    """method triggered by /c/<text> route"""
    return ("C {}".format(text.replace("_", "")))

@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_variable(text="is cool"):
    """ method triggered by /python and /python/<text> routes
    defaut text is is cool"""
    return ("python {}".format(text.replace("_", "")))

@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """method triggered by /number/<int:n> route
    returns n is a number, if n variable is a number"""
    return ("{} is a number".format(n))
    
@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """method triggered by /number_template/<int:n> route
    displays html template"""
    return render_template("5-number.html", n=n)
if __name__ == "__main__":
    app.run(host="0.0.0.0")
