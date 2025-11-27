import tkinter as tk
from src.core.database import connect_to_db

def save_user(username, email, dob):
    connection = connect_to_db()
    cursor = connection.cursor()

    query = f"INSERT INTO users(email, name, dob) VALUES (%s, %s, %s)"
    cursor.execute(query, (email.get(), username.get(), dob.get()))
    connection.commit()

def show_add_user_window(window):

    tk.Label(window, text="Unesite korisnicko ime:", font=("Arial", 16)).pack()
    username_entry = tk.Entry(window, font=("Arial", 16))
    username_entry.pack()

    tk.Label(window, text="Email ime:", font=("Arial", 16)).pack()
    email_entry = tk.Entry(window, font=("Arial", 16))
    email_entry.pack()

    tk.Label(window, text="Datum rodjenja:", font=("Arial", 16)).pack()
    dob_entry = tk.Entry(window, font=("Arial", 16))
    dob_entry.pack()

    tk.Button(window,
              text="Dodaj korisnika",
              font=("Arial", 16),
              command=lambda: save_user(username_entry, email_entry, dob_entry)).pack()