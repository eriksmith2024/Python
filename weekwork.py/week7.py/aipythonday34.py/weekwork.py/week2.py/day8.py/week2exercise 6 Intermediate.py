#Exercise 6 Intermediate Below is as far as I got

class Product:
    def __init__(self, name, price) -> None:
        self.name = name
        self.price = price

    def discount(self):
        self.price -= (self.price * self.discount)

item = Product

        
    
# Creste a class called product with attributes name and price and a method to apply a discount

#Hint: self.price -= (self.price * discount)

# Create an object of the product class, set the price to 10, apply a 20% discount, and the final price

# How can you midfy the code to ensure that the discount value is between 0 & 1?

#Skills City colleague code Efosa
# class Product():
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def __str__(self):
#         return f'Product: {self.name} | Price: £{self.price}'

#     def discount(self, percentage):
#         self.price -= self.price * percentage / 100
#         return f'Discounted price: £{self.price}'

#     def discount_percentage(self, value):
#         percentage = value / 100
#         return f'Discount value is: {value} OR {value *100}%'
    
# item = Product('Phone', 75.50)

# print (item)

# print(item.dicount(20))
# print('------Discount Value -------')
# print(item.discountvalue(20))

# Corrected by Chat GPT

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'Product: {self.name} | Price: £{self.price}'

    def discount(self, percentage):
        self.price -= self.price * percentage / 100
        return f'Discounted price: £{self.price}'

    def discount_percentage(self, value):
        percentage = value / 100
        return f'Discount value is: {percentage} OR {value}%'
    
item = Product('Phone', 75.50)

print(item)

print(item.discount(20))
print('------Discount Value -------')
print(item.discount_percentage(20))


#Aiden Option

class Product:
    def __init__(self, name, price):
        self.name = name  # corrected from price to name
        self.price = price
        self.discount = self.price * 0.80
        self.dt = self.price * 0.20
    
    def get_price(self):
        print(self.price)

    def get_discount(self):  # fixed method name
        print(self.dt, "Discount applied")

# Instantiate the product class
banana = Product('banana', 2.00)

# Call the methods
banana.get_price()
banana.get_discount()











