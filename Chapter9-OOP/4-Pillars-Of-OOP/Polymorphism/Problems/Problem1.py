# CREATE A class CALLED Order WHICH STORES ITEM AND IT'S PRICE.
# USE DUNDER FUNCTION __gt__() TO CONVEY THAT: ORDER1 > ORDER2 IF PRICE OF ORDER1 > PRICE OF ORDER2

class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price
    def __gt__(self, order2):
        return self.price > order2.price
    
order1 = Order("CHIPS",20)
order2 = Order("TEA",15)
print(order1 > order2)
