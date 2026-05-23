# Write a Python program using OOP to create a Vehicle class that models the basic working of a vehicle. The class should contain attributes
# such as wheels, doors, spark, gear, air valve, and fuel injection. Implement methods for ignition, starting the vehicle, changing gears,
# and braking. Create an object of the class, start the vehicle, shift the gear, and stop the vehicle by applying brakes. The program should
# display appropriate messages for each operation to demonstrate the concept of abstraction in OOP.

class Vehicle:
    def __init__(self):
        self.wheels = 4
        self.doors = 2
        self.spark = False
        self.gear = 0
        self.airValue = 0
        self.fuleInjection = False

    def ignition(self):
        self.airValue = True
        self.fuelIgnition = True
        self.spark = True
    def start(self):
        self.ignition()
        print("Vehicle started successfully.")
    def setGear(self, gear:int):
        self.gear = gear
        print(f"Gear shifted to {gear}.")
    def brk(self, gear:int):
        self.setGear(gear)
        print("Vehicle stopped safely.")

vehicle1 = Vehicle()
vehicle1.start()
vehicle1.setGear(4)
vehicle1.brk(1)
