# RECURSION
# WHEN A FUNCTION CALLS ITSELF REPEATEDLY.

def show(n):
    if(n == 0):             # BASE CASE
        return
    print(n)
    show(n-1)
    print("END",n)

show(5)
