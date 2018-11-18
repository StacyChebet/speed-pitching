from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
    profile = db.Column(db.String)
    prof_pic = db.Column(db.String)
    pitch = db.relationship("Pitch", backref="user", lazy="dynamic")
    Comment = db.relationship("Comment", backref ="user", lazy="dynamic")

   

class Pitch:
    '''
    User class to define pitch objects
    '''
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    name = db.Column(db.String)
    category = db.Column(db.String)
    pitch = db.Column(db.string(255))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    
    def __repr__(self):
        return f'User {self.username}'

    


