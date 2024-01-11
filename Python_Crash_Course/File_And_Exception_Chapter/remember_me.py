#!/usr/bin/python3

import json

file_name = "username.json"
try:
    with open(file_name) as file_obj:
        User_name = json.load(file_obj)
except FileNotFoundError:
    User_name = input("What is you'r name? ")
    with open(file_name, "w") as file_obj:
        json.dump(User_name, file_obj)
        print("We'll remember you when you come back, " + User_name + "!")
else:
    print("Welcome back, " + User_name + "!")