
# INHERITANCE
# WHEN ONE class (CHILD/DERIVED) DERIVES THE PROPERTIES AND METHODS OF ANOTHER class (PARENT/BASE).

# SINGLE-LEVEL INHERITANCE  (PARENT ---> CHILD)

class Car:
    color = "black"
    @staticmethod
    def start():
        print("CAR STARTED..")
    @staticmethod
    def stop():
        print("CAR STOPPED..")

class ToyotaCar(Car):
    def __init__(self, name):
        self.name = name

car1 = ToyotaCar("FORTUNER")
print(car1.name)
print(car1.color)
car1.start()
car1.stop()
