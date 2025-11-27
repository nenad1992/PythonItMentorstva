import tkinter as tk
from src.core.database import connect_to_db

def show_payment_window(window):

    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM payments")

    listbox = tk.Listbox(window)
    listbox.pack(side="left")

    for payment in cursor.fetchall():
        id, user_id, amount, create_at = payment
        listbox.insert(tk.END, f"{id}, {user_id}, {amount}, {create_at}")