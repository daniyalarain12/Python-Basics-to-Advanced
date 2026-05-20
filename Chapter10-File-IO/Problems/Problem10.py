# CREATE A data.txt FILE FOR STORING DETAILS OF AT-LEAST 5 USERS. (uid, name,  email, phone, cnic)
# CREATE A PROGRAM FOR UPDATING USER DETAILS BY USER ID.

data = [
    ["24SW039","DANIYAL","dani@gmail.com", "03092313464","44101-7359337-5"],
    ["24SW038","NABEEL","nabeel@gmail.com", "03123456789","44101-1234567-1"],
    ["24SW063","RAHEEM","raheem@gmail.com", "03234567890","44101-7654321-2"],
    ["24SW042","YASIR","yasir@gmail.com", "03345678901","44101-9876543-3"],
    ["24SW075","QAYOOM","qayoom@gmail.com", "03456789012","44101-4567891-4"]
]

with open("data.txt","w") as f:
    for user in data:
        f.write(",".join(user)+"\n")

users = []

with open("data.txt","r") as f:
    data = f.readlines()
    for user in data:
        users.append(user.strip().split(","))

userId = input("ENTER USER ID : ")
    
for i in range(len(users)):
    if (userId == users[i][0]):
        users[i][1] = input("ENTER UPDATED USER NAME : ")
        users[i][2] = input("ENTER UPDATED EMAIL : ")
        users[i][3] = input("ENTER UPDATED PHONE : ")
        users[i][4] = input("ENTER UPDATED CNIC : ")
        print("USER UPDATED SUCCESSFULLY")
        break
else:
    print("USER NOT FOUND")

with open("data.txt","w") as f:
    for user in users:
        f.write(",".join(user)+"\n")
