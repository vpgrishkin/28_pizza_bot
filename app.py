import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


ADMIN_LOGIN = os.environ['ADMIN_LOGIN']
ADMIN_PASSWORD = os.environ['ADMIN_PASSWORD']
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)