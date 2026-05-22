# CREATE AN ACCOUNT class WITH 2 ATTRIBUTES - BALANCE AND ACCOUNT NO. CREATE METHODS FOR DEBIT, CREDIT AND PRINTING THE BALANCE.

class Account:
    def __init__(self, account, balance):
        self.account = account
        self.balance = balance

    def get_balance(self):
        print("YOUR CURRENT BALANCE IS :",self.balance)
    
    def debit(self, amount):
        self.balance -= amount
        print("RS",amount,"IS DEBITED")
        self.get_balance()

    def credit(self, amount):
        self.balance += amount
        print("RS",amount,"IS CREDITED")
        self.get_balance()

account1 = Account("24SW039",5000)
account1.get_balance()
account1.debit(3000)
account1.credit(2000)
