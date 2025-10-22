products = {
    "hleb": {
        "cena": 100,
        "kolicina": 50
    },
    "pivo": {
        "cena": 150,
        "kolicina": 220
    }
}

print(products)

# Pitatajte korisnika sta zeli da uradi:
# A: Obrise proizvode (obrisati) -> Izvrsiti logiku za brisanje
# B: Dodaj proizvod (dodaj) -> "Test"
# C: Izlistaj proizvode

print("Sta zelite da uradite? ")
print("A: Obrisi proizvod")
print("B: Dodaj proizvod")
print("C: Izlistaj proizvode")
print("D: STOP")
allowed_options = ["a", "b", "c", "stop", "istorijat", "obrisi sve", "najskuplji"]

# Napraviti novu opciju: istorija -> sve sto se desilo!
# Prikazi najskuplji proizvod

odabir = None
history = []
while odabir not in allowed_options:
    odabir = input(f"Odaberite {', '.join(allowed_options)}: \n").lower()

    if odabir == "a":
        delete_product = None
        while delete_product not in products:
            delete_product = input("Koji proizvod zelite da obrisete? \n").lower()

        del products[delete_product]
        msg = f"Obrisali ste {delete_product}"
        print(msg)
        history.append(msg)
        print(products)
        odabir = None
    elif odabir == "b":
        novi_proizvod = None
        while novi_proizvod in products or novi_proizvod is None:
            novi_proizvod = input("Unesite novi proizvod: \n")
            if novi_proizvod in products or novi_proizvod == None:
                print("Proizvod vec postoji!")

        nova_cena = None
        while nova_cena is None or nova_cena <= 0:
            nova_cena = int(input("Unesite cenu za novi proizvod: \n"))

        nova_kolicina = None
        while nova_kolicina is None or nova_kolicina < 0:
            nova_kolicina = int(input("Unesite kolicinu za novi proizvod: \n"))

        products[novi_proizvod] = {"cena": nova_cena, "kolicina": nova_kolicina}
        msg = f"Dodali ste {novi_proizvod}"
        print(msg)
        history.append(msg)
        print(products)
        odabir = None
    elif odabir == "c":
        print(products)
        odabir = None
    elif odabir == "istorijat":
        print(history)
        odabir = None
    elif odabir == "obrisi sve":
        products = {}
        odabir = None
    elif odabir == "najskuplji":
        najskuplji_proizvod_cena = 0
        najskuplji_proizvod_ime = None
        for product in products:
            if najskuplji_proizvod_cena < products[product]['cena']:
                najskuplji_proizvod_cena = products[product]['cena']
                najskuplji_proizvod_ime = product
        print(najskuplji_proizvod_cena, najskuplji_proizvod_ime)

