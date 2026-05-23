# KEYWORD ARGUMENTS (**kwargs)

# Keyword arguments allow values to be passed to functions or constructors using parameter names instead of position.
# In inheritance, **kwargs is used to pass remaining named arguments from child to parent classes automatically using super().
# This avoids manually passing all parent class parameters and makes the code more flexible, scalable, and maintainable.

class Human:
    def __init__(self, color, hands=2):
        self.color = color
        self.hands = hands

class Person(Human):
    def __init__(self, name, fName, age, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.fName = fName
        self.age = age

class Student(Person):
    def __init__(self, rollNo, CGPA, **kwargs):
        super().__init__(**kwargs)
        self.rollNo = rollNo
        self.CGPA = CGPA

std1 = Student("24SW039", 3.71, name="DANIYAL", fName="GHULAM SHABBIR", age=20, color="BROWN")
print(std1.rollNo)
print(std1.name)
print(std1.color)
print(std1.hands)
