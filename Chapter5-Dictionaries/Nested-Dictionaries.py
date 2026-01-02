#NESTED DICTIONARIES

student = {
    "NAME" : "DANIYAL ARAIN",
    "MARKS" : {
        "PF" : 92,
        "OOP" : 96,
        "DSA" : 93
    }
}
print(student)
print(student["MARKS"])
print(student["MARKS"]["OOP"])     # ACCESSING VALUE FROM NESTED DICTIONARY
