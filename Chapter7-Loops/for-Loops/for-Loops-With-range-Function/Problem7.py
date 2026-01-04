# WRITE A PROGRAM TO FIND THE FACTORIAL OF FIRST "n" NUMBERS USING FOR LOOP.

n = int(input("ENTER ANY NUMBER : "))
factorial = 1
for i in range(2,n+1):
    factorial *= i
print(n,"! =",factorial)
