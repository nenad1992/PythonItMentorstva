# Korisnik treba da unese cenu korpe
# Ako je cena preko ili 1000 ispisati koliki popust su ostvarili (10%) - 1000, "Ostvarili ste 10% popusta sto iznosi 100eura"
# Ako je cena ispod 1000 ispisati "Vasa korpa iznosi 1000"

price = int(input("Unesite cenu korpe: "))

if price >= 1000:
    discount = price * 0.1
    print(f"Ostvarili ste 10% popusta sto iznosi {discount} eura")
else:
    print("Vasa korpa iznosi manje od 1000")