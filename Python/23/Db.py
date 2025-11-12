import pymysql

class Db:

    def __init__(self):
        self.__connection = pymysql.connect(
            host="localhost",
            user="root",
            password="12345",
            db="oop_2"
        )

    def _get_connection(self):
        return self.__connection

test = Db()