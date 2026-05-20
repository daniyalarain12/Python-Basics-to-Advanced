# Write a Python program that implements a login system using file handling where the program reads user data from a file, takes email and password
# as input from the user, checks whether the entered credentials match any record, prints the user details if a match is found, otherwise displays
# "USER NOT FOUND", and also handles FileNotFoundError using a try-except block.

try:
    with open("data2.txt") as f:
        userEmail = input("ENTER USER EMAIL : ")
        userPassword = input("ENTER USER PASSWORD : ")
        data = f.readlines()
        for line in data:
            user = line.strip().split(",")
            if (user[4] == userEmail and user[5] == userPassword):
                print(user)
                break
        else:
            print("USER NOT FOUND")
except FileNotFoundError as e:
    print(e)
