"""
Exception Handling: 

Exception: Problems that occur at runtime and can be managed using exception handling.

We have 4 clauses in Exception Handling:
1. try: Runs the risky code that might cause an error.
2. except: Catches and handles the error if error occurs.
3. else: Executes only if no exception occurs in the try block.
4. finally: Executes whether an exception occurs or not.
"""

list = [10,20,30,40,50]
n = int(input("ENTER ANY NUMBER : "))
try:
    print(f"ELEMENT AT INDEX {n} IS :",list[n])
except Exception as e:
    print(e)

try:
    num = int(input("ENTER ANY NUMBER : "))
    value = 10/num
except ZeroDivisionError:
    print("DIVIDE BY 0 IS NOT ALLOWED")
except ValueError:
    print("INVALID INPUT")
else:
    print(f"VALUE : {value}")
finally:
    print("END OF PROGRAM")
