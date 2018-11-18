from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String)
    profile = db.Column(db.String)
    prof_pic = db.Column(db.String)

    def __repr__(self):
        return f'User {self.username}'
   

class Pitch:
    '''
    User class to define pitch objects
    '''
    __tablename__ = "pitches"
    id = db.Column(db.Integer, primary_key = True)
    category = db.Column(db.String)
    pitch = db.Column(db.string(255))
    upvotes = db.Column(db.Integer)
    downvotes = db.Column(db.Integer)
    

    


