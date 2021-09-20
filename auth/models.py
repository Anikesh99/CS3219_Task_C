from . import db
import uuid
import jwt
import datetime
from functools import wraps

class User(db.Model):
    id = db.Column(db.String(100), primary_key=True) # primary keys are required by SQLAlchemy
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    admin = db.Column(db.Integer())

class Todos(db.Model):
    id = db.Column(db.String(100), primary_key=True)
    user_id = db.Column(db.String(100))
    description = db.Column(db.String(100), nullable=False)

