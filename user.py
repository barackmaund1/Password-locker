import string ,random
class User:
    """
    Class that generates new instance of users.
    """
    user_list=[]#Empty user lis

    def _init_(self,account,user_name,password):

        #docstring removed for simplicity

            self.account=account
            self.user_name=user_name
            self.password=password
    def save_account(self):

        """
        save      