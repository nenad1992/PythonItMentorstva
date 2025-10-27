import time
import threading

def writeHello():
    while True:
        print("Hello world")
        time.sleep(5)

threadHello = threading.Thread(target=writeHello)
threadHello.start()


print("Prosao petlju")