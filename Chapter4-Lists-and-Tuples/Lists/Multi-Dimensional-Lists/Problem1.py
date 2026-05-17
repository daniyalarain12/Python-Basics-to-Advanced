# Write a Python program to store and display the username, email, and password of at least 5 users using a multi-dimensional list 
# and nested loops.

data = [
    ["DANIYAL","daniyalarain123786@gmail.com","dani123"],
    ["UMAIR","umair123786@gmail.com","umair123"],
    ["RAHEEM","raheem123786@gmail.com","raheem123"],
    ["YASIR","yasir123786@gmail.com","yasir123"],
    ["BABAR","babar123786@gmail.com","babar123"],
]

for i in range(len(data)):
    user = data[i]
    for j in range(len(user)):
        print(user[j],end=" ")
    print()
