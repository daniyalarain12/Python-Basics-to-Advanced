# DICTIONARIES IN PYTHON

# DICTIONARY IS A BUILT-IN DATA TYPE IN PYTHON.
# DICTIONARIES ARE USED TO STORE DATA IN KEY-VALUE PAIRS.
# THEY ARE UNORDERED, MUTABLE (CHANGEABLE) AND DON'T ALLOW DUPLICATE KEYS.
# IN DICTIONARIES, KEYS CAN NOT BE LISTS OR DICTIONARIES.

info = {
    "NAME" : "DANIYAL ARAIN",
    "CGPA" : 3.75,
    "AGE" : 19,
    "IsAdult" : True,
    "SUBJECTS" : ["PF","OOP","DSA","DBS"],
    "LANGUAGES" : ("C++","JAVA","PYTHON")
}
print(info)
print(type(info))
print("LENGTH :",len(info))
print("OLD CGPA :",info["CGPA"])
info["CGPA"] = 3.78
print("NEW CGPA :",info["CGPA"])
info["SURNAME"] = "ARAIN"        # ADDING NEW KEY-VALUE PAIR IN THE DICTIONARY
print(info)

null_dict = {}                   # CREATING EMPTY DICTIONARY
print(null_dict)
null_dict["HEIGHT"] = 5.11
print(null_dict)
