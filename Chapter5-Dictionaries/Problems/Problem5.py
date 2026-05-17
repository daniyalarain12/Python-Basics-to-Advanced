# Create a Python program that stores multiple users in a list of dictionaries containing personal and academic information, and uses
# list comprehension to generate a new list of tuples containing only the name and email of each user, then display the resulting list.

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

mylist = [(user["NAME"], user["EMAIL"]) for user in data]
print(mylist)
