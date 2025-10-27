import subprocess
import webbrowser
import threading
from win10toast import ToastNotifier
import time
import random

toaster = ToastNotifier()


messages = [
    "Take a break",
    "It's time to chill",
    "Vreme je za odmor",
    "Predugo si ucio, 10 min pauze"
]

subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.2.3/bin/pycharm64.exe"])

webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open("https://itskola.net")

# Na svake 3 sekunde da se prikaze poruka/notifikacija
def show_notification():
    while True:
        toaster.show_toast("Remainder!", random.choice(messages), duration=2)
        time.sleep(3)

threadNofitication = threading.Thread(target=show_notification)
threadNofitication.start()