class Products:
    def __init__(self , name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def display_products(self):
        print("display products")
        print(self.name)
        print(self.price)
        print(self.quantity)


p1 = Products("soap", 45 ,50)
# print(p1.name)
# print(p1.price)
# print(p1.quantity)
p1.display_products()
