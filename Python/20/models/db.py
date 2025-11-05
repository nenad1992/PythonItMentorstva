import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="library",
    cursorclass=pymysql.cursors.DictCursor # Sve rezultate koje dobijas nazad pretvori u recnik (dict)
)

if connection.open:
    print("Connected")
else:
    print("Failed to connect")