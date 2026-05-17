# Create a Python program that stores multiple users in a list of dictionaries containing personal and academic information, 
# and implements a login system where the user enters their email and password to verify credentials and display the corresponding 
# user details or show "USER NOT FOUND" if the email does not exist.

data = [
    {
    "NAME" : "DANIYAL ARAIN",
    "CGPA" : 3.75,
    "AGE" : 19,
    "IsAdult" : True,
    "SUBJECTS" : ["PF","OOP","DSA","DBS"],
    "LANGUAGES" : ("C++","JAVA","PYTHON"),
    "EMAIL" : "daniyalarain123786@gmail.com",
    "password" : "da12"
},
{
    "NAME" : "SAMI ARAIN",
    "CGPA" : 3.30,
    "AGE" : 19,
    "IsAdult" : True,
    "SUBJECTS" : ["PF","OOP","DSA","DBS"],
    "LANGUAGES" : ("C++","JAVA","PYTHON"),
    "EMAIL" : "samiarain123786@gmail.com",
    "password" : "sa29"
},
{
    "NAME" : "IZHAN ARAIN",
    "CGPA" : 3.60,
    "AGE" : 19,
    "IsAdult" : True,
    "SUBJECTS" : ["PF","OOP","DSA","DBS"],
    "LANGUAGES" : ("C++","JAVA","PYTHON"),
    "EMAIL" : "izhanarain123786@gmail.com",
    "password" : "iz23"
}
]

userEmail = input("ENTER USER EMAIL : ")

for user in data:
    if(user["EMAIL"] == userEmail):
        userPass = input("ENTER USER PASSWORD : ")
        if(user["password"] == userPass):
            for k, v in user.items():
                print(f"{k} : {v}")
            break
else:
    print("USER NOT FOUND")
