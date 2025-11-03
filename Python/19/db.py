import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="library"
)

if connection.open:
    print("Connected")
else:
    print("Failed to connect")