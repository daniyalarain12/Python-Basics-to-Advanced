# Create a list of user details including Name, Father Name, CNIC, Phone, Email, and Password, then take email and password input from 
# the user and compare them with the stored email and password; if both match, print the user’s details, otherwise print 
# "incorrect email or password".

data = ["DANIYAL", "GHULAM SHABBIR", "44101-7359337-5", "03092313464", "daniyalarain123786@gmail.com", "da12"]
label = ["NAME", "FATHER NAME", "CNIC", "PHONE", "EMAIL", "PASSWORD"]
userEmail = input("ENTER USER EMAIL : ")
if (userEmail == data[4]):
    userPass = input("ENTER USER PASSWORD : ")
    if (userPass == data[5]):
        for i,j in zip(label,data):           # zip() FUNCTION COMBINES 2 LISTS
            print(i,":",j)
    else:
        print("INCORRECT PASSWORD")
else:
    print("INCORRECT EMAIL")
