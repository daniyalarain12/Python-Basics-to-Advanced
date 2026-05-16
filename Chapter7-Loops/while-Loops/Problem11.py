# Create an atm note counting program that takes a number as an input from the user and prints how many 5000, 1000 and 500 notes
#  are there in the number.
# - Example: 9500 is a number from the user which includes 1 note from 5000, 4 notes of 1000 and 1 note for 500.
# - Note: add a restriction to the user to enter a  number that is a multiple of 500 only.

while True:
    print("*"*20)
    selection = int(input("1. NOTE COUNTER\n2. EXIT\nENTER YOUR SELECTION : "))
    if(selection==1):
        while True:
            num = int(input("ENTER ANY NUMBER (ONLY MULTIPLE OF 500) : "))
            note5000, note1000, note500 = 0, 0, 0

            if(num%500 == 0):
                if(num >= 5000):
                    note5000 = num // 5000
                    num = num % 5000
                if(num >= 1000):
                    note1000 = num // 1000
                    num = num % 1000
                if(num >= 500):
                    note500 = num // 500
                print("COUNT OF 5000 NOTES : ",note5000)
                print("COUNT OF 1000 NOTES : ",note1000)
                print("COUNT OF 500 NOTES : ",note500)
                break
            else:
                print("ENTER CORRECT NUMBER (MULTIPLE OF 500)")
    elif(selection==2):
        print("EXITING THE PROGRAM")
        exit(0)
    else:
        print("WRONG SELECTION")
