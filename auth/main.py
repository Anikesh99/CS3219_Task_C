from flask import Blueprint
from . import db
from flask_login import login_required, current_user

main = Blueprint('main', __name__)

@main.route('/myName')
@login_required
def myName():
    return "I have made it here"

@main.route('/')
def index():
    return 'Index'

@main.route('/profile')
def profile():
    return 'Profile'