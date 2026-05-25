# Create a Python program to demonstrate the use of decorators by creating a greeting_decorator that prints a welcome message before a function
# call and a goodbye message after execution, and a confirmation_decorator that asks the user for confirmation before running the function.
# Then create a function named displayMessage() that prints "THIS IS DANIYAL ARAIN", apply both decorators to it, and call the function.
# Use *args and **kwargs inside the wrapper functions, and ensure the decorated function only executes when the user enters "y" for confirmation.

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

@ greeting_decorator
@ confirmation_decorator
def displayMessage():
        print("THIS IS DANIYAL ARAIN.")

displayMessage()
