# SETS IN PYTHON

# SET IS A BUILT-IN DATA TYPE IN PYTHON WHICH IS UNORDERED AND MUTABLE.
# A SET STORES ONLY UNIQUE ELEMENTS (NO DUPLICATES).
# THE ELEMENTS OF A SET MUST BE IMMUTABLE. THEREFORE, LISTS AND DICTIONARIES CAN NOT STORED IN A SET.

set1 = {1,2,3,4}
set2 = {1,2,3,1,3,4,2,5,4}
set3 = {19,"DANIYAL",5.11,True,("OOP","DSA")}
print(set1)
print(set2)                      # DUPLICATE VALUES WILL NOT PRINT AND ONLY UNIQUE VALUES WILL PRINT
print(set3)
print(type(set1))
print(type(set2))
print(type(set3))
print("LENGTH :",len(set1))
print("LENGTH :",len(set2))      # ONLY UNIQUE VALUES WILL BE COUNTED
print("LENGTH :",len(set3))

empty_set = set()                # CREATING EMPTY SET
print(type(empty_set))
