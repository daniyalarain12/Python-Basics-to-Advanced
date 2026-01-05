# WRITE A RECURSIVE FUNCTION TO PRINT THE SUM OF 1ST "n" NATURAL NUMBERS.

def calc_sum(n):
    if(n==0):
        return 0
    else:
        return n + calc_sum(n-1)
    
print("SUM :",calc_sum(10))
