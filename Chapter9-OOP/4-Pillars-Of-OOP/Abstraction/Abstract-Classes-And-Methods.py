# ABSTRACT CLASSES
# An abstract class in Python is a class that cannot be instantiated directly and is meant to serve as a blueprint for other classes. It defines
# a common structure for its subclasses by combining both concrete methods (with implementation) and abstract methods (without implementation).
# Abstract classes are created using the ABC class from the abc module, and they are mainly used to enforce a consistent interface across multiple
# related classes, ensuring that all subclasses follow the same design while allowing them to implement their own specific behavior.

# ABSTRACT METHODS
# An abstract method is a method declared inside an abstract class that does not contain any implementation and must be overridden in all subclasses.
# It is defined using the @abstractmethod decorator from the abc module and acts as a mandatory contract that forces child classes to provide their
# own specific implementation. If a subclass does not implement all abstract methods, it cannot be instantiated, which helps maintain structure,
# consistency, and reliability in object-oriented design.

from abc import ABC, abstractmethod            # abc module is used to create Abstract Base Classes in Python

class Animal(ABC):                             # Abstract class Animal inherits from ABC
    @abstractmethod                            # Must be implemented by all subclasses
    def sound(self):
        pass

class Lion(Animal):
    def sound(self):
        print("ROAR")

class Cat(Animal):
    def sound(self):
        print("MEOW")

lion = Lion()
lion.sound()

cat = Cat()
cat.sound()
