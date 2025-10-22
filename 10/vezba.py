# Napraviti folder "data" unutar koga cemo imati "user.json" i "products.json"
# Napraviti 5 proizvoda unutar products.json i ucitati ih u vezba.py
# load_file -> file_name

from methods import load_file

products = load_file("data/products.json")
users = load_file("data/users.json")
print(products)