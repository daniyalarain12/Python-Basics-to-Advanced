# CREATE A FUNCTION TO CALCULATE THE AREA OF A CIRCLE USING BUILT-IN METHODS OF THE PYTHON math MODULE.

import math

def area_of_circle(r):
    return math.pi * math.pow(r,2)

print("AREA OF CIRCLE :",area_of_circle(10))
