# WRITE A FUNCTION TO FIND THE FACTORIAL OF A NUMBER "n".

def calc_fact(n):
    fact = 1
    for i in range(2,n+1):
        fact *= i
    print(n,"! =",fact)

calc_fact(5) 
