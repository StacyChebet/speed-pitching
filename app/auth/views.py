from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user,logout_user,login_required
from . import auth
from ..models import User,Pitch,Comment
from .forms import LoginForm,SignupForm
from ..import db
from ..email import mail_message

@auth.route('/signup', methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(user)
        db.session.commit()

        mail_message("Welcome to Speed Pitching","email/welcome_user",user.email, user=user)
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

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))