# virtualna biblioteka
# CRUD
# Dodaj knjigu
# Izlistaj knjigu
# Obrisi knjigu

books = []

def add_book(book_name, book_author):
    books.append({"name": book_name, "author": book_author})

def find_book_by_name(name):
    for book in books:
        if book['name'] == name:
            return book

def delete_book_by_name(name):
    for book in books:
        if book['name'] == name:
            del book['name']
        else:
            print("Knjiga ne postoji!")


add_book("Harry Potter 1", "J K Rowling")
add_book("Harry Potter 3", "J K Rowling")
print(books)

book = find_book_by_name("Harry Potter 1")
print(book)

delete_book_by_name("Harry Potter 1")
print(books)
