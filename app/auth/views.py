from flask import render_template,redirect,url_for
from . import auth
from ..models import User,Pitch,Comment
from .forms import SignupForm
from ..import db

@auth.route(/'/signup', methods = ["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(email = form.email.data, username = form.username.data, password = form.password.data)
        db.session.add(User)
        db.sesion.commit()
        return redirect(url_for('auth.login'))
        title = "Create New Account"
    return render_template('auth/signup.html',signup_form = form)

@auth.route('/login')
def login():
    return render_template('auth/login.html')