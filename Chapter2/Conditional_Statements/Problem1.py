#Write a program that takes age as input from the user and determine whether the user can drive and/or vote based on their age.

age = int(input("ENTER YOUR AGE : "))
if(age>=18):
    print("YOU CAN DRIVE AND VOTE")
elif(age>=16 and age<18):
    print("YOU CAN DRIVE BUT CAN NOT VOTE")
else:
    print("YOU CAN NOT DRIVE AND CAN NOT VOTE")
