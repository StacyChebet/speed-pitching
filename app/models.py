class User:
    '''
    User class to define user objects
    '''
    def __init__(self,id,username,email,password):
        self.id = id
        self.username = username
        self.email = email
        self.password = password

class Pitches:
    '''
    User class to define pitch objects
    '''
    def __init__(self,pitch,category,upvote,downvote):
        self.pitch = pitch
        self.category = category
        self.upvote = upvote
        self.downvote = downvote
        

