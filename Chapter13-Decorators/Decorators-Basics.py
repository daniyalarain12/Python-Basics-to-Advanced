# DECORATOR
# A decorator is a function that takes another function as an argument and returns a new function with enhanced functionality.

def greeting_decorator(func):
    def wrapper(*args,**kwargs):
        print("HELLO! WELCOME TO SMIT.")
        func(*args,**kwargs)
        print("GOODBYE! THANK YOU FOR VISITING SMIT.")
    return wrapper

@ greeting_decorator
def displayMessage():
        print("THIS IS DANIYAL ARAIN.")

displayMessage()
