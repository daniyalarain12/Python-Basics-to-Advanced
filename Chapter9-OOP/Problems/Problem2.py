# DEFINE A CIRCLE class TO DEFINE A CIRCLE WITH RADIUS r USING THE CONSTRUCTOR.
# DEFINE AN Area() METHOD OF THE class WHICH CALCULATES THE AREA OF THE CIRCLE.
# DEFINE A Perimeter() METHOD OF THE class WHICH ALLOWS YOU TO CALCULATE THE PERIMETER OF THE CIRCLE.

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return (22/7) * self.r ** 2
    def perimeter(self):
        return (2 * (22/7) * self.r)

circle1 = Circle(21)
print(circle1.area())
print(circle1.perimeter())
