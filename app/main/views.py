from flask import render_template, request, redirect, url_for,abort
from ..models import User,Pitch,Comment
from . import main
from flask_login import login_required

#views
@main.route('/')
def index():
    '''
    Returns index page and it's data
    '''
    title = "Speed Pitching"
    return render_template('index.html', title = title)

@main.route('/user/<username>')
def profile(username):
    user = User.query.filter_by(username = username).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)