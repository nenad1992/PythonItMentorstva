def hello_world():
    print("Hello world")


hello_world()


def search(location, type):
    print(f"Predrazujemo.. {location} - {type}")

# calculate_delivery -> izracunaj dostavu
# Beograd - 500, Subotica - 1200, Novi Sad - 700
# Ako grad ne postoji, ispisati "Grad ne postoji"
def calculate_delivery(city):
    if city == "Beograd":
        print("Dostava je 500 dinara")
    elif city == "Subotica":
        print("Dostava je 1200 dinara")
    elif city == "Novi Sad":
        print("Dostava je 700 dinara")
    else:
        print("Grad ne postoji")

# ukupna_cena = cena + dostava

calculate_delivery("Beograd")