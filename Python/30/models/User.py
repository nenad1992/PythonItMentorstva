from Db import Db


class User(Db):

    def __init__(self):
        super().__init__()
        self.__age = None
        self.__name = None
        # con = super()._get_connection()
        # print(con)

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        if age < 18:
            raise ValueError("Godine moraju biti minimum 18")

        self.__age = age

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
