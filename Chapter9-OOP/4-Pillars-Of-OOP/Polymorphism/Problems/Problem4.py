# Write a Python program using OOP concepts to implement a Smart Shopping Cart System. Create an Item class to store item details such as
# name, price, and quantity, and a Cart class to manage cart operations. The program must demonstrate operator overloading by using __iadd__()
# to add items into the cart with the += operator, __isub__() to remove a specific quantity of an item using the -= operator, and __str__() to
# display a formatted receipt showing item number, item name, price, quantity, subtotal, total number of items, and total bill. The cart should
# automatically update the bill when items are added or removed, and remove an item completely if its quantity becomes zero. Finally, create
# multiple items, add them to the cart, remove some quantity from an item, and display the updated cart receipt.

class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Cart:
    def __init__(self):
        self.items = []
        self.totalBill = 0
        self.totalItems = 0
    
    def __iadd__(self, other):
        self.items.append(other)
        self.totalBill += other.price * other.qty
        self.totalItems += 1
        return self
    def __isub__(self, other:tuple):
        index = other[0] -1
        qty = other[1]

        if (index>=0 and index<len(self.items)):
            re_item = self.items[index]

            if (re_item.qty == qty):
                self.totalBill -= re_item.price * re_item.qty
                self.items.pop(index)
                self.totalItems -= 1
            else:
                re_item.qty -= qty
                self.totalBill -= re_item.price * qty
                self.items[index] = re_item
            
        return self

    def __str__(self):
        receipt = ""
        for index, item in enumerate(self.items):
            receipt += f"ITEM NO. {index+1}\n"
            receipt += f"ITEM NAME : {item.name}\n"
            receipt += f"ITEM PRICE : {item.price}\n"
            receipt += f"ITEM QUANTITY : {item.qty}\n"
            receipt += f"SUB TOTAL : {item.price * item.qty}\n"
            receipt += "*" * 20 + "\n"
        receipt += f"TOTAL NO. OF ITEMS : {self.totalItems}\n"
        receipt += f"TOTAL BILL : {self.totalBill}"
        return receipt

item1 = Item("COMPUTER",15000,10)
item2 = Item("SMARTPHONE",17000,5)

cart1 = Cart()
cart1 += item1
cart1 += item2
print(cart1)

cart1 -= (1,2)
print(cart1)
