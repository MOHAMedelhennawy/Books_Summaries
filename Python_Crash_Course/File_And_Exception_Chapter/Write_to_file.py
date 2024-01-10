#!/usr/bin/python3

# Why you may need to Write in a file?
# - One of the simplest ways to save data is to write it to a file. When you write 
#   text to a file, the output will still be available after you close the terminal 
#   containing your program’s output. You can examine output after a program 
#   finishes running, and you can share the output files with others as well. You 
#   can also write programs that read the text back into memory and work with 
#   it again later


file_name = "programming.txt"

with open(file_name, "w") as file_obj:
    file_obj.write("I love programming")    # it's create a file if file not exist

# - But note that python write only string, if you want to store numerical data in a 
#   text file, you’ll have to convert the data to string format first using the str() function.
#
# - Note that the write() function doesn’t add any newlines to the text you write.





# ===============================================================
# ===============================================================



# Appending to a File:

# Why you may need to use append?..
# - If you want to add content to a file instead of writing over existing content, 
#   you can open the file in append mode.


file_name = "programming.txt"

with open(file_name, "a") as file_obj:
    file_obj.write("I also love finding meaning in large datasets.\n")
    file_obj.write("I love creating apps that can run in a browser.\n")