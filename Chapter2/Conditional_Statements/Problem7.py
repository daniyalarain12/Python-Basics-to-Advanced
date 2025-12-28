#WRITE A PROGRAM TO FIND THE GREATEST OF 4 NUMBERS ENTERED BY THE USER.

num1 = int(input("ENTER 1ST NUMBER : "))
num2 = int(input("ENTER 2ND NUMBER : "))
num3 = int(input("ENTER 3RD NUMBER : "))
num4 = int(input("ENTER 4TH NUMBER : "))
if(num1>=num2 and num1>=num3 and num1>=num4):
    print("LARGEST NUMBER :", num1)
elif(num2>=num3 and num2>=num4):
    print("LARGEST NUMBER :", num2)
elif(num3>=num4):
    print("LARGEST NUMBER :", num3)
else:
    print("LARGEST NUMBER :", num4)
