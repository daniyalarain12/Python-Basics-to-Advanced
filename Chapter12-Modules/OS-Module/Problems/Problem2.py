# Write a Python program using the OS module to traverse the current working directory and display only the files having the .py extension.

import os

for file in os.listdir("."):
    if (file.endswith(".py")):
        print(file)
