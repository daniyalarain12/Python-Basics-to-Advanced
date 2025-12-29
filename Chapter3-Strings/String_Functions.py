#FUNCTIONS OF STRINGS

#startswith AND endswith FUNCTION
str = "I AM STUDYING PYTHON"
print(str.startswith("I AM"))  # startswith function returns True if a string starts with given substring else returns False.
print(str.endswith("ON"))      # endswith function returns True if a string ends with given substring else returns False.

#CAPITALIZE FUNCTION
str = "apnaCollege"
print(str)
print(str.capitalize())        # Capitalize 1st character of a string.

#REPLACE FUNCTION
str = "I AM STUDYING PYTHON"
print(str.replace("PYTHON","MACHINE LEARNING"))   # Replace all occurences of old substring with new substring.
print(str.replace("I","II"))

#FIND FUNCTION
str = "I AM STUDYING PYTHON"   
print(str.find("YI"))           # Returns starting index of 1st occurence of a given substring in a string.

#COUNT FUNCTION
str = "I AM STUDYING MACHINE LEARNING"
print(str.count("I"))           # Counts the occurence of a given substring in a string.
