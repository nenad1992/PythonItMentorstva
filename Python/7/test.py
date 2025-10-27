books = [{'name': 'Harry Potter 1', 'author': 'J K Rowling'}, {'name': 'Harry Potter 3', 'author': 'J K Rowling'}]

for book in books:
    if book['name'] == 'Harry Potter 1':
        books.remove(book)

print(books)