# MULTIPLE INHERITANCE ( PARENT --> CHILD <-- PARENT)

class A:
    varA = "WELCOME TO CLASS A"

class B:
    varB = "WELCOME TO CLASS B"

class C(A, B):
    varC = "WELCOME TO CLASS C"

c1 = C()
print(c1.varA)
print(c1.varB)
print(c1.varC)
