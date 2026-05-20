# Create a console-based Student Management System in Python using functions and file handling with a CSV file. The program should allow the user
# to add student records containing Student ID, Name, Father Name, CNIC, and Email, view all stored student records, and search for a student by 
# ID through a menu-driven system. The program should also use exception handling to handle file-related errors properly.

def addStudent():
    id = f"SMIT-{len(viewAllStudents()+1)}"
    name = input("ENTER NAME : ")
    fName = input("ENTER FATHER NAME  : ")
    CNIC = input("ENTER CNIC : ")
    email = input("ENTER EMAIL : ")
    
    user = f"{id},{name},{fName},{CNIC},{email}\n"
    with open("data.csv","a") as f:
        f.write(user)

def viewAllStudents():
    try:
        with open("data.csv","r") as f:
            users = f.readlines()
            for user in users:
                print(user.strip().split(","))
    except FileNotFoundError as e:
        print(e)

def searchById():
    id = input("ENTER ID : ")
    try:
        with open("data.csv","r") as f:
            users = f.readlines()
            for user in users:
                value = user.strip().split(",")
                if (value[0]==id):
                    print(value)
                    break
            else:
                print("USER NOT FOUND")
    except FileNotFoundError as e:
        print(e)

while True:
    selection = int(input("MENU\n1. ADD STUDENT\n2. VIEW ALL STUDENTS\n3. SEARCH BY ID\n4. EXIT\nENTER ANY OPTION : "))
    if (selection == 1):
        addStudent()
    elif (selection == 2):
        viewAllStudents()
    elif (selection == 3):
        searchById()
    elif (selection == 4):
        print("EXITING THE PROGRAM")
        break
    else:
        print("WRONG SELECTION")
