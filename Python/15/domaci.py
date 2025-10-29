# Pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda dodati proizvod u "kasu"
# Korisnik mora uneti 3 proizvoda ukupno

register = list()

while len(register) < 3:
    item = input("Unesite ime proizvoda: ")
    register.append(item)