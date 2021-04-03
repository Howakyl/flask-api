import os

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Base Directory
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
PORT = 8000

@app.route('/')
def hello_world():
    return 'Hello, world!'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)