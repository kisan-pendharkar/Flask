# importing libraries
from flask import Flask, request, Response, jsonify,make_response
from flask_sqlalchemy import SQLAlchemy


# creating an instance of the flask app
app = Flask(__name__)

# Configure our Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Jdfy&^13@10.110.174.80/room_management'
