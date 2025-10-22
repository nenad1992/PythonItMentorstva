# Svaka prodavnica ima svoje ime, svaka prodavnica ima svoje proizvode i njihove cene

shops ={
    "Maxi": {
        "Hleb": 100,
        "Novine": 50
    },
    "Idea": {
        "Hleb": 95,
        "Novine": 62
    },
    "Roda": {
        "Hleb": 97,
        "Novine": 62
    },
    "FreeShop": {
        "Novine": 62
    }
}

# Napisati petlju koja ce ispisati sve cene hleba
# Izracunati srednju cenu hleba

cena_hleba = []
for shop_name, items in shops.items():
    if "Hleb" not in items:
        continue
    cena_hleba.append(items["Hleb"])
    print(items["Hleb"])

srednja_cena = sum(cena_hleba) / len(cena_hleba)
print(cena_hleba)
print(srednja_cena)