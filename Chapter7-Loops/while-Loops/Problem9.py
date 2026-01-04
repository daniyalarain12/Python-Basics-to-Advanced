# WRITE A PROGRAM TO FIND THE SUM OF FIRST "n" NUMBERS USING WHILE LOOP.

n = int(input("ENTER ANY NUMBER : "))
sum = 0
i = 1
while i<=n:
    sum += i
    i += 1
print("SUM :",sum)
