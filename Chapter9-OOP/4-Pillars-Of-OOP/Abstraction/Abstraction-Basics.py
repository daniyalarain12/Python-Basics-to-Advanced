# ABSTRACTION
# HIDING THE IMPLEMENTATION DETAILS OF A CLASS AND ONLY SHOWING THE ESSENTIAL FEATURES TO THE USER.

class Car:
    def __init__(self):
        self.clutch = False
        self.acc = False
        self.brk = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("CAR STARTED...")

c1 = Car()
c1.start()
