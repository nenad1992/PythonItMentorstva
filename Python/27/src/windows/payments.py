import tkinter as tk

def show_payment_window(window):
    payments = ["Toma, 500, 25.05.2025", "Marko, 120, 24.04.2025"]

    listbox = tk.Listbox(window)
    listbox.pack(side="left")

    for payment in payments:
        listbox.insert(tk.END, payment)