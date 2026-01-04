# SEARCH FOR A NUMBER x IN THIS TUPLE USING LOOP: (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("ENTER THE TARGET : "))
idx = 0
for val in nums:
    if(val == x):
        print("TARGET FOUND AT INDEX :",idx)
        break
    idx += 1
