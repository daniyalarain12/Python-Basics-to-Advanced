# collections MODULE
# Used to create specialized container data types in Python like deque and Counter. It helps in storing and managing data efficiently.

import collections as col

# Creating a deque and adding elements from both sides
myqueue = col.deque([3,6])
myqueue.append(7)                 # Adding element at the right side
myqueue.appendleft(1)             # Adding element at the left side
print(myqueue)

myqueue = col.deque([3,6],maxlen=3)        # Creating a deque with maximum size 3
myqueue.append(7)                          # Adding element to deque
print(myqueue)
myqueue.append(8)                          # Oldest element is removed automatically
print(myqueue)

# Counting frequency of elements in a list
myCounterList = col.Counter(["hen","bread","chicken","hen"])
print(myCounterList["hen"])

# Creating Counter using dictionary data
myCounterList = col.Counter({"cat":2, "dog":3})
print(myCounterList["dog"])
print(myCounterList["hen"])                      # Returns 0 because "hen" does not exist

# Counting frequency of characters in a string
myCounterList = col.Counter("DANIYAL")
print(myCounterList["A"])
print(myCounterList["Z"])                        # Returns 0 because "Z" does not exist
