#!/usr/bin/python3
""" Flask app """
from flask import Flask

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


if __name__ == "__main__":
    app.run('0.0.0.0', '5000', False, None)
