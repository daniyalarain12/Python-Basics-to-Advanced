# CONSTRUCTOR OR __init__ FUNCTION
# ALL CLASSES HAVE A FUNCTION CALLED __init__(), WHICH IS ALWAYS EXECUTED WHEN THE OBJECT IS BEING EXECUTED.

class Student:

    # DEFAULT CONSTRUCTORS
    def __init__(self):
        pass

    # PARAMETERIZED CONSTRUCTORS
    def __init__(self, name, marks):      # THE self PARAMETER IS THE REFERENCE TO THE CURRENT INSTANCE OF THE CLASS,
        self.name = name                  # AND IS USED TO ACCESS VARIABLES THAT BELONGS TO THE CLASS.
        self.marks = marks
        print(self)

s1 = Student("DANIYAL ARAIN",98)
print(s1.name)
print(s1.marks)
print(s1)
