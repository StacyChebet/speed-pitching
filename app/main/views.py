from flask import render_template, request, redirect,flash, url_for,abort
from ..models import User,Pitch,Comment
from . import main
from flask_login import login_required
from .forms import UpdateProfile,AddComment,AddPitch
from .. import db,photos
import datetime

#views
@main.route('/')
def index():
    '''
    Returns index page and it's data
    '''
    pitches = Pitch.query.all()
    title = "Speed Pitching"
    return render_template('index.html', pitches=pitches, title = title)

@main.route("/pitches/<category>")
def categories(category):
    pitches = None
    if category == "all":
        pitches = Pitch.query.order_by(Pitch.date_created.desc())
    else:
        pitches = Pitch.query.filter_by(category=category).order_by(Pitch.date_created.desc()).all()

    return render_template("pitches.html",pitches=pitches,title=category.capitalize())

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

@main.route('/user/<username>/update/pic', methods=['POST'])
@login_required
def update_pic(username):
    user = User.query.filter_by(username=username).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.prof_pic = path
        db.session.commit()
    return redirect(url_for('main.profile',username=username))

@main.route("/<username>/add_pitch", methods = ["GET","POST"])
@login_required
def add_pitch(username):
    form = AddPitch()
    user = User.query.filter_by(username = username).first()
    if user is None:
        abort(404)
    title = "Add Pitch"
    if form.validate_on_submit():
        name = form.name.data
        category = form.category.data 
        content = form.content.data
        date_created= datetime.datetime.now()

        new_pitch = Pitch(name = name, category = category, pitch = content, user = user, date_created = date_created)
        new_pitch.save_pitch()  
        pitches = Pitch.query.all()
        
        return redirect(url_for("main.categories",category = category))
    return render_template("add_pitch.html",pitch_form = form, title = title)