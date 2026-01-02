# SET METHODS

collection = set()                              # EMPTY SET

collection.add(1)                               # ADDS AN ELEMENT
collection.add(2)
collection.add(2)
collection.add(3)
collection.add(4)
print(collection)

collection.remove(1)                            # REMOVES THE ELEMENT
print(collection)

print("DELETED ELEMENT :",collection.pop())     # REMOVES A RANDOM VALUE
print(collection)

collection.clear()                              # EMPTIES THE SET
print(collection)

set1 = {1,2,3}
set2 = {2,3,4}
print("UNION :",set1.union(set2))                # COMBINES BOTH SET VALUES AND RETURNS NEW

print("INTERSECTION :",set1.intersection(set2))  # COMBINES COMMON VALUES AND RETURNS NEW
