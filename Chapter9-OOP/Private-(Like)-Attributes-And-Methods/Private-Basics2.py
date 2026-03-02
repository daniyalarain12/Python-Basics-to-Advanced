# PRIVATE (LIKE) ATTRIBUTES AND METHODS
# CONCEPTUAL IMPLEMENTATION IN PYTHON
# PRIVATE ATTRIBUTES AND METHODS ARE MEANT TO BE USED ONLY WITHIN THE class AND ARE NOT ACCESSIBLE FROM OUTSIDE THE class.

class Person:
    __name = "Anonymous"

    def __hello(self):
        print("HELLO")

    def welcome(self):
        self.__hello()

p1 = Person()
p1.welcome()
