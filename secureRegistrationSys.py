# Name: secureRegistrationSys
# Purpose: secure registration and login of users
# Author: Aseer

import sys

username_pswd_dict = {}

# function to take in username
def name_input():

    user_name = input("Please enter your name: ")

    # remove any leading whitespaces
    user_name = user_name.lstrip()

    # I have chosen to let users add a maximum of 2 whitespaces within 20 characters 
    # for eg the user might need to enter 2 spaces between 3 of their names with the format - Firstname Middlename Lastname
    # also, the username must contain 3 alphabets at least
    # it can also contain digits, but it will not accept names with digits only
    # Therefore only names containing a-z, A-Z will be accepted

    if (user_name.count(" ") <= 2 and 
        len(user_name) in range(3,21) and 
        user_name.isalpha()):
        count = 0
        # counting the number of alphabets in the name
        for x in user_name: 
            if x.isalpha(): 
                count+=1
        # if there are 3 or more alphabets, the user_name is returned
        if count >= 3:
            return user_name

    # if username does not match our requirements a message, to help the user input a username, is printed
    print("Username must be 3 letters at least.")
    print("It can't be empty and no digits.") 
    print("It can be of maximum 20 letters and can have up to 2 spaces only")

# function to take in pswd
def pswd_input():
    for attempts in range(0, 4):
        #
        if attempts > 2:
            print("Too many attempts, try again later")
            break
        # a total of 3 attempts given to enter a proper pswd
        user_pswd = input("Please enter your password: ")

        # remove any leading whitespaces
        user_pswd = user_pswd.lstrip()

        # No whitespaces allowd and within 8 to 12 characters for password 
        # also, the password must contain at least 1 uppercase, 1 lower case alphabets at least and 1 digit 
        if (user_pswd.count(" ") <= 0 and 
        len(user_pswd) in range(8,13) and 
        any(x.isupper() for x in user_pswd) and 
        any(x.islower() for x in user_pswd) and 
        any(x.isdigit() for x in user_pswd)):
            return user_pswd
        # if password does not match our requirements a message, to help the user input a valid password, is printed
        # and the user is given 3 chances as to enter a name
        print("Password must be 8 characters at least and 12 maximum, it can't be empty,") 
        print("At least 1 uppercase, 1 lowercase and 1 digit")

# function to start a new registration and store new user name and password
def new_user_registration():
    # check if the username already exists in the dictionary
    # there are only 3 chances
    # also checks for nothing entered for name
    # if nothing is entered 
    for attempt in range(0,4):
        if attempt > 2:
            print("Too many attempts, try again later")
            break
        name = name_input()
        if name != None and name in username_pswd_dict:
            print("Entered name already exists, please enter another name: ")
        elif name == None:
            continue
        else:
            break
    
    # checking if name contains None and if it exists in the dictionary
    # if it does then the uswer will not be asked for entering their password
    # this will prevent users from entering none values and passwords 
    # which is very unsafe
    # furthermore this also prevents users from rewriting the password for already existing users
    if name != None and name not in username_pswd_dict:
        username_pswd_dict[name] = pswd_input()
    
    # if user tries to enter a valid user name but no password this will create a password with value None
    # therefore, the following loop deletes such key value pairs
    for key, value in dict(username_pswd_dict).items():
        if value is None:
            del username_pswd_dict[key] 

# login function
def login():
    # there are only 3 chances
    # also checks for nothing entered for name
    # if a name is entered which doesn't exist
    # there is a try block to handle that code
    # the except block catches the KeyError
    # and prints a msg
    for attempt in range(0,4):
        if attempt > 2:
            print("Too many attempts,, try again later")
            break
        existing_user_name = name_input()
        if existing_user_name in username_pswd_dict:
            existing_user_pswd = pswd_input()
        try:
            if username_pswd_dict[existing_user_name] == existing_user_pswd:
                print("You have logged in")
                break
            else:
                print("Incorrect password")
        except KeyError:
            print("Entered Name does not exit in system")      

# this function is used to take a user selection from the menu
# the selection is strictly made to be an integer from 1 to 3
# the try except blocks catches the errors when chars are entered
def user_selection_input():
    try:
        selection = int(input())
        if 3>=selection and 0<selection:
            return selection
        else:
            print("\nSelect a menu item from 0 to 3")
    except:
        print("\nSelect a menu item from 0 to 3")

def menu():

    # Start of the program
    print("Welcome")

    # After welcoming the user it will ask the user what they would like to do 
    # and present options
    print("What would you like to do?")

    # this while loop will stay true forever, 
    # however when the if statement (if the user selects a valid item) becomes true, 
    # the loop is broken
    # this is done so that the program does not stop unintentionally
    while True:
        print("Press 1 for New User Registration")
        print("Press 2 for Login")
        print("Press 3 to End")
        selections = [1,2,3]
        selected_item = user_selection_input()
        if selected_item in selections:
            # after the selection is stored, the respective function will be called 
            if selected_item == 1:
                new_user_registration()
            elif selected_item == 2:
                login()
            elif selected_item == 3:
                sys.exit()

menu()