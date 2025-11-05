import random
from faker import Faker
from datetime import datetime
from db import connection

faker = Faker()



# generate_author -> faker.name()
# generate_book_title -> ? -> ime knjige

# -> Generisi ime autora
# -> Generisi ime knjige
# -> Insertuj knjigu
# -> Insertuj autgora (usera)

# -> generate_random_dob
# -> generate_random_genre


# dob = generate_random_dob()
# genre = generate_random_genre()
# author = generate_random_author()
# book_title = generate_book_title(genre, author)
# author_id = insert_user(connection, author, dob)
# insert_book(connection, book_title, genre, author_id)

#print(dob, genre, author, book_title)

books = get_all_books(connection)
for book in books:
    print(book['name'])