import unittest #importing the unittest module 
from user import User,Credential # Importing the user class
import pyperclip

class TestUser(unittest.TestCase):
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_account= User("barack","maundu","barackmaundu","387r7b7a")

    def test_init(self):
        """
        test_init test case to test if the object is initialize properly
        """
        self.assertEqual(self.new_account.first_name,"barack")
        self.assertEqual(self.new_account.last_name,"maundu")
        self.assertEqual(self.new_account.user_name,"barackmaundu")
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
    def test_multiple_save(self):
        """
        To test to save multiple accounts
        """
        self.new_account= User("barack","maundu","barackmaundu","387r7b7a")
        self.new_account.save_account()
        test_account=User('jimmy','dot','jimmydot','777720fh')
        test_account.save_account()
        self.assertEqual(len(User.user_list),2)    

class TestCredentials(unittest.TestCase): 
    def setUp(self):
        """
        set up method to run before each test cases
        """
        self.new_credential=Credential("barackmaundu","387r7b7a")   
    def test_account_exist(self):
        """
        account_exist checks if account new_credintial exist
        """
        self.assertEqual(self.new_credential.user_name,"barackmaundu")
        self.assertEqual(self.new_credential.password,'387r7b7a')   
    def test_save_credential(self):
        """
        To save new_credential_accont in the credential list
        """
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list),1) 
    def test_save_multiple_credential(self):
        """
        To test how to save multiple
        """
        self.new_credential.save_credential()
        test_credential=Credential("barackmaundu",'387r7b7a')
        test_credential.save_credential()  

        self.assertEqual(len(Credential.credential_list),2)
    
    def test_delete_credential(self):
        """
        To test if credentail can be deleted
        """
        self.new_credential.save_credential()
        test_credential=Credential("barackjunior",'387r3b7a')
        test_credential.save_credential()  

        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list),1)
    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credential.credential_list = []
    def display_credential(self):
        """
        to test if credentials can be displayed using method
        """
        self.assertEqual(Credential.display_credential(),Credential.credential_list)     


if __name__ ==  '__main__':
    unittest.main()               