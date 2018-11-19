from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user
from . import auth
from ..models import User,Pitch,Comment
from .forms import LoginForm,SignupForm
from ..import db

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(User)
        db.sesion.commit()
        return redirect(url_for('auth.login'))
        title = "Create New Account"
    return render_template('auth/signup.html',signup_form = form)

@auth.route('/login',methods = ['GET','POST'])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        user = User.query.filter_by(email = login_form.email.data).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))

        flash("Invalid username or Password")
    
    title = "Speed Pitching Login"
    return render_template('auth/login.html', login_form = login_form, title = title)
    return render_template('auth/login.html')