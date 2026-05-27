# DESIGN AND CREATE AN ONLINE STORE FOR PRODUCTS (name, price). TRACK TOTAL PRODUCTS BEING CREATED.
# CREATE A static METHOD TO CALCULATE DISCOUNT ON EACH PRODUCT BASED ON A % PARAMETER.

class Product:
    count = 0
    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1
    
    @ classmethod
    def get_count(cls):
        print(f"TOTAL PRODUCTS IN STORE = {cls.count}")
    
    def get_info(self):
        print(f"PRICE OF {self.name} IS RS. {self.price}")

    @ staticmethod
    def cal_discount(price, discount):
        print(f"DISCOUNTED PRICE = {price - (price * discount) / 100 }")

p1 = Product("LAPTOP",200_000)
p2 = Product("SMARTPHONE",400_00)
p3 = Product("REFRIGERATOR",120_000)

p1.get_info()
p2.get_info()
p3.get_info()

Product.get_count()

p1.cal_discount(p1.price, 10)
