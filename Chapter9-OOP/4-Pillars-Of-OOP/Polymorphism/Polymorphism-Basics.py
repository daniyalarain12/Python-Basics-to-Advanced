# POLYMORPHISM
# OPERATOR OVERLOADING
# WHEN THE SAME OPERATOR IS ALLOWED TO HAVE DIFFERENT MEANINGS ACCORDING TO THE CONTEXT.

#OPERATORS AND DUNDER FUNCTIONS
# a + b  ---> ADDITION         --->    a.__add__(b)
# a - b  ---> SUBTRACTION      --->    a.__sub__(b)
# a * b  ---> MULTIPLICATION   --->    a.__mul__(b)
# a / b  ---> DIVISION         --->    a.__truediv__(b)
# a % b  ---> MODULUS          --->    a.__mod__(b)

class Complex:
    def __init__(self, real, img):
        self.real = real
        self.img = img
      
    def showNumber(self):
        print(self.real,"i +",self.img,"j")

    def __add__(self, num):
        newReal = self.real + num.real
        newImg = self.img + num.img
        return Complex(newReal, newImg)
    def __sub__(self, num):
        newReal = self.real - num.real
        newImg = self.img - num.img
        return Complex(newReal, newImg)

num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

sum = num1 + num2
sum.showNumber()

minus = num1 - num2
minus.showNumber()
