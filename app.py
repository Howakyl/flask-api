import os

from flask import Flask, request
# sql alchemy is an ORM used by flask to communicate with the DB
from flask_sqlalchemy import SQLAlchemy
# marshmallow is used to dictate what fields will be sent back to the user in response
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


# HOME ROUTE 
@app.route('/')
def hello_world():
    return 'Hello, world!!'

######## SUBS ########

# CREATE SUB / GET ONE SUB
@app.route('/sub', methods=['POST'])
@app.route('/sub/<subid>', methods=['GET'])
def create_sub(subid=None):
    from models import Sub
    if subid == None:
        name = request.json['name']
        description = request.json['description']

        return Sub.create_sub(name, description)
    else:
        return Sub.get_sub(subid)

# ALL SUBS
@app.route('/all', methods=['GET'])
def get_all():
    from models import Sub
    return Sub.get_all()


######## POSTS #######





if __name__ == '__main__':
    app.run(debug=DEBUG, port=PORT)