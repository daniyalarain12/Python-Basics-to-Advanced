# Write a Python program using OOP to implement a Smart Shopping Cart system where a Cart class stores items (each item contains name, price, and
# quantity). The program must demonstrate operator overloading by using += to add items to the cart, -= to remove items from the cart if they
# exist, and __str__() to display a formatted receipt. The receipt should show each item’s number, name, price, quantity, subtotal, along with
# the total number of items and the final bill. The total bill must automatically update whenever items are added or removed.

class Cart:
    def __init__(self):
        self.items = []
        self.totalBill = 0
        self.totalItems = 0
    
    def __iadd__(self, other):
        self.items.append(other)
        self.totalBill += other["price"] * other["qty"]
        self.totalItems += 1
        return self
    def __isub__(self, other):
        if (other in self.items):
            self.items.remove(other)
            self.totalBill -= other["price"] * other["qty"]
            self.totalItems -= 1
        return self
    def __str__(self):
        receipt = ""
        for index, item in enumerate(self.items):
            receipt += f"ITEM NO. {index+1}\n"
            receipt += f"ITEM NAME : {item["name"]}\n"
            receipt += f"ITEM PRICE : {item["price"]}\n"
            receipt += f"ITEM QUANTITY : {item["qty"]}\n"
            receipt += f"SUB TOTAL : {item["price"] * item["qty"]}\n"
            receipt += "*" * 20 + "\n"
        receipt += f"TOTAL NO. OF ITEMS : {self.totalItems}\n"
        receipt += f"TOTAL BILL : {self.totalBill}"
        return receipt

cart1 = Cart()
cart1 += {
    "name" : "COMPUTER",
    "price" : 15000,
    "qty" : 10
}
cart1 += {
    "name" : "SMARTPHONE",
    "price" : 17000,
    "qty" : 5
}
cart1 -= {
    "name" : "COMPUTER",
    "price" : 15000,
    "qty" : 10
}

print(cart1)
