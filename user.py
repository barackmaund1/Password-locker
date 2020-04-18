import string ,random
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
    def __init__(self,user_name,password):

        #docstring removed for simplicity
            self.user_name=user_name
            self.password=password
    @classmethod
    def credential_exist(cls,):

        for  in cls.user_list:
            if credential.user_name == account.user_list:
                return credential.user_name

            return False