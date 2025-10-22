# Pitati korisnika za godine
# Ako ima 18 ili vise godina ispisati "punoletni ste"
# Ako ima manje od 18 godina ispisati "maloletni ste"

age = int(input("Koliko imate godina? "))

# Ako korisnik ima 12 ili manje godina onda ispisati "Vi ste dete"
# Ako korisnik ima od 13 do 18 godina ispisati "Vi ste tinejdzer"
# Ako korisnik ima od 18 do 64 dogina ispisati "Vi ste odrasla osoba"
# Ako korisnik ima 65 ili vise godina ispisati "Vi ste penzioner"

# Ako korisnik unese bilo sta manje od 0, ispisati gresku i zaustaviti program

if age < 0:
    print("Godine ne mogu biti manje od 0")
    quit()

if age <= 12:
    print("Vi ste dete")
elif 13 <= age < 18:
    print("Vi ste tinejdzer")
elif 18 <= age <= 64:
    print("Vi ste odrasla osoba")
elif age >= 65:
    print("Vi ste penzioner")