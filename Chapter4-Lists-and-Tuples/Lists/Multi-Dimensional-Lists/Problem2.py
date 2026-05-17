# step1: Store atleast 5 user data (Name,Fname, Phone, Email and Pass) in a single multi dimensional list.
# step2: Ask user for useremail and userpass.
# step3: Match if useremail and userpass matches to any of the stored user.
# step4: Print user matched along with the details of that user otherwise print user not found.

data = [
    ["DANIYAL","GHULAM SHABBIR", "03092313464","daniyalarain123786@gmail.com","dani123"],
    ["UMAIR","TAHIR", "03042313464","umair123786@gmail.com","umair123"],
    ["RAHEEM","SHABBIR AHMED", "03192313464","raheem123786@gmail.com","raheem123"],
    ["YASIR","ABDULLAH", "03162313464","yasir123786@gmail.com","yasir123"],
    ["BABAR","YASIR", "03456313464","babar123786@gmail.com","babar123"],
]

userEmail = input("ENTER USER EMAIL : ")

for i in range(len(data)):
    user = data[i]
    if (userEmail == user[3]):
        userPass = input("ENTER USER PASSWORD : ")
        if (userPass == user[4]):
            print(f"NAME : {user[0]}")
            print(f"FATHER NAME : {user[1]}")
            print(f"PHONE : {user[2]}")
            break
else:
    print("USER NOT FOUND")
