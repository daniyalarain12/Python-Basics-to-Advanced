# class METHODS
# A class METHOD IS BOUND TO THE class AND RECEIVES THE class AS AN IMPLICIT FIRST ARGUMENT.
# Note: static METHOD CAN'T ACCESS OR MODIFY class STATE.

class Person:
    name = "Anonymous"
    @classmethod               # DECORATOR
    def changeName(cls, name):
        cls.name = name

p1 = Person()
p1.changeName("DANIYAL")
print(p1.name)
print(Person.name)
