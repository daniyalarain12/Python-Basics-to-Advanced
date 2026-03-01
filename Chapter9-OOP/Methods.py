# METHODS
# METHODS ARE FUNCTIONS THAT BELONG TO OBJECTS.

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def welcome(self):
        print("WELCOME",self.name)

    def get_marks(self):
        return self.marks    

s1 = Student("DANIYAL ARAIN",98) 
s1.welcome()
print(s1.get_marks())
