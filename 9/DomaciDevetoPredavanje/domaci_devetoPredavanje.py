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
    found_book = find_book_by_name(name)
    if found_book is None:
        print("Knjiga ne postoji")
    else:
        books.remove(found_book)
        print("Obrisana je knjiga")


add_book("Harry Potter 1", "J K Rowling")
add_book("Harry Potter 3", "J K Rowling")
print(books)

book = find_book_by_name("Harry Potter 1")
print(book)

delete_book_by_name("Harry Potter 1")
print(books)
