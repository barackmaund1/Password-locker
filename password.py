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
def delete_account():
    """
    function to delete the account and reset again
    """
    return User.delete.account()
def account_exist(user_name,password):
    """
    Function to check whether the account username and password exist
    """
    check_account=Crediantial.account_exist(user_name,password)
def create_credential(account_name,user_name,password):
    """
    Function to create new credential
    """
    new_credential=Crediantial(user_name,password)  
def save_credential(credential):
    """
    Function to save new credential
    """
    credential.save_credential() 
def display_credential():
    """
    Function to display all credentials in the list
    """
    return Crediantial.display_credential()    

def delete_credential(credential):
    """
    function to delete a credential in the credential_list
    """
    credential.delete_credential()
def search_credential(account_name):
    """
    Function to search credential and returns it from credentia_list
    """
    return Crediantial.search_credential(account_name) 
def if_credential_exist(account_name):
    """
    Function that search credential with account name and if finds it returns true otherwise false
    """
def generate_password():
    """
    Function that generates a random password wit range
    """
   
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
                password=generate_password()
                break
            else:
                print('Invalid password please try again') 
        save_account(create_account('first_name','last_name','user_name','password'))
        print('\n') 
        print(f"Hello {first_name} {last_name}, Your account has been succesfully created!Your password is:\n {password}")
        print('\n')
       
    elif short_code=='li':
        print('\n')
        print("Please enter your details to log in")
        print('\n')

        print('user name...')
        user_name=input('user_name')

        print('Enter your password')
        password=input('password')

        login=account_exist(user_name,password)
        if account_exist ==login:
            print(f"Hello{user_choice}.Welcome to your credentials")
            print("\n")
    while True:
        print("Use these short codes:\n CC-Create a new credential \n DC-Display credential \n SC-search a credential\n GP-Generate a random password \n D-Delete credential \n E-Exit")        
    else:
        print('Invalid input.Please enter valid input')     
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
                save_credential(create_credential(account_name,user_name,password))
                print("\n")  
                print(f"{account_name} -username is:{user_name} and password is:{password}")
                print("\n") 
        elif short_code =='dc':
            if                 
                   

if __name__ == '__main__':
    main()         
