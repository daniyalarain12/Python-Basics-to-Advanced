# ATTRIBUTES
# CLASS AND INSTANCE ATTRIBUTES

class Student:
    uni_name = "MUET"            # CLASS ATTRIBUTE

    def __init__(self, name):
        self.name = name         # INSTANCE ATTRIBUTE
    
s1 = Student("DANIYAL ARAIN")
print(s1.name)
print(s1.uni_name)

s2 = Student("UMAIR BHUTTO")
print(s2.name)
print(s2.uni_name)

print(Student.uni_name)
