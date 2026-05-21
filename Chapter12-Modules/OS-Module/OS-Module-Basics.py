# os MODULE
# The OS module in Python provides functions for interacting with the operating system. It allows us to perform tasks like working with
# files and folders, changing directories, accessing environment variables, and executing system commands.

# os.environ[]    ---> Used to access environment variables of the operating system.
# os.getcwd()     ---> Returns the path of the current working directory.
# os.chdir()      ---> Used to change the current working directory.
# os.listdir()    ---> Returns a list of all files and folders from a specified directory.
# os.walk()       ---> Traverses directories recursively and returns paths, folders, and files.
# os.system()     ---> Executes operating system commands directly from Python.

import os

# print(os.environ["OS"])

# print(os.getcwd())

# os.chdir("New directory/")
# print(os.getcwd())

# cwd = os.getcwd()
# print(os.listdir(cwd))
# print(os.listdir("."))                      # "." represents the current working directory
# print(os.listdir("New directory"))
# print(os.listdir("F:/DBS"))

# for file in os.walk("New directory/"):
#     print(file)

# os.system("mkdir newFolder")
