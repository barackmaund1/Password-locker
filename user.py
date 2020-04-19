import string 
import random
import pyperclip
class User:
    """
    Class that generates new instance of users.
    """
    user_list=[]#Empty user lis

    def __init__(self,first_name,last_name,user_name,password):

        #docstring removed for simplicity

            self.first_name=first_name
            self.last_name=last_name
            self.user_name=user_name
            self.password=password
    def save_account(self):

        """
        save_account method saves the accounts    
        """
        User.user_list.append(self)

    def delete_account(self):
        """
        del_account method deletes a saved accounts
        """
        User.user_list.remove(self) 

    @classmethod    
    def display_account(cls):
        """
        display_account method diplays account from the account_list
        """
        return cls.user_list 

    
class Credential:
    credential_list=[]
    def __init__(self,account_name,user_name,password):

        #docstring removed for simplicity
            self.account_name=account_name
            self.user_name=user_name
            self.password=password
            

    @classmethod
    def account_exist(cls,user_name,password):
        '''
        Method that checks if a account exists from the account list.
        Args:
            string:user_name  to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in User.user_list:
            if (account.user_name == user_name and account.password == password):
                    return True

        return False         
    def save_credential(self):

        '''
        save_credentials method saves account objects into credetial_list
        '''

        Credential.credential_list.append(self)

    def delete_credential(self):

        '''
        delete_credential method deletes a saved accounts from the credintials
        '''

        Credential.credential_list.remove(self)
    @classmethod        
    def display_credentials(cls):
        """
        display_credentials  methods displays crediantials from the credintials
        """
        return cls.credential_list

    @classmethod
    def search_credential(cls, account_name):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.
        """
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def if_credential_exist(cls, account_name):
        """
        Method that checks if a credential exists from the credential list and returns true or false depending if the credential exists.
        """
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True
        return False
    @classmethod 
    # def generates_password(stringLength=8):
    #     """Generate a random password string of letters and digits and special characters"""
    #     password = string.ascii_uppercase + string.ascii_lowercase + string.digits + "~!@#$%^&*"
    #     return ''.join(random.choice(password) for i in range(stringLength)) 
    def generates_password( stringLength=8):
        password=""
        for n in range(stringLength): 
            x=random.randit(0,94)
            password +=string.printable[x]
        return password    