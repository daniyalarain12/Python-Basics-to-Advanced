"""
Exception Handling: 

Exception: Problems that occur at runtime and can be managed using exception handling.

We have 2 clauses in Exception Handling:
1. try: Runs the risky code that might cause an error.
2. except: Catches and handles the error if error occurs.
"""

list = [10,20,30,40,50]
n = int(input("ENTER ANY NUMBER : "))
try:
    print(f"ELEMENT AT INDEX {n} IS :",list[n])
except Exception as e:
    print(e)
