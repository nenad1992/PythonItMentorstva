# Klasa moze imati attribute (varijable), metode/ def / funkcije
# self se odnosi na taj odredjeni objekat koji je napravljen
class Person:

    def __init__(self, name, age): # kada se kreira objekat mora da se prosledi ime
        self.name = name # To ime sto je prosledjeno vezujemo za taj objekat
        self.age = age

    def write_my_name(self):
        print(self.name, self.age) # Ispisi ime i godine ovog objekta

    def say_hello(self):
        print("Hello world")

toma = Person("Toma", 31) # Napravili smo novi objekat
toma.write_my_name()
toma.say_hello()