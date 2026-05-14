# Create variables name, fname, phone, email, and pass to store your information, then create useremail and userpass to take input from the user, and compare them with the 
# stored email and password; if both match, print the user’s name, father name, and phone number, otherwise print "incorrect pass or email".

name, fName, phone, email, pas = "DANIYAL", "GHULAM SHABBIR", "03092313464", "daniyalarain123786@gmail.com", "dani123786"
userEmail = input("ENTER USER EMAIL : ")
if (userEmail == email):
    userPass = input("ENTER USER PASSWORD : ")
    if (userPass == pas):
        print(f"name = {name}, fName = {fName}, phone = {phone}")
    else:
        print("INCORRECT PASSWORD")
else:
    print("INCORRECT EMAIL")
