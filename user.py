import string ,random
class User:
    """
    Class that generates new instance of users.
    """
    user_list=[]#Empty user lis

    def __init__(self,account_name,user_name,password):

        #docstring removed for simplicity

            self.account_name=account_name
            self.user_name=user_name
            self.password=password
    def save_account(self):

        """
        save_account method saves the accounts    
        """
        User.user_list.append(self)

    def del_account(self):
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
    def __init__(self,account,user_name,password):

        #docstring removed for simplicity

            self.account=account
            self.user_name=user_name
            self.password=password
    @classmethod 
    def save_user_list(cls,account):
        """
        save the user list in the credentials from the user class
        """
        return cls.credential_list.append(account)