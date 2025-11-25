import tkinter as tk

from pywin.scintilla.view import configManager

window = tk.Tk()
window.geometry("1024x720")
window.title("Moj program")

is_dark_mode = True

def toggle_dark_mode():
    global is_dark_mode

    if is_dark_mode:
        is_dark_mode = False
        window.configure(bg="white")
    else:
        is_dark_mode = True
        window.configure(bg="black")

tk.Button(window,
          text="Dark Mode",
          font=("Arial", 16),
          bg="orange",
          fg="white",
          command=toggle_dark_mode
          ).pack(pady=15)



window.mainloop()