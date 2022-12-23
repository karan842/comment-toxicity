'''
Author: Karan Shingde

'''

## Importing libraries
import pandas as pd
import numpy as np
import json
import re
import text
import tensorflow as tf
import tensorflow_text as text
from flask import Flask


app = Flask(__name__)

@app.route('/admin')
def hello_admin():
    return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
    return 'Hello %S as Guest ' % guest

@app.route('/user/<name>')
def hello_user(name):
    if name=='admin':
        return redirect(url_for('hello_admin'))
    else:
        return redirect(url_for('hello_guest',guest=name))

if __name__ == '__main__':
    app.run()