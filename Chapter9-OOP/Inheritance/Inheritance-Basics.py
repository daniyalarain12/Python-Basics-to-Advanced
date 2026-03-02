# INHERITANCE
# WHEN ONE class (CHILD/DERIVED) DERIVES THE PROPERTIES AND METHODS OF ANOTHER class (PARENT/BASE).

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

c1 = ToyotaCar("FORTUNER")
print(c1.name)
print(c1.color)
c1.start()
c1.stop()
