from flask import render_template, request, redirect, url_for,abort
from ..models import User,Pitch,Comment
from . import main
from flask_login import login_required
from .forms import UpdateProfile
from .. import db,photos

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

@main.route('/user/<username>/update', methods = ['GET', 'POST'])
@login_required
def update_profile(username):
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.profile = form.profile.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', username=user.username))

    return render_template('profile/update.html', form=form)

@main.route('/user/username/update/pic', methods=['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username=username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))