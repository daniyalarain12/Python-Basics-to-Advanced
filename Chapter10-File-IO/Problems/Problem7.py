# Write a Python program that takes user details (name, father name, phone number, email, and password) as input and stores them in a CSV file.
# The program should save the data in comma-separated format and overwrite any existing content in the file.

name = input("ENTER YOUR NAME : ")
fName = input("ENTER YOUR FATHER NAME : ")
phone = input("ENTER YOUR PHONE NO : ")
email = input("ENTER YOUR EMAIL : ")
password = input("ENTER YOUR PASSWORD : ")

data = f"{name},{fName},{phone},{email},{password}"
with open("data.csv","w") as f:
    f.write(data)
