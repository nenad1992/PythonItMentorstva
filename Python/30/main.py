# 1. Dodaj korisnika
# Pomocu klasnog atributa
# 2. Prikazi korisnike
# 3. Prikazi raspoloziva vozila
# 4. Prikazi rentirana vozila

from models.Car import Car
from models.User import User

print("Opcije: "
      "\n1. Dodaj korisnika "
      "\n2. Prikazi korisnike "
      "\n3. Prikazi raspoloziva vozila "
      "\n4. Prikazi rentirana vozila")

available_options = [1, 2, 3, 4]

option = None

while option is None:

    option = int(input("Unesite opciju koju zelite: \n"))

    if option not in available_options:
        raise ValueError("Nepoznata opcija")

    if option == 1:
        user = User()
        user.name = input("Enter users name")
        user.age = int(input("Enter users age"))
        user.create()
        option = None

    elif option == 2:
        print(User.ALL_USERS)
        option = None

    elif option == 3 or option == 4:
        for brand in Car.VALID_CARS:
            for car in Car.VALID_CARS[brand]:
                if not car['rented'] and option == 3:
                    print(car)
                elif car['rented'] and option == 4:
                    print(car)