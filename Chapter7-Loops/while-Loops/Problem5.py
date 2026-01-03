# SEARCH FOR A NUMBER x IN THIS TUPLE USING LOOP: (1,4,9,16,25,36,49,64,81,100)

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("ENTER THE TARGET : "))
i = 0
while i < len(nums):
    if(nums[i]==x):
        print("TARGET FOUND AT INDEX :",i)
    i += 1
