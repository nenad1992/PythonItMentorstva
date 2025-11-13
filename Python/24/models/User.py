from Db import Db

class User(Db):

    def __init__(self):
        super().__init__()
        con = super()._get_connection()
        #print(con)

    def set_age(self, age):
        if age < 18:
            raise ValueError("Godine moraju biti minimum 18")
        self.__age = age

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def set_name(self, name):
        if len(name) < 3:
            raise ValueError("Ime mora imati minimum 3 karaktera")
        self.__name = name
