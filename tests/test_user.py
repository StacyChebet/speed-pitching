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
        self.new_user = User(password = chocolate)
    
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)