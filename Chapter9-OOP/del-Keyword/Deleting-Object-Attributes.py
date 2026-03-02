# del KEYWORD
# USED TO DELETE OBJECT PROPERTIES OR OBJECT ITSELF.

class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("DANIYAL ARAIN")
print(s1.name)
del s1.name
print(s1.name)
