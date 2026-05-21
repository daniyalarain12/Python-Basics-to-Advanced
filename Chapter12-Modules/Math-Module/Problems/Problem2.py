# CREATE A FUNCTION TO CHECK WHETHER A NUMBER IS A PERFECT SQUARE ROOT OR NOT USING BUILT-IN METHODS OF THE PYTHON math MODULE.

import math

def check_sqrt(value:int):
    return math.sqrt(value) == math.isqrt(value)

print(check_sqrt(25))
