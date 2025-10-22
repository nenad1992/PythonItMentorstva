# Pitati korisnika da unese ime proizvoda
# Kada unese ime proizvoda dodati proizvod u "kasu"
# Korisnik mora uneti 3 proizvoda ukupno

kasa = []

proizvod = ""

while len(kasa) < 3:
    proizvod = input("Unesite proizvod: ")
    if proizvod.isdigit():
        continue
    kasa.append(proizvod)

print(kasa)