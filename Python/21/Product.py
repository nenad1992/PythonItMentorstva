# Product
# name, price, amount, type
# food, technology...



class Product:
    number_of_products = 0
    allowed_types = ['android', 'ios']
    number_of_types = {
        'android': 0,
        'ios': 0
    }

    def __init__(self, name, price, amount, type):

        if amount < 1:
            raise ValueError("Amount must be more than 0")

        if type not in Product.allowed_types:
            raise ValueError("You didn't pass the correct type")

        self.name = name
        self.price = price
        self.amount = amount
        self.type = type
        Product.number_of_products += 1
        # Povecava vrednosti u number_of_types u zavisnosti koji je tip OS-a
        Product.number_of_types[type] += amount

