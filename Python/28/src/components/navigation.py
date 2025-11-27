import tkinter as tk
from src.windows.users import show_users_window
from src.windows.payments import show_payment_window
from src.windows.add_user_window import show_add_user_window
from src.windows.add_payments_window import show_add_payments_window

def switch_navigation_window(event, content):
    listbox = event.widget
    selection = listbox.curselection()

    if not selection:
        return

    name = listbox.get(selection)

    for child in content.winfo_children():
        child.destroy()

    if name.lower() == "uplate":
        show_payment_window(content)
    elif name.lower() == "korisnici":
        show_users_window(content)
    elif name.lower() == "dodavanje korisnika":
        show_add_user_window(content)
    elif name.lower() == "dodavanje uplata":
        show_add_payments_window(content)

def show_navigation(window):
    nav_items = ["Uplate", "Korisnici", "Dodavanje uplata", "Dodavanje korisnika"]
    navigation = tk.Listbox(window)
    navigation.pack(side="left", fill='y', padx=5)

    for item in nav_items:
        navigation.insert(tk.END, item)

    return navigation