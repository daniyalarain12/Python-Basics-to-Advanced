# Create a class named Person to demonstrate the concept of abstraction in Python. The class should contain attributes for storing a person's name
# and age along with setter and getter methods to assign and retrieve these values. Then create an object of the class, set the name as
# "DANIYAL ARAIN" and age as 20, and display both values using getter methods.

class Person:
    def __init__(self):
        self.name = ""
        self.age = 0

    # SETTER METHODS
    def set_name(self,name):
        self.name = name
    def set_age(self,age):
        self.age = age

    # GETTER METHODS
    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    
p1 = Person()

# Setting values using setter methods
p1.set_name("DANIYAL ARAIN")
p1.set_age(20)

# Displaying values using getter methods
print(p1.get_name())
print(p1.get_age())
