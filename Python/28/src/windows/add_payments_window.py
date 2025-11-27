import tkinter as tk
from src.core.database import connect_to_db

def save_payment(user_id, amount, created_at):
    connection = connect_to_db()
    cursor = connection.cursor()

    query = f"INSERT INTO payments(user_id, amount, created_at) VALUES (%s, %s, %s)"
    cursor.execute(query, (user_id.get(), amount.get(), created_at.get()))
    connection.commit()

def show_add_payments_window(window):

    tk.Label(window, text="ID Korisnika:", font=("Arial", 16)).pack()
    user_id = tk.Entry(window, font=("Arial", 16))
    user_id.pack()

    tk.Label(window, text="Iznos:", font=("Arial", 16)).pack()
    amount = tk.Entry(window, font=("Arial", 16))
    amount.pack()

    tk.Label(window, text="Kada je izvrsena uplata:", font=("Arial", 16)).pack()
    created_at = tk.Entry(window, font=("Arial", 16))
    created_at.pack()

    tk.Button(window,
      text="Dodaj uplatu",
      font=("Arial", 16),
      command=lambda: save_payment(user_id, amount, created_at)).pack()