from . import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin,db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), unique = True, index = True)
    profile = db.Column(db.String)
    prof_pic = db.Column(db.String)
    pitch = db.relationship("Pitch", backref="user", lazy="dynamic")
    Comment = db.relationship("Comment", backref ="user", lazy="dynamic")
    pass_hash = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('Stick to your lane bro!')
    
    def verify_password(self, password):
        return check_password_hash(self.pass_hash, password)

class Pitch(db.Model):
    '''
    User class to define pitch objects
    '''
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.String(255))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    comments = db.relationship("Comment", backref="pitch", lazy="dynamic")

class Comment(db.Model):
    '''
    Defines comment objects
    '''
    __tablename__ = "comments"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    pitch_id = db.Column(db.Integer, db.ForeignKey("pitches.id"))
    comment = db.Column(db.String(255))

    
    def __repr__(self):
        return f'User {self.username}'

    


