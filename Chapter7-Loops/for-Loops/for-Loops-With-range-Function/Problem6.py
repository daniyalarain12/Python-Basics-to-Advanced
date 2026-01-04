# WRITE A PROGRAM TO FIND THE SUM OF FIRST "n" NUMBER USING FOR LOOP.

n = int(input("ENTER ANY NUMBER : "))
sum = 0
for i in range(1,n+1):
    sum += i
print("SUM :",sum)
