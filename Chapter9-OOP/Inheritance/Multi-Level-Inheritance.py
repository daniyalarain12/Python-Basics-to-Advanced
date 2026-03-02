# MULTI-LEVEL INHERITANCE (GRAND-PARENT --> PARENT --> CHILD)

class Car:
    @staticmethod
    def start():
        print("CAR STARTED..")
    @staticmethod
    def stop():
        print("CAR STOPPED..")

class ToyotaCar(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("DIESEL")
car1.start()
car1.stop()
