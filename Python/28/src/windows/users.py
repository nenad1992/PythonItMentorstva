import tkinter as tk
from src.core.database import connect_to_db

def show_users_window(window):

    user_list = tk.Listbox(window)
    user_list.pack(side="left", fill="y")

    connection = connect_to_db()
    cursor = connection.cursor()

    cursor.execute("SELECT name FROM users")

    for row in cursor.fetchall():
        user_list.insert(tk.END, row[0])