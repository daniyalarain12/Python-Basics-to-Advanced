# Write a Python program that stores multiple users’ details (name, father name, email, and password) in a list. Then write this data into a
# CSV file named data.csv using file handling. Each user’s record should be saved in a separate line with values separated by commas.

data = [
    ["DANIYAL","SHABBIR","dani@gmail.com","da12"],
    ["NABEEL","SHAHID","dani@gmail.com","da12"],
    ["RAHEEM","KATIAR","dani@gmail.com","da12"],
    ["YASIR","NAWAZ","dani@gmail.com","da12"],
]

with open("data.csv","a") as f:
    for user in data:
        f.write(",".join(user)+"\n")
