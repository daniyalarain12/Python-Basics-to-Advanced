# CREATE A LIST OF SQUARES OF ONLY ODD NUMBERS FROM 1 TO 5 USING LIST COMPREHENSION.

list = [i*i for i in range(1,6) if i%2 != 0]
print(list)
