# REPLACE ALL NEGATIVE NUMBERS IN A LIST WITH 0 USING LIST COMPREHENSION.

nums = [-1,-4,3,5,2,-1]

nums = [value if value >= 0 else 0 for value in nums]
print(nums)
