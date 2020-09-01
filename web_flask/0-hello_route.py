#!/usr/bin/python3
""" Flask app """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run('0.0.0.0', '5000', False, None)
