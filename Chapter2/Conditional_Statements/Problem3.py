#Write a Python program that takes marks as input and displays the corresponding grade.

marks = int(input("ENTER YOUR MARKS : "))
if(marks>=90):
    print("YOUR GRADE IS : A")
elif(marks>=80 and marks<90):
    print("YOUR GRADE IS : B")
elif(marks>=70 and marks<80):
    print("YOUR GRADE IS : C")
else:
    print("YOUR GRADE IS : D")
