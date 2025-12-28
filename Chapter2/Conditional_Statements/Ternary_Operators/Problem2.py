#Write a Python program that takes age as input and uses conditional indexing to determine whether a person can vote.

age = int(input("ENTER YOUR AGE : "))
vote = ("no","yes") [age>=18]
print("CAN VOTE :",vote)
