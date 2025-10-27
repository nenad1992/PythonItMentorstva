# Pitaj korisnika koliko godina ima
# ako nije uneo godine pitaj opet

age = ""

while not age.isdigit() or int(age) < 18:
    age = input("Koliko godina imate? ")

print(age)