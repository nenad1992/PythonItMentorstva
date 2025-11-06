def insert_user(con, name, date_of_birth):
    cursor = con.cursor()
    cursor.execute("INSERT INTO users(name, dob) VALUES (%s, %s)", (name, date_of_birth))
    con.commit()
    cursor.close()
    return cursor.lastrowid