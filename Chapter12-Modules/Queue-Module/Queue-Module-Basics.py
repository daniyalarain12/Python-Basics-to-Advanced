# queue MODULE
# Used to create FIFO and LIFO queues in Python. It helps in storing and managing data in a specific order.

import queue

stack = queue.LifoQueue(maxsize=5)    # Creating a stack using LifoQueue with maximum size 5
print(stack.full())                   # Checking whether the stack is full or not

# Adding elements into the stack
stack.put(1)
stack.put(2)
stack.put(3)
stack.put(4)
stack.put(5)

print(stack.full())                   # Checking again if the stack is full
print(stack.get())                    # Removing the top element from the stack
print(stack.full())                   # Checking stack status after removing one element
