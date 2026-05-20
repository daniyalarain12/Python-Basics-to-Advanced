# Write a Python program that takes user details (name, father name, phone number, email, and password) as input and appends them to a CSV file.
# Each new record should be added on a new line in comma-separated format without deleting previous data.

name = input("ENTER YOUR NAME : ")
fName = input("ENTER YOUR FATHER NAME : ")
phone = input("ENTER YOUR PHONE NO : ")
email = input("ENTER YOUR EMAIL : ")
password = input("ENTER YOUR PASSWORD : ")

data = f"{name},{fName},{phone},{email},{password}\n"
with open("data.csv","a") as f:
    f.write(data)
