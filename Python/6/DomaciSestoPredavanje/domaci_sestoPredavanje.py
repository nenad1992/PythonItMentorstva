# Ispisato prodavnicu koja ima najvisu cenu hleba => Maxi

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
    },
    "Pijaca": {
        "Hleb": 99
    }
}

max_bread_price = 0
max_bread_price_shop = ""
for shop, item in shops.items():
    if "Hleb" in item:
        if max_bread_price < item["Hleb"]:
            max_bread_price = item["Hleb"]
            max_bread_price_shop = shop

print(max_bread_price, max_bread_price_shop)


