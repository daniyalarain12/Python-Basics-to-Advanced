# property DECORATOR
# WE USE @property DECORATOR ON ANY METHOD IN THE class TO USE THE METHOD AS A PROPERTY.

class Student:
    def __init__(self, phy, chem, maths):
        self.phy = phy
        self.chem = chem
        self.maths = maths

    @property           # decorator
    def percentage(self):
        return (self.phy + self.chem + self.maths) / 3

s1 = Student(97,98,99)
print(s1.percentage)

s1.phy = 80
print(s1.percentage)
