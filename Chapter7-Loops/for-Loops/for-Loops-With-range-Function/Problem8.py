# Step 1: Add three options at the start of the program:
# Login
# Check User
# Exit
# Step 2: Create a user login system in the program. Store five variables: Name, Father Name, Email, CNIC, and Password.
# Step 3: Take two inputs from the user: userEmail and userPassword.
#         If the entered password matches the stored password, display all the details of the user.
# Step 4: If the user enters an incorrect password three times, display the following message:
#         "You have entered the wrong password three times and your account has been blocked. Please call the helpline."
# Step 5: Once the user enters the wrong password three times, the user account should be blocked and the user should no longer
#         be able to access the information.

name, fName, email, CNIC, password = "DANIYAL", "GHULAM SHABBIR", "daniyalarain123786@gmail.com", "44101-7359337-5", "da12"
status = "UNBLOCKED"

while True:
    selection = int(input("1. LOGIN\n2. CHECK USER\n3. EXIT\nENTER YOUR SELECTION : "))

    if(selection==1):
        userEmail = input("ENTER USER EMAIL : ")
        if(status=="UNBLOCKED"):
            if(userEmail==email):
                counter = 0
                for i in range(3):
                    userPass = input("ENTER YOUR PASSWORD : ")
                    if(userPass==password):
                        print(f"name = {name}, fName = {fName}, CNIC = {CNIC}")
                        break
                    else:
                        counter += 1
                        if(counter==3):
                            print("You have entered the wrong password three times and your account has been blocked. Please call the helpline.")
                            status = "BLOCKED"
                            break
                        print("INCORRECT PASSWORD")
            else:
                print("INCORRECT EMAIL")
        else:
            print("YOUR ACCOUNT HAS BEEN BLOCKED")
    elif(selection==2):
        userEmail = input("ENTER YOUR EMAIL : ")
        if(userEmail==email):
            print("YOUR ACCOUNT IS",status)
    elif(selection==3):
        print("EXITING THE PROGRAM")
        exit(0)
    else:
        print("WRONG SELECTION")
