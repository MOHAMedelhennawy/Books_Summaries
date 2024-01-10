#!/usr/bin/python3

# Reading an entire file:
with open("pi_digits.txt") as file_obj:
    """open: Returns an object representing the file "pi_digits.txt",
       and store it in file_obj
    """
    content = file_obj.read()
    print(content.rstrip())
# print(file_obj.read())  => ValueError: I/O operation on closed file.


# =======================================================================
# =======================================================================


# Read line by line:
file_name = "pi_digits.txt"
with open(file_name) as file_obj:
    for line in file_obj:
        print(line, end="")         # Without using rstrip or end="", you find even more blank lines
                                    # and it's new lines appear because, The print statement adds its own 
                                    # newline each time we call it 



# =======================================================================
# =======================================================================


# Making a list of lines from a file:
"""The following example stores the lines of pi_digits.txt in a list inside the 
 with block and then prints the lines outside the with block:
"""

file_name = 'pi_digits.txt'
with open(file_name) as file_obj:
    lines = file_obj.readlines()    # Store a lines as a list

print(lines)    # Output => ['3.1415926535 \n', ' 8979323846 \n', ' 2643383279\n']
for line in lines:
    print(line.rstrip())



# =======================================================================
# =======================================================================



# Working with a File’s Contents:
file_name = 'pi_digits.txt'
with open(file_name) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    # pi_string += line.rstrip()     # => Just remove the whitespace that was on the left side of the digits in each line ..
                                   #    Output: 3.1415926535 8979323846 2643383279
    pi_string += line.strip()    # => So get ride of that by using strip() To delet both whitespace at the First, End of the line
print(pi_string)
print(len(pi_string))



# =======================================================================
# =======================================================================


# Large Files, One Million Digits:

# => first write a program to write a big number in a file:
file_name = "pi_million_digits.txt"
with open(file_name, "w") as file_obj:
    for i in range(1, 1000000):
        file_obj.write(f"{str(i)} ")


# => Then write a program that print just first 50 charchter:
with open(file_name) as file_obj:
    lines = file_obj.readlines()

pi_string = ''
for line in lines:
    pi_string += line.strip()

print(pi_string[:51] + "...")



# =======================================================================
# =======================================================================


# Is Your Birthday Contained in Pi?
# If you too been curious to know if my birthday appears anywhere in the 
# digits of 1 to 1000000, see this program:

file_name = "pi_million_digits.txt"

with open(file_name) as file_obj:
    lines = file_obj.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

Birthday = input("Enter your birthday, in the form mmddyy: ")
if Birthday in pi_string:
    print("Your birthday appears in the first million digits!")
else:
    print("Your birthday does not appear in the first million digits of pi.")








# Notes from the book:
#
#   * Read: return empty string when it reaches the end of the file,
#     and hows up as a blank line
#
#   * rstrip(): removes, or strips, any whitespace 
#     characters from the right side of a string
#
#   * When a relative path is too long, it's helpful
#     to store it in a varible, For Example:
#     =>    file_path = '/home/ehmatthes/other_files/text_files/filename.txt'   "In linux"
#     =>    file_path = 'C:\Users\ehmatthes\other_files\text_files\filename.txt'    "In Windows"
#
#   * Why you may need to read a file line by line:
#       => you might want to modify the text in the file in some way.
#          For example: you wont to modify any line that contain a specific word,
#                       and rewrite that line with a specific kind of formatting.
#                       see ""Read line by line Chapter""
#
#   * Why you may need to store the contant of the file in the variable:
#       => When you use with statmen, the file object returned by open() is only available inside 
#          the with block that contains it, so you can store the file line's in a list inside the block
#          to process parts of the file immediately and postpone some processing for later in the program
#          outside the with statment. For Example see ""Making a List of Lines from a File Chapter""