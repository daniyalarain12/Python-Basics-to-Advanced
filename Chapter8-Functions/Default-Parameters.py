# DEFAULT PARAMETERS
# ASSIGNING A DEFAULT VALUE TO PARAMETERS, WHICH IS USED WHEN NO ARGUMENT IS PASSED.

def calc_prod1(a,b):
    prod = a*b
    return prod

print("PRODUCT :",calc_prod1(1,2))

def calc_prod2(a=2,b=3):
    prod = a*b
    return prod

print("PRODUCT :",calc_prod2(1,2))

def calc_prod3(a=2,b=3):
    prod = a*b
    return prod

print("PRODUCT :",calc_prod3())

def calc_prod4(a,b=3):
    prod = a*b
    return prod

print("PRODUCT :",calc_prod4(1))
