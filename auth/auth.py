from flask import Blueprint, redirect, url_for, request, jsonify, make_response
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User, Todos
from . import db
from flask_login import login_user
import uuid
import jwt
import datetime
from functools import wraps

auth = Blueprint('auth', __name__)
# change this
def authentication_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return make_response("Token is invalid", 401, 'Valid token is missing')
        try:
            data = jwt.decode(token, "hhh", algorithms="HS256")
            current_user = User.query.filter_by(id=data['id']).first()
            return f(current_user, *args, **kwargs)
        except:
            return make_response("Token is invalid", 401, 'Valid token is missing')
    return decorator

def authorization_required(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        token = None
        if 'x-access-tokens' in request.headers:
            token = request.headers['x-access-tokens']
        if not token:
            return make_response("Token is invalid", 401, 'Valid token is missing')
        try:
            data = jwt.decode(token, "hhh", algorithms="HS256")
            current_user = User.query.filter_by(id=data['id']).first()
            if current_user.admin == 0:
                return make_response('Not authorized', 403, {"Authorization": "user is not admin"})
            return f(current_user, *args, **kwargs)
        except:
            return make_response("Token is invalid", 401, 'Valid token is missing')
    return decorator

@auth.route('/login', methods=['POST'])
def login():
    auth = request.authorization
    if not auth:
        return make_response('Invalid authetication', 401, {"Authentication": "Get my password"})
    username = request.form.get('username')
    password = request.form.get('password')
    user = User.query.filter_by(username=username).first()
    if user is not None and check_password_hash(user.password, auth.password):
        token = jwt.encode({'id': user.id}, "hhh")
        return jsonify({'token': token})
    return make_response('Failed login', 401, {"Authentication": "Failed"})

@auth.route('/signup', methods=['POST'])
def signup():
    username = request.form.get('username')
    password = request.form.get('password')
    isAdmin = request.form.get('isAdmin')
    print(username, password, isAdmin)
    user = User.query.filter_by(username=username).first()
    if user is not None:
        return "User already exists"
    pw = generate_password_hash(password, method='sha256')
    user = User(id=str(uuid.uuid4()), username=username, password=pw, admin=int(isAdmin))
    db.session.add(user)
    db.session.commit()
    return jsonify({"status": "User created"})

@auth.route('/todo', methods=['POST'])
@authentication_required
def create_todo(user):
   data = request.get_json() 
   todo = Todos(description=request.form.get("description"), user_id=user.id, id=str(uuid.uuid4()))  
   db.session.add(todo)   
   db.session.commit()   

   return jsonify({'message' : 'new todo added'})

@auth.route('/todos', methods=['GET'])
@authorization_required
def getTodos(user):
    todos = Todos.query.filter_by(user_id=user.id).all()
    lst = []
    for i in range(len(todos)):
        lst.append({"description": todos[i].description})
    return jsonify({'todos' : lst})