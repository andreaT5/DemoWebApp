from flask import Blueprint
from flask import render_template, redirect, url_for, session
from models.user import User

route_index = Blueprint('index', __name__)

@route_index.route('/')
def index():
    if 'user' in session:
        user_email = session['user']['email']
        user = User.query.filter_by(email=user_email).first()

        user_info = {
            'username': user.username,
            'email': user.email
        }

        action = 'dashboard'

        return render_template('page/index.html', action=action)
    else:
        # return render_template('user/login.html')
        return render_template('user/login.html')
    
@route_index.route('/chart')
def chart():
    if 'user' in session:
        user_email = session['user']['email']
        user = User.query.filter_by(email=user_email).first()

        action = 'chart'

        return render_template('page/index.html', action=action)
    else:
        # return render_template('user/login.html')
        return render_template('user/login.html')