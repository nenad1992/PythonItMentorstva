from ast import NodeVisitor
from cgi import print_directory

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

print("Sta zelite da uradite? ")
print("A: Obrisi proizvod")
print("B: Dodaj proizvod")

odabir = None
while odabir not in ["a", "b"]:
    odabir = input("Odaberite A ili B: ").lower()

if odabir == "a":
    delete_product = None
    while delete_product not in products:
        delete_product = input("Koji proizvod zelite da obrisete? ").lower()

    del products[delete_product]
    print(products)
elif odabir == "b":
    novi_proizvod = None
    while novi_proizvod in products or novi_proizvod == None:
        novi_proizvod = input("Unesite novi proizvod: ")
        if novi_proizvod in products or novi_proizvod == None:
            print("Proizvod vec postoji!")

    nova_cena = None
    while nova_cena == None or nova_cena <= 0:
        nova_cena = int(input("Unesite cenu za novi proizvod: "))

    nova_kolicina = None
    while nova_kolicina == None or nova_kolicina < 0:
        nova_kolicina = int(input("Unesite kolicinu za novi proizvod: "))

    products[novi_proizvod] = {"cena": nova_cena, "kolicina": nova_kolicina}

    print(products)