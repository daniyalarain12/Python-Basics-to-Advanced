# Write a Python program using the OS module to traverse all folders, subfolders, and files from the current working directory using os.walk()
# and display their paths, folders, and file names.

import os

cwd = os.getcwd()
for path, folder, file in os.walk(cwd):
    print(f"PATH : {path}")
    print(f"FOLDER : {folder}")
    print(f"FILE : {file}")
    print("*"*20)
