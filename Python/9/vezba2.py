def search(location, type):
    print(f"Predrazujemo.. {location} - {type}")

# calculate_delivery -> izracunaj dostavu
# Beograd - 500, Subotica - 1200, Novi Sad - 700
# Ako grad ne postoji, ispisati "Grad ne postoji"
def calculate_delivery(city):
    if city == "Beograd":
        return 500
    elif city == "Subotica":
        return 1200
    elif city == "Novi Sad":
        return 700
    else:
        return -1


belgrad_delivery = calculate_delivery("Beograd")
product_price = 200
total_cart_price = belgrad_delivery + product_price
print(f"Vasa naruzbina kosta {product_price}, a dostava je {belgrad_delivery}")
print(f"Ukupno za naplatu {total_cart_price}")