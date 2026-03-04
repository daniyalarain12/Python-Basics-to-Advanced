class Person:
    name = "Anonymous"
    def changeName(self, name):
        Person.name = name

p1 = Person()
p1.changeName("DANIYAL")
print(p1.name)
print(Person.name)
