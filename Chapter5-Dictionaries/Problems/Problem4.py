# Create a Python program that stores multiple users in a dictionary where each user has a unique ID (u1, u2, u3) and contains 
# personal and academic information, and implements a login system that asks the user for an email and password to verify credentials 
# and display the corresponding user details or show "USER NOT FOUND" if no matching email exists.

data = {
    "u1" : {
        "NAME" : "DANIYAL ARAIN",
        "CGPA" : 3.75,
        "AGE" : 19,
        "IsAdult" : True,
        "SUBJECTS" : ["PF","OOP","DSA","DBS"],
        "LANGUAGES" : ("C++","JAVA","PYTHON"),
        "EMAIL" : "daniyalarain123786@gmail.com",
        "password" : "da12"
    },
    "u2" : {
        "NAME" : "SAMI ARAIN",
        "CGPA" : 3.30,
        "AGE" : 19,
        "IsAdult" : True,
        "SUBJECTS" : ["PF","OOP","DSA","DBS"],
        "LANGUAGES" : ("C++","JAVA","PYTHON"),
        "EMAIL" : "samiarain123786@gmail.com",
        "password" : "sa29"
    },
    "u3" : {
        "NAME" : "IZHAN ARAIN",
        "CGPA" : 3.60,
        "AGE" : 19,
        "IsAdult" : True,
        "SUBJECTS" : ["PF","OOP","DSA","DBS"],
        "LANGUAGES" : ("C++","JAVA","PYTHON"),
        "EMAIL" : "izhanarain123786@gmail.com",
        "password" : "iz23"
    }
}

userEmail = input("ENTER USER EMAIL : ")

for userId, userValue in data.items():
    if(userValue["EMAIL"] == userEmail):
        userPass = input("ENTER USER PASSWORD : ")
        if(userValue["password"] == userPass):
            for k, v in userValue.items():
                print(f"{k} : {v}")
            break
else:
    print("USER NOT FOUND")
