# queue MODULE
# Used to create FIFO and LIFO queues in Python. It helps in storing and managing data in a specific order.

import queue

myStack = queue.LifoQueue(maxsize=5) # Creating a stack using LifoQueue with maximum size 5
print(myStack.full())                # Checking whether the stack is full or not

# Adding elements into the stack
myStack.put(1)
myStack.put(2)
myStack.put(3)
myStack.put(4)
myStack.put(5)

print(myStack.full())                # Checking again if the stack is full
print(myStack.get())                 # Removing the top element from the stack
print(myStack.full())                # Checking stack status after removing one element
