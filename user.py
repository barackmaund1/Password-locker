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
    def account_exist(cls,user_name,password):
        '''
        Method that checks if a account exists from the account list.
        Args:
            string:user_name  to search if it exists
        Returns :
            Boolean: True or false depending if the account exists
        '''
        for account in User.user_list:
            if (account.user_name == user_name and password.user_name == password):
                    return True

        return False         
    def save_credentials(self):

        '''
        save_credentials method saves account objects into credetial_list
        '''

        Credential.credential_list.append(self)

    def delete_crediantials(cls):

        '''
        delete_credential method deletes a saved accounts from the credintials
        '''

        Credential.credential_list.remove(self)
    @classmethod        
    def display_crediantials(cls):
        """
        display_credentials  methods displays crediantials from the credintials
        """
    return cls.credential_list

    