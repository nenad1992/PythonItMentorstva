import subprocess
import webbrowser
import time
from win10toast import ToastNotifier
import random

# Otvoriti pycharm (done)
# Otvoriti chrome
# itskola.net

toaster = ToastNotifier()
#toaster.show_toast("Remainder!", "Take a break!", duration=5)


messages = [
    "Take a break",
    "It's time to chill",
    "Vreme je za odmor",
    "Predugo si ucio, 10 min pauze"
]

#subprocess.Popen(["C:/Program Files/JetBrains/PyCharm 2025.2.3/bin/pycharm64.exe"])

#webbrowser.get("C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe %s").open("https://google.com")

# Na svakih 10 sekundi da se prikaze poruka/notifikacija


while True:
    toaster.show_toast("Remainder!", random.choice(messages), duration=2)
    time.sleep(3)