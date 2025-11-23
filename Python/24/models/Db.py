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

    # Definisanje cursora
    def _get_cursor(self):
        return self.__connection.cursor()

    # Commit transakcije
    def commit(self):
        self.__connection.commit()

    # Zatvaranje konekcije sa bazom
    def close(self):
        self.__connection.close()


#test = Db()
