# super() METHOD
# USED TO ACCESS THE METHODS OF THE PARENT class.

class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("CAR STARTED..")
    @staticmethod
    def stop():
        print("CAR STOPPED..")

class ToyotaCar(Car):
    def __init__(self, name, type):
        self.name = name
        super().__init__(type)
        super().start()

car1 = ToyotaCar("FORTUNER","ELECTRIC")
print(car1.name)
print(car1.type)
