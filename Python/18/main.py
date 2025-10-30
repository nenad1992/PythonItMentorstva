import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="python17"
)

if connection.open:
    print("Connected")
else:
    print("Not connected")

cursor = connection.cursor()

cursor.execute("INSERT INTO users (username, password, age) VALUES ('Toma', '2d112d21', 35)")
connection.commit()