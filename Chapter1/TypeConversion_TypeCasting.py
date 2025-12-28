#TYPE CONVERSION (IMPLICIT)
a , b = 2 , 6.25
sum = a + b         # sum = 2.0 + 6.25
print("SUM :",sum)

#TYPE CASTING (EXPLICIT)
a , b , c = 2 , int("3") , 5
c = str(c)
sum = a + b
print(type(b))
print(type(c))
print("SUM :",sum)
print("c :",c)
