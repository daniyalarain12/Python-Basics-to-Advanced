"""
Exception Handling: Exception means an error.
We had 2 clauses in Exception Handling:
1. try: we provide the code to try if there is an error.
2. except: except clause will only be executed when there is an error in try clause.
"""

list = [10,20,30,40,50]
n = int(input("ENTER ANY NUMBER : "))
try:
    print(f"ELEMENT AT INDEX {n} IS :",list[n])
except Exception as e:
    print(e)
