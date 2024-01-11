#!/usr/bin/python3
import json

# # stores a set of numbers using json.dump()
# # dump syntax: json.dump(data, file)

# my_list = [1, 2, 3, 4, 5]

# file_name = 'numbers.json'  # - .json to indicate that the data in 
#                             #   the file is stored in the JSON format

# with open(file_name, "w") as file_obj:
#     json.dump(my_list, file_obj)

# with open(file_name, "r") as file_obj:
#     contant = json.load(file_obj)

# print("The contant of the file using json:", contant)
# print("The type of data that stored: ", type(contant))

# with open("number.txt", "w") as file_obj:
#     file_obj.write(str(my_list))        # Note that you have to convert to str, you can store another type of data
#                                         # You can see that you can't to store any type of data structure,
#                                         # just string you can to store, otherwise will be error, so you have
#                                         # to use json
# print()

# with open("number.txt", "r") as file_obj:
#     contant = file_obj.read()
 
# print("The contant of the .txt file :", contant)
# print("The type of data that stored: ", type(contant))



# # Saving and Reading User-Generated Data:

user_name = input("What is your name? ")
file_name = "user_name.json"

with open(file_name, "w") as file_obj:
    """prompt the user for their name the first time they run a program and then 
       remember their name when they run the program again.
    """
    json.dump(user_name, file_obj)
    print("We'll remember you when you come back, " + user_name + "!")



with open(file_name, "r") as file_obj:
    user_name = json.load(file_obj)
    print("Welcome back, " + user_name + "!")

# Note that if there more than one user_name, error will happend



