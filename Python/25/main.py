import re
import tkinter as tk

window = tk.Tk() # Napravio je novi prozor (window)
window.geometry("1024x720")
window.title("Moj program")
window.configure(bg="black")

# Creating a main label
tk.Label(window,
         text="Hello how are you doing?",
         font=("Arial", 16),
         fg="dark blue",
         bg="orange"
        ).pack()

# Sign Up Button
def on_click():
    email = email_entry.get()
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

    if re.match(pattern, email) is None:
        print("Uneti email nije u dobrom formatu")

    if email == "admin@admin.com" and password_entry.get() == "123456":
        print("Dobrodosao")
    else:
        print("Pogresni kredencijali!")

tk.Button(window,
          text="Sign up!",
          font=("Arial", 16),
          bg="dark blue",
          fg="white",
          command=on_click
          ).pack(pady=15)

# Entry
password_entry = tk.Entry(window, width=50)
password_entry.pack()

#=========== Email Entry ================
email_entry = tk.Entry(window, width=50)
email_entry.pack()


window.mainloop()