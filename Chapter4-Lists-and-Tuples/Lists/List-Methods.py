#METHODS OF LISTS

#append METHOD
marks = [98,97,88,67,89]
marks.append(90)            # Adds one element at the end.
print(marks)

#sort METHOD (SORTING IN ASCENDING ORDER)
marks = [98,97,88,67,89]
marks.sort()                 # Sorts the list in ascending order.
print(marks)

fruits = ["apple","orange","banana"]
fruits.sort()                # Sorts the list in ascending order.
print(fruits)

#sort METHOD (SORTING IN DESCENDING ORDER)
marks = [98,97,88,67,89]
marks.sort(reverse=True)     # Sorts the list in descending order.
print(marks)

fruits = ["apple","orange","banana"]
fruits.sort(reverse=True)    # Sorts the list in descending order.
print(fruits)

#reverse METHOD
marks = [98,97,88,67,89]
marks.reverse()              # Reverses the list.
print(marks)

#insert METHOD
marks = [98,97,88,67,89]
marks.insert(2,100)          # Insert the element at specific index.
print(marks)

#remove METHOD
marks = [98,97,88,67,89,67]
marks.remove(67)             # DELETE 1ST OCCURRENCE OF AN ELEMENT.
print(marks)

#pop METHOD
marks = [98,97,88,67,89,67]
marks.pop(2)                 # DELETE ELEMENT AT PARTICULAR INDEX.
print(marks)

#copy METHOD
marks1 = [98,97,88,67,89,67]
marks2 = marks1.copy()       # Creates a copy of the list.
print(marks1)
print(marks2)
