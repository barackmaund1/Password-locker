#!/usr/bin/env python3.6
from user import User,Credential

def create_account(first_name,last_name,user_name,password):
    """
    function to create new account or to sign up
    """
    new_account=User("first_name","last_name","user_name","password")
    return new_account

def save_account(account): 
    """
    Function to save new account 
    """
    account.save_account()
def display_account():
    """
    function to display existing account
    """
    return User.display_account()
def delete_account(account):
    """
    function to delete the account and reset again
    """
    return account.delete.account()
def account_exist(user_name):
    """
    Function to check whether the account username and password exist
    """
    return Credential.account_exist(user_name)
def create_credential(account_name,user_name,password):
    """
    Function to create new credential
    """
    new_credential=Credential('account_name',"user_name","password")  
    return new_credential

def save_credential(credential):
    """
    Function to save new credential
    """
    credential.save_credential() 
def display_credential():
    """
    Function to display all credentials in the list
    """
    return Credential.display_credentials()    

def delete_credential(credential):
    """
    function to delete a credential in the credential_list
    """
    credential.delete_credential()
def search_credential(account_name):
    """
    Function to search credential and returns it from credentia_list
    """
    return Credential.search_credential(account_name) 
def if_credential_exist(account_name):
    """
    Function that search credential with account name and if finds it returns true otherwise false
    """
    return Credential.if_credential_exist(account_name)
def generate_password():
    """
    Function that generates a random password wit range
    """    
    password =Credential.generate_password()
    return password
def generates_password ():
    """
    Function to generate a random password to the users
    """
    password =User.generates_password()
    return password

   
def main():
    print("Hello Welocome to your Credentials...\n Kindly if you have no account sign in by typing\n SI--\n Otherwise login by typing \n LI----")
    short_code=input("").lower().strip()
    if short_code=="si":
        print('sign in')
        print('*40')

        print('first name....')
        first_name=input()

        print('last name....')
        last_name=input()

        print('Enter username...')
        user_name=input()

        while True:
            print('Type:OP-To type your password:\n  GP -To generate random password')
            user_choice=input().lower().strip()
            if user_choice =='op':
                password=input('Enter your password')
                break
            elif user_choice=='gp':
               password=generates_password()
               break
            else:
                print('Invalid password please try again') 
        save_account(create_account('first_name','last_name','user_name','password'))
        print('\n') 
        print(f"Hello {first_name} {last_name}, Your account has been succesfully created!Your password is:\n {password}")
        print('\n')
        while True:
            print("Please type:'LI' to login...")
            short_code=input().lower().strip()

            if short_code=='li':
                print('\n')
                print("Please enter your details to log in")
                print('\n')

                print('username...')
                user_name=input('username...')

                print('Enter your password')
                password=input('password....')

                login=account_exist(user_name)
                if  user_name !=login:
                    print(f"Hello{user_name}.Welcome to your credentials")
                    print("\n")
                
                       
                
                    while True:
                        print("Use these short codes:\n CC-Create a new credential \n DC-Display credential \n SC-search a credential\n GP-Generate a random password \n D-Delete credential \n E-Exit")            
                        short_code=input().lower().strip()
                        if short_code == "cc":
                            print("Create New credential")
                            print("."*30)
                            print("Account name e.g twitter,whatsapp,facebook")
                            account_name=input().lower()
                            print('Your account username')
                            user_name=input()
                            while True:
                                print('Type:TP-To type your own password if already have an account:\nGP-To generate your own password')
                                password_choice=input().lower().strip()
                                if password_choice=='tp':
                                    password=input("Enter Your Own password\n")
                                    break
                                elif password_choice=='gp':
                                    password=generate_password()
                                    break
                                else:
                                    print('invalid password please try again') 
                                save_credential(create_credential("account_name","user_name","password"))
                                print("\n")  
                                print(f"{account_name} -username is:{user_name} and password is:{password}")
                                print("\n") 
                        elif short_code =='dc':
                            if  display_credential():
                                print('list of you accounts')
                                print('\n')   
                                for credential in display_credential():
                                    print(f'Account:{credential.account_name}Username:{credential.user_name}password:{credential.password}')
                                    print('\n') 
                            else:
                                print("You don't have any credential saved..") 
                        elif short_code=='sc' :
                            print("Enter the account name i.e twitter,instagram to search credential")          
                            account_name=input().lower()
                            if search_credential(account_name):
                                credential=search_credential(account_name)
                                print(f"Account name:{credential.account_name}")
                                print(f"Username:{credential.user_name}")
                                print(f"password:{credential.password}")
                            else:
                                print("invalid account or credential doesn't exist")
                                print('\n')
                        elif short_code=='d' :
                            print("Enter the account name of credential you want to delete")
                            account_name=input().lower()
                            if search_credential(account_name):
                                credential=search_credential(account_name)
                                credential.delete_credential()
                                print(f'{credential.account_name} has been deleted succefully')
                            else:
                                print('please you do not have that credential')
                        elif short_code=='e' :
                            print("Thank you.See you next time")
                        elif short_code=='gp':
                            password=generate_password()
                            print(f'{password}Your password has been generated successfully')
                        else :
                
                            print('Oops!wrong entry try again') 
                # else:
                #     print('please enter valid username')            
            else:
                print("you entered wrong code")
    else:
        print("Invalid input")
              
if __name__ == '__main__':
    main()         
