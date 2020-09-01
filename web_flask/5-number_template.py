#!/usr/bin/python3
""" Flask app """
from flask import Flask, abort, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ index html page """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ basic html page """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ page that displays 'C <text>' """
    spaced = text.replace("_", " ")
    return "C {}".format(spaced)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """ page that displays 'Python <text>' """
    spaced = text.replace("_", " ")
    return "Python {}".format(spaced)


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """ displays if n is a number """
    try:
        num = int(n)
        return "{} is a number".format(num)
    except:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def num_template(n):
    """ display number with html template """

    try:
        num = int(n)
        return render_template('5-number.html', n=num)
    except:
        abort(404)


if __name__ == "__main__":
    app.run('0.0.0.0', '5000', False, None)
