#!/usr/bin/env python3.6
from user import User,Crediantial

def create_account(first_name,last_name,user_name,password):
    """
    function to create new account or to sign up
    """
    new_account=User(first_name,last_name,user_name,password)
    return new_account

def save_account(acount): 
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
    Function to display all credentials in list
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
   
