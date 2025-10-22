# Vezba 1:
# Napraviti listu proizvoda i ubaciti 3 proizvoda iPhone 14, iPhone 15, Samsung S23
# Napisati proveru koja proverava da li postoji "iPhone 14" u nasoj listi proizvoda

products = ["iPhone 14", "iPhone 15", "Samsung S23"]
search_item = input("Unesite ime telefona koji trazite")
print("Korisnik je uneo " + search_item)

if search_item in products:
    print("Pronasli smo telefon")
else:
    print("Nismo pronasli trazeni proizvod")