# importing libraries
from flask import Flask, request, Response, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy


# creating an instance of the flask app
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:PWD@123@127.0.0.1room_management'
