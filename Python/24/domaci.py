# Prebaciti svu logiku da koristi MySQL
# Dodati rentiranje automobila (do kada)
# Prilikom ispisivanja rentiranih vozila, ispisati pored do kada je rentiran (npr. jos 5 dana)
    # Ako je manje od 1 dana, ispisati u satima npr jos 10 sati

from models.Car import Car
from models.User import User
from models.Db import Db
from datetime import datetime

print("Opcije: "
      "\n1. Dodaj korisnika "
      "\n2. Prikazi korisnike "
      "\n3. Prikazi raspoloziva vozila "
      "\n4. Prikazi rentirana vozila"
      "\n5. Odaberi id vozila i unesi do kada je rentirano")

available_options = [1, 2, 3, 4, 5]

option = None

while option is None:

    option = int(input("Unesite opciju koju zelite: \n"))

    if option not in available_options:
        raise ValueError("Nepoznata opcija")

    if option == 1:
        conn = Db()
        cursor = conn._get_cursor()
        user = User()
        user.name = input("Enter users name")
        user.age = int(input("Enter users age"))
        user.create()
        print(User.ALL_USERS)
        query = "INSERT INTO users (name, age) VALUES (%s, %s)"
        cursor.execute(query, User.ALL_USERS[0])
        conn.commit()
        cursor.close()
        conn.close()
        option = None

    elif option == 2:
        conn = Db()
        cursor = conn._get_cursor()
        cursor.execute("SELECT * FROM users")
        print(cursor.fetchall())
        #print(User.ALL_USERS)
        option = None

    elif option == 3:
        conn = Db()
        cursor = conn._get_cursor()
        cursor.execute("SELECT * FROM cars WHERE rented = 0")
        print(cursor.fetchall())
        cursor.close()
        conn.close()
        option = None

    elif option == 4:
        conn = Db()
        cursor = conn._get_cursor()
        cursor.execute("SELECT * FROM cars WHERE rented = 1")
        fetched_rented = cursor.fetchall()
        for i in fetched_rented:
            delta = i[5] - datetime.now()
            days = delta.days
            seconds = delta.seconds
            hours = seconds // 3600
            minutes = (seconds % 3600) // 60
            print(i + ("Preostalo vreme: " + str(days) + "d " + str(hours) + "h " + str(minutes) + "m",))
        cursor.close()
        conn.close()
        option = None

    elif option == 5:
        conn = Db()
        cursor = conn._get_cursor()
        cursor.execute("SELECT * FROM cars WHERE rented = 0")
        print(cursor.fetchall())

        # Validacija za ID
        while True:
            try:
                car_id = int(input("Odaberite id vozila "))
                #print(car_id)
                cursor.execute("SELECT COUNT(*) FROM cars WHERE id = %s AND rented = %s", (car_id, 0))
                exists = cursor.fetchone()[0]
                #print(exists)
                if exists == 0:
                    print("ID ne postoji. Pokusajte ponovo: ")
                else:
                    break
            except ValueError:
                print("Morate uneti ceo broj!")

        # Validacija datum
        while True:
            rented_until = input("Unesite do kada je vozilo rentirano u formatu YYYY-MM-DD hh:mm:ss ")
            try:
                dt = datetime.strptime(rented_until, "%Y-%m-%d %H:%M:%S")
                break
            except ValueError:
                print("Pogrešan format! Primer: 2025-12-01 14:30:00")

        # Update tabele cars
        query_update = "UPDATE cars SET rented = 1, rented_until = %s WHERE id = %s"
        cursor.execute(query_update, (rented_until, car_id))
        conn.commit()
        cursor.close()
        conn.close()
        option = None
