# Product
# name, price, amount, type
# food, technology...

from Db import Db

# parent - Glavna klasa (Product)
# child - Klasa koju ucitavamo / nasledjujemo (Child)

class Product(Db):
    number_of_products = 0
    allowed_types = ['android', 'ios']
    number_of_types = {
        'android': 0,
        'ios': 0
    }

    def __init__(self):
        super().__init__()

    def create(self, name, price, amount, type):
        if amount < 1:
            raise ValueError("Amount must be more than 0")

        if type not in Product.allowed_types:
            raise ValueError("You didn't pass the correct type")

        if self.check_if_user_exists(name) is not None:
            raise ValueError("Product with this name already exists")

        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1

        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO products (name, price, amount, type) VALUES (%s, %s, %s, %s)", (
            name, price, amount, type
        ))
        self.connection.commit()
        cursor.close()

    def increment_number_of_products_for_type(self, type, amount):
        # Povecava vrednosti u number_of_types u zavisnosti koji je tip OS-a
        Product.number_of_types[type] += amount

        # Domaci
    def check_if_user_exists(self, name):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM products WHERE name = %s", (name))
        self.connection.commit()
        result = cursor.fetchone()
        cursor.close()
        return result