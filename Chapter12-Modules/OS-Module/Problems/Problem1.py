# Change the current working directory to "Chapter9/New directory/" using the OS module and then open and read the contents of "data.txt"
# file from that directory.

import os

os.chdir("Chapter9/New directory/")
with open("data.txt","r") as f:
    print(f.read())
