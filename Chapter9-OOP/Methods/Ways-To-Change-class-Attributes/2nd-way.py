class Person:
    name = "Anonymous"
    def changeName(self, name):
        self.__class__.name = name

p1 = Person()
p1.changeName("DANIYAL")
print(p1.name)
print(Person.name)
