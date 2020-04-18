import unittest #importing the unittest module 
from user import User # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_account= User("twitter","barack","387r7b7a")

    def test_init(self):
        """
        test_init test case to test if the object is initialize properly
        """
        self.assertEqual(self.new_account.account_name,"twitter")
        self.assertEqual(self.new_account.user_name,"barack")
        self.assertEqual(self.new_account.password,"387r7b7a")

    def test_save_account(self):
        """
        test_save_test case is to test if acount is saved
        """
        self.new_account.save_account()
        self.assertEqual(len(User.user_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        User.user_list = []

    def test_display_account(self):
        """
        method that return a list of acounts
        """
        self.assertEqual(User.display_account(),User.user_list) 

if __name__ ==  '__main__':
    unittest.main()               