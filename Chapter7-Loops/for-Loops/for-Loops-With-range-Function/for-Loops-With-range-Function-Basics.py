# FOR LOOPS WITH range FUNCTION
# range FUNCTION RETURNS A SEQUENCE OF NUMBERS, STARTING FROM 0 BY DEFAULT, AND INCREMENTS BY 1 BY DEFAULT AND
# STOPS BEFORE A SPECIFIED NUMBER.

for i in range(10):             # range(stop)            start = 0, stop = 10, step = 1
    print(i)

for i in range(2,10):           # range(start,stop)      start = 2, stop = 10, step = 1
    print(i)

for i in range(2,10,2):         # range(start,stop,step) start = 2, stop = 10, step = 2
    print(i)
