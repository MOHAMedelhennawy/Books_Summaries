#!/usr/bin/python3
import json


# based on "remember_me.py" file
# - Refactoring: makes your code cleaner,
#   easier to understand, and easier to extend. and this by breaking 
#   the code into a serires of function that have specific jobs


def get_stored_username(file_name):
    try:
        with open(file_name) as file_obj:
            user_name = json.load(file_obj)
    except FileNotFoundError:
        return False
    else:
        return user_name

def greet_user(file_name):
    user_name = get_stored_username(file_name)
    if user_name:
        print("Welcome back, " + user_name + "!")
    else:
        User_name = input("What is you'r name? ")
        with open(file_name, "w") as file_obj:
            json.dump(User_name, file_obj)
            print("We'll remember you when you come back, " + User_name + "!")

file_name = "username.json"
greet_user(file_name)