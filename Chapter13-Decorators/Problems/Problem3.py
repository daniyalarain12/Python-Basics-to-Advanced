# Write a Python program using OOP to implement an ATM System. Create a class named Account with two instance variables: title and balance.
# Add four methods named checkBalance(), viewTitle(), withdrawMoney(amount), and depositMoney(amount) to perform ATM operations. Also create
# decorators named greeting_decorator and confirmation_decorator where the greeting decorator displays a welcome message with the account
# holder’s name and the confirmation decorator asks the user for confirmation before performing any transaction. Additionally, create a
# logs_decorator that stores the function name along with the current date and time in a logs.txt file whenever a function is called. Apply
# all decorators to each ATM method and demonstrate the functionality by creating an account object and performing different transactions.

from datetime import datetime as dt

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance
    
    def greeting_decorator(func):
        def wrapper(*args,**kwargs):
            self = args[0]
            print(f"HELLO! {self.title}")
            func(*args,**kwargs)
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
    @ logs_decorator
    def checkBalance(self):
        print(f"YOUR CURRENT BALANCE IS : {self.balance}")
    
    @ greeting_decorator
    @ confirmation_decorator
    @ logs_decorator
    def viewTitle(self):
        print(f"YOUR ACCOUNT TITLE IS : {self.title}")
    
    @ greeting_decorator
    @ confirmation_decorator
    @ logs_decorator
    def withdrawMoney(self, amount):
        if (amount <= self.balance):
            self.balance -= amount
            print(f"RS. {amount} IS SUCCESSFULLY WITHDRAWN")
        else:
            print("INSUFFICIENT BALANCE")
    
    @ greeting_decorator
    @ confirmation_decorator
    @ logs_decorator
    def depositMoney(self, amount):
        self.balance += amount
        print(f"RS. {amount} IS SUCCESSFULLY DEPOSITED")

acc1 = Account("DANIYAL ARAIN",200000)
acc1.checkBalance()
acc1.viewTitle()
acc1.withdrawMoney(5000)
acc1.checkBalance()
acc1.depositMoney(10000)
acc1.checkBalance()
