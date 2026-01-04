# FOR LOOPS WITH else
# else CONDITION WILL EXECUTES ONLY WHEN FOR LOOP EXECUTES COMPLETELY.

nums = [1,2,3,4,5]
for val in nums:
    print(val)
else:
    print("END")    

name = "DANIYAL ARAIN"
for char in name:
    if(char == "Y"):
        print("Y IS FOUND")
        break
    print(char)
else:
    print("END")
