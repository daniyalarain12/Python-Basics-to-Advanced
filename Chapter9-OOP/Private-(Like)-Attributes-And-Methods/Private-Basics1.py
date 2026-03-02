# PRIVATE (LIKE) ATTRIBUTES AND METHODS
# CONCEPTUAL IMPLEMENTATION IN PYTHON

# PRIVATE ATTRIBUTES AND METHODS ARE MEANT TO BE USED ONLY WITHIN THE class AND ARE NOT ACCESSIBLE FROM OUTSIDE THE class.
# IN PYTHON, WE USE DOUBLE UNDERSCORES (__) BEFORE AN ATTRIBUTE OR METHOD NAME TO MAKE IT PRIVATE.

class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

    def get_pass(self):
        print(self.__acc_pass)

acc1 = Account("24SW039","dani786")
print(acc1.acc_no)

# print(acc1.__acc_pass)              # CAN NOT ACCESS

acc1.get_pass()
print(acc1.acc_no)

# print(acc1.__acc_pass)              # CAN NOT ACCESS

acc1.get_pass()
