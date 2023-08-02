from flask import Blueprint, session, url_for, redirect, request, render_template
from resources.user_token import TokenResource
from models.user import User

route_user = Blueprint('login', __name__)

@route_user.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('index.index'))
    
    email = request.form.get('username')
    if email == None:
        return render_template('user/login.html')
    password = request.form.get('password')

    user = User.get_by_email(email)
    
    if user and User.verify_password(password, user.password):
        TokenResource().post(email, password)

        session['user'] = {'email': email, 'name': user.username, 'fullname': user.fullname}
        return redirect(url_for('index.index'))
    elif user == None:
        return render_template('user/login.html', info='Invalid User Name')
    elif User.verify_password(password, user.password) == False:
        return render_template('user/login.html', info='Invalid Password')
    else:
        return render_template('user/login.html')

@route_user.route('/register', methods=['GET', 'POST'])
def register():
    email = request.form.get('Email')
    if email == None:
        return render_template('user/register.html')
    username = request.form.get('UserName')
    fullname = request.form.get('FirstName') + ' ' + request.form.get('LastName')

    password = request.form.get('Password')
    password2 = request.form.get('ConfirmPassword')
    if password != password2:
        return render_template('user/register.html', info='Input correct password')

    existing_user = User.get_by_email(email)
    if existing_user:
        return render_template('user/register.html', info='this user already existed')
    
    hashed_password = User.hash_password(password)

    new_user = User(username=username, email=email, password=hashed_password, fullname=fullname)
    new_user.save()

    return redirect(url_for('login.login'))

@route_user.route('/logout', methods=['GET', 'POST'])
def logout():
    session.clear()

    return redirect(url_for('index.index'))