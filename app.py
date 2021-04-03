import os

from flask import Flask, request
# sql alchemy is an ORM used by flask to communicate with the DB
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

app = Flask(__name__)

# Base Directory
basedir = os.path.abspath(os.path.dirname(__file__))

# SQLite database
# DATABASE = 'sqlite:///' + os.path.join(basedir, 'db.flask-reddit')

# Local postgres database
DATABASE = 'postgresql://localhost/flask-reddit'

# setup database
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# init database
db = SQLAlchemy(app)

# init marshmallow
marshmallow = Marshmallow(app)

DEBUG = True
PORT = 8000

@app.route('/')
def hello_world():
    return 'Hello, world!!'

if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)