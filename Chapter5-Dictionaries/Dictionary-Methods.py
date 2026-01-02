#DICTIONARY METHODS

info = {
    "NAME" : "DANIYAL ARAIN",
    "CGPA" : 3.75,
    "AGE" : 19,
    "IsAdult" : True,
    "SUBJECTS" : ["PF","OOP","DSA","DBS"],
    "LANGUAGES" : ("C++","JAVA","PYTHON")
}

print(info.keys())                              # RETURNS ALL THE KEYS
print(list(info.keys()))

print(info.values())                            # RETURNS ALL THE VALUES
print(list(info.values()))

print(info.items())                             # RETURNS ALL KEY-VALUE PAIRS AS TUPLES
print(list(info.items()))

pairs = list(info.items())
print(pairs[0])

print("CGPA :",info.get("CGPA"))                # RETURNS THE VALUE ACCORDING TO KEY

info.update({"NATIONALITY" : "PAKISTANI"})      # INSERTS THE SPECIFIED ITEMS TO THE DICTIONARY
print(info)

new_dict = {
    "CGPA" : 3.81,
    "CITY" : "HYDERABAD"
}
info.update(new_dict)
print(info)
