import pymysql

# Konekcija ka bazi:
# __init__ -> konekcija SQL -> connection

class Db:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345",
            database="oop_2"
        )