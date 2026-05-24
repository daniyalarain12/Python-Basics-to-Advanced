# Write a Python program using Object-Oriented Programming (OOP) concepts to create a class named Calculate that stores a list of numbers and
# demonstrates operator overloading using magic methods. The class should overload __len__() to return the total number of elements, __str__()
# and __repr__() to display a custom string representation of the object, __add__() to concatenate the lists of two objects using the + operator,
# __sub__() to return the symmetric difference of two lists using set operations, __iadd__() to implement the += operator for extending the
# current object’s list, and __isub__() to implement the -= operator for updating the current object with the symmetric difference of both lists.
# Create two objects of the class and demonstrate all overloaded operators by displaying the results of addition, subtraction, +=, -=,
# object length, and object representation.

class Calculate:
    def __init__(self, numbers:list):
        self.numbers = numbers
    
    def __len__(self):
        return len(self.numbers)
    def __str__(self):
        return "THIS IS THE OBJECT OF CALCULATOR"
    def __repr__(self):
        return "THIS IS THE OBJECT OF CALCULATOR"
    
    def __add__(self, list2):
        sum = self.numbers.copy()
        sum.extend(list2.numbers)
        return sum
    def __sub__(Self, list2):
        list1 = set(Self.numbers)
        list2 = set(list2.numbers)
        return list1.union(list2) - list1.intersection(list2)
    
    def __iadd__(self, list2):
        self.numbers.extend(list2.numbers)
        return self
    def __isub__(self, list2):
        list1 = set(self.numbers)
        list2 = set(list2.numbers)
        self.numbers = list1.union(list2) - list1.intersection(list2)
        return self

cal1 = Calculate([1,2,3,4])
cal2 = Calculate([2,13,4,5])

sum = cal1 + cal2
print(sum)

minus = cal1 - cal2
print(minus)

cal1 += cal2
print(cal1.numbers)

cal1 -= cal2
print(cal1.numbers)
