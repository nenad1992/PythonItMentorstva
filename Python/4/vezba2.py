# Napisite program koji trazi od korisnika da unese ime proizvoda, a zatim ispisuje cenu tog proizvoda.
# Ako proizvod ne postoji, ispisite poruku "Prozivod nije pronadjen"

products = {
    "iphone 14": 999,
    "iphone 15": 1200,
    "samsung S23": 1200
}

search_product = input("Unesite model telefona: ")
search_product = search_product.lower()

if search_product in products:
    print(search_product + ": " + str(products[search_product]))
else:
    print("Proizvod nije pronadjen")