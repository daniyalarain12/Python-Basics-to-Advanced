# CREATE A FUNCTION TO CALCULATE THE DISTANCE BETWEEN TWO POINTS USING BUILT-IN METHODS OF THE PYTHON math MODULE.

import math

def distance(p1:tuple,p2:tuple):
    return math.sqrt(math.pow((p2[0]-p1[0]),2) + math.pow((p2[1]-p1[1]),2))

print(distance((3,4),(8,5)))
