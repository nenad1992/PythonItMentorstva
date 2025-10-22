import json

# r - read
with open("data/data.json", 'r') as file:
    data = json.load(file)
    data.append({
        "name": "Petar Petrovic",
        "age": 35,
        "height": 190,
        "gender": "male"
    })

print(data)

# w - write
with open("data/data.json", 'w') as file:
    json.dump(data, file, indent=4) # dupm - upisivanje u json fajl, ident=4 - formatiranje data.json fajla