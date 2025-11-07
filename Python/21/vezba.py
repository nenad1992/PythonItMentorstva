from Product import Product
from ShoppingCart import ShoppingCart

iPhone16 = Product("iPhone 16 pro max", 1500, 3, "ios")
samsungS23Pro = Product("Samsung S23 Pro", 1200, 200, "android")
samsungA55 = Product("Samsung A55", 500, 5, "android")

phoneCart = ShoppingCart()
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)

phoneCart.show_products()
print(Product.number_of_types)