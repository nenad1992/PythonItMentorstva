# create_user -> ime, sifra, godine
import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="12345",
    database="python17"

)

def create_user(con, ime, sifra, godine):
    cursor = con.cursor()
    query = "INSERT INTO users (username, password, age) VALUES (%s, %s, %s)"
    cursor.execute(query, (ime, sifra, godine))
    con.commit()
    cursor.close()


create_user("Toma", "sadasdsa", 55)