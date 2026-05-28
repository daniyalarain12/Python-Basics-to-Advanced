# JSON MODULE
# JSON (JavaScript Object Notation) is a lightweight data format used for storing and exchanging data. It is easy for humans to read and easy 
# for machines to understand. Python provides a built-in json module to work with JSON data.

# JSON MODULE METHODS
# json.loads(json_string)                 ---> Converts a JSON string into a Python object (usually a dictionary).
# json.dumps(python_object)               ---> Converts a Python object into a JSON string.
# json.load(file_object)                  ---> Reads JSON data from a file and converts it into a Python object.
# json.dump(python_object, file_object)   ---> Writes Python object data into a JSON file.

import json

json_string = '{"name" : "RABEEA JAFFARI", "isTeacher" : true}'
print(type(json_string))

python_object = json.loads(json_string)                   # CONVERT JSON STRING INTO PYTHON DICTIONARY
print(type(python_object), python_object)

python_object = {
    "name" : "RABEEA JAFFARI",
    "isTeacher" : True
}
print(type(python_object))

json_string = json.dumps(python_object)                    # CONVERT PYTHON OBJECT INTO JSON STRING
print(type(json_string), json_string)

with open("practice.json","r") as f:
    python_object = json.load(f)                           # READ JSON DATA AND CONVERT INTO PYTHON OBJECT
    print(type(python_object),python_object)

data = {
    "name" : "RABEEA JAFFARI",
    "isTeacher" : True
    }

with open("practice.json","w") as f:
    json_string = json.dump(data,f)                        # WRITE PYTHON OBJECT INTO JSON FILE

data = {
    "name" : "RABEEA JAFFARI",
    "isTeacher" : True
    }

with open("practice.json","w") as f:
    json_string = json.dump(data, f, sort_keys=True, indent=4)
