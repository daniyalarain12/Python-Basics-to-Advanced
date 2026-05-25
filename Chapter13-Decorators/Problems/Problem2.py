# Write a Python program to demonstrate the use of multiple decorators. Create a greeting_decorator that displays a welcome message before
# function execution and a goodbye message after execution, a confirmation_decorator that asks the user to confirm before running the function,
# and a logs_decorator that stores the function name along with the current date and time in a logs.txt file whenever the function is called.
# Then create a function named displayMessage() that prints "THIS IS DANIYAL ARAIN", apply all three decorators to it, and call the function.
# Use *args and **kwargs inside all wrapper functions.

from datetime import datetime as dt

def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("HELLO! WELCOME TO SMIT.")
        func(*args,**kwargs)
        print("GOODBYE! THANK YOU FOR VISITING SMIT.")
    return wrapper

def confirmation_decorator(func):
    def wrapper(*args,**kwargs):
        user_input = input("ENTER y TO CONFIRM YOUR TRANSACTION : ")
        if (user_input.lower() == "y"):
             func(*args,**kwargs)
    return wrapper

def logs_decorator(func):
    def wrapper(*args,**kwargs):
        with open("logs.txt","a") as f:
             f.write(f"{dt.now()} :: {func.__name__} FUNCTION IS CALLED\n")
        func(*args,**kwargs)
    return wrapper

@ greeting_decorator
@ confirmation_decorator
@logs_decorator
def displayMessage():
        print("THIS IS DANIYAL ARAIN.")

displayMessage()
