# Create a Python ATM Management System using a dictionary and Exception Handling that asks the user to enter a PIN code and, 
# if the PIN is correct, repeatedly displays a menu to check balance, withdraw money in multiples of 500 with sufficient balance 
# validation, deposit money, and exit the program while handling invalid inputs and displaying appropriate messages for each operation.

user = {
    "name" : "Daniyal",
    "balance" : 10000,
    "pinCode" : 1234
}

try:
    pin = int(input("ENTER USER PIN CODE : "))
    if (user["pinCode"] == pin):
        while True:
            print("*"*20)
            try:
                selection = int(input("MENU :\n1. CHECK BALANCE\n2. WITHDRAW MONEY\n3. DEPOSIT MONEY\n0. EXIT\nENTER YOUR SELECTION : "))
            except:
                print("PLEASE SELECT A VALID OPTION FROM THE MENU.")
                continue
            if (selection == 1):
                print("YOUR CURRENT BALANCE IS :",user["balance"])
            elif (selection == 2):
                try:
                    money = int(input("ENTER AMOUNT IN MULTIPLES OF 500 : "))
                    if (money%500 == 0 and money >= 500):
                        if (money <= user["balance"]):
                            print(f"RS. {money} HAS BEEN SUCCESSFULLY WITHDRAWN.")
                            user["balance"] -= money
                            print("YOUR UPDATED BALANCE IS :",user["balance"])
                        else:
                            print("INSUFFICIENT BALANCE.")
                    else:
                        print("PLEASE ENTER AN AMOUNT IN MULTIPLES OF 500.")
                except:
                    print("INVALID AMOUNT. PLEASE ENTER NUMBERS ONLY.")
            elif (selection == 3):
                try:
                    money = int(input("ENTER AMOUNT TO DEPOSIT : "))
                    print(f"RS. {money} HAS BEEN SUCCESSFULLY DEPOSITED.")
                    user["balance"] += money
                    print("YOUR UPDATED BALANCE IS :",user["balance"])
                except:
                    print("INVALID AMOUNT. PLEASE ENTER NUMBERS ONLY.")
            elif (selection == 0):
                print("THANK YOU FOR USING OUR ATM SERVICE.")
                break
            else:
                print("INVALID INPUT. PLEASE ENTER A VALID MENU OPTION.")
    else:
        print("INCORRECT PIN CODE.")
except:
    print("INVALID PIN CODE. PLEASE ENTER NUMBERS ONLY.")
