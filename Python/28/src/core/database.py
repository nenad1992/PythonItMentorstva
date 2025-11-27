import pymysql

def connect_to_db():
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="12345",
        db="book_keeping"
    )
    return connection