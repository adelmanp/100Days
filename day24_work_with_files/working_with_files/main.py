#!/usr/bin/python3


# example of opening a file, but required to manually close the file
# file = open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# open the file and let python auto close it.
with open("my_file.txt") as file:
    contents = file.read()
    print(contents)


with open("new_file.txt", mode="w") as file:
    file.write("New text.")
