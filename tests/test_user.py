import unittest
from app.models import User

class UserTest(unittest.TestCase):
    '''
    Tests behaviour of User class
    '''

    def setUp(self):
        '''
        Runs before every Test
        '''
        self.new_user = User(1, "Tracy Kimathi", "tracykimathi@gmail.com", "chocolate")