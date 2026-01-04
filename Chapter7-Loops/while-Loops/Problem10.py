# WRITE A PROGRAM TO FIND THE FACTORIAL OF FIRST "n" NUMBERS USING WHILE LOOP.

n = int(input("ENTER ANY NUMBER : "))
factorial = 1
i = 2
while i<=n:
    factorial *= i
    i += 1
print(n,"! =",factorial)
