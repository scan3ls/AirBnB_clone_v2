#!/usr/bin/python3
""" Flask app """
from flask import Flask, abort, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    " close session "
    storage.close()


@app.route('/states_list', strict_slashes=False)
def state_list():
    " display number with html template "

    states = storage.all(State)

    # try:
    return render_template('7-states_list.html', states=states.values())
    # except:
    #    abort(404)

if __name__ == "__main__":
    app.run('0.0.0.0', '5000', False, None)
