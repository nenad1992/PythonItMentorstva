from models.db import connection
from models.book import *
from models.user import insert_user

# Upisite broj sta zelite da uradite.

# 1. Napravi random knjigu
# 2. Prikazi knjige

choice = None
while choice is None or choice == '':
    choice = int(input("What do you want to do? \n 1. Create random book \n 2. Show books \n 3. Show book by ID \n 4. Delete a book"))

    if choice == 1:
        genre = generate_random_genre()
        author = generate_random_author()
        title = generate_book_title(genre, author)
        dob = generate_random_dob()
        user = insert_user(connection, author, dob)
        insert_book(connection, title, genre, user)
        print(f"Created new book called: {title}")
    elif choice == 2:
        books = get_all_books(connection)
        print(books)
    elif choice == 3:
        book_id = None
        while book_id is None:
            book_id = int(input("Enter book ID"))
            book = get_book_by_id(connection, book_id)
            if book:
                print(f"This book name is: {book['name']}")
            else:
                print("This book doesn't exist, try again")
                book_id = None
    elif choice == 4:
        book_id = None
        while book_id is None:
            book_id = int(input("Enter book ID"))
            delete_book_by_id(connection, book_id)
    else:
        choice = None

