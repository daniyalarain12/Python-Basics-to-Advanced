# ENCAPSULATION
# WRAPPING DATA AND FUNCTIONS INTO A SINGLE UNIT (OBJECT).

class Student:
    def __init__(self,name):
        self.name = name

    def welcome(self):
        print("WELCOME",self.name)

s1 = Student("DANIYAL ARAIN")
s1.welcome()
