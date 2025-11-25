import tkinter as tk
from src.components.navigation import show_navigation, switch_navigation_window
from src.components.body_frame import show_body_frame
from src.windows.users import show_users_window

def init():
    window = tk.Tk()
    window.geometry("1080x720")

    navigation = show_navigation(window)
    content = show_body_frame(window)

    navigation.bind("<<ListboxSelect>>", lambda event: switch_navigation_window(event, content))

    show_users_window(content)

    window.mainloop()

init()