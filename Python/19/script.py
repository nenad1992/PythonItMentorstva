from faker import Faker
import random
from db import connection
from datetime import datetime

faker = Faker()

# Zanr: Misterija, Avantura
# Imenice: Tajna, Zamak
# Pridevi: Zaboravljena

genres = ["Mystery", "Adventure", "Fantasy"]
adjectives = ["Dark", "Forbidden", "Mysterious", "Hidden", "Eternal"]
nouns = ["Secrets", "Kingdom", "Journey", "Love", "Shadow"]


def generate_book_title(con):
    genre = random.choice(genres)
    noun = random.choice(nouns)
    adjective = random.choice(adjectives)
    author_name = faker.name()

    book_name = f"{adjective} {noun}: A {genre} story by {author_name}"
    dob = faker.date_between(start_date=datetime(1950,1,1), end_date=datetime(2000,1,1))


def insert_user(con, name, dob):
    cursor = con.cursor()
    cursor.execute("INSERT INTO users(name, dob) VALUES (%s, %s)", (name, dob))
    con.commit()
    cursor.close()

def insert_book(con, name, genre, author):
    cursor = con.cursor()
    cursor.execute("INSERT INTO books (name, category, author) VALUES (%s, %s, %s)", (name, genre, author))
    con.commit()
    cursor.close()


insert_user(connection, "Tomislav Nikolic", "1993-05-09")
insert_book(connection, "Neka knjiga", "Nesto", "Toma")
generate_book_title(connection)