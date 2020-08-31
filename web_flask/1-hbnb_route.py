#!/usr/bin/python3
""" Flask app """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


app.run('0.0.0.0', '5000', False, None)
