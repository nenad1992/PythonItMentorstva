from Product import Product
from ShoppingCart import ShoppingCart

iPhone16 = Product()
samsungS23Pro = Product()
samsungA55 = Product()

iPhone16.create("iPhone 16 pro", 1500, 3, "ios")
#iPhone16.check_if_user_exists("iPhone 16 pro max")
iPhone16.increment_number_of_products_for_type("ios", 5)

samsungS23Pro.create("Samsung S23 Pro", 1200, 200, "android")
samsungS23Pro.increment_number_of_products_for_type("android", 200)

samsungA55.create("Samsung A55", 500, 5, "android")
samsungA55.increment_number_of_products_for_type("android", 5)

phoneCart = ShoppingCart()
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)
phoneCart.add_product(iPhone16)

phoneCart.show_products()
print(Product.number_of_types)