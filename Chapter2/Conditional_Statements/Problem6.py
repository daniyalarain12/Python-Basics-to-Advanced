#WRITE A PROGRAM TO FIND THE GREATEST OF 3 NUMBERS ENTERED BY THE USER.

num1 = int(input("ENTER 1ST NUMBER : "))
num2 = int(input("ENTER 2ND NUMBER : "))
num3 = int(input("ENTER 3RD NUMBER : "))
if(num1>=num2 and num1>=num3): 
    print("LARGEST NUMBER :", num1)
elif(num2>=num3):
    print("LARGEST NUMBER :", num2)
else:
    print("LARGEST NUMBER :", num3)
