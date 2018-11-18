from . import db

class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(255))

    def __repr__(self):
        return f'User {self.username}'
   

class Pitches:
    '''
    User class to define pitch objects
    '''
    def __init__(self,pitch,category,upvote,downvote):
        self.pitch = pitch
        self.category = category
        self.upvote = upvote
        self.downvote = downvote


